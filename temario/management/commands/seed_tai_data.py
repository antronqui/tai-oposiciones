from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Invitacion, UserProfile
from temario.models import Bloque, Tema, Subtema, Concepto
from tarjetas.models import Tarjeta
from examenes.models import Examen, PreguntaExamen
import datetime


class Command(BaseCommand):
    help = "Carga el temario oficial íntegro TAI (36 temas en 4 bloques), banco de preguntas INAP y flashcards trazables."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Iniciando carga del temario oficial íntegro TAI (36 temas)..."))

        # 1. Usuarios e invitaciones
        email_admin = "antronqui@gmail.com"
        email_test = "opositor@tai.es"

        Invitacion.objects.get_or_create(email=email_admin, defaults={"activo": True, "comentario": "Administrador Principal"})
        Invitacion.objects.get_or_create(email=email_test, defaults={"activo": True, "comentario": "Usuario de pruebas"})

        if not User.objects.filter(username="admin").exists():
            admin_user = User.objects.create_superuser("admin", email_admin, "admin1234")
            admin_user.first_name = "Juan Antonio"
            admin_user.last_name = "Montes"
            admin_user.save()
            admin_user.profile.horas_semanales = 15
            admin_user.profile.nivel_previo = "medio"
            admin_user.profile.fecha_objetivo = datetime.date(2027, 6, 1)
            admin_user.profile.onboarding_completado = True
            admin_user.profile.save()

        # 2. Los 4 Bloques Oficiales TAI
        bloques_data = [
            {
                "numero": 1,
                "nombre": "Organización del Estado y Administración Pública",
                "descripcion": "Constitución Española, Gobierno, Ley 40/2015, Ley 39/2015, TREBEP, Presupuestos Generales del Estado, Políticas de Igualdad, Transparencia y Protección de Datos (RGPD/LOPDGDD).",
                "icono": "bi-bank"
            },
            {
                "numero": 2,
                "nombre": "Tecnología Básica",
                "descripcion": "Arquitectura de computadores, representación y codificación de datos, sistemas operativos (Windows, Linux), arquitectura de redes, modelo OSI, pila TCP/IP, direccionamiento IPv4/IPv6 y equipos de interconexión.",
                "icono": "bi-cpu"
            },
            {
                "numero": 3,
                "nombre": "Desarrollo de Sistemas",
                "descripcion": "Metodologías de desarrollo (MÉTRICA v3, Scrum, Kanban), modelado UML, patrones de diseño, lenguajes de programación, modelo relacional, SQL, SGBD, NoSQL, desarrollo web, APIs RESTful, Git, CI/CD y accesibilidad (RD 1112/2018).",
                "icono": "bi-code-slash"
            },
            {
                "numero": 4,
                "nombre": "Sistemas y Comunicaciones",
                "descripcion": "Administración Electrónica (SIR, DEHú), firma e identificación (eIDAS, Cl@ve, @firma), Esquema Nacional de Interoperabilidad (RD 4/2010), Esquema Nacional de Seguridad (RD 311/2022), ciberseguridad (CCN-CERT), criptografía, CPD, virtualización, Docker, Cloud y continuidad de negocio (DRP/BCP).",
                "icono": "bi-shield-check"
            }
        ]

        bloques_map = {}
        for b_data in bloques_data:
            b, _ = Bloque.objects.update_or_create(
                numero=b_data["numero"],
                defaults={
                    "nombre": b_data["nombre"],
                    "descripcion": b_data["descripcion"],
                    "icono": b_data["icono"]
                }
            )
            bloques_map[b.numero] = b

        # 3. Los 36 Temas Oficiales del Programa TAI
        temas_completos = [
            # ================= BLOQUE I (9 Temas) =================
            {
                "bloque": 1, "numero": 1,
                "titulo": "La Constitución Española de 1978. Principios, derechos y deberes fundamentales. La Corona y las Cortes Generales.",
                "fuente": "BOE - Constitución Española de 1978",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229",
                "subtemas": ["Estructura y valores superiores", "Derechos y deberes fundamentales (Título I)", "Garantía y suspensión de derechos", "La Corona y las Cortes Generales", "El Poder Judicial"]
            },
            {
                "bloque": 1, "numero": 2,
                "titulo": "El Gobierno y la Administración General del Estado. Organización central, territorial y exterior.",
                "fuente": "BOE - Ley 50/1997 del Gobierno y Ley 40/2015",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-1997-25336",
                "subtemas": ["El Consejo de Ministros y el Presidente del Gobierno", "Órganos superiores y directivos de la AGE", "Delegados y Subdelegados del Gobierno", "Comunidades Autónomas y Administración Local"]
            },
            {
                "bloque": 1, "numero": 3,
                "titulo": "Régimen Jurídico del Sector Público: Ley 40/2015. Principios de actuación, órganos colegiados y convenios.",
                "fuente": "BOE - Ley 40/2015 de Régimen Jurídico del Sector Público",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566",
                "subtemas": ["Principios generales de la potestad sancionadora", "Régimen de los órganos colegiados", "Relaciones interadministrativas y convenios", "Sector público institucional"]
            },
            {
                "bloque": 1, "numero": 4,
                "titulo": "El Procedimiento Administrativo Común: Ley 39/2015. Interesados, fases y recursos administrativos.",
                "fuente": "BOE - Ley 39/2015 del Procedimiento Administrativo Común",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565",
                "subtemas": ["Capacidad de obrar y concepto de interesado", "Iniciación, ordenación, instrucción y finalización", "Eficacia y nulidad de los actos administrativos", "Recursos de alzada, potestativo de reposición y extraordinario de revisión"]
            },
            {
                "bloque": 1, "numero": 5,
                "titulo": "El personal funcionario al servicio de las AAPP: Real Decreto Legislativo 5/2015 (TREBEP).",
                "fuente": "BOE - RDL 5/2015 (Texto Refundido del Estatuto Básico del Empleado Público)",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11719",
                "subtemas": ["Clases de personal (funcionario, laboral, eventual)", "Derechos y deberes. Código de conducta", "Situaciones administrativas", "Régimen disciplinario y faltas"]
            },
            {
                "bloque": 1, "numero": 6,
                "titulo": "El presupuesto del Estado en España. Estructura, ciclo presupuestario y control del gasto público.",
                "fuente": "BOE - Ley 47/2003 General Presupuestaria",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2003-21614",
                "subtemas": ["Concepto y principios presupuestarios", "Estructura presupuestaria (orgánica, por programas, económica)", "Fases de ejecución del gasto (A, D, O, P)", "Control interno (IGAE) y externo (Tribunal de Cuentas)"]
            },
            {
                "bloque": 1, "numero": 7,
                "titulo": "Políticas de Igualdad de Género (LO 3/2007), contra la Violencia de Género (LO 1/2004) e integración de la discapacidad.",
                "fuente": "BOE - Ley Orgánica 3/2007 y Ley Orgánica 1/2004",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2007-6115",
                "subtemas": ["Principio de igualdad y tutela contra la discriminación", "Medidas de protección integral contra la violencia de género", "Planes de igualdad en la Administración General del Estado", "Acceso al empleo público de personas con discapacidad"]
            },
            {
                "bloque": 1, "numero": 8,
                "titulo": "Transparencia, acceso a la información pública y buen gobierno: Ley 19/2013.",
                "fuente": "BOE - Ley 19/2013 de Transparencia",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2013-12887",
                "subtemas": ["Publicidad activa y Portal de Transparencia", "Derecho de acceso a la información pública y sus límites", "El Consejo de Transparencia y Buen Gobierno (CTBG)"]
            },
            {
                "bloque": 1, "numero": 9,
                "titulo": "Protección de Datos Personales: Reglamento (UE) 2016/679 (RGPD) y Ley Orgánica 3/2018 (LOPDGDD).",
                "fuente": "BOE - Ley Orgánica 3/2018 y Reglamento General de Protección de Datos",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673",
                "subtemas": ["Principios del tratamiento de datos", "Derechos de los interesados (Acceso, Rectificación, Supresión, Oposición, Portabilidad, Limitación)", "El Delegado de Protección de Datos (DPD)", "La Agencia Española de Protección de Datos (AEPD)"]
            },

            # ================= BLOQUE II (8 Temas) =================
            {
                "bloque": 2, "numero": 1,
                "titulo": "Arquitectura de ordenadores. CPU, ALU, unidad de control, registros, memoria y periféricos.",
                "fuente": "INAP - Programa Oficial de Tecnología Básica TAI",
                "url": "https://sede.inap.gob.es",
                "subtemas": ["Arquitectura Von Neumann y Harvard", "Estructura de la CPU: ALU, UC y banco de registros", "Jerarquía de memoria: registros, cachés (L1/L2/L3), RAM, memoria virtual", "Buses del sistema (datos, direcciones, control) y periféricos"]
            },
            {
                "bloque": 2, "numero": 2,
                "titulo": "Representación y codificación de la información. Sistemas de numeración y códigos de caracteres.",
                "fuente": "Estándares IEEE / Unicode Consortium",
                "url": "https://www.unicode.org",
                "subtemas": ["Sistemas de numeración (binario, octal, hexadecimal) y conversiones", "Representación de enteros (complemento a 2) y coma flotante (IEEE 754)", "Codificación de texto: ASCII, UTF-8, UTF-16", "Detección y corrección de errores (Paridad, Hamming, CRC)"]
            },
            {
                "bloque": 2, "numero": 3,
                "titulo": "Sistemas operativos: conceptos, componentes y gestión de recursos.",
                "fuente": "INAP - Fundamentos de Sistemas Operativos",
                "url": "https://sede.inap.gob.es",
                "subtemas": ["Estructura del SO: núcleo, llamadas al sistema (syscalls)", "Gestión de procesos: estados, PCB y algoritmos de planificación (FIFO, Round Robin, SJF)", "Gestión de memoria: paginación, segmentación y memoria virtual", "Gestión de entrada/salida y sistemas de archivos"]
            },
            {
                "bloque": 2, "numero": 4,
                "titulo": "Sistemas operativos Windows: arquitectura, administración, servicios y seguridad.",
                "fuente": "Microsoft Learn - Windows Architecture",
                "url": "https://learn.microsoft.com/windows",
                "subtemas": ["Arquitectura del kernel Windows (HAL, Executive, Win32)", "Gestión de usuarios, grupos y permisos NTFS", "Registro de Windows y servicios del sistema", "Línea de comandos CMD y PowerShell"]
            },
            {
                "bloque": 2, "numero": 5,
                "titulo": "Sistemas operativos Linux/Unix: arquitectura, administración, comandos y scripting.",
                "fuente": "Linux Foundation / GNU Documentation",
                "url": "https://www.gnu.org",
                "subtemas": ["Arquitectura del kernel Linux y distribuciones", "Sistema de ficheros (jerarquía FHS y ext4)", "Gestión de usuarios, grupos y permisos (chmod, chown, ACLs)", "Comandos esenciales de administración y scripts en Bash"]
            },
            {
                "bloque": 2, "numero": 6,
                "titulo": "Redes de computadores: conceptos fundamentales, topologías y el Modelo OSI de ISO.",
                "fuente": "ISO/IEC 7498-1 - Open Systems Interconnection",
                "url": "https://www.iso.org",
                "subtemas": ["Clasificación de redes (LAN, MAN, WAN) y topologías (estrella, bus, malla)", "Medios de transmisión (par trenzado, fibra óptica, medios inalámbricos)", "Las 7 capas del Modelo OSI y sus funciones", "Encapsulamiento y unidades de datos de protocolo (PDU)"]
            },
            {
                "bloque": 2, "numero": 7,
                "titulo": "La arquitectura TCP/IP: niveles, protocolos y direccionamiento IPv4/IPv6.",
                "fuente": "IETF RFCs (RFC 791, RFC 793, RFC 8200)",
                "url": "https://www.rfc-editor.org",
                "subtemas": ["Pila TCP/IP y correspondencia con el modelo OSI", "Nivel de red: Protocolos IP, ICMP, ARP; Direccionamiento IPv4 y subredes CIDR", "Protocolo IPv6: estructura de cabecera y tipos de direcciones (Unicast, Multicast, Anycast)", "Nivel de transporte: TCP (fiable, 3-way handshake) vs UDP (no orientado a conexión)", "Protocolos de aplicación: DNS, DHCP, HTTP/HTTPS, FTP, SMTP, SSH"]
            },
            {
                "bloque": 2, "numero": 8,
                "titulo": "Equipos de interconexión y redes de área local (LAN, VLAN, Wi-Fi y WAN).",
                "fuente": "IEEE 802 Standards",
                "url": "https://www.ieee.org",
                "subtemas": ["Equipos de red: Switches (Capa 2/3), Routers y Puntos de Acceso", "Redes LAN Ethernet (IEEE 802.3) y Redes de Área Local Virtual (VLANs 802.1Q)", "Redes Inalámbricas Wi-Fi (Estándares IEEE 802.11a/b/g/n/ac/ax)", "Tecnologías de acceso WAN y enrutamiento (estático y dinámico)"]
            },

            # ================= BLOQUE III (10 Temas) =================
            {
                "bloque": 3, "numero": 1,
                "titulo": "Metodologías de desarrollo de software: MÉTRICA Versión 3 y Metodologías Ágiles.",
                "fuente": "PAe - Metodología MÉTRICA Versión 3",
                "url": "https://administracionelectronica.gob.es/pae_Home/pae_Metodologias/pae_Metrica_v3.html",
                "subtemas": ["Estructura de MÉTRICA v3: Procesos principales (PSI, EVS, DSI, CSI, IAS)", "Interfaces de MÉTRICA v3 (Gestión de Proyectos, Seguridad, Aseguramiento de Calidad)", "Metodologías Ágiles: Principios del Manifiesto Ágil", "Framework Scrum (Roles, Eventos, Artefactos) y Kanban"]
            },
            {
                "bloque": 3, "numero": 2,
                "titulo": "Análisis y diseño orientado a objetos: Lenguaje de Modelado Unificado (UML).",
                "fuente": "Object Management Group (OMG) UML Standard",
                "url": "https://www.omg.org/spec/UML/",
                "subtemas": ["Conceptos OOP: Clases, objetos, herencia, polimorfismo, encapsulamiento", "Diagramas estructurales: Diagrama de clases, componentes, despliegue", "Diagramas de comportamiento: Casos de uso, secuencia, actividades, estados"]
            },
            {
                "bloque": 3, "numero": 3,
                "titulo": "Patrones de diseño de software (GoF) y arquitecturas de software.",
                "fuente": "Gang of Four (GoF) Patterns Standard",
                "url": "https://inap.es",
                "subtemas": ["Patrones Creacionales: Singleton, Factory Method, Abstract Factory, Builder", "Patrones Estructurales: Adapter, Composite, Decorator, Facade, Proxy", "Patrones de Comportamiento: Observer, Strategy, Command, Iterator", "Patrones Arquitectónicos: MVC (Modelo-Vista-Controlador), Microservicios"]
            },
            {
                "bloque": 3, "numero": 4,
                "titulo": "Lenguajes de programación: paradigmas, características y entornos de ejecución.",
                "fuente": "INAP - Lenguajes de Programación",
                "url": "https://inap.es",
                "subtemas": ["Paradigmas: Imperativo, Orientado a Objetos, Funcional", "Compiladores, intérpretes, bytecode y máquinas virtuales", "Lenguajes modernos: Java (JVM), Python, C#, JavaScript/TypeScript, PHP", "Gestión de memoria y Garbage Collection"]
            },
            {
                "bloque": 3, "numero": 5,
                "titulo": "Bases de datos relacionales: Modelo Relacional, normalización y álgebra relacional.",
                "fuente": "Codd's Relational Model Standard",
                "url": "https://inap.es",
                "subtemas": ["Conceptos del modelo relacional: Tablas, tuplas, atributos, claves primarias y foráneas", "Integridad de datos: Integridad de entidad e integridad referencial", "Formas Normales: 1FN, 2FN, 3FN y Boyce-Codd (BCNF)", "Operaciones del Álgebra Relacional (Selección, Proyección, Unión, Join)"]
            },
            {
                "bloque": 3, "numero": 6,
                "titulo": "Lenguaje de consulta estructurado (SQL): DDL, DML, DCL y TCL.",
                "fuente": "ANSI/ISO SQL Standard",
                "url": "https://inap.es",
                "subtemas": ["Sentencias DDL: CREATE, ALTER, DROP, TRUNCATE", "Sentencias DML: SELECT, INSERT, UPDATE, DELETE", "Cláusulas de consulta: WHERE, GROUP BY, HAVING, ORDER BY", "Tipos de Joins (INNER, LEFT, RIGHT, FULL OUTER) y Subconsultas", "Sentencias DCL (GRANT, REVOKE) y TCL (COMMIT, ROLLBACK)"]
            },
            {
                "bloque": 3, "numero": 7,
                "titulo": "Sistemas Gestores de Bases de Datos (SGBD) Relacionales y Bases de Datos NoSQL.",
                "fuente": "INAP - Sistemas de Gestión de Bases de Datos",
                "url": "https://inap.es",
                "subtemas": ["Arquitectura ANSI-SPARC de 3 niveles", "Propiedades ACID de transacciones y niveles de aislamiento", "Índices (B-Tree, Hash) y optimización de consultas", "SGBD Relacionales: PostgreSQL, MySQL, Oracle, SQL Server", "Bases de datos NoSQL: Documentales (MongoDB), Clave-Valor (Redis), Grafos (Neo4j), Columnares"]
            },
            {
                "bloque": 3, "numero": 8,
                "titulo": "Desarrollo web y aplicaciones cliente-servidor: Frontend, Backend y APIs Web.",
                "fuente": "W3C Standards / MDN Web Docs",
                "url": "https://www.w3.org",
                "subtemas": ["Arquitectura Web de 3 capas: Presentación, Lógica de Negocio y Datos", "Frontend: HTML5 semántico, CSS3, JavaScript (ES6+) y frameworks (React, Vue, Angular)", "Backend: Servidores de aplicaciones y frameworks (Django, Spring Boot, Node.js)", "Servicios Web y APIs: Arquitectura RESTful (JSON), SOAP (XML/WSDL) y GraphQL"]
            },
            {
                "bloque": 3, "numero": 9,
                "titulo": "Control de versiones, pruebas de software y Ciclo de Integración Continua (CI/CD).",
                "fuente": "Git SCM & IEEE Standard for Software Testing",
                "url": "https://git-scm.com",
                "subtemas": ["Control de versiones distribuido con Git (ramas, commit, merge, rebase)", "Plataformas colaborativas (GitHub, GitLab)", "Tipos de pruebas de software: Unitarias, Integración, Sistema, Rendimiento y Aceptación", "Integración y Despliegue Continuo (CI/CD)"]
            },
            {
                "bloque": 3, "numero": 10,
                "titulo": "Accesibilidad web y usabilidad: Real Decreto 1112/2018 y Pautas WCAG.",
                "fuente": "BOE - Real Decreto 1112/2018 sobre Accesibilidad Web del Sector Público",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2018-12699",
                "subtemas": ["Principios de accesibilidad WCAG: Perceptible, Operable, Comprensible y Robusto (POUR)", "Niveles de conformidad: A, AA (exigido en el sector público) y AAA", "Declaración de Accesibilidad e informes periódicos", "Herramientas de validación de accesibilidad"]
            },

            # ================= BLOQUE IV (9 Temas) =================
            {
                "bloque": 4, "numero": 1,
                "titulo": "Administración Electrónica en la AGE: Sedes electrónicas, Registro Electrónico y Notificaciones (DEHú/SIR).",
                "fuente": "PAe - Portal de Administración Electrónica",
                "url": "https://administracionelectronica.gob.es",
                "subtemas": ["Sede Electrónica y Punto de Acceso General electrónico (PAGe)", "Registro Electrónico General (REG) y Sistema de Interconexión de Registros (SIR)", "Notificaciones electrónicas: Dirección Electrónica Habilitada única (DEHú) y Notifica", "Intermediación de datos (PID)"]
            },
            {
                "bloque": 4, "numero": 2,
                "titulo": "Identificación, autenticación y firma electrónica: Reglamento eIDAS y Ley 6/2020. Plataformas Cl@ve y @firma.",
                "fuente": "BOE - Ley 6/2020 y Reglamento (UE) 910/2014 (eIDAS)",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2020-14046",
                "subtemas": ["Tipos de firma electrónica: Simple, Avanzada y Cualificada", "Certificados electrónicos y Prestadores de Servicios de Confianza", "Plataforma de Identificación Cl@ve (Cl@ve PIN, Cl@ve Permanente, Cl@ve Firma)", "Plataforma @firma y cliente AutoFirma"]
            },
            {
                "bloque": 4, "numero": 3,
                "titulo": "Esquema Nacional de Interoperabilidad (ENI): Real Decreto 4/2010 y Normas Técnicas de Interoperabilidad (NTI).",
                "fuente": "BOE - Real Decreto 4/2010 (ENI)",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2010-1331",
                "subtemas": ["Principios del ENI y dimensiones: Técnica, Semántica y Organizativa", "NTI de Documento Electrónico y Expediente Electrónico", "NTI de Digitalización de Documentos y Copiado Auténtico", "Catálogo de Estándares del ENI"]
            },
            {
                "bloque": 4, "numero": 4,
                "titulo": "Esquema Nacional de Seguridad (ENS): Real Decreto 311/2022. Principios, dimensiones y categorización.",
                "fuente": "BOE - Real Decreto 311/2022 (ENS)",
                "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191",
                "subtemas": ["Ámbito de aplicación y principios básicos del ENS", "Dimensiones de seguridad (Disponibilidad, Integridad, Confidencialidad, Autenticidad, Trazabilidad)", "Categorización de sistemas: Categoría Básica, Media y Alta", "Medidas de seguridad (Marco Organizativo, Operacional y Medidas de Protección)"]
            },
            {
                "bloque": 4, "numero": 5,
                "titulo": "Seguridad de la información y ciberseguridad: Amenazas, vulnerabilidades, ataques y guías CCN-STIC.",
                "fuente": "CCN-CERT - Centro Criptológico Nacional",
                "url": "https://www.ccn-cert.cni.es",
                "subtemas": ["Tipos de malware: Virus, gusanos, troyanos, ransomware, spyware", "Vulnerabilidades y ataques: Phishing, DoS/DDoS, SQL Injection, XSS, Man-in-the-Middle", "Sistemas de detección y prevención de intrusos (IDS/IPS) y Cortafuegos (Firewalls)", "Series de Guías CCN-STIC del Centro Criptológico Nacional"]
            },
            {
                "bloque": 4, "numero": 6,
                "titulo": "Criptografía y mecanismos de seguridad: Criptografía simétrica, asimétrica, hash y protocolos seguros.",
                "fuente": "NIST Cryptographic Standards / CCN-STIC",
                "url": "https://csrc.nist.gov",
                "subtemas": ["Criptografía Simétrica: Cifrado en bloque (AES, DES, 3DES) y cifrado en flujo", "Criptografía Asimétrica: Clave pública/privada (RSA, Criptografía de Curva Elíptica - ECC)", "Funciones Resumen (Hash): SHA-256, SHA-512, SHA-3", "Infraestructura de Clave Pública (PKI) y Autoridades de Certificación (CA)", "Protocolos de comunicación segura: SSL/TLS, SSH, IPsec y Redes Privadas Virtuales (VPN)"]
            },
            {
                "bloque": 4, "numero": 7,
                "titulo": "Centros de Proceso de Datos (CPD), virtualización de sistemas y contenedores (Docker/Kubernetes).",
                "fuente": "Standards TIA-942 / Docker Docs",
                "url": "https://docs.docker.com",
                "subtemas": ["Infraestructura de CPD: Climatización, extinción de incendios, suministro eléctrico (SAI/UPS) y Tiers (TIA-942)", "Virtualización: Hipervisores Tipo 1 (Bare-Metal: VMware ESXi, KVM) y Tipo 2 (VirtualBox)", "Contenerización con Docker: Imágenes, contenedores, Dockerfile y volúmenes", "Orquestación de contenedores con Kubernetes: Pods, Services, Deployments"]
            },
            {
                "bloque": 4, "numero": 8,
                "titulo": "Cloud Computing: Modelos de servicio (IaaS, PaaS, SaaS) y Estrategia Cloud de la AGE.",
                "fuente": "NIST SP 800-145 / Plan de Digitalización de las AAPP",
                "url": "https://administracionelectronica.gob.es",
                "subtemas": ["Modelos de servicio en la nube: IaaS (Infraestructura), PaaS (Plataforma), SaaS (Software)", "Modelos de despliegue: Nube Pública, Nube Privada, Nube Híbrida y Nube Comunitaria", "Características esenciales del Cloud (Escalabilidad, Elasticidad, Pago por uso)", "Estrategia Cloud de la Administración General del Estado"]
            },
            {
                "bloque": 4, "numero": 9,
                "titulo": "Continuidad de negocio, copias de seguridad y recuperación ante desastres (DRP/BCP).",
                "fuente": "ISO 22301 / Guías CCN-STIC",
                "url": "https://www.ccn-cert.cni.es",
                "subtemas": ["Tipos de copias de seguridad: Completa, Incremental, Diferencial y Regla 3-2-1", "Métricas clave de recuperación: RTO (Recovery Time Objective) y RPO (Recovery Point Objective)", "Planes de Continuidad de Negocio (BCP) y Planes de Recuperación ante Desastres (DRP)", "Centros de respaldo: Hot Site, Warm Site y Cold Site"]
            }
        ]

        temas_map = {}
        total_subtemas = 0
        for t_data in temas_completos:
            bloque = bloques_map[t_data["bloque"]]
            t, _ = Tema.objects.update_or_create(
                bloque=bloque,
                numero=t_data["numero"],
                defaults={
                    "titulo": t_data["titulo"],
                    "fuente_oficial": t_data["fuente"],
                    "url_oficial": t_data["url"],
                    "fecha_consulta": datetime.date.today(),
                }
            )
            temas_map[(bloque.numero, t.numero)] = t

            for i, st_nombre in enumerate(t_data["subtemas"], 1):
                Subtema.objects.get_or_create(
                    tema=t,
                    titulo=st_nombre,
                    defaults={"orden": i}
                )
                total_subtemas += 1

        self.stdout.write(self.style.SUCCESS(f"36 Temas oficiales TAI y {total_subtemas} subtemas normalizados cargados."))

        # 4. Banco Ampliado de Flashcards ("Una tarjeta = una idea")
        tarjetas_data = [
            # BLOQUE 1
            {
                "bloque": 1, "tema": 1, "tipo": "fecha",
                "pregunta": "¿En qué fecha fue aprobada la Constitución Española por las Cortes Generales?",
                "respuesta": "El 31 de octubre de 1978.",
                "explicacion": "Fue aprobada por las Cortes el 31 de octubre, ratificada por el pueblo español el 6 de diciembre y sancionada por el Rey el 27 de diciembre de 1978.",
                "dificultad": "facil", "fuente": "Constitución Española de 1978"
            },
            {
                "bloque": 1, "tema": 1, "tipo": "definicion",
                "pregunta": "¿Cuáles son los valores superiores del ordenamiento jurídico según el artículo 1.1 de la CE?",
                "respuesta": "La libertad, la justicia, la igualdad y el pluralismo político.",
                "explicacion": "Artículo 1.1 de la Constitución Española.",
                "dificultad": "facil", "fuente": "CE 1978, Art. 1.1"
            },
            {
                "bloque": 1, "tema": 3, "tipo": "procedimiento",
                "pregunta": "¿Quién ostenta el voto de calidad en caso de empate en los órganos colegiados según la Ley 40/2015?",
                "respuesta": "El Presidente del órgano colegiado.",
                "explicacion": "Artículo 19.2.c de la Ley 40/2015.",
                "dificultad": "facil", "fuente": "BOE Ley 40/2015, Art. 19"
            },
            {
                "bloque": 1, "tema": 4, "tipo": "definicion",
                "pregunta": "¿Qué plazo general establece la Ley 39/2015 para interponer el recurso de alzada contra un acto expreso?",
                "respuesta": "Un mes.",
                "explicacion": "Artículo 122 de la Ley 39/2015. Si el acto no fuera expreso, el solicitante y otros posibles interesados podrán interponer recurso de alzada en cualquier momento a partir del día siguiente a aquel en que se produzcan los efectos del silencio administrativo.",
                "dificultad": "media", "fuente": "BOE Ley 39/2015, Art. 122"
            },
            {
                "bloque": 1, "tema": 5, "tipo": "comparativa",
                "pregunta": "¿Qué diferencia existe entre el personal funcionario de carrera y el personal laboral en el TREBEP?",
                "respuesta": "El funcionario de carrera se rige por el Derecho Administrativo y una relación estatutaria; el personal laboral se rige por el Derecho Laboral mediante un contrato de trabajo.",
                "explicacion": "Artículos 9 y 11 del Real Decreto Legislativo 5/2015 (TREBEP).",
                "dificultad": "media", "fuente": "BOE RDL 5/2015 (TREBEP)"
            },
            {
                "bloque": 1, "tema": 8, "tipo": "organismo",
                "pregunta": "¿Qué órgano independiente vela por el cumplimiento de las obligaciones de publicidad activa y el derecho de acceso en la Ley 19/2013?",
                "respuesta": "El Consejo de Transparencia y Buen Gobierno (CTBG).",
                "explicacion": "Regulado en el Título III de la Ley 19/2013.",
                "dificultad": "facil", "fuente": "BOE Ley 19/2013, Art. 33"
            },
            {
                "bloque": 1, "tema": 9, "tipo": "definicion",
                "pregunta": "¿Cuáles son los conocidos como 'Derechos ARSOPOL' en materia de protección de datos según el RGPD/LOPDGDD?",
                "respuesta": "Acceso, Rectificación, Supresión (olvido), Oposición, Portabilidad y Limitación del tratamiento.",
                "explicacion": "Regulados en los Artículos 15 a 22 del RGPD (UE) 2016/679.",
                "dificultad": "media", "fuente": "RGPD (UE) 2016/679 / LO 3/2018"
            },

            # BLOQUE 2
            {
                "bloque": 2, "tema": 1, "tipo": "comparativa",
                "pregunta": "¿Cuál es la diferencia fundamental entre la arquitectura Von Neumann y la Harvard?",
                "respuesta": "Von Neumann utiliza un único bus y memoria compartida para datos e instrucciones; Harvard utiliza buses y memorias físicas separadas para datos e instrucciones.",
                "explicacion": "Harvard permite accesos simultáneos a instrucciones y datos, evitando el cuello de botella de Von Neumann.",
                "dificultad": "media", "fuente": "Manual de Arquitectura de Computadores INAP"
            },
            {
                "bloque": 2, "tema": 2, "tipo": "definicion",
                "pregunta": "¿Cuántos bytes utiliza la codificación UTF-8 para representar un carácter?",
                "respuesta": "Es una codificación de longitud variable que utiliza entre 1 y 4 bytes por carácter.",
                "explicacion": "Los primeros 128 caracteres (código ASCII) ocupan 1 solo byte en UTF-8.",
                "dificultad": "facil", "fuente": "Estándar Unicode RFC 3629"
            },
            {
                "bloque": 2, "tema": 3, "tipo": "definicion",
                "pregunta": "¿Qué es la 'inanición' (starvation) en la planificación de procesos de un Sistema Operativo?",
                "respuesta": "Situación en la que un proceso listo para ejecutarse espera indefinidamente en la cola de CPU porque otros procesos de mayor prioridad se ejecutan continuamente.",
                "explicacion": "Se resuelve mediante técnicas de envejecimiento (aging) que incrementan gradualmente la prioridad con el tiempo.",
                "dificultad": "media", "fuente": "Fundamentos de SO INAP"
            },
            {
                "bloque": 2, "tema": 5, "tipo": "procedimiento",
                "pregunta": "¿Qué comando Linux se utiliza para cambiar los permisos de un archivo a lectura, escritura y ejecución para el propietario, y solo lectura para el resto?",
                "respuesta": "chmod 744 <nombre_archivo>",
                "explicacion": "7 = 4(r)+2(w)+1(x) para el usuario; 4 = 4(r) para grupo; 4 = 4(r) para otros.",
                "dificultad": "facil", "fuente": "Manual GNU Coreutils"
            },
            {
                "bloque": 2, "tema": 6, "tipo": "procedimiento",
                "pregunta": "¿Cuáles son las 7 capas del Modelo OSI en orden desde la capa física (1) hasta la capa superior (7)?",
                "respuesta": "1. Física\n2. Enlace de Datos\n3. Red\n4. Transporte\n5. Sesión\n6. Presentación\n7. Aplicación",
                "explicacion": "Estándar ISO/IEC 7498-1.",
                "dificultad": "facil", "fuente": "ISO/IEC 7498-1"
            },
            {
                "bloque": 2, "tema": 7, "tipo": "definicion",
                "pregunta": "¿Qué máscara de subred en notación decimal equivale al prefijo CIDR /26?",
                "respuesta": "255.255.255.192",
                "explicacion": "Los primeros 26 bits son '1' (8+8+8+2 = 255.255.255.192), dejando 6 bits para hosts (64 direcciones, 62 útiles).",
                "dificultad": "media", "fuente": "IETF RFC 4632 (CIDR)"
            },
            {
                "bloque": 2, "tema": 7, "tipo": "comparativa",
                "pregunta": "¿Cuál es la diferencia principal de transporte entre TCP y UDP?",
                "respuesta": "TCP es orientado a conexión, fiable y con control de congestión (3-way handshake); UDP es no orientado a conexión, no garantiza entrega pero tiene menor latencia.",
                "explicacion": "Capa 4 (Transporte) del modelo OSI.",
                "dificultad": "facil", "fuente": "IETF RFC 793 / RFC 768"
            },

            # BLOQUE 3
            {
                "bloque": 3, "tema": 1, "tipo": "procedimiento",
                "pregunta": "¿Cuáles son los 5 procesos principales del ciclo de vida del software según MÉTRICA Versión 3?",
                "respuesta": "1. PSI (Planificación de Sistemas de Información)\n2. EVS (Estudio de Viabilidad del Sistema)\n3. DSI (Análisis y Diseño del Sistema)\n4. CSI (Construcción del Sistema)\n5. IAS (Implantación y Aceptación del Sistema)",
                "explicacion": "Metodología oficial de desarrollo de las Administraciones Públicas españolas.",
                "dificultad": "media", "fuente": "PAe - MÉTRICA v3"
            },
            {
                "bloque": 3, "tema": 3, "tipo": "definicion",
                "pregunta": "¿Cuál es el propósito del patrón de diseño creacional 'Singleton'?",
                "respuesta": "Garantizar que una clase tenga una única instancia en toda la aplicación y proporcionar un punto de acceso global a ella.",
                "explicacion": "Patrón GoF (Gang of Four) Creacional.",
                "dificultad": "facil", "fuente": "Patrones de Diseño GoF"
            },
            {
                "bloque": 3, "tema": 5, "tipo": "definicion",
                "pregunta": "¿Qué condición exige la Segunda Forma Normal (2FN) en el modelo relacional?",
                "respuesta": "Estar en 1FN y que todos los atributos que no forman parte de la clave primaria dependan funcionalmente de forma completa de toda la clave primaria (sin dependencias parciales).",
                "explicacion": "Aplica especialmente en tablas con claves primarias compuestas.",
                "dificultad": "media", "fuente": "Teoría Relacional Codd / ANSI SQL"
            },
            {
                "bloque": 3, "tema": 6, "tipo": "definicion",
                "pregunta": "¿Cuál es la diferencia entre las cláusulas WHERE y HAVING en una sentencia SQL SELECT?",
                "respuesta": "WHERE filtra filas antes de que se realice la agrupación (GROUP BY); HAVING filtra los grupos resultantes tras la agregación.",
                "explicacion": "HAVING se utiliza típicamente con funciones de agregación como COUNT, SUM, AVG, MAX, MIN.",
                "dificultad": "media", "fuente": "ANSI SQL Standard"
            },
            {
                "bloque": 3, "tema": 9, "tipo": "definicion",
                "pregunta": "¿Cuál es la diferencia entre 'git merge' y 'git rebase' al integrar cambios de ramas en Git?",
                "respuesta": "'git merge' crea un commit de fusión combinando los historiales manteniendo la estructura bifurcada; 'git rebase' reescribe el historial aplicando los commits de la rama actual uno a uno sobre la punta de la rama destino de forma lineal.",
                "explicacion": "Rebase crea un historial más limpio pero modifica los hashes SHA de los commits.",
                "dificultad": "media", "fuente": "Git SCM Documentation"
            },
            {
                "bloque": 3, "tema": 10, "tipo": "organismo",
                "pregunta": "¿Qué nivel de conformidad de las pautas WCAG es exigible con carácter general a los sitios web del sector público español según el Real Decreto 1112/2018?",
                "respuesta": "Nivel de conformidad AA (WCAG 2.1 nivel AA).",
                "explicacion": "Artículo 5 del Real Decreto 1112/2018.",
                "dificultad": "media", "fuente": "BOE Real Decreto 1112/2018, Art. 5"
            },

            # BLOQUE 4
            {
                "bloque": 4, "tema": 1, "tipo": "definicion",
                "pregunta": "¿Qué es el SIR (Sistema de Interconexión de Registros)?",
                "respuesta": "La plataforma de la AGE que permite el intercambio electrónico seguro de asientos registrales entre todas las Administraciones Públicas españolas conforme a la norma SICRES.",
                "explicacion": "Permite eliminar el trasvase de papel entre oficinas de registro de diferentes administraciones.",
                "dificultad": "media", "fuente": "PAe - Plataforma SIR"
            },
            {
                "bloque": 4, "tema": 2, "tipo": "definicion",
                "pregunta": "¿Qué tres modalidades principales de firma electrónica reconoce el Reglamento eIDAS (UE 910/2014)?",
                "respuesta": "1. Firma electrónica simple\n2. Firma electrónica avanzada\n3. Firma electrónica cualificada (con certificado cualificado y dispositivo cualificado)",
                "explicacion": "Solo la firma cualificada tiene una equivalencia jurídica automática y plena a la firma manuscrita.",
                "dificultad": "media", "fuente": "Reglamento eIDAS (UE) 910/2014, Art. 25"
            },
            {
                "bloque": 4, "tema": 3, "tipo": "definicion",
                "pregunta": "¿Cuáles son las 3 dimensiones de la interoperabilidad según el Esquema Nacional de Interoperabilidad (ENI RD 4/2010)?",
                "respuesta": "1. Interoperabilidad Técnica\n2. Interoperabilidad Semántica\n3. Interoperabilidad Organizativa",
                "explicacion": "Artículo 6 del Real Decreto 4/2010.",
                "dificultad": "facil", "fuente": "BOE Real Decreto 4/2010, Art. 6"
            },
            {
                "bloque": 4, "tema": 4, "tipo": "definicion",
                "pregunta": "¿Cuáles son las 5 dimensiones de seguridad según el Esquema Nacional de Seguridad (ENS RD 311/2022)?",
                "respuesta": "1. Disponibilidad (D)\n2. Integridad (I)\n3. Confidencialidad (C)\n4. Autenticidad (A)\n5. Trazabilidad (T)",
                "explicacion": "Regulado en el Anexo I del Real Decreto 311/2022.",
                "dificultad": "facil", "fuente": "BOE Real Decreto 311/2022 (ENS)"
            },
            {
                "bloque": 4, "tema": 4, "tipo": "definicion",
                "pregunta": "¿Cuáles son las tres categorías de seguridad en las que se clasifican los sistemas según el RD 311/2022 (ENS)?",
                "respuesta": "Categoría Básica, Categoría Media y Categoría Alta.",
                "explicacion": "Determinadas según el impacto más desfavorable entre todas las dimensiones de seguridad evaluadas.",
                "dificultad": "facil", "fuente": "BOE Real Decreto 311/2022, Art. 24"
            },
            {
                "bloque": 4, "tema": 6, "tipo": "comparativa",
                "pregunta": "¿Cuál es la diferencia básica entre el cifrado simétrico (AES) y el cifrado asimétrico (RSA)?",
                "respuesta": "El cifrado simétrico utiliza la misma clave secreta tanto para cifrar como para descifrar; el cifrado asimétrico utiliza un par de claves matemáticamente vinculadas: una clave pública para cifrar y una clave privada para descifrar.",
                "explicacion": "El simétrico es mucho más rápido y eficiente para grandes volúmenes de datos; el asimétrico soluciona la distribución segura de claves.",
                "dificultad": "facil", "fuente": "Guías CCN-STIC / NIST"
            },
            {
                "bloque": 4, "tema": 7, "tipo": "comparativa",
                "pregunta": "¿Cuál es la diferencia fundamental entre una Máquina Virtual tradicional y un Contenedor Docker?",
                "respuesta": "Una máquina virtual emula el hardware completo y ejecuta su propio Sistema Operativo huésped sobre un hipervisor; un contenedor comparte el kernel del Sistema Operativo anfitrión aislando solo los procesos a nivel de usuario, siendo mucho más ligero y rápido.",
                "explicacion": "Los contenedores comparten recursos de forma más eficiente.",
                "dificultad": "media", "fuente": "Docker Documentation"
            },
            {
                "bloque": 4, "tema": 9, "tipo": "definicion",
                "pregunta": "¿Qué significan las métricas RTO y RPO en un Plan de Recuperación ante Desastres (DRP)?",
                "respuesta": "RTO (Recovery Time Objective): Tiempo máximo admisible que un servicio puede permanecer inactivo tras un fallo.\nRPO (Recovery Point Objective): Cantidad máxima admisible de pérdida de datos medida en tiempo (intervalo entre copias de seguridad).",
                "explicacion": "RTO mide tiempo de inactividad; RPO mide pérdida tolerable de datos.",
                "dificultad": "media", "fuente": "ISO 22301 / CCN-STIC"
            }
        ]

        total_tarjetas = 0
        for card in tarjetas_data:
            tema_obj = temas_map.get((card["bloque"], card["tema"]))
            if tema_obj:
                Tarjeta.objects.get_or_create(
                    tema=tema_obj,
                    pregunta=card["pregunta"],
                    defaults={
                        "tipo": card["tipo"],
                        "respuesta": card["respuesta"],
                        "explicacion": card["explicacion"],
                        "nivel_dificultad": card["dificultad"],
                        "fuente": card["fuente"],
                    }
                )
                total_tarjetas += 1

        self.stdout.write(self.style.SUCCESS(f"{total_tarjetas} Flashcards atómicas precargadas."))

        # 5. Exámenes Oficiales INAP
        examen_2024, _ = Examen.objects.get_or_create(
            año=2024,
            convocatoria="libre",
            defaults={
                "tipo": "Primer Ejercicio OEP 2023/2024 TAI",
                "organismo": "INAP / Comisión Permanente de Selección",
                "url_oficial": "https://sede.inap.gob.es",
                "descripcion": "Cuestionario oficial de 100 preguntas + 5 de reserva."
            }
        )

        preguntas_inap = [
            {
                "numero": 1, "bloque": 1, "tema": 4,
                "pregunta": "De acuerdo con la Ley 39/2015, ¿cuál de los siguientes NO es considerado un medio de notificación electrónica válido?",
                "a": "Dirección electrónica habilitada única (DEHú).",
                "b": "Comparecencia en la sede electrónica de la Administración u Organismo actuante.",
                "c": "Envío de mensaje SMS sin confirmación ni certificado de entrega en sede.",
                "d": "Puesta a disposición del interesado en la sede electrónica con acreditación de la fecha y hora de acceso.",
                "correcta": "C",
                "explicacion": "El SMS sólo actúa como aviso accesorio; no constituye por sí mismo la notificación válida regulada en el artículo 41 y 43 de la Ley 39/2015."
            },
            {
                "numero": 2, "bloque": 2, "tema": 7,
                "pregunta": "En el modelo de referencia OSI, ¿en qué nivel o capa opera el protocolo ICMP (Internet Control Message Protocol)?",
                "a": "Capa 2 - Enlace de Datos.",
                "b": "Capa 3 - Red.",
                "c": "Capa 4 - Transporte.",
                "d": "Capa 7 - Aplicación.",
                "correcta": "B",
                "explicacion": "ICMP es un protocolo de soporte en la capa de red (Capa 3 OSI / Capa de Internet TCP/IP), utilizado para diagnósticos de conectividad (ej: ping) y control de errores."
            },
            {
                "numero": 3, "bloque": 3, "tema": 5,
                "pregunta": "En el modelo relacional, ¿qué forma normal exige que una tabla esté en 2FN y que ningún atributo no clave dependa transitivamente de la clave primaria?",
                "a": "Primera Forma Normal (1FN).",
                "b": "Tercera Forma Normal (3FN).",
                "c": "Forma Normal de Boyce-Codd (BCNF).",
                "d": "Cuarta Forma Normal (4FN).",
                "correcta": "B",
                "explicacion": "La 3FN elimina las dependencias transitivas entre atributos no clave respecto a la clave primaria."
            },
            {
                "numero": 4, "bloque": 4, "tema": 4,
                "pregunta": "Según el Real Decreto 311/2022 (ENS), ¿cuáles son las tres categorías de seguridad en las que se clasifican los sistemas de información?",
                "a": "Nivel 1, Nivel 2 y Nivel 3.",
                "b": "Básica, Media y Alta.",
                "c": "Restringida, Confidencial y Secreta.",
                "d": "Inicial, Definida y Optimizada.",
                "correcta": "B",
                "explicacion": "El Artículo 24 y Anexo I del RD 311/2022 establece las categorías Básica, Media y Alta según el impacto que causaría un incidente de seguridad."
            },
            {
                "numero": 5, "bloque": 4, "tema": 3,
                "pregunta": "El Real Decreto 4/2010 por el que se regula el Esquema Nacional de Interoperabilidad (ENI) establece que los documentos electrónicos deben incluir:",
                "a": "Únicamente el archivo en formato ejecutable.",
                "b": "Contenido, metadatos mínimos obligatorios y firma electrónica o sello de órgano.",
                "c": "Sólo la marca temporal del prestador de confianza.",
                "d": "Exclusivamente formato PDF/A sin metadatos.",
                "correcta": "B",
                "explicacion": "Según el artículo 14 del ENI y la Norma Técnica de Interoperabilidad (NTI) de Documento Electrónico, un documento electrónico consta de contenido, metadatos mínimos y firma electrónica."
            },
            {
                "numero": 6, "bloque": 1, "tema": 1,
                "pregunta": "Según el artículo 68 de la Constitución Española, el Congreso de los Diputados se compone de un mínimo y un máximo de:",
                "a": "250 y 350 Diputados.",
                "b": "300 y 400 Diputados.",
                "c": "350 y 450 Diputados.",
                "d": "300 y 500 Diputados.",
                "correcta": "B",
                "explicacion": "Artículo 68.1 de la Constitución: El Congreso se compone de un mínimo de 300 y un máximo de 400 Diputados (la LOREG fijó actualmente el número en 350)."
            },
            {
                "numero": 7, "bloque": 2, "tema": 7,
                "pregunta": "¿Cuál de los siguientes rangos de direcciones IPv4 pertenece al bloque de direcciones privadas de Clase B según la RFC 1918?",
                "a": "10.0.0.0 a 10.255.255.255",
                "b": "172.16.0.0 a 172.31.255.255",
                "c": "192.168.0.0 a 192.168.255.255",
                "d": "169.254.0.0 a 169.254.255.255",
                "correcta": "B",
                "explicacion": "RFC 1918: Clase A (10.0.0.0/8), Clase B (172.16.0.0/12, es decir 172.16.0.0 a 172.31.255.255), Clase C (192.168.0.0/16)."
            },
            {
                "numero": 8, "bloque": 3, "tema": 1,
                "pregunta": "En la metodología MÉTRICA Versión 3, ¿en qué proceso se define el catálogo de requisitos del sistema y se elabora el modelo de casos de uso?",
                "a": "PSI (Planificación de Sistemas de Información).",
                "b": "EVS (Estudio de Viabilidad del Sistema).",
                "c": "ASI (Análisis del Sistema de Información dentro de DSI).",
                "d": "IAS (Implantación y Aceptación del Sistema).",
                "correcta": "C",
                "explicacion": "En el proceso ASI (Análisis del Sistema de Información) de MÉTRICA v3 se obtienen los requisitos y se modelan los casos de uso."
            }
        ]

        for p_data in preguntas_inap:
            tema_obj = temas_map.get((p_data["bloque"], p_data["tema"]))
            PreguntaExamen.objects.update_or_create(
                examen=examen_2024,
                numero=p_data["numero"],
                defaults={
                    "pregunta": p_data["pregunta"],
                    "opcion_a": p_data["a"],
                    "opcion_b": p_data["b"],
                    "opcion_c": p_data["c"],
                    "opcion_d": p_data["d"],
                    "opcion_correcta": p_data["correcta"],
                    "tema": tema_obj,
                    "explicacion_oficial": p_data["explicacion"],
                }
            )

        self.stdout.write(self.style.SUCCESS("¡Semillado del temario completo (36 temas) y banco de preguntas INAP finalizado!"))
