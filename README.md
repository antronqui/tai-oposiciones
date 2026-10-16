# Plataforma Inteligente de Preparación TAI 2027 (MVP v1)

ARRANQUE:
 C:\Users\antro\antigravity> .\.venv\Scripts\python.exe manage.py runserver

Plataforma web basada en **Django** y **Bootstrap 5** para la preparación integral de las oposiciones de **Técnico Auxiliar de Informática (TAI)** de la Administración General del Estado (AGE).

---

## 🚀 Características del MVP v1

1. **Temario Oficial Normalizado**:
   - 4 Bloques Oficiales (Organización del Estado, Tecnología Básica, Desarrollo, Sistemas y Redes).
   - Trazabilidad legal a fuentes de BOE, INAP y CCN-STIC.
2. **Flashcards con Repetición Espaciada (SRS)**:
   - Principio "Una tarjeta = una idea".
   - Intervalos de consolidación en memoria: **1, 3, 7, 15, 30 y 60 días**.
   - Visor interactivo 3D con atajos de teclado y temporizador.
3. **Simulacro de Exámenes Oficiales INAP**:
   - Banco de preguntas reales con plantilla oficial definitiva y justificación de respuestas.
   - Fórmula oficial de corrección AGE: `Puntuación = Aciertos - (Errores / 3)`.
4. **Sesiones Adaptativas de Estudio**:
   - Modalidades configurables de 15, 30, 45 y 60 minutos con balance de estudio y test.
5. **Autenticación con Google y Control por Invitación**:
   - Integración con `django-allauth`.
   - Control de acceso por lista blanca en base de datos.
6. **Despliegue Listo en PythonAnywhere**:
   - Arquitectura preparada para SQLite / MySQL y WhiteNoise para archivos estáticos.

---

## 🛠️ Instalación y Uso Local

### 1. Clonar el repositorio y activar entorno
```bash
python -m venv .venv
# En Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# En Linux / macOS:
source .venv/bin/activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar migraciones y semillado inicial
```bash
python manage.py migrate
python manage.py seed_tai_data
```

> **Nota:** El comando `seed_tai_data` crea automáticamente los 4 bloques oficiales, temas clave, tarjetas flashcards, preguntas de examen del INAP y el usuario administrador (`admin` / `admin1234`).

### 4. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```

Abre [http://127.0.0.1:8000](http://127.0.0.1:8000) en tu navegador.

---

## 🌐 Despliegue en PythonAnywhere

1. Sube los archivos a tu cuenta de PythonAnywhere en `/home/<tu_usuario>/antigravity`.
2. Crea el virtualenv e instala los requisitos:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 tai-env
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py seed_tai_data
   python manage.py collectstatic --noinput
   ```
3. En la pestaña **Web** de PythonAnywhere:
   - Configura el archivo **WSGI** copiando el contenido de [wsgi_pythonanywhere.py](file:///C:/Users/antro/antigravity/wsgi_pythonanywhere.py).
   - Define el Virtualenv: `/home/<tu_usuario>/.virtualenvs/tai-env`.
4. Recarga la aplicación web.
