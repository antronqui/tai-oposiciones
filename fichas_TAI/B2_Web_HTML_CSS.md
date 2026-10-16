# 🌐 BLOQUE 2B — WEB: HTML5, CSS3, ACCESIBILIDAD Y SEGURIDAD WEB
> *Fichas de estudio basadas en exámenes oficiales TAI 2022, 2024 y 2025*

---

## ÍNDICE RÁPIDO
| Tema | Preguntas 2025 | Dificultad |
|------|---------------|------------|
| HTML5 — Estructura y DOCTYPE | 2-3 preguntas | ⭐⭐ |
| XML — Documentos bien formados | 1-2 preguntas | ⭐⭐ |
| CSS3 | 0-1 preguntas | ⭐ |
| Accesibilidad (WCAG / RD 1112/2018) | 2-3 preguntas | ⭐⭐ |
| Seguridad Web (XSS, OWASP) | 1-2 preguntas | ⭐⭐ |
| HTTP / REST / WSDL / WebSocket | 4-5 preguntas | ⭐⭐⭐ |
| JavaScript / ECMAScript | 1-2 preguntas | ⭐⭐ |

---

## 1. HTML5 — ESTRUCTURA BÁSICA

### 1.1 Posición del DOCTYPE — PREGUNTA CLAVE EXAMEN
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Título de la página</title>
</head>
<body>
  <header>
    <h1>Nombre del sitio</h1>
    <nav><ul><li><a href="/index.html">Inicio</a></li></ul></nav>
  </header>
  <main>
    <article><h2>Título</h2><p>Contenido...</p></article>
    <aside>Información relacionada</aside>
  </main>
  <footer>
    <p>Esta web no recopila datos</p>
  </footer>
</body>
</html>
```

> [!CAUTION]
> **TRAMPA 2025 (pregunta frecuente)**: El DOCTYPE debe estar en la **PRIMERA LÍNEA, antes del elemento raíz `<html>`** (no dentro de `<head>`, no dentro de `<html>`, no dentro de `<body>`). Respuesta: **a**.
> Según **HTML Living Standard de WHATWG**: posición = primera línea antes del `<html>`.

### 1.2 Elementos Semánticos HTML5
| Elemento | Propósito |
|---------|----------|
| `<header>` | Cabecera de página o sección |
| `<nav>` | Navegación principal |
| `<main>` | **Contenido principal** único de la página |
| `<article>` | Contenido independiente y autónomo |
| `<section>` | Sección temática del contenido |
| `<aside>` | Contenido relacionado pero secundario |
| `<footer>` | Pie de página o sección |
| `<figure>` + `<figcaption>` | Imagen con descripción |

**Para estructurar contenido principal con accesibilidad → `<main>`, `<section>`, `<header>`** (no `<div>` solo, no `<table>` para estructurar).

### 1.3 Metadatos (HEAD)
```html
<meta charset="UTF-8">
<meta name="description" content="Descripción para SEO">
<meta name="keywords" content="palabraclave1, palabraclave2">
<meta name="author" content="Autor">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Vinculación -->
<link rel="stylesheet" href="estilos.css">
<link rel="icon" href="favicon.ico" type="image/x-icon">
<link rel="preload"> <!-- Cargar recursos antes del árbol de renderizado -->
```

### 1.4 Scripts en HTML5
```html
<!-- Al final del body (mejor rendimiento) -->
<script src="script.js"></script>

<!-- Con defer: se ejecuta tras parsear el HTML -->
<script src="script.js" defer></script>

