# 🗄️ BLOQUE 2A — BASES DE DATOS Y DESARROLLO DE SOFTWARE
> *Fichas de estudio basadas en exámenes oficiales TAI 2022, 2024 y 2025*

---

## ÍNDICE RÁPIDO
| Tema | Preguntas 2025 | Dificultad |
|------|---------------|------------|
| Modelo Relacional / E-R | 3-4 preguntas | ⭐⭐ |
| SQL (DML, DDL, DCL, TCL) | 4-6 preguntas | ⭐⭐⭐ |
| NoSQL y tipos de BD | 2-3 preguntas | ⭐⭐ |
| Oracle específico | 2-3 preguntas | ⭐⭐⭐ |
| Patrones de diseño OOP | 2-3 preguntas | ⭐⭐⭐ |
| Java / JVM / Jakarta EE | 2-3 preguntas | ⭐⭐⭐ |
| .NET / CLR | 1-2 preguntas | ⭐⭐ |
| Spring Boot / REST | 2-3 preguntas | ⭐⭐⭐ |
| Pruebas de software | 2-3 preguntas | ⭐⭐ |
| Git / Control de versiones | 1-2 preguntas | ⭐⭐ |
| Algoritmos y estructuras | 2-3 preguntas | ⭐⭐ |
| Formatos de datos (JSON/CSV/XML) | 2-3 preguntas | ⭐⭐ |

---

## 1. MODELO ENTIDAD-RELACIÓN (E-R)

### 1.1 Conceptos Básicos
| Concepto | Definición |
|---------|-----------|
| **Grado** | Número de **columnas** (atributos) de una relación |
| **Cardinalidad** | Número de **filas** (tuplas) de una relación |
| **Dominio** | Conjunto de valores válidos para un atributo |

> [!CAUTION]
> **TRAMPA 2025**: En una entidad con **4 columnas y 7 filas**: grado = **4**, cardinalidad = **7**. Muchos confunden grado con cardinalidad. Respuesta: **a**.

### 1.2 Tipos de Atributos en Diagramas E-R
| Símbolo | Tipo de atributo |
|---------|----------------|
| Elipse sólida | Atributo simple |
| Elipse **discontinua/punteada** | Atributo **derivado** |
| Elipse doble | Atributo **multivaluado** |
| Elipse con subatributos | Atributo **compuesto** |
| Elipse subrayada | Atributo **clave primaria** |

> [!CAUTION]
> **TRAMPA 2025**: Elipse **discontinua** = atributo **derivado** (no multivaluado, no clave). Respuesta: **d**.

### 1.3 Reglas de Integridad Relacional
| Regla | Definición |
|-------|-----------|
| **Integridad de entidad** | La clave primaria no puede contener valores NULL |
| **Integridad referencial** | Todo valor **no nulo** de clave ajena debe existir en la clave referenciada |

> [!CAUTION]
> **TRAMPA 2025**: Integridad referencial = valor no nulo de clave ajena debe existir en la referenciada. La clave ajena **puede ser NULL** (diferencia con la clave primaria). Respuesta: **a**.

### 1.4 Modelo Dimensional de Kimball
| Concepto | Definición |
|---------|-----------|
| **Tabla de hechos** | Contiene medidas/métricas del negocio y FK a dimensiones |
| **Dimensión** | Tabla con atributos descriptivos para analizar los hechos |
| **Dimensión outrigger** | **Tabla de dimensión** enlazada **en otra tabla de dimensión** |
| **Fact constellation** | Tabla de hechos enlazada en otra tabla de hechos |

> [!CAUTION]
> **TRAMPA 2025**: Dimensión **outrigger** = dimensión que referencia a otra dimensión (no hechos). Respuesta: **b**.

---

## 2. SQL — LENGUAJE DE CONSULTA ESTRUCTURADO

