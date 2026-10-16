from django.db import models


class Tarjeta(models.Model):
    """
    Tarjeta de estudio (Flashcard) - Principio 'Una tarjeta = una idea'
    """
    TIPO_CHOICES = [
        ('definicion', 'Definición'),
        ('fecha', 'Fecha clave'),
        ('organismo', 'Organismo / Entidad'),
        ('procedimiento', 'Procedimiento / Fases'),
        ('comparativa', 'Comparativa / Diferencias'),
    ]

    DIFICULTAD_CHOICES = [
        ('facil', 'Fácil'),
        ('media', 'Media'),
        ('dificil', 'Difícil'),
    ]

    tema = models.ForeignKey('temario.Tema', on_delete=models.CASCADE, related_name='tarjetas')
    subtema = models.ForeignKey('temario.Subtema', on_delete=models.SET_NULL, null=True, blank=True, related_name='tarjetas')
    concepto = models.ForeignKey('temario.Concepto', on_delete=models.SET_NULL, null=True, blank=True, related_name='tarjetas')
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='definicion')
    pregunta = models.TextField(help_text="Enunciado o pregunta de la tarjeta (Anverso)")
    respuesta = models.TextField(help_text="Respuesta concisa y directa (Reverso)")
    explicacion = models.TextField(blank=True, help_text="Contexto adicional o razonamiento")
    imagen = models.ImageField(upload_to='tarjetas/', null=True, blank=True, help_text="Esquema o apoyo visual opcional")
    
    nivel_dificultad = models.CharField(max_length=10, choices=DIFICULTAD_CHOICES, default='media')
    fuente = models.CharField(max_length=255, default='BOE / INAP', help_text="Fuente oficial de la norma/manual")
    url_fuente = models.URLField(blank=True, help_text="Enlace a la fuente de verificación")
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Tarjeta"
        verbose_name_plural = "Tarjetas"
        ordering = ['tema', 'tipo', 'id']

    def __str__(self):
        return f"[{self.get_tipo_display()}] {self.pregunta[:60]}..."
