"""Avisos de configuración para despliegues (no rompen `manage.py check`)."""
import os

from django.conf import settings
from django.core.checks import Warning, register


@register()
def produccion_check(app_configs, **kwargs):
    issues = []
    if settings.DEBUG:
        return issues

    if not getattr(settings, 'EMAIL_HOST_USER', ''):
        issues.append(Warning(
            'No hay credenciales de correo (EMAIL_HOST_USER / EMAIL_HOST_PASSWORD): '
            'los correos de verificación y de reseteo de contraseña no se enviarán.',
            hint='Configura Brevo en Render (EMAIL_HOST=smtp-relay.brevo.com, EMAIL_PORT=2525).',
            id='accounts.W001',
        ))

    if not os.getenv('DATABASE_URL', '').strip():
        issues.append(Warning(
            'No hay DATABASE_URL: se está usando db.sqlite3, que en Render free es '
            'efímero y se restaura en cada despliegue.',
            hint='Configura DATABASE_URL con un Postgres (Neon/Supabase/Render).',
            id='accounts.W002',
        ))

    return issues