### 2.1 Categorías de Comandos SQL
| Categoría | Sigla | Comandos |
|-----------|-------|---------|
| **Definición de datos** | DDL | CREATE, ALTER, DROP, TRUNCATE |
| **Manipulación de datos** | DML | SELECT, INSERT, UPDATE, DELETE |
| **Control de datos** | DCL | GRANT, REVOKE, **DENY** |
| **Control de transacciones** | TCL | COMMIT, ROLLBACK, SAVEPOINT |
| **Consulta** | DQL | SELECT (a veces separado) |

> [!CAUTION]
> **TRAMPA 2025**: **DENY** (en Transact-SQL) pertenece a **DCL** (no DML, no TCL). Respuesta: **a**.
> **GRANT** = asignar permisos a tablas (no ALTER TABLE, no PERMISSION).

### 2.2 ROLLBACK vs SAVEPOINT
| Comando | Acción |
|---------|--------|
| **ROLLBACK** | Restituye **todas** las modificaciones desde el inicio de la transacción o desde un punto de retorno |
| **SAVEPOINT** | Crea un punto de retorno parcial dentro de la transacción |
| **COMMIT** | Confirma permanentemente los cambios de la transacción |

> [!CAUTION]
> **TRAMPA 2025**: Para deshacer cambios → **ROLLBACK** (no RETURNBACK, que no existe). Respuesta: **c**.

### 2.3 Triggers en ANSI SQL
Sintaxis estándar de creación de trigger:
```sql
CREATE TRIGGER nombre_trigger
BEFORE UPDATE ON nombre_tabla
FOR EACH ROW
BEGIN
  -- instrucciones
END;
```

> [!CAUTION]
> **TRAMPA 2025**: La forma correcta en ANSI SQL es `CREATE TRIGGER ... BEFORE UPDATE ON Departamento` (opción d). NO es `OF TABLE`, NO es `ON TABLE`, NO es `NEW TRIGGER`.

### 2.4 Consultas SQL Frecuentes en Supuestos

**INNER JOIN** (solo registros con coincidencia en ambas tablas):
```sql
SELECT * FROM ALUMNO 
INNER JOIN MATRICULA ON ALUMNO.id_alumno = MATRICULA.id_alumno;
```

**GROUP BY con COUNT**:
```sql
SELECT id_programa, COUNT(*) 
FROM MATRICULA 
GROUP BY id_programa;
```

> [!CAUTION]
> **TRAMPA 2025**: `COUNT(*)` no `COUNT(id_programa)` para contar todas las filas. El `GROUP BY` es obligatorio cuando hay función de agregación con columnas no agregadas.

### 2.5 Transacciones — Propiedades ACID
| Propiedad | Definición | Mnemotecnia |
|-----------|-----------|-------------|
| **Atomicidad** | Todo o nada | **A**tomicidad |
| **Consistencia** | Los datos cumplen todas las restricciones | **C**onsistencia |
| **Aislamiento** | Las transacciones concurrentes **no se interfieren** entre sí | **I**solation |
| **Durabilidad** | Cambios confirmados persisten ante fallos | **D**urabilidad |

> [!CAUTION]
> **TRAMPA 2025**: Aislamiento = transacciones concurrentes no interfieren (no es "todo o nada" que es atomicidad). Respuesta: **c**.

---

## 3. ORACLE — COMANDOS ESPECÍFICOS

### 3.1 SEQUENCE en Oracle
Sintaxis correcta:
```sql
CREATE SEQUENCE seq_nombre
  START WITH 1
  INCREMENT BY 1;
```

Para usar: `seq_nombre.NEXTVAL`

> [!CAUTION]
> **TRAMPA 2025**: La sintaxis correcta usa `START WITH` e `INCREMENT BY` (no `START`, `BEGIN WITH`, `INIT`). Respuesta: **c**.

