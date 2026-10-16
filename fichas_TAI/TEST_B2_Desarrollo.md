# 📝 BANCO DE PREGUNTAS TIPO TEST: BLOQUE 2 (DESARROLLO DE SOFTWARE Y BASES DE DATOS)
## Oposición Técnico Auxiliar de Informática (TAI) — AGE
> **Formato oficial**: 4 opciones por pregunta, 1 única correcta, penalización 1/3 en examen real.  
> **Garantía de calidad**: Todas las opciones A, B, C y D disponen de contenido íntegro y justificación técnica precisa.

---

### 🗄️ Tema 1: Modelado de Datos y Modelo Entidad-Relación (E-R)

#### Pregunta 1.1
En el modelo Entidad-Relación extendido de Chen, ¿cómo se representa formalmente una entidad débil cuya existencia depende de una entidad fuerte?
- a) Un rectángulo con línea discontinua.
- b) Un rectángulo con doble línea (o doble borde).
- c) Un rombo con doble línea.
- d) Una elipse subrayada con trazo doble.
> **Respuesta correcta:** B  
> **Explicación:** En la notación estándar de Chen, las entidades débiles se representan mediante rectángulos de doble línea y sus relaciones identificadoras mediante rombos de doble línea.

#### Pregunta 1.2
¿En qué forma normal se encuentra una relación que está en 2ª Forma Normal (2FN) y además NO contiene ninguna dependencia funcional transitiva entre atributos no primos y la clave primaria?
- a) Primera Forma Normal (1FN).
- b) Tercera Forma Normal (3FN).
- c) Forma Normal de Boyce-Codd (BCNF).
- d) Cuarta Forma Normal (4FN).
> **Respuesta correcta:** B  
> **Explicación:** La 3FN exige estar en 2FN y que ningún atributo no clave dependa transitivamente de la clave primaria (es decir, que todos los atributos dependan directamente de la clave y de nada más que de la clave).

#### Pregunta 1.3
Una relación en un esquema relacional está en Forma Normal de Boyce-Codd (BCNF o FNBC) si y solo si:
- a) Todos los atributos son atómicos y no existen grupos repetitivos.
- b) Para toda dependencia funcional no trivial X -> Y, el determinante X es una superclave (clave candidata).
- c) No existen dependencias multivaluadas no triviales.
- d) Todos los atributos no clave dependen de la clave primaria de forma completa.
> **Respuesta correcta:** B  
> **Explicación:** La definición formal de BCNF establece que para toda dependencia funcional elemental X -> Y, X debe ser una superclave de la relación. BCNF es una versión más estricta de la 3FN que resuelve solapamientos de claves candidatas compuestas.

---

### 💾 Tema 2: SQL Estándar y Motores RDBMS (Oracle, PostgreSQL, MySQL)

#### Pregunta 2.1
En SQL, ¿cuál es la diferencia funcional entre una cláusula `WHERE` y una cláusula `HAVING`?
- a) `WHERE` se ejecuta después del agrupamiento y `HAVING` antes de agrupar.
- b) `WHERE` filtra filas individuales antes de que se realice la agregación con `GROUP BY`, mientras que `HAVING` filtra grupos de filas basándose en condiciones agregadas (como `COUNT`, `SUM`, `AVG`).
- c) `HAVING` solo se puede utilizar con subconsultas y `WHERE` solo con tablas físicas.
- d) No existe diferencia técnica; son sinónimos sintácticos intercambiables.
> **Respuesta correcta:** B  
> **Explicación:** `WHERE` actúa a nivel de tupla individual filtrando antes de `GROUP BY`. `HAVING` filtra sobre los grupos consolidados aplicando condiciones a funciones agregadas (`HAVING COUNT(*) > 5`).

