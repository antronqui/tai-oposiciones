from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Invitacion(models.Model):
    """
    Tabla de control de acceso por lista blanca (Principio de acceso restringido)
    """
    email = models.EmailField(unique=True, help_text="Correo autorizado para iniciar sesión con Google")
    nombre = models.CharField(max_length=150, blank=True, help_text="Nombre de la cuenta o nota")
    activo = models.BooleanField(default=True, help_text="Si está activo, el usuario tiene permiso para entrar")
    fecha_alta = models.DateTimeField(auto_now_add=True)
    comentario = models.CharField(max_length=200, blank=True, help_text="Nota interna del usuario o motivo de solicitud")

    class Meta:
        verbose_name = "Invitación / Acceso"
        verbose_name_plural = "Invitaciones y Accesos"
        ordering = ['-fecha_alta']

    def __str__(self):
        estado = "Autorizado" if self.activo else "Pendiente"
        return f"{self.email} ({estado})"


class UserProfile(models.Model):
    """
    Perfil de opositor y configuración del plan de estudio
    """
    NIVEL_CHOICES = [
        ('ninguno', 'Ninguno (Desde cero)'),
        ('basico', 'Básico (Conocimientos iniciales)'),
        ('medio', 'Medio (Repasando temario)'),
        ('alto', 'Alto (Nivel avanzado / consolidación)'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    horas_semanales = models.PositiveIntegerField(default=10, help_text="Horas dedicadas por semana")
    nivel_previo = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='ninguno')
    fecha_objetivo = models.DateField(null=True, blank=True, help_text="Fecha estimada de la convocatoria o examen")
    onboarding_completado = models.BooleanField(default=False)
    fecha_alta = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"

    def __str__(self):
        return f"Perfil de {self.user.username} - {self.horas_semanales}h/sem"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()