### 3.2 Garantizar Unicidad en Oracle
| Necesidad | Solución |
|-----------|---------|
| Valores únicos + rendimiento máximo en búsquedas | `ALTER TABLE ... ADD CONSTRAINT ... UNIQUE (campo)` + índice implícito |
| Solo unicidad | `ALTER TABLE ... ADD CONSTRAINT ... UNIQUE` |
| Solo búsqueda rápida (sin unicidad) | `CREATE INDEX` |

> [!CAUTION]
> **TRAMPA 2025**: Para garantizar unicidad Y rendimiento, se usa `ALTER TABLE ADD CONSTRAINT UNIQUE` (que crea índice implícito). No es `CREATE INDEX` solo (no garantiza unicidad). Respuesta: **b**.

### 3.3 CREATE USER en Oracle
```sql
CREATE USER nombre_usuario IDENTIFIED BY contraseña;
```

> [!CAUTION]
> **TRAMPA 2025**: `CREATE USER ... IDENTIFIED BY ...` es la sintaxis Oracle. No es `REGISTER USER`, `ADD USER`, ni `NEW USER`. Respuesta: **d**.

### 3.4 Jakarta Persistence / Hibernate — Anotaciones
```java
@Entity
public class Alumno {
    @Id
    private Long id;
    private String nombre;
}
```

| Anotación | Uso |
|-----------|-----|
| `@Entity` | Define clase como entidad persistente |
| `@Table` | Especifica tabla de BD (opcional) |
| `@Id` | Marca la clave primaria |
| `@Column` | Personaliza columna |

> [!CAUTION]
> **TRAMPA 2025**: Para definir entidad persistente = `@Entity` (no `@Table`, no `@Persistent`, no `@DatabaseEntity`). Respuesta: **a**.

---

## 4. BASES DE DATOS NoSQL

### 4.1 Tipos de Bases de Datos NoSQL
| Tipo | Ejemplo | Características |
|------|---------|----------------|
| **Clave-valor** | Redis, DynamoDB | Máxima velocidad, estructura simple |
| **Documentos** | MongoDB, CouchDB | Documentos JSON/BSON, esquema flexible |
| **Grafos** | **Neo4j** | Relaciones complejas, lenguaje Cypher |
| **Columnar** | Cassandra, HBase | Grandes volúmenes, columnas agrupadas |

> [!CAUTION]
> **TRAMPA 2025**: Los tipos NoSQL son **Clave-valor, Documentales, Grafos y Columnares** (no "sistemáticos" ni "metodológicas"). Respuesta: **c**.
> **Neo4j** usa **Cypher** como lenguaje de consulta. Respuesta: **d**.

### 4.2 Bases de Datos Orientadas a Objetos

**Constructores de tipo de colección:**
- ✅ Array
- ✅ Bolsa (Bag) — admite duplicados sin orden
- ✅ Lista — admite duplicados con orden
- ❌ **Columna** — NO es constructor de colección

**OID (Object Identifier):**
- Generado por el **sistema** (no visible al usuario externo)
- No depende de atributos del objeto
- Proporciona identidad independiente del estado

> [!CAUTION]
> **TRAMPA 2025**: **Columna** NO es constructor de tipo de colección. OID está **generado por el sistema** (no almacenado en el programa de aplicación). Respuestas: **a** y **c**.

---

## 5. PROGRAMACIÓN ORIENTADA A OBJETOS

### 5.1 Conceptos de Herencia
| Concepto | Definición |
|---------|-----------|
| **Sobrescritura (Overriding)** | Subclase **redefine** un método de la superclase con **misma firma** |
| **Sobrecarga (Overloading)** | Mismo nombre de método, **diferente lista de parámetros** |
| **Ocultación (Field Hiding)** | Subclase declara campo con mismo nombre que superclase |

> [!CAUTION]
> **TRAMPA 2025**: Misma lista de parámetros + especializar comportamiento = **Overriding** (no Overloading). Respuesta: **c**.

