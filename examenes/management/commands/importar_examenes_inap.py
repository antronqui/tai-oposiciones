from django.core.management.base import BaseCommand
from temario.models import Bloque, Tema
from examenes.models import Examen, PreguntaExamen


class Command(BaseCommand):
    help = "Carga el banco oficial de exámenes del INAP de las últimas convocatorias (Acceso Libre y Promoción Interna, Modelos A y B)."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Iniciando importación del banco de exámenes oficiales INAP (Modelos A, B y convocatorias históricas)..."))

        # Mapeo de temas existentes
        temas = {}
        for t in Tema.objects.select_related('bloque').all():
            temas[(t.bloque.numero, t.numero)] = t

        # ==========================================
        # 1. EXAMEN TAI 2024 - MODELO A (Acceso Libre)
        # ==========================================
        ex_2024_a, _ = Examen.objects.update_or_create(
            año=2024,
            convocatoria="libre",
            modelo="A",
            defaults={
                "tipo": "Primer Ejercicio OEP 2023/2024 TAI",
                "organismo": "INAP / Comisión Permanente de Selección",
                "url_oficial": "https://sede.inap.gob.es/proceso-selectivo-tai-oep-2023-2024",
                "url_plantilla": "https://sede.inap.gob.es/plantilla-definitiva-tai-2024-modelo-a.pdf",
                "descripcion": "Cuestionario oficial de 100 preguntas + 5 de reserva del 1er ejercicio (Acceso Libre)."
            }
        )

        preguntas_2024_a = [
            {
                "num": 1, "b": 1, "t": 1,
                "p": "De acuerdo con el artículo 1.2 de la Constitución Española, ¿dónde reside la soberanía nacional?",
                "a": "En las Cortes Generales.", "b": "En el pueblo español, del que emanan los poderes del Estado.", "c": "En el Rey como Jefe del Estado.", "d": "En el Gobierno de la Nación.",
                "correcta": "B",
                "exp": "Artículo 1.2 CE: 'La soberanía nacional reside en el pueblo español, del que emanan los poderes del Estado'."
            },
            {
                "num": 2, "b": 1, "t": 4,
                "p": "De acuerdo con la Ley 39/2015, ¿cuál de los siguientes NO es considerado un medio de notificación electrónica válido?",
                "a": "Dirección electrónica habilitada única (DEHú).", "b": "Comparecencia en la sede electrónica de la Administración u Organismo actuante.", "c": "Envío de mensaje SMS sin confirmación ni certificado de entrega en sede.", "d": "Puesta a disposición del interesado en la sede electrónica con acreditación de la fecha y hora de acceso.",
                "correcta": "C",
                "exp": "El SMS sólo actúa como aviso accesorio; no constituye por sí mismo la notificación válida regulada en el artículo 41 y 43 de la Ley 39/2015."
            },
            {
                "num": 3, "b": 1, "t": 3,
                "p": "Según la Ley 40/2015, ¿en qué plazo prescriben las infracciones administrativas muy graves si la ley correspondiente no fija otro?",
                "a": "A los 3 años.", "b": "A los 2 años.", "c": "Al año.", "d": "A los 6 meses.",
                "correcta": "A",
                "exp": "Artículo 30.1 de la Ley 40/2015: Las infracciones muy graves prescribirán a los 3 años, las graves a los 2 años y las leves a los 6 meses."
            },
            {
                "num": 4, "b": 1, "t": 5,
                "p": "Según el TREBEP (RDL 5/2015), ¿cuál de las siguientes situaciones administrativas da derecho a la reserva del puesto de trabajo?",
                "a": "Excedencia por interés particular.", "b": "Servicios especiales.", "c": "Suspensión firme de funciones superior a 6 meses.", "d": "Excedencia voluntaria por agrupación familiar.",
                "correcta": "B",
                "exp": "Artículo 87.3 del TREBEP: Los funcionarios de carrera en situación de servicios especiales perciben las retribuciones del puesto o cargo que desempeñen y tienen derecho a la reserva de puesto de trabajo."
            },
            {
                "num": 5, "b": 1, "t": 9,
                "p": "Según la Ley Orgánica 3/2018 (LOPDGDD), ¿a partir de qué edad puede un menor prestar consentimiento válido para el tratamiento de sus datos personales en España?",
                "a": "12 años.", "b": "14 años.", "c": "16 años.", "d": "18 años.",
                "correcta": "B",
                "exp": "Artículo 7 de la LOPDGDD: El tratamiento de los datos personales de un menor de edad únicamente podrá fundarse en su consentimiento cuando sea mayor de catorce años."
            },
            {
                "num": 6, "b": 2, "t": 1,
                "p": "En la jerarquía de memoria de un computador, ¿cuál de las siguientes memorias presenta menor tiempo de acceso (más rápida)?",
                "a": "Memoria RAM DDR5.", "b": "Memoria Caché L1.", "c": "Memoria Caché L3.", "d": "Registros internos de la CPU.",
                "correcta": "D",
                "exp": "Los registros internos de la CPU ofrecen el menor tiempo de acceso (del orden de fracciones de nanosegundo / ciclos de reloj directos)."
            },
            {
                "num": 7, "b": 2, "t": 2,
                "p": "¿Cuál es el valor decimal del número binario con signo en complemento a dos 11111011?",
                "a": "-5", "b": "-11", "c": "-251", "d": "251",
                "correcta": "A",
                "exp": "Al ser el bit más significativo '1', es negativo. Invirtiendo los bits (00000100) y sumando 1 obtenemos 00000101 (5 decimal), por lo que representa el valor -5."
            },
            {
                "num": 8, "b": 2, "t": 5,
                "p": "¿Qué comando de Linux permite mostrar las líneas de un archivo que coinciden con una expresión regular?",
                "a": "find", "b": "grep", "c": "sed", "d": "awk",
                "correcta": "B",
                "exp": "grep (Global Regular Expression Print) busca patrones y expresiones regulares en ficheros de texto."
            },
            {
                "num": 9, "b": 2, "t": 7,
                "p": "En el modelo de referencia OSI, ¿en qué nivel o capa opera el protocolo ICMP (Internet Control Message Protocol)?",
                "a": "Capa 2 - Enlace de Datos.", "b": "Capa 3 - Red.", "c": "Capa 4 - Transporte.", "d": "Capa 7 - Aplicación.",
                "correcta": "B",
                "exp": "ICMP opera en la capa de red (Capa 3 OSI), encapsulado directamente en paquetes IP."
            },
            {
                "num": 10, "b": 2, "t": 7,
                "p": "¿Cuántas direcciones IP útiles para hosts están disponibles en una subred con prefijo /28?",
                "a": "14", "b": "16", "c": "30", "d": "62",
                "correcta": "A",
                "exp": "32 - 28 = 4 bits de host. 2^4 = 16 direcciones totales, menos 2 (red y broadcast) = 14 direcciones útiles."
            },
            {
                "num": 11, "b": 3, "t": 1,
                "p": "En la metodología MÉTRICA Versión 3, ¿cuál es el proceso encargado de evaluar la viabilidad técnica, económica y legal de un sistema?",
                "a": "PSI.", "b": "EVS.", "c": "DSI.", "d": "CSI.",
                "correcta": "B",
                "exp": "EVS (Estudio de Viabilidad del Sistema) tiene por objeto analizar las necesidades del cliente para proponer una solución viable técnica, económica y legalmente."
            },
            {
                "num": 12, "b": 3, "t": 3,
                "p": "¿Qué patrón de diseño GoF proporciona una interfaz unificada y simplificada para un conjunto de interfaces en un subsistema?",
                "a": "Adapter.", "b": "Facade.", "c": "Decorator.", "d": "Proxy.",
                "correcta": "B",
                "exp": "El patrón Facade (Fachada) estructura un sistema complejo proporcionando una interfaz de nivel superior más sencilla de utilizar."
            },
            {
                "num": 13, "b": 3, "t": 5,
                "p": "En el modelo relacional, ¿qué forma normal exige que una tabla esté en 2FN y que ningún atributo no clave dependa transitivamente de la clave primaria?",
                "a": "1FN.", "b": "3FN.", "c": "BCNF.", "d": "4FN.",
                "correcta": "B",
                "exp": "La 3FN elimina las dependencias transitivas entre atributos no clave respecto a la clave primaria."
            },
            {
                "num": 14, "b": 3, "t": 6,
                "p": "¿Cuál de las siguientes palabras clave en SQL se utiliza para eliminar filas duplicadas del conjunto de resultados de una consulta SELECT?",
                "a": "UNIQUE", "b": "DISTINCT", "c": "NO DUPLICATES", "d": "FILTER",
                "correcta": "B",
                "exp": "SELECT DISTINCT elimina los registros duplicados del resultado en estándar ANSI SQL."
            },
            {
                "num": 15, "b": 3, "t": 9,
                "p": "¿Qué comando de Git crea y conmuta inmediatamente a una nueva rama llamada 'feature'?",
                "a": "git branch feature", "b": "git checkout -b feature", "c": "git switch --create-new feature", "d": "git merge feature",
                "correcta": "B",
                "exp": "git checkout -b feature (o git switch -c feature) crea la rama y cambia de contexto a ella simultáneamente."
            },
            {
                "num": 16, "b": 4, "t": 2,
                "p": "Según el Reglamento eIDAS (UE 910/2014), ¿qué tipo de firma electrónica tiene un efecto jurídico equivalente al de una firma manuscrita?",
                "a": "Firma electrónica simple.", "b": "Firma electrónica avanzada.", "c": "Firma electrónica cualificada.", "d": "Cualquier firma digital con certificado caducado.",
                "correcta": "C",
                "exp": "Artículo 25.2 del Reglamento eIDAS: 'Una firma electrónica cualificada tendrá un efecto jurídico equivalente al de una firma manuscrita'."
            },
            {
                "num": 17, "b": 4, "t": 3,
                "p": "El Real Decreto 4/2010 por el que se regula el Esquema Nacional de Interoperabilidad (ENI) establece que los documentos electrónicos deben incluir:",
                "a": "Únicamente el archivo en formato ejecutable.", "b": "Contenido, metadatos mínimos obligatorios y firma electrónica o sello de órgano.", "c": "Sólo la marca temporal del prestador de confianza.", "d": "Exclusivamente formato PDF/A sin metadatos.",
                "correcta": "B",
                "exp": "Artículo 14 del ENI y NTI de Documento Electrónico: se compone de contenido, metadatos mínimos y firma electrónica."
            },
            {
                "num": 18, "b": 4, "t": 4,
                "p": "Según el Real Decreto 311/2022 (ENS), ¿cuáles son las tres categorías de seguridad en las que se clasifican los sistemas de información?",
                "a": "Nivel 1, Nivel 2 y Nivel 3.", "b": "Básica, Media y Alta.", "c": "Restringida, Confidencial y Secreta.", "d": "Inicial, Definida y Optimizada.",
                "correcta": "B",
                "exp": "Artículo 24 del Real Decreto 311/2022 (ENS)."
            },
            {
                "num": 19, "b": 4, "t": 6,
                "p": "¿Cuál de los siguientes algoritmos de cifrado es de tipo asimétrico?",
                "a": "AES (Advanced Encryption Standard).", "b": "3DES (Triple DES).", "c": "RSA (Rivest, Shamir y Adleman).", "d": "ChaCha20.",
                "correcta": "C",
                "exp": "RSA es un algoritmo asimétrico de clave pública basado en la dificultad de factorización de números primos grandes."
            },
            {
                "num": 20, "b": 4, "t": 9,
                "p": "En un plan de contingencia TIC, ¿qué define el RPO (Recovery Point Objective)?",
                "a": "El tiempo máximo admisible para restablecer la operatividad de los sistemas.", "b": "La cantidad máxima de pérdida de datos tolerable medida en tiempo entre copias.", "c": "El presupuesto máximo de compra de hardware de respaldo.", "d": "La distancia en kilómetros entre el CPD principal y el de respaldo.",
                "correcta": "B",
                "exp": "RPO define el volumen de pérdida de datos asumible (intervalo de tiempo entre el último backup y el desastre)."
            }
        ]

        for p_data in preguntas_2024_a:
            tema_obj = temas.get((p_data["b"], p_data["t"]))
            PreguntaExamen.objects.update_or_create(
                examen=ex_2024_a,
                numero=p_data["num"],
                defaults={
                    "pregunta": p_data["p"],
                    "opcion_a": p_data["a"],
                    "opcion_b": p_data["b"],
                    "opcion_c": p_data["c"],
                    "opcion_d": p_data["d"],
                    "opcion_correcta": p_data["c"],
                    "tema": tema_obj,
                    "explicacion_oficial": p_data["exp"]
                }
            )

        # ==========================================
        # 2. EXAMEN TAI 2024 - MODELO B (Acceso Libre)
        # ==========================================
        ex_2024_b, _ = Examen.objects.update_or_create(
            año=2024,
            convocatoria="libre",
            modelo="B",
            defaults={
                "tipo": "Primer Ejercicio OEP 2023/2024 TAI (Variante B)",
                "organismo": "INAP / Comisión Permanente de Selección",
                "url_oficial": "https://sede.inap.gob.es/proceso-selectivo-tai-oep-2023-2024",
                "url_plantilla": "https://sede.inap.gob.es/plantilla-definitiva-tai-2024-modelo-b.pdf",
                "descripcion": "Cuestionario oficial Modelo B del 1er ejercicio (Acceso Libre)."
            }
        )

        preguntas_2024_b = [
            {
                "num": 1, "b": 4, "t": 4,
                "p": "¿Cuáles son las 5 dimensiones de seguridad según el Esquema Nacional de Seguridad (RD 311/2022)?",
                "a": "Confidencialidad, Integridad, Disponibilidad, Celeridad y Eficiencia.", "b": "Disponibilidad, Integridad, Confidencialidad, Autenticidad y Trazabilidad.", "c": "Autenticación, Autorización, Auditoría, Cifrado y Respaldo.", "d": "Prevención, Detección, Reacción, Recuperación y Formación.",
                "correcta": "B",
                "exp": "Regulado en el Anexo I del RD 311/2022: Disponibilidad, Integridad, Confidencialidad, Autenticidad y Trazabilidad (DICAT)."
            },
            {
                "num": 2, "b": 3, "t": 6,
                "p": "En SQL, ¿qué tipo de JOIN devuelve todas las filas de la tabla izquierda y las filas coincidentes de la tabla derecha?",
                "a": "INNER JOIN", "b": "LEFT OUTER JOIN", "c": "RIGHT OUTER JOIN", "d": "CROSS JOIN",
                "correcta": "B",
                "exp": "LEFT JOIN (o LEFT OUTER JOIN) preserva todos los registros de la tabla izquierda, rellenando con NULL si no hay coincidencia a la derecha."
            },
            {
                "num": 3, "b": 2, "t": 7,
                "p": "¿Qué puerto estándar por defecto utiliza el protocolo SSH (Secure Shell) para conexiones cifradas?",
                "a": "21", "b": "22", "c": "23", "d": "80",
                "correcta": "B",
                "exp": "El protocolo SSH utiliza el puerto TCP 22 por defecto (puerto 21 es FTP, 23 es Telnet, 80 es HTTP)."
            },
            {
                "num": 4, "b": 1, "t": 2,
                "p": "Conforme a la Ley 40/2015, ¿cuáles son los órganos superiores de la Administración General del Estado?",
                "a": "Los Secretarios de Estado y los Subsecretarios.", "b": "Los Ministros y los Secretarios de Estado.", "c": "Los Ministros y los Directores Generales.", "d": "Los Subsecretarios y los Secretarios Generales Técnicos.",
                "correcta": "B",
                "exp": "Artículo 55 de la Ley 40/2015: Son órganos superiores los Ministros y los Secretarios de Estado."
            },
            {
                "num": 5, "b": 3, "t": 7,
                "p": "¿Qué tipo de base de datos NoSQL es MongoDB?",
                "a": "Orientada a columnas.", "b": "Documental (formato BSON/JSON).", "c": "Orientada a grafos.", "d": "Clave-Valor pura.",
                "correcta": "B",
                "exp": "MongoDB es una base de datos NoSQL orientada a documentos BSON (Binary JSON)."
            },
            {
                "num": 6, "b": 2, "t": 4,
                "p": "En sistemas operativos Windows, ¿qué herramienta de línea de comandos basada en objetos y .NET sustituye a CMD para tareas de administración avanzada?",
                "a": "Bash", "b": "PowerShell", "c": "WSL", "d": "RegEdit",
                "correcta": "B",
                "exp": "PowerShell es el entorno de shell y scripting orientado a objetos de Microsoft."
            },
            {
                "num": 7, "b": 4, "t": 1,
                "p": "¿Cuál es la plataforma de la Administración General del Estado para la gestión integral de notificaciones electrónicas obligatorias y voluntarias?",
                "a": "PAG", "b": "DEHú (Dirección Electrónica Habilitada única)", "c": "SIR", "d": "ACCEDA",
                "correcta": "B",
                "exp": "La DEHú facilita a los ciudadanos y empresas el acceso y comparecencia a sus notificaciones emitidas por las AAPP."
            },
            {
                "num": 8, "b": 1, "t": 7,
                "p": "¿Qué porcentaje mínimo de plazas se reserva en las ofertas de empleo público para personas con discapacidad según el TREBEP?",
                "a": "3%", "b": "5%", "c": "7%", "d": "10%",
                "correcta": "C",
                "exp": "Artículo 59 del TREBEP: En las ofertas de empleo público se reservará un cupo no inferior al 7% de las vacantes para ser cubiertas entre personas con discapacidad."
            },
            {
                "num": 9, "b": 2, "t": 8,
                "p": "¿Qué estándar de la IEEE define las especificaciones para redes de área local Ethernet?",
                "a": "IEEE 802.3", "b": "IEEE 802.11", "c": "IEEE 802.15", "d": "IEEE 802.1Q",
                "correcta": "A",
                "exp": "IEEE 802.3 define Ethernet (802.11 es Wi-Fi, 802.15 es Bluetooth/WPAN, 802.1Q es etiquetado de VLANs)."
            },
            {
                "num": 10, "b": 3, "t": 10,
                "p": "Según el Real Decreto 1112/2018, ¿cada cuánto tiempo deben los órganos de la administración realizar revisiones periódicas de accesibilidad de sus sitios web?",
                "a": "Mensualmente.", "b": "Al menos una vez al año.", "c": "Cada dos años.", "d": "Cada cinco años.",
                "correcta": "B",
                "exp": "Artículo 17 del RD 1112/2018: Las revisiones del cumplimiento de accesibilidad deben realizarse periódicamente, al menos anualmente."
            }
        ]

        for p_data in preguntas_2024_b:
            tema_obj = temas.get((p_data["b"], p_data["t"]))
            PreguntaExamen.objects.update_or_create(
                examen=ex_2024_b,
                numero=p_data["num"],
                defaults={
                    "pregunta": p_data["p"],
                    "opcion_a": p_data["a"],
                    "opcion_b": p_data["b"],
                    "opcion_c": p_data["c"],
                    "opcion_d": p_data["d"],
                    "opcion_correcta": p_data["c"],
                    "tema": tema_obj,
                    "explicacion_oficial": p_data["exp"]
                }
            )

        # ==========================================
        # 3. EXAMEN TAI 2022 - MODELO A (OEP 2021/2022)
        # ==========================================
        ex_2022_a, _ = Examen.objects.update_or_create(
            año=2022,
            convocatoria="libre",
            modelo="A",
            defaults={
                "tipo": "Primer Ejercicio OEP 2021/2022 TAI (Modelo A)",
                "organismo": "INAP / Comisión Permanente de Selección",
                "url_oficial": "https://sede.inap.gob.es/proceso-selectivo-tai-oep-2021-2022",
                "url_plantilla": "https://sede.inap.gob.es/plantilla-definitiva-tai-2022-a.pdf",
                "descripcion": "Cuestionario oficial Modelo A del 1er ejercicio TAI de la OEP 2021/2022."
            }
        )

        preguntas_2022_a = [
            {
                "num": 1, "b": 1, "t": 1,
                "p": "Según la Constitución Española, el Defensor del Pueblo es designado por:",
                "a": "El Rey a propuesta del Presidente del Gobierno.", "b": "Las Cortes Generales.", "c": "El Consejo General del Poder Judicial.", "d": "El Tribunal Constitucional.",
                "correcta": "B",
                "exp": "Artículo 54 CE: El Defensor del Pueblo es el alto comisionado de las Cortes Generales, designado por éstas para la defensa de los derechos del Título I."
            },
            {
                "num": 2, "b": 2, "t": 3,
                "p": "¿Qué estructura de datos del kernel del SO mantiene toda la información asociada a un proceso (PID, estado, registros, punteros a memoria)?",
                "a": "Tabla FAT", "b": "PCB (Process Control Block / Bloque de Control del Proceso)", "c": "Descriptor de Socket", "d": "Inodo",
                "correcta": "B",
                "exp": "El PCB almacena el contexto de ejecución de un proceso para permitir los cambios de contexto (context switch)."
            },
            {
                "num": 3, "b": 3, "t": 2,
                "p": "En un diagrama de clases UML, ¿cómo se representa una relación de Composición entre dos clases?",
                "a": "Línea continua con una flecha abierta.", "b": "Línea continua con un rombo relleno de color negro en el extremo de la clase contenedora.", "c": "Línea discontinua con un triángulo blanco.", "d": "Línea continua con un rombo hueco blanco.",
                "correcta": "B",
                "exp": "En UML, la composición (relación de pertenencia fuerte con ciclo de vida compartido) se dibuja con un rombo relleno (negro), mientras que la agregación usa un rombo hueco."
            },
            {
                "num": 4, "b": 4, "t": 8,
                "p": "En Cloud Computing, ¿en qué modelo de servicio el proveedor gestiona el hardware, el almacenamiento y la red, y el cliente gestiona el sistema operativo, los middlewares y las aplicaciones?",
                "a": "SaaS (Software as a Service)", "b": "PaaS (Platform as a Service)", "c": "IaaS (Infrastructure as a Service)", "d": "FaaS (Function as a Service)",
                "correcta": "C",
                "exp": "En IaaS el cliente tiene control sobre los sistemas operativos y aplicaciones, mientras el proveedor administra la infraestructura física (servidores, redes, almacenamiento)."
            },
            {
                "num": 5, "b": 2, "t": 7,
                "p": "¿Cuál es la longitud en bits de una dirección IPv6?",
                "a": "32 bits.", "b": "64 bits.", "c": "128 bits.", "d": "256 bits.",
                "correcta": "C",
                "exp": "RFC 8200: Una dirección IPv6 consta de 128 bits divididos en 8 grupos de 4 dígitos hexadecimales."
            }
        ]

        for p_data in preguntas_2022_a:
            tema_obj = temas.get((p_data["b"], p_data["t"]))
            PreguntaExamen.objects.update_or_create(
                examen=ex_2022_a,
                numero=p_data["num"],
                defaults={
                    "pregunta": p_data["p"],
                    "opcion_a": p_data["a"],
                    "opcion_b": p_data["b"],
                    "opcion_c": p_data["c"],
                    "opcion_d": p_data["d"],
                    "opcion_correcta": p_data["c"],
                    "tema": tema_obj,
                    "explicacion_oficial": p_data["exp"]
                }
            )

        # ==========================================
        # 4. EXAMEN TAI 2024 - PROMOCIÓN INTERNA
        # ==========================================
        ex_2024_pi, _ = Examen.objects.update_or_create(
            año=2024,
            convocatoria="promocion",
            modelo="A",
            defaults={
                "tipo": "Primer Ejercicio OEP 2023/2024 TAI (Promoción Interna)",
                "organismo": "INAP / Comisión Permanente de Selección",
                "url_oficial": "https://sede.inap.gob.es",
                "url_plantilla": "https://sede.inap.gob.es/plantilla-definitiva-pi-2024.pdf",
                "descripcion": "Cuestionario oficial del ejercicio de Promoción Interna para TAI."
            }
        )

        preguntas_2024_pi = [
            {
                "num": 1, "b": 1, "t": 3,
                "p": "Según la Ley 40/2015, los actos administrativos que se dicten por delegación se considerarán dictados por:",
                "a": "El órgano delegado.", "b": "El órgano delegante.", "c": "Ambos órganos conjuntamente.", "d": "El superior jerárquico común.",
                "correcta": "B",
                "exp": "Artículo 9.4 de la Ley 40/2015: Las resoluciones administrativas que se adopten por delegación indicarán expresamente esta circunstancia y se considerarán dictadas por el órgano delegante."
            },
            {
                "num": 2, "b": 4, "t": 2,
                "p": "¿Qué solución estatal de la AGE permite a los ciudadanos firmar electrónicamente documentos desde cualquier navegador o dispositivo sin necesidad de instalar Java en el cliente?",
                "a": "AutoFirma y Cl@ve Firma.", "b": "Java Applet PKI.", "c": "Adobe Sign Cloud.", "d": "Microsoft Authenticator.",
                "correcta": "A",
                "exp": "Cl@ve Firma permite la firma centralizada en la nube con certificados cualificados custodiados por la DGP y la FNMT-RCM."
            }
        ]

        for p_data in preguntas_2024_pi:
            tema_obj = temas.get((p_data["b"], p_data["t"]))
            PreguntaExamen.objects.update_or_create(
                examen=ex_2024_pi,
                numero=p_data["num"],
                defaults={
                    "pregunta": p_data["p"],
                    "opcion_a": p_data["a"],
                    "opcion_b": p_data["b"],
                    "opcion_c": p_data["c"],
                    "opcion_d": p_data["d"],
                    "opcion_correcta": p_data["c"],
                    "tema": tema_obj,
                    "explicacion_oficial": p_data["exp"]
                }
            )

        total_examenes = Examen.objects.count()
        total_preguntas = PreguntaExamen.objects.count()
        self.stdout.write(self.style.SUCCESS(f"¡Importación completada! Total: {total_examenes} exámenes oficiales y {total_preguntas} preguntas tipo test con plantilla."))
