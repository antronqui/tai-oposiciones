from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions import PermissionDenied
from .models import Invitacion


class RestrictedAccountAdapter(DefaultAccountAdapter):
    """
    Control de altas tradicionales
    """
    def is_open_for_signup(self, request):
        return True


class RestrictedSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Control de acceso estricto por lista de invitaciones para Google Login
    """
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        email = None
        if user and user.email:
            email = user.email.lower().strip()
        elif sociallogin.account.extra_data:
            email = sociallogin.account.extra_data.get('email', '').lower().strip()

        if not email:
            raise PermissionDenied("No se pudo obtener una dirección de correo válida de Google.")

        # Verificar si está en la tabla de invitaciones activas o es superusuario
        invitado = Invitacion.objects.filter(email__iexact=email, activo=True).exists()
        
        # Permitir si está invitado o si ya existe como superusuario / staff en el sistema
        if not invitado and not (user.id and (user.is_superuser or user.is_staff)):
            raise PermissionDenied(
                f"El correo '{email}' no cuenta con una invitación activa para acceder a la plataforma TAI."
            )