### 5.2 Instancia vs Clase
- **Instancia**: ejemplar **concreto e individualizado** de una clase que posee su **propio estado**
- No es el código fuente, no es un método estático, no es el paquete

### 5.3 Patrones de Diseño — Más Frecuentes en TAI

| Patrón | Tipo | Propósito |
|--------|------|-----------|
| **Observer** | Comportamiento | **Notificar automáticamente** a múltiples objetos sobre cambios de estado. Acoplamiento débil |
| **Singleton** | Creacional | Una sola instancia de la clase |
| **Adapter** | Estructural | Adapta una interfaz incompatible |
| **Factory Method** | Creacional | Delega la creación de objetos a subclases |
| **Strategy** | Comportamiento | Encapsula algoritmos intercambiables |
| **Decorator** | Estructural | Añade responsabilidades dinámicamente |

> [!CAUTION]
> **TRAMPA 2025**: Notificar múltiples objetos sobre cambios de estado = **Observer** (no Singleton, no Adapter, no Factory). Respuesta: **b**.

---

## 6. JAVA / JVM / JAKARTA EE

### 6.1 Componentes de la JVM/JDK
| Componente | Función |
|-----------|---------|
| **JIT (Just-In-Time Compiler)** | **Compila bytecode a código máquina en tiempo de ejecución** |
| **Garbage Collector** | Libera memoria automáticamente |
| **Bytecode** | Código intermedio independiente de plataforma |
| **SDK/JDK** | Kit de desarrollo, incluye compilador javac |

> [!CAUTION]
> **TRAMPA 2025**: El componente que **compila código intermedio a código máquina en tiempo de ejecución** es el **JIT**. Respuesta: **c**.

### 6.2 Jakarta EE — REST
```java
// Jakarta RESTful Web Services (JAX-RS)
@Path("/alumnos")
public class AlumnoResource {
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public List<Alumno> getAll() { ... }
}
```

**Para microservicios REST en Jakarta EE** → **Jakarta RESTful Web Services** (no Jakarta Mail, no Jakarta Pages)

> [!CAUTION]
> **TRAMPA 2025**: Especificación para REST en Jakarta EE = **Jakarta RESTful Web Services**. Respuesta: **b**.

### 6.3 Spring Boot — Controlador REST
```java
@RestController
public class AlumnoController {
    @GetMapping("/alumnos")
    public List<Alumno> obtenerAlumnos() {
        return repository.findAll();
    }
}
```

**Anotaciones clave:**
| Anotación | Uso |
|-----------|-----|
| `@RestController` | Controlador REST (= `@Controller` + `@ResponseBody`) |
| `@GetMapping` | Mapea peticiones GET |
| `@PostMapping` | Mapea peticiones POST |
| `@RequestBody` | Mapea cuerpo de la petición |
| `@PathVariable` | Extrae variable de la URL |

> [!CAUTION]
> **TRAMPA 2025**: Usar `@RestController` + `@GetMapping` (no `@Controller` + `@Get`, no `@WebController`). Respuesta: **a**.

**Comando Maven para ejecutar Spring Boot:**
```bash
mvn spring-boot:run
```

> [!CAUTION]
> **TRAMPA 2025**: `mvn spring-boot:run` (no `launch`, no `run spring-boot`). Respuesta: **c**.

### 6.4 JUnit — Pruebas Unitarias
```java
@Test
void testCalcularMatriculas() {
    AlumnoService service = new AlumnoService();
    assertEquals(3, service.calcularMatriculas(3));
}
```

Reglas:
- Se crea instancia del objeto a probar
- Se usa `assertEquals(expected, actual)` para verificar
- El objeto no puede ser `null`

---

## 7. PLATAFORMA .NET / CLR

### 7.1 Componentes .NET
| Componente | Función |
|-----------|---------|
| **CLR (Common Language Runtime)** | **Manejo de excepciones + Garbage Collection** |
| MSBuild | Herramienta de compilación/construcción |
| Kestrel | Servidor web integrado de ASP.NET Core |
| NuGet | Gestor de paquetes de .NET |

