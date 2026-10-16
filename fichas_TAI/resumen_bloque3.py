# -*- coding: utf-8 -*-
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from temario.models import Bloque, Tema


# ============================================================
# TEMA 1 - Metodologias de desarrollo de software
# ============================================================
Tema.objects.filter(bloque__numero=3, numero=1).update(resumen_estudio="""1. CONCEPTO DE METODOLOGIA DE DESARROLLO DE SOFTWARE

Una metodologia de desarrollo de software es un conjunto estructurado de practicas, tecnicas y herramientas que guian el proceso de construccion de un sistema informatico desde su concepcion hasta su puesta en produccion. Su objetivo es garantizar la calidad del producto, controlar los plazos y costes, y facilitar el trabajo en equipo.

Las metodologias se clasifican en dos grandes familias: las metodologias tradicionales (predictivas o en cascada), que planifican el proyecto de forma exhaustiva al inicio, y las metodologias agiles (adaptativas), que responden al cambio de forma iterativa e incremental.

2. METRICA v3: CONCEPTO Y ESTRUCTURA

METRICA v3 es la metodologia oficial de la Administracion General del Estado para el desarrollo y mantenimiento de sistemas de informacion. Fue publicada por el Ministerio de Administraciones Publicas y es de aplicacion obligatoria en los proyectos TIC de la AGE.

DATO CLAVE: METRICA v3 cubre los paradigmas estructurado y orientado a objetos, y es aplicable al desarrollo de software, mantenimiento y planificacion de sistemas de informacion.

Los procesos principales de METRICA v3 son cinco:

- PSI (Planificacion de Sistemas de Informacion): define el marco de desarrollo de los sistemas de informacion de una organizacion. Establece la arquitectura tecnologica y el plan de accion.
- EVS (Estudio de Viabilidad del Sistema): analiza si el proyecto es viable tecnica, economica y operacionalmente. Su producto es el Estudio de Viabilidad.
- ASI (Analisis del Sistema de Informacion): define el catalogo de requisitos del sistema y los modelos de analisis. Produce el Documento de Analisis.
- DSI (Diseno del Sistema de Informacion): especifica la arquitectura del sistema, el diseno de la base de datos y los modulos. Produce el Documento de Diseno.
- CSI (Construccion del Sistema de Informacion): genera el codigo fuente, los procedimientos de migracion y los manuales. Produce el software construido.
- IAS (Implantacion y Aceptacion del Sistema): realiza las pruebas de aceptacion, la formacion y la puesta en produccion. Produce el Sistema en Produccion.

DATO CLAVE: Las interfaces transversales de METRICA v3 son tres: Gestion de Proyectos (GP), Seguridad (SEG) y Aseguramiento de Calidad (CAL). Son transversales porque aplican a todos los procesos principales.

3. CICLO DE VIDA DEL SOFTWARE

El ciclo de vida del software describe las fases que atraviesa un sistema desde su concepcion hasta su retirada. Los modelos mas relevantes son:

- Modelo en cascada: las fases se ejecutan secuencialmente (requisitos, diseno, implementacion, pruebas, mantenimiento). No permite retrocesos, lo que lo hace rigido.
- Modelo en espiral: combina el desarrollo iterativo con el analisis de riesgos en cada ciclo. Propuesto por Boehm.
- Modelo iterativo e incremental: el sistema se construye en incrementos funcionales. Cada iteracion entrega un producto parcial operativo.
- Modelo en V: asocia cada fase de desarrollo con su fase de pruebas correspondiente (verificacion y validacion).

4. METODOLOGIAS AGILES: MANIFIESTO AGIL

El Manifiesto Agil fue publicado en 2001 por 17 expertos en desarrollo de software. Establece 4 valores fundamentales:

- Individuos e interacciones sobre procesos y herramientas.
- Software funcionando sobre documentacion exhaustiva.
- Colaboracion con el cliente sobre negociacion contractual.
- Respuesta ante el cambio sobre seguimiento de un plan.

DATO CLAVE: El Manifiesto Agil tiene 4 valores y 12 principios. El primer principio establece que la maxima prioridad es satisfacer al cliente mediante la entrega temprana y continua de software con valor.

5. FRAMEWORK SCRUM

Scrum es el framework agil mas extendido. Se basa en ciclos de trabajo llamados Sprints (iteraciones de 1 a 4 semanas) que producen un incremento de producto potencialmente entregable.

Roles de Scrum:
- Product Owner (PO): es el responsable del producto y gestiona el Product Backlog. Prioriza los elementos segun el valor de negocio.
- Scrum Master (SM): es el facilitador del proceso. Elimina impedimentos y protege al equipo. No es jefe de proyecto.
- Equipo de Desarrollo: equipo autoorganizado y multifuncional de entre 3 y 9 miembros que construye el incremento.

Eventos de Scrum:
- Sprint Planning: reunion al inicio del Sprint para seleccionar elementos del backlog y crear el Sprint Backlog.
- Daily Scrum: reunion diaria de 15 minutos para sincronizar el trabajo del equipo.
- Sprint Review: revision del incremento al final del Sprint con el Product Owner y stakeholders.
- Sprint Retrospective: el equipo reflexiona sobre su proceso de trabajo para mejorar.

Artefactos de Scrum:
- Product Backlog: lista ordenada de todo lo que podria necesitar el producto.
- Sprint Backlog: subconjunto del Product Backlog seleccionado para el Sprint en curso.
- Incremento: suma de todos los elementos del Product Backlog completados durante el Sprint.

DATO CLAVE: En Scrum, el Sprint tiene una duracion fija (time-box) de entre 1 y 4 semanas. El Daily Scrum dura exactamente 15 minutos (time-box).

6. KANBAN

Kanban es un metodo agil de gestion del flujo de trabajo originado en el sistema de produccion de Toyota. Se basa en la visualizacion del trabajo, la limitacion del trabajo en curso (WIP - Work In Progress) y la mejora continua del flujo.

Sus principios fundamentales son:
- Visualizar el flujo de trabajo mediante un tablero con columnas (Pendiente, En Proceso, Terminado).
- Limitar el WIP para evitar la sobrecarga del equipo y detectar cuellos de botella.
- Gestionar el flujo midiendo el tiempo de ciclo (cycle time) y el tiempo de entrega (lead time).
- Mejora continua (Kaizen).

A diferencia de Scrum, Kanban no tiene roles definidos, ni iteraciones fijas, ni eventos obligatorios. Es un metodo de gestion del flujo continuo.

PREGUNTAS TIPO EXAMEN INAP:

1. Segun METRICA v3, el proceso que define la arquitectura de los sistemas de informacion de una organizacion y establece el plan de accion es:
a) EVS  b) PSI  c) ASI  d) DSI
Respuesta correcta: b) PSI

2. Las interfaces transversales de METRICA v3 son:
a) PSI, EVS y ASI  b) DSI, CSI e IAS  c) Gestion de Proyectos, Seguridad y Aseguramiento de Calidad  d) Analisis, Diseno y Construccion
Respuesta correcta: c) Gestion de Proyectos, Seguridad y Aseguramiento de Calidad

3. En el framework Scrum, el responsable de gestionar y priorizar el Product Backlog es:
a) Scrum Master  b) Equipo de Desarrollo  c) Product Owner  d) Project Manager
Respuesta correcta: c) Product Owner

4. En Kanban, la practica de limitar el numero de tareas en proceso simultaneamente se denomina:
a) Sprint Backlog  b) Time-box  c) WIP (Work In Progress)  d) Velocity
Respuesta correcta: c) WIP (Work In Progress)
""")

