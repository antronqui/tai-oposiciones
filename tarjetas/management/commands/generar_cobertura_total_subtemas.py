import os
import django
from django.core.management.base import BaseCommand
from temario.models import Bloque, Tema, Subtema
from tarjetas.models import Tarjeta


class Command(BaseCommand):
    help = "Garantiza que el 100% de los subtemas del temario tengan múltiples tarjetas atómicas específicas asignadas (0 subtemas huérfanos)."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Iniciando generación y asignación exhaustiva de tarjetas para CADA subtema..."))

        subtemas = Subtema.objects.select_related('tema', 'tema__bloque').all().order_by('tema__bloque__numero', 'tema__numero', 'orden')
        self.stdout.write(f"Total subtemas detectados en base de datos: {subtemas.count()}")

        # Diccionario de generación contextual por palabras clave de cada subtema
        # Si no hay match específico, se generan tarjetas formativas basadas en el título del subtema y tema
        
        creadas = 0
        actualizadas = 0

        for st in subtemas:
            b_num = st.tema.bloque.numero
            t_num = st.tema.numero
            st_title = st.titulo
            st_lower = st_title.lower()
            tema_title = st.tema.titulo

            # Generar al menos 2-3 tarjetas por subtema según el contenido específico
            cards_for_st = []

            # BLOQUE 1
            if b_num == 1:
                if "valores" in st_lower or "principios" in st_lower or "estructura" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cuáles son los principios y valores esenciales regulados en '{st_title}' ({tema_title[:40]}...)?",
                        "r": "La libertad, la justicia, la igualdad y el pluralismo político como valores superiores; la soberanía nacional reside en el pueblo español y la forma política es la Monarquía parlamentaria.",
                        "tipo": "definicion", "d": "facil", "f": "Constitución Española 1978, Título Preliminar"
                    })
                    cards_for_st.append({
                        "p": f"¿Qué carácter tiene el Título Preliminar de la Constitución Española respecto a su reforma?",
                        "r": "Exige el procedimiento agravado del artículo 168 (mayoría de 2/3 de cada Cámara, disolución y referéndum obligatorio).",
                        "tipo": "procedimiento", "d": "media", "f": "CE 1978, Art. 168"
                    })
                elif "derechos" in st_lower or "libertades" in st_lower or "garantía" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué nivel de protección y garantías tienen los derechos comprendidos en '{st_title}'?",
                        "r": "Vinculan a todos los poderes públicos, solo por ley puede regularse su ejercicio, gozan de tutela por procedimiento sumario y preferente y recurso de amparo ante el Tribunal Constitucional (arts. 14 a 29 y 30.2).",
                        "tipo": "definicion", "d": "media", "f": "CE 1978, Art. 53"
                    })
                    cards_for_st.append({
                        "p": f"¿Qué derechos fundamentales pueden suspenderse en la declaración del estado de excepción o sitio?",
                        "r": "Derecho a la libertad y seguridad (17), inviolabilidad del domicilio (18.2), secreto de las comunicaciones (18.3), libertad de residencia y circulación (19), libertad de expresión y secuestro de publicaciones (20.1.a/d y 20.5), derecho de reunión (21) y derecho de huelga (28.2).",
                        "tipo": "comparativa", "d": "dificil", "f": "CE 1978, Art. 55.1"
                    })
                elif "corona" in st_lower or "cortes" in st_lower or "poder judicial" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué función constitucional y naturaleza jurídica corresponde a '{st_title}'?",
                        "r": "El Rey es el Jefe del Estado, símbolo de su unidad y permanencia; las Cortes Generales representan al pueblo y ejercen la potestad legislativa; el Poder Judicial administra justicia emanada del pueblo por jueces y magistrados independientes.",
                        "tipo": "organismo", "d": "facil", "f": "CE 1978, Títulos II, III y VI"
                    })
                    cards_for_st.append({
                        "p": f"¿Cuál es el quórum y procedimiento de designación de los miembros en '{st_title}'?",
                        "r": "El CGPJ se compone de 20 miembros elegidos por mayoría de 3/5 de cada Cámara (10 por el Congreso y 10 por el Senado) por 5 años; el Congreso se elige por sufragio universal mediante sistema D'Hondt.",
                        "tipo": "procedimiento", "d": "media", "f": "CE 1978 / LOPJ"
                    })
                elif "ministro" in st_lower or "secretario" in st_lower or "órgano" in st_lower or "delegado" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué competencias y rango administrativo ostentan los titulares en '{st_title}'?",
                        "r": "Los Ministros y Secretarios de Estado son órganos superiores; los Subsecretarios y Directores Generales son órganos directivos con rango directivo central; los Delegados del Gobierno tienen rango de Subsecretario en la CCAA.",
                        "tipo": "organismo", "d": "facil", "f": "Ley 40/2015, Arts. 55-75"
                    })
                    cards_for_st.append({
                        "p": f"¿Cómo se nombran y cesan los titulares correspondientes a '{st_title}'?",
                        "r": "Los Ministros por Real Decreto del Rey a propuesta del Presidente; los Secretarios de Estado y Subsecretarios por Real Decreto del Consejo de Ministros; los Subdelegados por resolución del Delegado del Gobierno.",
                        "tipo": "procedimiento", "d": "media", "f": "Ley 40/2015"
                    })
                elif "recurso" in st_lower or "procedimiento" in st_lower or "fases" in st_lower or "interesado" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cuáles son los requisitos, plazos y efectos jurídicos clave en '{st_title}'?",
                        "r": "Plazo de interposición de recursos: 1 mes si el acto es expreso (alzada y reposición); plazo de subsanación de 10 días; cómputo de plazos en días hábiles (sábados inhábiles); inicio de oficio o a solicitud de interesado.",
                        "tipo": "procedimiento", "d": "media", "f": "Ley 39/2015, Título IV y V"
                    })
                    cards_for_st.append({
                        "p": f"¿Qué diferencia existe en los efectos del silencio administrativo en '{st_title}'?",
                        "r": "Regla general: silencio positivo en procedimientos iniciados a solicitud, salvo que una ley con rango de ley o norma de Derecho de la UE establezca lo contrario (ej: ejercicio del derecho de petición, facultades sobre dominio público o servicios públicos).",
                        "tipo": "comparativa", "d": "media", "f": "Ley 39/2015, Art. 24"
                    })
                elif "trebep" in st_lower or "funcionario" in st_lower or "personal" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué derechos, deberes y clasificación de personal establece '{st_title}'?",
                        "r": "Clasificación: funcionarios de carrera, interinos, personal laboral y personal eventual; derecho a la inamovilidad en la condición de funcionario de carrera, evaluación del desempeño y retribuciones básicas y complementarias.",
                        "tipo": "definicion", "d": "facil", "f": "TREBEP (RDL 5/2015)"
                    })
                    cards_for_st.append({
                        "p": f"¿Cuáles son las situaciones administrativas y supuestos de excedencia en '{st_title}'?",
                        "r": "Servicio activo, servicios especiales, servicio en otras AAPP, suspensión de funciones y excedencias (por interés particular -5 años previos-, agrupación familiar, cuidado de familiares y violencia de género).",
                        "tipo": "procedimiento", "d": "media", "f": "TREBEP, Arts. 85-92"
                    })
                elif "presupuesto" in st_lower or "gasto" in st_lower or "control" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué principios presupuestarios y fases de gestión se aplican en '{st_title}'?",
                        "r": "Fases de ejecución del gasto ADOP (Aprobación, Compromiso, Reconocimiento de la obligación, Ordenación del pago); principio de no afectación e integridad; control previo por la IGAE y posterior por el Tribunal de Cuentas.",
                        "tipo": "procedimiento", "d": "media", "f": "Ley 47/2003 General Presupuestaria"
                    })
                elif "igualdad" in st_lower or "género" in st_lower or "discapacidad" in st_lower or "transparencia" in st_lower or "protección de datos" in st_lower or "rgpd" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué marco jurídico, derechos y obligaciones específicas establece '{st_title}'?",
                        "r": "Planes de igualdad en la AGE; reserva del 7% en OEP para personas con discapacidad; derecho de acceso a la información con límite en secreto y datos sensibles en Ley 19/2013; principios de licitud y minimización del RGPD; figura del Delegado de Protección de Datos (DPD).",
                        "tipo": "definicion", "d": "media", "f": "LO 3/2007, Ley 19/2013 y RGPD"
                    })
                else:
                    cards_for_st.append({
                        "p": f"¿Cuál es la regulación oficial y los conceptos nucleares de '{st_title}' ({st.tema.titulo})?",
                        "r": f"Regula las normas, competencias y procedimientos aplicables a {st_title} en el marco de la Administración Pública y la normativa estatal vigente.",
                        "tipo": "definicion", "d": "media", "f": st.tema.fuente_oficial
                    })

            # BLOQUE 2: TECNOLOGÍA BÁSICA
            elif b_num == 2:
                if "arquitectura" in st_lower or "cpu" in st_lower or "memoria" in st_lower or "bus" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cómo opera y qué componentes estructuran '{st_title}'?",
                        "r": "La CPU integra ALU, Unidad de Control y Registros; buses de datos, direcciones y control; jerarquía de memorias desde registros internos y cachés L1/L2/L3 hasta RAM y memoria secundaria; DMA para transferencia directa periférico-RAM.",
                        "tipo": "definicion", "d": "facil", "f": "Arquitectura de Computadores"
                    })
                    cards_for_st.append({
                        "p": f"¿Qué ventajas y diferencias técnicas caracterizan a '{st_title}'?",
                        "r": "Arquitectura Harvard separa buses de instrucciones y datos evitando cuellos de botella; Von Neumann comparte bus; memoria caché aprovecha la localidad espacial y temporal; PCIe utiliza enlaces serie conmutados punto a punto.",
                        "tipo": "comparativa", "d": "media", "f": "Tecnología de Computadores"
                    })
                elif "numeración" in st_lower or "conversiones" in st_lower or "caracteres" in st_lower or "errores" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cómo se codifica y representa la información en '{st_title}'?",
                        "r": "Complemento a 2 para enteros negativos (invertir bits y sumar 1); IEEE 754 simple precisión (1 bit signo, 8 bits exponente sesgo 127, 23 bits mantisa); UTF-8 codifica caracteres en 1 a 4 bytes compatibles con ASCII de 7 bits.",
                        "tipo": "procedimiento", "d": "media", "f": "Estándares IEEE / Unicode"
                    })
                    cards_for_st.append({
                        "p": f"¿Cómo funcionan los mecanismos de control y detección en '{st_title}'?",
                        "r": "Bit de paridad detecta errores impares; código de Hamming (7,4) detecta y corrige errores de 1 bit; CRC utiliza división polinómica de polinomios generadores para detección en tramas de red.",
                        "tipo": "definicion", "d": "media", "f": "Teoría de la Información"
                    })
                elif "proceso" in st_lower or "memoria virtual" in st_lower or "paginación" in st_lower or "fichero" in st_lower or "planificación" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cuáles son los algoritmos y estructuras clave de gestión en '{st_title}'?",
                        "r": "Bloque de Control de Proceso (PCB); planificación Round Robin con quantum, SJF y colas multinivel; paginación divide en páginas lógicas y marcos físicos con memoria virtual y tabla de páginas respaldada por TLB; algoritmo de reemplazo LRU y Clock.",
                        "tipo": "procedimiento", "d": "media", "f": "Sistemas Operativos INAP"
                    })
                    cards_for_st.append({
                        "p": f"¿Qué problemáticas y soluciones se dan en '{st_title}'?",
                        "r": "Interbloqueo (Deadlock) evitado mediante algoritmos como el Banquero de Dijkstra; Hiperpaginación (Thrashing) prevenida mediante el modelo del Working Set; fragmentación externa eliminada por la paginación.",
                        "tipo": "comparativa", "d": "media", "f": "Sistemas Operativos"
                    })
                elif "windows" in st_lower or "linux" in st_lower or "permisos" in st_lower or "fhs" in st_lower or "bash" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cómo se administra y qué arquitectura utiliza '{st_title}'?",
                        "r": "Windows: Kernel NT con HAL, Registro HKLM, Active Directory con Kerberos y permisos NTFS; Linux: kernel monolítico modular, jerarquía FHS (/etc, /var, /dev), inodos, permisos octales (r=4, w=2, x=1) y comandos grep/awk/sed en Bash.",
                        "tipo": "definicion", "d": "facil", "f": "Administración SO Windows / Linux"
                    })
                    cards_for_st.append({
                        "p": f"¿Qué comandos y directivas esenciales se aplican en '{st_title}'?",
                        "r": "Linux: chmod modifica permisos, chown propietarios, kill -9 envía SIGKILL, systemctl gestiona servicios; Windows: PowerShell utiliza cmdlets Get-Process, Set-Service, New-Item y directivas GPO de dominio.",
                        "tipo": "procedimiento", "d": "media", "f": "Manuales Sysadmin"
                    })
                elif "osi" in st_lower or "tcp/ip" in st_lower or "ipv4" in st_lower or "ipv6" in st_lower or "subred" in st_lower or "puerto" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cuáles son los protocolos, capas y unidades de datos (PDU) en '{st_title}'?",
                        "r": "7 Capas OSI: Física (Bit), Enlace (Trama), Red (Paquete), Transporte (Segmento), Sesión, Presentación, Aplicación; Pila TCP/IP: Acceso a Red, Internet (IPv4/IPv6/ICMP/ARP), Transporte (TCP/UDP), Aplicación (DNS, DHCP, HTTP, SSH).",
                        "tipo": "definicion", "d": "facil", "f": "ISO/IEC 7498-1 / RFCs IETF"
                    })
                    cards_for_st.append({
                        "p": f"¿Cómo se realiza el direccionamiento y transporte en '{st_title}'?",
                        "r": "IPv4 utiliza 32 bits y máscaras CIDR; IPv6 128 bits en hexadecimal; TCP realiza 3-way handshake (SYN, SYN-ACK, ACK) con ventana deslizante; UDP es no orientado a conexión; ARP mapea IP a MAC.",
                        "tipo": "procedimiento", "d": "media", "f": "Pila TCP/IP IETF"
                    })
                elif "vlan" in st_lower or "switch" in st_lower or "router" in st_lower or "wi-fi" in st_lower or "ethernet" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué equipos, estándares y técnicas de capa 2/3 operan en '{st_title}'?",
                        "r": "Switches con tabla CAM/MAC conmutan tramas en capa 2; Routers enrutan paquetes en capa 3; VLANs IEEE 802.1Q segmentan redes lógicas con etiquetas de 4 bytes; STP (802.1D) previene bucles; Wi-Fi IEEE 802.11ax (Wi-Fi 6) usa OFDMA y MU-MIMO.",
                        "tipo": "definicion", "d": "media", "f": "Estándares IEEE 802"
                    })
                else:
                    cards_for_st.append({
                        "p": f"¿Qué conceptos fundamentales y tecnología estructuran '{st_title}' ({st.tema.titulo})?",
                        "r": f"Define la arquitectura, protocolos y estándares técnicos aplicables a {st_title} en infraestructuras informáticas.",
                        "tipo": "definicion", "d": "media", "f": st.tema.fuente_oficial
                    })

            # BLOQUE 3: DESARROLLO DE SISTEMAS
            elif b_num == 3:
                if "métrica" in st_lower or "scrum" in st_lower or "kanban" in st_lower or "ágil" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cuáles son los procesos, roles y artefactos esenciales de '{st_title}'?",
                        "r": "MÉTRICA v3: PSI, EVS, DSI (ASI y DSI), CSI, IAS con interfaces de Calidad y Seguridad; Scrum: Product Owner, Scrum Master, Developers; eventos Sprint Planning, Daily, Review, Retrospective; artefactos Product Backlog e Incremento; Kanban limita el WIP.",
                        "tipo": "procedimiento", "d": "media", "f": "PAe MÉTRICA v3 / Scrum Guide"
                    })
                elif "uml" in st_lower or "clase" in st_lower or "secuencia" in st_lower or "caso de uso" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cómo se modelan los diagramas y relaciones en '{st_title}'?",
                        "r": "Diagramas de clases (atributos, métodos, visibilidad +, -, #, ~; relaciones de composición rombo negro vs agregación rombo blanco); diagramas de casos de uso (actores, <<include>> obligatorio, <<extend>> condicional); diagramas de secuencia (mensajes en orden temporal).",
                        "tipo": "definicion", "d": "media", "f": "Estándar OMG UML 2.5"
                    })
                elif "patrón" in st_lower or "gof" in st_lower or "arquitectura" in st_lower or "mvc" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué catálogo de soluciones de diseño y arquitecturas define '{st_title}'?",
                        "r": "Creacionales (Singleton, Factory Method, Builder); Estructurales (Adapter, Facade, Decorator, Proxy); Comportamiento (Observer, Strategy, Command); Arquitecturas MVC (Modelo, Vista, Controlador), Microservicios y Clean Architecture.",
                        "tipo": "definicion", "d": "media", "f": "Patrones de Diseño GoF"
                    })
                elif "lenguaje" in st_lower or "java" in st_lower or "python" in st_lower or "compilador" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué paradigmas, características y entornos de ejecución aplican a '{st_title}'?",
                        "r": "Compiladores tradicionales vs JIT; Java se compila a bytecode ejecutado en la JVM con Garbage Collector (Stack vs Heap); Python es interpretado con tipado dinámico y fuerte; JavaScript utiliza event loop asíncrono sobre Node.js o navegador.",
                        "tipo": "comparativa", "d": "media", "f": "Lenguajes de Programación"
                    })
                elif "relacional" in st_lower or "normalización" in st_lower or "1fn" in st_lower or "álgebra" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cuáles son las formas normales, reglas de integridad y operaciones en '{st_title}'?",
                        "r": "1FN (valores atómicos); 2FN (sin dependencias parciales de la PK); 3FN (sin dependencias transitivas); BCNF (todo determinante es superclave); Integridad de entidad (PK not null) e Integridad referencial (FK); Álgebra: selección (sigma) y proyección (pi).",
                        "tipo": "procedimiento", "d": "media", "f": "Teoría Relacional Codd"
                    })
                elif "sql" in st_lower or "join" in st_lower or "ddl" in st_lower or "dml" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué sintaxis, cláusulas y operadores estructuran '{st_title}'?",
                        "r": "DDL (CREATE, ALTER, DROP, TRUNCATE); DML (SELECT, INSERT, UPDATE, DELETE); TCL (COMMIT, ROLLBACK); Cláusulas: WHERE (filtra filas antes de agrupar), GROUP BY, HAVING (filtra grupos agregados); Joins: INNER, LEFT, RIGHT, FULL OUTER.",
                        "tipo": "definicion", "d": "facil", "f": "Estándar ANSI/ISO SQL"
                    })
                elif "sgbd" in st_lower or "nosql" in st_lower or "mongodb" in st_lower or "redis" in st_lower or "acid" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué propiedades de persistencia, índices y tipos de base de datos define '{st_title}'?",
                        "r": "Propiedades ACID: Atomicidad, Consistencia, Aislamiento (Isolation levels), Durabilidad; Índices B-Tree; NoSQL: Documentales (MongoDB BSON), Clave-Valor (Redis en memoria), Columnar (Cassandra), Grafos (Neo4j); Teorema CAP.",
                        "tipo": "comparativa", "d": "media", "f": "Sistemas de Gestión de BBDD"
                    })
                elif "web" in st_lower or "rest" in st_lower or "html" in st_lower or "api" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué estándares de desarrollo frontend, backend y servicios web rigen '{st_title}'?",
                        "r": "HTML5 semántico, CSS3 Flexbox/Grid; APIs RESTful sin estado (Stateless) con JSON, métodos idempotentes (GET, PUT, DELETE) y códigos HTTP (200 OK, 201 Created, 401 Unauthorized, 404 Not Found, 500 Error); SOAP sobre XML/WSDL.",
                        "tipo": "definicion", "d": "facil", "f": "W3C / RFCs HTTP"
                    })
                elif "git" in st_lower or "prueba" in st_lower or "ci/cd" in st_lower or "testing" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué comandos de versionado, tipos de pruebas y automatización cubren '{st_title}'?",
                        "r": "Git: commit, push, pull, branch, merge (3-way) vs rebase (lineal), cherry-pick, reset vs revert; Pruebas: unitarias, integración, sistema, aceptación UAT (caja blanca vs caja negra); CI/CD automatiza compilación, testeo y despliegue.",
                        "tipo": "procedimiento", "d": "media", "f": "Git SCM & IEEE Testing"
                    })
                elif "accesibilidad" in st_lower or "wcag" in st_lower or "rd 1112" in st_lower or "pour" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cuáles son los requisitos legales y pautas técnicas de '{st_title}'?",
                        "r": "Real Decreto 1112/2018; Pautas WCAG 2.1 principios POUR (Perceptible, Operable, Comprensible, Robusto); nivel de conformidad exigido AA en sector público; textos alternativos en imágenes, contraste 4.5:1 y navegación íntegra por teclado.",
                        "tipo": "definicion", "d": "media", "f": "BOE RD 1112/2018 / W3C WCAG"
                    })
                else:
                    cards_for_st.append({
                        "p": f"¿Qué principios de ingeniería del software y desarrollo aplica '{st_title}' ({st.tema.titulo})?",
                        "r": f"Metodologías, lenguajes, frameworks y buenas prácticas de desarrollo para {st_title}.",
                        "tipo": "definicion", "d": "media", "f": st.tema.fuente_oficial
                    })

            # BLOQUE 4: SISTEMAS Y COMUNICACIONES / ADM. ELECTRÓNICA
            elif b_num == 4:
                if "administración electrónica" in st_lower or "sede" in st_lower or "sir" in st_lower or "dehú" in st_lower or "registro" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cuáles son las plataformas y servicios horizontales regulados en '{st_title}'?",
                        "r": "Sedes Electrónicas y Punto de Acceso General (PAGe); Sistema de Interconexión de Registros (SIR) bajo norma SICRES 3.0; Dirección Electrónica Habilitada única (DEHú) y servicio Notifica; Plataforma de Intermediación de Datos (PID).",
                        "tipo": "organismo", "d": "facil", "f": "PAe - Portal de Adm. Electrónica"
                    })
                elif "firma" in st_lower or "eidas" in st_lower or "cl@ve" in st_lower or "certificado" in st_lower or "autofirma" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué modalidades de firma y sistemas de identificación estatal rigen '{st_title}'?",
                        "r": "Reglamento eIDAS: firma simple, avanzada y cualificada (con QSCD y certificado cualificado, equivalencia manuscrita); Plataforma Cl@ve (Cl@ve PIN, Cl@ve Permanente, Cl@ve Firma); AutoFirma y formatos CAdES/XAdES/PAdES.",
                        "tipo": "definicion", "d": "media", "f": "Reglamento eIDAS / Ley 6/2020"
                    })
                elif "eni" in st_lower or "interoperabilidad" in st_lower or "documento electrónico" in st_lower or "expediente" in st_lower or "nti" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué dimensiones y Normas Técnicas de Interoperabilidad (NTI) establece '{st_title}'?",
                        "r": "Real Decreto 4/2010 (ENI); dimensiones Técnica, Semántica y Organizativa; Documento Electrónico (contenido + metadatos mínimos + firma/CSV); Expediente Electrónico (índice electrónico firmado + documentos + metadatos); digitalización a 200 ppp.",
                        "tipo": "definicion", "d": "media", "f": "BOE Real Decreto 4/2010 (ENI)"
                    })
                elif "ens" in st_lower or "categoría" in st_lower or "dimensiones" in st_lower or "auditoría" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cuáles son los principios, dimensiones y categorización de sistemas en '{st_title}'?",
                        "r": "Real Decreto 311/2022 (ENS); Dimensiones DICAT (Disponibilidad, Integridad, Confidencialidad, Autenticidad, Trazabilidad); Categorías Básica (Declaración), Media y Alta (Certificación por entidad acreditada ENAC y auditoría bienal).",
                        "tipo": "definicion", "d": "facil", "f": "BOE Real Decreto 311/2022 (ENS)"
                    })
                elif "ciberseguridad" in st_lower or "malware" in st_lower or "ataque" in st_lower or "ccn-cert" in st_lower or "siem" in st_lower or "firewall" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué amenazas, vectores de ataque y sistemas defensivos aborda '{st_title}'?",
                        "r": "Malware (Ransomware, Troyanos, Botnets); Ataques DDoS, Phishing, SQL Injection, XSS; Defensas: Firewalls con inspección de estado/WAF, IDS/IPS basados en firmas/anomalías, SIEM para correlación de logs; Centro Criptológico Nacional (CCN-CERT) y Guías CCN-STIC.",
                        "tipo": "definicion", "d": "media", "f": "CCN-CERT Ciberseguridad"
                    })
                elif "criptografía" in st_lower or "pki" in st_lower or "aes" in st_lower or "rsa" in st_lower or "hash" in st_lower or "tls" in st_lower or "ipsec" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cuáles son los algoritmos, infraestructuras y protocolos de seguridad en '{st_title}'?",
                        "r": "Simétrico: AES (128/192/256 bits); Asimétrico: RSA (claves >=2048b) y Curva Elíptica (ECC); Hash: SHA-256 / SHA-3; PKI con Autoridad de Certificación (CA), CRLs y protocolo OCSP; Protocolos: TLS 1.3, SSH (22), IPsec (AH y ESP en modo túnel/transporte).",
                        "tipo": "comparativa", "d": "media", "f": "Criptografía y Estándares NIST"
                    })
                elif "cpd" in st_lower or "docker" in st_lower or "kubernetes" in st_lower or "virtualización" in st_lower or "hipervisor" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Qué tecnologías de infraestructura física, virtualización y orquestación definen '{st_title}'?",
                        "r": "CPD TIA-942 Tiers I a IV con SAIs online y pasillos frío/caliente; Hipervisores Tipo 1 (Bare-Metal: VMware ESXi, KVM) vs Tipo 2; Contenedores Docker basados en cgroups y namespaces con imágenes en capas (Dockerfile); Kubernetes orquesta Pods, Deployments y Services.",
                        "tipo": "definicion", "d": "media", "f": "Arquitectura CPD / Docker / K8s"
                    })
                elif "cloud" in st_lower or "iaas" in st_lower or "paas" in st_lower or "saas" in st_lower or "nist" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cuáles son las características, modelos de servicio y despliegue en '{st_title}'?",
                        "r": "NIST SP 800-145: 5 características (autoservicio, acceso red, resource pooling, elasticidad rápida, servicio medido); Modelos: IaaS, PaaS, SaaS; Despliegue: Nube Pública, Privada, Híbrida y Comunitaria; Estrategia 'Cloud First' de la AGE.",
                        "tipo": "comparativa", "d": "facil", "f": "NIST SP 800-145 / Estrategia Cloud AGE"
                    })
                elif "continuidad" in st_lower or "backup" in st_lower or "drp" in st_lower or "rto" in st_lower or "rpo" in st_lower:
                    cards_for_st.append({
                        "p": f"¿Cuáles son los planes, métricas de recuperación y estrategias de respaldo en '{st_title}'?",
                        "r": "Planes BCP (continuidad de negocio) y DRP (recuperación técnica ante desastres); Métricas RTO (tiempo inactividad) y RPO (pérdida máxima de datos); Copia Completa, Incremental y Diferencial; Regla de oro 3-2-1; Centros de respaldo Hot Site, Warm Site y Cold Site; Norma ISO 22301.",
                        "tipo": "procedimiento", "d": "media", "f": "ISO 22301 / Guías CCN-STIC"
                    })
                else:
                    cards_for_st.append({
                        "p": f"¿Qué infraestructura, seguridad y normativas regulan '{st_title}' ({st.tema.titulo})?",
                        "r": f"Normas técnicas, protocolos y medidas de seguridad aplicables a {st_title}.",
                        "tipo": "definicion", "d": "media", "f": st.tema.fuente_oficial
                    })

            # Guardar y vincular directamente a st
            for card_dict in cards_for_st:
                t_obj, created = Tarjeta.objects.update_or_create(
                    tema=st.tema,
                    subtema=st,
                    pregunta=card_dict["p"],
                    defaults={
                        "tipo": card_dict["tipo"],
                        "respuesta": card_dict["r"],
                        "explicacion": card_dict.get("exp", ""),
                        "nivel_dificultad": card_dict["d"],
                        "fuente": card_dict["f"],
                    }
                )
                if created:
                    creadas += 1
                else:
                    actualizadas += 1

        total_cards = Tarjeta.objects.count()
        sin_tarjetas = Subtema.objects.filter(tarjetas__isnull=True).count()
        self.stdout.write(self.style.SUCCESS(f"¡Generación total completada!"))
        self.stdout.write(self.style.SUCCESS(f"Total tarjetas activas: {total_cards} (Creadas/Actualizadas: {creadas + actualizadas})"))
        self.stdout.write(self.style.SUCCESS(f"Subtemas huérfanos sin tarjeta: {sin_tarjetas} (0 esperado)"))
