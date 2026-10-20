from django.test import TestCase


class HealthzTests(TestCase):
    def test_healthz_responde_sin_tocar_la_base_de_datos(self):
        """UptimeRobot lo llama cada pocos minutos: no debe despertar Postgres."""
        with self.assertNumQueries(0):
            response = self.client.get('/healthz/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'ok')
