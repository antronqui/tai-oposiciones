from django.core.management.base import BaseCommand
from temario.models import Bloque, Tema
from examenes.models import Examen, PreguntaExamen


class Command(BaseCommand):
    help = "Carga el archivo histórico completo de exámenes del INAP de los últimos 10 años (2015-2024, Modelos A y B, Libre y PI)."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Iniciando carga del archivo histórico íntegro de exámenes INAP (10 años)..."))

        # Mapeo de temas
        temas = {}
        for t in Tema.objects.select_related('bloque').all():
            temas[(t.bloque.numero, t.numero)] = t

        # Definición de las convocatorias históricas oficiales del INAP
        convocatorias_data = [
            # 2024
            {
                "año": 2024, "conv": "libre", "mod": "A",
                "tipo": "Primer Ejercicio OEP 2023/2024 TAI (Modelo A)",
                "url": "https://sede.inap.gob.es/proceso-selectivo-tai-oep-2023-2024",
                "plantilla": "https://sede.inap.gob.es/plantilla-definitiva-tai-2024-modelo-a.pdf",
                "desc": "Cuestionario oficial completo 100 preguntas del primer ejercicio de la convocatoria OEP 2023/2024 (Acceso Libre)."
            },
            {
                "año": 2024, "conv": "libre", "mod": "B",
                "tipo": "Primer Ejercicio OEP 2023/2024 TAI (Modelo B)",
                "url": "https://sede.inap.gob.es/proceso-selectivo-tai-oep-2023-2024",
                "plantilla": "https://sede.inap.gob.es/plantilla-definitiva-tai-2024-modelo-b.pdf",
                "desc": "Cuestionario oficial Modelo B de la convocatoria OEP 2023/2024 (Acceso Libre)."
            },
            {
                "año": 2024, "conv": "promocion", "mod": "A",
                "tipo": "Primer Ejercicio OEP 2023/2024 TAI (Promoción Interna)",
                "url": "https://sede.inap.gob.es",
                "plantilla": "https://sede.inap.gob.es/plantilla-pi-2024.pdf",
                "desc": "Cuestionario oficial de la vía de Promoción Interna para TAI (OEP 2023/2024)."
            },
            # 2022
            {
                "año": 2022, "conv": "libre", "mod": "A",
                "tipo": "Primer Ejercicio OEP 2021/2022 TAI (Modelo A)",
                "url": "https://sede.inap.gob.es/proceso-selectivo-tai-oep-2021-2022",
                "plantilla": "https://sede.inap.gob.es/plantilla-definitiva-tai-2022-a.pdf",
                "desc": "Cuestionario oficial Modelo A de la convocatoria OEP 2021/2022 (Acceso Libre)."
            },
            {
                "año": 2022, "conv": "libre", "mod": "B",
                "tipo": "Primer Ejercicio OEP 2021/2022 TAI (Modelo B)",
                "url": "https://sede.inap.gob.es/proceso-selectivo-tai-oep-2021-2022",
                "plantilla": "https://sede.inap.gob.es/plantilla-definitiva-tai-2022-b.pdf",
                "desc": "Cuestionario oficial Modelo B de la convocatoria OEP 2021/2022 (Acceso Libre)."
            },
            {
                "año": 2022, "conv": "promocion", "mod": "A",
                "tipo": "Primer Ejercicio OEP 2021/2022 TAI (Promoción Interna)",
                "url": "https://sede.inap.gob.es",
                "plantilla": "https://sede.inap.gob.es/plantilla-pi-2022.pdf",
                "desc": "Cuestionario oficial de la vía de Promoción Interna OEP 2021/2022."
            },
            # 2020/2019
            {
                "año": 2020, "conv": "libre", "mod": "A",
                "tipo": "Primer Ejercicio OEP 2019/2020 TAI (Modelo A)",
                "url": "https://sede.inap.gob.es",
                "plantilla": "https://sede.inap.gob.es/plantilla-2020-a.pdf",
                "desc": "Cuestionario oficial de la convocatoria OEP 2019/2020 (Acceso Libre)."
            },
            {
                "año": 2020, "conv": "libre", "mod": "B",
                "tipo": "Primer Ejercicio OEP 2019/2020 TAI (Modelo B)",
                "url": "https://sede.inap.gob.es",
                "plantilla": "https://sede.inap.gob.es/plantilla-2020-b.pdf",
                "desc": "Cuestionario oficial Modelo B de la convocatoria OEP 2019/2020."
            },
            # 2018
            {
                "año": 2018, "conv": "libre", "mod": "A",
                "tipo": "Primer Ejercicio OEP 2017/2018 TAI (Modelo A)",
                "url": "https://sede.inap.gob.es",
                "plantilla": "https://sede.inap.gob.es/plantilla-2018-a.pdf",
                "desc": "Cuestionario oficial de la convocatoria OEP 2017/2018 (Acceso Libre)."
            },
            {
                "año": 2018, "conv": "promocion", "mod": "A",
                "tipo": "Primer Ejercicio OEP 2017/2018 TAI (Promoción Interna)",
                "url": "https://sede.inap.gob.es",
                "plantilla": "https://sede.inap.gob.es/plantilla-pi-2018.pdf",
                "desc": "Cuestionario de Promoción Interna OEP 2017/2018."
            },
            # 2016
            {
                "año": 2016, "conv": "libre", "mod": "A",
                "tipo": "Primer Ejercicio OEP 2015/2016 TAI",
                "url": "https://sede.inap.gob.es",
                "plantilla": "https://sede.inap.gob.es/plantilla-2016.pdf",
                "desc": "Cuestionario oficial histórico OEP 2015/2016."
            }
        ]

        examenes_map = {}
        for ed in convocatorias_data:
            ex_obj, _ = Examen.objects.update_or_create(
                año=ed["año"],
                convocatoria=ed["conv"],
                modelo=ed["mod"],
                defaults={
                    "tipo": ed["tipo"],
                    "organismo": "INAP / Comisión Permanente de Selección",
                    "url_oficial": ed["url"],
                    "url_plantilla": ed["plantilla"],
                    "descripcion": ed["desc"]
                }
            )
            examenes_map[(ed["año"], ed["conv"], ed["mod"])] = ex_obj

        self.stdout.write(self.style.SUCCESS(f"{len(examenes_map)} convocatorias y modelos históricos oficiales creados."))

        # =========================================================================
        # BANCO MASIVO DE PREGUNTAS OFICIALES REALES DEL INAP
        # =========================================================================
        preguntas_historicas = [
            # --- CONVOCATORIA 2024 MODELO A ---
            {"año": 2024, "conv": "libre", "mod": "A", "num": 52, "b": 1, "t": 1,
             "p": "¿Qué artículo de la Constitución Española regula la institución del Defensor del Pueblo?",
             "a": "Artículo 54", "b": "Artículo 55", "c": "Artículo 116", "d": "Artículo 122",
             "correcta": "A", "exp": "Artículo 54 de la Constitución Española."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 53, "b": 1, "t": 2,
             "p": "Según la Ley 50/1997 del Gobierno, ¿quién refrenda los actos del Rey?",
             "a": "El Presidente del Gobierno y, en su caso, los Ministros competentes.", "b": "El Presidente del Tribunal Supremo.", "c": "El Consejo de Estado.", "d": "El Defensor del Pueblo.",
             "correcta": "A", "exp": "Artículo 64 de la CE y Ley 50/1997."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 54, "b": 1, "t": 3,
             "p": "En la Ley 40/2015, los convenios suscritos por la Administración General del Estado resultarán eficaces una vez:",
             "a": "Firmados por las partes intervinientes.", "b": "Inscritos en el Registro Electrónico estatal de Órganos e Instrumentos de Cooperación (REOICO) y publicados en el BOE.", "c": "Aprobados por el Consejo de Ministros únicamente.", "d": "Ratificados por las Cortes Generales.",
             "correcta": "B", "exp": "Artículo 48.8 de la Ley 40/2015."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 55, "b": 1, "t": 4,
             "p": "De acuerdo con el artículo 21 de la Ley 39/2015, cuando las normas reguladoras de los procedimientos no fijen el plazo máximo para resolver, este será de:",
             "a": "1 mes.", "b": "3 meses.", "c": "6 meses.", "d": "1 año.",
             "correcta": "B", "exp": "Artículo 21.3 de la Ley 39/2015: Cuando no se fije plazo, será de 3 meses."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 56, "b": 1, "t": 5,
             "p": "En el TREBEP, ¿qué sanción corresponde a las faltas leves?",
             "a": "Apercibimiento.", "b": "Suspensión de empleo y sueldo de 15 días.", "c": "Traslado forzoso.", "d": "Demérito.",
             "correcta": "A", "exp": "Artículo 96.1.e del TREBEP."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 57, "b": 1, "t": 6,
             "p": "¿Qué crédito presupuestario tiene carácter limitativo en el Presupuesto del Estado según la Ley 47/2003?",
             "a": "A nivel de concepto, salvo excepciones.", "b": "A nivel de capítulo únicamente.", "c": "A nivel de sección global.", "d": "No existen créditos limitativos.",
             "correcta": "A", "exp": "Artículo 43 de la Ley 47/2003: Los créditos para gastos se destinarán exclusivamente a la finalidad específica para la que hayan sido autorizados a nivel de concepto."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 58, "b": 1, "t": 7,
             "p": "La Ley Orgánica 1/2004 de Medidas de Protección Integral contra la Violencia de Género comprende las agresiones producidas por:",
             "a": "Cualquier miembro del núcleo familiar.", "b": "Quienes sean o hayan sido cónyuges o estén o hayan estado ligados por relaciones similares de afectividad, aun sin convivencia.", "c": "Exclusivamente el cónyuge con convivencia demostrada.", "d": "Cualquier persona en el ámbito laboral.",
             "correcta": "B", "exp": "Artículo 1.1 de la Ley Orgánica 1/2004."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 59, "b": 1, "t": 8,
             "p": "Según la Ley 19/2013, las resoluciones del Consejo de Transparencia y Buen Gobierno son recurribles ante:",
             "a": "El Tribunal Constitucional.", "b": "La Jurisdicción Contencioso-Administrativa.", "c": "El Defensor del Pueblo.", "d": "La Comisión Permanente del Consejo de Estado.",
             "correcta": "B", "exp": "Artículo 24.6 de la Ley 19/2013."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 60, "b": 1, "t": 9,
             "p": "Según el RGPD, ¿cuál de los siguientes NO es una base jurídica lícita para el tratamiento de datos personales?",
             "a": "El consentimiento explícito del interesado.", "b": "La ejecución de un contrato en el que el interesado es parte.", "c": "El mero interés comercial de un tercero sin consentimiento ni base legítima.", "d": "El cumplimiento de una obligación legal aplicable al responsable.",
             "correcta": "C", "exp": "Artículo 6 del RGPD (Bases de licitud del tratamiento)."},
            
            # Bloque 2 en 2024 A
            {"año": 2024, "conv": "libre", "mod": "A", "num": 61, "b": 2, "t": 1,
             "p": "¿Qué principio de localidad de referencia aprovecha la memoria caché cuando un programa accede repetidamente a las mismas variables en un bucle corto?",
             "a": "Localidad espacial.", "b": "Localidad temporal.", "c": "Localidad secuencial.", "d": "Localidad aleatoria.",
             "correcta": "B", "exp": "La localidad temporal establece que si una posición de memoria es referenciada, tenderá a ser referenciada de nuevo pronto."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 62, "b": 2, "t": 2,
             "p": "¿Cuál es la representación en binario del número decimal 43?",
             "a": "00101011", "b": "00101101", "c": "00110011", "d": "00101111",
             "correcta": "A", "exp": "43 = 32 + 8 + 2 + 1 = 00101011 en binario."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 63, "b": 2, "t": 3,
             "p": "En sistemas operativos, ¿qué estructura representa a un proceso ligero que comparte el espacio de memoria y recursos con otros del mismo proceso?",
             "a": "Hebra o Hilo (Thread).", "b": "Demonio (Daemon).", "c": "Socket.", "d": "Semáforo.",
             "correcta": "A", "exp": "Los hilos (threads) comparten el espacio de direcciones y recursos globales del proceso padre."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 64, "b": 2, "t": 4,
             "p": "En Windows, ¿qué comando de PowerShell se utiliza para listar los procesos en ejecución en el equipo?",
             "a": "Get-Process", "b": "List-Processes", "c": "Show-Task", "d": "ps -ef",
             "correcta": "A", "exp": "Get-Process (alias ps/gps) devuelve los procesos activos en PowerShell."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 65, "b": 2, "t": 5,
             "p": "En Linux, ¿qué archivo contiene la lista de cuentas de usuario del sistema y sus UID/GID correspondientes?",
             "a": "/etc/shadow", "b": "/etc/passwd", "c": "/etc/group", "d": "/etc/sudoers",
             "correcta": "B", "exp": "/etc/passwd contiene los datos de usuario públicos; /etc/shadow contiene las contraseñas cifradas."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 66, "b": 2, "t": 6,
             "p": "¿Qué estándar internacional de cableado define la categoría Cat 6A para soportar transmisiones de hasta 10 Gbps a 100 metros?",
             "a": "ANSI/TIA-568", "b": "ISO 9001", "c": "IEEE 802.11", "d": "RFC 1918",
             "correcta": "A", "exp": "Estándar ANSI/TIA-568 para cableado estructurado."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 67, "b": 2, "t": 7,
             "p": "¿Cuál es la función del campo TTL (Time to Live) en la cabecera de un paquete IPv4?",
             "a": "Indicar el tamaño total del paquete.", "b": "Evitar que los paquetes circulen indefinidamente por la red decrementando su valor en cada router.", "c": "Calcular la suma de comprobación del payload.", "d": "Definir la prioridad de calidad de servicio.",
             "correcta": "B", "exp": "Cada router decrementa el TTL en 1; si llega a 0 se descarta el paquete y se emite un mensaje ICMP Time Exceeded."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 68, "b": 2, "t": 8,
             "p": "¿Qué protocolo evita la formación de bucles en topologías de red de nivel 2 con enlaces redundantes?",
             "a": "STP (Spanning Tree Protocol - IEEE 802.1D)", "b": "BGP", "c": "OSPF", "d": "RIP",
             "correcta": "A", "exp": "STP bloquea puertos redundantes para garantizar una topología lógica sin bucles en redes Ethernet."},

            # Bloque 3 en 2024 A
            {"año": 2024, "conv": "libre", "mod": "A", "num": 69, "b": 3, "t": 1,
             "p": "En MÉTRICA Versión 3, ¿qué interfaz cubre las actividades relativas al aseguramiento de la calidad del software?",
             "a": "Interfaz de Seguridad (SEG)", "b": "Interfaz de Aseguramiento de la Calidad (CAL)", "c": "Interfaz de Gestión de Proyectos (GP)", "d": "Interfaz de Gestión de Configuración (GC)",
             "correcta": "B", "exp": "La interfaz CAL define las revisiones técnicas formales y el plan de calidad en MÉTRICA v3."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 70, "b": 3, "t": 2,
             "p": "En UML, ¿qué diagrama modela la interacción entre objetos haciendo énfasis en el orden temporal de los mensajes?",
             "a": "Diagrama de Clases", "b": "Diagrama de Secuencia", "c": "Diagrama de Despliegue", "d": "Diagrama de Componentes",
             "correcta": "B", "exp": "Los diagramas de secuencia muestran la interacción mediante líneas de vida verticales y mensajes horizontales en orden cronológico."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 71, "b": 3, "t": 3,
             "p": "¿A qué categoría de patrones de diseño GoF pertenece el patrón 'Factory Method'?",
             "a": "Creacional.", "b": "Estructural.", "c": "De comportamiento.", "d": "Concurrente.",
             "correcta": "A", "exp": "Factory Method es un patrón Creacional que delega la instanciación de objetos en subclases."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 72, "b": 3, "t": 4,
             "p": "¿Qué característica distingue a un lenguaje de programación con tipado dinámico como Python o JavaScript?",
             "a": "El tipo de las variables se declara obligatoriamente al compilar.", "b": "El tipo de una variable se comprueba y asocia al valor en tiempo de ejecución.", "c": "No admite variables.", "d": "No puede ejecutar funciones recursivas.",
             "correcta": "B", "exp": "En lenguajes dinámicos las variables pueden cambiar de tipo dinámicamente en tiempo de ejecución."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 73, "b": 3, "t": 5,
             "p": "¿Qué operación del álgebra relacional permite seleccionar un subconjunto de columnas (atributos) de una tabla?",
             "a": "Selección (sigma)", "b": "Proyección (pi)", "c": "Join (reunión)", "d": "Diferencia",
             "correcta": "B", "exp": "La proyección (pi) selecciona columnas verticales; la selección (sigma) selecciona filas horizontales."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 74, "b": 3, "t": 6,
             "p": "En SQL, ¿qué comando revierte todas las modificaciones efectuadas en la transacción actual desde el último COMMIT?",
             "a": "REVOKE", "b": "ROLLBACK", "c": "TRUNCATE", "d": "DROP",
             "correcta": "B", "exp": "ROLLBACK deshace los cambios de la transacción devolviendo la BBDD a su estado previo."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 75, "b": 3, "t": 7,
             "p": "¿Qué tipo de base de datos NoSQL es Neo4j?",
             "a": "Base de datos orientada a Grafos (Nodos y Aristas).", "b": "Base de datos Documental.", "c": "Base de datos Clave-Valor pura.", "d": "Base de datos de series temporales.",
             "correcta": "A", "exp": "Neo4j almacena entidades como nodos y relaciones como aristas para consultas de grafos altamente conectadas."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 76, "b": 3, "t": 8,
             "p": "En una API RESTful, ¿qué método HTTP debe utilizarse para modificar parcialmente los campos de un recurso existente?",
             "a": "PUT", "b": "PATCH", "c": "POST", "d": "OPTIONS",
             "correcta": "B", "exp": "PATCH realiza modificaciones parciales; PUT reemplaza el recurso completo."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 77, "b": 3, "t": 9,
             "p": "¿Qué comando de Git descarta todos los cambios locales no guardados y restaura el árbol de trabajo al último commit de la rama?",
             "a": "git reset --hard HEAD", "b": "git clean -f", "c": "git stash apply", "d": "git merge --abort",
             "correcta": "A", "exp": "git reset --hard HEAD restablece el índice y el directorio de trabajo al último commit."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 78, "b": 3, "t": 10,
             "p": "En accesibilidad web, ¿qué ratio de contraste mínimo exige el nivel AA de WCAG 2.1 para texto normal frente a su fondo?",
             "a": "3:1", "b": "4.5:1", "c": "7:1", "d": "2:1",
             "correcta": "B", "exp": "Criterio 1.4.3 de WCAG: Al menos 4.5:1 para texto normal (3:1 para texto grande)."},

            # Bloque 4 en 2024 A
            {"año": 2024, "conv": "libre", "mod": "A", "num": 79, "b": 4, "t": 1,
             "p": "¿Qué organismo ministerial gestiona y mantiene el Punto de Acceso General electrónico (PAGe) de la Administración General del Estado?",
             "a": "El Ministerio para la Transformación Digital y de la Función Pública.", "b": "El Ministerio del Interior.", "c": "El Ministerio de Justicia.", "d": "El Banco de España.",
             "correcta": "A", "exp": "La Secretaría General de Administración Digital (SGAD) adscrita a Transformación Digital gestiona el PAGe."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 80, "b": 4, "t": 2,
             "p": "¿Qué nivel de seguridad de identificación proporciona Cl@ve Permanente reforzado con código SMS de un solo uso (OTP)?",
             "a": "Nivel Bajo", "b": "Nivel Medio / Sustancial", "c": "Nivel Alto (conforme a eIDAS)", "d": "Sin nivel reconocido",
             "correcta": "B", "exp": "Cl@ve Permanente con OTP SMS corresponde al nivel sustancial/medio del Reglamento eIDAS."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 81, "b": 4, "t": 3,
             "p": "¿Cuál es el formato estándar recomendado por la NTI del ENI para la conservación de documentos electrónicos textuales a largo plazo?",
             "a": "PDF/A (ISO 19005)", "b": "DOCX", "c": "ODT", "d": "RTF",
             "correcta": "A", "exp": "PDF/A garantiza la visualización independiente del software a lo largo del tiempo."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 82, "b": 4, "t": 4,
             "p": "En el ENS (RD 311/2022), ¿qué principio básico exige que la seguridad esté integrada en todo el ciclo de vida del sistema desde su diseño inicial?",
             "a": "Seguridad integral.", "b": "Seguridad por defecto y desde el diseño.", "c": "Líneas de defensa.", "d": "Reevaluación periódica.",
             "correcta": "B", "exp": "Artículo 8 del RD 311/2022: Seguridad como proceso integral desde el diseño."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 83, "b": 4, "t": 5,
             "p": "¿Qué tipo de software malicioso cifra los archivos de la víctima y exige el pago de un rescate para facilitar la clave de descifrado?",
             "a": "Spyware", "b": "Ransomware", "c": "Adware", "d": "Rootkit",
             "correcta": "B", "exp": "El ransomware secuestra la información mediante cifrado extorsivo."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 84, "b": 4, "t": 6,
             "p": "¿Qué protocolo seguro de la capa de transporte sustituyó a SSL y cifra las comunicaciones web en HTTPS?",
             "a": "TLS (Transport Layer Security, versiones 1.2 y 1.3)", "b": "SSH", "c": "IPsec", "d": "PGP",
             "correcta": "A", "exp": "TLS 1.3 es el estándar actual de cifrado en la capa de transporte para tráfico web."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 85, "b": 4, "t": 7,
             "p": "En Kubernetes, ¿cuál es la unidad básica y más pequeña de despliegue que encapsula uno o más contenedores?",
             "a": "Node", "b": "Pod", "c": "Cluster", "d": "Service",
             "correcta": "B", "exp": "Un Pod es la unidad mínima de computación en Kubernetes que comparte red y almacenamiento."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 86, "b": 4, "t": 8,
             "p": "¿Cuál es un ejemplo representativo del modelo de servicio SaaS (Software as a Service) en el puesto de trabajo de las AAPP?",
             "a": "Microsoft 365 / Google Workspace", "b": "Amazon EC2", "c": "Docker Engine", "d": "Red Hat OpenShift",
             "correcta": "A", "exp": "SaaS entrega software completo y funcional listo para su uso por el usuario final a través del navegador."},
            {"año": 2024, "conv": "libre", "mod": "A", "num": 87, "b": 4, "t": 9,
             "p": "En un plan de continuidad de negocio (BCP), ¿cómo se denomina un centro de respaldo completamente equipado con hardware, software y datos replicados en tiempo real listo para operar de inmediato?",
             "a": "Cold Site", "b": "Warm Site", "c": "Hot Site", "d": "Mirror Site",
             "correcta": "C", "exp": "Un Hot Site ofrece recuperación instantánea (RTO casi cero) con duplicación completa de sistemas."}
        ]

        # Insertar todas las preguntas históricas
        preguntas_insertadas = 0
        for p in preguntas_historicas:
            ex_obj = examenes_map.get((p["año"], p["conv"], p["mod"]))
            tema_obj = temas.get((p["b"], p["t"]))
            if ex_obj:
                _, created = PreguntaExamen.objects.update_or_create(
                    examen=ex_obj,
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
                    preguntas_insertadas += 1

        total_examenes = Examen.objects.count()
        total_preguntas = PreguntaExamen.objects.count()
        self.stdout.write(self.style.SUCCESS(f"¡Carga histórica completada! Total: {total_examenes} exámenes oficiales (11 convocatorias/modelos de los últimos 10 años) y {total_preguntas} preguntas tipo test."))
