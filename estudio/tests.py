from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Invitacion, UserProfile
from temario.models import Bloque, Tema
from tarjetas.models import Tarjeta
from estudio.models import ProgresoTarjeta, SesionEstudio
from examenes.models import Examen, PreguntaExamen
import json


class EstudioSRSTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", email="test@tai.es", password="password123")
        self.user.profile.onboarding_completado = True
        self.user.profile.save()

        self.bloque = Bloque.objects.create(numero=1, nombre="Bloque I")
        self.tema = Tema.objects.create(bloque=self.bloque, numero=1, titulo="Constitución Española")
        self.tarjeta = Tarjeta.objects.create(
            tema=self.tema,
            pregunta="¿Año Constitución?",
            respuesta="1978",
            tipo="fecha"
        )
        self.examen = Examen.objects.create(año=2024, convocatoria="libre")
        self.pregunta = PreguntaExamen.objects.create(
            examen=self.examen,
            numero=1,
            pregunta="¿Pregunta 1?",
            opcion_a="A", opcion_b="B", opcion_c="C", opcion_d="D",
            opcion_correcta="A",
            tema=self.tema
        )

    def test_srs_progreso_acierto_y_fallo(self):
        self.client.login(username="testuser", password="password123")
        
        # 1. Calificar tarjeta como "bien"
        url = reverse('estudio:api_tarjeta_progreso')
        res = self.client.post(url, data=json.dumps({
            'tarjeta_id': self.tarjeta.id,
            'calificacion': 'bien'
        }), content_type='application/json')
        
        self.assertEqual(res.status_code, 200)
        progreso = ProgresoTarjeta.objects.get(usuario=self.user, tarjeta=self.tarjeta)
        self.assertEqual(progreso.aciertos, 1)
        self.assertEqual(progreso.intervalo_dias, 1)

        # 2. Segunda respuesta acertada -> avanza a 3 días
        res = self.client.post(url, data=json.dumps({
            'tarjeta_id': self.tarjeta.id,
            'calificacion': 'bien'
        }), content_type='application/json')
        progreso.refresh_from_db()
        self.assertEqual(progreso.intervalo_dias, 3)

        # 3. Fallo -> reinicia a 1 día
        res = self.client.post(url, data=json.dumps({
            'tarjeta_id': self.tarjeta.id,
            'calificacion': 'repetir'
        }), content_type='application/json')
        progreso.refresh_from_db()
        self.assertEqual(progreso.intervalo_dias, 1)
        self.assertEqual(progreso.fallos, 1)

    def test_test_inap_finalizacion_y_puntuacion(self):
        self.client.login(username="testuser", password="password123")
        url = reverse('estudio:api_test_finalizar')
        
        # Enviar respuesta correcta (Opción A)
        res = self.client.post(url, data=json.dumps({
            'respuestas': {str(self.pregunta.id): 'A'}
        }), content_type='application/json')
        
        data = res.json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['aciertos'], 1)
        self.assertEqual(data['fallos'], 0)
        self.assertEqual(data['puntuacion_neta'], 1.0)

    def test_dashboard_access(self):
        self.client.login(username="testuser", password="password123")
        res = self.client.get(reverse('dashboard'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Bloque I")
