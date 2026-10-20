"""
Tests del control de acceso: lista blanca, Google OAuth y email + contraseña.

Casos críticos:
- Un opositor aprobado sin fila en auth_user debe poder darse de alta con Google
  (si el adapter hereda `is_open_for_signup() -> False`, allauth responde
  "Registro cerrado" y nunca se crea la cuenta).
- El registro con contraseña exige verificar el correo y la aprobación del
  administrador antes de dejar entrar.
"""
import re

from django.conf import settings
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sites.models import Site
from django.core import mail
from django.core.cache import cache
from django.test import RequestFactory, TestCase, override_settings

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

    def test_las_cuentas_de_admin_reciben_superusuario(self):
        for indice, correo in enumerate(settings.ADMIN_EMAILS):
            with self.subTest(correo=correo):
                response = self._login_con_google(
                    correo, uid=f"uid-admin-{indice}", nombre="Admin"
                )

                self.assertEqual(response.status_code, 302)
                admin = User.objects.get(email=correo)
                self.assertTrue(admin.is_superuser)
                self.assertTrue(admin.is_staff)


@override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
class PasswordSignupTests(TestCase):
    PASSWORD = "ClaveSegura2027!"

    def setUp(self):
        # los limites de allauth viven en la cache y persisten entre tests
        cache.clear()
        mail.outbox = []
        self.app = SocialApp.objects.create(
            provider="google", name="Google", client_id="cid", secret="sec"
        )
        self.app.sites.add(Site.objects.get_current())

    def _registro(self, email):
        return self.client.post(
            "/accounts/signup/",
            {"email": email, "password1": self.PASSWORD, "password2": self.PASSWORD},
        )

    def _enlace_confirmacion(self):
        cuerpo = mail.outbox[-1].body
        return re.search(r"/accounts/confirm-email/[^\s]+", cuerpo).group(0)

    def _login(self, email):
        return self.client.post(
            "/accounts/login/", {"login": email, "password": self.PASSWORD}
        )

    def test_registro_crea_usuario_invitacion_pendiente_y_envia_correo(self):
        response = self._registro("nueva@gmail.com")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/accounts/confirm-email/")
        user = User.objects.get(email="nueva@gmail.com")
        self.assertTrue(user.username)
        self.assertFalse(EmailAddress.objects.get(user=user).verified)
        self.assertTrue(Invitacion.objects.filter(email="nueva@gmail.com", activo=False).exists())
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("confirma", mail.outbox[0].subject.lower())

    def test_no_puede_entrar_sin_verificar_el_correo(self):
        self._registro("nueva@gmail.com")

        response = self._login("nueva@gmail.com")

        self.assertEqual(response.status_code, 302)
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_verificado_pero_pendiente_de_aprobacion_ve_pantalla_de_espera(self):
        self._registro("nueva@gmail.com")
        self.client.get(self._enlace_confirmacion())
        self.assertTrue(EmailAddress.objects.get(email="nueva@gmail.com").verified)

        response = self._login("nueva@gmail.com")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Solicitud de Acceso Registrada", response.content.decode())
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_tras_la_aprobacion_del_admin_puede_entrar(self):
        self._registro("nueva@gmail.com")
        self.client.get(self._enlace_confirmacion())
        Invitacion.objects.filter(email="nueva@gmail.com").update(activo=True)

        response = self._login("nueva@gmail.com")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/dashboard/")
        self.assertIn("_auth_user_id", self.client.session)

    def test_invitado_de_antemano_entra_al_verificar_sin_esperar(self):
        Invitacion.objects.create(email="invitada@gmail.com", activo=True)
        self._registro("invitada@gmail.com")
        self.client.get(self._enlace_confirmacion())

        response = self._login("invitada@gmail.com")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/dashboard/")
        self.assertEqual(Invitacion.objects.filter(email="invitada@gmail.com").count(), 1)

    def test_el_admin_se_crea_como_superusuario(self):
        correo = settings.ADMIN_EMAILS[0]
        self._registro(correo)
        self.client.get(self._enlace_confirmacion())

        self._login(correo)

        admin = User.objects.get(email=correo)
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)

    def test_usuario_desactivado_ve_pantalla_de_acceso_suspendido(self):
        user = User.objects.create_user(
            username="fuera", email="fuera@gmail.com", password=self.PASSWORD, is_active=False
        )
        Invitacion.objects.create(email="fuera@gmail.com", activo=True)

        response = self._login("fuera@gmail.com")

        self.assertEqual(response.status_code, 403)
        self.assertIn("Acceso suspendido", response.content.decode())
        self.assertNotIn("_auth_user_id", self.client.session)
        self.assertFalse(User.objects.get(pk=user.pk).is_active)

    def test_recuperar_contrasena_envia_correo(self):
        User.objects.create_user(
            username="olvidadiza", email="olvido@gmail.com", password=self.PASSWORD
        )

        response = self.client.post("/accounts/password/reset/", {"email": "olvido@gmail.com"})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("contraseña", mail.outbox[0].subject.lower())

    def test_el_registro_con_un_email_ya_registrado_no_filtra_la_cuenta(self):
        User.objects.create_user(
            username="existente", email="repetido@gmail.com", password=self.PASSWORD
        )

        response = self._registro("repetido@gmail.com")

        # allauth responde igual que si se hubiera enviado la verificación
        self.assertEqual(response.status_code, 302)
        self.assertNotIn("ya existe", response.content.decode().lower())


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


class LandingYTemasTests(TestCase):
    def test_la_landing_tiene_un_unico_acceso_con_formulario(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        html = response.content.decode()
        self.assertEqual(html.count(">Acceder<"), 1)
        self.assertIn('id="acceso"', html)
        self.assertIn('name="login"', html)
        self.assertIn('name="password"', html)
        # el CTA del hero ya no es un segundo botón de login
        self.assertIn("Empezar ahora", html)
        self.assertNotIn("Entrar con Google", html)

    def test_logout_por_post_cierra_la_sesion(self):
        user = User.objects.create_user(
            username="dentro", email="dentro@gmail.com", password="ClaveSegura2027!"
        )
        self.client.force_login(user)

        response = self.client.post("/accounts/logout/")

        self.assertEqual(response.status_code, 302)
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_ensure_site_sincroniza_el_dominio(self):
        from django.contrib.sites.models import Site
        from django.core.management import call_command

        with override_settings(SITE_NAME="TAI 2027", SITE_DOMAIN="tai.example.com"):
            call_command("ensure_site")

        site = Site.objects.get(pk=1)
        self.assertEqual(site.name, "TAI 2027")
        self.assertEqual(site.domain, "tai.example.com")

    def test_seed_if_empty_respeta_una_base_ya_sembrada(self):
        from django.core.management import call_command

        from temario.models import Bloque

        Bloque.objects.create(numero=1, nombre="Bloque de prueba", descripcion="x")

        call_command("seed_if_empty", verbosity=0)

        self.assertEqual(Bloque.objects.count(), 1)

