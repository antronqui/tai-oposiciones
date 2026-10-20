"""Carga el contenido inicial solo si la base de datos está vacía.

`build.sh` lo ejecuta en cada despliegue:
- Base ya sembrada -> no hace nada.
- Base nueva (Postgres recién creado) -> carga el fixture con el temario, las
  tarjetas y los exámenes oficiales (522 tarjetas / 1.100 preguntas).
- Si el fixture no estuviera disponible -> recurre a `seed_tai_data`.
"""
from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection

from temario.models import Bloque

FIXTURE = "contenido_inicial"


class Command(BaseCommand):
    help = "Carga el contenido inicial (fixture) únicamente si no hay bloques en la base de datos."

    def handle(self, *args, **options):
        if Bloque.objects.exists():
            self.stdout.write('La base de datos ya tiene contenido: no se carga nada.')
            return

        ruta = Path(settings.BASE_DIR) / 'temario' / 'fixtures' / f'{FIXTURE}.json'
        if ruta.exists():
            self.stdout.write(self.style.NOTICE(f'Base de datos vacía: cargando {ruta.name}...'))
            call_command('loaddata', FIXTURE, verbosity=0)
            self._resetear_secuencias()
        else:
            self.stdout.write(self.style.WARNING(
                'No se encontró el fixture: usando seed_tai_data (contenido reducido).'
            ))
            call_command('seed_tai_data')

        self.stdout.write(self.style.SUCCESS(
            f'Contenido cargado: {Bloque.objects.count()} bloques.'
        ))

    def _resetear_secuencias(self):
        """loaddata inserta PKs explícitas: hay que avanzar las secuencias."""
        from django.core.management.color import no_style

        from examenes.models import Examen, PreguntaExamen
        from tarjetas.models import Tarjeta
        from temario.models import Concepto, Subtema, Tema

        modelos = [Bloque, Tema, Subtema, Concepto, Tarjeta, Examen, PreguntaExamen]
        sentencias = connection.ops.sequence_reset_sql(no_style(), modelos)
        if not sentencias:
            return
        with connection.cursor() as cursor:
            for sentencia in sentencias:
                cursor.execute(sentencia)
        self.stdout.write('Secuencias de las tablas de contenido reiniciadas.')
