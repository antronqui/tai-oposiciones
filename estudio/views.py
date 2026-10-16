import json
import random
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from tarjetas.models import Tarjeta
from examenes.models import PreguntaExamen, Examen
from temario.models import Bloque, Tema
from .models import ProgresoTarjeta, SesionEstudio, ProgresoPregunta


class SeleccionarSesionView(LoginRequiredMixin, TemplateView):
    """
    Pantalla de selección de tiempo y tipo de sesión adaptativa
    """
    template_name = "estudio/seleccionar_sesion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now().date()
        user = self.request.user
        
        # Tarjetas pendientes de repaso hoy
        context['tarjetas_pendientes'] = ProgresoTarjeta.objects.filter(
            usuario=user,
            proxima_revision__lte=hoy
        ).count()
        context['bloques'] = Bloque.objects.all()
        return context


class IniciarSesionView(LoginRequiredMixin, View):
    """
    Inicia y prepara una nueva sesión de estudio adaptativa
    """
    def get(self, request, *args, **kwargs):
        duracion = int(request.GET.get('duracion', 15))
        bloque_id = request.GET.get('bloque', None)
        modo = request.GET.get('modo', 'mixto') # mixto, flashcards, test
        
        sesion = SesionEstudio.objects.create(
            usuario=request.user,
            duracion_minutos=duracion
        )
        request.session['sesion_estudio_id'] = sesion.id
        request.session['sesion_bloque_id'] = bloque_id
        request.session['sesion_modo'] = modo
        
        if modo == 'test':
            return redirect('estudio:test_examen')
        return redirect('estudio:sesion_flashcards')


class SesionFlashcardsView(LoginRequiredMixin, TemplateView):
    """
    Interfaz interactiva de estudio con Flashcards y repetición espaciada
    """
    template_name = "estudio/sesion_flashcards.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        hoy = timezone.now().date()
        bloque_id = self.request.session.get('sesion_bloque_id')
        sesion_id = self.request.session.get('sesion_estudio_id')
        
        sesion = None
        if sesion_id:
            sesion = SesionEstudio.objects.filter(id=sesion_id, usuario=user).first()

        # Filtrar tarjetas disponibles
        tarjetas_qs = Tarjeta.objects.filter(activa=True)
        if bloque_id and bloque_id.isdigit():
            tarjetas_qs = tarjetas_qs.filter(tema__bloque_id=int(bloque_id))

        # 1. Tarjetas vencidas o pendientes de repaso para hoy
        progresos_pendientes = ProgresoTarjeta.objects.filter(
            usuario=user,
            tarjeta__in=tarjetas_qs,
            proxima_revision__lte=hoy
        ).select_related('tarjeta', 'tarjeta__tema', 'tarjeta__tema__bloque')

        tarjetas_repaso = [p.tarjeta for p in progresos_pendientes]

        # 2. Tarjetas nuevas (no vistas por el usuario)
        tarjetas_vistas_ids = ProgresoTarjeta.objects.filter(
            usuario=user
        ).values_list('tarjeta_id', flat=True)

        tarjetas_nuevas = list(tarjetas_qs.exclude(id__in=tarjetas_vistas_ids).select_related('tema', 'tema__bloque')[:15])

        # Combinar: prioridad a repasos, luego nuevas
        cola_tarjetas = tarjetas_repaso + tarjetas_nuevas
        if not cola_tarjetas:
            # Si no hay pendientes ni nuevas, repasar tarjetas aleatorias
            cola_tarjetas = list(tarjetas_qs.order_by('?')[:10])

        context['tarjetas_json'] = json.dumps([
            {
                'id': t.id,
                'bloque': f"Bloque {t.tema.bloque.numero}",
                'tema': f"Tema {t.tema.numero}: {t.tema.titulo}",
                'tipo': t.get_tipo_display(),
                'tipo_raw': t.tipo,
                'pregunta': t.pregunta,
                'respuesta': t.respuesta,
                'explicacion': t.explicacion,
                'fuente': t.fuente,
                'url_fuente': t.url_fuente or t.tema.url_oficial,
                'dificultad': t.get_nivel_dificultad_display(),
            } for t in cola_tarjetas
        ])
        context['total_cola'] = len(cola_tarjetas)
        context['sesion'] = sesion
        return context


