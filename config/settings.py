"""
Django settings for config project.
Proyecto TAI 2027 - Plataforma de Preparación
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-*)i)94(g#*ak&b6%-324zhf62f@*vv*(4t&6fib@6((93ca-8f')

# Por defecto False: una variable DEBUG ausente en producción NO debe dejar el
# modo depuración activo (expone rutas, settings y variables de entorno).
# En local se activa con DEBUG=True en .env.
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'https://*.pythonanywhere.com',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
]

# Reverse Proxy SSL Header (Render / HTTPS)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'crispy_forms',
    'crispy_bootstrap5',

    # Local TAI apps
    'core',
    'accounts',
    'temario',
    'tarjetas',
    'examenes',
    'estudio',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context_processors.access_requests_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Base de datos
# En producción se usa Postgres vía DATABASE_URL (Render / Neon / Supabase).
# Sin DATABASE_URL se mantiene SQLite, útil solo para desarrollo local: el disco
# de Render free es efímero y cada despliegue restauraría el fichero del repo.
DATABASE_URL = os.getenv('DATABASE_URL', '').strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if DATABASE_URL:
    import dj_database_url

    DATABASES['default'] = dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        conn_health_checks=True,
    )

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Allauth & Invitations Configuration
# Cuentas con permisos de superadministrador (lista separada por comas).
# Con una sola basta; se admiten varias para no perder el acceso si cambias de
# cuenta de Google. Se puede sobreescribir con ADMIN_EMAILS (o el antiguo ADMIN_EMAIL).
ADMIN_EMAILS = [
    correo.strip().lower()
    for correo in os.getenv(
        'ADMIN_EMAILS',
        os.getenv('ADMIN_EMAIL', 'antronqui1@gmail.com,antronqui@gmail.com'),
    ).split(',')
    if correo.strip()
]
ADMIN_EMAIL = ADMIN_EMAILS[0]  # compatibilidad con código/plantillas antiguas

ACCOUNT_ADAPTER = 'accounts.adapter.RestrictedAccountAdapter'
SOCIALACCOUNT_ADAPTER = 'accounts.adapter.RestrictedSocialAccountAdapter'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# Login con email + contraseña (el username se genera automáticamente)
ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']
ACCOUNT_UNIQUE_EMAIL = True

# Verificación de correo obligatoria: sin confirmar el email no se puede entrar.
# Los usuarios de Google no la necesitan porque el proveedor ya verifica el correo.
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

# El botón de cerrar sesión del navbar es un POST (sin página intermedia).
ACCOUNT_LOGOUT_ON_GET = False

# Nombre y dominio que aparecen en los correos salientes
SITE_NAME = os.getenv('SITE_NAME', 'TAI 2027')
SITE_DOMAIN = os.getenv('SITE_DOMAIN', 'tai-oposiciones.onrender.com')

# Email saliente (Brevo)
# Render free bloquea los puertos SMTP 25/465/587: Brevo permite el 2525.
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp-relay.brevo.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '2525'))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '').strip()
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '').strip()
EMAIL_TIMEOUT = 10
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'TAI 2027 <antronqui1@gmail.com>')
SERVER_EMAIL = DEFAULT_FROM_EMAIL

if EMAIL_HOST_USER and EMAIL_HOST_PASSWORD:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
else:
    # Sin credenciales el correo se imprime en el log (consola) en lugar de
    # perderse: en local sirve para copiar el enlace, y en producción delata un
    # despliegue sin Brevo configurado.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Direct social login & auto-link
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True

# Socialaccount Google Provider Configuration
GOOGLE_CLIENT_ID = (
    os.getenv('GOOGLE_CLIENT_ID')
    or os.getenv('google_client_id')
    or os.getenv('SOCIAL_AUTH_GOOGLE_CLIENT_ID')
    or ''
).strip()

GOOGLE_CLIENT_SECRET = (
    os.getenv('GOOGLE_CLIENT_SECRET')
    or os.getenv('google_client_secret')
    or os.getenv('SOCIAL_AUTH_GOOGLE_SECRET')
    or ''
).strip()

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

if GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET:
    SOCIALACCOUNT_PROVIDERS['google']['APP'] = {
        'client_id': GOOGLE_CLIENT_ID,
        'secret': GOOGLE_CLIENT_SECRET,
        'key': ''
    }

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Internationalization
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_TZ = True

# Static & Media Files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
