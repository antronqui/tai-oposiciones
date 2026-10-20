"""
Tests del control de acceso por lista blanca y del alta vía Google OAuth.

El caso crítico: un opositor recién aprobado todavía no tiene fila en
auth_user, por lo que allauth debe crear su cuenta en ese momento. Si el
adapter social hereda `is_open_for_signup() -> False` (registro tradicional
cerrado), allauth aborta con SignupClosedException y el usuario ve la página
"Registro cerrado" en lugar de entrar.
"""
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sites.models import Site
from django.test import RequestFactory, TestCase

from allauth.account.models import EmailAddress
from allauth.core.context import request_context
from allauth.socialaccount.internal.flows.login import complete_login
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialLogin
from allauth.socialaccount.providers.google.provider import GoogleProvider

from .models import Invitacion, UserProfile


class GoogleLoginTests(TestCase):
    def setUp(self):
        self.app = SocialApp.objects.create(
            provider="google", name="Google", client_id="cid", secret="sec"
        )
        self.app.sites.add(Site.objects.get_current())

    def _login_con_google(self, email, uid="uid-1", nombre="Opositor", verificado=True):
        request = RequestFactory().get("/accounts/google/login/callback/")
        request.user = AnonymousUser()
        request.session = SessionStore()
        setattr(request, "_messages", FallbackStorage(request))
        sociallogin = SocialLogin(
            account=SocialAccount(
                provider="google",
                uid=uid,
                extra_data={"email": email, "name": nombre, "verified_email": verificado},
            ),
            user=User(email=email, first_name=nombre),
            email_addresses=[EmailAddress(email=email, verified=verificado, primary=True)],
            provider=GoogleProvider(request=request, app=self.app),
        )
        with request_context(request):
            return complete_login(request, sociallogin)

    def test_usuario_aprobado_puede_entrar_con_google(self):
        """Regresión: el alta social no debe quedar bloqueada por el registro cerrado."""
        Invitacion.objects.create(email="aprobado@gmail.com", nombre="Aprobado", activo=True)

        response = self._login_con_google("aprobado@gmail.com")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/dashboard/")
        user = User.objects.get(email="aprobado@gmail.com")
        self.assertTrue(UserProfile.objects.filter(user=user).exists())
        self.assertTrue(SocialAccount.objects.filter(uid="uid-1", user=user).exists())
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_segundo_login_no_duplica_la_cuenta(self):
        Invitacion.objects.create(email="aprobado@gmail.com", activo=True)
        self._login_con_google("aprobado@gmail.com")

        response = self._login_con_google("aprobado@gmail.com")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.filter(email="aprobado@gmail.com").count(), 1)

    def test_usuario_sin_invitacion_ve_pantalla_de_solicitud(self):
        response = self._login_con_google("desconocido@gmail.com", uid="uid-2")
        contenido = response.content.decode()

        self.assertIn("Solicitud de Acceso Registrada", contenido)
        self.assertNotIn("Registro cerrado", contenido)
        self.assertTrue(
            Invitacion.objects.filter(email="desconocido@gmail.com", activo=False).exists()
        )
        self.assertFalse(User.objects.filter(email="desconocido@gmail.com").exists())

    def test_invitacion_pendiente_no_abre_el_registro_social(self):
        Invitacion.objects.create(email="pendiente@gmail.com", activo=False)
        response = self._login_con_google("pendiente@gmail.com", uid="uid-3")

        self.assertIn("Solicitud de Acceso Registrada", response.content.decode())
        self.assertFalse(User.objects.filter(email="pendiente@gmail.com").exists())

    def test_email_duplicado_no_provoca_error_500(self):
        """auth_user.email no es único: no debe lanzar MultipleObjectsReturned.

        Se usa un email no verificado para que allauth no auto-conecte por
        email y sea el adapter quien busque al usuario existente.
        """
        User.objects.create(username="dup1", email="dup@gmail.com")
        User.objects.create(username="dup2", email="dup@gmail.com")
        Invitacion.objects.create(email="dup@gmail.com", activo=True)

        response = self._login_con_google("dup@gmail.com", uid="uid-4", verificado=False)

        self.assertEqual(response.status_code, 302)

    def test_admin_recibe_permisos_de_superusuario(self):
        response = self._login_con_google("antronqui@gmail.com", uid="uid-admin", nombre="Admin")

        self.assertEqual(response.status_code, 302)
        admin = User.objects.get(email="antronqui@gmail.com")
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)


class AprobarAccesoViewTests(TestCase):
    def test_aprobar_activa_la_invitacion_y_reactiva_al_usuario(self):
        gestor = User.objects.create_user(
            username="gestor", email="gestor@gmail.com", password="x", is_staff=True
        )
        user = User.objects.create_user(
            username="opositor", email="opositor@gmail.com", password="x", is_active=False
        )
        invitacion = Invitacion.objects.create(email="opositor@gmail.com", activo=False)
        self.client.force_login(gestor)

        response = self.client.post(f"/perfil/gestion-accesos/aprobar/{invitacion.pk}/")

        self.assertRedirects(response, "/perfil/gestion-accesos/")
        invitacion.refresh_from_db()
        user.refresh_from_db()
        self.assertTrue(invitacion.activo)
        self.assertTrue(user.is_active)
