from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta


class ProgresoTarjeta(models.Model):
    """
    Progreso individual de cada usuario con una tarjeta (Algoritmo SRS)
    Intervalos oficiales: 1, 3, 7, 15, 30, 60 días.
    """
    INTERVALOS_SRS = [1, 3, 7, 15, 30, 60]

    ESTADO_CHOICES = [
        ('nueva', 'Nueva'),
        ('aprendizaje', 'En Aprendizaje'),
        ('repaso', 'En Repaso'),
        ('dominada', 'Dominada'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progresos_tarjetas')
    tarjeta = models.ForeignKey('tarjetas.Tarjeta', on_delete=models.CASCADE, related_name='progresos')
    
    intervalo_actual_idx = models.PositiveIntegerField(default=0, help_text="Índice dentro de INTERVALOS_SRS")
    intervalo_dias = models.PositiveIntegerField(default=0)
    repeticiones = models.PositiveIntegerField(default=0)
    aciertos = models.PositiveIntegerField(default=0)
    fallos = models.PositiveIntegerField(default=0)
    
    ultima_revision = models.DateTimeField(null=True, blank=True)
    proxima_revision = models.DateField(default=timezone.now)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='nueva')

    class Meta:
        verbose_name = "Progreso de Tarjeta"
        verbose_name_plural = "Progresos de Tarjetas"
        unique_together = ('usuario', 'tarjeta')
        ordering = ['proxima_revision', 'tarjeta']

    def __str__(self):
        return f"{self.usuario.username} - Tarjeta #{self.tarjeta.id} ({self.get_estado_display()})"

    def registrar_respuesta(self, acertada: bool):
        """
        Aplica la regla de repetición espaciada:
        - Si acierta: avanza al siguiente intervalo (1 -> 3 -> 7 -> 15 -> 30 -> 60 días)
        - Si falla: vuelve al intervalo inicial (1 día)
        """
        now = timezone.now()
        hoy = now.date()
        self.ultima_revision = now
        self.repeticiones += 1

        if acertada:
            self.aciertos += 1
            # Obtener el intervalo correspondiente
            if self.intervalo_actual_idx < len(self.INTERVALOS_SRS):
                dias = self.INTERVALOS_SRS[self.intervalo_actual_idx]
                if self.intervalo_actual_idx + 1 < len(self.INTERVALOS_SRS):
                    self.intervalo_actual_idx += 1
                else:
                    self.estado = 'dominada'
            else:
                dias = 60
                self.estado = 'dominada'
            
            if self.estado != 'dominada':
                self.estado = 'repaso' if self.repeticiones > 2 else 'aprendizaje'
                
            self.intervalo_dias = dias
            self.proxima_revision = hoy + timedelta(days=dias)
        else:
            self.fallos += 1
            self.intervalo_actual_idx = 0
            self.intervalo_dias = 1
            self.estado = 'aprendizaje'
            self.proxima_revision = hoy + timedelta(days=1)

        self.save()


class SesionEstudio(models.Model):
    """
    Registro histórico de una sesión adaptativa de estudio
    """
    DURACIONES = [
        (15, '15 minutos (10m estudio + 5m test)'),
        (30, '30 minutos (20m estudio + 10m test)'),
        (45, '45 minutos (30m estudio + 15m test)'),
        (60, '60 minutos (40m estudio + 20m test)'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sesiones_estudio')
    duracion_minutos = models.PositiveIntegerField(choices=DURACIONES, default=15)
    
    tarjetas_estudiadas = models.PositiveIntegerField(default=0)
    preguntas_respondidas = models.PositiveIntegerField(default=0)
    aciertos_test = models.PositiveIntegerField(default=0)
    fallos_test = models.PositiveIntegerField(default=0)
    
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Sesión de Estudio"
        verbose_name_plural = "Sesiones de Estudio"
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"Sesión {self.duracion_minutos}m de {self.usuario.username} ({self.fecha_inicio.strftime('%d/%m/%Y %H:%M')})"


class ProgresoPregunta(models.Model):
    """
    Control de preguntas falladas y repetición activa para el usuario
    """
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progresos_preguntas')
    pregunta = models.ForeignKey('examenes.PreguntaExamen', on_delete=models.CASCADE, related_name='progresos_usuarios')
    
    aciertos = models.PositiveIntegerField(default=0)
    fallos = models.PositiveIntegerField(default=0)
    ultima_respuesta_correcta = models.BooleanField(default=False)
    ultima_fecha = models.DateTimeField(auto_now=True)
    en_repaso_fallos = models.BooleanField(default=False, help_text="Marcado como fallo pendiente de acertar")

    class Meta:
        verbose_name = "Progreso de Pregunta"
        verbose_name_plural = "Progresos de Preguntas"
        unique_together = ('usuario', 'pregunta')
        ordering = ['-en_repaso_fallos', '-ultima_fecha']

    def __str__(self):
        return f"{self.usuario.username} - Pregunta #{self.pregunta.id} (Fallos: {self.fallos}, Pendiente: {self.en_repaso_fallos})"
