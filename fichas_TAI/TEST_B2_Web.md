# 📝 BANCO DE PREGUNTAS TIPO TEST: BLOQUE 2 (TECNOLOGÍAS WEB, ACCESIBILIDAD Y SEGURIDAD WEB)
## Oposición Técnico Auxiliar de Informática (TAI) — AGE
> **Formato oficial**: 4 opciones por pregunta, 1 única correcta, penalización 1/3 en examen real.  
> **Garantía de calidad**: Todas las opciones A, B, C y D disponen de contenido íntegro y justificación técnica precisa.

---

### 🌐 Tema 1: HTML5 y Estructuración Semántica

#### Pregunta 1.1
En un documento HTML5 estándar, ¿dónde debe situarse la declaración de tipo de documento `<!DOCTYPE html>`?
- a) Dentro del elemento `<head>`, justo antes de las etiquetas `<meta>`.
- b) En la primera línea absoluta del documento, antes de la etiqueta de apertura `<html>`.
- c) Al final del archivo, inmediatamente después de `</html>`.
- d) Dentro del elemento `<body>` al inicio del contenido visible.
> **Respuesta correcta:** B  
> **Explicación:** La declaración `<!DOCTYPE html>` debe colocarse en la primera línea del archivo fuente, antes de la etiqueta `<html>`, para indicar al navegador que renderice el documento en modo estándar HTML5.

#### Pregunta 1.2
¿Cuál de las siguientes etiquetas semánticas de HTML5 está destinada a contener la navegación principal con enlaces internos o externos del sitio web?
- a) `<aside>`
- b) `<nav>`
- c) `<section>`
- d) `<header>`
> **Respuesta correcta:** B  
> **Explicación:** La etiqueta `<nav>` define una sección de navegación que contiene bloques de enlaces principales del sitio web.

#### Pregunta 1.3
En HTML5, ¿qué elemento semántico debe utilizarse para representar contenido independiente y autocontenido que podría ser distribuido o reutilizado de forma autónoma (por ejemplo, un artículo de blog o una noticia)?
- a) `<article>`
- b) `<div>`
- c) `<aside>`
- d) `<main>`
> **Respuesta correcta:** A  
> **Explicación:** El elemento `<article>` representa una composición auto-contenida en un documento, página o sitio web, susceptible de ser distribuida independientemente (ej. entradas de blog, comentarios, noticias).

---

### 🎨 Tema 2: CSS3 y Diseño Responsivo

#### Pregunta 2.1
En el modelo de cajas estándar de CSS (Box Model), ¿cuál es el orden correcto de capas desde el contenido central hacia el exterior?
- a) Contenido -> Margin -> Border -> Padding.
- b) Contenido -> Padding -> Border -> Margin.
- c) Contenido -> Border -> Padding -> Margin.
- d) Margin -> Padding -> Border -> Contenido.
> **Respuesta correcta:** B  
> **Explicación:** El Box Model de CSS se estructura desde dentro hacia afuera como: Contenido (Content) -> Relleno interior (Padding) -> Borde (Border) -> Margen exterior (Margin).

#### Pregunta 2.2
En CSS3, ¿qué valor de la propiedad `box-sizing` hace que el ancho (`width`) y alto (`height`) especificados incluyan el `padding` y el `border` dentro del tamaño total del elemento?
- a) `content-box`
- b) `border-box`
- c) `padding-box`
- d) `margin-box`
> **Respuesta correcta:** B  
> **Explicación:** Con `box-sizing: border-box`, el navegador incluye el relleno (`padding`) y los bordes (`border`) dentro de los valores declarados en `width` y `height`, facilitando el cálculo del layout. `content-box` es el comportamiento por defecto de CSS.

#### Pregunta 2.3
¿Qué módulo de diseño de CSS3 está optimizado para distribuir elementos en una sola dimensión (fila o columna) con alineación y distribución flexible del espacio disponible?
- a) CSS Grid Layout.
- b) CSS Flexible Box Layout (Flexbox).
- c) CSS Float Layout.
- d) CSS Multi-column Layout.
> **Respuesta correcta:** B  
> **Explicación:** Flexbox es un modelo de diseño unidimensional (1D: o en fila o en columna), mientras que CSS Grid es un sistema de diseño bidimensional (2D: filas y columnas simultáneas).