# ============================================================
# TEMA 2 - Analisis y diseno orientado a objetos: UML
# ============================================================
Tema.objects.filter(bloque__numero=3, numero=2).update(resumen_estudio="""1. PARADIGMA ORIENTADO A OBJETOS

El paradigma orientado a objetos (OOP) organiza el software en torno a objetos que combinan datos (atributos) y comportamiento (metodos). Surgio como respuesta a la complejidad creciente del software y es el paradigma dominante en el desarrollo moderno de aplicaciones.

Los conceptos fundamentales de OOP son:

- Clase: plantilla o molde que define los atributos y metodos comunes a un conjunto de objetos. Es la unidad basica del diseno OOP.
- Objeto: instancia concreta de una clase. Tiene estado (valores de sus atributos), comportamiento (metodos) e identidad (referencia unica).
- Encapsulamiento: mecanismo que oculta los detalles internos de un objeto y expone solo una interfaz publica. Se implementa con modificadores de acceso (public, private, protected).
- Herencia: mecanismo por el que una clase (subclase o clase hija) adquiere los atributos y metodos de otra clase (superclase o clase padre). Permite la reutilizacion de codigo.
- Polimorfismo: capacidad de un objeto de tomar multiples formas. Permite tratar objetos de distintas subclases de forma uniforme a traves de la interfaz de la superclase.
- Abstraccion: proceso de identificar las caracteristicas esenciales de un objeto, ignorando los detalles irrelevantes.

DATO CLAVE: Los cuatro pilares del OOP son Encapsulamiento, Herencia, Polimorfismo y Abstraccion (acronimo: EHPA).

2. LENGUAJE DE MODELADO UNIFICADO (UML)

UML (Unified Modeling Language) es el lenguaje estandar de la industria para visualizar, especificar, construir y documentar los artefactos de un sistema software. Fue desarrollado por Grady Booch, Ivar Jacobson y James Rumbaugh (los "Tres Amigos") y es mantenido por el Object Management Group (OMG).

DATO CLAVE: UML es un lenguaje de modelado, NO una metodologia. No prescribe como hacer el analisis o diseno, sino como representarlo. La version actual es UML 2.x.

Los diagramas UML se clasifican en dos grandes categorias:

3. DIAGRAMAS ESTRUCTURALES UML

Representan la estructura estatica del sistema (que elementos existen y como se relacionan):

- Diagrama de Clases: es el diagrama mas importante del analisis y diseno OOP. Muestra las clases del sistema, sus atributos, metodos y las relaciones entre ellas (asociacion, agregacion, composicion, herencia, dependencia). Es el nucleo del modelo de analisis en METRICA v3 ASI.
- Diagrama de Componentes: muestra la organizacion y dependencias entre componentes fisicos del software (modulos, librerias, ejecutables). Util para el diseno fisico de la arquitectura.
- Diagrama de Despliegue: representa la arquitectura fisica del sistema: nodos hardware (servidores, dispositivos) y como se distribuyen los componentes software en ellos.
- Diagrama de Objetos: muestra instancias concretas de clases en un momento dado. Es una "fotografia" del sistema en ejecucion.
- Diagrama de Paquetes: organiza los elementos del modelo en grupos logicos llamados paquetes.

4. DIAGRAMAS DE COMPORTAMIENTO UML

Representan el comportamiento dinamico del sistema (como cambia a lo largo del tiempo):

- Diagrama de Casos de Uso: muestra las interacciones entre los actores (usuarios o sistemas externos) y el sistema. Captura los requisitos funcionales desde el punto de vista del usuario. Los actores se representan como figuras humanas ("stick men") y los casos de uso como elipses.
- Diagrama de Secuencia: muestra la interaccion entre objetos a lo largo del tiempo, enfatizando el orden temporal de los mensajes. Es el diagrama de interaccion mas utilizado. Los objetos se situan en el eje horizontal y el tiempo avanza en el eje vertical.
- Diagrama de Actividades: representa el flujo de trabajo o algoritmo de un proceso. Similar a un diagrama de flujo, pero con semantica de concurrencia (bifurcaciones y uniones paralelas).
- Diagrama de Estados (Maquina de Estados): muestra los estados por los que pasa un objeto a lo largo de su vida y las transiciones entre estados provocadas por eventos.
- Diagrama de Comunicacion: similar al de secuencia pero enfatizando las relaciones entre objetos en lugar del orden temporal.

DATO CLAVE: El Diagrama de Casos de Uso captura los REQUISITOS FUNCIONALES. El Diagrama de Clases es el artefacto central del DISENO OOP. El Diagrama de Secuencia modela la INTERACCION entre objetos en el tiempo.

5. CONTROL DE VERSIONES CON GIT

Git es un sistema de control de versiones distribuido (DVCS). En un DVCS, cada desarrollador tiene una copia completa del repositorio en su maquina local (incluyendo todo el historial).

Conceptos clave de Git:
- Repositorio (repo): almacen de todos los archivos y su historial de cambios.
- Commit: instantanea del estado del repositorio en un momento dado. Cada commit tiene un identificador SHA-1 unico.
- Branch (rama): linea de desarrollo independiente. La rama principal suele llamarse main o master.
- Merge: integracion de los cambios de una rama en otra.
- Rebase: reorganizacion del historial de commits de una rama, aplicandolos sobre la punta de otra rama.
- Pull Request / Merge Request: solicitud de integracion de cambios revisada por pares antes de fusionarse.

DATO CLAVE: En Git, el area de preparacion previa al commit se llama Staging Area o Index. El comando git add mueve cambios al Staging Area y git commit los registra en el repositorio local.

6. UML EN METRICA v3

METRICA v3 utiliza UML en sus procesos de analisis y diseno orientado a objetos. En el proceso ASI (Analisis), los productos principales incluyen el Modelo de Casos de Uso y el Modelo de Analisis (diagrama de clases de analisis). En el proceso DSI (Diseno), se elaboran los diagramas de componentes y despliegue.

PREGUNTAS TIPO EXAMEN INAP:

1. El diagrama UML que representa los requisitos funcionales del sistema desde el punto de vista del usuario es:
a) Diagrama de Clases  b) Diagrama de Secuencia  c) Diagrama de Casos de Uso  d) Diagrama de Despliegue
Respuesta correcta: c) Diagrama de Casos de Uso

2. Los creadores del lenguaje UML son conocidos como "los Tres Amigos". Son:
a) Booch, Jacobson y Rumbaugh  b) Beck, Fowler y Martin  c) Stroustrup, Gosling y Torvalds  d) Gamma, Helm y Johnson
Respuesta correcta: a) Booch, Jacobson y Rumbaugh

3. El pilar del OOP que permite ocultar los detalles internos de un objeto exponiendo solo una interfaz publica es:
a) Herencia  b) Polimorfismo  c) Abstraccion  d) Encapsulamiento
Respuesta correcta: d) Encapsulamiento

4. En Git, el area intermedia donde se preparan los cambios antes de realizar un commit se denomina:
a) Working Directory  b) Staging Area o Index  c) Remote Repository  d) Stash
Respuesta correcta: b) Staging Area o Index
""")

# ============================================================
# TEMA 3 - Patrones de diseno de software (GoF) y arquitecturas
# ============================================================
Tema.objects.filter(bloque__numero=3, numero=3).update(resumen_estudio="""1. CONCEPTO DE PATRON DE DISENO

Un patron de diseno es una solucion reutilizable a un problema recurrente en el diseno de software orientado a objetos. No es codigo directamente ejecutable, sino una descripcion o plantilla de como resolver un tipo de problema que puede aplicarse en distintos contextos.

Los patrones de diseno mas influyentes fueron catalogados por el "Gang of Four" (GoF): Erich Gamma, Richard Helm, Ralph Johnson y John Vlissides, en su libro "Design Patterns: Elements of Reusable Object-Oriented Software" (1994). Definieron 23 patrones clasificados en tres categorias: creacionales, estructurales y de comportamiento.

DATO CLAVE: Los autores del catalogo de 23 patrones GoF son conocidos como el "Gang of Four" (Banda de los Cuatro): Gamma, Helm, Johnson y Vlissides.

2. PATRONES CREACIONALES

Los patrones creacionales abstraen el proceso de instanciacion de objetos, haciendo que el sistema sea independiente de como se crean, componen y representan sus objetos.

- Singleton: garantiza que una clase tenga una unica instancia y proporciona un punto de acceso global a ella. Se usa para recursos compartidos como conexiones a bases de datos, ficheros de configuracion o logs. Implementacion: constructor privado + metodo estatico getInstance().

- Factory Method: define una interfaz para crear un objeto, pero deja que las subclases decidan que clase instanciar. La superclase delega la creacion a las subclases.

- Abstract Factory: proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas. Crea "fabricas de fabricas".

- Builder: separa la construccion de un objeto complejo de su representacion, de modo que el mismo proceso de construccion pueda crear distintas representaciones. Util para objetos con muchos parametros opcionales.

DATO CLAVE: Singleton = 1 sola instancia. Factory Method = subclases deciden que instanciar. Abstract Factory = familias de objetos relacionados. Builder = construccion paso a paso de objetos complejos.

3. PATRONES ESTRUCTURALES

Los patrones estructurales se ocupan de como se componen clases y objetos para formar estructuras mas grandes.

- Adapter (Adaptador): convierte la interfaz de una clase en otra interfaz que el cliente espera. Permite que clases con interfaces incompatibles trabajen juntas. Es como un "enchufe adaptador".

- Composite (Composicion): permite tratar objetos individuales y composiciones de objetos de manera uniforme. Organiza los objetos en estructuras de arbol para representar jerarquias parte-todo (ej: sistema de ficheros, menus anidados).

- Decorator (Decorador): adjunta responsabilidades adicionales a un objeto de forma dinamica. Proporciona una alternativa flexible a la herencia para extender funcionalidades.

- Facade (Fachada): proporciona una interfaz simplificada a un conjunto complejo de clases, una libreria o un subsistema. Oculta la complejidad interna.

- Proxy: proporciona un sustituto o representante de otro objeto para controlar el acceso a el. Variantes: Proxy remoto (acceso a objeto en otro proceso), Proxy virtual (creacion perezosa), Proxy de proteccion (control de acceso).

DATO CLAVE: Adapter = adapta interfaces incompatibles. Facade = simplifica interfaz de subsistema complejo. Decorator = anade funcionalidad dinamicamente sin herencia. Proxy = controla acceso a otro objeto.

4. PATRONES DE COMPORTAMIENTO

Los patrones de comportamiento se ocupan de la comunicacion y responsabilidades entre objetos.

- Observer (Observador): define una dependencia de uno a muchos entre objetos, de modo que cuando un objeto cambia de estado, todos sus dependientes son notificados automaticamente. Patron fundamental para la programacion orientada a eventos y el patron Publicador/Suscriptor (Pub/Sub).

- Strategy (Estrategia): define una familia de algoritmos, encapsula cada uno de ellos y los hace intercambiables. Permite que el algoritmo varie independientemente de los clientes que lo usan. Ej: distintas estrategias de ordenacion o de calculo de impuestos.

- Command (Comando): encapsula una solicitud como un objeto, permitiendo parametrizar clientes con distintas operaciones, encolar operaciones, registrar logs y soportar operaciones reversibles (undo/redo).

- Iterator (Iterador): proporciona una forma de acceder secuencialmente a los elementos de un objeto agregado sin exponer su representacion subyacente.

DATO CLAVE: Observer = notificacion de cambios (uno a muchos). Strategy = algoritmos intercambiables. Command = encapsula operaciones como objetos (permite undo). Iterator = recorre colecciones sin exponer su estructura interna.

5. PATRONES ARQUITECTONICOS

Los patrones arquitectonicos operan a un nivel de abstraccion mayor que los patrones GoF, definiendo la organizacion global del sistema.

- MVC (Modelo-Vista-Controlador): separa la aplicacion en tres componentes:
  * Modelo: gestiona los datos, la logica de negocio y las reglas del dominio. Notifica a las vistas cuando cambia.
  * Vista: presenta los datos al usuario. Es la interfaz de usuario.
  * Controlador: recibe la entrada del usuario, la procesa e interactua con el Modelo para actualizar la Vista.
  El patron MVC favorece la separacion de responsabilidades y la testabilidad. Es la base de frameworks como Django (MVT), Spring MVC y Ruby on Rails.

DATO CLAVE: En Django se usa una variante llamada MVT (Modelo-Vista-Template) donde el "Template" equivale a la Vista de MVC y la "Vista" de Django equivale al Controlador de MVC.

- Microservicios: arquitectura en la que la aplicacion se construye como un conjunto de servicios pequenos, independientes y desplegables por separado, cada uno con su propia logica de negocio y base de datos. Se comunican mediante APIs (tipicamente REST o mensajeria asincrona). Ventajas: escalabilidad independiente, tecnologia heterogenea, resiliencia. Desventajas: mayor complejidad operacional, latencia de red, gestion de consistencia distribuida.

- Arquitectura en capas (N-tier): organiza el sistema en capas horizontales (Presentacion, Logica de Negocio, Acceso a Datos) con dependencias unidireccionales de arriba a abajo.

- Arquitectura orientada a eventos (Event-Driven): los componentes se comunican mediante la produccion y consumo de eventos. Muy usada en sistemas de alta concurrencia y microservicios.

PREGUNTAS TIPO EXAMEN INAP:

1. El patron de diseno GoF que garantiza que una clase tenga una unica instancia en todo el sistema es:
a) Factory Method  b) Builder  c) Singleton  d) Prototype
Respuesta correcta: c) Singleton

2. El patron GoF que convierte la interfaz de una clase en otra interfaz esperada por el cliente, permitiendo trabajar a clases con interfaces incompatibles, es:
a) Facade  b) Proxy  c) Decorator  d) Adapter
Respuesta correcta: d) Adapter

3. En el patron MVC, el componente responsable de gestionar los datos y la logica de negocio es:
a) Vista  b) Controlador  c) Modelo  d) Repositorio
Respuesta correcta: c) Modelo

4. El patron de comportamiento que define una dependencia uno-a-muchos entre objetos, notificando automaticamente a todos los dependientes cuando el objeto cambia de estado, es:
a) Command  b) Strategy  c) Iterator  d) Observer
Respuesta correcta: d) Observer
""")

