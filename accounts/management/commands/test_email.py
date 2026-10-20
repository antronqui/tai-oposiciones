"""Comprueba la configuración de correo enviando un mensaje de prueba."""
from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = (
        'Envía un correo de prueba con la configuración SMTP actual. '
        'Ejecútalo tras poner EMAIL_HOST_USER / EMAIL_HOST_PASSWORD.'
    )

    def add_arguments(self, parser):
        parser.add_argument('destinatario', help='Dirección que recibirá la prueba')

    def handle(self, *args, **options):
        destinatario = options['destinatario']
        self.stdout.write(f'Backend:  {settings.EMAIL_BACKEND}')
        self.stdout.write(f'Servidor: {settings.EMAIL_HOST}:{settings.EMAIL_PORT} '
                          f'(TLS={settings.EMAIL_USE_TLS})')
        self.stdout.write(f'Usuario:  {settings.EMAIL_HOST_USER or "(vacío)"}')
        self.stdout.write(f'Remitente: {settings.DEFAULT_FROM_EMAIL}')

        if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
            raise CommandError(
                'Faltan credenciales: define EMAIL_HOST_USER y EMAIL_HOST_PASSWORD '
                '(en local en el fichero .env; en Render, en Environment Variables). '
                'Sin ellas Django usa el backend de consola y el correo no sale.'
            )

        try:
            send_mail(
                subject='Prueba de correo - TAI 2027',
                message=(
                    'Si estás leyendo esto, el SMTP de Brevo funciona y los correos '
                    'de verificación de TAI 2027 podrán salir.'
                ),
                from_email=None,  # usa DEFAULT_FROM_EMAIL
                recipient_list=[destinatario],
                fail_silently=False,
            )
        except Exception as exc:  # noqa: BLE001
            raise CommandError(f'No se pudo enviar: {type(exc).__name__}: {exc}')

        self.stdout.write(self.style.SUCCESS(f'Correo enviado a {destinatario}. Revisa también el spam.'))