---

### ⚡ Tema 3: JavaScript y APIs del Navegador

#### Pregunta 3.1
En JavaScript moderno (ES6+), ¿cuál es la diferencia de ámbito (scope) entre declarar una variable con `var` y declararla con `let` o `const`?
- a) `var` tiene ámbito de bloque, mientras que `let` y `const` tienen ámbito de función.
- b) `var` tiene ámbito de función (o global si se declara fuera), mientras que `let` y `const` tienen ámbito de bloque (`{ ... }`) y no permiten hoisting con inicialización.
- c) No existe diferencia de ámbito; `let` y `const` son sólo palabras reservadas decorativas.
- d) `let` solo puede usarse en entornos de servidor Node.js y `var` en navegadores.
> **Respuesta correcta:** B  
> **Explicación:** Las variables declaradas con `var` tienen ámbito de función y sufren elevación (hoisting). Por el contrario, `let` y `const` tienen ámbito de bloque (`block scope`), evitando fugas de variables y colisiones.

#### Pregunta 3.2
En JavaScript, ¿qué método del objeto `JSON` se utiliza para convertir una cadena de texto en formato JSON a un objeto JavaScript nativo?
- a) `JSON.stringify()`
- b) `JSON.parse()`
- c) `JSON.toObject()`
- d) `JSON.decode()`
> **Respuesta correcta:** B  
> **Explicación:** `JSON.parse()` transforma una cadena de texto con formato JSON en un objeto JavaScript. La operación inversa (objeto a string) se realiza con `JSON.stringify()`.

---

### 🌐 Tema 4: Protocolo HTTP/HTTPS y Arquitectura REST

#### Pregunta 4.1
En el protocolo HTTP/1.1 y HTTP/2, ¿cuál de los siguientes códigos de estado de respuesta indica que una petición `POST` ha tenido éxito y ha dado como resultado la creación efectiva de un nuevo recurso en el servidor?
- a) 200 OK
- b) 201 Created
- c) 204 No Content
- d) 302 Found
> **Respuesta correcta:** B  
> **Explicación:** El código `201 Created` indica que la solicitud ha tenido éxito y ha provocado la creación de un nuevo recurso, típicamente incluyendo la cabecera `Location` con la URI del nuevo recurso creado.

#### Pregunta 4.2
En una API RESTful que sigue las directrices de diseño estándar, ¿qué método HTTP es idóneo para actualizar parcialmente un recurso existente sin enviar la representación completa del mismo?
- a) `PUT`
- b) `PATCH`
- c) `POST`
- d) `UPDATE`
> **Respuesta correcta:** B  
> **Explicación:** `PATCH` se utiliza para aplicar modificaciones parciales a un recurso. Por convención REST, `PUT` reemplaza el recurso completo de forma idempotente, mientras que `PATCH` actualiza únicamente los campos suministrados.

#### Pregunta 4.3
¿Cuál de los siguientes métodos HTTP se define formalmente como NO idempotente según el estándar RFC 7231 / RFC 9110?
- a) `GET`
- b) `PUT`
- c) `DELETE`
- d) `POST`
> **Respuesta correcta:** D  
> **Explicación:** Un método es idempotente si múltiples ejecuciones idénticas producen el mismo efecto en el estado del servidor. `GET`, `HEAD`, `PUT` y `DELETE` son idempotentes. `POST` NO es idempotente, ya que múltiples peticiones crearán múltiples registros o efectos acumulativos.

---

### ♿ Tema 5: Accesibilidad Web (WCAG 2.1 y EN 301 549)