> [!CAUTION]
> **TRAMPA 2025**: CLR = encargado de **excepciones y Garbage Collection**. Respuesta: **c**.

### 7.2 Ensamblados .NET
- Solo se **cargan en memoria si son necesarios**
- En .NET Framework: pueden compartirse en **GAC** (Global Assembly Cache, no GAP)

---

## 8. ALGORITMOS Y ESTRUCTURAS DE DATOS

### 8.1 Complejidad de Algoritmos de Ordenación
| Algoritmo | Mejor caso | Caso medio | Peor caso |
|-----------|-----------|------------|-----------|
| **Radix Sort** | **O(n·k)** — tiempo **lineal** | O(n·k) | O(n·k) |
| QuickSort | O(n log n) | O(n log n) | O(n²) |
| MergeSort | O(n log n) | O(n log n) | O(n log n) |
| HeapSort | O(n log n) | O(n log n) | O(n log n) |

> [!CAUTION]
> **TRAMPA 2025**: Algoritmo que se ejecuta en **tiempo lineal** = **Radix Sort** (no HeapSort, no MergeSort, no QuickSort). Respuesta: **c**.

### 8.2 Árboles Rojo-Negro
Propiedades:
1. Cada nodo es rojo o negro
2. La **raíz es NEGRA** ✅
3. Las hojas (NIL) son negras
4. Si un nodo es **rojo**, sus hijos son **negros** (no rojos)
5. Para cada nodo, todos los caminos a hojas contienen el **mismo número de nodos NEGROS**

> [!CAUTION]
> **TRAMPA 2025**: La raíz es **negra** (opción d correcta). Si un nodo es rojo, sus hijos son **negros** (no rojos). El camino mismo número de nodos **negros** (no rojos). Respuesta: **d**.

### 8.3 Colas y Pilas
| Estructura | Política | Característica |
|-----------|---------|----------------|
| **Cola (Queue)** | **FIFO** (First In, First Out) | Inserción por cola, extracción por cabeza |
| **Pila (Stack)** | **LIFO** (Last In, First Out) | Inserción y extracción por el mismo extremo |

> [!CAUTION]
> **TRAMPA 2025**: Una cola sigue política **FIFO** (no LIFO). Tiene cabecera y cola. No permite acceder a cualquier posición.

### 8.4 Estructuras de Arrays
- **Slice de un array**: Una **subestructura** (subarray) del array original — no es su longitud, primer elemento, ni último

### 8.5 Algoritmo Greedy (Voraz)
- **Siempre toma la decisión que parece mejor en el momento** (óptima local)
- No siempre alcanza la solución globalmente óptima
- No es solo para selección de actividades (se aplica a varios problemas)
- No divide en subproblemas (eso es divide y vencerás)

---

## 9. SERVICIOS WEB Y ARQUITECTURAS

### 9.1 WSDL 2.0
**Web Services Description Language 2.0** — según W3C:
- Lenguaje **XML para describir servicios web**
- Permite describir el servicio a partir de un **modelo abstracto**

> [!CAUTION]
> **TRAMPA**: SOAP define "envelope" y reglas de codificación. REST define métodos GET/POST y códigos de estado. WebSocket es bidireccional sobre TCP. **WSDL** es para DESCRIBIR servicios. Respuesta: **a**.

### 9.2 Métodos HTTP — Idempotencia y Seguridad
| Método | Seguro | Idempotente |
|--------|--------|-------------|
| GET | ✅ Sí | ✅ Sí |
| HEAD | ✅ Sí | ✅ Sí |
| **PUT** | ❌ No | ✅ **Sí** |
| DELETE | ❌ No | ✅ Sí |
| **POST** | ❌ No | ❌ No |
| PATCH | ❌ No | ❌ No |

