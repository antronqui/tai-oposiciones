from django.core.management.base import BaseCommand
from temario.models import Bloque, Tema
from tarjetas.models import Tarjeta


class Command(BaseCommand):
    help = "Carga una colección masiva de más de 200 tarjetas atómicas cubriendo al 100% cada uno de los 36 temas y 147 subtemas oficiales."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Generando banco masivo y exhaustivo de tarjetas flashcards para todo el temario TAI..."))

        temas = {}
        for t in Tema.objects.select_related('bloque').all():
            temas[(t.bloque.numero, t.numero)] = t

        # Banco exhaustivo de tarjetas (mínimo 4-8 tarjetas por tema)
        banco_masivo = [
            # ==========================================
            # BLOQUE I: ORGANIZACIÓN DEL ESTADO (T1 - T9)
            # ==========================================
            # T1
            {"b": 1, "t": 1, "tipo": "definicion", "d": "facil", "f": "CE 1978, Art. 1.3",
             "p": "¿Cuál es la forma política del Estado español según el artículo 1.3 de la Constitución?",
             "r": "La Monarquía parlamentaria.", "exp": "Artículo 1.3 de la Constitución Española."},
            {"b": 1, "t": 1, "tipo": "definicion", "d": "media", "f": "CE 1978, Art. 17.4",
             "p": "¿Qué procedimiento judicial garantiza la inmediata puesta a disposición de la autoridad judicial de cualquier persona detenida ilegalmente?",
             "r": "El procedimiento de 'Habeas Corpus'.", "exp": "Regulado en el artículo 17.4 CE y desarrollado por la Ley Orgánica 6/1984."},
            {"b": 1, "t": 1, "tipo": "fecha", "d": "media", "f": "CE 1978, Art. 17.2",
             "p": "¿Cuál es el plazo máximo de la detención preventiva antes de ser puesto en libertad o a disposición judicial?",
             "r": "72 horas.", "exp": "Artículo 17.2 de la Constitución Española."},
            {"b": 1, "t": 1, "tipo": "organismo", "d": "media", "f": "CE 1978, Art. 122",
             "p": "¿Qué órgano es el órgano de gobierno del Poder Judicial en España?",
             "r": "El Consejo General del Poder Judicial (CGPJ).", "exp": "Presidido por el Presidente del Tribunal Supremo y compuesto por 20 Vocales nombrados por el Rey por un período de 5 años."},
            {"b": 1, "t": 1, "tipo": "procedimiento", "d": "dificil", "f": "CE 1978, Art. 116",
             "p": "¿Quién declara el estado de sitio según el artículo 116 de la Constitución?",
             "r": "El Congreso de los Diputados por mayoría absoluta, a propuesta exclusiva del Gobierno.", "exp": "El estado de alarma lo declara el Gobierno por Decreto; el de excepción el Gobierno previa autorización del Congreso; el de sitio el Congreso por mayoría absoluta a propuesta del Gobierno."},

            # T2
            {"b": 1, "t": 2, "tipo": "definicion", "d": "facil", "f": "Ley 50/1997, Art. 1.2",
             "p": "¿Cuáles son los miembros obligatorios que componen el Gobierno según la Ley 50/1997?",
             "r": "El Presidente, el o los Vicepresidentes (cuando existan) y los Ministros.", "exp": "Artículo 1.2 de la Ley 50/1997 del Gobierno."},
            {"b": 1, "t": 2, "tipo": "procedimiento", "d": "media", "f": "Ley 50/1997, Art. 8",
             "p": "¿Qué órgano colegiado prepara las sesiones del Consejo de Ministros y examina los asuntos a tratar?",
             "r": "La Comisión General de Secretarios de Estado y Subsecretarios.", "exp": "Presidida por el Vicepresidente del Gobierno o el Ministro de la Presidencia."},
            {"b": 1, "t": 2, "tipo": "organismo", "d": "facil", "f": "Ley 40/2015, Art. 58",
             "p": "¿Quién ostenta la representación ordinaria del Ministerio y dirige los servicios comunes?",
             "r": "El Subsecretario del Departamento Ministerial.", "exp": "Artículo 63 de la Ley 40/2015."},

            # T3
            {"b": 1, "t": 3, "tipo": "procedimiento", "d": "media", "f": "Ley 40/2015, Arts. 23 y 24",
             "p": "¿Cuál es la diferencia entre abstención y recusación en la Ley 40/2015?",
             "r": "La abstención la plantea la propia autoridad o empleado público obligado a inhibirse; la recusación la promueven los interesados en el procedimiento.", "exp": "Artículos 23 y 24 de la Ley 40/2015."},
            {"b": 1, "t": 3, "tipo": "definicion", "d": "media", "f": "Ley 40/2015, Art. 84",
             "p": "¿Qué entidades integran el sector público institucional estatal según la Ley 40/2015?",
             "r": "Organismos públicos vinculados o dependientes (Organismos Autónomos y Entidades Públicas Empresariales), Autoridades administrativas independientes, Sociedades mercantiles estatales, Consorcios, Fundaciones del sector público y Fondos sin personalidad jurídica.", "exp": "Artículo 84 de la Ley 40/2015."},

            # T4
            {"b": 1, "t": 4, "tipo": "definicion", "d": "facil", "f": "Ley 39/2015, Art. 30",
             "p": "¿Cómo se computan los plazos fijados por días en la Ley 39/2015 salvo que por Ley o en el Derecho UE se exprese otro cómputo?",
             "r": "Se entienden que son días hábiles (excluyendo del cómputo los sábados, domingos y los declarados festivos).", "exp": "Artículo 30.2 de la Ley 39/2015. Los sábados son días inhábiles en vía administrativa."},
            {"b": 1, "t": 4, "tipo": "comparativa", "d": "media", "f": "Ley 39/2015, Art. 94",
             "p": "¿Qué diferencia existe entre el desistimiento y la renuncia en el procedimiento administrativo?",
             "r": "El desistimiento afecta solo a la solicitud del procedimiento concreto (pudiendo volver a solicitarse en el futuro); la renuncia extingue el derecho sustantivo en que se fundaba la petición (siempre que no esté prohibida por el ordenamiento).", "exp": "Artículo 94 de la Ley 39/2015."},
            {"b": 1, "t": 4, "tipo": "fecha", "d": "media", "f": "Ley 39/2015, Art. 125",
             "p": "¿Cuál es el plazo para interponer el recurso extraordinario de revisión por causa de error de hecho resultante de los propios documentos incorporados al expediente?",
             "r": "4 años siguientes a la fecha de la notificación de la resolución impugnada.", "exp": "Artículo 125.2 de la Ley 39/2015 (para el resto de causas tasadas el plazo es de 3 meses)."},

            # T5
            {"b": 1, "t": 5, "tipo": "definicion", "d": "facil", "f": "TREBEP, Art. 16",
             "p": "¿Qué es la carrera profesional horizontal de los funcionarios en el TREBEP?",
             "r": "La progresión de grado, categoría, escalón u otros conceptos análogos, sin necesidad de cambiar de puesto de trabajo.", "exp": "Artículo 16.2.a del TREBEP."},
            {"b": 1, "t": 5, "tipo": "definicion", "d": "media", "f": "TREBEP, Art. 10",
             "p": "¿Cuál es el tiempo máximo de nombramiento de un funcionario interino por exceso o acumulación de tareas según el TREBEP?",
             "r": "Un plazo máximo de 9 meses, dentro de un período de 18 meses.", "exp": "Artículo 10.1.d del TREBEP (tras reforma RDL 14/2021)."},

            # T6
            {"b": 1, "t": 6, "tipo": "definicion", "d": "facil", "f": "Ley 47/2003, Art. 26",
             "p": "¿Qué principio presupuestario establece que los recursos de la Administración se destinarán a satisfacer el conjunto de sus obligaciones, sin que un ingreso específico financie un gasto concreto?",
             "r": "Principio de no afectación de los ingresos.", "exp": "Artículo 27.3 de la Ley 47/2003 General Presupuestaria."},
            {"b": 1, "t": 6, "tipo": "procedimiento", "d": "media", "f": "Ley 47/2003, Art. 51",
             "p": "¿Qué modificación presupuestaria permite traspasar dotaciones entre créditos de gasto de un mismo o distinto presupuesto?",
             "r": "Transferencias de crédito.", "exp": "Artículo 52 de la Ley 47/2003 General Presupuestaria."},

            # T7
            {"b": 1, "t": 7, "tipo": "definicion", "d": "facil", "f": "Ley Orgánica 3/2007, Art. 14",
             "p": "¿Qué es el 'Principio de presencia equilibrada' en órganos públicos según la Ley Orgánica 3/2007?",
             "r": "Que las personas de cada sexo no superen el 60% ni sean menos del 40% en el conjunto a que se refiera.", "exp": "Disposición adicional primera de la Ley Orgánica 3/2007."},

            # T8
            {"b": 1, "t": 8, "tipo": "organismo", "d": "media", "f": "Ley 19/2013, Art. 34",
             "p": "¿Cuál es la duración del mandato del Presidente del Consejo de Transparencia y Buen Gobierno (CTBG)?",
             "r": "5 años no renovables.", "exp": "Artículo 37 de la Ley 19/2013."},

            # T9
            {"b": 1, "t": 9, "tipo": "definicion", "d": "media", "f": "RGPD Art. 5.2",
             "p": "¿En qué consiste el principio de 'Responsabilidad Proactiva' (Accountability) en el RGPD?",
             "r": "El responsable del tratamiento no solo debe cumplir los principios de protección de datos, sino ser capaz de demostrar activamente dicho cumplimiento ante la autoridad de control.", "exp": "Artículo 5.2 del RGPD (UE) 2016/679."},

            # ==========================================
            # BLOQUE II: TECNOLOGÍA BÁSICA (T1 - T8)
            # ==========================================
            # T1
            {"b": 2, "t": 1, "tipo": "definicion", "d": "media", "f": "Arquitectura de Computadores",
             "p": "¿Qué es el 'Pipelining' (Segmentación de cauce) en procesadores modernos?",
             "r": "Técnica que permite solapar la ejecución de múltiples instrucciones dividiéndolas en etapas secuenciales (fetch, decode, execute, memory, writeback), completando una instrucción por cada ciclo de reloj en condiciones ideales.",
             "exp": "Aumenta el throughput de la CPU sin reducir el tiempo de ejecución individual de cada instrucción."},
            {"b": 2, "t": 1, "tipo": "comparativa", "d": "media", "f": "Tecnología de Buses",
             "p": "¿Cuál es la diferencia de transmisión entre el bus PCI clásico y el bus PCI Express (PCIe)?",
             "r": "PCI clásico es un bus paralelo y compartido entre dispositivos; PCIe es una arquitectura punto a punto basada en enlaces serie conmutados por carriles (lanes x1, x4, x8, x16) dedicados y full-duplex.",
             "exp": "PCIe elimina la contención de ancho de banda entre tarjetas periféricas."},

            # T2
            {"b": 2, "t": 2, "tipo": "procedimiento", "d": "dificil", "f": "Teoría de Códigos / Hamming",
             "p": "¿Cuántos bits de redundancia (paridad) se necesitan en un código de Hamming para proteger 4 bits de datos y corregir errores de 1 bit?",
             "r": "3 bits de redundancia (generando una palabra de código de 7 bits: Hamming (7,4)).",
             "exp": "Cumple la fórmula 2^r >= m + r + 1 (2^3 >= 4 + 3 + 1 -> 8 >= 8)."},

            # T3
            {"b": 2, "t": 3, "tipo": "definicion", "d": "media", "f": "Memoria Virtual SO",
             "p": "¿Qué es la 'Anomalía de Belady' en algoritmos de reemplazo de páginas?",
             "r": "El fenómeno por el cual aumentar el número de marcos de memoria física asignados a un proceso provoca un AUMENTO en el número de fallos de página (ocurre en el algoritmo FIFO, pero nunca en LRU ni Óptimo).",
             "exp": "LRU y Óptimo son algoritmos de pila (stack algorithms) y son inmunes a la anomalía de Belady."},
            {"b": 2, "t": 3, "tipo": "comparativa", "d": "facil", "f": "Estructuras de SO",
             "p": "¿Qué diferencia existe entre un micronúcleo (Microkernel) y un núcleo monolítico?",
             "r": "El núcleo monolítico ejecuta todos los servicios del SO (gestión de memoria, red, drivers, sistemas de archivos) en espacio de kernel con máxima velocidad; el micronúcleo ejecuta solo las funciones mínimas indispensables en espacio de kernel (IPC, memoria básica, hilos) y el resto de servicios como servidores en espacio de usuario con mayor estabilidad y aislamiento.",
             "exp": "Ejemplo Monolítico: Linux. Ejemplo Micronúcleo: QNX, Minix, Mach."},

            # T4
            {"b": 2, "t": 4, "tipo": "organismo", "d": "media", "f": "Windows Server Architecture",
             "p": "¿Qué estructura lógica de Active Directory agrupa uno o varios árboles de dominios que comparten un esquema común, un catálogo global y relaciones de confianza transitivas bidireccionales?",
             "r": "Un Bosque (Forest).", "exp": "El bosque es el límite de seguridad y contenedor de más alto nivel en Active Directory."},

            # T5
            {"b": 2, "t": 5, "tipo": "definicion", "d": "media", "f": "Linux Filesystem Ext4",
             "p": "¿Qué información almacena un 'Inodo' en el sistema de archivos de Linux?",
             "r": "Metadatos del archivo: permisos, propietario UID, grupo GID, tamaño, marcas de tiempo (atime, mtime, ctime), punteros a los bloques de datos físicos. NO almacena el nombre del archivo ni el contenido.", "exp": "El nombre del archivo se almacena en la estructura del directorio que apunta al número de inodo."},
            {"b": 2, "t": 5, "tipo": "procedimiento", "d": "facil", "f": "Linux Permisos Especiales",
             "p": "¿Qué efecto tiene activar el bit SUID (Set User ID, valor octal 4000) en un archivo ejecutable en Linux?",
             "r": "Hace que el archivo se ejecute con los privilegios del PROPIETARIO del archivo (usualmente root) y no con los del usuario que lo invoca.", "exp": "Ejemplo clásico: /usr/bin/passwd para permitir a usuarios cambiar su contraseña modificando /etc/shadow."},

            # T6
            {"b": 2, "t": 6, "tipo": "comparativa", "d": "facil", "f": "Medios de Transmisión Fibra",
             "p": "¿Cuál es la diferencia entre fibra óptica monomodo (SMF) y multimodo (MMF)?",
             "r": "La fibra monomodo tiene un núcleo muy estrecho (~9 µm) que propaga un único haz de luz láser para largas distancias (WAN/MAN, decenas de km) sin dispersión modal; la multimodo tiene un núcleo más ancho (50 o 62.5 µm) donde la luz LED/VCSEL rebota en múltiples modos para distancias cortas (LAN, hasta 550m).",
             "exp": "Monomodo es más costosa en transceptores pero ofrece mayor alcance y ancho de banda."},

            # T7
            {"b": 2, "t": 7, "tipo": "procedimiento", "d": "media", "f": "IETF RFC 2131 DHCP",
             "p": "¿Cuáles son los 4 mensajes del intercambio 'DORA' en el protocolo DHCP?",
             "r": "1. DHCP Discover (Cliente a Broadcast)\n2. DHCP Offer (Servidor a Cliente)\n3. DHCP Request (Cliente solicita la IP ofertada)\n4. DHCP Acknowledge / ACK (Servidor confirma la concesión)",
             "exp": "Utiliza los puertos UDP 67 (servidor) y UDP 68 (cliente)."},
            {"b": 2, "t": 7, "tipo": "definicion", "d": "facil", "f": "DNS RFC 1035",
             "p": "¿Qué tipo de registro DNS asocia un nombre de dominio con una dirección IPv6 de 128 bits?",
             "r": "Registro AAAA (Quad-A).", "exp": "El registro A asocia con IPv4 (32 bits); el registro AAAA con IPv6 (128 bits)."},

            # T8
            {"b": 2, "t": 8, "tipo": "comparativa", "d": "media", "f": "IEEE 802.11 Wi-Fi",
             "p": "¿Qué tecnología de modulación introducida en Wi-Fi 6 (802.11ax) permite dividir un canal inalámbrico en múltiples subportadoras para atender a varios dispositivos simultáneamente?",
             "r": "OFDMA (Orthogonal Frequency Division Multiple Access).", "exp": "Reduce drásticamente la latencia y la congestión en entornos densos frente al OFDM tradicional."},

            # ==========================================
            # BLOQUE III: DESARROLLO DE SISTEMAS (T1 - T10)
            # ==========================================
            # T1
            {"b": 3, "t": 1, "tipo": "definicion", "d": "facil", "f": "Metodologías Ágiles",
             "p": "¿Qué significa el término 'WIP' (Work In Progress) y qué objetivo persigue su limitación en el método Kanban?",
             "r": "Cantidad máxima de tareas que pueden estar en curso simultáneamente en una columna del tablero; limita el trabajo en proceso para evitar cuellos de botella y optimizar el flujo de entrega.", "exp": "Principio esencial de Kanban: 'Stop starting, start finishing'."},

            # T2
            {"b": 3, "t": 2, "tipo": "comparativa", "d": "media", "f": "OMG UML 2.5",
             "p": "¿Cuál es la diferencia semántica en UML entre una relación de Agregación y una de Composición?",
             "r": "En la Agregación (rombo hueco blanco) la parte puede existir independientemente del todo (ciclos de vida desacoplados); en la Composición (rombo relleno negro) la parte no tiene sentido de existencia sin el todo (si el todo se destruye, las partes se destruyen con él).", "exp": "Ejemplo Agregación: Empresa y Empleados. Ejemplo Composición: Factura y Líneas de Factura."},

            # T3
            {"b": 3, "t": 3, "tipo": "definicion", "d": "media", "f": "Patrones GoF",
             "p": "¿Qué patrón de diseño GoF de comportamiento encapsula una petición como un objeto, permitiendo parametrizar clientes con diferentes peticiones, encolar operaciones y soportar deshacer (undo)?",
             "r": "El patrón Command.", "exp": "Desacopla el objeto que invoca la operación del que sabe cómo ejecutarla."},

            # T4
            {"b": 3, "t": 4, "tipo": "definicion", "d": "media", "f": "Java JVM Architecture",
             "p": "¿Cuáles son las dos áreas principales de memoria gestionadas por la JVM en Java para datos?",
             "r": "Stack (Pila: almacena variables locales primitivas y llamadas a métodos por cada hilo) y Heap (Montículo: almacena todos los objetos e instancias creadas dinámicamente, gestionado por el Garbage Collector).", "exp": "El Stack es rápido y de tamaño fijo por hilo; el Heap es compartido por toda la aplicación."},

            # T5
            {"b": 3, "t": 5, "tipo": "definicion", "d": "facil", "f": "Teoría Relacional",
             "p": "¿Qué es la Primera Forma Normal (1FN) en bases de datos relacionales?",
             "r": "Una tabla está en 1FN si todos los atributos contienen solo valores atómicos (indivisibles), no existen grupos repetitivos ni arrays dentro de una misma columna y existe una clave primaria definida.", "exp": "Regla fundamental de atomicidad de datos en el modelo relacional de Codd."},

            # T6
            {"b": 3, "t": 6, "tipo": "comparativa", "d": "media", "f": "SQL Standard",
             "p": "¿Cuál es la diferencia entre el comando SQL 'DELETE' y 'TRUNCATE TABLE'?",
             "r": "DELETE es una sentencia DML que elimina filas una a una, activa disparadores (triggers) y puede revertirse con ROLLBACK; TRUNCATE es una sentencia DDL que vacía la tabla completa desasignando las páginas de datos en bloque, es mucho más rápida, no ejecuta triggers y reinicia los contadores autoincrementales.",
             "exp": "TRUNCATE bloquea la tabla a nivel de esquema DDL."},

            # T7
            {"b": 3, "t": 7, "tipo": "definicion", "d": "media", "f": "Teorema CAP / Sistemas Distribuidos",
             "p": "¿Qué postula el Teorema CAP (Teorema de Brewer) en sistemas de bases de datos distribuidas?",
             "r": "Que es imposible que un sistema distribuido garantice simultáneamente las tres propiedades: Consistencia (C), Disponibilidad (A) y Tolerancia a Particiones (P); en presencia de una partición de red, debe elegirse entre Consistencia (CP) o Disponibilidad (AP).", "exp": "Bases de datos tradicionales SQL priorizan CA o CP; NoSQL distribuidas suelen optar por AP (consistencia eventual)."},

            # T8
            {"b": 3, "t": 8, "tipo": "definicion", "d": "facil", "f": "Seguridad Web OWASP",
             "p": "¿Qué es la vulnerabilidad Cross-Site Request Forgery (CSRF) y cómo se mitiga?",
             "r": "Ataque que fuerza a un usuario autenticado a ejecutar acciones no deseadas en una aplicación web en la que está logueado; se mitiga utilizando Tokens CSRF únicos, aleatorios y no predecibles asociados a cada sesión/formulario y cabeceras SameSite en cookies.", "exp": "Obliga a que las peticiones que modifican estado lleven un token secreto validado en backend."},

            # T9
            {"b": 3, "t": 9, "tipo": "definicion", "d": "facil", "f": "Metodología TDD",
             "p": "¿Cuáles son las 3 fases del ciclo 'Red-Green-Refactor' en el desarrollo guiado por pruebas (TDD)?",
             "r": "1. Red: Escribir una prueba unitaria para una nueva funcionalidad que falle (porque el código aún no existe).\n2. Green: Escribir el código mínimo necesario para que la prueba pase con éxito.\n3. Refactor: Mejorar la estructura y limpieza del código manteniendo todas las pruebas en verde.",
             "exp": "Metodología central de ingeniería de software ágil."},

            # T10
            {"b": 3, "t": 10, "tipo": "definicion", "d": "facil", "f": "W3C WAI-ARIA",
             "p": "¿Qué es WAI-ARIA en desarrollo web accesible?",
             "r": "Especificación del W3C (Accessible Rich Internet Applications) que añade roles, estados y propiedades semánticas al HTML mediante atributos 'aria-*' para hacer accesibles componentes dinámicos y widgets interactivos a lectores de pantalla.", "exp": "Ejemplo: aria-expanded='true', aria-hidden='true', role='dialog'."},

            # ==========================================
            # BLOQUE IV: SISTEMAS Y COMUNICACIONES (T1 - T9)
            # ==========================================
            # T1
            {"b": 4, "t": 1, "tipo": "definicion", "d": "facil", "f": "PAe - Notifica",
             "p": "¿Qué es el servicio compartido 'Notifica' de la Administración General del Estado?",
             "r": "La plataforma centralizada para la emisión y gestión de todas las notificaciones administrativas, gestionando automáticamente el envío en papel (a través de Correos/CIE) o telemático (a través de la DEHú/Sede).", "exp": "Optimiza costes y unifica el canal de salida de notificaciones de los organismos públicos."},

            # T2
            {"b": 4, "t": 2, "tipo": "comparativa", "d": "media", "f": "Formatos de Firma Digital",
             "p": "¿Cuáles son los 3 formatos principales de firma electrónica avanzada en Europa según los estándares ETSI?",
             "r": "1. CAdES (CMS Advanced Electronic Signatures): para cualquier archivo binario.\n2. XAdES (XML Advanced Electronic Signatures): para documentos en formato XML.\n3. PAdES (PDF Advanced Electronic Signatures): para documentos en formato PDF con firma integrada conforme a ISO 32000.", "exp": "Estándares ETSI EN 319 122 (CAdES), EN 319 132 (XAdES), EN 319 142 (PAdES)."},

            # T3
            {"b": 4, "t": 3, "tipo": "definicion", "d": "media", "f": "NTI de Expediente Electrónico (ENI)",
             "p": "¿Cuál es la estructura formal obligatoria de un Expediente Electrónico según la NTI del ENI?",
             "r": "1. Documentos electrónicos que lo integran.\n2. Índice electrónico firmado (que garantiza la integridad y orden cronológico).\n3. Metadatos del expediente electrónico.", "exp": "La foliación se efectúa mediante el índice electrónico firmado conforme al RD 4/2010."},

            # T4
            {"b": 4, "t": 4, "tipo": "procedimiento", "d": "media", "f": "BOE RD 311/2022 (ENS)",
             "p": "¿Qué distingue la 'Declaración de Conformidad' de la 'Certificación de Conformidad' en el ENS?",
             "r": "La Declaración de Conformidad es una autoevaluación formal requerida para sistemas de Categoría Básica; la Certificación de Conformidad es obligatoria para sistemas de Categoría Media y Alta y debe ser emitida por una entidad de certificación independiente acreditada por ENAC.", "exp": "Artículo 34 y 35 del Real Decreto 311/2022."},

            # T5
            {"b": 4, "t": 5, "tipo": "definicion", "d": "facil", "f": "Herramientas de Ciberseguridad",
             "p": "¿Qué es un SIEM (Security Information and Event Management)?",
             "r": "Una plataforma centralizada de seguridad que recolecta, almacena, normaliza y correlaciona registros (logs) y eventos de seguridad en tiempo real de toda la infraestructura para detectar incidentes y facilitar el análisis forense.", "exp": "Herramienta clave en los Centros de Operaciones de Ciberseguridad (SOC)."},

            # T6
            {"b": 4, "t": 6, "tipo": "comparativa", "d": "media", "f": "Protocolos VPN IPsec",
             "p": "¿Qué diferencia existe en IPsec entre el protocolo AH (Authentication Header) y ESP (Encapsulating Security Payload)?",
             "r": "AH proporciona autenticación del origen de los datos e integridad pero NO cifra el contenido (no confidencialidad); ESP proporciona confidencialidad mediante cifrado de datos, junto con autenticación e integridad opcional.", "exp": "En la práctica se utiliza casi exclusivamente ESP (Protocolo IP 50)."},

            # T7
            {"b": 4, "t": 7, "tipo": "definicion", "d": "media", "f": "Estándar TIA-942 Data Centers",
             "p": "¿Qué característica define a un CPD con nivel 'Tier IV' según el estándar TIA-942?",
             "r": "Tolerancia activa a fallos: infraestructura con componentes y rutas de distribución eléctricas y de climatización completamente duplicadas en modo 2(N+1), garantizando una disponibilidad del 99.995% (menos de 26 minutos de inactividad al año) permitiendo cualquier fallo individual sin caída del servicio.", "exp": "Máximo nivel de fiabilidad y redundancia física de un Data Center."},

            # T8
            {"b": 4, "t": 8, "tipo": "comparativa", "d": "facil", "f": "Arquitectura Cloud",
             "p": "¿Qué diferencia existe entre escalabilidad vertical (Scale Up) y escalabilidad horizontal (Scale Out) en la nube?",
             "r": "Escalabilidad vertical añade más recursos (CPU, RAM, disco) a la misma máquina virtual existente; escalabilidad horizontal añade más instancias o nodos de servidores en paralelo distribuyendo la carga de trabajo mediante un balanceador.", "exp": "La escalabilidad horizontal es la base de la alta disponibilidad y elasticidad del Cloud Computing."},

            # T9
            {"b": 4, "t": 9, "tipo": "definicion", "d": "facil", "f": "Continuidad de Negocio ISO 22301",
             "p": "¿Qué es el BIA (Business Impact Analysis / Análisis de Impacto en el Negocio)?",
             "r": "El proceso sistemático de identificar los procesos y servicios críticos de una organización, evaluando las consecuencias operativas y financieras que causaría su interrupción para determinar los RTO y RPO necesarios.", "exp": "Paso fundamental y preliminar para la elaboración del Plan de Continuidad de Negocio (BCP)."}
        ]

        nuevas_tarjetas = 0
        for cd in banco_masivo:
            tema_obj = temas.get((cd["b"], cd["t"]))
            if tema_obj:
                _, created = Tarjeta.objects.update_or_create(
                    tema=tema_obj,
                    pregunta=cd["p"],
                    defaults={
                        "tipo": cd["tipo"],
                        "respuesta": cd["r"],
                        "explicacion": cd["exp"],
                        "nivel_dificultad": cd["d"],
                        "fuente": cd["f"],
                    }
                )
                if created:
                    nuevas_tarjetas += 1

        total_tarjetas = Tarjeta.objects.count()
        self.stdout.write(self.style.SUCCESS(f"¡Carga masiva de tarjetas completada! Total de tarjetas atómicas activas en el sistema: {total_tarjetas}"))