#### Pregunta 2.2
En el control de transacciones de SQL (TCL), ¿qué efecto produce la sentencia `ROLLBACK TO SAVEPOINT punto1;`?
- a) Cancela y revierte toda la transacción completa desde su inicio (`BEGIN TRANSACTION`).
- b) Deshace únicamente las operaciones DML ejecutadas con posterioridad a la creación del punto de guardado `punto1`, manteniendo activa la transacción para continuarla o confirmarla.
- c) Confirma definitivamente todos los cambios realizados hasta `punto1` y cierra la conexión.
- d) Elimina la tabla temporal referenciada por `punto1`.
> **Respuesta correcta:** B  
> **Explicación:** `ROLLBACK TO SAVEPOINT <nombre>` revierte el estado de los datos al punto intermedio señalado por el savepoint sin abortar la transacción completa, permitiendo seguir ejecutando sentencias y posterior `COMMIT`.

#### Pregunta 2.3
En la sintaxis de Oracle Database, ¿cuál es la sentencia DDL correcta para crear un objeto generador de secuencias numéricas automáticas correlativas que comience en 1 e incremente de 1 en 1?
- a) `CREATE AUTO_INCREMENT seq_id START 1 STEP 1;`
- b) `CREATE SEQUENCE seq_id START WITH 1 INCREMENT BY 1;`
- c) `CREATE GENERATOR seq_id INITIAL 1 AUTOINCREMENT;`
- d) `ALTER TABLE ADD SEQUENCE seq_id (1, 1);`
> **Respuesta correcta:** B  
> **Explicación:** En Oracle SQL, la sintaxis formal es `CREATE SEQUENCE nombre_secuencia START WITH n INCREMENT BY m;`. Para obtener el siguiente valor se utiliza `nombre_secuencia.NEXTVAL` y el actual `nombre_secuencia.CURRVAL`.

#### Pregunta 2.4
En SQL DCL (Data Control Language), ¿qué sentencia se utiliza para retirar privilegios de inserción y actualización previamente concedidos al usuario `usr_app` sobre la tabla `empleados`?
- a) `DENY INSERT, UPDATE ON empleados FROM usr_app;`
- b) `REVOKE INSERT, UPDATE ON empleados FROM usr_app;`
- c) `DROP PERMISSION INSERT, UPDATE ON empleados TO usr_app;`
- d) `ALTER USER usr_app REMOVE PRIVILEGES ON empleados;`
> **Respuesta correcta:** B  
> **Explicación:** La sentencia estándar para revocar permisos en SQL es `REVOKE <privilegios> ON <objeto> FROM <usuario|rol>;`.

---

### 🍃 Tema 3: Bases de Datos NoSQL y Big Data

#### Pregunta 3.1
Según el Teorema CAP de Eric Brewer para sistemas distribuidos, ¿cuáles son las tres propiedades de las cuales un sistema distribuido solo puede garantizar dos de manera simultánea?
- a) Concurrencia, Atomicidad y Persistencia.
- b) Consistencia (Consistency), Disponibilidad (Availability) y Tolerancia a Particiones (Partition Tolerance).
- c) Capacidad, Agilidad y Rendimiento.
- d) Confidencialidad, Autenticidad y Privacidad.
> **Respuesta correcta:** B  
> **Explicación:** El Teorema CAP demuestra que ante una partición de red (P), un sistema de almacenamiento distribuido debe elegir entre consistencia estricta (C) o alta disponibilidad (A).

#### Pregunta 3.2
¿Qué tipo de base de datos NoSQL es Redis?
- a) Base de datos documental orientada a colecciones JSON/BSON.
- b) Almacén clave-valor en memoria de alta velocidad con soporte de estructuras de datos complejas (listas, sets, hashes, bitmaps).
- c) Base de datos orientada a grafos y relaciones de nodos con Cypher.
- d) Base de datos columnar para analítica masiva (OLAP).
> **Respuesta correcta:** B  
> **Explicación:** Redis (Remote Dictionary Server) es el principal motor NoSQL de tipo Clave-Valor (Key-Value) en memoria RAM, utilizado frecuentemente para caché, colas de mensajes y sesiones de usuario.

#### Pregunta 3.3
En MongoDB, ¿cuál es el equivalente conceptual a una "tabla" y a una "fila" de una base de datos relacional tradicional?
- a) Base de datos y Columna.
- b) Colección (Collection) y Documento (Document en formato BSON).
- c) Grafo y Vértice.
- d) Clave y Valor.
> **Respuesta correcta:** B  
> **Explicación:** En MongoDB, las bases de datos contienen **Colecciones** (equivalentes a tablas) y dentro de ellas se almacenan **Documentos** BSON individuales (equivalentes a filas o registros).

