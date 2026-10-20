from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from allauth.account.forms import LoginForm
from temario.models import Bloque, Tema
from tarjetas.models import Tarjeta
from estudio.models import ProgresoTarjeta, SesionEstudio, ProgresoPregunta
from examenes.models import Examen, PreguntaExamen


def healthz(request):
    """Latido para UptimeRobot / Render.

    No toca la base de datos a propósito: mantiene el servicio web despierto sin
    despertar el Postgres de Neon (que tiene horas de cómputo limitadas en el
    plan gratuito).
    """
    return HttpResponse('ok', content_type='text/plain; charset=utf-8')


class LandingView(TemplateView):
    template_name = "core/landing.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_bloques'] = Bloque.objects.count()
        context['total_temas'] = Tema.objects.count()
        context['total_tarjetas'] = Tarjeta.objects.count()
        context['total_preguntas'] = PreguntaExamen.objects.count()
        # La tarjeta de acceso del hero es la única superficie de login
        context['login_form'] = LoginForm()
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"

    def get(self, request, *args, **kwargs):
        # Si el usuario no ha completado el onboarding inicial, redirigir
        profile = getattr(request.user, 'profile', None)
        if profile and not profile.onboarding_completado:
            return redirect('accounts:onboarding')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        hoy = timezone.now().date()

        # Métricas generales de tarjetas
        total_tarjetas = Tarjeta.objects.filter(activa=True).count()
        progresos = ProgresoTarjeta.objects.filter(usuario=user)
        
        tarjetas_dominadas = progresos.filter(estado='dominada').count()
        tarjetas_repaso = progresos.filter(estado='repaso').count()
        tarjetas_aprendizaje = progresos.filter(estado='aprendizaje').count()
        
        # Tarjetas pendientes de revisión para hoy o retrasadas
        tarjetas_pendientes_hoy = progresos.filter(proxima_revision__lte=hoy).count()
        
        # Nuevas tarjetas que el usuario aún no ha estudiado
        tarjetas_estudiadas_ids = progresos.values_list('tarjeta_id', flat=True)
        tarjetas_nuevas = total_tarjetas - len(tarjetas_estudiadas_ids)

        # Métricas de Preguntas de Test y Circuito de Repetición de Fallos
        total_preguntas_banco = PreguntaExamen.objects.filter(anulada=False).count()
        progresos_preguntas = ProgresoPregunta.objects.filter(usuario=user)
        preguntas_falladas_pendientes = progresos_preguntas.filter(en_repaso_fallos=True).count()
        preguntas_acertadas_total = progresos_preguntas.filter(ultima_respuesta_correcta=True).count()

        # Cálculo de porcentaje de progreso global
        porcentaje_completado = 0
        if total_tarjetas > 0:
            porcentaje_completado = round(((tarjetas_dominadas + (tarjetas_repaso * 0.7) + (tarjetas_aprendizaje * 0.3)) / total_tarjetas) * 100, 1)

        # Progreso por Bloques
        bloques = Bloque.objects.all().prefetch_related('temas__tarjetas')
        bloques_stats = []
        for b in bloques:
            b_tarjetas_total = Tarjeta.objects.filter(tema__bloque=b, activa=True).count()
            b_dominadas = progresos.filter(tarjeta__tema__bloque=b, estado='dominada').count()
            b_repaso = progresos.filter(tarjeta__tema__bloque=b, estado__in=['aprendizaje', 'repaso']).count()
            b_pct = round((b_dominadas / b_tarjetas_total * 100) if b_tarjetas_total > 0 else 0, 1)
            bloques_stats.append({
                'bloque': b,
                'total': b_tarjetas_total,
                'dominadas': b_dominadas,
                'en_proceso': b_repaso,
                'porcentaje': b_pct
            })

        # Historial de últimas sesiones
        ultimas_sesiones = SesionEstudio.objects.filter(usuario=user).order_by('-fecha_inicio')[:5]

        context.update({
            'total_tarjetas': total_tarjetas,
            'tarjetas_dominadas': tarjetas_dominadas,
            'tarjetas_aprendizaje': tarjetas_aprendizaje,
            'tarjetas_repaso': tarjetas_repaso,
            'tarjetas_nuevas': max(0, tarjetas_nuevas),
            'tarjetas_pendientes_hoy': tarjetas_pendientes_hoy,
            'total_preguntas_banco': total_preguntas_banco,
            'preguntas_falladas_pendientes': preguntas_falladas_pendientes,
            'preguntas_acertadas_total': preguntas_acertadas_total,
            'porcentaje_completado': min(100.0, porcentaje_completado),
            'bloques_stats': bloques_stats,
            'ultimas_sesiones': ultimas_sesiones,
            'hoy': hoy,
        })
        return context