# ============================================================
# TEMA 4 - Lenguajes de programacion: paradigmas y entornos
# ============================================================
Tema.objects.filter(bloque__numero=3, numero=4).update(resumen_estudio="""1. PARADIGMAS DE PROGRAMACION

Un paradigma de programacion es un modelo o estilo fundamental de programacion que proporciona el marco conceptual para construir programas. Los lenguajes modernos suelen ser multiparadigma.

- Paradigma imperativo: el programador especifica COMO debe ejecutarse el programa, mediante una secuencia de instrucciones que modifican el estado del programa. Es el paradigma mas clasico. Incluye la programacion procedural (C, Pascal) y la orientada a objetos.

- Paradigma orientado a objetos (OOP): organiza el software en objetos que combinan datos y comportamiento. Soporta encapsulamiento, herencia y polimorfismo. Lenguajes: Java, C++, C#, Python, Ruby.

- Paradigma funcional: trata la computacion como la evaluacion de funciones matematicas. Evita el estado mutable y los efectos secundarios. Las funciones son ciudadanos de primera clase (pueden pasarse como argumentos, retornarse como valores). Conceptos clave: funciones puras, inmutabilidad, funciones de orden superior (map, filter, reduce). Lenguajes: Haskell, Erlang, Clojure. Soporte funcional en: Python, Java 8+, JavaScript, Scala.

- Paradigma declarativo: el programador especifica QUE debe obtenerse, no como. SQL es el ejemplo mas conocido. Incluye la programacion logica (Prolog).

DATO CLAVE: Los tres paradigmas principales son Imperativo, Orientado a Objetos y Funcional. Python es multiparadigma: soporta imperativo, OOP y funcional. SQL es declarativo.

2. COMPILADORES, INTERPRETES, BYTECODE Y MAQUINAS VIRTUALES

El proceso de traduccion del codigo fuente a codigo ejecutable puede seguir distintos modelos:

- Compilador: traduce el codigo fuente completo a codigo maquina (binario nativo) antes de la ejecucion. El resultado es un ejecutable especifico para una plataforma. Ventaja: alta velocidad de ejecucion. Ej: GCC (C/C++), Rustc (Rust).

- Interprete: traduce y ejecuta el codigo fuente linea a linea en tiempo de ejecucion, sin generar un ejecutable previo. Ventaja: portabilidad y facilidad de depuracion. Desventaja: menor rendimiento. Ej: CPython (interprete de Python), Ruby MRI.

- Bytecode y Maquinas Virtuales: modelo hibrido en dos fases. El compilador traduce el codigo fuente a un codigo intermedio (bytecode) independiente de la plataforma. Luego, una maquina virtual (VM) interpreta o compila JIT (Just-In-Time) el bytecode en la plataforma destino. Ventaja: portabilidad + rendimiento.

DATO CLAVE: Java compila a bytecode (.class) que ejecuta la JVM (Java Virtual Machine). El bytecode de Python genera archivos .pyc. El lema historico de Java es "Write Once, Run Anywhere" (WORA) gracias a la JVM.

3. LENGUAJES MODERNOS Y SUS ENTORNOS

- Java: lenguaje OOP compilado a bytecode ejecutado por la JVM (Java Virtual Machine). Fuertemente tipado, con recoleccion de basura automatica. Muy usado en aplicaciones empresariales (Spring Framework), Android y sistemas distribuidos. Version LTS actual: Java 21.

- Python: lenguaje interpretado, multiparadigma, con tipado dinamico y fuerte. Destacado por su sintaxis clara y su enorme ecosistema de librerias (NumPy, Pandas, TensorFlow, Django). Muy usado en ciencia de datos, IA, automatizacion y desarrollo web. El interprete de referencia es CPython.

- C#: lenguaje OOP de Microsoft, compilado a bytecode CIL (Common Intermediate Language) que ejecuta el CLR (Common Language Runtime), la maquina virtual de .NET. Similar a Java en arquitectura. Usado principalmente en entornos Windows y juegos (Unity).

- JavaScript/TypeScript: JavaScript es el unico lenguaje nativo de los navegadores web. TypeScript es un superconjunto de JavaScript con tipado estatico opcional, desarrollado por Microsoft. Ambos se ejecutan en motores JavaScript (V8 de Google en Chrome y Node.js). Node.js lleva JavaScript al lado del servidor.

- PHP: lenguaje interpretado del lado del servidor, diseñado especificamente para desarrollo web. Ejecutado por el motor Zend. Usado en sistemas de gestion de contenidos como WordPress, Drupal y Joomla.

DATO CLAVE: Java -> JVM. C# -> CLR (.NET). JavaScript del lado del servidor -> Node.js (motor V8). Python -> CPython (interprete de referencia). TypeScript transpila a JavaScript antes de ejecutarse.

4. GESTION DE MEMORIA Y GARBAGE COLLECTION

La gestion de memoria es uno de los aspectos criticos de los lenguajes de programacion:

- Gestion manual: el programador reserva y libera memoria explicitamente (malloc/free en C, new/delete en C++). Mayor control y rendimiento, pero propenso a errores: fugas de memoria (memory leaks) y acceso a memoria ya liberada (dangling pointers).

- Gestion automatica - Garbage Collection (GC): el entorno de ejecucion detecta y libera automaticamente los objetos que ya no son alcanzables (no tienen referencias). Simplifica el desarrollo y evita fugas de memoria.

Algoritmos principales de GC:
- Conteo de referencias: cada objeto mantiene un contador de referencias que apuntan a el. Cuando llega a 0, el objeto se libera. Problema: no detecta referencias circulares. Usado en CPython (complementado con GC ciclico).
- Mark-and-Sweep (Marcar y Barrer): el GC recorre el grafo de objetos marcando los alcanzables, luego libera los no marcados. Detecta referencias circulares. Usado en JVM y .NET CLR.
- Generational GC (GC generacional): divide el heap en generaciones (joven, media, vieja). La mayoria de objetos mueren joven (hipotesis generacional). El GC recolecta la generacion joven con mas frecuencia. Optimizacion usada en JVM, .NET y CPython.

DATO CLAVE: CPython usa conteo de referencias como mecanismo principal de GC, complementado con un detector de ciclos. La JVM usa GC generacional (Mark-and-Sweep generacional). Lenguajes como Rust gestionan la memoria sin GC mediante el sistema de Ownership y Borrowing en tiempo de compilacion.

5. TIPADO DE LENGUAJES

- Tipado estatico: los tipos se verifican en tiempo de compilacion. Mayor seguridad y rendimiento. Ej: Java, C#, C++, TypeScript.
- Tipado dinamico: los tipos se verifican en tiempo de ejecucion. Mayor flexibilidad. Ej: Python, JavaScript, Ruby, PHP.
- Tipado fuerte: no permite conversiones implicitas entre tipos incompatibles. Ej: Python, Java.
- Tipado debil: permite conversiones implicitas (coercion). Ej: JavaScript, PHP.

PREGUNTAS TIPO EXAMEN INAP:

1. El mecanismo por el que Java consigue portabilidad entre plataformas es:
a) La compilacion a codigo maquina nativo  b) La compilacion a bytecode ejecutado por la JVM  c) La interpretacion linea a linea del codigo fuente  d) El uso del motor V8
Respuesta correcta: b) La compilacion a bytecode ejecutado por la JVM

2. El interprete de referencia del lenguaje Python se denomina:
a) PyPy  b) Jython  c) CPython  d) IronPython
Respuesta correcta: c) CPython

3. Un algoritmo de Garbage Collection que divide el heap en regiones segun la edad de los objetos es:
a) Conteo de referencias  b) Mark-and-Sweep simple  c) GC generacional  d) Reference counting
Respuesta correcta: c) GC generacional

4. TypeScript es:
a) Un lenguaje completamente independiente de JavaScript  b) Un superconjunto de JavaScript con tipado estatico opcional  c) El lenguaje de programacion de la maquina virtual .NET  d) Un framework de JavaScript para el desarrollo de interfaces de usuario
Respuesta correcta: b) Un superconjunto de JavaScript con tipado estatico opcional
""")

