from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.core.exceptions import ImmediateHttpResponse
from .models import Invitacion


class RestrictedAccountAdapter(DefaultAccountAdapter):
    """
    Control de altas tradicionales.
    Desactivamos el registro abierto tradicional por formulario para asegurar
    que la autenticación se realice vía Google OAuth conforme a la política del sistema.
    """
    def is_open_for_signup(self, request):
        return False


class RestrictedSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Control de acceso estricto para Google OAuth:
    1. Si es la cuenta del Administrador (antronqui@gmail.com o ADMIN_EMAIL en settings):
       - Acceso inmediato garantizado.
       - Se le otorgan permisos totales de Superusuario y Staff automáticamente.
    2. Si es otra persona:
       - Si ya ha sido aceptada / invitada previamente (Invitacion con activo=True):
         Acceso permitido como usuario opositor estándar.
       - Si NO está en la lista o no está activa:
         Se registra automáticamente su solicitud (email, nombre) en estado pendiente (activo=False)
         y se le muestra una pantalla amigable indicando que su solicitud está en espera de aprobación
         por el administrador.
    """
    def get_app(self, request, provider, client_id=None):
        try:
            return super().get_app(request, provider, client_id=client_id)
        except Exception:
            raise ImmediateHttpResponse(
                render(request, 'accounts/solicitud_pendiente.html', {
                    'error': (
                        "Las credenciales de Google OAuth (GOOGLE_CLIENT_ID y GOOGLE_CLIENT_SECRET) "
                        "no se han detectado en el servidor o aún se están aplicando en Render. "
                        "Comprueba que ambas variables estén añadidas en Render > Environment Variables."
                    )
                })
            )
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        email = None
        if user and user.email:
            email = user.email.lower().strip()
        elif sociallogin.account.extra_data:
            email = sociallogin.account.extra_data.get('email', '').lower().strip()

        admin_email = getattr(settings, 'ADMIN_EMAIL', 'antronqui@gmail.com').lower().strip()

        if not email:
            raise ImmediateHttpResponse(
                render(request, 'accounts/solicitud_pendiente.html', {
                    'error': "No se pudo obtener una dirección de correo válida de tu cuenta de Google."
                })
            )

        # Extraer nombre si está disponible desde Google
        extra = sociallogin.account.extra_data or {}
        nombre = extra.get('name') or f"{extra.get('given_name', '')} {extra.get('family_name', '')}".strip()

        is_admin = (email == admin_email)

        # Conectar con usuario existente si ya existe por email
        if not sociallogin.is_existing:
            try:
                existing_user = User.objects.get(email__iexact=email)
                try:
                    sociallogin.connect(request, existing_user)
                except Exception:
                    sociallogin.user = existing_user
            except User.DoesNotExist:
                pass

        if is_admin:
            # Asegurar registro de invitación y permisos de superusuario
            inv, _ = Invitacion.objects.get_or_create(
                email=email,
                defaults={
                    'nombre': nombre or 'Administrador Principal',
                    'activo': True,
                    'comentario': 'Superadministrador'
                }
            )
            if not inv.activo:
                inv.activo = True
                inv.save(update_fields=['activo'])

            if sociallogin.user and sociallogin.user.pk:
                u = sociallogin.user
                u.is_superuser = True
                u.is_staff = True
                u.is_active = True
                u.save(update_fields=['is_superuser', 'is_staff', 'is_active'])
            return

        # Para otros usuarios: verificar si está en la lista de invitaciones
        invitacion = Invitacion.objects.filter(email__iexact=email).first()

        if not invitacion:
            # Nuevo intento de acceso: registrar automáticamente la solicitud
            Invitacion.objects.create(
                email=email,
                nombre=nombre,
                activo=False,
                comentario="Solicitud enviada al iniciar sesión con Google"
            )
            raise ImmediateHttpResponse(
                render(request, 'accounts/solicitud_pendiente.html', {
                    'email': email,
                    'nombre': nombre,
                    'nuevo': True,
                    'admin_email': admin_email,
                })
            )

        if not invitacion.activo:
            # Ya existe solicitud pero aún no ha sido aprobada
            if nombre and not invitacion.nombre:
                invitacion.nombre = nombre
                invitacion.save(update_fields=['nombre'])

            raise ImmediateHttpResponse(
                render(request, 'accounts/solicitud_pendiente.html', {
                    'email': email,
                    'nombre': nombre or invitacion.nombre,
                    'nuevo': False,
                    'admin_email': admin_email,
                })
            )

        # Usuario autorizado (invitacion.activo == True)
        if sociallogin.user and sociallogin.user.pk:
            u = sociallogin.user
            if not is_admin and (u.is_superuser or u.is_staff):
                u.is_superuser = False
                u.is_staff = False
                u.save(update_fields=['is_superuser', 'is_staff'])

    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        email = (user.email or data.get('email', '')).lower().strip()
        admin_email = getattr(settings, 'ADMIN_EMAIL', 'antronqui@gmail.com').lower().strip()
        if email == admin_email:
            user.is_superuser = True
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = False
        return user

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        email = (user.email or '').lower().strip()
        admin_email = getattr(settings, 'ADMIN_EMAIL', 'antronqui@gmail.com').lower().strip()
        if email == admin_email:
            user.is_superuser = True
            user.is_staff = True
            user.is_active = True
            user.save(update_fields=['is_superuser', 'is_staff', 'is_active'])
        return user
