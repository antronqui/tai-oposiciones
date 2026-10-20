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
5. **Acceso con Google o con email + contraseña**:
   - Integración con `django-allauth`.
   - Registro abierto con **verificación de correo obligatoria**.
   - Control de acceso por lista blanca (`Invitacion`) y aprobación del administrador.
6. **Despliegue Listo en Render / PythonAnywhere**:
   - WhiteNoise para estáticos y Postgres vía `DATABASE_URL`.

---

## 🔐 Flujo de acceso

Hay dos formas de entrar y ambas pasan por la lista blanca:

| Vía | Qué ocurre |
|---|---|
| **Google** | Si el correo está autorizado entra directamente; si no, se registra la solicitud y se muestra la pantalla de espera. |
| **Email + contraseña** | Se registra en `/accounts/signup/`, recibe un correo de verificación y, una vez verificado, entra si el administrador aprobó su solicitud. |

- Si el administrador **invita antes** el correo (`/perfil/gestion-accesos/`), el usuario entra en cuanto confirma su correo, sin esperar aprobación.
- Los usuarios de Google no necesitan verificar el correo: lo garantiza el proveedor.
- Un usuario desactivado desde el panel ve una pantalla de "Acceso suspendido".

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

---

## ☁️ Despliegue en Render (producción)

### Variables de entorno

| Variable | Obligatoria | Para qué |
|---|---|---|
| `SECRET_KEY` | sí | Django |
| `DEBUG` | sí (`False`) | Producción |
| `ADMIN_EMAILS` | sí | Cuentas que se crean como superusuario, separadas por comas |
| `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` | sí (Google) | OAuth de Google |
| `DATABASE_URL` | muy recomendada | Postgres; sin ella se usa SQLite efímero |
| `EMAIL_HOST` | sí (correo) | `smtp-relay.brevo.com` |
| `EMAIL_PORT` | sí | `2525` |
| `EMAIL_USE_TLS` | sí | `True` |
| `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD` | sí | Credenciales SMTP de Brevo |
| `DEFAULT_FROM_EMAIL` | sí | Remitente verificado en Brevo |
| `SITE_NAME` / `SITE_DOMAIN` | opcional | Nombre y dominio que salen en los correos |

### Correo con Brevo (gratis, 300/día)

Render bloquea los puertos SMTP **25, 465 y 587** en el plan free, por eso se
usa el **2525** de Brevo.

1. Crear cuenta en [brevo.com](https://www.brevo.com).
2. **Senders & IP** → añadir `antronqui1@gmail.com` y confirmar el código de validación.
3. **SMTP & API → SMTP**: copiar el *login* (`xxxx@smtp-brevo.com`) y la *clave SMTP*.
4. En Render, definir `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` y
   `DEFAULT_FROM_EMAIL=TAI 2027 <antronqui1@gmail.com>`. El remitente debe ser
   exactamente el correo verificado en Brevo.

Para comprobar que el SMTP funciona (en local o desde la Shell de Render):

```bash
python manage.py test_email tu@correo.com
```

> En local, sin credenciales y con `DEBUG=True`, los correos se imprimen en la
> consola de `runserver` (backend `console`), así que el enlace de verificación
> se puede copiar sin configurar nada.

### Base de datos Postgres (Neon, gratis)

1. Crear un proyecto en [neon.tech](https://neon.tech) y copiar la cadena de
   conexión (`postgresql://...?sslmode=require`).
2. En Render, definir `DATABASE_URL` con esa cadena.

`build.sh` ejecuta `migrate`, `ensure_site` y `seed_if_empty` en cada despliegue.

**Contenido inicial:** `seed_if_empty` carga `temario/fixtures/contenido_inicial.json`
(4 bloques, 36 temas, 522 tarjetas, 10 exámenes y 1.100 preguntas) cuando la base
está vacía, y no hace nada si ya hay contenido. Así un Postgres recién creado
queda listo en el propio despliegue.

> **Importante:** sin `DATABASE_URL` la app usa `db.sqlite3`, que está
> commiteado. El disco de Render free es efímero: cada despliegue o reinicio
> restaura el fichero del repositorio y se pierden usuarios, invitaciones y
> progreso creados en producción.

### Mantener el servicio despierto (UptimeRobot)

Render free duerme el servicio a los 15 minutos sin tráfico. Un monitor de
UptimeRobot **cada 10 minutos** lo mantiene despierto (750 h/mes de plan free,
24/7 son ~730 h).

Pero conviene apuntarlo a **`/healthz/`**, no a `/`:

- `/healthz/` responde `ok` sin consultar la base de datos.
- `/` sí consulta Postgres, y Neon free tiene ~190 h de cómputo al mes. Como
  Neon suspende 5 minutos después de la última consulta, un ping cada 10 minutos
  deja la base encendida la mitad del mes (~365 h) y agota la cuota.

Con el monitor en `/healthz/` el primer acceso real del día tarda ~1 segundo más
mientras Neon despierta, y el resto va normal.

### Comprobación antes de subir

```bash
python manage.py check
python manage.py test
```