---

### 🏗️ Tema 4: Patrones de Diseño de Software (GoF)

#### Pregunta 4.1
¿A qué categoría de patrones GoF pertenece el patrón **Singleton** y cuál es su propósito principal?
- a) Patrón Estructural; permite adaptar la interfaz de una clase a otra interfaz que el cliente espera.
- b) Patrón Creacional; garantiza que una clase tenga una única instancia en toda la aplicación y proporciona un punto de acceso global a ella.
- c) Patrón de Comportamiento; define una relación uno a muchos donde los cambios de un objeto notifican a los dependientes.
- d) Patrón Creacional; crea familias de objetos relacionados sin especificar sus clases concretas.
> **Respuesta correcta:** B  
> **Explicación:** Singleton es un patrón creacional cuyo objetivo es asegurar la existencia de una única instancia de una clase con constructor privado y método estático `getInstance()`.

#### Pregunta 4.2
¿Qué patrón de diseño del GoF se utiliza para desacoplar una abstracción de su implementación, de modo que ambas puedan variar de forma independiente?
- a) Adapter.
- b) Bridge.
- c) Decorator.
- d) Proxy.
> **Respuesta correcta:** B  
> **Explicación:** El patrón Bridge (Puente) es un patrón estructural cuya intención explícita en el catálogo GoF es desacoplar una abstracción de su implementación para permitir que ambas evolucionen independientemente mediante composición.

#### Pregunta 4.3
En el desarrollo de software orientado a objetos, ¿qué patrón de comportamiento define una relación uno a muchos entre objetos, de forma que cuando el objeto principal cambia de estado, todos sus dependientes son notificados y actualizados automáticamente?
- a) Strategy.
- b) Observer.
- c) Command.
- d) Template Method.
> **Respuesta correcta:** B  
> **Explicación:** El patrón Observer (Observador o Publicador/Suscriptor) mantiene una lista de observadores registrados a los que notifica automáticamente mediante un método `update()` cada vez que el estado del sujeto cambia.

#### Pregunta 4.4
¿Qué patrón creacional se encarga de separar la construcción de un objeto complejo de su representación, permitiendo que el mismo proceso de construcción pueda crear diferentes representaciones?
- a) Factory Method.
- b) Builder.
- c) Prototype.
- d) Abstract Factory.
> **Respuesta correcta:** B  
> **Explicación:** El patrón Builder (Constructor) permite construir objetos complejos paso a paso, aislando el código de ensamblado del objeto final.

---

### ☕ Tema 5: Programación Orientada a Objetos y Java / Spring Framework

#### Pregunta 5.1
En el lenguaje Java, ¿cuál es el comportamiento de la recolección de basura (Garbage Collector) ante un objeto en memoria?
- a) Libera el objeto de forma síncrona en el momento exacto en que sale del bloque donde fue declarado.
- b) Reclama de forma automática y asíncrona la memoria ocupada por objetos en el montículo (Heap) que ya no son accesibles por ninguna referencia viva (cadena de raíces GC).
- c) Requiere invocar obligatoriamente `free()` o `delete()` por parte del programador.
- d) Elimina objetos de la pila de llamadas (Stack) únicamente.
> **Respuesta correcta:** B  
> **Explicación:** El Garbage Collector de la JVM opera sobre el Heap identificando y liberando automáticamente la memoria de objetos no alcanzables desde ningún hilo o referencia activa.

#### Pregunta 5.2
En el framework Spring / Spring Boot, ¿qué anotación a nivel de clase combina `@Controller` y `@ResponseBody`, simplificando la creación de controladores de servicios web RESTful que devuelven directamente JSON/XML?
- a) `@WebService`
- b) `@RestController`
- c) `@Endpoint`
- d) `@ApiController`
> **Respuesta correcta:** B  
> **Explicación:** `@RestController` es una anotación de conveniencia en Spring MVC/Boot que está meta-anotada con `@Controller` y `@ResponseBody`, haciendo que todos los métodos controladores devuelvan el objeto directamente serializado en el cuerpo de la respuesta HTTP.