<!-- Con async: se ejecuta en cuanto se descarga -->
<script src="script.js" async></script>
```

### 1.5 HTML5 Bien Formado — Estructura Válida
✅ **Correcta:**
```html
<!DOCTYPE html><html><head><title>EducaData</title></head><body><div id="alumnos"></div></body></html>
```

❌ Sin DOCTYPE → no cumple estándar W3C  
❌ `<html version="5">` → no existe atributo version en HTML5  
❌ `<container>` → no existe este elemento  
❌ `<!HTML5>` → declaración incorrecta  

---

## 2. XML — DOCUMENTOS BIEN FORMADOS

### 2.1 Requisitos de XML Bien Formado
1. Un único **elemento raíz**
2. Todas las etiquetas deben estar **correctamente cerradas**
3. Las etiquetas de cierre deben coincidir con las de apertura (`<id_alumno>...</id_alumno>`)
4. Los atributos entre comillas
5. Los elementos deben estar correctamente **anidados** (no entrecruzados)

```xml
<!-- CORRECTO: bien formado -->
<?xml version="1.0" encoding="UTF-8"?>
<alumno>
  <id_alumno>10</id_alumno>
  <nombre>Juan Pérez</nombre>
</alumno>
```

```xml
<!-- INCORRECTO: etiqueta de cierre incorrecta -->
<alumno><id_alumno>10</nombre></alumno>  <!-- ERROR -->

<!-- INCORRECTO: sin cerrar elemento raíz -->
<alumno><id_alumno>10</id_alumno><nombre>Juan</nombre>  <!-- ERROR -->
```

### 2.2 Número de Elementos Raíz
- Un documento XML bien formado puede tener **solo UN elemento raíz**
- Cuyas etiquetas de apertura y cierre **no se encuentran dentro de ningún otro elemento**

> [!CAUTION]
> **TRAMPA 2025**: XML bien formado = **un solo elemento raíz** (no varios, no cero). Respuesta: **d**.

---

## 3. CSS3 — CONCEPTOS BÁSICOS

### 3.1 Selectores CSS
```css
/* Selector de elemento */
p { color: red; }

/* Selector de clase */
.mi-clase { font-size: 16px; }

/* Selector de ID */
#mi-id { margin: 0; }

/* Selector combinado (descendiente) */
main article { padding: 10px; }

/* Pseudoclases */
a:hover { color: blue; }
li:first-child { font-weight: bold; }
```

### 3.2 Box Model
```
┌─────────────────────────────┐
│           MARGIN            │
│  ┌───────────────────────┐  │
│  │        BORDER         │  │
│  │  ┌─────────────────┐  │  │
│  │  │    PADDING      │  │  │
│  │  │  ┌───────────┐  │  │  │
│  │  │  │  CONTENT  │  │  │  │
│  │  │  └───────────┘  │  │  │
│  │  └─────────────────┘  │  │
│  └───────────────────────┘  │
└─────────────────────────────┘
```

### 3.3 Flexbox y Grid
```css
/* Flexbox */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
}

