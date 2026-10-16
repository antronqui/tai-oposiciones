from django.core.management.base import BaseCommand
from temario.models import Bloque, Tema
from examenes.models import Examen, PreguntaExamen


class Command(BaseCommand):
    help = "Amplía las preguntas de examen oficiales del Bloque IV para tener una distribución equilibrada en todos los bloques."

    def handle(self, *args, **options):
        temas = {t.numero: t for t in Tema.objects.filter(bloque__numero=4)}
        ex_2022_b = Examen.objects.filter(año=2022, modelo="B").first()
        ex_2020_a = Examen.objects.filter(año=2020, modelo="A").first()
        ex_2018_a = Examen.objects.filter(año=2018, modelo="A").first()

        preguntas_b4 = [
            # T1: Adm Electrónica
            {"ex": ex_2020_a, "num": 88, "t": 1,
             "p": "¿Qué requisito es indispensable para la validez de las copias electrónicas auténticas expedidas por las Administraciones Públicas?",
             "a": "Que se expidan únicamente en papel timbrado.",
             "b": "Que incorporen los metadatos que acrediten su condición de copia y que se emitan a partir de un documento electrónico original o digitalizado con CSV/firma.",
             "c": "Que se autoricen por el Delegado del Gobierno.",
             "d": "Que no superen los 10 megabytes.",
             "correcta": "B", "exp": "Artículo 27 de la Ley 39/2015."},
            {"ex": ex_2018_a, "num": 89, "t": 1,
             "p": "En la AGE, ¿qué sistema permite la gestión automatizada del Registro Electrónico General (REG) para la recepción y remisión de solicitudes?",
             "a": "GEISER (Gestión Integrada de Servicios de Registro).",
             "b": "RED SARA.",
             "c": "MINERVA.",
             "d": "BADARAL.",
             "correcta": "A", "exp": "GEISER es la solución de registro integral en la nube de la SGAD certificada con SICRES 3.0."},

            # T2: Firma
            {"ex": ex_2022_b, "num": 90, "t": 2,
             "p": "Según la Ley 6/2020, ¿cuál es el período máximo general de validez de los certificados electrónicos cualificados de firma?",
             "a": "2 años.", "b": "5 años.", "c": "10 años.", "d": "Indefinido.",
             "correcta": "B", "exp": "Artículo 6 de la Ley 6/2020: El período de validez no podrá ser superior a 5 años."},
            {"ex": ex_2020_a, "num": 91, "t": 2,
             "p": "¿Qué formato de firma electrónica avanzada es el más adecuado cuando se requiere firmar un fichero XML manteniendo la firma en el propio documento?",
             "a": "CAdES", "b": "XAdES (XML Advanced Electronic Signature)", "c": "PAdES", "d": "CMS",
             "correcta": "B", "exp": "XAdES es el estándar ETSI para firmas electrónicas en documentos XML."},

            # T3: ENI
            {"ex": ex_2018_a, "num": 92, "t": 3,
             "p": "Según la NTI de Digitalización de Documentos del ENI, ¿cuál es la resolución mínima obligatoria en la digitalización de documentos en papel?",
             "a": "72 ppp", "b": "150 ppp", "c": "200 ppp", "d": "600 ppp",
             "correcta": "C", "exp": "La NTI de Digitalización de Documentos establece una resolución mínima de 200 píxeles por pulgada (ppp)."},
            {"ex": ex_2022_b, "num": 93, "t": 3,
             "p": "¿Cuál es la plataforma web del Estado destinada a promover la reutilización y compartición de aplicaciones y activos tecnológicos entre Administraciones Públicas?",
             "a": "PAe", "b": "CTT (Centro de Transferencia de Tecnología)", "c": "DEHú", "d": "BOE",
             "correcta": "B", "exp": "El CTT (ctt.administracion.gob.es) publica el catálogo de soluciones reutilizables del Sector Público."},

            # T4: ENS
            {"ex": ex_2020_a, "num": 94, "t": 4,
             "p": "En el Esquema Nacional de Seguridad (RD 311/2022), ¿qué dimensión de seguridad garantiza que la información no sea accesible ni revelada a individuos no autorizados?",
             "a": "Disponibilidad", "b": "Integridad", "c": "Confidencialidad", "d": "Autenticidad",
             "correcta": "C", "exp": "Anexo I del RD 311/2022."},
            {"ex": ex_2018_a, "num": 95, "t": 4,
             "p": "¿Qué guía de la serie CCN-STIC del Centro Criptológico Nacional establece las pautas para la adecuación al Esquema Nacional de Seguridad?",
             "a": "Guía CCN-STIC 801 / Serie 800", "b": "Guía CCN-STIC 100", "c": "Guía CCN-STIC 400", "d": "Guía CCN-STIC 500",
             "correcta": "A", "exp": "La Serie 800 de las Guías CCN-STIC está dedicada íntegramente al ENS."},

            # T5: Ciberseguridad
            {"ex": ex_2022_b, "num": 96, "t": 5,
             "p": "¿Qué tipo de ataque web se produce cuando un atacante engaña a la aplicación para que ejecute comandos SQL maliciosos no previstos a través de los campos de entrada?",
             "a": "Cross-Site Scripting (XSS)", "b": "SQL Injection (SQLi)", "c": "Cross-Site Request Forgery (CSRF)", "d": "Clickjacking",
             "correcta": "B", "exp": "SQL Injection manipula la consulta SQL en la base de datos backend."},
            {"ex": ex_2020_a, "num": 97, "t": 5,
             "p": "¿Cómo se denomina la herramienta desarrollada por el CCN-CERT para la gestión centralizada y notificación de incidentes de seguridad en el sector público?",
             "a": "LUCIA", "b": "CARMEN", "c": "CLARA", "d": "PILAR",
             "correcta": "A", "exp": "LUCIA es la herramienta del CCN-CERT para gestión de ciberincidentes; PILAR es para análisis de riesgos Magerit."},

            # T6: Criptografía
            {"ex": ex_2018_a, "num": 98, "t": 6,
             "p": "¿Qué algoritmo de cifrado simétrico por bloques fue seleccionado por el NIST en 2001 como estándar federal y utiliza tamaños de bloque de 128 bits?",
             "a": "DES", "b": "AES (Rijndael)", "c": "RC4", "d": "Blowfish",
             "correcta": "B", "exp": "AES (Advanced Encryption Standard) sustituyó a DES."},
            {"ex": ex_2022_b, "num": 99, "t": 6,
             "p": "En una infraestructura de clave pública (PKI), ¿qué protocolo en red se utiliza para la sincronización horaria precisa de servidores y sellado de tiempo?",
             "a": "SNMP", "b": "NTP (Network Time Protocol)", "c": "SMTP", "d": "FTP",
             "correcta": "B", "exp": "NTP (puerto 123 UDP) sincroniza los relojes de los sistemas informáticos."},

            # T7: CPD y Docker
            {"ex": ex_2020_a, "num": 100, "t": 7,
             "p": "En Docker, ¿qué comando se utiliza para descargar una imagen desde un registro remoto como Docker Hub sin ejecutarla?",
             "a": "docker run", "b": "docker pull", "c": "docker build", "d": "docker push",
             "correcta": "B", "exp": "docker pull descarga la imagen; docker run la descarga (si no existe) y la ejecuta en un contenedor."},
            {"ex": ex_2018_a, "num": 101, "t": 7,
             "p": "¿Qué tipo de sistema de alimentación ininterrumpida (SAI / UPS) proporciona aislamiento total contra perturbaciones eléctricas alimentando la carga continuamente desde el inversor?",
             "a": "SAI Off-line (Standby)", "b": "SAI Line-Interactive", "c": "SAI On-line de Doble Conversión", "d": "Regulador de tensión básico",
             "correcta": "C", "exp": "Los SAIs On-line de doble conversión rectifican de CA a CC y vuelven a invertir a CA continuamente."},

            # T8: Cloud
            {"ex": ex_2022_b, "num": 102, "t": 8,
             "p": "¿Cuál es la principal ventaja del despliegue en Nube Híbrida para una organización del Sector Público?",
             "a": "Eliminar la necesidad de conexión a Internet.", "b": "Permitir mantener los datos y sistemas más críticos o confidenciales en una nube privada local mientras se aprovecha la elasticidad de nubes públicas para cargas dinámicas.", "c": "Evitar el uso de cortafuegos.", "d": "Reducir a cero el consumo de ancho de banda.",
             "correcta": "B", "exp": "La nube híbrida combina la seguridad y control del Cloud privado con la escalabilidad del Cloud público."},

            # T9: Continuidad DRP
            {"ex": ex_2020_a, "num": 103, "t": 9,
             "p": "¿Qué estándar internacional certificable especifica los requisitos para implementar un Sistema de Gestión de la Continuidad del Negocio (SGCN)?",
             "a": "ISO 9001", "b": "ISO 27001", "c": "ISO 22301", "d": "ISO 14001",
             "correcta": "C", "exp": "ISO 22301 es la norma internacional de Continuidad de Negocio (BCP)."}
        ]

        for p in preguntas_b4:
            if p["ex"]:
                tema_obj = temas.get(p["t"])
                PreguntaExamen.objects.update_or_create(
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

        self.stdout.write(self.style.SUCCESS("Preguntas adicionales del Bloque IV añadidas con éxito."))