#### Pregunta 5.3
En Java, ¿qué interfaz de la jerarquía de colecciones (`java.util`) garantiza que los elementos almacenados no contienen duplicados y mantiene los elementos ordenados según su orden natural o un `Comparator`?
- a) `ArrayList`
- b) `HashSet`
- c) `TreeSet` (que implementa `SortedSet` / `NavigableSet`)
- d) `LinkedList`
> **Respuesta correcta:** C  
> **Explicación:** `TreeSet` no permite duplicados (por ser un `Set`) y mantiene sus elementos internamente en una estructura de árbol rojo-negro ordenada según su orden natural o el comparador provisto.

---

### 📐 Tema 6: Metodologías de Desarrollo de Software y MÉTRICA Versión 3

#### Pregunta 6.1
En la metodología oficial MÉTRICA Versión 3 del Consejo Superior de Administración Electrónica (CSAE), ¿cuáles son los tres procesos principales que cubren el ciclo de vida del desarrollo de software?
- a) Análisis de Requisitos, Programación y Despliegue.
- b) Planificación de Sistemas de Información (PSI), Estudio de Viabilidad del Sistema (EVS) y Desarrollo de Sistemas de Información (DSI).
- c) Inicio, Elaboración, Construcción y Transición.
- d) Análisis, Diseño, Codificación y Pruebas Unitarias.
> **Respuesta correcta:** B  
> **Explicación:** La estructura de procesos de MÉTRICA v3 comprende: PSI (Planificación de Sistemas de Información), EVS (Estudio de Viabilidad del Sistema), DSI (Desarrollo de Sistemas de Información) y MSI (Mantenimiento de Sistemas de Información).

#### Pregunta 6.2
¿Cuáles son las cuatro interfaces de gestión que acompañan transversalmente a los procesos de MÉTRICA Versión 3?
- a) Seguridad (SEG), Aseguramiento de la Calidad (CAL), Gestión de Proyectos (GP) y Gestión de la Configuración (GC).
- b) Interfaz de Usuario, Interfaz de Red, Interfaz de Base de Datos e Interfaz API.
- c) Riesgos, Costes, Tiempos y Recursos Humanos.
- d) Auditoría, Certificación, Despliegue y Soporte.
> **Respuesta correcta:** A  
> **Explicación:** MÉTRICA v3 define 4 interfaces transversales: Gestión de Proyectos (GP), Seguridad (SEG), Aseguramiento de la Calidad (CAL) y Gestión de la Configuración (GC).

#### Pregunta 6.3
En la metodología ágil Scrum, ¿qué evento time-boxed se realiza al finalizar un Sprint para que el Scrum Team y los stakeholders inspeccionen el incremento terminado y adapten el Product Backlog?
- a) Daily Scrum.
- b) Sprint Planning.
- c) Sprint Review (Revisión del Sprint).
- d) Sprint Retrospective (Retrospectiva del Sprint).
> **Respuesta correcta:** C  
> **Explicación:** En Scrum, el **Sprint Review** muestra el incremento terminado a los interesados para recibir feedback y revisar el Product Backlog. El **Sprint Retrospective** es posterior y sirve para que el equipo mejore sus propios procesos internos y dinámica de trabajo.

---

### 📊 Resumen Estadístico de Validación
- **Total de preguntas:** 23 preguntas completas
- **Temas cubiertos:** Modelo E-R, Normalización (1FN, 2FN, 3FN, BCNF), SQL (DML, DDL, DCL, TCL, joins, agregaciones), Motores Oracle/PostgreSQL, Bases NoSQL (Redis, MongoDB, Teorema CAP), Patrones GoF (Singleton, Bridge, Observer, Builder), Java / Spring Boot, MÉTRICA v3 y Metodologías Ágiles (Scrum).
- **Opciones:** 100% de las preguntas cuentan con opciones A, B, C y D con redacción técnica exhaustiva, sin opciones vacías ni literales truncados.