/* Grid */
.grid {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: 16px;
}
```

---

## 4. ACCESIBILIDAD WEB

### 4.1 WCAG — 4 Principios (Mnemotecnia "POCR")
| Letra | Principio | Significado |
|-------|-----------|------------|
| **P** | **Perceptible** | La información debe ser presentable a todos los sentidos |
| **O** | **Operable** | Los componentes de interfaz deben ser operables |
| **C** | **Comprensible** | La información y operación de la UI deben ser comprensibles |
| **R** | **Robusto** | El contenido debe interpretarse por agentes de usuario actuales y futuros |

**Niveles de conformidad WCAG:**
| Nivel | Descripción |
|-------|------------|
| A | Mínimo obligatorio |
| AA | Requerido por la mayoría de legislaciones (incluido RD 1112/2018) |
| AAA | Máximo nivel |

### 4.2 RD 1112/2018 — Accesibilidad Sitios Web y Apps

**Contenido accesible incluye** (Art. 3):
- ✅ Información textual y no textual
- ✅ Documentos y formularios descargables
- ✅ Contenidos multimedia pregrabados
- ✅ Interacción bidireccional
- ✅ Cumplimentación de procesos de **identificación, autenticación, firma y pago**
- ❌ NO incluye el diseño de dispositivos físicos (teclados, pantallas, ratones)

> [!CAUTION]
> **TRAMPA 2025**: La opción correcta incluye **identificación, autenticación, firma y pago**. La opción que incluye "diseño de pantallas y teclados" es INCORRECTA. Respuesta: **b**.

### 4.3 Recomendaciones WCAG 2.1 para Accesibilidad en Aplicaciones
Para usuarios con tecnologías de asistencia (lectores de pantalla):
- ✅ Usar **etiquetas semánticas HTML5**: `<main>`, `<section>`, `<header>`, `<nav>`, `<article>`
- ❌ NO usar solo `<div>` con atributos class
- ❌ NO usar `<table>` para estructurar contenido no tabular
- ❌ NO usar solo CSS para definir estructura

> [!CAUTION]
> **TRAMPA 2025**: La respuesta correcta = usar etiquetas **semánticas** `<main>`, `<section>`, `<header>`. Respuesta: **c**.

---

## 5. SEGURIDAD WEB — OWASP

### 5.1 OWASP Top 10 (Más Frecuentes en Examen)
| Vulnerabilidad | Descripción |
|----------------|------------|
| **XSS (Cross-Site Scripting)** | Inyección de scripts maliciosos en páginas web vistas por otros usuarios |
| **SQL Injection** | Inyección de SQL malicioso en consultas |
| **CSRF** | Falsificación de peticiones en sitios cruzados |
| **Broken Authentication** | Fallos en autenticación y gestión de sesiones |
| **Sensitive Data Exposure** | Exposición de datos sensibles |

### 5.2 Prevención de XSS — OWASP
Para prevenir ataques XSS:
- ✅ **Validar y escapar correctamente** los datos antes de mostrarlos en el navegador
- ❌ Usar HTTP en lugar de HTTPS no ayuda (al contrario)
- ❌ La redundancia física no previene XSS
- ❌ La base de datos usada no previene XSS

> [!CAUTION]
> **TRAMPA 2025**: Prevención XSS = **validar y escapar datos**. Respuesta: **a**.

### 5.3 Otras Amenazas Web
| Amenaza | Descripción |
|---------|-------------|
| **Pharming** | Alteración del proceso de resolución de nombres (**fichero hosts o caché DNS**) para redirigir a página falsa aunque se escriba la dirección correcta |
| **Phishing** | Correos electrónicos que suplantan identidad para obtener credenciales |
| **Keylogger** | Programa que registra pulsaciones de teclas |
| **Vishing** | Ingeniería social telefónica |

> [!CAUTION]
> **TRAMPA 2025**: **Pharming** = alteración de DNS/hosts (no correo, no keylogger, no teléfono). Respuesta: **a**.

---

## 6. PROTOCOLOS WEB Y DE RED

### 6.1 HTTP — Métodos, Idempotencia, Seguridad
| Método | Seguro | Idempotente | Uso |
|--------|--------|-------------|-----|
| **GET** | ✅ | ✅ | Obtener recurso |
| **POST** | ❌ | ❌ | Crear recurso |
| **PUT** | ❌ | ✅ | Reemplazar recurso completo |
| **PATCH** | ❌ | ❌ | Modificar parcialmente |
| **DELETE** | ❌ | ✅ | Eliminar recurso |
| **HEAD** | ✅ | ✅ | Como GET sin cuerpo |
| **OPTIONS** | ✅ | ✅ | Opciones disponibles |

**Códigos de estado HTTP:**
```
1xx - Informacional
2xx - Éxito:
  200 OK              - Éxito general (GET, PUT)
  201 Created         - Recurso creado (POST exitoso)
  204 No Content      - Sin cuerpo (DELETE exitoso)
3xx - Redirección:
  301 Moved Permanently
  302 Found (temporal)
4xx - Error del CLIENTE:
  400 Bad Request
  401 Unauthorized
  403 Forbidden
  404 Not Found
5xx - Error del SERVIDOR:
  500 Internal Server Error
  502 Bad Gateway
  503 Service Unavailable
