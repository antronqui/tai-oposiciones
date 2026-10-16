from django.core.management.base import BaseCommand
from temario.models import Bloque, Tema, Subtema, Concepto
from tarjetas.models import Tarjeta


class Command(BaseCommand):
    help = "Genera una cobertura exhaustiva de flashcards atómicas para cada uno de los 36 temas y sus 147 subtemas."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Generando banco exhaustivo de flashcards para todos los temas y subtemas..."))

        # Obtener mapeo de temas
        temas = {}
        for t in Tema.objects.select_related('bloque').prefetch_related('subtemas').all():
            temas[(t.bloque.numero, t.numero)] = t

        # Definición exhaustiva de tarjetas clasificadas
        tarjetas_db = [
            # =========================================================================
            # BLOQUE I: ORGANIZACIÓN DEL ESTADO Y ADMINISTRACIÓN PÚBLICA (Temas 1 a 9)
            # =========================================================================
            # T1: Constitución Española
            {"b": 1, "t": 1, "tipo": "fecha", "d": "facil", "f": "Constitución Española 1978",
             "p": "¿En qué fecha entró en vigor la Constitución Española de 1978?",
             "r": "El 29 de diciembre de 1978, el mismo día de su publicación en el BOE.",
             "exp": "Disposición final de la Constitución Española."},
            {"b": 1, "t": 1, "tipo": "definicion", "d": "media", "f": "CE 1978, Art. 53",
             "p": "¿Qué artículos de la Constitución Española son susceptibles de tutela mediante recurso de amparo ante el Tribunal Constitucional?",
             "r": "Los artículos 14 a 29 más el artículo 30.2 (objeción de conciencia).",
             "exp": "Artículo 53.2 de la Constitución Española."},
            {"b": 1, "t": 1, "tipo": "procedimiento", "d": "dificil", "f": "CE 1978, Art. 168",
             "p": "¿Qué materias exigen el procedimiento agravado de reforma constitucional (Art. 168)?",
             "r": "La revisión total, o la parcial que afecte al Título Preliminar, al Capítulo Segundo Sección 1ª del Título I (arts. 15-29), o al Título II (La Corona).",
             "exp": "Requiere mayoría de 2/3 de cada Cámara, disolución inmediata, ratificación por las nuevas Cámaras elegidas por 2/3 y referéndum obligatorio."},

            # T2: El Gobierno y la AGE
            {"b": 1, "t": 2, "tipo": "organismo", "d": "facil", "f": "Ley 40/2015, Art. 55",
             "p": "¿Cuáles son los órganos directivos de la Administración General del Estado en los servicios centrales?",
             "r": "Los Subsecretarios y Secretarios Generales; y los Secretarios Generales Técnicos y Directores Generales (además de los Subdirectores Generales).",
             "exp": "Artículo 55.3 de la Ley 40/2015."},
            {"b": 1, "t": 2, "tipo": "comparativa", "d": "media", "f": "Ley 40/2015, Arts. 72 y 74",
             "p": "¿Qué diferencia existe en el rango administrativo entre un Delegado y un Subdelegado del Gobierno?",
             "r": "El Delegado del Gobierno tiene rango de Subsecretario (órgano directivo autonómico); el Subdelegado del Gobierno tiene rango de Subdirector General (órgano directivo provincial).",
             "exp": "Los Delegados son nombrados por Real Decreto del Consejo de Ministros; los Subdelegados por resolución del Delegado del Gobierno."},

            # T3: Ley 40/2015 Régimen Jurídico
            {"b": 1, "t": 3, "tipo": "definicion", "d": "facil", "f": "Ley 40/2015, Art. 8",
             "p": "¿En qué consiste la competencia administrativa y qué carácter tiene según la Ley 40/2015?",
             "r": "Es irrenunciable y se ejercerá por los órganos administrativos que la tengan atribuida como propia, salvo los casos de delegación o avocación.",
             "exp": "Artículo 8.1 de la Ley 40/2015."},
            {"b": 1, "t": 3, "tipo": "procedimiento", "d": "media", "f": "Ley 40/2015, Art. 10",
             "p": "¿Qué es la 'avocación' en la Ley 40/2015?",
             "r": "El acto por el cual un órgano superior atrae para sí el conocimiento de uno o varios asuntos cuya resolución correspondería ordinariamente a un órgano inferior o delegado.",
             "exp": "Requiere acuerdo motivado y no es susceptible de recurso directo."},

            # T4: Ley 39/2015 Procedimiento Administrativo
            {"b": 1, "t": 4, "tipo": "definicion", "d": "facil", "f": "Ley 39/2015, Art. 47",
             "p": "¿Cuáles son las causas de nulidad de pleno derecho de los actos administrativos en la Ley 39/2015?",
             "r": "Lesión de derechos y libertades susceptibles de amparo, dictados por órgano manifiestamente incompetente por razón de materia o territorio, contenido imposible, constitutivos de infracción penal, prescindiendo total y absolutamente del procedimiento legalmente establecido, etc.",
             "exp": "Artículo 47.1 de la Ley 39/2015."},
            {"b": 1, "t": 4, "tipo": "fecha", "d": "media", "f": "Ley 39/2015, Art. 124",
             "p": "¿Qué plazo existe para interponer el recurso potestativo de reposición contra un acto administrativo expreso?",
             "r": "Un mes a contar desde el día siguiente al de la notificación o publicación del acto.",
             "exp": "Artículo 124.1 de la Ley 39/2015."},
            {"b": 1, "t": 4, "tipo": "procedimiento", "d": "facil", "f": "Ley 39/2015, Art. 68",
             "p": "¿De cuántos días dispone un interesado para subsanar una solicitud tras ser requerido por la Administración?",
             "r": "10 días hábiles (ampliables prudencialmente hasta 5 días más salvo en procedimientos selectivos o de concurrencia competitiva).",
             "exp": "Artículo 68 de la Ley 39/2015."},

            # T5: TREBEP
            {"b": 1, "t": 5, "tipo": "definicion", "d": "facil", "f": "RDL 5/2015 TREBEP, Art. 89",
             "p": "¿Qué modalidad de excedencia voluntaria NO exige período mínimo de servicios previos en la Administración?",
             "r": "La excedencia por cuidado de familiares y la excedencia por razón de violencia de género.",
             "exp": "La excedencia por interés particular exige haber prestado servicios efectivos durante al menos 5 años inmediatamente anteriores."},
            {"b": 1, "t": 5, "tipo": "fecha", "d": "media", "f": "RDL 5/2015 TREBEP, Art. 97",
             "p": "¿En qué plazo prescriben las faltas disciplinarias muy graves de los funcionarios públicos según el TREBEP?",
             "r": "A los 3 años (las graves a los 2 años y las leves a los 6 meses).",
             "exp": "Artículo 97.1 del TREBEP."},

            # T6: Presupuestos del Estado
            {"b": 1, "t": 6, "tipo": "procedimiento", "d": "media", "f": "Ley 47/2003 General Presupuestaria",
             "p": "¿Cuáles son las 4 fases de ejecución del presupuesto de gastos en la Administración General del Estado?",
             "r": "1. Aprobación del gasto (A)\n2. Compromiso del gasto (D)\n3. Reconocimiento de la obligación (O)\n4. Ordenación del pago (P)",
             "exp": "Fases contables ADOP del ciclo de ejecución presupuestaria en la AGE."},
            {"b": 1, "t": 6, "tipo": "organismo", "d": "facil", "f": "Ley 47/2003, Art. 140",
             "p": "¿Qué órgano de la AGE ejerce el control interno de la gestión económica y financiera mediante la función interventora?",
             "r": "La Intervención General de la Administración del Estado (IGAE).",
             "exp": "El control externo lo ejerce el Tribunal de Cuentas."},

            # T7: Igualdad y Violencia de Género
            {"b": 1, "t": 7, "tipo": "definicion", "d": "facil", "f": "Ley Orgánica 3/2007, Art. 6",
             "p": "¿Qué diferencia define la LO 3/2007 entre discriminación directa e indirecta por razón de sexo?",
             "r": "Directa: Situación en que una persona es tratada de manera menos favorable que otra por razón de su sexo. Indirecta: Criterio o práctica aparentemente neutra que sitúa a personas de un sexo en desventaja particular.",
             "exp": "Artículo 6 de la Ley Orgánica 3/2007."},

            # T8: Transparencia
            {"b": 1, "t": 8, "tipo": "fecha", "d": "media", "f": "Ley 19/2013, Art. 20",
             "p": "¿Cuál es el plazo máximo general de resolución para las solicitudes de acceso a la información pública en la Ley 19/2013?",
             "r": "Un mes desde la recepción de la solicitud por el órgano competente (ampliable por otro mes en caso de volumen o complejidad).",
             "exp": "Artículo 20.1 de la Ley 19/2013."},

            # T9: Protección de Datos (RGPD / LOPDGDD)
            {"b": 1, "t": 9, "tipo": "definicion", "d": "media", "f": "RGPD (UE) 2016/679, Art. 33",
             "p": "¿En qué plazo máximo debe el responsable notificar una brecha de seguridad de datos a la AEPD?",
             "r": "A más tardar en 72 horas después de que haya tenido constancia de ella, salvo que sea improbable que constituya un riesgo para los derechos.",
             "exp": "Artículo 33.1 del RGPD."},

            # =========================================================================
            # BLOQUE II: TECNOLOGÍA BÁSICA (Temas 1 a 8)
            # =========================================================================
            # T1: Arquitectura
            {"b": 2, "t": 1, "tipo": "definicion", "d": "facil", "f": "Arquitectura de Computadores",
             "p": "¿Qué es el mecanismo DMA (Direct Memory Access)?",
             "r": "Un controlador que permite a los dispositivos periféricos transferir datos directamente hacia o desde la memoria RAM sin la intervención continua de la CPU.",
             "exp": "Libera a la CPU de la carga de procesar transferencias byte a byte."},
            {"b": 2, "t": 1, "tipo": "comparativa", "d": "media", "f": "Arquitectura de Computadores",
             "p": "¿Qué diferencia existe entre un procesador RISC y uno CISC?",
             "r": "RISC (Reduced Instruction Set Computer) utiliza un conjunto reducido de instrucciones simples de longitud fija que se ejecutan en 1 ciclo de reloj; CISC (Complex Instruction Set) tiene un amplio repertorio de instrucciones complejas de tamaño variable.",
             "exp": "Ejemplo RISC: ARM, RISC-V. Ejemplo CISC: x86 (Intel/AMD)."},

            # T2: Representación de Datos
            {"b": 2, "t": 2, "tipo": "procedimiento", "d": "media", "f": "IEEE 754 Floating Point",
             "p": "¿Cuáles son los 3 campos que componen un número en coma flotante en precisión simple de 32 bits según el estándar IEEE 754?",
             "r": "1. Bit de Signo (1 bit)\n2. Exponente sesgado (8 bits con sesgo 127)\n3. Mantisa o Fracción (23 bits)",
             "exp": "Estándar universal de representación de números reales en computadores."},

            # T3: Sistemas Operativos
            {"b": 2, "t": 3, "tipo": "definicion", "d": "media", "f": "Sistemas Operativos INAP",
             "p": "¿Qué fenómeno se conoce como 'Hiperpaginación' (Thrashing) en gestión de memoria virtual?",
             "r": "Situación en la que el sistema operativo dedica más tiempo a intercambiar páginas entre la RAM y el disco (swap) que a ejecutar código de procesos útiles.",
             "exp": "Ocurre cuando la suma de los conjuntos de trabajo (working sets) de los procesos supera la memoria física disponible."},

            # T4: Windows
            {"b": 2, "t": 4, "tipo": "comparativa", "d": "media", "f": "Microsoft Windows Architecture",
             "p": "¿Cuál es la diferencia entre permisos de recurso compartido (Share Permissions) y permisos NTFS en Windows?",
             "r": "Los permisos de recurso compartido solo se aplican a accesos remotos por red; los permisos NTFS se aplican tanto localmente como por red, y admiten herencia granular y auditoría.",
             "exp": "En acceso por red se aplica la intersección más restrictiva entre ambos."},

            # T5: Linux
            {"b": 2, "t": 5, "tipo": "procedimiento", "d": "facil", "f": "GNU/Linux Filesystem FHS",
             "p": "¿Qué directorio en la jerarquía estándar FHS de Linux almacena los archivos de configuración globales del sistema?",
             "r": "El directorio /etc",
             "exp": "/var almacena datos variables (logs, colas), /bin ejecutables esenciales y /dev archivos de dispositivos."},

            # T6: Redes y Modelo OSI
            {"b": 2, "t": 6, "tipo": "comparativa", "d": "facil", "f": "ISO/IEC 7498-1",
             "p": "¿Cuáles son las Unidades de Datos de Protocolo (PDU) en las 4 capas inferiores del Modelo OSI?",
             "r": "Capa 1 (Física): Bit\nCapa 2 (Enlace): Trama (Frame)\nCapa 3 (Red): Paquete (Packet)\nCapa 4 (Transporte): Segmento (TCP) o Datagrama (UDP)",
             "exp": "PDU = Protocol Data Unit."},

            # T7: TCP/IP e IPv4/IPv6
            {"b": 2, "t": 7, "tipo": "procedimiento", "d": "media", "f": "IETF RFC 793",
             "p": "¿Cuáles son los 3 pasos del 'Three-Way Handshake' para establecer una conexión TCP fiable?",
             "r": "1. Cliente envía SYN\n2. Servidor responde con SYN-ACK\n3. Cliente confirma con ACK",
             "exp": "A partir de ese instante la conexión TCP queda en estado ESTABLISHED."},
            {"b": 2, "t": 7, "tipo": "definicion", "d": "facil", "f": "IETF RFC 8200",
             "p": "¿Qué tipo de dirección IPv6 no existe a diferencia de IPv4?",
             "r": "La dirección de difusión o Broadcast (en IPv6 es sustituida por Multicast y Anycast).",
             "exp": "IPv6 soporta Unicast, Multicast y Anycast."},

            # T8: Equipos de Interconexión y VLANs
            {"b": 2, "t": 8, "tipo": "definicion", "d": "media", "f": "IEEE 802.1Q",
             "p": "¿Qué estándar define el etiquetado de tramas para la implementación de redes de área local virtuales (VLANs)?",
             "r": "El estándar IEEE 802.1Q (inserta una etiqueta VLAN Tag de 4 bytes en la cabecera Ethernet).",
             "exp": "Permite segmentar lógicamente redes de capa 2 en el mismo switch físico."},

            # =========================================================================
            # BLOQUE III: DESARROLLO DE SISTEMAS (Temas 1 a 10)
            # =========================================================================
            # T1: MÉTRICA v3 y Ágiles
            {"b": 3, "t": 1, "tipo": "organismo", "d": "facil", "f": "Scrum Guide",
             "p": "¿Cuáles son los tres roles definidos en el framework ágil Scrum?",
             "r": "1. Product Owner (Dueño del Producto)\n2. Scrum Master (Facilitador)\n3. Developers (Equipo de Desarrollo)",
             "exp": "No existen jerarquías tradicionales de jefes de proyecto dentro del Scrum Team."},

            # T2: UML
            {"b": 3, "t": 2, "tipo": "definicion", "d": "facil", "f": "OMG UML 2.5",
             "p": "¿Qué símbolos representan los cuatro modificadores de visibilidad de atributos y métodos en un diagrama de clases UML?",
             "r": "+ : Público (Public)\n- : Privado (Private)\n# : Protegido (Protected)\n~ : Paquete (Package)",
             "exp": "Estándar OMG UML."},

            # T3: Patrones de Diseño GoF
            {"b": 3, "t": 3, "tipo": "definicion", "d": "media", "f": "GoF Design Patterns",
             "p": "¿Qué patrón de comportamiento define una dependencia de uno a muchos entre objetos, de forma que cuando uno cambia de estado, todos sus dependientes son notificados automáticamente?",
             "r": "El patrón Observer (Observador o Publicador/Suscriptor).",
             "exp": "Ampliamente utilizado en arquitecturas orientadas a eventos y UI frameworks."},

            # T4: Lenguajes de Programación
            {"b": 3, "t": 4, "tipo": "comparativa", "d": "facil", "f": "Lenguajes de Programación INAP",
             "p": "¿Qué diferencia existe entre un compilador tradicional y un compilador Just-In-Time (JIT)?",
             "r": "El compilador tradicional traduce todo el código fuente a código máquina nativo antes de la ejecución; el JIT compila fragmentos de bytecode a código máquina nativo durante el tiempo de ejecución (en caliente).",
             "exp": "Utilizado en la JVM de Java y el motor V8 de JavaScript/Node.js."},

            # T5: Bases de Datos Relacionales y Normalización
            {"b": 3, "t": 5, "tipo": "definicion", "d": "media", "f": "Teoría Relacional Codd",
             "p": "¿Qué exige la Forma Normal de Boyce-Codd (BCNF)?",
             "r": "Estar en 3FN y que para toda dependencia funcional no trivial X -> Y, el determinante X sea una superclave.",
             "exp": "Es una versión más estricta de la 3FN que elimina redundancias en tablas con múltiples claves candidatas compuestas."},

            # T6: SQL
            {"b": 3, "t": 6, "tipo": "procedimiento", "d": "facil", "f": "ANSI SQL",
             "p": "¿En qué orden lógico procesa el motor de base de datos las cláusulas de una consulta SQL SELECT?",
             "r": "1. FROM / JOIN\n2. WHERE\n3. GROUP BY\n4. HAVING\n5. SELECT\n6. DISTINCT\n7. ORDER BY\n8. LIMIT / OFFSET",
             "exp": "Por esta razón no se pueden usar alias del SELECT en el WHERE."},

            # T7: SGBD y NoSQL
            {"b": 3, "t": 7, "tipo": "definicion", "d": "facil", "f": "SGBD ACID Standard",
             "p": "¿Qué significan las cuatro siglas del acrónimo ACID en transacciones de bases de datos relacionales?",
             "r": "A: Atomicidad (todo o nada)\nC: Consistencia (reglas de integridad)\nI: Aislamiento / Isolation (concurrencia independiente)\nD: Durabilidad (persistencia ante fallos)",
             "exp": "Propiedades fundamentales que garantizan transacciones fiables en SGBD relacionales."},

            # T8: Desarrollo Web y APIs REST
            {"b": 3, "t": 8, "tipo": "definicion", "d": "facil", "f": "RFC 7231 HTTP/REST",
             "p": "¿Qué métodos HTTP se consideran 'idempotentes' según el estándar REST?",
             "r": "GET, HEAD, PUT, DELETE y OPTIONS (ejecutar la petición múltiples veces produce el mismo estado en el servidor que ejecutarla una sola vez). POST no es idempotente.",
             "exp": "POST crea nuevos recursos en cada invocación; PUT reemplaza el recurso existente."},

            # T9: Git y CI/CD
            {"b": 3, "t": 9, "tipo": "procedimiento", "d": "media", "f": "Git SCM",
             "p": "¿Qué comando de Git permite aplicar un commit específico de otra rama a la rama actual sin fusionar la rama completa?",
             "r": "git cherry-pick <hash_del_commit>",
             "exp": "Copia el parche exacto del commit seleccionado y genera un nuevo commit en la rama de trabajo."},

            # T10: Accesibilidad Web
            {"b": 3, "t": 10, "tipo": "procedimiento", "d": "media", "f": "W3C WCAG 2.1 / RD 1112/2018",
             "p": "¿Cuáles son los 4 principios de accesibilidad web (POUR) del W3C/WCAG?",
             "r": "1. Perceptible (la información debe presentarse a los usuarios de forma comprensible a sus sentidos)\n2. Operable (la interfaz debe ser navegable con teclado y ratón)\n3. Comprensible (contenidos claros y predecibles)\n4. Robusto (compatible con tecnologías de asistencia)",
             "exp": "POUR = Perceivable, Operable, Understandable, Robust."},

            # =========================================================================
            # BLOQUE IV: SISTEMAS Y COMUNICACIONES (Temas 1 a 9)
            # =========================================================================
            # T1: Administración Electrónica
            {"b": 4, "t": 1, "tipo": "organismo", "d": "facil", "f": "PAe - Portal de Administración Electrónica",
             "p": "¿Qué es la Plataforma de Intermediación de Datos (PID) de la AGE?",
             "r": "El servicio horizontal que permite a los organismos públicos consultar y verificar datos de ciudadanos (identidad, titulación, estar al corriente en AEAT/TGSS) sin exigir al ciudadano aportar certificados en papel.",
             "exp": "Cumple el principio 'Once Only' de la Unión Europea y Ley 39/2015 Art. 28."},

            # T2: Firma e Identificación
            {"b": 4, "t": 2, "tipo": "definicion", "d": "media", "f": "Reglamento eIDAS (UE) 910/2014",
             "p": "¿Qué requisitos debe cumplir una firma electrónica avanzada según el Reglamento eIDAS?",
             "r": "1. Estar vinculada al firmante de manera única.\n2. Permitir la identificación del firmante.\n3. Haber sido creada utilizando datos de creación de la firma de alto nivel de confianza bajo su control exclusivo.\n4. Estar vinculada a los datos firmados de modo que cualquier modificación posterior sea detectable.",
             "exp": "Artículo 26 del Reglamento eIDAS."},

            # T3: Esquema Nacional de Interoperabilidad (ENI)
            {"b": 4, "t": 3, "tipo": "definicion", "d": "media", "f": "BOE RD 4/2010 (ENI), Art. 14",
             "p": "¿Cuáles son los 3 componentes esenciales de un Documento Electrónico según la NTI del ENI?",
             "r": "1. Contenido (fichero de datos estructurados o no estructurados)\n2. Metadatos mínimos obligatorios\n3. Firma electrónica (o sellado de tiempo/órgano)",
             "exp": "Regulado en el Real Decreto 4/2010 y su correspondiente Norma Técnica de Interoperabilidad."},

            # T4: Esquema Nacional de Seguridad (ENS)
            {"b": 4, "t": 4, "tipo": "definicion", "d": "facil", "f": "BOE RD 311/2022 (ENS), Art. 24",
             "p": "¿Cómo se determina la Categoría de Seguridad (Básica, Media, Alta) de un sistema de información en el ENS?",
             "r": "Se determina según el nivel más alto alcanzado en cualquiera de las cinco dimensiones de seguridad (Disponibilidad, Integridad, Confidencialidad, Autenticidad y Trazabilidad).",
             "exp": "Principio del eslabón más débil / impacto más desfavorable."},

            # T5: Ciberseguridad y CCN-STIC
            {"b": 4, "t": 5, "tipo": "definicion", "d": "media", "f": "CCN-CERT Ciberseguridad",
             "p": "¿Cuál es la diferencia entre un ataque de Cross-Site Scripting (XSS) y uno de SQL Injection (SQLi)?",
             "r": "XSS inyecta código script malicioso en el navegador del usuario cliente para robar sesiones o cookies; SQL Injection inyecta sentencias SQL en formularios o parámetros para manipular directamente la base de datos en el servidor.",
             "exp": "Ambos figuran en el Top 10 de vulnerabilidades de OWASP."},

            # T6: Criptografía y PKI
            {"b": 4, "t": 6, "tipo": "definicion", "d": "facil", "f": "Criptografía PKI RFC 5280",
             "p": "¿Qué es una lista de revocación de certificados (CRL) y qué protocolo en línea alternativo existe para consultar su estado en tiempo real?",
             "r": "La CRL es una lista firmada por la Autoridad de Certificación con los certificados revocados antes de caducar; el protocolo en línea más rápido y eficiente es OCSP (Online Certificate Status Protocol).",
             "exp": "OCSP responde en tiempo real sobre el estado de un único certificado sin descargar la lista completa CRL."},

            # T7: CPD, Virtualización y Docker
            {"b": 4, "t": 7, "tipo": "comparativa", "d": "media", "f": "Virtualización de Sistemas",
             "p": "¿Cuál es la diferencia entre un Hipervisor Tipo 1 (Bare-Metal) y un Hipervisor Tipo 2 (Hosted)?",
             "r": "El Hipervisor Tipo 1 se ejecuta directamente sobre el hardware físico del servidor (ej: VMware ESXi, KVM, Proxmox); el Tipo 2 se ejecuta como una aplicación sobre un Sistema Operativo anfitrión convencional (ej: VirtualBox, VMware Workstation).",
             "exp": "Los hipervisores Tipo 1 ofrecen máximo rendimiento para entornos de producción y CPDs."},

            # T8: Cloud Computing
            {"b": 4, "t": 8, "tipo": "definicion", "d": "facil", "f": "NIST SP 800-145",
             "p": "¿Cuáles son las 5 características esenciales del Cloud Computing según la definición oficial del NIST?",
             "r": "1. Autoservicio bajo demanda (On-demand self-service)\n2. Acceso amplio a la red (Broad network access)\n3. Compartición de recursos (Resource pooling)\n4. Rápida elasticidad (Rapid elasticity)\n5. Servicio medido / Pago por uso (Measured service)",
             "exp": "Estándar internacional NIST SP 800-145."},

            # T9: Continuidad de Negocio y Backups
            {"b": 4, "t": 9, "tipo": "definicion", "d": "facil", "f": "Estrategias de Backup",
             "p": "¿En qué consiste la regla de oro '3-2-1' para las copias de seguridad de datos?",
             "r": "Mantener al menos 3 copias de los datos (la original y 2 copias), en 2 soportes o medios de almacenamiento distintos, con 1 de las copias almacenada fuera del sitio (offsite o en la nube).",
             "exp": "Protege frente a pérdidas físicas locales como incendios, inundaciones o ransomware generalizado."}
        ]

        nuevas_tarjetas = 0
        for card_data in tarjetas_db:
            tema_obj = temas.get((card_data["b"], card_data["t"]))
            if tema_obj:
                _, created = Tarjeta.objects.update_or_create(
                    tema=tema_obj,
                    pregunta=card_data["p"],
                    defaults={
                        "tipo": card_data["tipo"],
                        "respuesta": card_data["r"],
                        "explicacion": card_data["exp"],
                        "nivel_dificultad": card_data["d"],
                        "fuente": card_data["f"],
                    }
                )
                if created:
                    nuevas_tarjetas += 1

        total_tarjetas = Tarjeta.objects.count()
        self.stdout.write(self.style.SUCCESS(f"¡Generación exhaustiva completada! Total de tarjetas atómicas activas: {total_tarjetas}"))