# ============================================================
# TEMA 5 - Bases de datos relacionales: Modelo Relacional
# ============================================================
Tema.objects.filter(bloque__numero=3, numero=5).update(resumen_estudio="""1. EL MODELO RELACIONAL: CONCEPTO Y ORIGEN

El modelo relacional fue propuesto por Edgar Frank Codd en 1970 en su articulo "A Relational Model of Data for Large Shared Data Banks". Se basa en la teoria matematica de las relaciones y el algebra relacional. Es el modelo subyacente de todos los SGBD relacionales (Oracle, PostgreSQL, MySQL, SQL Server).

DATO CLAVE: El modelo relacional fue definido por E.F. Codd en 1970. Sus doce reglas (Reglas de Codd) definen los requisitos que debe cumplir un SGBD para considerarse plenamente relacional.

2. CONCEPTOS FUNDAMENTALES DEL MODELO RELACIONAL

- Relacion (Tabla): estructura bidimensional compuesta de filas y columnas que representa un conjunto de entidades o asociaciones. En el modelo relacional formal se llama relacion; en la implementacion practica se llama tabla.
- Tupla (Fila/Registro): cada fila de la tabla representa una instancia concreta de la entidad. En la relacion formal se llama tupla.
- Atributo (Columna): cada columna de la tabla representa una propiedad de la entidad. Tiene un nombre y un dominio (conjunto de valores posibles).
- Dominio: conjunto de valores atomicos permitidos para un atributo (ej: enteros positivos, cadenas de texto de hasta 50 caracteres).
- Valor NULL: representacion de la ausencia de valor o de informacion desconocida. Distinto de cero o cadena vacia.

DATO CLAVE: La correspondencia terminologica es: Relacion = Tabla; Tupla = Fila/Registro; Atributo = Columna. El numero de tuplas es la cardinalidad; el numero de atributos es el grado de la relacion.

3. CLAVES EN EL MODELO RELACIONAL

- Superclave: cualquier conjunto de atributos que identifica de forma unica cada tupla de la relacion.
- Clave candidata: superclave minimal (no tiene subconjuntos propios que sean superclaves). Una relacion puede tener varias claves candidatas.
- Clave primaria (Primary Key, PK): la clave candidata elegida por el disenador como identificador principal de la tabla. Debe ser unica y no nula (NOT NULL). Una tabla solo puede tener una PK.
- Clave alternativa: clave candidata que no fue elegida como clave primaria.
- Clave foranea (Foreign Key, FK): atributo o conjunto de atributos en una tabla que hace referencia a la clave primaria de otra tabla (o de la misma). Implementa las asociaciones entre tablas y garantiza la integridad referencial.

4. INTEGRIDAD DE DATOS

Las restricciones de integridad garantizan la coherencia y validez de los datos:

- Integridad de entidad: la clave primaria de cualquier tabla no puede contener valores NULL. Toda tupla debe ser identificable de forma unica.
- Integridad referencial: si una tabla B tiene una clave foranea que referencia a la tabla A, entonces cada valor de esa FK debe existir como valor de la PK en la tabla A, o bien ser NULL. Impide las "referencias huerfanas".
- Integridad de dominio: los valores de cada atributo deben pertenecer al dominio definido para ese atributo.
- Integridad definida por el usuario: restricciones adicionales definidas segun las reglas de negocio (CHECK, UNIQUE, NOT NULL).

DATO CLAVE: Integridad de ENTIDAD = la PK no puede ser NULL. Integridad REFERENCIAL = los valores de la FK deben existir en la tabla referenciada (o ser NULL).

5. NORMALIZACION: FORMAS NORMALES

La normalizacion es el proceso de organizar las tablas de una base de datos para reducir la redundancia de datos y evitar anomalias de actualizacion, insercion y borrado. Se basa en el concepto de dependencia funcional.

Dependencia funcional: el atributo B depende funcionalmente del atributo A (A -> B) si para cada valor de A existe exactamente un valor de B.

- Primera Forma Normal (1FN): una tabla esta en 1FN si todos sus atributos contienen valores atomicos (indivisibles) y no existen grupos repetitivos. Cada celda contiene un unico valor.

- Segunda Forma Normal (2FN): una tabla esta en 2FN si esta en 1FN y todos los atributos no clave dependen funcionalmente de la TOTALIDAD de la clave primaria (no de una parte de ella). Solo es relevante cuando la PK es compuesta. Elimina las dependencias parciales.

- Tercera Forma Normal (3FN): una tabla esta en 3FN si esta en 2FN y no existen dependencias transitivas: ningun atributo no clave depende de otro atributo no clave. Elimina las dependencias transitivas.

- Forma Normal de Boyce-Codd (BCNF o 3.5FN): es una version mas estricta de la 3FN. Una tabla esta en BCNF si para cada dependencia funcional X -> Y, X es una superclave. Elimina anomalias que la 3FN no cubre cuando hay multiples claves candidatas solapadas.

DATO CLAVE: 1FN = valores atomicos. 2FN = sin dependencias parciales de la PK. 3FN = sin dependencias transitivas. BCNF = todo determinante es superclave. La normalizacion hasta 3FN es el objetivo practico habitual.

6. ALGEBRA RELACIONAL

El algebra relacional es el lenguaje formal del modelo relacional. Define operaciones sobre relaciones que producen nuevas relaciones. SQL es su implementacion practica.

Operaciones fundamentales:
- Seleccion (sigma): filtra tuplas que satisfacen una condicion. Equivale a la clausula WHERE de SQL.
- Proyeccion (pi): selecciona un subconjunto de atributos (columnas). Equivale al SELECT de columnas en SQL.
- Union: combina las tuplas de dos relaciones compatibles (mismo esquema), eliminando duplicados.
- Diferencia: obtiene las tuplas que estan en la primera relacion pero no en la segunda.
- Producto cartesiano (x): combina cada tupla de la primera relacion con cada tupla de la segunda.
- Join (Combinacion): operacion derivada del producto cartesiano + seleccion. Combina tuplas de dos relaciones que satisfacen una condicion de join. El Natural Join combina automaticamente por los atributos con el mismo nombre.

DATO CLAVE: La Seleccion (sigma) opera sobre FILAS (como el WHERE de SQL). La Proyeccion (pi) opera sobre COLUMNAS (como el SELECT de SQL). El Join combina relaciones mediante una condicion.

PREGUNTAS TIPO EXAMEN INAP:

1. Una tabla de base de datos esta en Segunda Forma Normal (2FN) si:
a) No tiene valores NULL en ninguna columna  b) Esta en 1FN y todos los atributos no clave dependen de la totalidad de la clave primaria  c) Esta en 3FN y no tiene dependencias transitivas  d) Todos los atributos son atomicos
Respuesta correcta: b) Esta en 1FN y todos los atributos no clave dependen de la totalidad de la clave primaria

2. La restriccion de integridad que impide que la clave primaria de una tabla contenga valores NULL es:
a) Integridad referencial  b) Integridad de dominio  c) Integridad de entidad  d) Integridad definida por el usuario
Respuesta correcta: c) Integridad de entidad

3. En el algebra relacional, la operacion que filtra tuplas que satisfacen una condicion (equivalente al WHERE de SQL) es:
a) Proyeccion  b) Union  c) Seleccion  d) Join
Respuesta correcta: c) Seleccion

4. El modelo relacional fue propuesto por:
a) Peter Chen  b) James Martin  c) Edgar Frank Codd  d) Charles Bachman
Respuesta correcta: c) Edgar Frank Codd
""")