```

### 6.2 TLS 1.3 vs TLS 1.2
| Característica | TLS 1.2 | TLS 1.3 |
|----------------|---------|---------|
| Handshake | 2-RTT | **1-RTT** (reducción de latencia) |
| Forward Secrecy | Opcional | Obligatorio |
| Algoritmos obsoletos | Admite RC4, 3DES, etc. | Eliminados |
| Cipher suites | Muchas (algunas inseguras) | Solo las seguras |

> [!CAUTION]
> **TRAMPA 2025**: TLS 1.3 permite handshake en **1-RTT** (no más pasos, no sin certificados, no misma subred física). Respuesta: **d**.

### 6.3 DNS — Registros Frecuentes en Examen
| Registro | Función |
|---------|--------|
| **A** | Nombre → IPv4 |
| **AAAA** | Nombre → IPv6 |
| **CNAME** | Alias de otro nombre |
| **MX** | Servidor de correo |
| **NS** | Servidor de nombres |
| **PTR** | IP → Nombre (DNS inverso) |
| **TXT** | Texto libre |
| **SPF** | Autorización de servidores de correo |
| **DKIM** | **Firma digital automática** de correos del dominio |
| **DMARC** | Política de autenticación de correo (combina SPF y DKIM) |

> [!CAUTION]
> **TRAMPA 2025**: Para que los propietarios de dominios **firmen automáticamente los correos** → **DKIM** (no SPF, no DMARC, no CNAME). Respuesta: **a**.

### 6.4 Modelo OSI — Capas
| Capa | Nombre | Función principal |
|------|--------|------------------|
| 7 | **Aplicación** | Interfaz con el usuario/app |
| 6 | **Presentación** | **Cifrado, compresión, negociación de sintaxis** |
| 5 | **Sesión** | Control del diálogo entre aplicaciones |
| 4 | **Transporte** | Entrega extremo a extremo (TCP/UDP) |
| 3 | **Red** | Enrutamiento (IP) |
| 2 | **Enlace de datos** | Tramas, MAC |
| 1 | **Física** | Bits, medio físico |

> [!CAUTION]
> **TRAMPA 2025**: Cifrado y compresión = capa de **Presentación** (capa 6), no sesión ni aplicación. Respuesta: **b**.

**Subcapas de la Capa 2 (Enlace de datos) — IEEE:**
| Subcapa | Función |
|---------|---------|
| **LLC (Logical Link Control)** | **Sincronización de tramas, control de flujo y detección de errores** independientemente del medio |
| **MAC (Media Access Control)** | Control de acceso al medio físico, direccionamiento MAC |

> [!CAUTION]
> **TRAMPA 2025**: **LLC** = sincronización, control de flujo, detección de errores (NO MAC). Respuesta: **c**.

### 6.5 TCP — Three-Way Handshake
```
Cliente          Servidor
   |---SYN------->|   Paso 1: SYN
   |<---SYN+ACK---|   Paso 2: SYN + ACK  ← PREGUNTA FRECUENTE
   |---ACK------->|   Paso 3: ACK
   |   [Conectado]|
```

> [!CAUTION]
> **TRAMPA 2025**: En el **segundo paso** del handshake de TCP se activan **SYN y ACK** (no solo ACK, no SYN+FIN). Respuesta: **c**.

---

## 7. JAVASCRIPT — CONCEPTOS BÁSICOS

### 7.1 Operadores y Expresiones
```javascript
// Operador ternario
condición ? valor_si_true : valor_si_false