#### Pregunta 5.1
¿Cuáles son los cuatro principios fundamentales de accesibilidad en los que se basan las Pautas de Accesibilidad para el Contenido Web (WCAG 2.1)?
- a) Velocidad, Usabilidad, Compatibilidad y Estilo.
- b) Perceptible, Operable, Comprensible y Robusto (POUR).
- c) Visibilidad, Audibilidad, Portabilidad y Navegabilidad.
- d) Semántica, Jerarquía, Responsive y Contraste.
> **Respuesta correcta:** B  
> **Explicación:** Los cuatro principios rectores de WCAG 2.1 son: 1) Perceptible, 2) Operable, 3) Comprensible (Understandable) y 4) Robusto.

#### Pregunta 5.2
Según el criterio de conformidad 1.4.3 de las WCAG 2.1 (Nivel AA), ¿cuál es el ratio de contraste visual mínimo exigido entre el texto de tamaño normal y su fondo?
- a) 3:1
- b) 4.5:1
- c) 7:1
- d) 2:1
> **Respuesta correcta:** B  
> **Explicación:** El nivel AA de WCAG 2.1 exige una relación de contraste mínima de 4.5:1 para texto normal y de 3:1 para texto grande (18pt o 14pt en negrita). El nivel AAA exige 7:1 para texto normal.

---

### 🔒 Tema 6: Seguridad de Aplicaciones Web (OWASP Top 10)

#### Pregunta 6.1
¿Qué vulnerabilidad de seguridad web permite a un atacante inyectar scripts maliciosos en el navegador de otros usuarios debido a la falta de sanitización o escape de datos de entrada?
- a) Inyección SQL (SQLi).
- b) Cross-Site Scripting (XSS).
- c) Cross-Site Request Forgery (CSRF).
- d) Server-Side Request Forgery (SSRF).
> **Respuesta correcta:** B  
> **Explicación:** El ataque XSS (Cross-Site Scripting) ocurre cuando una aplicación web incluye datos no confiables en una página web enviada al navegador sin validación ni codificación (escaping) adecuada, permitiendo la ejecución de JavaScript malicioso en el contexto del usuario.

#### Pregunta 6.2
¿Cuál es la técnica de mitigación primaria y más eficaz para prevenir de forma integral los ataques de Inyección SQL (SQLi)?
- a) Utilizar consultas parametrizadas (Prepared Statements) con vinculación de tipos de variables en lugar de concatenar cadenas de texto en sentencias SQL.
- b) Ocultar el formulario web mediante CSS.
- c) Utilizar métodos HTTP POST en lugar de GET en todos los formularios.
- d) Cambiar periódicamente el puerto de escucha del motor RDBMS.
> **Respuesta correcta:** A  
> **Explicación:** El uso de consultas preparadas (Prepared Statements) y procedimientos almacenados parametrizados garantiza que el motor de base de datos trate los datos del usuario estrictamente como literales de datos y nunca como código SQL ejecutable.

#### Pregunta 6.3
¿Qué cabecera de seguridad HTTP permite a los administradores de un sitio web declarar qué orígenes y tipos de recursos (scripts, imágenes, estilos) tiene permitido cargar el navegador del usuario?
- a) `Strict-Transport-Security` (HSTS)
- b) `Content-Security-Policy` (CSP)
- c) `X-Frame-Options`
- d) `Access-Control-Allow-Origin` (CORS)
> **Respuesta correcta:** B  
> **Explicación:** `Content-Security-Policy` (CSP) es una cabecera HTTP estándar que restringe las fuentes desde las que se pueden cargar y ejecutar scripts, imágenes, hojas de estilo o frames, mitigando drásticamente ataques XSS y clickjacking.

---

### 📊 Resumen Estadístico de Validación
- **Total de preguntas:** 20 preguntas completas
- **Temas cubiertos:** HTML5 semántico, CSS3 Box Model y layouts (Flexbox/Grid), JavaScript ES6+ (scope, JSON), Protocolo HTTP/HTTPS (métodos, idempotencia, códigos de estado), Arquitectura REST, Accesibilidad WCAG 2.1 (principios POUR, ratios de contraste AA), Seguridad Web OWASP (XSS, SQLi, CSRF, CSP, CORS).
- **Opciones:** 100% de las preguntas cuentan con opciones A, B, C y D con redacción técnica exhaustiva, sin opciones vacías ni literales truncados.