# ============================================================
# TEMA 6 - SQL: DDL, DML, DCL y TCL
# ============================================================
Tema.objects.filter(bloque__numero=3, numero=6).update(resumen_estudio="""1. CONCEPTO Y CLASIFICACION DE SQL

SQL (Structured Query Language) es el lenguaje estandar para la definicion, manipulacion y control de bases de datos relacionales. Fue desarrollado por IBM en los anos 70 (como SEQUEL) y estandarizado por ANSI/ISO. Los estandares mas relevantes son SQL-92, SQL:1999 (SQL3) y SQL:2003.

DATO CLAVE: SQL no distingue entre mayusculas y minusculas en las palabras reservadas (SELECT = select). El estandar actual es SQL:2016. Las sentencias SQL se clasifican en cuatro categorias: DDL, DML, DCL y TCL.

Las sentencias SQL se clasifican segun su funcion:
- DDL (Data Definition Language): definicion de la estructura de la base de datos.
- DML (Data Manipulation Language): manipulacion de los datos.
- DCL (Data Control Language): control de permisos y acceso.
- TCL (Transaction Control Language): control de transacciones.

2. SENTENCIAS DDL (DATA DEFINITION LANGUAGE)

Las sentencias DDL definen o modifican la estructura de los objetos de la base de datos (tablas, vistas, indices, esquemas). Sus cambios son permanentes e implicitos (ejecutan un COMMIT automatico en la mayoria de SGBD).

- CREATE TABLE: crea una nueva tabla con sus columnas, tipos de datos y restricciones.
  Ejemplo: CREATE TABLE Empleado (id INT PRIMARY KEY, nombre VARCHAR(100) NOT NULL, dept_id INT REFERENCES Departamento(id));

- ALTER TABLE: modifica la estructura de una tabla existente. Permite anadir columnas (ADD COLUMN), eliminarlas (DROP COLUMN) o modificarlas (MODIFY/ALTER COLUMN), asi como agregar o eliminar restricciones.

- DROP TABLE: elimina una tabla y todos sus datos permanentemente. Si existen FK que referencian a la tabla, puede dar error (a menos que se use CASCADE).

- TRUNCATE TABLE: elimina TODOS los registros de una tabla de forma rapida, pero mantiene la estructura de la tabla. A diferencia de DELETE, no genera logs por fila y no puede deshacerse con ROLLBACK en muchos SGBD.

DATO CLAVE: DDL = CREATE, ALTER, DROP, TRUNCATE. TRUNCATE elimina datos pero mantiene la estructura. DROP elimina la tabla completa. En la mayoria de SGBD, DDL ejecuta un COMMIT automatico implicito.

3. SENTENCIAS DML (DATA MANIPULATION LANGUAGE)

Las sentencias DML operan sobre los datos de las tablas y sus cambios pueden deshacerse con ROLLBACK (son transaccionales).

- SELECT: recupera datos de una o varias tablas. Es la sentencia mas compleja y utilizada de SQL.
  Estructura: SELECT [columnas] FROM [tablas] WHERE [condicion] GROUP BY [atributos] HAVING [condicion grupo] ORDER BY [atributos] [ASC|DESC] LIMIT [n];

- INSERT: inserta nuevas filas en una tabla.
  Ejemplo: INSERT INTO Empleado (id, nombre) VALUES (1, 'Ana Garcia');

- UPDATE: modifica los valores de filas existentes.
  Ejemplo: UPDATE Empleado SET nombre = 'Ana Lopez' WHERE id = 1;

- DELETE: elimina filas que cumplen una condicion. Si se omite el WHERE, elimina todas las filas (pero es recuperable con ROLLBACK, a diferencia de TRUNCATE).

4. CLAUSULAS DE CONSULTA SELECT

- WHERE: filtra filas segun una condicion logica. Admite operadores de comparacion (=, <, >, <>, BETWEEN, IN, LIKE, IS NULL).
- GROUP BY: agrupa filas por los valores de uno o mas atributos para aplicar funciones de agregacion (COUNT, SUM, AVG, MAX, MIN).
- HAVING: filtra GRUPOS (resultado de GROUP BY) segun una condicion. Es como el WHERE pero aplicado a grupos. Se ejecuta DESPUES del GROUP BY.
- ORDER BY: ordena el resultado por uno o mas atributos. Por defecto ascendente (ASC); se puede especificar DESC.

DATO CLAVE: Orden de ejecucion logico de SQL: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY. HAVING filtra grupos (tras GROUP BY); WHERE filtra filas (antes de GROUP BY). No se puede usar funciones de agregacion en WHERE.

5. TIPOS DE JOIN

Los JOIN combinan filas de dos o mas tablas basandose en una condicion relacionada:

- INNER JOIN (JOIN): devuelve solo las filas con correspondencia en AMBAS tablas.
- LEFT JOIN (LEFT OUTER JOIN): devuelve todas las filas de la tabla izquierda y las correspondencias de la derecha. Si no hay correspondencia, los campos de la tabla derecha son NULL.
- RIGHT JOIN (RIGHT OUTER JOIN): devuelve todas las filas de la tabla derecha y las correspondencias de la izquierda.
- FULL OUTER JOIN: devuelve todas las filas de ambas tablas, con NULL donde no hay correspondencia.
- CROSS JOIN: producto cartesiano; combina cada fila de la primera tabla con cada fila de la segunda.
- SELF JOIN: una tabla se une consigo misma (util para relaciones jerarquicas dentro de la misma tabla).

DATO CLAVE: INNER JOIN = solo coincidencias. LEFT JOIN = todas las de la izquierda + coincidencias de la derecha. FULL OUTER JOIN = todas las filas de ambas tablas.

6. SUBCONSULTAS

Una subconsulta (subquery) es una consulta SELECT anidada dentro de otra sentencia SQL. Puede usarse en:
- La clausula WHERE: SELECT * FROM E WHERE dept_id IN (SELECT id FROM D WHERE nombre = 'IT');
- La clausula FROM (tabla derivada): SELECT * FROM (SELECT dept_id, COUNT(*) as total FROM E GROUP BY dept_id) AS resumen;
- La clausula SELECT (subconsulta escalar): SELECT nombre, (SELECT nombre FROM D WHERE D.id = E.dept_id) FROM E;

7. SENTENCIAS DCL (DATA CONTROL LANGUAGE)

Gestionan los privilegios y permisos de acceso a los objetos de la base de datos:
- GRANT: otorga privilegios a un usuario o rol. Ej: GRANT SELECT, INSERT ON Empleado TO usuario1;
- REVOKE: revoca privilegios previamente otorgados. Ej: REVOKE INSERT ON Empleado FROM usuario1;

8. SENTENCIAS TCL (TRANSACTION CONTROL LANGUAGE)

Gestionan las transacciones en la base de datos:
- COMMIT: confirma y hace permanentes todos los cambios de la transaccion actual.
- ROLLBACK: deshace todos los cambios de la transaccion actual, volviendo al ultimo COMMIT o SAVEPOINT.
- SAVEPOINT: crea un punto de guardado dentro de una transaccion al que se puede volver con ROLLBACK.

DATO CLAVE: DCL = GRANT y REVOKE (permisos). TCL = COMMIT, ROLLBACK, SAVEPOINT (transacciones). Las sentencias DDL en la mayoria de SGBD hacen COMMIT automatico, por lo que no son reversibles con ROLLBACK.

PREGUNTAS TIPO EXAMEN INAP:

1. La clausula SQL que permite filtrar grupos de registros tras un GROUP BY, equivalente al WHERE pero para grupos, es:
a) ORDER BY  b) WHERE  c) HAVING  d) DISTINCT
Respuesta correcta: c) HAVING

2. El tipo de JOIN que devuelve todas las filas de la tabla izquierda y las correspondencias de la tabla derecha (con NULL donde no hay coincidencia) es:
a) INNER JOIN  b) RIGHT JOIN  c) FULL OUTER JOIN  d) LEFT JOIN
Respuesta correcta: d) LEFT JOIN

3. La sentencia SQL que elimina todos los registros de una tabla de forma rapida sin registrar las eliminaciones individuales y sin poder deshacerse con ROLLBACK (en la mayoria de SGBD) es:
a) DELETE  b) DROP  c) TRUNCATE  d) REMOVE
Respuesta correcta: c) TRUNCATE

4. Las sentencias SQL del grupo DCL son:
a) CREATE y DROP  b) COMMIT y ROLLBACK  c) GRANT y REVOKE  d) SELECT e INSERT
Respuesta correcta: c) GRANT y REVOKE
""")