- **Seguro**: no modifica el recurso
- **Idempotente**: múltiples peticiones idénticas tienen el mismo efecto que una sola

> [!CAUTION]
> **TRAMPA 2025**: **PUT** es **idempotente pero NO seguro** (no GET que es seguro, no POST que no es idempotente). Respuesta: **c**.

### 9.3 Códigos de Estado HTTP
| Rango | Significado |
|-------|------------|
| 1xx | Informacional |
| 2xx | Éxito |
| **201 Created** | Recurso **creado correctamente** (respuesta a POST exitoso) |
| **200 OK** | Éxito general |
| **204 No Content** | Éxito sin cuerpo de respuesta |
| 3xx | Redirección |
| **4xx** | Error del **cliente** |
| 404 Not Found | Recurso no encontrado |
| **5xx** | Error del **servidor** |

> [!CAUTION]
> **TRAMPA 2025**: Crear un recurso (POST exitoso) → código **201 Created** (no 200 OK). Errores del cliente → **4xx**. Respuesta supuesto: **b**.

### 9.4 Git — Repositorios y Pull Requests
**Repositorio**: Espacio que contiene el conjunto de archivos de un proyecto y el **historial completo de cambios**

**Pull request**: Propuesta para **fusionar (merge) un conjunto de cambios de una rama en otra**
- No es `git pull`
- No es una etiqueta (eso es `git tag`)
- No es retirar código de producción

---

## 10. FORMATOS DE DATOS

### 10.1 JSON — RFC 8259
**Tipos de valores JSON** (conjunto correcto):
- `object`, `array`, `number`, `string`, `true`, `false`, `null`

> [!CAUTION]
> **TRAMPA 2025**: JSON NO tiene tipos `date`, `undefined`, `function`, `NaN`, ni `boolean` como tipo (tiene los literales `true` y `false`). Respuesta: **c**.

### 10.2 CSV — RFC 4180
Reglas del formato CSV según RFC 4180:
- Cada registro en una **línea separada por CRLF**
- Campos que contengan **coma, comillas o saltos de línea** → deben ir con **comillas dobles**
- Tipo MIME: `text/csv` (no `application/csv`)

> [!CAUTION]
> **TRAMPA 2025**: Regla correcta de CSV = CRLF + comillas dobles para campos especiales. El MIME es `text/csv`. Respuesta: **b**.

### 10.3 XML — Documento Bien Formado
**Requisitos para XML bien formado:**
1. Un único **elemento raíz**
2. Etiquetas de apertura y cierre correctamente anidadas
3. Atributos entre comillas
4. Sin caracteres ilegales sin escapar

```xml
<?xml version="1.0" encoding="UTF-8"?>
<alumno>
  <id_alumno>10</id_alumno>
  <nombre>Juan Pérez</nombre>
</alumno>
```

> [!CAUTION]
> **TRAMPA 2025**: Solo **un elemento raíz** (no varios aunque haya DTD). Las etiquetas deben coincidir (`<id_alumno>...</id_alumno>`). Respuesta: **b**.

**Número de elementos raíz en XML bien formado**: Solo **uno**. Respuesta: **d**.

---

## 11. PRUEBAS DE SOFTWARE

### 11.1 Tipos de Pruebas
| Tipo | Descripción |
|------|-------------|
| **Regresión** | Comprueban que cambios en un componente **no introducen errores** en otros componentes no modificados |
| **Caja blanca** | Conocen la estructura interna del sistema (no solo E/S) |
| **Caja negra** | Solo E/S, sin conocer la estructura interna |
| **Unitarias** | Prueban unidades individuales de código |
| **Integración** | Prueban interfaces entre grupos de componentes |
| **Aceptación** | El **usuario** determina si el sistema es aceptable |

> [!CAUTION]
> **TRAMPA 2025**: Pruebas de **regresión** = verifican que cambios no introducen errores en otros componentes. Las de "caja blanca" SÍ se preocupan por la estructura interna. Las unitarias no son para el usuario final.

