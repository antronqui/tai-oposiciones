from django.db import models


class Examen(models.Model):
    """
    Examen oficial recopilado de convocatorias anteriores
    """
    CONVOCATORIA_CHOICES = [
        ('libre', 'Acceso Libre'),
        ('promocion', 'Promoción Interna'),
        ('estabilizacion', 'Estabilización'),
        ('extraordinaria', 'Convocatoria Extraordinaria'),
    ]

    MODELO_CHOICES = [
        ('A', 'Modelo A'),
        ('B', 'Modelo B'),
        ('U', 'Modelo Único'),
    ]

    año = models.PositiveIntegerField(help_text="Año de la convocatoria oficial (ej: 2024, 2023...)")
    convocatoria = models.CharField(max_length=50, choices=CONVOCATORIA_CHOICES, default='libre')
    modelo = models.CharField(max_length=10, choices=MODELO_CHOICES, default='A', help_text="Variante de examen (Modelo A / Modelo B)")
    tipo = models.CharField(max_length=100, default='Primer Ejercicio TAI (Cuestionario 100 preguntas)')
    organismo = models.CharField(max_length=100, default='INAP / Comisión Permanente de Selección')
    url_oficial = models.URLField(blank=True, help_text="Enlace a la web oficial del INAP donde se publicó")
    url_plantilla = models.URLField(blank=True, help_text="Enlace a la plantilla correctora definitiva oficial")
    descripcion = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Examen Oficial"
        verbose_name_plural = "Exámenes Oficiales"
        ordering = ['-año', 'convocatoria', 'modelo']

    def __str__(self):
        return f"Examen TAI {self.año} ({self.get_convocatoria_display()} - {self.get_modelo_display()})"


class PreguntaExamen(models.Model):
    """
    Pregunta oficial de examen tipo test con plantilla verificada
    """
    OPCION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    examen = models.ForeignKey(Examen, on_delete=models.CASCADE, related_name='preguntas')
    numero = models.PositiveIntegerField(help_text="Número de orden en el examen original (ej: 1 a 100)")
    pregunta = models.TextField(help_text="Texto completo del enunciado oficial")
    opcion_a = models.TextField(help_text="Opción A")
    opcion_b = models.TextField(help_text="Opción B")
    opcion_c = models.TextField(help_text="Opción C")
    opcion_d = models.TextField(help_text="Opción D")
    opcion_correcta = models.CharField(max_length=1, choices=OPCION_CHOICES, help_text="Respuesta según plantilla oficial definitiva")
    tema = models.ForeignKey('temario.Tema', on_delete=models.SET_NULL, null=True, blank=True, related_name='preguntas_examen')
    explicacion_oficial = models.TextField(blank=True, help_text="Justificación normativa o técnica con artículo/guía aplicable")
    anulada = models.BooleanField(default=False, help_text="Marcar si fue anulada por la Comisión del INAP")

    class Meta:
        verbose_name = "Pregunta de Examen"
        verbose_name_plural = "Preguntas de Examen"
        ordering = ['examen__año', 'examen__modelo', 'numero']
        unique_together = ('examen', 'numero')

    def __str__(self):
        return f"{self.examen} - #{self.numero}: {self.pregunta[:50]}..."
