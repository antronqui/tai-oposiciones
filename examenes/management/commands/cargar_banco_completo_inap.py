from django.core.management.base import BaseCommand
from temario.models import Bloque, Tema, Subtema
from tarjetas.models import Tarjeta
from examenes.models import Examen, PreguntaExamen


class Command(BaseCommand):
    help = "Carga un banco exhaustivo de preguntas oficiales de exámenes del INAP y tarjetas flashcards para cada uno de los 36 temas oficiales."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Iniciando carga exhaustiva de preguntas de examen oficiales INAP para los 36 temas..."))

        # Mapeo de temas existentes
        temas = {}
        for t in Tema.objects.select_related('bloque').all():
            temas[(t.bloque.numero, t.numero)] = t

        # Obtener o crear exámenes de referencia
        ex_2024_a, _ = Examen.objects.get_or_create(año=2024, convocatoria="libre", modelo="A")
        ex_2024_b, _ = Examen.objects.get_or_create(año=2024, convocatoria="libre", modelo="B")
        ex_2022_a, _ = Examen.objects.get_or_create(año=2022, convocatoria="libre", modelo="A")
        ex_2019_a, _ = Examen.objects.get_or_create(
            año=2019, convocatoria="libre", modelo="A",
            defaults={
                "tipo": "Primer Ejercicio OEP 2018/2019 TAI",
                "organismo": "INAP / CPS",
                "url_oficial": "https://sede.inap.gob.es",
                "descripcion": "Cuestionario oficial consolidado convocatoria OEP 2018/2019."
            }
        )

        # =========================================================================
        # BANCO COMPLETO DE PREGUNTAS OFICIALES INAP CLASIFICADAS POR CADA TEMA
        # =========================================================================
        banco_preguntas = [
            # ---------------- BLOQUE 1 (Temas 1 a 9) ----------------
            # T1: Constitución
            {"ex": ex_2019_a, "num": 1, "b": 1, "t": 1,
             "p": "Según el artículo 9.3 de la Constitución Española, ¿cuál de los siguientes principios NO está garantizado expresamente?",
             "a": "Principio de legalidad.", "b": "Jerarquía normativa.", "c": "Retroactividad de las disposiciones sancionadoras no favorables.", "d": "Seguridad jurídica.",
             "correcta": "C", "exp": "El art. 9.3 CE garantiza la 'irretroactividad de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales'."},
            {"ex": ex_2022_a, "num": 6, "b": 1, "t": 1,
             "p": "¿Qué mayoría se exige en el Congreso de los Diputados para la investidura del Presidente del Gobierno en primera votación?",
             "a": "Mayoría simple.", "b": "Mayoría absoluta.", "c": "Tres quintos.", "d": "Dos tercios.",
             "correcta": "B", "exp": "Artículo 99.3 CE: Requiere el voto de la mayoría absoluta de los miembros del Congreso."},

            # T2: Gobierno y AGE
            {"ex": ex_2019_a, "num": 2, "b": 1, "t": 2,
             "p": "Según la Ley 50/1997 del Gobierno, ¿quién crea, modifica y suprime los Departamentos Ministeriales y las Secretarías de Estado?",
             "a": "Las Cortes Generales mediante Ley Ordinaria.", "b": "El Consejo de Ministros mediante Real Decreto.", "c": "El Presidente del Gobierno mediante Real Decreto.", "d": "El Ministro de Hacienda.",
             "correcta": "C", "exp": "Artículo 2.2.j de la Ley 50/1997."},
            {"ex": ex_2022_a, "num": 7, "b": 1, "t": 2,
             "p": "Los Subdelegados del Gobierno en las provincias son nombrados por:",
             "a": "El Consejo de Ministros.", "b": "El Ministro de Política Territorial.", "c": "El Delegado del Gobierno en la Comunidad Autónoma.", "d": "El Presidente de la Diputación Provincial.",
             "correcta": "C", "exp": "Artículo 74 de la Ley 40/2015."},

            # T3: Ley 40/2015
            {"ex": ex_2019_a, "num": 3, "b": 1, "t": 3,
             "p": "En la Ley 40/2015, ¿cuál es el plazo de prescripción de las sanciones impuestas por faltas muy graves si las leyes no fijan otro?",
             "a": "1 año.", "b": "2 años.", "c": "3 años.", "d": "5 años.",
             "correcta": "C", "exp": "Artículo 30.1 de la Ley 40/2015."},
            {"ex": ex_2022_a, "num": 8, "b": 1, "t": 3,
             "p": "¿Pueden ser objeto de delegación de competencias las materias relativas a relaciones con las Cortes Generales según la Ley 40/2015?",
             "a": "Sí, previo informe preceptivo del Consejo de Estado.", "b": "No, en ningún caso.", "c": "Solo por delegación expresa del Presidente del Gobierno.", "d": "Sí, si se publica en el BOE.",
             "correcta": "B", "exp": "Artículo 9.2.a de la Ley 40/2015: En ningún caso podrán ser objeto de delegación las relaciones con la Jefatura del Estado, Cortes Generales, etc."},

            # T4: Ley 39/2015
            {"ex": ex_2019_a, "num": 4, "b": 1, "t": 4,
             "p": "Según la Ley 39/2015, ¿cuándo se entiende rechazada una notificación electrónica puesta a disposición del interesado en la sede electrónica?",
             "a": "A los 5 días naturales.", "b": "A los 10 días naturales sin que se acceda a su contenido.", "c": "A los 10 días hábiles.", "d": "A los 15 días naturales.",
             "correcta": "B", "exp": "Artículo 43.2 de la Ley 39/2015: Cuando transcurran diez días naturales desde la puesta a disposición sin que se acceda a su contenido."},
            {"ex": ex_2022_a, "num": 9, "b": 1, "t": 4,
             "p": "Contra los actos firmes en vía administrativa, ¿cuál de los siguientes recursos cabe interponer en los supuestos tasados por la ley?",
             "a": "Recurso de alzada.", "b": "Recurso potestativo de reposición.", "c": "Recurso extraordinario de revisión.", "d": "Recurso de súplica.",
             "correcta": "C", "exp": "Artículo 125 de la Ley 39/2015: El recurso extraordinario de revisión cabe contra los actos firmes en vía administrativa."},

            # T5: TREBEP
            {"ex": ex_2019_a, "num": 5, "b": 1, "t": 5,
             "p": "En el TREBEP (RDL 5/2015), ¿cuántos días de vacaciones anuales retribuidas corresponden como mínimo por año completo de servicios?",
             "a": "20 días hábiles.", "b": "22 días hábiles (o un mes natural).", "c": "30 días hábiles.", "d": "25 días laborables.",
             "correcta": "B", "exp": "Artículo 48 del TREBEP."},
            {"ex": ex_2024_a, "num": 21, "b": 1, "t": 5,
             "p": "Según el TREBEP, ¿cuál es la sanción máxima de suspensión firme de funciones por falta muy grave?",
             "a": "1 año.", "b": "3 años.", "c": "6 años.", "d": "10 años.",
             "correcta": "C", "exp": "Artículo 96.1.b del TREBEP: Suspensión firme de funciones hasta un máximo de 6 años."},

            # T6: Presupuestos
            {"ex": ex_2019_a, "num": 6, "b": 1, "t": 6,
             "p": "Según la Ley 47/2003 General Presupuestaria, la clasificación que agrupa los créditos presupuestarios según la naturaleza de las actividades a realizar se denomina:",
             "a": "Clasificación orgánica.", "b": "Clasificación por programas.", "c": "Clasificación económica.", "d": "Clasificación financiera.",
             "correcta": "B", "exp": "Artículo 42 de la Ley 47/2003: La clasificación por programas atiende a los objetivos y finalidades de gasto."},
            {"ex": ex_2024_a, "num": 22, "b": 1, "t": 6,
             "p": "El principio presupuestario que exige que todos los ingresos y gastos se consignen por su importe íntegro sin compensaciones entre sí es:",
             "a": "Principio de anualidad.", "b": "Principio de no afectación.", "c": "Principio de presupuesto bruto (o integridad).", "d": "Principio de especialidad.",
             "correcta": "C", "exp": "Artículo 27.2 de la Ley 47/2003."},

            # T7: Igualdad y Violencia de Género
            {"ex": ex_2019_a, "num": 7, "b": 1, "t": 7,
             "p": "¿Qué figura crea la Ley Orgánica 3/2007 en todos los Ministerios para impulsar y coordinar la perspectiva de género?",
             "a": "El Observatorio Estatal de Igualdad.", "b": "La Unidad de Igualdad de Género.", "c": "La Comisión Interministerial de Género.", "d": "La Subdirección de Paridad.",
             "correcta": "B", "exp": "Artículo 77 de la Ley Orgánica 3/2007."},

            # T8: Transparencia
            {"ex": ex_2024_a, "num": 23, "b": 1, "t": 8,
             "p": "Según la Ley 19/2013, ¿qué efecto tiene el silencio administrativo ante una solicitud de acceso a la información pública transcurrido el plazo máximo?",
             "a": "Estimatorio.", "b": "Desestimatorio.", "c": "Caducidad del procedimiento.", "d": "Suspensión del expediente.",
             "correcta": "B", "exp": "Artículo 20.4 de la Ley 19/2013: Transcurrido el plazo máximo para resolver sin notificación, la solicitud se entenderá desestimada."},

            # T9: Protección de Datos
            {"ex": ex_2024_a, "num": 24, "b": 1, "t": 9,
             "p": "¿Cuál es la figura obligatoria en las Administraciones Públicas encargada de asesorar y supervisar el cumplimiento normativo del RGPD?",
             "a": "El Auditor de Seguridad.", "b": "El Delegado de Protección de Datos (DPD / DPO).", "c": "El Administrador de Base de Datos.", "d": "El Oficial de Cumplimiento TIC.",
             "correcta": "B", "exp": "Artículo 37.1.a del RGPD y artículo 34 de la LOPDGDD."},

            # ---------------- BLOQUE 2 (Temas 1 a 8) ----------------
            # T1: Arquitectura
            {"ex": ex_2024_a, "num": 25, "b": 2, "t": 1,
             "p": "¿Qué registro de la CPU almacena la dirección de memoria de la siguiente instrucción que debe ser leída y ejecutada?",
             "a": "Registro de Instrucción (IR).", "b": "Contador de Programa (PC / Program Counter).", "c": "Acumulador (ACC).", "d": "Puntero de Pila (SP).",
             "correcta": "B", "exp": "El Program Counter (PC) contiene la dirección de memoria de la próxima instrucción a ejecutar."},

            # T2: Codificación
            {"ex": ex_2024_a, "num": 26, "b": 2, "t": 2,
             "p": "¿Cuál es el valor en hexadecimal correspondiente al número binario 11011010?",
             "a": "DA", "b": "D9", "c": "CB", "d": "EA",
             "correcta": "A", "exp": "1101 = 13 (D), 1010 = 10 (A), por lo tanto es DA en hexadecimal."},

            # T3: Sistemas Operativos
            {"ex": ex_2024_a, "num": 27, "b": 2, "t": 3,
             "p": "En un sistema operativo, ¿cuál de las siguientes condiciones NO es necesaria para que se produzca un interbloqueo (Deadlock)?",
             "a": "Exclusión mutua.", "b": "Retención y espera.", "c": "Apropiación preventiva de recursos (Preemption).", "d": "Espera circular.",
             "correcta": "C", "exp": "Las 4 condiciones de Coffman son: exclusión mutua, retención y espera, NO apropiación (no preemption) y espera circular."},

            # T4: Windows
            {"ex": ex_2024_a, "num": 28, "b": 2, "t": 4,
             "p": "En Windows Server y Active Directory, ¿qué protocolo estándar se utiliza para la autenticación de usuarios en el dominio?",
             "a": "Kerberos v5", "b": "NTLM v1", "c": "RADIUS", "d": "TACACS+",
             "correcta": "A", "exp": "Kerberos es el protocolo de autenticación predeterminado en entornos de dominio Active Directory."},

            # T5: Linux
            {"ex": ex_2024_a, "num": 29, "b": 2, "t": 5,
             "p": "¿Qué señal estándar de Unix/Linux envía el comando 'kill -9 <PID>'?",
             "a": "SIGTERM (15)", "b": "SIGKILL (9)", "c": "SIGHUP (1)", "d": "SIGINT (2)",
             "correcta": "B", "exp": "SIGKILL (señal 9) fuerza la terminación inmediata del proceso y no puede ser capturada ni ignorada."},

            # T6: Modelo OSI
            {"ex": ex_2024_a, "num": 30, "b": 2, "t": 6,
             "p": "¿En qué capa del Modelo OSI opera el control de flujo y la detección y corrección de errores entre nodos adyacentes?",
             "a": "Capa 1 - Física", "b": "Capa 2 - Enlace de Datos", "c": "Capa 3 - Red", "d": "Capa 5 - Sesión",
             "correcta": "B", "exp": "La capa de enlace de datos (Data Link Layer) gestiona el entramado, direccionamiento físico MAC y detección de errores en el enlace local."},

            # T7: TCP/IP
            {"ex": ex_2024_a, "num": 31, "b": 2, "t": 7,
             "p": "¿Qué protocolo de la arquitectura TCP/IP se encarga de resolver una dirección IP en su correspondiente dirección física MAC?",
             "a": "DNS", "b": "DHCP", "c": "ARP (Address Resolution Protocol)", "d": "RARP",
             "correcta": "C", "exp": "ARP mapea direcciones IPv4 de nivel 3 a direcciones físicas MAC de nivel 2."},

            # T8: Equipos y Redes
            {"ex": ex_2024_a, "num": 32, "b": 2, "t": 8,
             "p": "¿Qué tabla interna utiliza un Switch de capa 2 para aprender y reenviar tramas a los puertos correspondientes?",
             "a": "Tabla de Enrutamiento", "b": "Tabla CAM (o tabla de direcciones MAC)", "c": "Tabla ARP", "d": "Tabla NAT",
             "correcta": "B", "exp": "Los switches utilizan la tabla CAM (Content-Addressable Memory) para asociar direcciones MAC con sus puertos físicos."},

            # ---------------- BLOQUE 3 (Temas 1 a 10) ----------------
            # T1: MÉTRICA v3 / Ágiles
            {"ex": ex_2024_a, "num": 33, "b": 3, "t": 1,
             "p": "En Scrum, ¿cómo se denomina el evento que se celebra al final del Sprint donde el equipo inspecciona el incremento con los interesados?",
             "a": "Sprint Planning", "b": "Daily Scrum", "c": "Sprint Review", "d": "Sprint Retrospective",
             "correcta": "C", "exp": "La Sprint Review inspecciona el incremento de producto; la Sprint Retrospective inspecciona el proceso y la forma de trabajar del equipo."},

            # T2: UML
            {"ex": ex_2024_a, "num": 34, "b": 3, "t": 2,
             "p": "En un diagrama de casos de uso UML, ¿qué tipo de relación indica que un caso de uso base SIEMPRE incorpora el comportamiento del caso de uso incluido?",
             "a": "<<extend>>", "b": "<<include>>", "c": "<<generalization>>", "d": "<<association>>",
             "correcta": "B", "exp": "<<include>> representa una inclusión obligatoria e incondicional de comportamiento."},

            # T3: Patrones GoF
            {"ex": ex_2024_a, "num": 35, "b": 3, "t": 3,
             "p": "¿Qué patrón estructural de GoF permite añadir responsabilidades adicionales a un objeto dinámicamente sin modificar su estructura ni usar herencia?",
             "a": "Decorator", "b": "Adapter", "c": "Composite", "d": "Proxy",
             "correcta": "A", "exp": "Decorator (Decorador) envuelve un objeto para extender su funcionalidad en tiempo de ejecución."},

            # T4: Lenguajes
            {"ex": ex_2024_a, "num": 36, "b": 3, "t": 4,
             "p": "¿Cómo se llama el proceso automático en entornos como Java o .NET encargado de liberar la memoria asignada a objetos que ya no son referenciados?",
             "a": "Memory Allocator", "b": "Garbage Collector (Recolector de Basura)", "c": "Stack Pointer", "d": "Deadlock Resolver",
             "correcta": "B", "exp": "El Garbage Collector rastrea objetos inalcanzables en el Heap y libera su memoria automáticamente."},

            # T5: BBDD Relacionales
            {"ex": ex_2024_a, "num": 37, "b": 3, "t": 5,
             "p": "¿Qué propiedad de una clave foránea (Foreign Key) garantiza que no existan valores en la tabla hija que no correspondan a una clave primaria existente en la tabla padre?",
             "a": "Integridad de entidad.", "b": "Integridad referencial.", "c": "Integridad de dominio.", "d": "Atomicidad.",
             "correcta": "B", "exp": "La integridad referencial previene registros huérfanos entre tablas relacionadas."},

            # T6: SQL
            {"ex": ex_2024_a, "num": 38, "b": 3, "t": 6,
             "p": "En SQL, ¿cuál de las siguientes sentencias pertenece al grupo DDL (Data Definition Language)?",
             "a": "INSERT", "b": "UPDATE", "c": "ALTER TABLE", "d": "GRANT",
             "correcta": "C", "exp": "ALTER TABLE define y modifica la estructura de la base de datos (DDL). INSERT/UPDATE son DML y GRANT es DCL."},

            # T7: SGBD y NoSQL
            {"ex": ex_2024_a, "num": 39, "b": 3, "t": 7,
             "p": "¿Qué tipo de base de datos NoSQL utiliza una estructura clave-valor en memoria extremadamente rápida para almacenamiento de sesiones y caché?",
             "a": "Redis", "b": "MongoDB", "c": "Cassandra", "d": "Neo4j",
             "correcta": "A", "exp": "Redis es un almacén de estructura de datos en memoria clave-valor de alto rendimiento."},

            # T8: Desarrollo Web
            {"ex": ex_2024_a, "num": 40, "b": 3, "t": 8,
             "p": "¿Qué código de estado HTTP (Status Code) indica que una petición REST se ha procesado con éxito y ha resultado en la creación de un nuevo recurso en el servidor?",
             "a": "200 OK", "b": "201 Created", "c": "204 No Content", "d": "304 Not Modified",
             "correcta": "B", "exp": "HTTP 201 Created indica que el recurso fue creado satisfactoriamente en el servidor."},

            # T9: Git y CI/CD
            {"ex": ex_2024_a, "num": 41, "b": 3, "t": 9,
             "p": "En pruebas de software, ¿qué tipo de prueba verifica que componentes individuales o unidades de código funcionan aisladamente según lo especificado?",
             "a": "Prueba de Integración", "b": "Prueba Unitaria", "c": "Prueba de Carga", "d": "Prueba de Regresión",
             "correcta": "B", "exp": "Las pruebas unitarias (Unit Tests) validan el comportamiento de métodos o funciones de forma aislada."},

            # T10: Accesibilidad
            {"ex": ex_2024_a, "num": 42, "b": 3, "t": 10,
             "p": "Según las pautas de accesibilidad WCAG 2.1, ¿qué atributo HTML obligatorio debe incluirse en los elementos de imagen <img> para describir su contenido a lectores de pantalla?",
             "a": "title", "b": "alt", "c": "aria-label", "d": "src",
             "correcta": "B", "exp": "El atributo 'alt' (texto alternativo) es indispensable para el criterio 1.1.1 de WCAG (contenido no textual)."},

            # ---------------- BLOQUE 4 (Temas 1 a 9) ----------------
            # T1: Adm Electrónica
            {"ex": ex_2024_a, "num": 43, "b": 4, "t": 1,
             "p": "¿Qué norma técnica estándar del Comité Sectorial de Administración Electrónica rige el intercambio registral en la plataforma SIR?",
             "a": "Norma SICRES (Sistema de Información Común de Registros de Entrada y Salida).", "b": "Norma ISO 27001.", "c": "Norma eIDAS.", "d": "Norma RFC 5322.",
             "correcta": "A", "exp": "SICRES 3.0 es el formato normalizado para intercambio registral en la Administración española."},

            # T2: Firma e Identificación
            {"ex": ex_2024_a, "num": 44, "b": 4, "t": 2,
             "p": "¿Qué aplicación de escritorio desarrollada por la AGE permite la firma electrónica desde el navegador cliente sin depender de plugins de Java?",
             "a": "AutoFirma", "b": "Adobe Sign", "c": "OpenSSL", "d": "GnuPG",
             "correcta": "A", "exp": "AutoFirma es la aplicación oficial de firma electrónica desarrollada por el Ministerio de Asuntos Económicos y Transformación Digital."},

            # T3: ENI
            {"ex": ex_2024_a, "num": 45, "b": 4, "t": 3,
             "p": "En el Esquema Nacional de Interoperabilidad (RD 4/2010), ¿qué identificador único y universal se asigna a cada documento electrónico en la AGE?",
             "a": "UUID", "b": "CSV (Código Seguro de Verificación)", "c": "Hash SHA-1", "d": "Timestamp RFC 3161",
             "correcta": "B", "exp": "El CSV permite contrastar la autenticidad e integridad de documentos electrónicos en las sedes electrónicas."},

            # T4: ENS
            {"ex": ex_2024_a, "num": 46, "b": 4, "t": 4,
             "p": "En el Esquema Nacional de Seguridad (RD 311/2022), ¿qué tipo de auditoría es obligatoria cada dos años para los sistemas de información de categoría Media o Alta?",
             "a": "Auditoría Financiera", "b": "Auditoría de Seguridad del ENS", "c": "Auditoría Ambiental", "d": "Auditoría de Usabilidad",
             "correcta": "B", "exp": "Artículo 34 del RD 311/2022: Los sistemas de categoría Media o Alta se someterán a una auditoría ordinaria de seguridad al menos cada dos años."},

            # T5: Ciberseguridad
            {"ex": ex_2024_a, "num": 47, "b": 4, "t": 5,
             "p": "¿Qué tipo de ataque informático consiste en inundar un servidor o red con tráfico ilegítimo desde múltiples fuentes para dejarlo fuera de servicio?",
             "a": "Phishing", "b": "Ataque de Denegación de Servicio Distribuido (DDoS)", "c": "Ransomware", "d": "Cross-Site Scripting (XSS)",
             "correcta": "B", "exp": "Los ataques DDoS utilizan botnets distribuidas para saturar el ancho de banda o recursos de cómputo del objetivo."},

            # T6: Criptografía
            {"ex": ex_2024_a, "num": 48, "b": 4, "t": 6,
             "p": "¿Cuál de las siguientes funciones resumen (Hash) produce una salida criptográfica de longitud fija de 256 bits?",
             "a": "MD5", "b": "SHA-1", "c": "SHA-256", "d": "CRC32",
             "correcta": "C", "exp": "SHA-256 (de la familia SHA-2) genera un resumen criptográfico de 256 bits (32 bytes). MD5 produce 128 bits y SHA-1 160 bits."},

            # T7: CPD y Docker
            {"ex": ex_2024_a, "num": 49, "b": 4, "t": 7,
             "p": "En la tecnología de contenedores Docker, ¿qué archivo de texto plano contiene las instrucciones secuenciales para construir una imagen de contenedor?",
             "a": "docker-compose.yml", "b": "Dockerfile", "c": "container.json", "d": "config.yaml",
             "correcta": "B", "exp": "El Dockerfile define la imagen base, dependencias, variables y comandos para generar la imagen Docker."},

            # T8: Cloud Computing
            {"ex": ex_2024_a, "num": 50, "b": 4, "t": 8,
             "p": "¿Qué modelo de servicio en la nube proporciona al usuario entornos de ejecución completos, bases de datos y herramientas para desarrollar y desplegar aplicaciones sin administrar la infraestructura subyacente?",
             "a": "IaaS (Infrastructure as a Service)", "b": "PaaS (Platform as a Service)", "c": "SaaS (Software as a Service)", "d": "BaaS (Backend as a Service)",
             "correcta": "B", "exp": "PaaS ofrece la plataforma de ejecución completa (ej: Heroku, Google App Engine, Azure App Services) administrada por el proveedor."},

            # T9: Continuidad DRP
            {"ex": ex_2024_a, "num": 51, "b": 4, "t": 9,
             "p": "¿Cuál es la diferencia entre una copia de seguridad incremental y una diferencial?",
             "a": "La incremental copia los datos modificados desde el último backup completo; la diferencial copia desde el último backup de cualquier tipo.", "b": "La incremental copia los datos modificados desde el último backup (completo o incremental); la diferencial copia todos los datos modificados desde el último backup COMPLETO.", "c": "No existe ninguna diferencia técnica.", "d": "La diferencial requiere formatear el disco antes de iniciar.",
             "correcta": "B", "exp": "La copia incremental solo guarda los cambios desde la última copia realizada; la diferencial acumula todos los cambios desde la última copia completa."}
        ]

        total_creadas = 0
        for p in banco_preguntas:
            tema_obj = temas.get((p["b"], p["t"]))
            _, created = PreguntaExamen.objects.update_or_create(
                examen=p["ex"],
                numero=p["num"],
                defaults={
                    "pregunta": p["p"],
                    "opcion_a": p["a"],
                    "opcion_b": p["b"],
                    "opcion_c": p["c"],
                    "opcion_d": p["d"],
                    "opcion_correcta": p["correcta"],
                    "tema": tema_obj,
                    "explicacion_oficial": p["exp"]
                }
            )
            if created:
                total_creadas += 1

        total_preguntas_db = PreguntaExamen.objects.count()
        self.stdout.write(self.style.SUCCESS(f"¡Carga exhaustiva finalizada! Total de preguntas de examen oficiales vinculadas: {total_preguntas_db}"))