### 11.2 Herramientas de Pruebas
✅ **Productos de pruebas de software**: Avocado, Cucumber, TestLink  
❌ **OneTrust** = herramienta de **privacidad y cumplimiento** (NO de pruebas)

> [!CAUTION]
> **TRAMPA 2025**: OneTrust NO es herramienta de pruebas. Respuesta: **d**.

---

## 12. SISTEMAS OPERATIVOS — COMANDOS LINUX

### 12.1 Comandos Frecuentes en Exámenes TAI
| Comando | Función |
|---------|---------|
| `tail -f fichero` | Ver en **tiempo real** el contenido de un fichero a medida que crece |
| `chmod` | **Cambiar permisos** de acceso de un archivo/directorio |
| `chown` | Cambiar propietario |
| `ln -s` | Crear enlace simbólico |
| `ip route show` | Ver tabla de enrutamiento en Linux |
| `ip route get IP` | Ver **ruta efectiva** a una IP específica |
| `ss -ltn` | Listar **puertos en escucha** del sistema |

> [!CAUTION]
> **TRAMPA 2025**: `chmod` = cambiar **permisos** (no propietario). `tail -f` = tiempo real. `ip route show` = tabla de rutas. `ss -ltn` = puertos en escucha.

### 12.2 Crontab — Sintaxis
```
minuto hora dia_mes mes dia_semana comando
```

Ejemplo: `0 5 8 11 *` = A las **05:00 del día 8 de noviembre**

> [!CAUTION]
> **TRAMPA 2025**: El orden es `min hora dia mes dia_semana`. `0 5 8 11 *` = minuto 0, hora 5, día 8, mes 11 (noviembre). Respuesta: **b**.

### 12.3 Sistemas de Archivos
| Sistema | Uso |
|---------|-----|
| **ExFAT** | Compatible nativo con **Windows** (>32GB) **y macOS** |
| APFS | Solo macOS/iOS |
| HFS+ | macOS antiguo |
| ReFS | Solo Windows Server |
| NTFS | Windows (no nativo en macOS sin software adicional) |

> [!CAUTION]
> **TRAMPA 2025**: El único formato usable nativamente en Windows (>32GB) Y macOS es **ExFAT**. Respuesta: **a**.

---

## 13. VIRTUALIZACIÓN

### 13.1 Hipervisores
| Tipo | Características |
|------|----------------|
| **Tipo 1 (bare-metal)** | Se ejecuta **directamente sobre hardware** sin SO anfitrión. Ej: VMware ESXi, Hyper-V, KVM |
| **Tipo 2 (hosted)** | Se ejecuta como aplicación sobre un SO anfitrión. Ej: VirtualBox, VMware Workstation |

> [!CAUTION]
> **TRAMPA 2025**: Hipervisor tipo 1 = **sobre hardware físico sin SO anfitrión**. Respuesta: **b**.

### 13.2 Snapshot vs Backup
| Concepto | Definición |
|---------|-----------|
| **Snapshot** | Captura del **estado completo** en un momento específico. Depende del sistema original |
| **Backup** | Réplica exacta de datos con propósito de **restaurar** en caso de pérdida/daño |

### 13.3 Docker
| Comando | Función |
|---------|---------|
| `docker run` | **Crear e iniciar** un nuevo contenedor (descarga imagen si necesario) |
| `docker start` | Iniciar contenedor existente (ya parado) |
| `docker exec` | Ejecutar comando en contenedor **ya en ejecución** |
| `docker kill ID` | **Detener inmediatamente** un contenedor (SIGKILL) |
| `docker stop ID` | Parar contenedor gracefully (SIGTERM) |

> [!CAUTION]
> **TRAMPA 2025**: `docker run` = crear e iniciar (no `docker start` que es para contenedores parados). `docker kill` = parar inmediatamente. Respuestas: **a** y **a**.