class RegistrarProgresoTarjetaAPI(LoginRequiredMixin, View):
    """
    Endpoint AJAX para actualizar el algoritmo SRS al calificar una tarjeta
    """
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            tarjeta_id = data.get('tarjeta_id')
            calificacion = data.get('calificacion') # 'repetir', 'dificil', 'bien', 'facil'
            sesion_id = request.session.get('sesion_estudio_id')
            
            tarjeta = get_object_or_404(Tarjeta, id=tarjeta_id)
            progreso, created = ProgresoTarjeta.objects.get_or_create(
                usuario=request.user,
                tarjeta=tarjeta
            )

            acertada = calificacion in ['bien', 'facil']
            progreso.registrar_respuesta(acertada=acertada)

            # Si fue calificada como 'facil', avanzamos un nivel extra
            if calificacion == 'facil' and progreso.intervalo_actual_idx + 1 < len(ProgresoTarjeta.INTERVALOS_SRS):
                progreso.intervalo_actual_idx += 1
                progreso.intervalo_dias = ProgresoTarjeta.INTERVALOS_SRS[progreso.intervalo_actual_idx]
                progreso.proxima_revision = timezone.now().date() + timedelta(days=progreso.intervalo_dias)
                progreso.save()

            # Actualizar métricas de la sesión activa
            if sesion_id:
                sesion = SesionEstudio.objects.filter(id=sesion_id, usuario=request.user).first()
                if sesion:
                    sesion.tarjetas_estudiadas += 1
                    sesion.save()

            return JsonResponse({
                'status': 'ok',
                'nuevo_intervalo_dias': progreso.intervalo_dias,
                'proxima_revision': progreso.proxima_revision.strftime('%d/%m/%Y'),
                'estado': progreso.get_estado_display(),
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


class TestAdaptativoView(LoginRequiredMixin, TemplateView):
    """
    Simulador de test con preguntas oficiales del INAP y circuito de repetición de fallos
    """
    template_name = "estudio/test_examen.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        examen_id = self.request.GET.get('examen') or self.request.session.get('sesion_examen_id')
        bloque_id = self.request.GET.get('bloque') or self.request.session.get('sesion_bloque_id')
        tema_id = self.request.GET.get('tema')
        modo = self.request.GET.get('modo') # 'falladas', etc.
        limite = self.request.GET.get('limite', '')

        preguntas_qs = PreguntaExamen.objects.filter(anulada=False).select_related('tema', 'tema__bloque', 'examen')
        
        titulo_test = "Simulacro Adaptativo TAI"
        subtitulo_test = "Preguntas extraídas del banco oficial de exámenes INAP"

        # Modo 1: Exclusivo preguntas falladas pendientes de repasar
        if modo == 'falladas':
            fallos_qs = ProgresoPregunta.objects.filter(
                usuario=user,
                en_repaso_fallos=True,
                pregunta__anulada=False
            ).select_related('pregunta', 'pregunta__tema', 'pregunta__tema__bloque', 'pregunta__examen')
            
            if tema_id and str(tema_id).isdigit():
                tema = get_object_or_404(Tema, id=int(tema_id))
                fallos_qs = fallos_qs.filter(pregunta__tema=tema)
                titulo_test = f"Repaso de Fallos: Tema {tema.numero} ({tema.titulo})"
                subtitulo_test = f"Preguntas que has fallado previamente en el Tema {tema.numero}"
            elif bloque_id and str(bloque_id).isdigit():
                bloque = get_object_or_404(Bloque, id=int(bloque_id))
                fallos_qs = fallos_qs.filter(pregunta__tema__bloque=bloque)
                titulo_test = f"Repaso de Fallos: Bloque {bloque.numero} ({bloque.nombre})"
                subtitulo_test = f"Preguntas falladas en el Bloque {bloque.numero}"
            else:
                titulo_test = "Repaso General de Preguntas Falladas"
                subtitulo_test = "Preguntas de todo el temario pendientes de afianzar"

            preguntas = [f.pregunta for f in fallos_qs]

        # Modo 2: Test de un Tema específico (con desarrollo y preguntas directas)
        elif tema_id and str(tema_id).isdigit():
            tema = get_object_or_404(Tema, id=int(tema_id))
            qs_tema = list(preguntas_qs.filter(tema=tema))
            
            # Priorizar las falladas por el usuario al inicio
            falladas_ids = set(ProgresoPregunta.objects.filter(
                usuario=user,
                pregunta__tema=tema,
                en_repaso_fallos=True
            ).values_list('pregunta_id', flat=True))
            
            preguntas_falladas = [p for p in qs_tema if p.id in falladas_ids]
            preguntas_otras = [p for p in qs_tema if p.id not in falladas_ids]
            random.shuffle(preguntas_otras)
            
            preguntas = preguntas_falladas + preguntas_otras
            if limite.isdigit():
                preguntas = preguntas[:int(limite)]
                
            titulo_test = f"Test de Evaluación: Tema {tema.numero}"
            subtitulo_test = f"{tema.titulo} · Bloque {tema.bloque.numero} ({tema.bloque.nombre})"

        # Modo 3: Test de un Examen Oficial específico
        elif examen_id and str(examen_id).isdigit():
            examen = get_object_or_404(Examen, id=int(examen_id))
            preguntas_qs = preguntas_qs.filter(examen=examen).order_by('numero')
            titulo_test = f"{examen.tipo} - {examen.get_modelo_display()}"
            subtitulo_test = f"Convocatoria Oficial {examen.año} ({examen.get_convocatoria_display()}) · Organismo: {examen.organismo}"
            preguntas = list(preguntas_qs)

        # Modo 4: Test de un Bloque
        elif bloque_id and str(bloque_id).isdigit():
            bloque = get_object_or_404(Bloque, id=int(bloque_id))
            preguntas_qs = preguntas_qs.filter(tema__bloque=bloque).order_by('?')
            titulo_test = f"Test Específico: Bloque {bloque.numero} ({bloque.nombre})"
            subtitulo_test = "Preguntas oficiales vinculadas a este bloque temático"
            num_preguntas = int(limite) if limite.isdigit() else 20
            preguntas = list(preguntas_qs[:num_preguntas])

        # Modo 5: Test general aleatorio
        else:
            num_preguntas = int(limite) if limite.isdigit() else 20
            preguntas = list(preguntas_qs.order_by('?')[:num_preguntas])

        context['preguntas'] = preguntas
        context['total_preguntas'] = len(preguntas)
        context['titulo_test'] = titulo_test
        context['subtitulo_test'] = subtitulo_test
        context['tema_id'] = tema_id
        return context


class FinalizarTestAPI(LoginRequiredMixin, View):
    """
    Valida las respuestas del test, calcula nota oficial, guarda sesión y actualiza el circuito de fallos
    Fórmula oficial TAI: Puntuación = Aciertos - (Errores / 3)
    """
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            respuestas = data.get('respuestas', {}) # {pregunta_id: 'A'}
            sesion_id = request.session.get('sesion_estudio_id')
            user = request.user
            
            aciertos = 0
            fallos = 0
            en_blanco = 0
            detalles = []
            recuperadas_count = 0

            for p_id_str, opcion_seleccionada in respuestas.items():
                pregunta = get_object_or_404(PreguntaExamen, id=int(p_id_str))
                es_correcta = (opcion_seleccionada == pregunta.opcion_correcta)
                
                # Actualizar progreso individual de la pregunta para el usuario
                progreso_p, _ = ProgresoPregunta.objects.get_or_create(
                    usuario=user,
                    pregunta=pregunta
                )
                
                if not opcion_seleccionada:
                    en_blanco += 1
                elif es_correcta:
                    aciertos += 1
                    progreso_p.aciertos += 1
                    progreso_p.ultima_respuesta_correcta = True
                    if progreso_p.en_repaso_fallos:
                        recuperadas_count += 1
                        progreso_p.en_repaso_fallos = False # Fallo superado
                else:
                    fallos += 1
                    progreso_p.fallos += 1
                    progreso_p.ultima_respuesta_correcta = False
                    progreso_p.en_repaso_fallos = True # Marcada para repreguntar
                
                progreso_p.save()

                detalles.append({
                    'id': pregunta.id,
                    'pregunta': pregunta.pregunta,
                    'seleccionada': opcion_seleccionada,
                    'correcta': pregunta.opcion_correcta,
                    'es_correcta': es_correcta,
                    'explicacion': pregunta.explicacion_oficial,
                    'tema': f"B{pregunta.tema.bloque.numero}T{pregunta.tema.numero} {pregunta.tema.titulo}" if pregunta.tema else "General TAI"
                })

            total_respondidas = aciertos + fallos
            # Puntuación neta tipo oposición AGE: Aciertos - (Fallos / 3)
            puntuacion_neta = max(0.0, round(aciertos - (fallos / 3.0), 2))
            porcentaje_acierto = round((aciertos / len(detalles) * 100), 1) if detalles else 0

            # Guardar en la sesión
            if sesion_id:
                sesion = SesionEstudio.objects.filter(id=sesion_id, usuario=user).first()
                if sesion:
                    sesion.preguntas_respondidas += len(detalles)
                    sesion.aciertos_test += aciertos
                    sesion.fallos_test += fallos
                    sesion.completada = True
                    sesion.save()

            return JsonResponse({
                'status': 'ok',
                'aciertos': aciertos,
                'fallos': fallos,
                'en_blanco': en_blanco,
                'recuperadas': recuperadas_count,
                'puntuacion_neta': puntuacion_neta,
                'porcentaje': porcentaje_acierto,
                'detalles': detalles
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
