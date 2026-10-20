import logging

from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailAddress
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.core.exceptions import ImmediateHttpResponse
from .models import Invitacion

logger = logging.getLogger(__name__)


def admin_emails():
    """Lista de correos con permisos de superadministrador (ADMIN_EMAILS)."""
    emails = getattr(settings, 'ADMIN_EMAILS', None)
    if emails:
        return [correo.lower().strip() for correo in emails if correo.strip()]
    return [getattr(settings, 'ADMIN_EMAIL', 'antronqui1@gmail.com').lower().strip()]


def es_admin(email):
    return (email or '').lower().strip() in admin_emails()


def admin_email_display():
    """Texto para las plantillas: los correos de administración separados por comas."""
    return ', '.join(admin_emails())


def email_autorizado(email):
    """La lista blanca: los administradores o un correo con invitación activa."""
    email = (email or '').lower().strip()
    if not email:
        return False
    if es_admin(email):
        return True
    return Invitacion.objects.filter(email__iexact=email, activo=True).exists()


class RestrictedAccountAdapter(DefaultAccountAdapter):
    """
    Alta y login tradicionales (email + contraseña) sometidos a la lista blanca.

    - El formulario de registro está abierto (`is_open_for_signup` -> True), pero
      el correo debe verificarse (ACCOUNT_EMAIL_VERIFICATION = 'mandatory').
    - El acceso no se concede hasta que el administrador aprueba la solicitud en
      el panel de Accesos (Invitacion.activo = True).
    - Si el correo ya estaba invitado de antemano, el usuario entra en cuanto
      verifica su email, sin esperar aprobación.
    """
    def is_open_for_signup(self, request):
        return True

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=commit)
        email = (user.email or '').lower().strip()
        if not email:
            return user

        if es_admin(email):
            user.is_superuser = True
            user.is_staff = True
            if commit:
                user.save(update_fields=['is_superuser', 'is_staff'])
            return user

        # Registrar la solicitud de acceso si el correo no estaba en la lista
        if not Invitacion.objects.filter(email__iexact=email).exists():
            nombre = (user.get_full_name() or user.username or '').strip()
            Invitacion.objects.create(
                email=email,
                nombre=nombre[:150],
                activo=False,
                comentario='Solicitud desde el formulario de registro',
            )
        return user

    def pre_login(self, request, user, **kwargs):
        """Bloquea el login (con una pantalla amable) si el acceso no está aprobado.

        Se dejan pasar dos casos para no romper el flujo de allauth:
        - `signup=True`: el alta acaba de crearse y aún debe enviarse el correo.
        - correo sin verificar: allauth mostrará el aviso de verificación, que es
          el paso que toca antes de hablar de aprobación.
        """
        if not user.is_active:
            return render(request, 'accounts/solicitud_pendiente.html', {
                'motivo': 'revocado',
                'icono': 'bi-slash-circle',
                'email': user.email,
                'admin_email': admin_email_display(),
            }, status=403)

        if not kwargs.get('signup') and not email_autorizado(user.email):
            if EmailAddress.objects.filter(user=user, verified=True).exists():
                return render(request, 'accounts/solicitud_pendiente.html', {
                    'motivo': 'pendiente',
                    'email': user.email,
                    'nombre': user.get_full_name() or user.username,
                    'nuevo': False,
                    'admin_email': admin_email_display(),
                })

        return super().pre_login(request, user, **kwargs)

    def send_mail(self, template_prefix, email, context):
        """Un fallo del proveedor de correo no debe romper el registro."""
        try:
            return super().send_mail(template_prefix, email, context)
        except Exception:
            logger.exception('No se pudo enviar el correo %r a %s', template_prefix, email)


class RestrictedSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Control de acceso estricto para Google OAuth:
    1. Si es una cuenta de administrador (ADMIN_EMAILS en settings):
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
        from allauth.socialaccount.models import SocialApp

        try:
            return super().get_app(request, provider, client_id=client_id)
        except (SocialApp.DoesNotExist, SocialApp.MultipleObjectsReturned):
            # Solo se capturan los fallos de configuracion de la app OAuth, no
            # cualquier error, para no ocultar problemas reales del login.
            raise ImmediateHttpResponse(
                render(request, 'accounts/solicitud_pendiente.html', {
                    'error': (
                        "Las credenciales de Google OAuth (GOOGLE_CLIENT_ID y GOOGLE_CLIENT_SECRET) "
                        "no se han detectado en el servidor o aún se están aplicando en Render. "
                        "Comprueba que ambas variables estén añadidas en Render > Environment Variables."
                    )
                })
            )

    @staticmethod
    def _email_from_sociallogin(sociallogin):
        """Devuelve el email normalizado que Google ha devuelto en este login."""
        user = getattr(sociallogin, 'user', None)
        email = ''
        if user is not None and getattr(user, 'email', ''):
            email = user.email
        elif sociallogin.account and sociallogin.account.extra_data:
            email = sociallogin.account.extra_data.get('email', '')
        return (email or '').lower().strip()

    def is_open_for_signup(self, request, sociallogin):
        """
        Solo se permite el alta social de correos que estén en la lista blanca.

        Sin este override, DefaultSocialAccountAdapter delega en el adapter de
        cuenta y allauth aborta con SignupClosedException ("Registro cerrado").
        Con él, un opositor aprobado (que aún no tiene fila en auth_user) puede
        darse de alta con Google. El resto de controles se aplican en
        pre_social_login, que es el que muestra la pantalla de solicitud.
        """
        return email_autorizado(self._email_from_sociallogin(sociallogin))

    def pre_social_login(self, request, sociallogin):
        email = self._email_from_sociallogin(sociallogin)

        if not email:
            raise ImmediateHttpResponse(
                render(request, 'accounts/solicitud_pendiente.html', {
                    'error': "No se pudo obtener una dirección de correo válida de tu cuenta de Google."
                })
            )

        # Extraer nombre si está disponible desde Google
        extra = sociallogin.account.extra_data or {}
        nombre = extra.get('name') or f"{extra.get('given_name', '')} {extra.get('family_name', '')}".strip()

        is_admin = es_admin(email)

        # Conectar con usuario existente si ya existe por email.
        # OJO: el email NO es unico en auth_user, por lo que get() puede lanzar
        # MultipleObjectsReturned (error 500). Usamos filter().first() y damos
        # prioridad al superusuario mas antiguo.
        if not sociallogin.is_existing:
            existing_user = (
                User.objects
                .filter(email__iexact=email)
                .order_by('-is_superuser', 'id')
                .first()
            )
            if existing_user is not None:
                try:
                    sociallogin.connect(request, existing_user)
                except Exception:
                    sociallogin.user = existing_user

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
                    'admin_email': admin_email_display(),
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
                    'admin_email': admin_email_display(),
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
        if es_admin(email):
            user.is_superuser = True
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = False
        return user

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        email = (user.email or '').lower().strip()
        if es_admin(email):
            user.is_superuser = True
            user.is_staff = True
            user.is_active = True
            user.save(update_fields=['is_superuser', 'is_staff', 'is_active'])
        return user