### 13.4 Kubernetes — Plano de Control
| Componente | Función |
|-----------|---------|
| **kube-scheduler** | **Decide en qué nodo** ejecutar un Pod según recursos disponibles |
| kube-apiserver | Punto de entrada a la API del clúster |
| etcd | Almacén clave-valor con el estado del clúster |
| kube-controller-manager | Gestiona controladores (replicasets, deployments...) |

> [!CAUTION]
> **TRAMPA 2025**: El que decide dónde ejecutar un Pod = **kube-scheduler** (no etcd, no apiserver). Respuesta: **c**.

---

## 14. SEGURIDAD EN REDES

### 14.1 Bases de Datos de Vulnerabilidades
- **NVD** (National Vulnerability Database) = base de datos de vulnerabilidades ✅
- UTM = Unified Threat Management (dispositivo de seguridad de red)
- SCAP = Security Content Automation Protocol
- CVDB no existe como estándar conocido

### 14.2 Contraseñas Robustas — CCN-CERT
Requisitos para contraseña robusta:
- **Longitud mínima de 8 caracteres** (no 7)
- Mezcla de mayúsculas, minúsculas, números y símbolos
- NO incluir datos del usuario (nombre, fecha nacimiento)
- NO apuntar en papel accesible
- NO usar frases cortas sin sentido (preferir frases largas con sentido)

### 14.3 MFA — Autenticación Multi-Factor
**Factores de autenticación** (debe ser de distintas categorías):
| Factor | Tipo |
|--------|------|
| Contraseña/PIN | Algo que **sabes** |
| Token OTP | Algo que **tienes** |
| Huella dactilar | Algo que **eres** (biometría) |
| Escáner de iris | Algo que **eres** (biometría) |
| Tarjeta | Algo que **tienes** |

> [!CAUTION]
> **TRAMPA 2025**: **Escáner de Iris + Huella dactilar** = ambos son biometría (mismo factor "algo que eres") → NO es MFA. Los factores deben ser de categorías DISTINTAS. Respuesta: **b**.

---

## 15. RESUMEN DE RESPUESTAS CORRECTAS — SUPUESTOS 2025

### Supuesto I (EDUCA-DATA 2030) — TAI-L Modelo A
| Preg | Tema | Respuesta |
|------|------|-----------|
| 1 | Oracle UNIQUE | **b** (ALTER TABLE ADD CONSTRAINT UNIQUE) |
| 2 | INNER JOIN | **b** |
| 3 | GROUP BY COUNT | **c** |
| 4 | Spring Boot @RestController | **a** |
| 5 | JUnit assertEquals | **a** |
| 6 | mvn spring-boot:run | **c** |
| 7 | HTML5 bien formado | **b** |
| 8 | XML bien formado | **b** |
| 9 | JavaScript nativo | **d** |
| 10 | HTTP 201 Created | **b** |
| 11 | WCAG semántica HTML5 | **c** |
| 12 | OWASP XSS prevención | **a** |

### Supuesto II (CPD SGTIC) — TAI-P Modelo A
| Preg | Tema | Respuesta |
|------|------|-----------|
| 1 | Subred /25 | **d** (10.30.16.0 y 10.30.16.127) |
| 2 | Hosts /20 | **c** (4094) |
| 3 | DHCP relay Cisco | **a** (ip helper-address) |
| 4 | ip route show Linux | **c** |
| 5 | systemctl enable | **a** |
| 6 | docker kill | **a** |
| 7 | ip route get | **b** |
| 8 | ss -ltn | **d** |
| 9 | Estrategia 3-2-1 | **c** (3 copias, 2 soportes distintos, 1 fuera) |
| 10 | tar -czf | **b** |
| 11 | dsa.msc AD | **a** |
| 12 | Copy-Item PowerShell | **c** |

---

*Última actualización: Octubre 2026 — Basado en exámenes oficiales TAI 2022, 2024, 2025*