# ============================================================
# TEMA 7 - SGBD Relacionales y Bases de Datos NoSQL
# ============================================================
Tema.objects.filter(bloque__numero=3, numero=7).update(resumen_estudio="""1. ARQUITECTURA ANSI-SPARC DE TRES NIVELES

La arquitectura ANSI-SPARC (propuesta en 1975 por el American National Standards Institute) define tres niveles de abstraccion en un SGBD para garantizar la independencia de datos:

- Nivel interno (fisico): describe como se almacenan fisicamente los datos en el disco (ficheros, indices, paginas). Es el nivel mas cercano al hardware. Solo lo gestionan los administradores de la base de datos.
- Nivel conceptual (logico): descripcion global de la estructura de toda la base de datos, independiente del almacenamiento fisico y de las aplicaciones. Define tablas, relaciones, restricciones e integridad. Es el modelo relacional.
- Nivel externo (de vistas): es el nivel mas cercano al usuario. Define las vistas parciales de la base de datos que perciben los distintos grupos de usuarios. Una vista es un subconjunto del nivel conceptual.

DATO CLAVE: Arquitectura ANSI-SPARC: Nivel INTERNO (fisico, disco) -> Nivel CONCEPTUAL (logico, esquema global) -> Nivel EXTERNO (vistas de usuario). La independencia logica aisla el nivel externo del conceptual; la independencia fisica aisla el conceptual del interno.

2. PROPIEDADES ACID DE LAS TRANSACCIONES

Una transaccion es una unidad logica de trabajo compuesta por una o varias operaciones que deben ejecutarse de forma atomica. Las propiedades ACID garantizan la fiabilidad de las transacciones:

- Atomicidad (Atomicity): la transaccion se ejecuta completamente o no se ejecuta en absoluto. Si falla alguna operacion, se deshacen todas las operaciones previas (ROLLBACK).
- Consistencia (Consistency): una transaccion lleva la base de datos de un estado consistente a otro estado consistente, respetando todas las restricciones de integridad.
- Aislamiento (Isolation): las transacciones concurrentes se ejecutan de forma aislada, como si fueran secuenciales. Los cambios de una transaccion no son visibles para otras hasta que se confirman con COMMIT.
- Durabilidad (Durability): una vez que una transaccion se confirma (COMMIT), sus cambios son permanentes, incluso ante fallos del sistema.

DATO CLAVE: Las propiedades ACID son Atomicidad, Consistencia, Aislamiento y Durabilidad. El acronimo en ingles es ACID: Atomicity, Consistency, Isolation, Durability.

3. NIVELES DE AISLAMIENTO

El estandar SQL define cuatro niveles de aislamiento que equilibran consistencia y rendimiento:
- READ UNCOMMITTED: nivel mas bajo. Permite leer datos no confirmados (dirty reads).
- READ COMMITTED: solo lee datos confirmados. Evita dirty reads. Es el nivel por defecto en Oracle y SQL Server.
- REPEATABLE READ: garantiza que si se lee una fila dos veces en la misma transaccion, el resultado es el mismo. Evita dirty reads y non-repeatable reads. Por defecto en MySQL/InnoDB.
- SERIALIZABLE: nivel mas alto. Las transacciones se ejecutan como si fueran completamente secuenciales. Evita todos los fenomenos (dirty reads, non-repeatable reads, phantom reads).

4. INDICES EN BASES DE DATOS

Un indice es una estructura de datos auxiliar que acelera la busqueda de registros en una tabla. Mejora el rendimiento de las consultas SELECT pero penaliza las operaciones de INSERT, UPDATE y DELETE (que deben mantener el indice actualizado).

- Indice B-Tree (Balanced Tree): el tipo mas comun. Organiza los valores de la clave en un arbol binario balanceado. Eficiente para busquedas de igualdad (=), rango (BETWEEN, <, >) y ordenacion (ORDER BY). Es el tipo por defecto en la mayoria de SGBD.
- Indice Hash: utiliza una funcion hash para mapear la clave a una posicion. Extremadamente rapido para busquedas de igualdad exacta (=), pero NO soporta busquedas por rango.
- Indice unico (UNIQUE): garantiza que no existen dos filas con el mismo valor indexado. Las claves primarias crean automaticamente un indice unico.

DATO CLAVE: Indice B-Tree = soporta igualdad Y rango. Indice Hash = solo igualdad exacta, mas rapido que B-Tree para igualdad. La PK crea automaticamente un indice unico en todos los SGBD relacionales.

5. SGBD RELACIONALES PRINCIPALES

- PostgreSQL: SGBD relacional de codigo abierto, considerado el mas avanzado en cumplimiento del estandar SQL. Soporta tipos de datos avanzados (JSON, arrays, tipos geometricos), transacciones ACID completas y extensibilidad mediante extensiones (PostGIS para datos geograficos). Licencia BSD.
- MySQL: el SGBD relacional de codigo abierto mas difundido en aplicaciones web. Actualmente propiedad de Oracle. El motor de almacenamiento principal es InnoDB (soporte ACID completo). El motor MyISAM no soporta transacciones.
- Oracle Database: el SGBD relacional comercial lider en entornos empresariales. Muy potente en rendimiento, escalabilidad y alta disponibilidad. Ampliamente usado en la Administracion Publica.
- Microsoft SQL Server: SGBD comercial de Microsoft integrado con el ecosistema Windows y Azure. Usa el lenguaje T-SQL (Transact-SQL) como extension de SQL.

6. BASES DE DATOS NoSQL

NoSQL (Not Only SQL) engloba sistemas de gestion de bases de datos que no utilizan el modelo relacional. Surgieron para gestionar grandes volumenes de datos (Big Data), alta concurrencia y estructuras de datos flexibles.

Caracteristicas generales: escala horizontal (sharding), esquema flexible o sin esquema, alta disponibilidad y tolerancia a particiones (modelo BASE en lugar de ACID).

DATO CLAVE: Teorema CAP (Brewer, 2000): un sistema distribuido solo puede garantizar simultaneamente 2 de las 3 propiedades: Consistencia (C), Disponibilidad/Availability (A) y Tolerancia a Particiones (P). Los SGBD NoSQL suelen sacrificar Consistencia a favor de A y P.

Tipos de bases de datos NoSQL:

- Documentales: almacenan datos como documentos semi-estructurados (tipicamente JSON o BSON). Schema-less: cada documento puede tener una estructura distinta. Principal representante: MongoDB. Casos de uso: CMS, catalogos de productos, perfiles de usuario.

- Clave-Valor (Key-Value): el modelo mas simple. Cada elemento es un par clave-valor, donde el valor puede ser cualquier tipo de dato (string, lista, set, hash). Extremadamente rapido. Principal representante: Redis (en memoria, usado como cache y broker de mensajes). Casos de uso: caches, sesiones de usuario, colas de mensajes.

- Columnares (Wide-Column): organizan los datos en familias de columnas en lugar de filas. Optimizadas para consultas analiticas sobre grandes volumenes de datos. Representantes: Apache Cassandra, HBase. Casos de uso: IoT, series temporales, analisis de logs.

- Grafos: almacenan entidades como nodos y las relaciones entre ellas como aristas, con propiedades en ambos. Optimizadas para consultas de grafos (caminos, vecinos, comunidades). Principal representante: Neo4j. Casos de uso: redes sociales, deteccion de fraude, grafos de conocimiento.

PREGUNTAS TIPO EXAMEN INAP:

1. En la arquitectura ANSI-SPARC, el nivel que describe como se almacenan fisicamente los datos en el disco es:
a) Nivel externo  b) Nivel conceptual  c) Nivel interno  d) Nivel de vistas
Respuesta correcta: c) Nivel interno

2. La propiedad ACID que garantiza que los cambios de una transaccion confirmada son permanentes incluso ante fallos del sistema es:
a) Atomicidad  b) Consistencia  c) Aislamiento  d) Durabilidad
Respuesta correcta: d) Durabilidad

3. El tipo de indice de base de datos que soporta busquedas de igualdad exacta pero NO busquedas por rango es:
a) Indice B-Tree  b) Indice Hash  c) Indice de texto completo  d) Indice unico
Respuesta correcta: b) Indice Hash

4. La base de datos NoSQL orientada a grafos mas conocida es:
a) MongoDB  b) Redis  c) Cassandra  d) Neo4j
Respuesta correcta: d) Neo4j
""")

# ============================================================
# TEMA 8 - Desarrollo web y aplicaciones cliente-servidor
# ============================================================
Tema.objects.filter(bloque__numero=3, numero=8).update(resumen_estudio="""1. ARQUITECTURA WEB DE TRES CAPAS

La arquitectura web de tres capas (3-tier) separa la aplicacion en tres niveles logicos y fisicos independientes:

- Capa de Presentacion (Frontend): la interfaz de usuario que se ejecuta en el navegador del cliente. Responsable de la visualizacion y la interaccion con el usuario. Tecnologias: HTML, CSS, JavaScript.
- Capa de Logica de Negocio (Backend / Servidor de Aplicaciones): contiene las reglas de negocio, el procesamiento de datos y la logica de la aplicacion. Se ejecuta en el servidor. Tecnologias: Django, Spring Boot, Node.js.
- Capa de Datos (Servidor de Base de Datos): almacena y gestiona los datos de la aplicacion. Tecnologias: PostgreSQL, MySQL, Oracle, MongoDB.

DATO CLAVE: La arquitectura de 3 capas separa Presentacion (navegador/frontend), Logica de Negocio (servidor de aplicaciones/backend) y Datos (base de datos). Esta separacion mejora la escalabilidad, el mantenimiento y la seguridad.

2. FRONTEND: HTML5, CSS3 Y JAVASCRIPT

- HTML5 (HyperText Markup Language): es el lenguaje de marcado estandar para la estructura y el contenido de las paginas web. HTML5 introdujo elementos semanticos (<header>, <nav>, <main>, <article>, <section>, <footer>, <aside>) que mejoran la accesibilidad y el SEO. Tambien incluye <video>, <audio>, <canvas> y APIs como Geolocation y localStorage.

- CSS3 (Cascading Style Sheets): lenguaje de hojas de estilo que controla la presentacion visual (colores, tipografia, diseno, animaciones). CSS3 introdujo Flexbox y CSS Grid para disenos de maquetacion complejos, variables CSS (custom properties), animaciones y media queries para el diseno responsive.

- JavaScript (ES6+): es el unico lenguaje de programacion nativo de los navegadores. ECMAScript 6 (2015) fue una actualizacion mayor que introdujo: arrow functions, const/let, clases, modulos (import/export), promesas (Promise), async/await, destructuring, template literals y el operador spread/rest.

Frameworks y librerias de Frontend:
- React: libreria de JavaScript de Meta (Facebook) para construir interfaces de usuario basadas en componentes reutilizables y un DOM virtual (Virtual DOM). Es la mas usada en la industria.
- Vue.js: framework progresivo de JavaScript, considerado mas sencillo de aprender que React. Ideal para integracion progresiva en proyectos existentes.
- Angular: framework completo (opinionated) de Google, basado en TypeScript. Incluye todo lo necesario (routing, estado, inyeccion de dependencias). Usado en aplicaciones empresariales grandes.

DATO CLAVE: React (Meta/Facebook) = libreria de componentes con Virtual DOM. Angular (Google) = framework completo con TypeScript. Vue.js = framework progresivo. Los tres siguen el paradigma de componentes.

3. BACKEND: SERVIDORES DE APLICACIONES Y FRAMEWORKS

- Django (Python): framework web de alto nivel que sigue el patron MVT (Model-View-Template) y el principio "Don't Repeat Yourself" (DRY). Incluye ORM, sistema de autenticacion, panel de administracion, migraciones de base de datos y proteccion contra vulnerabilidades comunes (CSRF, XSS, inyeccion SQL). Muy usado en la AGE y administraciones publicas.

- Spring Boot (Java): framework que simplifica la configuracion de aplicaciones Spring en Java. Sigue el patron MVC. Muy usado en entornos empresariales. Usa inyeccion de dependencias (IoC) y anotaciones.

- Node.js (JavaScript): entorno de ejecucion de JavaScript del lado del servidor, basado en el motor V8. Destaca por su modelo de E/S no bloqueante y orientado a eventos, ideal para aplicaciones en tiempo real y de alta concurrencia (chats, streaming). El framework mas popular es Express.js.

4. SERVICIOS WEB Y APIS

Una API (Application Programming Interface) es un conjunto de definiciones y protocolos que permite la comunicacion entre aplicaciones de software.

- Arquitectura RESTful (Representational State Transfer): estilo arquitectonico para disenar servicios web propuesto por Roy Fielding. Se basa en los principios HTTP:
  * Recursos identificados por URLs (URIs).
  * Operaciones mediante metodos HTTP: GET (leer), POST (crear), PUT (actualizar completo), PATCH (actualizar parcial), DELETE (eliminar).
  * Sin estado (stateless): cada peticion contiene toda la informacion necesaria.
  * Formato de datos preferido: JSON.
  * Respuestas con codigos de estado HTTP (200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 500 Internal Server Error).

DATO CLAVE: REST es un ESTILO ARQUITECTONICO, no un protocolo. SOAP es un PROTOCOLO. REST usa JSON habitualmente. SOAP usa XML siempre. REST es mas ligero y flexible; SOAP tiene mayor seguridad integrada (WS-Security).

- SOAP (Simple Object Access Protocol): protocolo de mensajeria basado en XML que define un formato de mensaje estricto. El contrato del servicio se define en un fichero WSDL (Web Services Description Language). Tiene estandares propios de seguridad (WS-Security), transacciones y mensajeria fiable. Usado en entornos empresariales con alta exigencia de seguridad e interoperabilidad.

- GraphQL: lenguaje de consulta para APIs desarrollado por Meta (2015). El cliente especifica exactamente que datos necesita (evita el over-fetching y under-fetching). El servidor expone un unico endpoint. Usa un esquema de tipos fuertemente tipado.

5. PROTOCOLO HTTP

HTTP (HyperText Transfer Protocol) es el protocolo de la capa de aplicacion que sustenta la web. HTTPS es la version segura (HTTP + TLS/SSL).

Metodos HTTP principales: GET (obtener recurso), POST (crear recurso), PUT (reemplazar recurso), PATCH (modificar parcialmente), DELETE (eliminar), HEAD (cabeceras sin cuerpo), OPTIONS (metodos soportados).

Codigos de estado HTTP:
- 1xx: informativos  - 2xx: exito (200 OK, 201 Created, 204 No Content)
- 3xx: redireccion  - 4xx: error del cliente (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found)
- 5xx: error del servidor (500 Internal Server Error, 503 Service Unavailable)

PREGUNTAS TIPO EXAMEN INAP:

1. El metodo HTTP que se usa en una API RESTful para ACTUALIZAR COMPLETAMENTE un recurso existente es:
a) POST  b) PATCH  c) PUT  d) GET
Respuesta correcta: c) PUT

2. El formato de datos preferido en las APIs RESTful es:
a) XML  b) YAML  c) CSV  d) JSON
Respuesta correcta: d) JSON

3. El framework web de Python que sigue el patron MVT (Model-View-Template) y el principio DRY (Don't Repeat Yourself) es:
a) Flask  b) FastAPI  c) Django  d) Express.js
Respuesta correcta: c) Django

4. La diferencia fundamental entre REST y SOAP es que:
a) REST usa XML y SOAP usa JSON  b) REST es un protocolo y SOAP es un estilo arquitectonico  c) REST es un estilo arquitectonico y SOAP es un protocolo que usa XML  d) REST solo funciona con HTTP y SOAP no
Respuesta correcta: c) REST es un estilo arquitectonico y SOAP es un protocolo que usa XML
""")

