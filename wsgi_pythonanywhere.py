"""
Configuración WSGI para PythonAnywhere
======================================
Guía rápida de configuración en la pestaña 'Web' de PythonAnywhere:

1. Código fuente y directorio de trabajo:
   - Source code:      /home/<tu_usuario>/antigravity
   - Working directory:/home/<tu_usuario>/antigravity

2. Entorno virtual:
   - Virtualenv:       /home/<tu_usuario>/.virtualenvs/tai-env

3. Archivos estáticos (Static Files):
   - URL: /static/     Directory: /home/<tu_usuario>/antigravity/staticfiles
   - URL: /media/      Directory: /home/<tu_usuario>/antigravity/media

4. Archivo WSGI (Code -> WSGI configuration file):
   Pega este código reemplazando '<tu_usuario>' por tu nombre de usuario en PythonAnywhere:
"""

import os
import sys
from pathlib import Path

# Cambia '<tu_usuario>' por tu nombre de usuario real en PythonAnywhere
USUARIO_PYTHONANYWHERE = '<tu_usuario>'

project_home = f'/home/{USUARIO_PYTHONANYWHERE}/antigravity'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Configurar variables de entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ['DEBUG'] = 'False'

# Cargar variables de .env si existe
env_path = Path(project_home) / '.env'
if env_path.exists():
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=env_path)

# Cargar aplicación WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