// Ejemplo examen 2025: a=10, b=4, c=4
// (a + b) % 2 == 0 ? c + 4 : c - 2
// (10 + 4) % 2 == 0 ? 4 + 4 : 4 - 2
// 14 % 2 == 0 ? 8 : 2
// 0 == 0 → true → 8
```

> [!CAUTION]
> **TRAMPA 2025**: El resultado es **8** (14%2=0, condición verdadera, c+4=8). Respuesta: **a**.

### 7.2 JavaScript como Lenguaje Nativo del Navegador
- **JavaScript (ECMAScript 2022)** es el único lenguaje que los navegadores Chrome, Edge y Firefox ejecutan **nativamente**
- Python, Java, Oracle SQL → No son ejecutados nativamente por el navegador

---

## 8. WINDOWS SERVER — AD Y SEGURIDAD

### 8.1 Password Settings Object (PSO)
- Permite aplicar **políticas de contraseña diferentes** a usuarios o grupos dentro del **mismo dominio**
- Es un objeto del Directorio Activo
- Soluciona la limitación de tener una sola política de contraseñas por dominio en Active Directory

> [!CAUTION]
> **TRAMPA 2025**: Para distintas políticas de contraseña en el mismo dominio → **PSO (Password Settings Object)**. Respuesta: **a**.

### 8.2 Herramienta Gestión AD — dsa.msc
| Herramienta | Descripción |
|-------------|-------------|
| **dsa.msc** (Active Directory Users and Computers) | Gestión de usuarios, grupos y equipos del dominio |
| lusrmgr.msc | Usuarios y grupos **locales** (no del dominio) |
| netplwiz | Cuentas de usuario locales (Panel Control) |
| certmgr.msc | Certificados |

### 8.3 PowerShell — Copy-Item
```powershell
# Copiar contenido de directorio de forma recursiva
Copy-Item -Path "C:\DirectorioA\*" -Destination "C:\DirectorioB" -Recurse
```

> [!CAUTION]
> **TRAMPA 2025**: `Copy-Item` (no `Copy-Path`), `-Recurse` (no `-Recursive`). Respuesta: **c**.

---

## 9. ACCESO A DATOS — PLATAFORMA DE INTERMEDIACIÓN

### 9.1 Plataforma de Intermediación de Datos (PID)
**Servicios disponibles:**
- ✅ Consulta de datos de identidad
- ✅ Consulta de datos catastrales
- ✅ Consulta de situación de prestaciones por desempleo  
- ✅ Consulta de títulos no universitarios por documentación
- ✅ Consulta de datos de residencia legal
- ❌ **Consulta de datos de patrimonio** → NO es servicio de la PID

### 9.2 RD 203/2021 — Principio de Personalización y Proactividad
Las AAPP pueden:
- ✅ **Proporcionar servicios precumplimentados**
- ✅ **Anticiparse a las posibles necesidades** del usuario
- Todo ello partiendo del conocimiento adquirido del usuario

---

## 10. RESUMEN DE PREGUNTAS WEB MÁS FRECUENTES

### Top Preguntas que SIEMPRE aparecen:

| Pregunta | Respuesta |
|---------|-----------|
| Posición del DOCTYPE en HTML5 | **Primera línea**, antes de `<html>` |
| Número de elementos raíz en XML | **Uno solo** |
| Principios WCAG | **POCR**: Perceptible, Operable, Comprensible, Robusto |
| RD 1112/2018 accesibilidad incluye | Identificación, autenticación, firma y pago ✅ |
| Prevención XSS según OWASP | **Validar y escapar** datos antes de mostrarlos |
| Pharming | Alteración de **DNS/hosts** para redirigir |
| TLS 1.3 ventaja principal | **1-RTT** (handshake más rápido) |
| TCP handshake paso 2 | **SYN + ACK** |
| Capa OSI con cifrado/compresión | Capa 6 — **Presentación** |
| LLC en capa 2 | **Sincronización, control de flujo, detección de errores** |
| DKIM | Firma automática de **correos** del dominio |
| Método HTTP idempotente pero NO seguro | **PUT** |
| HTTP 201 | Recurso **creado** (respuesta a POST) |
| Error de cliente HTTP | **4xx** |
| JavaScript nativo en navegador | Solo **JavaScript** (no Python, Java, etc.) |

---

*Última actualización: Octubre 2026 — Basado en exámenes oficiales TAI 2022, 2024, 2025*