# ============================================================
# TEMA 9 - Control de versiones, pruebas de software y CI/CD
# ============================================================
Tema.objects.filter(bloque__numero=3, numero=9).update(resumen_estudio="""1. CONTROL DE VERSIONES DISTRIBUIDO CON GIT

Git es un sistema de control de versiones distribuido (DVCS) creado por Linus Torvalds en 2005 para el desarrollo del kernel de Linux. En un sistema distribuido, cada desarrollador tiene una copia completa del repositorio (con todo el historial) en su maquina local.

Conceptos fundamentales de Git:
- Repositorio (repo): directorio que contiene todos los archivos del proyecto y la carpeta oculta .git con el historial completo.
- Working Directory: el directorio de trabajo donde el desarrollador edita los archivos.
- Staging Area (Index): area intermedia donde se preparan los cambios (git add) antes de confirmarlos.
- Commit: instantanea del estado del Staging Area. Tiene un identificador SHA-1 unico de 40 caracteres, autor, fecha y mensaje.
- Branch (rama): puntero movil a un commit especifico. Permite trabajar en funcionalidades o correcciones de forma aislada. La rama principal se llama main (anteriormente master).
- HEAD: puntero especial que indica el commit actual en el que se trabaja.

DATO CLAVE: El flujo basico de Git es: Working Directory -> (git add) -> Staging Area -> (git commit) -> Repositorio Local -> (git push) -> Repositorio Remoto.

Operaciones clave de Git:
- git clone: clona un repositorio remoto en local.
- git branch <nombre>: crea una nueva rama.
- git checkout / git switch: cambia de rama.
- git merge: integra los cambios de una rama en la rama actual. Genera un merge commit.
- git rebase: reescribe el historial aplicando los commits de una rama sobre la punta de otra. Crea un historial mas lineal, pero modifica los SHA-1 de los commits (no usar en ramas publicas).
- git pull: descarga cambios del repositorio remoto (git fetch + git merge).
- git push: sube los commits locales al repositorio remoto.
- git stash: guarda temporalmente los cambios no confirmados del Working Directory.

2. PLATAFORMAS COLABORATIVAS: GITHUB Y GITLAB

- GitHub: plataforma de alojamiento de repositorios Git propiedad de Microsoft. Ofrece repositorios publicos y privados, Pull Requests (revision de codigo entre pares), GitHub Actions (CI/CD integrado), GitHub Issues (gestion de tareas) y GitHub Pages (hosting de paginas estaticas).

- GitLab: plataforma similar a GitHub, disponible como servicio en la nube (GitLab.com) o como instalacion propia (self-hosted). Destaca por su CI/CD integrado (GitLab CI/CD) y su enfoque en el ciclo DevOps completo. Muy usado en organizaciones que prefieren infraestructura propia.

DATO CLAVE: En GitHub, la solicitud de revision e integracion de cambios se llama Pull Request (PR). En GitLab se llama Merge Request (MR). Ambas facilitan la revision de codigo antes de fusionar ramas.

3. TIPOS DE PRUEBAS DE SOFTWARE

Las pruebas de software verifican que el sistema cumple los requisitos y funciona correctamente. Se clasifican segun su nivel, objetivo y tecnica.

Segun el nivel:
- Pruebas Unitarias: verifican el funcionamiento de la unidad mas pequeña del software (metodo, funcion, clase) de forma aislada, usando objetos simulados (mocks y stubs) para sustituir dependencias externas. Son las mas rapidas y numerosas. Frameworks: JUnit (Java), pytest (Python), NUnit (.NET).
- Pruebas de Integracion: verifican que los diferentes modulos o componentes del sistema funcionan correctamente juntos. Detectan problemas en las interfaces entre modulos.
- Pruebas de Sistema: verifican el sistema completo contra los requisitos especificados. Se realizan sobre un entorno lo mas similar posible al de produccion.
- Pruebas de Aceptacion (UAT - User Acceptance Testing): el cliente o usuario final verifica que el sistema cumple sus necesidades y requisitos de negocio. Son el ultimo paso antes de la puesta en produccion.

DATO CLAVE: Piramide de pruebas (Mike Cohn): la base son muchas pruebas Unitarias (rapidas y baratas), el nivel medio son las de Integracion, y la cima son pocas pruebas de Interfaz de Usuario (lentas y caras). Las pruebas unitarias deben ser la mayoria.

Segun el objetivo:
- Pruebas de Rendimiento: verifican el comportamiento del sistema bajo carga. Incluyen: pruebas de carga (carga esperada), pruebas de estres (carga extrema), pruebas de estabilidad (carga sostenida prolongada).
- Pruebas de Regresion: verifican que los cambios nuevos no han roto funcionalidades que ya funcionaban correctamente. Son fundamentales en CI/CD.
- Pruebas de Seguridad: identifican vulnerabilidades en el sistema.
- Pruebas de Usabilidad: evaluan la facilidad de uso e interfaz de usuario.

Segun la tecnica:
- Caja blanca (White-box): el tester conoce el codigo fuente interno. Se disenan casos de prueba para cubrir el codigo (cobertura de ramas, sentencias, caminos).
- Caja negra (Black-box): el tester no conoce el codigo interno. Se prueba la funcionalidad segun los requisitos de entrada/salida.
- Caja gris: combinacion de ambas.

4. INTEGRACION Y DESPLIEGUE CONTINUO (CI/CD)

CI/CD es un conjunto de practicas de DevOps que automatizan la construccion, prueba y despliegue del software para detectar errores rapido y entregar valor de forma continua.

- Integracion Continua (CI - Continuous Integration): practica por la que los desarrolladores integran su codigo en el repositorio compartido frecuentemente (varias veces al dia). Cada integracion se verifica automaticamente mediante la construccion del proyecto y la ejecucion de las pruebas automatizadas. Objetivo: detectar errores de integracion temprano.

- Entrega Continua (CD - Continuous Delivery): extension de la CI. Garantiza que el software siempre esta en un estado listo para desplegarse en produccion. El despliegue final requiere aprobacion manual.

- Despliegue Continuo (CD - Continuous Deployment): el despliegue en produccion es completamente automatico, sin aprobacion manual, cada vez que el pipeline de CI pasa exitosamente.

Un pipeline CI/CD tipico incluye las siguientes fases: Codigo fuente (commit) -> Build (compilacion) -> Pruebas unitarias -> Analisis de calidad de codigo -> Pruebas de integracion -> Despliegue en entorno de staging -> Pruebas de aceptacion -> Despliegue en produccion.

DATO CLAVE: Herramientas CI/CD: Jenkins (el mas clasico, open source), GitHub Actions (integrado en GitHub), GitLab CI/CD (integrado en GitLab), Azure DevOps (Microsoft). La diferencia entre Entrega Continua y Despliegue Continuo es que la Entrega requiere aprobacion humana para el despliegue en produccion y el Despliegue es completamente automatico.

5. DEVOPS

DevOps es una cultura y conjunto de practicas que une los equipos de Desarrollo (Dev) y Operaciones (Ops) para acortar el ciclo de vida del desarrollo y entregar software con mayor calidad y frecuencia. Sus pilares son: automatizacion, colaboracion, medicion y mejora continua. CI/CD es la practica tecnica central de DevOps.

PREGUNTAS TIPO EXAMEN INAP:

1. En Git, el comando que mueve los cambios del Working Directory al Staging Area es:
a) git commit  b) git push  c) git add  d) git stash
Respuesta correcta: c) git add

2. El tipo de prueba de software que verifica el funcionamiento de la unidad mas pequeña del codigo (metodo o funcion) de forma aislada es:
a) Prueba de integracion  b) Prueba de aceptacion  c) Prueba de sistema  d) Prueba unitaria
Respuesta correcta: d) Prueba unitaria

3. La diferencia entre Entrega Continua (Continuous Delivery) y Despliegue Continuo (Continuous Deployment) es:
a) La Entrega Continua ejecuta las pruebas automaticamente; el Despliegue Continuo no  b) El Despliegue Continuo automatiza tambien el despliegue en produccion sin aprobacion manual  c) La Entrega Continua solo aplica a proyectos pequeños  d) No hay diferencia, son sinonimos
Respuesta correcta: b) El Despliegue Continuo automatiza tambien el despliegue en produccion sin aprobacion manual

4. En el contexto de las pruebas de software, las pruebas que verifican que los cambios nuevos no han roto funcionalidades que ya funcionaban se denominan:
a) Pruebas de aceptacion  b) Pruebas de regresion  c) Pruebas de estres  d) Pruebas de caja blanca
Respuesta correcta: b) Pruebas de regresion
""")

# ============================================================
# TEMA 10 - Accesibilidad web y usabilidad: RD 1112/2018 y WCAG
# ============================================================
Tema.objects.filter(bloque__numero=3, numero=10).update(resumen_estudio="""1. MARCO NORMATIVO: REAL DECRETO 1112/2018

El Real Decreto 1112/2018, de 7 de septiembre, sobre accesibilidad de los sitios web y aplicaciones para dispositivos moviles del sector publico, transpone al ordenamiento juridico espanol la Directiva Europea 2016/2102 del Parlamento Europeo y del Consejo.

Ambito de aplicacion: es de aplicacion obligatoria a todas las Administraciones Publicas espanolas, incluyendo la Administracion General del Estado, las Comunidades Autonomas y las Entidades Locales, asi como a otras entidades del sector publico.

Contenidos afectados: sitios web y aplicaciones moviles del sector publico. Quedan excluidos algunos contenidos como archivos de ofimativa publicados antes del 23 de septiembre de 2018, contenido de terceros no financiado por el organismo publico y algunas emisiones en directo.

DATO CLAVE: El RD 1112/2018 transpone la Directiva Europea 2016/2102. Nivel de conformidad EXIGIDO en el sector publico: nivel AA de las Pautas WCAG 2.1. Publicado el 7 de septiembre de 2018.

Obligaciones principales del RD 1112/2018:
- Cumplir el nivel AA de las Pautas WCAG 2.1 (actualmente se actualiza a WCAG 2.2).
- Publicar una Declaracion de Accesibilidad actualizada para cada sitio web y aplicacion movil.
- Proporcionar un mecanismo de contacto para que los usuarios puedan notificar incumplimientos y solicitar informacion inaccesible en formatos alternativos.
- Realizar auditorias periodicas de accesibilidad. El Observatorio de Accesibilidad Web (OAW) del MPTFP es el organismo encargado del seguimiento.

2. PAUTAS WCAG: CONCEPTO Y ESTRUCTURA

Las Pautas de Accesibilidad para el Contenido Web (WCAG - Web Content Accessibility Guidelines) son el estandar internacional de accesibilidad web, publicadas por el W3C (World Wide Web Consortium) a traves del grupo de trabajo WAI (Web Accessibility Initiative).

La version de referencia es WCAG 2.1 (2018); WCAG 2.2 fue publicada en 2023. WCAG 2.0 data de 2008.

Las WCAG se organizan en una jerarquia de cuatro niveles:
- Principios (4): el nivel mas alto y abstracto.
- Pautas (13): objetivos que guian el cumplimiento de cada principio.
- Criterios de exito: requisitos verificables y comprobables. Cada criterio tiene un nivel (A, AA o AAA).
- Tecnicas suficientes y de asesoramiento: ejemplos de como cumplir los criterios.

DATO CLAVE: La estructura de WCAG es: 4 Principios (POUR) -> 13 Pautas -> Criterios de Exito (con niveles A, AA, AAA). WCAG 2.1 tiene 78 criterios de exito (61 de WCAG 2.0 + 17 nuevos).

3. LOS CUATRO PRINCIPIOS WCAG: POUR

Los cuatro principios de las WCAG son el fundamento de la accesibilidad web y se recuerdan con el acronimo POUR:

- Perceptible: la informacion y los componentes de la interfaz de usuario deben presentarse a los usuarios de formas que puedan percibir. Esto significa que ningun contenido debe ser invisible a todos sus sentidos. Incluye: alternativas de texto para contenido no textual (alt en imagenes), subtitulos y audiodescripciones para contenido audiovisual, contraste de color suficiente, contenido adaptable a diferentes presentaciones.

- Operable: los componentes de la interfaz de usuario y la navegacion deben ser operables. Ningun usuario debe requerir una interaccion que no pueda realizar. Incluye: toda funcionalidad debe ser accesible mediante teclado, tiempo suficiente para leer e interactuar, contenido que no provoque convulsiones (no mas de 3 destellos por segundo), navegacion coherente.

- Comprensible: la informacion y el funcionamiento de la interfaz de usuario deben ser comprensibles. Incluye: texto legible (idioma identificado), funcionamiento predecible, ayuda para evitar y corregir errores de entrada.

- Robusto: el contenido debe ser suficientemente robusto como para ser interpretado por una amplia variedad de agentes de usuario, incluyendo los productos de apoyo (lectores de pantalla). Requiere maximizar la compatibilidad con tecnologias actuales y futuras. Incluye: codigo HTML valido y bien formado, nombre, rol y valor de los componentes de la interfaz accesibles via APIs de accesibilidad (WAI-ARIA).

DATO CLAVE: POUR = Perceptible, Operable, Comprensible (Understandable) y Robusto. Son los 4 principios de WCAG. Si un contenido falla en CUALQUIERA de estos principios, no es accesible.

4. NIVELES DE CONFORMIDAD WCAG

Cada criterio de exito de las WCAG tiene asignado un nivel de conformidad:

- Nivel A: el nivel minimo. Incluye los criterios mas basicos. Si no se cumple el nivel A, el contenido es practicamente inutilizable para algunos usuarios con discapacidad. Ejemplo: todas las imagenes deben tener texto alternativo (alt).

- Nivel AA: nivel intermedio. Es el NIVEL EXIGIDO por la normativa europea y el RD 1112/2018 para las Administraciones Publicas. Incluye todos los criterios de nivel A mas criterios adicionales. Ejemplo: el contraste entre el texto y el fondo debe ser de al menos 4,5:1 para texto normal y 3:1 para texto grande.

- Nivel AAA: el nivel mas alto. Proporciona accesibilidad optima pero no es exigible como requisito general ya que no todos los contenidos pueden cumplirlo. Ejemplo: contraste de 7:1, lengua de signos para contenido de audio.

DATO CLAVE: El nivel de conformidad exigido al sector publico espanol por el RD 1112/2018 es el nivel AA de WCAG 2.1. El nivel AAA no es exigible como requisito general.

5. DECLARACION DE ACCESIBILIDAD

La Declaracion de Accesibilidad es un documento publico y actualizado que cada organismo publico debe publicar en su sitio web y aplicacion movil. Debe incluir:

- El nivel de conformidad con las WCAG alcanzado.
- Las partes del contenido que no son accesibles y las razones.
- El mecanismo de contacto para que los usuarios soliciten informacion alternativa o notifiquen problemas.
- El enlace al procedimiento de reclamacion ante el organo supervisor (Observatorio de Accesibilidad Web).
- La fecha de la ultima revision.

6. HERRAMIENTAS DE VALIDACION DE ACCESIBILIDAD

- TAW (Test de Accesibilidad Web): herramienta desarrollada por la Fundacion CTIC, muy usada en Espana para la evaluacion automatica de la accesibilidad web segun WCAG.
- WAVE (Web Accessibility Evaluation Tool): herramienta en linea y extension de navegador de WebAIM.
- Axe: extension de navegador y herramienta de desarrollo de accesibilidad ampliamente usada.
- Lighthouse: herramienta de auditoria integrada en Chrome DevTools que incluye un modulo de accesibilidad.

DATO CLAVE: Ninguna herramienta automatica puede detectar el 100% de los problemas de accesibilidad. La evaluacion completa requiere pruebas automaticas + revision manual + pruebas con usuarios con discapacidad y tecnologias de apoyo (lectores de pantalla como NVDA, JAWS o VoiceOver).

7. USABILIDAD Y SU RELACION CON LA ACCESIBILIDAD

La usabilidad (ISO 9241-11) se define como el grado en que un producto puede ser usado por usuarios especificos para conseguir objetivos especificos con efectividad, eficiencia y satisfaccion en un contexto de uso especifico. Jakob Nielsen definio 10 heuristicas de usabilidad.

Aunque accesibilidad y usabilidad son conceptos distintos (la accesibilidad se centra en las personas con discapacidad; la usabilidad, en todos los usuarios), se complementan: un sitio accesible generalmente es mas usable para todos.

PREGUNTAS TIPO EXAMEN INAP:

1. El Real Decreto 1112/2018 transpone al ordenamiento espanol:
a) La Directiva 95/46/CE sobre proteccion de datos  b) La Directiva 2016/2102 sobre accesibilidad de sitios web del sector publico  c) La Directiva 2019/882 sobre los requisitos de accesibilidad de los productos y servicios  d) El Reglamento General de Proteccion de Datos (RGPD)
Respuesta correcta: b) La Directiva 2016/2102 sobre accesibilidad de sitios web del sector publico

2. El nivel de conformidad WCAG exigido a los sitios web de las Administraciones Publicas espanolas por el RD 1112/2018 es:
a) Nivel A  b) Nivel AA  c) Nivel AAA  d) Nivel WCAG 2.0
Respuesta correcta: b) Nivel AA

3. Los cuatro principios de las Pautas WCAG, recordados con el acronimo POUR, son:
a) Practico, Optimizado, Usable y Responsivo  b) Perceptible, Operable, Comprensible y Robusto  c) Publico, Ordenado, Universal y Razonable  d) Preciso, Operativo, Claro y Resistente
Respuesta correcta: b) Perceptible, Operable, Comprensible y Robusto

4. La Declaracion de Accesibilidad que deben publicar los organismos publicos debe incluir obligatoriamente:
a) El codigo fuente del sitio web  b) El nivel de conformidad alcanzado, las partes no accesibles y un mecanismo de contacto  c) Solo el nivel de conformidad WCAG  d) Un certificado de accesibilidad emitido por una entidad certificadora acreditada
Respuesta correcta: b) El nivel de conformidad alcanzado, las partes no accesibles y un mecanismo de contacto
""")

print("="*60)
print("BLOQUE III - Actualizacion de resumen_estudio completada")
print("="*60)
print("Temas actualizados: T1 a T10 del Bloque 3 (Desarrollo de Sistemas)")
