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
# TEMA 1: Administracion Electronica en la AGE
# ============================================================
t1 = """1. CONCEPTO Y MARCO NORMATIVO

La Administracion Electronica en la Administracion General del Estado (AGE) se regula principalmente por la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Comun de las Administraciones Publicas (LPACAP), y la Ley 40/2015, de 1 de octubre, de Regimen Juridico del Sector Publico (LRJSP). Ambas leyes establecen la obligacion de relacionarse electronicamente con la Administracion para personas juridicas, entidades sin personalidad juridica, profesionales colegiados y empleados publicos, entre otros.

El Esquema Nacional de Seguridad (ENS, RD 311/2022) y el Esquema Nacional de Interoperabilidad (ENI, RD 4/2010) complementan este marco, estableciendo los requisitos tecnicos y de seguridad que deben cumplir los sistemas de informacion que soportan la administracion electronica.

DATO CLAVE: La Ley 39/2015 regula el procedimiento administrativo; la Ley 40/2015 regula el regimen juridico del sector publico. Ambas entraron en vigor el 2 de octubre de 2016.

2. SEDE ELECTRONICA Y PUNTO DE ACCESO GENERAL ELECTRONICO (PAGe)

La Sede Electronica es la direccion electronica disponible para los ciudadanos a traves de redes de telecomunicaciones, cuya titularidad, gestion y administracion corresponde a una Administracion Publica. La sede electronica debe garantizar la identificacion del organo titular, la seguridad de las comunicaciones y la disponibilidad del servicio.

Requisitos minimos de la sede electronica:
- Identificacion clara del titular y del organo responsable
- Informacion sobre los servicios disponibles
- Acceso al registro electronico
- Carta de servicios electronicos
- Sistema de verificacion de certificados de la sede
- Fecha y hora oficial

El Punto de Acceso General electronico (PAGe) es el portal administracion.gob.es, que actua como puerta de entrada unica a los servicios electronicos de la AGE. Permite a los ciudadanos acceder a tramites, informacion y servicios de multiples organismos desde un unico punto.

DATO CLAVE: El PAGe es administracion.gob.es. La sede electronica debe contar con certificado de sede (no de servidor) emitido por prestador de confianza.

3. DIMENSIONES DE SEGURIDAD EN LOS SISTEMAS DE INFORMACION

El ENS establece cinco dimensiones de seguridad que deben evaluarse para categorizar los sistemas de informacion:

- D (Disponibilidad): capacidad de los usuarios autorizados para acceder a la informacion y sistemas cuando lo necesiten.
- I (Integridad): propiedad por la que la informacion no ha sido alterada de manera no autorizada.
- C (Confidencialidad): la informacion no esta disponible ni es revelada a individuos, entidades o procesos no autorizados.
- A (Autenticidad): propiedad de que una entidad es quien dice ser o que garantiza la fuente de la informacion.
- T (Trazabilidad): propiedad que permite registrar y rastrear las actuaciones realizadas sobre un activo de informacion.

DATO CLAVE: Las cinco dimensiones del ENS forman el acronimo DICAT: Disponibilidad, Integridad, Confidencialidad, Autenticidad y Trazabilidad.

4. REGISTRO ELECTRONICO GENERAL (REG) Y SISTEMA DE INTERCONEXION DE REGISTROS (SIR)

El Registro Electronico General (REG) es el sistema mediante el cual los ciudadanos pueden presentar documentos y solicitudes ante la AGE en cualquier momento del dia, todos los dias del ano. Cada Administracion dispone de un registro electronico general, y cada organismo puede tener registros auxiliares interconectados con el principal.

Caracteristicas del REG:
- Disponible 24 horas al dia, 365 dias al ano
- Emite resguardo electronico con numero de registro, fecha y hora de presentacion
- El computo de plazos se inicia el primer dia habil siguiente a la presentacion en dia inhabil

El Sistema de Interconexion de Registros (SIR) permite el intercambio de asientos registrales entre las distintas Administraciones Publicas. Utiliza el estandar SICRES (Sistema de Informacion Comun de Registros de Entrada y Salida) en su version 3.0.

DATO CLAVE: El SIR utiliza el estandar SICRES 3.0 para el intercambio de asientos registrales entre administraciones.

5. CATEGORIAS DE LOS SISTEMAS (BASICA, MEDIA Y ALTA)

El ENS clasifica los sistemas de informacion en tres categorias segun el impacto que tendria un incidente de seguridad:

- Categoria BASICA: el perjuicio seria de escasa trascendencia. Ninguna dimension supera el nivel BAJO.
- Categoria MEDIA: el perjuicio seria de moderada importancia. Alguna dimension alcanza el nivel MEDIO pero ninguna supera el nivel ALTO.
- Categoria ALTA: el perjuicio seria de grave o muy grave importancia. Alguna dimension alcanza el nivel ALTO o MUY ALTO.

La categoria del sistema determina las medidas de seguridad aplicables del Anexo II del ENS.

DATO CLAVE: La categoria de un sistema se determina por la dimension con mayor nivel de valoracion. Si una sola dimension es ALTA, el sistema es de categoria ALTA.

6. NOTIFICACIONES ELECTRONICAS: DEHu Y NOTIFICA

La Direccion Electronica Habilitada Unica (DEHu) es el sistema de notificacion electronica de la AGE, gestionado por la Secretaria de Estado de Digitalizacion e Inteligencia Artificial (SEDIA). Sustituyo a la antigua DEH (Direccion Electronica Habilitada).

Caracteristicas de la DEHu:
- Accesible en dehunot.gob.es
- Permite a ciudadanos y empresas recibir notificaciones y comunicaciones de la AGE
- Integra las funciones de Notifica (plataforma de envio para las AAPP) y la DEH
- Las notificaciones caducan a los 10 dias sin acceder

La plataforma Notifica es el sistema que usan las Administraciones para enviar notificaciones electronicas. Integra varios canales: DEHu, correo postal hibrido, SMS y correo electronico de aviso.

DATO CLAVE: Las notificaciones electronicas en la DEHu caducan a los 10 dias naturales. La DEHu es accesible en dehunot.gob.es.

7. INTERMEDIACION DE DATOS (PID)

La Plataforma de Intermediacion de Datos (PID) permite a las Administraciones Publicas intercambiar informacion entre si, eliminando la obligacion del ciudadano de aportar documentos que ya obran en poder de la Administracion (principio "once only"). Se articula a traves del servicio de Verificacion y Consulta de Datos del Ministerio de Hacienda.

Servicios principales de la PID:
- Verificacion de datos de identidad (DNI/NIE)
- Consulta de datos de residencia
- Verificacion de datos de titulaciones universitarias
- Consulta de datos tributarios y de la Seguridad Social

DATO CLAVE: El principio "once only" obliga a la Administracion a no solicitar datos que ya posea. La PID lo hace posible tecnicamente entre administraciones.

PREGUNTAS TIPO EXAMEN INAP:

1. Segun la Ley 39/2015, cual es el plazo de caducidad de una notificacion electronica puesta a disposicion en la DEHu sin que el destinatario acceda a ella?
a) 5 dias naturales
b) 10 dias naturales
c) 15 dias habiles
d) 30 dias naturales
Respuesta correcta: b)

2. El estandar utilizado por el Sistema de Interconexion de Registros (SIR) para el intercambio de asientos registrales entre administraciones es:
a) SICRES 2.0
b) SICRES 3.0
c) SIRHUS 3.0
d) SIRED 4.0
Respuesta correcta: b)

3. En el ENS, si un sistema de informacion tiene una dimension valorada como ALTA, la categoria del sistema sera:
a) Media
b) Alta
c) Basica
d) Depende de las demas dimensiones
Respuesta correcta: b)

4. Cual de las siguientes NO es una dimension de seguridad reconocida por el ENS?
a) Trazabilidad
b) Disponibilidad
c) Escalabilidad
d) Confidencialidad
Respuesta correcta: c)"""

Tema.objects.filter(bloque__numero=4, numero=1).update(resumen_estudio=t1)
print("Tema 4.1 actualizado.")

# ============================================================
# TEMA 2: Identificacion, autenticacion y firma electronica
# ============================================================
t2 = """1. MARCO NORMATIVO: REGLAMENTO eIDAS Y LEY 6/2020

El Reglamento (UE) n.o 910/2014, conocido como eIDAS (Electronic IDentification, Authentication and trust Services), establece el marco juridico europeo para la identificacion electronica y los servicios de confianza. Tiene aplicacion directa en todos los Estados miembros y fue complementado en Espana por la Ley 6/2020, de 11 de noviembre, reguladora de determinados aspectos de los servicios electronicos de confianza.

El eIDAS reconoce tres niveles de seguridad para la identificacion electronica:
- Nivel BAJO: riesgo reducido de uso indebido de la identidad
- Nivel SUSTANCIAL: riesgo sustancial de uso indebido de la identidad
- Nivel ALTO: riesgo elevado de uso indebido, requiere verificacion presencial o equivalente

DATO CLAVE: El Reglamento eIDAS es el 910/2014. La Ley 6/2020 es la norma espanola que lo complementa en materia de servicios de confianza electronicos.

2. DIMENSIONES DE LA INTEROPERABILIDAD

El Esquema Nacional de Interoperabilidad (ENI) define tres dimensiones de la interoperabilidad:

- Interoperabilidad TECNICA: garantiza la interconexion de sistemas y servicios a nivel de infraestructura, protocolos y estandares tecnicos.
- Interoperabilidad SEMANTICA: asegura que el significado de la informacion intercambiada se preserve y entienda de igual manera por los sistemas que la comparten (uso de vocabularios controlados, ontologias, esquemas de metadatos).
- Interoperabilidad ORGANIZATIVA: define como las organizaciones acuerdan colaborar para prestar servicios conjuntos, incluyendo aspectos legales y de gobernanza.

DATO CLAVE: Las tres dimensiones del ENI son: Tecnica, Semantica y Organizativa. La organizativa incluye los acuerdos de colaboracion entre administraciones.

3. TIPOS DE FIRMA ELECTRONICA

El Reglamento eIDAS y la Ley 6/2020 reconocen tres tipos de firma electronica:

- Firma Electronica SIMPLE: datos electronicos adjuntos o asociados logicamente a otros datos para firmar. No exige requisito tecnico especial. Ejemplo: escanear una firma manuscrita.
- Firma Electronica AVANZADA: vinculada de manera unica al firmante, permite identificarlo, creada con datos bajo control exclusivo del firmante, y detecta cualquier cambio posterior. Se basa en certificados cualificados pero no necesariamente en dispositivos cualificados.
- Firma Electronica CUALIFICADA: firma avanzada creada mediante un dispositivo cualificado de creacion de firma (QSCD) y basada en un certificado cualificado de firma electronica. Tiene efecto juridico equivalente a la firma manuscrita en toda la UE.

DATO CLAVE: Solo la firma CUALIFICADA tiene efecto juridico equivalente a la firma manuscrita en toda la UE. Requiere certificado cualificado Y dispositivo cualificado (QSCD).

4. CERTIFICADOS ELECTRONICOS Y PRESTADORES DE SERVICIOS DE CONFIANZA

Un certificado electronico es un documento electronico emitido por un Prestador de Servicios de Confianza (TSP) que vincula los datos de verificacion de firma de una persona con su identidad. Los certificados cualificados son emitidos por Prestadores de Servicios de Confianza Cualificados (QTSP), incluidos en la lista de confianza de cada Estado miembro (en Espana, gestionada por el Ministerio de Asuntos Economicos).

En Espana, el principal emisor de certificados de ciudadano es la Fabrica Nacional de Moneda y Timbre (FNMT-RCM), a traves del Certificado de Ciudadano (antiguo CERES). Tambien emite certificados la Direccion General de la Policia (DNIe).

DATO CLAVE: La FNMT-RCM emite los certificados de ciudadano en Espana. El DNIe incorpora un certificado de autenticacion y otro de firma, ambos cualificados.

5. NORMAS TECNICAS DE INTEROPERABILIDAD (NTI)

Las NTI desarrollan aspectos concretos del ENI y son aprobadas por Resolucion de la Secretaria de Estado de Digitalizacion e Inteligencia Artificial. Las principales NTI relacionadas con firma e identificacion son:

- NTI de Politica de Firma Electronica y de Certificados: define los formatos de firma admitidos (XAdES, CAdES, PAdES) y los perfiles de certificado.
- NTI de Catalogo de Estandares: especifica los estandares tecnicos de uso obligatorio en las AAPP.
- NTI de Documento Electronico: define estructura, metadatos y requisitos de los documentos electronicos.
- NTI de Expediente Electronico: establece estructura y requisitos del expediente electronico administrativo.

DATO CLAVE: Los formatos de firma admitidos por la NTI de Politica de Firma son XAdES (XML), CAdES (CMS/PKCS#7) y PAdES (PDF).

6. DOCUMENTO Y EXPEDIENTE ELECTRONICO

El documento electronico administrativo es la informacion de cualquier naturaleza en forma electronica, archivada en un soporte electronico segun un formato determinado y susceptible de identificacion y tratamiento diferenciado. Debe incluir: contenido, datos de identificacion (metadatos minimos), firma electronica y, en su caso, metadatos complementarios.

El expediente electronico es el conjunto ordenado de documentos y actuaciones que sirven de antecedente y fundamento a la resolucion administrativa, incorporados en soporte electronico. El indice electronico garantiza la integridad e inmutabilidad del expediente y sus documentos, haciendo uso de la firma del organo o sello electronico.

DATO CLAVE: El expediente electronico se cierra con un indice electronico firmado por el organo o sello electronico del organismo, que garantiza la integridad del conjunto.

7. PLATAFORMA CL@VE (PIN, PERMANENTE Y FIRMA)

Cl@ve es el sistema comun de identificacion, autenticacion y firma electronica de las Administraciones Publicas espanolas. Ofrece tres modalidades:

- Cl@ve PIN: clave de un solo uso con validez limitada (generalmente 10 minutos), enviada por SMS o generada con la app Cl@ve PIN. Nivel de seguridad SUSTANCIAL. Indicada para tramites ocasionales.
- Cl@ve Permanente: usuario y contrasena de larga duracion reforzada con OTP. Nivel de seguridad SUSTANCIAL. Indicada para tramites frecuentes.
- Cl@ve Firma: firma en la nube basada en certificado centralizado, que permite firmar documentos sin necesidad de tener un certificado local instalado. Requiere activacion previa presencial o por video.

DATO CLAVE: Cl@ve PIN tiene validez de 10 minutos. Cl@ve Firma es la unica modalidad de Cl@ve que permite firmar electronicamente documentos (las otras dos solo autentican).

8. PLATAFORMA @FIRMA Y AUTOFIRMA

@firma es la plataforma de validacion de firma electronica y certificados de la AGE, gestionada por la SEDIA. Proporciona servicios de validacion de firmas, certificados, sellado de tiempo y custodia de firmas.

AutoFirma es el cliente de escritorio de firma electronica de la AGE, descargable gratuitamente. Permite a los ciudadanos firmar documentos y formularios electronicos directamente desde el navegador en tramites de la AGE. Es compatible con Windows, Linux y macOS.

DATO CLAVE: @firma es la plataforma servidora de validacion; AutoFirma es el cliente de escritorio para el ciudadano. @firma tambien ofrece el servicio TS@ de sellado de tiempo (timestamping).

PREGUNTAS TIPO EXAMEN INAP:

1. Cual de los siguientes tipos de firma electronica tiene efecto juridico equivalente a la firma manuscrita en toda la Union Europea?
a) Firma electronica simple
b) Firma electronica avanzada
c) Firma electronica cualificada
d) Firma electronica reconocida (termino espanol anterior al eIDAS)
Respuesta correcta: c)

2. Los formatos de firma electronica admitidos por la NTI de Politica de Firma en la AGE son:
a) RSA, DSA y ECDSA
b) XAdES, CAdES y PAdES
c) SHA-256, SHA-512 y MD5
d) PKCS#1, PKCS#7 y PKCS#12
Respuesta correcta: b)

3. En la plataforma Cl@ve, cual de las siguientes modalidades permite firmar documentos electronicamente?
a) Cl@ve PIN
b) Cl@ve Permanente
c) Cl@ve Firma
d) Cl@ve PIN y Cl@ve Permanente
Respuesta correcta: c)

4. El Reglamento eIDAS establece cuantos niveles de seguridad para la identificacion electronica?
a) Dos: basico y avanzado
b) Tres: bajo, sustancial y alto
c) Cuatro: minimo, basico, avanzado y cualificado
d) Dos: simple y cualificado
Respuesta correcta: b)"""

Tema.objects.filter(bloque__numero=4, numero=2).update(resumen_estudio=t2)
print("Tema 4.2 actualizado.")

# ============================================================
# TEMA 3: Esquema Nacional de Interoperabilidad (ENI)
# ============================================================
t3 = """1. CONCEPTO Y MARCO NORMATIVO DEL ENI

El Esquema Nacional de Interoperabilidad (ENI) fue aprobado por el Real Decreto 4/2010, de 8 de enero. Su objetivo es establecer los principios y directrices de interoperabilidad en el intercambio y conservacion de la informacion electronica por parte de las Administraciones Publicas, en el ejercicio de sus competencias y en el desarrollo de sus servicios y sistemas de informacion.

El ENI tiene caracter de norma de minimos: las Administraciones pueden establecer requisitos mas estrictos, pero nunca inferiores a los previstos en el ENI. Su ambito de aplicacion incluye la AGE, las administraciones de las comunidades autonomas, las entidades locales y las universidades publicas cuando usen medios electronicos.

DATO CLAVE: El ENI es el Real Decreto 4/2010. El ENS es el Real Decreto 311/2022. Son normas distintas y complementarias: el ENI regula interoperabilidad; el ENS regula seguridad.

2. PRINCIPIOS DEL ENI

Los principios basicos del ENI son:

- Interoperabilidad como cualidad integral: debe estar presente desde el diseno de los sistemas.
- Caracter multidimensional de la interoperabilidad: contempla las dimensiones tecnica, semantica y organizativa.
- Enfoque de soluciones multilaterales: priorizar estandares abiertos y soluciones de uso comun.
- Uso de estandares abiertos: los sistemas deben basarse en estandares de libre acceso y uso sin restricciones.
- Neutralidad tecnologica: no imponer tecnologias concretas, garantizando la libre competencia.
- Reutilizacion y colaboracion: compartir y reutilizar activos y soluciones entre administraciones.

DATO CLAVE: El ENI prioriza los estandares abiertos sobre los propietarios. Un estandar abierto es aquel de libre acceso, libre implementacion y sin restricciones de uso.

3. DIMENSIONES DE LA INTEROPERABILIDAD EN EL ENI

- Interoperabilidad ORGANIZATIVA: define como las organizaciones acuerdan cooperar para prestar servicios conjuntos. Incluye la publicacion de servicios en el Directorio de Aplicaciones para la Administracion (DIR3) y los convenios de colaboracion. El inventario de procedimientos administrativos es el catalogo de tramites publicado en el PAGe.

- Interoperabilidad SEMANTICA: garantiza que el significado de la informacion intercambiada se comprenda uniformemente. Incluye el uso de vocabularios controlados, esquemas de metadatos (Dublin Core, METS), modelos de datos compartidos y el Centro de Interoperabilidad Semantica de la Administracion (CISA).

- Interoperabilidad TECNICA: asegura la conexion tecnica entre sistemas. Incluye los protocolos de comunicacion, los formatos de datos, los esquemas XML y los estandares tecnicos del Catalogo de Estandares del ENI.

DATO CLAVE: El CISA (Centro de Interoperabilidad Semantica de la Administracion) gestiona los activos semanticos compartidos de las AAPP espanolas.

4. NTI DE DOCUMENTO ELECTRONICO

La Norma Tecnica de Interoperabilidad de Documento Electronico define los componentes del documento electronico administrativo:

- Contenido: la informacion propiamente dicha en formato electronico.
- Firma electronica: garantiza autenticidad e integridad. Puede ser firma de persona fisica, sello de organo o codigo de verificacion (CSV).
- Metadatos minimos obligatorios: identificador, organo, fecha de captura, origen (ciudadano/administracion), estado de elaboracion, tipo documental y tipo de firma.

El estado de elaboracion indica si el documento es: original, copia electronica autentica de original, copia electronica autentica de copia en papel, o copia en papel autentica de documento electronico.

DATO CLAVE: Los metadatos minimos obligatorios del documento electronico segun la NTI incluyen: identificador, organo, fecha de captura, origen, estado de elaboracion, tipo documental y tipo de firma.

5. NTI DE EXPEDIENTE ELECTRONICO

El expediente electronico esta compuesto por:
- Documentos electronicos: el contenido del expediente
- Indice electronico: lista ordenada de documentos con su firma, que garantiza la integridad
- Metadatos del expediente: datos descriptivos del conjunto
- Firma del indice: firma del organo o sello electronico que cierra el expediente

La NTI establece el estandar de intercambio basado en el formato ZIP que contiene: los documentos electronicos, el fichero de indice XML firmado y los metadatos.

DATO CLAVE: El indice electronico del expediente debe estar firmado con sello del organo o firma del responsable. El formato de intercambio de expedientes es un fichero ZIP con estructura normalizada.

6. NTI DE DIGITALIZACION DE DOCUMENTOS Y COPIADO AUTENTICO

La NTI de Digitalizacion define el proceso mediante el cual un documento en papel se convierte en documento electronico autentico. Requisitos:
- Calidad de imagen: suficiente para garantizar la fidelidad al original
- Formato: preferentemente PDF/A (para archivo a largo plazo) o TIFF
- Resolucion minima: 200 ppp en blanco y negro, 300 ppp para documentos a color o con graficos
- Firma: el documento digitalizado debe firmarse electronicamente por el funcionario habilitado o mediante sello del organo

El Copiado Autentico permite generar copias electronicas autenticas de documentos electronicos originales (ya existentes en formato electronico). La autenticidad se garantiza mediante firma o sello electronico.

DATO CLAVE: La resolucion minima para digitalizacion es 200 ppp en blanco y negro y 300 ppp en color. El formato de archivo a largo plazo es PDF/A.

7. CATALOGO DE ESTANDARES DEL ENI

El Catalogo de Estandares es una NTI que especifica los estandares tecnicos de uso obligatorio o preferente para las AAPP en sus sistemas de informacion. Se estructura en categorias:

- Estandares de documentos: ODF, PDF/A, CSV, XML, JSON
- Estandares de imagen: JPEG, PNG, TIFF, SVG
- Estandares de audio y video: MP3, MP4, OGG
- Estandares de compresion: ZIP, TAR.GZ
- Estandares de firma: XAdES, CAdES, PAdES
- Protocolos de comunicacion: HTTP/HTTPS, SMTP, FTP/SFTP

El catalogo se actualiza periodicamente para adaptarse a la evolucion tecnologica y se publica en el portal de la administracion electronica (PAe).

DATO CLAVE: El Catalogo de Estandares del ENI se publica y actualiza en el Portal de la Administracion Electronica (PAe), accesible en administracionelectronica.gob.es.

PREGUNTAS TIPO EXAMEN INAP:

1. El Esquema Nacional de Interoperabilidad fue aprobado por:
a) Real Decreto 311/2022
b) Real Decreto 4/2010
c) Ley 39/2015
d) Real Decreto 3/2010
Respuesta correcta: b)

2. Cual de las siguientes dimensiones de interoperabilidad del ENI se ocupa de garantizar que el significado de la informacion intercambiada sea comprendido de igual manera?
a) Interoperabilidad tecnica
b) Interoperabilidad organizativa
c) Interoperabilidad semantica
d) Interoperabilidad juridica
Respuesta correcta: c)

3. Segun la NTI de Digitalizacion de Documentos, cual es la resolucion minima recomendada para la digitalizacion de documentos a color?
a) 72 ppp
b) 150 ppp
c) 200 ppp
d) 300 ppp
Respuesta correcta: d)

4. El formato de archivo a largo plazo preferente segun el Catalogo de Estandares del ENI es:
a) DOCX
b) PDF/A
c) RTF
d) ODT
Respuesta correcta: b)"""

Tema.objects.filter(bloque__numero=4, numero=3).update(resumen_estudio=t3)
print("Tema 4.3 actualizado.")

# ============================================================
# TEMA 4: Esquema Nacional de Seguridad (ENS)
# ============================================================
t4 = """1. CONCEPTO Y MARCO NORMATIVO DEL ENS

El Esquema Nacional de Seguridad (ENS) fue aprobado inicialmente por el Real Decreto 3/2010, de 8 de enero, y posteriormente actualizado y derogado por el Real Decreto 311/2022, de 3 de mayo, que es la norma vigente. El ENS tiene por objeto establecer la politica de seguridad en la utilizacion de medios electronicos de las entidades de su ambito de aplicacion y esta constituido por sus principios basicos, requisitos minimos y medidas de seguridad.

El ambito de aplicacion del ENS incluye:
- La Administracion General del Estado (AGE)
- Las administraciones de las comunidades autonomas
- Las entidades locales
- Las universidades publicas
- Los proveedores privados que presten servicios o soluciones a las AAPP

DATO CLAVE: El ENS vigente es el Real Decreto 311/2022, de 3 de mayo. Deroga y sustituye al anterior RD 3/2010.

2. PRINCIPIOS BASICOS DEL ENS

El ENS establece los siguientes principios basicos que deben guiar la seguridad de los sistemas de informacion:

- Seguridad integral: la seguridad debe contemplarse globalmente como un proceso integral de gestion del riesgo.
- Gestion de la seguridad basada en riesgos: las medidas de seguridad se proporcionales al riesgo estimado.
- Prevencion, deteccion, respuesta y conservacion: se debe actuar antes, durante y despues de los incidentes.
- Lineas de defensa: los sistemas disponen de multiples capas de seguridad.
- Vigilancia continua: supervision permanente del estado de seguridad.
- Reevaluacion periodica: revision regular de las medidas implantadas.
- Diferenciacion de la responsabilidad: clara asignacion de roles y responsabilidades.

DATO CLAVE: El principio de "seguridad integral" implica que la seguridad afecta a personas, procesos y tecnologia, no solo a los sistemas informaticos.

3. DIMENSIONES DE SEGURIDAD DEL ENS

El ENS define cinco dimensiones de seguridad que se valoran para categorizar los sistemas:

- DISPONIBILIDAD (D): los activos estan accesibles y operativos cuando los usuarios autorizados los necesitan.
- INTEGRIDAD (I): los activos no han sido alterados de forma no autorizada.
- CONFIDENCIALIDAD (C): la informacion no se revela a personas o sistemas no autorizados.
- AUTENTICIDAD (A): la identidad de usuarios y sistemas puede verificarse de forma fehaciente.
- TRAZABILIDAD (T): las actuaciones sobre los activos quedan registradas y pueden ser auditadas.

Cada dimension se valora en cuatro niveles: BAJO, MEDIO, ALTO y MUY ALTO. La valoracion se hace en funcion del impacto que tendria un incidente de seguridad que comprometiera esa dimension.

DATO CLAVE: Las cinco dimensiones del ENS son DICAT: Disponibilidad, Integridad, Confidencialidad, Autenticidad y Trazabilidad. Los niveles de valoracion son: BAJO, MEDIO, ALTO y MUY ALTO.

4. CATEGORIZACION DE SISTEMAS: BASICA, MEDIA Y ALTA

La categoria del sistema determina el conjunto de medidas de seguridad aplicables del Anexo II del ENS. La categoria se determina por la dimension con el nivel mas alto:

- Categoria BASICA: cuando el mayor nivel de valoracion de las cinco dimensiones es BAJO.
- Categoria MEDIA: cuando el mayor nivel alcanza MEDIO, sin que ninguna dimension alcance ALTO.
- Categoria ALTA: cuando alguna dimension alcanza el nivel ALTO o MUY ALTO.

El proceso de categorizacion debe documentarse en el Documento de Seguridad del sistema y debe ser aprobado por el responsable de informacion y el responsable del servicio.

DATO CLAVE: Si una sola dimension es valorada como ALTA o MUY ALTA, el sistema es automaticamente de categoria ALTA, independientemente del valor del resto de dimensiones.

5. MEDIDAS DE SEGURIDAD: MARCO ORGANIZATIVO, OPERACIONAL Y PROTECCION

El Anexo II del ENS organiza las medidas de seguridad en tres grupos (marcos):

MARCO ORGANIZATIVO (org): medidas relacionadas con la organizacion y gestion de la seguridad.
- org.1: Politica de seguridad
- org.2: Normativa de seguridad
- org.3: Procedimientos de seguridad
- org.4: Proceso de autorizacion

MARCO OPERACIONAL (op): medidas que protegen la operacion del sistema.
- op.pl: Planificacion (analisis de riesgos, arquitectura de seguridad)
- op.acc: Control de acceso (identificacion, autenticacion, privilegios minimos)
- op.exp: Explotacion (inventario de activos, gestion de configuraciones)
- op.ext: Servicios externos (cadena de suministro)
- op.mon: Monitorizacion del sistema
- op.cont: Continuidad del servicio

MEDIDAS DE PROTECCION (mp): medidas que protegen activos concretos.
- mp.if: Proteccion de instalaciones (fisica)
- mp.per: Gestion del personal
- mp.eq: Proteccion de equipos
- mp.com: Proteccion de las comunicaciones
- mp.si: Proteccion de los soportes de informacion
- mp.sw: Proteccion de las aplicaciones
- mp.info: Proteccion de la informacion
- mp.s: Proteccion de los servicios

DATO CLAVE: Las medidas del ENS se dividen en tres marcos: Organizativo (org), Operacional (op) y Proteccion (mp). Su aplicacion depende de la categoria del sistema (Basica, Media o Alta).

6. ROLES Y RESPONSABILIDADES EN EL ENS

El ENS establece una clara diferenciacion de responsabilidades:

- Responsable de la Informacion: determina los requisitos de seguridad de la informacion tratada.
- Responsable del Servicio: determina los requisitos de seguridad de los servicios prestados.
- Responsable de Seguridad: determina las decisiones de seguridad e implementa las medidas. Es el CISO (Chief Information Security Officer) de la organizacion.
- Responsable del Sistema: desarrolla, opera y mantiene el sistema de informacion.

DATO CLAVE: El Responsable de Seguridad (CISO) es diferente al Responsable del Sistema. El Responsable de Seguridad no puede coincidir con el Responsable del Sistema en sistemas de categoria MEDIA y ALTA.

PREGUNTAS TIPO EXAMEN INAP:

1. El Real Decreto que aprueba el Esquema Nacional de Seguridad vigente es:
a) Real Decreto 4/2010, de 8 de enero
b) Real Decreto 3/2010, de 8 de enero
c) Real Decreto 311/2022, de 3 de mayo
d) Real Decreto 951/2015, de 23 de octubre
Respuesta correcta: c)

2. En el ENS, un sistema cuya dimension de mayor valoracion es MEDIO se clasifica como:
a) Categoria Basica
b) Categoria Media
c) Categoria Alta
d) Categoria Especial
Respuesta correcta: b)

3. Cual de los siguientes NO es un marco de medidas de seguridad del Anexo II del ENS?
a) Marco Organizativo
b) Marco Operacional
c) Marco Juridico
d) Medidas de Proteccion
Respuesta correcta: c)

4. Segun el ENS, el Responsable de Seguridad puede coincidir con el Responsable del Sistema en:
a) Sistemas de categoria Alta
b) Sistemas de categoria Media
c) Sistemas de categoria Basica
d) Nunca pueden coincidir
Respuesta correcta: c)"""

Tema.objects.filter(bloque__numero=4, numero=4).update(resumen_estudio=t4)
print("Tema 4.4 actualizado.")

# ============================================================
# TEMA 5: Seguridad de la informacion y ciberseguridad
# ============================================================
t5 = """1. CONCEPTO DE CIBERSEGURIDAD Y AMENAZAS

La ciberseguridad comprende el conjunto de actividades dirigidas a proteger las redes, los sistemas informaticos, los programas de computadora y los datos frente a ataques, daños o accesos no autorizados. El CCN (Centro Criptologico Nacional) es el organismo de la AGE responsable de la ciberseguridad en el ambito de la Administracion.

Las amenazas a la seguridad se clasifican segun su origen:
- Amenazas internas: empleados maliciosos, errores humanos, configuraciones incorrectas.
- Amenazas externas: ciberdelincuentes, grupos de ciberespionaje, hacktivistas, Estados.
- Amenazas ambientales: desastres naturales, cortes de suministro electrico.

DATO CLAVE: El CCN (Centro Criptologico Nacional) depende del CNI (Centro Nacional de Inteligencia) y es responsable de la ciberseguridad de la Administracion espanola.

2. TIPOS DE MALWARE

El malware (software malicioso) engloba todo programa disenado para causar daño o comprometer sistemas:

- VIRUS: codigo que se adjunta a programas legitimos y se replica cuando el programa se ejecuta. Requiere accion del usuario para propagarse. Ejemplo: virus de macro en documentos Office.
- GUSANO (Worm): se propaga automaticamente por redes sin necesidad de accion del usuario, explotando vulnerabilidades. Ejemplo: WannaCry, NotPetya.
- TROYANO: se disfraza de software legitimo. No se replica solo, pero abre puertas traseras o roba informacion. Ejemplo: troyanos bancarios como Emotet.
- RANSOMWARE: cifra los datos de la victima y exige rescate para recuperarlos. Es la amenaza mas prevalente en organismos publicos. Ejemplo: LockBit, Conti.
- SPYWARE: recopila informacion del usuario sin su conocimiento (contraseñas, habitos de navegacion). Ejemplo: keyloggers.
- ADWARE: muestra publicidad no deseada, normalmente asociado a spyware.
- ROOTKIT: oculta la presencia de malware en el sistema, modificando el sistema operativo.
- BOTNET: red de sistemas infectados controlados de forma remota para llevar a cabo ataques coordinados.

DATO CLAVE: La diferencia clave entre virus y gusano es que el virus necesita un archivo huesped y accion del usuario; el gusano se propaga solo por la red. El ransomware cifra datos y pide rescate.

3. VULNERABILIDADES Y ATAQUES

- PHISHING: correo electronico fraudulento que suplanta una identidad legítima para robar credenciales. Variantes: spear phishing (dirigido), whaling (a directivos), smishing (SMS), vishing (voz).
- DoS/DDoS: ataque de Denegacion de Servicio (DoS) o Distribuido (DDoS) que satura un sistema con trafico para dejarlo inoperativo. El DDoS usa botnets.
- SQL INJECTION: insercion de codigo SQL malicioso en campos de entrada de aplicaciones web para manipular la base de datos. Es la vulnerabilidad OWASP Top 10 mas conocida.
- XSS (Cross-Site Scripting): inyeccion de scripts maliciosos en paginas web que se ejecutan en el navegador de la victima. Permite robar sesiones o cookies.
- MAN-IN-THE-MIDDLE (MitM): el atacante se interpone en la comunicacion entre dos partes para interceptar o modificar el trafico. Se combate con cifrado TLS.
- ZERO-DAY: vulnerabilidad desconocida para el fabricante y sin parche disponible. Muy valorada en mercados de cibercrimen.
- INGENIERIA SOCIAL: manipulacion psicologica de personas para obtener informacion confidencial o acceso no autorizado.

DATO CLAVE: OWASP (Open Web Application Security Project) publica el Top 10 de vulnerabilidades web mas criticas. SQL Injection y XSS son habitualmente las mas representadas.

4. SISTEMAS DE DETECCION Y PREVENCION DE INTRUSOS (IDS/IPS)

- IDS (Intrusion Detection System): sistema PASIVO que monitoriza el trafico de red y genera alertas cuando detecta patrones anomalos o firmas de ataques conocidos. No bloquea el trafico.
- IPS (Intrusion Prevention System): sistema ACTIVO que, ademas de detectar, bloquea automaticamente el trafico malicioso. Se coloca en linea (inline) en la red.

Tipos segun su ubicacion:
- NIDS/NIPS: basados en red, analizan el trafico de la red.
- HIDS/HIPS: basados en host, analizan eventos del sistema operativo (logs, llamadas al sistema).

Metodos de deteccion:
- Por firmas (signature-based): compara el trafico con firmas de ataques conocidos. Eficaz pero no detecta ataques nuevos.
- Por anomalias (anomaly-based): detecta desviaciones del comportamiento normal. Puede detectar ataques nuevos pero genera mas falsos positivos.

DATO CLAVE: El IDS es PASIVO (solo alerta); el IPS es ACTIVO (alerta y bloquea). El IPS se coloca en linea en la red. Un SIEM (Security Information and Event Management) correlaciona eventos de seguridad de multiples fuentes.

5. CORTAFUEGOS (FIREWALLS)

Un cortafuegos es un dispositivo o software que controla el trafico de red entre redes o segmentos, aplicando reglas de seguridad. Tipos:

- Firewall de filtrado de paquetes: analiza cabeceras IP/TCP/UDP. Opera en capa 3-4 del modelo OSI. Sencillo y rapido pero limita inspeccion.
- Firewall de estado (stateful): rastrea el estado de las conexiones. Opera en capa 4. Mas seguro que el filtrado simple.
- Firewall de aplicacion (WAF - Web Application Firewall): opera en capa 7, analiza el contenido de las peticiones HTTP/HTTPS. Protege aplicaciones web de SQL Injection, XSS, etc.
- Next-Generation Firewall (NGFW): combina firewall tradicional con IPS, inspeccion SSL, control de aplicaciones y filtrado de URL.

DATO CLAVE: Un WAF (Web Application Firewall) opera en capa 7 y protege aplicaciones web. Un NGFW integra firewall + IPS + otras funciones de seguridad avanzada.

6. SERIES DE GUIAS CCN-STIC

El Centro Criptologico Nacional publica las Guias CCN-STIC (Series de Seguridad de las Tecnologias de la Informacion y las Comunicaciones). Se organizan en series:

- Serie 000: Politica y Estrategia
- Serie 100: Organizacion y normativa
- Serie 200: Instrucciones tecnicas del ENS
- Serie 300: Instrucciones tecnicas (aplicacion del ENS)
- Serie 400: Guias de configuracion de productos
- Serie 500: Guias para entornos Windows
- Serie 600: Guias para otros sistemas operativos (Linux, iOS, Android)
- Serie 800: Aplicacion del ENS (la mas relevante para el ENS)
- Serie 900: Informes tecnicos de ciberseguridad

La Guia CCN-STIC 808 es la referencia para la verificacion del cumplimiento del ENS. La serie 800 incluye guias para la aplicacion practica del ENS en distintos tipos de sistemas.

DATO CLAVE: La serie 800 de guias CCN-STIC es la mas importante para la aplicacion practica del ENS. El portal de acceso a las guias es ccn-cert.cni.es.

PREGUNTAS TIPO EXAMEN INAP:

1. Cual de los siguientes tipos de malware cifra los datos de la victima y exige un rescate economico para recuperarlos?
a) Spyware
b) Rootkit
c) Ransomware
d) Adware
Respuesta correcta: c)

2. La diferencia principal entre un IDS y un IPS es:
a) El IDS analiza trafico de red y el IPS analiza eventos del host
b) El IDS es pasivo (solo alerta) y el IPS es activo (alerta y bloquea)
c) El IDS usa firmas y el IPS usa anomalias
d) El IPS solo funciona en redes corporativas
Respuesta correcta: b)

3. Que tipo de ataque consiste en inyectar codigo SQL malicioso en campos de entrada de aplicaciones web?
a) XSS
b) DoS
c) Phishing
d) SQL Injection
Respuesta correcta: d)

4. La serie de guias CCN-STIC mas relevante para la aplicacion practica del Esquema Nacional de Seguridad es:
a) Serie 400
b) Serie 600
c) Serie 800
d) Serie 900
Respuesta correcta: c)"""

Tema.objects.filter(bloque__numero=4, numero=5).update(resumen_estudio=t5)
print("Tema 4.5 actualizado.")

# ============================================================
# TEMA 6: Criptografia y mecanismos de seguridad
# ============================================================
t6 = """1. CONCEPTO DE CRIPTOGRAFIA

La criptografia es la ciencia que estudia las tecnicas matematicas para proteger la informacion, garantizando la confidencialidad, integridad y autenticidad de los datos. Se divide en dos grandes familias: criptografia simetrica (clave secreta compartida) y criptografia asimetrica (par de claves publica/privada). Complementariamente, las funciones hash o resumen proporcionan integridad sin necesidad de clave.

DATO CLAVE: La criptografia garantiza tres propiedades fundamentales: Confidencialidad (nadie no autorizado lee el mensaje), Integridad (el mensaje no ha sido alterado) y Autenticidad (el emisor es quien dice ser).

2. CRIPTOGRAFIA SIMETRICA

En la criptografia simetrica, emisor y receptor comparten la misma clave secreta para cifrar y descifrar. Es muy rapida y eficiente, pero presenta el problema del intercambio seguro de la clave.

Cifrado en bloque: cifra bloques de tamano fijo de datos.
- DES (Data Encryption Standard): estandar historico, clave de 56 bits. Ya obsoleto por ser vulnerable a ataques de fuerza bruta.
- 3DES (Triple DES): aplica DES tres veces con dos o tres claves distintas. Clave efectiva de 112 o 168 bits. En desuso progresivo.
- AES (Advanced Encryption Standard): estandar actual, adoptado por NIST en 2001. Longitudes de clave: 128, 192 o 256 bits. Es el algoritmo simetrico mas utilizado del mundo.

Modos de operacion de cifrado en bloque:
- ECB (Electronic Codebook): el mas simple, inseguro para datos con patrones.
- CBC (Cipher Block Chaining): cada bloque depende del anterior. Mas seguro.
- CTR (Counter): convierte el cifrado en bloque en cifrado en flujo.
- GCM (Galois/Counter Mode): proporciona cifrado y autenticacion simultaneamente. Usado en TLS 1.3.

Cifrado en flujo: cifra bit a bit o byte a byte. Ejemplo: RC4 (obsoleto), ChaCha20 (moderno, usado en TLS 1.3).

DATO CLAVE: AES-256 es el algoritmo simetrico de referencia. El ENS recomienda AES con claves de al menos 128 bits. AES fue seleccionado por el NIST en 2001 tras un concurso publico.

3. CRIPTOGRAFIA ASIMETRICA

En la criptografia asimetrica cada entidad tiene un par de claves matematicamente relacionadas: una clave publica (que se comparte libremente) y una clave privada (que se mantiene en secreto). Lo que se cifra con una clave solo puede descifrarse con la otra.

Usos:
- Cifrado: se cifra con la clave publica del destinatario; solo el destinatario puede descifrar con su clave privada.
- Firma electronica: se firma con la clave privada del emisor; cualquiera puede verificar con la clave publica del emisor.

Algoritmos principales:
- RSA (Rivest-Shamir-Adleman): basado en la dificultad de factorizar numeros enteros grandes. Clave minima recomendada: 2048 bits (preferible 4096).
- ECC (Criptografia de Curva Eliptica): basada en la dificultad del problema del logaritmo discreto en curvas elipticas. Ofrece igual seguridad que RSA con claves mucho mas cortas. Una clave ECC de 256 bits equivale a RSA de 3072 bits.
- Diffie-Hellman: protocolo de intercambio de claves, no de cifrado directo. Permite establecer un secreto compartido sobre un canal inseguro.
- DSA/ECDSA: algoritmos de firma digital (Digital Signature Algorithm). ECDSA es la variante con curvas elipticas.

DATO CLAVE: ECC de 256 bits ofrece la misma seguridad que RSA de 3072 bits. RSA requiere claves de al menos 2048 bits para considerarse seguro hoy. La clave privada NUNCA se comparte.

4. FUNCIONES RESUMEN (HASH)

Una funcion hash criptografica transforma una entrada de tamano arbitrario en una salida de tamano fijo (el "digest" o resumen). Propiedades clave:
- Determinista: la misma entrada produce siempre el mismo hash.
- Resistencia a la preimagen: imposible calcular la entrada a partir del hash.
- Resistencia a colisiones: imposible encontrar dos entradas distintas con el mismo hash.
- Efecto avalancha: un cambio minimo en la entrada produce un hash totalmente diferente.

Algoritmos:
- MD5: resumen de 128 bits. Completamente roto y vulnerable a colisiones. NO usar.
- SHA-1: resumen de 160 bits. Obsoleto y vulnerable. NO usar para seguridad.
- SHA-256: pertenece a la familia SHA-2. Resumen de 256 bits. Ampliamente utilizado. Seguro.
- SHA-512: familia SHA-2. Resumen de 512 bits. Mayor seguridad, mas lento.
- SHA-3: familia basada en Keccak, diferente arquitectura a SHA-2. El NIST lo estandarizo en 2015.

DATO CLAVE: MD5 y SHA-1 estan rotos y NO deben usarse para seguridad. El estandar actual es SHA-256 (o superior). SHA-3 usa una arquitectura "esponja" diferente a SHA-1/SHA-2.

5. INFRAESTRUCTURA DE CLAVE PUBLICA (PKI)

La PKI (Public Key Infrastructure) es el conjunto de hardware, software, politicas y procedimientos que permiten crear, gestionar, distribuir, almacenar y revocar certificados digitales.

Componentes de una PKI:
- Autoridad de Certificacion (CA): entidad que emite y firma los certificados digitales. La CA raiz es la de mayor confianza.
- Autoridad de Registro (RA): verifica la identidad del solicitante antes de que la CA emita el certificado.
- Repositorio de certificados: directorio publico donde se publican los certificados emitidos.
- CRL (Certificate Revocation List): lista de certificados revocados publicada por la CA.
- OCSP (Online Certificate Status Protocol): servicio en linea para comprobar en tiempo real si un certificado esta revocado. Mas eficiente que la CRL.

DATO CLAVE: OCSP es mas eficiente que CRL para verificar la revocacion de certificados en tiempo real. La FNMT-RCM es la CA raiz de confianza en Espana para certificados de ciudadano.

6. PROTOCOLOS DE COMUNICACION SEGURA

- SSL/TLS: Secure Sockets Layer / Transport Layer Security. Protocolo de cifrado de comunicaciones en la capa de transporte. SSL esta obsoleto; TLS 1.3 es la version actual y recomendada. Usado en HTTPS, SMTPS, IMAPS. TLS 1.3 elimina algoritmos debiles y es mas rapido (0-RTT handshake).

- SSH (Secure Shell): protocolo de acceso remoto seguro a sistemas Unix/Linux. Puerto 22. Sustituye a Telnet (no cifrado). Soporta autenticacion por clave publica.

- IPsec (Internet Protocol Security): protocolo de seguridad en la capa de red (IP), que autentica y/o cifra cada paquete IP. Modos: Transporte (solo payload) y Tunel (todo el paquete). Usado en VPN de sitio a sitio.

- VPN (Virtual Private Network): red privada virtual que crea un tunel cifrado sobre una red publica. Tipos: acceso remoto (cliente-servidor) y sitio a sitio (entre sedes). Protocolos: IPsec, OpenVPN, WireGuard.

DATO CLAVE: TLS 1.3 es la version actual de TLS. Las versiones SSL, TLS 1.0 y TLS 1.1 estan obsoletas y prohibidas por el ENS. SSH usa el puerto 22 y sustituye a Telnet (puerto 23).

PREGUNTAS TIPO EXAMEN INAP:

1. Cual es el algoritmo de cifrado simetrico estandar mas utilizado actualmente, aprobado por el NIST?
a) DES
b) 3DES
c) AES
d) RSA
Respuesta correcta: c)

2. Que ventaja ofrece la criptografia de curva eliptica (ECC) frente a RSA?
a) Mayor velocidad con claves de igual longitud
b) Igual nivel de seguridad con claves mucho mas cortas
c) Compatibilidad con todos los algoritmos de hash
d) No requiere infraestructura PKI
Respuesta correcta: b)

3. Cual de los siguientes algoritmos de hash esta considerado roto y no debe usarse para aplicaciones de seguridad?
a) SHA-256
b) SHA-512
c) SHA-3
d) MD5
Respuesta correcta: d)

4. El protocolo OCSP se utiliza para:
a) Establecer conexiones VPN cifradas
b) Verificar en tiempo real si un certificado digital ha sido revocado
c) Intercambiar claves simetricas de forma segura
d) Firmar documentos electronicos con formato XAdES
Respuesta correcta: b)"""

Tema.objects.filter(bloque__numero=4, numero=6).update(resumen_estudio=t6)
print("Tema 4.6 actualizado.")

# ============================================================
# TEMA 7: CPD, virtualizacion y contenedores
# ============================================================
t7 = """1. CENTROS DE PROCESO DE DATOS (CPD): CONCEPTO Y CLASIFICACION

Un Centro de Proceso de Datos (CPD) o Data Center es la instalacion fisica que alberga los sistemas informaticos y de telecomunicaciones de una organizacion. Debe garantizar disponibilidad, seguridad y eficiencia energetica. El estandar de referencia para la clasificacion de CPD es la norma TIA-942 (Telecommunications Infrastructure Standard for Data Centers), que define cuatro niveles de disponibilidad denominados "Tiers":

- TIER I (Basic Site Infrastructure): sin redundancia. Disponibilidad del 99,671% (~28,8 h parada/ano). Mantenimiento programado requiere parada.
- TIER II (Redundant Capacity Components): redundancia de componentes criticos (N+1). Disponibilidad del 99,741% (~22 h parada/ano).
- TIER III (Concurrently Maintainable): mantenimiento sin interrupcion del servicio. Disponibilidad del 99,982% (~1,6 h parada/ano). Doble acometida electrica.
- TIER IV (Fault Tolerant): tolerante a fallos, redundancia 2N. Disponibilidad del 99,995% (~0,4 h parada/ano). Ningun fallo aislado detiene el servicio.

DATO CLAVE: El Tier IV garantiza disponibilidad del 99,995% (~26 minutos de parada al ano). El Tier III permite mantenimiento sin parar el servicio (concurrently maintainable).

2. INFRAESTRUCTURA FISICA DEL CPD

Un CPD requiere sistemas auxiliares criticos para su operacion:

Climatizacion:
- El calor generado por los servidores debe evacuarse para mantener temperatura (18-27 degC, recomendacion ASHRAE) y humedad relativa (40-60%).
- Sistemas CRAC (Computer Room Air Conditioning) y CRAH (Computer Room Air Handler).
- Estrategia de pasillos frios y calientes (hot aisle/cold aisle) para optimizar la refrigeracion.

Suministro electrico:
- SAI/UPS (Sistema de Alimentacion Ininterrumpida): proporciona alimentacion durante cortes breves de corriente hasta que el generador arranca.
- Generadores diesel: garantizan suministro electrico en cortes prolongados.
- PDU (Power Distribution Unit): distribuye la corriente a los racks.

Extincion de incendios:
- Sistemas de deteccion temprana (VESDA: Very Early Smoke Detection Apparatus).
- Extincion por gas inerte (Argon, Novec 1230, CO2) para no danar los equipos electronicos. Nunca agua.
- Doble piso y techo tecnico para canalizacion de cableado y aire.

DATO CLAVE: En un CPD se usa extincion por GAS (nunca agua). El SAI/UPS cubre el tiempo hasta que arranca el generador diesel. VESDA es el sistema de deteccion de humo muy temprana.

3. VIRTUALIZACION DE SISTEMAS

La virtualizacion permite ejecutar multiples sistemas operativos (maquinas virtuales) sobre un unico hardware fisico, optimizando el uso de recursos. El componente clave es el hipervisor (o VMM, Virtual Machine Monitor), que gestiona las maquinas virtuales.

Tipos de hipervisor:

TIPO 1 - Bare Metal (nativo): el hipervisor se ejecuta directamente sobre el hardware, sin sistema operativo anfitron. Mayor rendimiento y seguridad.
- Ejemplos: VMware ESXi, Microsoft Hyper-V (en modo servidor), KVM (Kernel-based Virtual Machine, integrado en el kernel Linux), Xen.

TIPO 2 - Hosted (alojado): el hipervisor se ejecuta como una aplicacion sobre un sistema operativo anfitron. Menor rendimiento pero mas sencillo de instalar.
- Ejemplos: Oracle VirtualBox, VMware Workstation, Parallels Desktop.

Ventajas de la virtualizacion:
- Consolidacion de servidores: reduccion del numero de servidores fisicos.
- Aislamiento: los fallos en una VM no afectan a otras.
- Snapshots: capturas del estado de la VM que permiten restaurar rapidamente.
- Alta disponibilidad: migracion en caliente (vMotion en VMware) de VMs entre hosts.
- Recuperacion ante desastres: replicacion de VMs a sitios alternativos.

DATO CLAVE: KVM es un hipervisor Tipo 1 de codigo abierto integrado en el kernel Linux. VMware ESXi es el lider de mercado en hipervisores Tipo 1 empresariales. VirtualBox es Tipo 2.

4. CONTENERIZACION CON DOCKER

Los contenedores son una tecnologia de virtualizacion a nivel de sistema operativo que empaqueta aplicaciones junto con sus dependencias en unidades aisladas y portables. A diferencia de las VMs, los contenedores comparten el kernel del sistema operativo anfitron, lo que los hace mucho mas ligeros y rapidos.

Conceptos clave de Docker:
- IMAGEN: plantilla de solo lectura que define el contenido del contenedor. Se construye a partir de un Dockerfile. Se almacena en registros como Docker Hub.
- CONTENEDOR: instancia en ejecucion de una imagen. Efimero y aislado.
- DOCKERFILE: fichero de texto con instrucciones para construir una imagen Docker (FROM, RUN, COPY, CMD, EXPOSE, ENV).
- VOLUMEN: mecanismo para persistir datos generados por los contenedores, fuera del sistema de ficheros del contenedor.
- DOCKER COMPOSE: herramienta para definir y ejecutar aplicaciones multi-contenedor mediante un fichero YAML (docker-compose.yml).
- DOCKER HUB: registro publico de imagenes Docker. Permite buscar y descargar imagenes oficiales.

DATO CLAVE: Los contenedores Docker comparten el kernel del host (a diferencia de las VMs). Una imagen Docker es inmutable; un contenedor es la instancia en ejecucion. Los datos persistentes se gestionan con volumenes.

5. ORQUESTACION CON KUBERNETES

Kubernetes (K8s) es la plataforma de orquestacion de contenedores mas extendida, desarrollada originalmente por Google y donada a la CNCF (Cloud Native Computing Foundation). Automatiza el despliegue, escalado y gestion de aplicaciones en contenedores.

Conceptos clave de Kubernetes:
- POD: la unidad minima de despliegue en Kubernetes. Agrupa uno o mas contenedores que comparten red y almacenamiento.
- DEPLOYMENT: objeto que gestiona el ciclo de vida de los Pods, garantizando el numero deseado de replicas en ejecucion.
- SERVICE: abstraccion que expone un conjunto de Pods como un servicio de red accesible. Tipos: ClusterIP, NodePort, LoadBalancer.
- NAMESPACE: mecanismo de aislamiento logico dentro del cluster para organizar recursos.
- CONFIGMAP / SECRET: objetos para gestionar configuracion y secretos (contrasenas, tokens) de forma desacoplada de la imagen.
- INGRESS: objeto que gestiona el acceso HTTP/HTTPS externo a los servicios del cluster, actuando como proxy inverso.
- NODO MASTER (Control Plane): gestiona el cluster. Componentes: API Server, etcd (base de datos de estado), Scheduler, Controller Manager.
- NODO WORKER: ejecuta los Pods. Componentes: kubelet, kube-proxy, container runtime.

DATO CLAVE: El Pod es la unidad minima de Kubernetes. etcd es la base de datos clave-valor que almacena el estado del cluster Kubernetes. Un Deployment gestiona replicas de Pods.

PREGUNTAS TIPO EXAMEN INAP:

1. Segun el estandar TIA-942, que nivel Tier garantiza que el mantenimiento puede realizarse sin interrumpir el servicio (concurrently maintainable)?
a) Tier I
b) Tier II
c) Tier III
d) Tier IV
Respuesta correcta: c)

2. Cual de los siguientes es un hipervisor de Tipo 1 (Bare Metal)?
a) Oracle VirtualBox
b) VMware Workstation
c) VMware ESXi
d) Parallels Desktop
Respuesta correcta: c)

3. En Docker, que elemento contiene las instrucciones para construir una imagen?
a) docker-compose.yml
b) Dockerfile
c) Volumen
d) Registry
Respuesta correcta: b)

4. En Kubernetes, cual es la unidad minima de despliegue?
a) Container
b) Node
c) Service
d) Pod
Respuesta correcta: d)"""

Tema.objects.filter(bloque__numero=4, numero=7).update(resumen_estudio=t7)
print("Tema 4.7 actualizado.")

# ============================================================
# TEMA 8: Cloud Computing
# ============================================================
t8 = """1. CONCEPTO Y CARACTERISTICAS DEL CLOUD COMPUTING

El Cloud Computing o computacion en la nube es un modelo que permite el acceso ubicuo, conveniente y bajo demanda a traves de la red a un conjunto compartido de recursos informaticos configurables (redes, servidores, almacenamiento, aplicaciones y servicios) que pueden aprovisionarse y liberarse rapidamente con minimo esfuerzo de gestion o interaccion del proveedor.

Esta definicion, ampliamente aceptada, proviene del NIST (National Institute of Standards and Technology) de EE.UU. (publicacion NIST SP 800-145).

El NIST define cinco caracteristicas esenciales del Cloud:
- AUTOSERVICIO BAJO DEMANDA: el usuario puede aprovisionar recursos sin interaccion humana con el proveedor.
- ACCESO UBICUO A LA RED: los recursos son accesibles a traves de la red desde multiples dispositivos.
- AGRUPACION DE RECURSOS (Resource Pooling): los recursos fisicos se comparten entre multiples usuarios (modelo multi-tenant).
- ELASTICIDAD RAPIDA: los recursos se escalan hacia arriba o hacia abajo de forma rapida y en ocasiones automatica.
- SERVICIO MEDIDO (Pago por uso): el uso de recursos se mide, controla y factura segun el consumo.

DATO CLAVE: La definicion de referencia del Cloud Computing es del NIST (SP 800-145). Las cinco caracteristicas esenciales son: Autoservicio bajo demanda, Acceso ubicuo, Agrupacion de recursos, Elasticidad y Servicio medido.

2. MODELOS DE SERVICIO: IaaS, PaaS y SaaS

El NIST define tres modelos de servicio en la nube:

IaaS (Infrastructure as a Service - Infraestructura como Servicio):
- El proveedor ofrece infraestructura de computacion virtualizada (CPU, memoria, almacenamiento, redes).
- El cliente gestiona el sistema operativo, middleware y aplicaciones.
- Ejemplos: Amazon EC2, Microsoft Azure Virtual Machines, Google Compute Engine.
- El cliente tiene el maximo control pero tambien la maxima responsabilidad de gestion.

PaaS (Platform as a Service - Plataforma como Servicio):
- El proveedor ofrece una plataforma de desarrollo y despliegue de aplicaciones.
- El cliente gestiona sus aplicaciones y datos; el proveedor gestiona el SO, middleware y la infraestructura.
- Ejemplos: Google App Engine, Microsoft Azure App Service, Heroku, OpenShift.
- Ideal para desarrolladores que quieren centrarse en el codigo sin gestionar infraestructura.

SaaS (Software as a Service - Software como Servicio):
- El proveedor ofrece aplicaciones completas accesibles por internet.
- El cliente solo usa la aplicacion; el proveedor gestiona todo.
- Ejemplos: Microsoft 365 (Office 365), Google Workspace, Salesforce, Zoom.
- El cliente tiene el minimo control pero la maxima simplicidad.

DATO CLAVE: En IaaS el cliente gestiona desde el SO hacia arriba. En PaaS, desde la aplicacion. En SaaS, solo usa la aplicacion. "Pizza as a Service" es la metafora popular para explicar la diferencia.

3. MODELOS DE DESPLIEGUE

- NUBE PUBLICA: infraestructura gestionada por un proveedor comercial (AWS, Azure, Google Cloud) y compartida entre multiples clientes. Mayor elasticidad y menor coste inicial, pero menor control.

- NUBE PRIVADA: infraestructura dedicada exclusivamente a una organizacion, gestionada internamente o por un tercero. Mayor control y seguridad, mayor coste. Ejemplos: OpenStack, VMware Cloud Foundation.

- NUBE HIBRIDA: combinacion de nube publica y privada, conectadas y con portabilidad de datos y aplicaciones entre ellas. Permite "cloud bursting" (desbordamiento a nube publica en picos de demanda).

- NUBE COMUNITARIA: infraestructura compartida por varias organizaciones con intereses comunes (sector publico, sanidad, educacion). Ejemplo: la nube de la AGE para administraciones publicas.

DATO CLAVE: La nube comunitaria es especialmente relevante para el sector publico. La nube hibrida permite "cloud bursting": desbordamiento de la nube privada a la publica en picos de demanda.

4. ESTRATEGIA CLOUD DE LA AGE

La estrategia Cloud de la Administracion General del Estado se articula en torno al principio "Cloud First" o "Nube Primero": los nuevos sistemas de informacion de la AGE deben evaluarse en primer lugar para su despliegue en la nube antes de considerarse soluciones on-premise.

El organismo responsable de la estrategia cloud en la AGE es la Secretaria de Estado de Digitalizacion e Inteligencia Artificial (SEDIA), a traves de la empresa publica RED.ES.

Elementos clave de la estrategia cloud AGE:
- Centro de Operaciones de Ciberseguridad de la AGE (COCS): supervisa la seguridad de los servicios cloud.
- Clasificacion de datos: los datos de la AGE se clasifican segun su sensibilidad para determinar el tipo de nube admisible.
- Nivel 1 (Datos publicos): nube publica admisible.
- Nivel 2 (Datos de uso interno): nube privada o publica con medidas adicionales.
- Nivel 3 (Datos sensibles): nube privada o comunitaria de la AGE.
- Nivel 4 (Datos clasificados): solo entornos bajo control directo de la AGE.

El portal Sara Cloud es la plataforma de servicios cloud de la AGE para los organismos de la Administracion.

DATO CLAVE: La estrategia cloud de la AGE sigue el principio "Cloud First". Los datos mas sensibles (Nivel 4) solo pueden alojarse en infraestructuras bajo control directo de la AGE.

5. VENTAJAS, RIESGOS Y CONSIDERACIONES DEL CLOUD

Ventajas del cloud computing:
- Reduccion de costes de infraestructura (CAPEX a OPEX)
- Escalabilidad y elasticidad bajo demanda
- Acceso global y disponibilidad alta
- Actualizaciones y mantenimiento gestionados por el proveedor
- Rapidez de aprovisionamiento

Riesgos y consideraciones:
- Dependencia del proveedor (vendor lock-in)
- Seguridad y privacidad de datos (soberania del dato)
- Cumplimiento normativo (RGPD, ENS, ENI)
- Disponibilidad de la conexion a internet
- Latencia en algunas aplicaciones criticas

Para el sector publico, el RGPD impone restricciones sobre la transferencia de datos personales fuera del Espacio Economico Europeo (EEE). Los proveedores cloud deben ofrecer garantias adecuadas.

DATO CLAVE: El "vendor lock-in" es la dependencia excesiva de un unico proveedor cloud. El RGPD limita la transferencia de datos fuera del EEE. Los proveedores cloud que operan para la AGE deben cumplir con el ENS.

PREGUNTAS TIPO EXAMEN INAP:

1. Segun el NIST, cual es el modelo de servicio cloud en el que el cliente gestiona desde el sistema operativo hacia arriba, siendo el proveedor responsable de la infraestructura subyacente?
a) SaaS
b) PaaS
c) IaaS
d) FaaS
Respuesta correcta: c)

2. Que modelo de despliegue cloud permite a una organizacion usar su nube privada normalmente y desbordarse a la nube publica en momentos de alta demanda?
a) Nube comunitaria
b) Nube hibrida
c) Nube publica
d) Nube multi-cloud
Respuesta correcta: b)

3. Cual es el principio que guia la estrategia cloud de la AGE, segun el cual los nuevos sistemas deben evaluarse primero para su despliegue en la nube?
a) Cloud Last
b) Cloud Only
c) Cloud First
d) Cloud Native
Respuesta correcta: c)

4. Cual de las siguientes NO es una caracteristica esencial del Cloud Computing segun el NIST?
a) Autoservicio bajo demanda
b) Elasticidad rapida
c) Licencias perpetuas de software
d) Servicio medido (pago por uso)
Respuesta correcta: c)"""

Tema.objects.filter(bloque__numero=4, numero=8).update(resumen_estudio=t8)
print("Tema 4.8 actualizado.")

# ============================================================
# TEMA 9: Continuidad de negocio, copias de seguridad y DRP/BCP
# ============================================================
t9 = """1. CONCEPTO DE CONTINUIDAD DE NEGOCIO

La continuidad de negocio es la capacidad de una organizacion para seguir operando y prestando sus servicios criticos durante y despues de una interrupcion, ya sea planificada o no. En el contexto de la Administracion Publica, la continuidad de los servicios electronicos es un requisito del ENS (medida op.cont).

Diferencia entre BCP y DRP:
- BCP (Business Continuity Plan / Plan de Continuidad de Negocio): plan integral que cubre la continuidad de TODOS los procesos criticos de la organizacion, incluyendo personas, instalaciones, comunicaciones y tecnologia.
- DRP (Disaster Recovery Plan / Plan de Recuperacion ante Desastres): plan especifico de TI para recuperar los sistemas de informacion y la infraestructura tecnologica tras un desastre. Es un componente del BCP.

DATO CLAVE: El DRP es un subconjunto del BCP. El BCP es el plan global; el DRP se centra en la recuperacion de los sistemas TI.

2. METRICAS CLAVE DE RECUPERACION: RTO Y RPO

Las dos metricas fundamentales para planificar la recuperacion ante desastres son:

- RTO (Recovery Time Objective / Objetivo de Tiempo de Recuperacion): tiempo maximo tolerable que puede estar un sistema o servicio inoperativo tras un incidente. Define cuanto tiempo puede permitirse la organizacion sin el servicio. Un RTO bajo (ej: 1 hora) implica mayor inversion en disponibilidad.

- RPO (Recovery Point Objective / Objetivo de Punto de Recuperacion): maxima cantidad de datos que la organizacion puede permitirse perder, medida en tiempo. Define hasta que punto en el pasado se puede restaurar la informacion. Un RPO de 4 horas significa que, en el peor caso, se perderan los datos generados en las ultimas 4 horas.

Relacion entre RTO/RPO y coste:
- A menor RTO y menor RPO, mayor coste en infraestructura de recuperacion.
- Lograr RTO=0 y RPO=0 (sin perdida de datos y sin interrupcion) requiere replicacion sincrona en tiempo real y sitios de respaldo Hot Site.

DATO CLAVE: RTO = cuanto tiempo puede estar caido el sistema. RPO = cuantos datos (en tiempo) puede perder la organizacion. RTO y RPO bajos = mayor coste. Ambos se miden en tiempo.

3. TIPOS DE COPIAS DE SEGURIDAD

Las copias de seguridad (backups) son la principal herramienta para garantizar la recuperabilidad de los datos:

- COPIA COMPLETA (Full Backup): copia de todos los datos seleccionados en cada ejecucion. Ventaja: restauracion rapida y sencilla. Inconveniente: mayor tiempo y espacio de almacenamiento.

- COPIA INCREMENTAL: solo copia los datos que han cambiado desde la ULTIMA copia (ya sea completa o incremental anterior). Ventaja: rapida y consume poco espacio. Inconveniente: restauracion lenta (requiere la completa + todas las incrementales sucesivas).

- COPIA DIFERENCIAL: copia los datos que han cambiado desde la ULTIMA COPIA COMPLETA. Ventaja: restauracion mas rapida que la incremental (solo necesita la completa + la ultima diferencial). Inconveniente: crece progresivamente hasta la proxima copia completa.

Comparativa:
- Espacio: Full > Diferencial > Incremental
- Tiempo de restauracion: Full < Diferencial < Incremental
- Tiempo de backup: Full > Diferencial > Incremental

DATO CLAVE: La copia incremental es la mas rapida de hacer pero la mas lenta de restaurar. La diferencial necesita solo la ultima completa + la ultima diferencial. La completa es la mas lenta pero la mas rapida de restaurar.

4. REGLA 3-2-1 DE COPIAS DE SEGURIDAD

La regla 3-2-1 es la practica recomendada para garantizar la recuperabilidad de los datos:

- 3: mantener al menos TRES copias de los datos (una original + dos copias de seguridad).
- 2: almacenar las copias en al menos DOS tipos de medios diferentes (ej: disco duro + cinta magnetica).
- 1: mantener al menos UNA copia en una ubicacion OFFSITE (fuera del centro de datos principal), preferiblemente geograficamente distante.

Variante moderna 3-2-1-1-0:
- +1 copia inmutable (protegida contra ransomware, no modificable).
- 0 errores verificados (las copias se comprueban regularmente).

DATO CLAVE: La regla 3-2-1: 3 copias, 2 medios distintos, 1 copia offsite. Es la recomendacion basica de cualquier plan de backup. La variante 3-2-1-1-0 anade copia inmutable y verificacion de errores.

5. CENTROS DE RESPALDO: HOT SITE, WARM SITE Y COLD SITE

Un centro de respaldo (o sitio alternativo) es una instalacion que permite reanudar las operaciones cuando el CPD principal falla. Se clasifican segun su grado de preparacion:

- HOT SITE (Sitio Caliente): centro totalmente equipado y operativo, con los sistemas actualizados en tiempo real (replicacion sincrona). Puede asumir las operaciones en minutos. Coste muy elevado. RTO minimo (minutos u horas).

- WARM SITE (Sitio Templado): centro equipado con hardware pre-instalado y configurado, pero los sistemas no estan completamente actualizados. Requiere restaurar los ultimos backups. RTO de horas a dias. Equilibrio entre coste y disponibilidad.

- COLD SITE (Sitio Frio): instalacion basica (espacio fisico, suministro electrico y conectividad) sin equipos instalados. Es necesario adquirir e instalar el hardware y restaurar todos los datos. RTO de dias a semanas. El de menor coste.

DATO CLAVE: Hot Site = disponible en minutos, maximo coste, replicacion en tiempo real. Warm Site = disponible en horas, coste intermedio. Cold Site = disponible en dias, minimo coste. A menor RTO, mayor coste del sitio.

6. PLAN DE CONTINUIDAD EN EL ENS

El ENS, en su medida op.cont, exige a los organismos publicos disponer de un plan de continuidad de los sistemas de informacion que soporte los servicios criticos. El plan debe incluir:

- Analisis de Impacto en el Negocio (BIA - Business Impact Analysis): identificacion de procesos criticos, recursos necesarios, RTO y RPO para cada proceso.
- Estrategia de continuidad: seleccion del tipo de sitio alternativo y modalidad de copia de seguridad.
- Procedimientos de activacion del plan: criterios para declarar un desastre y activar el plan.
- Pruebas y mantenimiento: el plan debe probarse periodicamente para verificar su eficacia.

El BIA es la base de todo plan de continuidad: sin saber que procesos son criticos y cuanto tiempo puede tolerarse su interrupcion, no es posible disenar una estrategia de recuperacion eficaz.

DATO CLAVE: El BIA (Business Impact Analysis) es el primer paso en la elaboracion de un BCP. Identifica los procesos criticos y determina el RTO y RPO de cada uno. El ENS exige que el plan de continuidad sea probado periodicamente.

PREGUNTAS TIPO EXAMEN INAP:

1. Cual es la diferencia entre RTO y RPO en un plan de recuperacion ante desastres?
a) RTO mide la perdida de datos y RPO mide el tiempo de inactividad
b) RTO mide el tiempo de inactividad tolerable y RPO mide la perdida de datos tolerable (en tiempo)
c) Son sinonimos, ambos miden el tiempo maximo de recuperacion
d) RTO aplica a hardware y RPO aplica a software
Respuesta correcta: b)

2. Que tipo de copia de seguridad solo copia los datos modificados desde la ultima copia completa?
a) Copia incremental
b) Copia diferencial
c) Copia completa
d) Copia sintetica
Respuesta correcta: b)

3. Segun la regla 3-2-1 de copias de seguridad, cuantas copias deben mantenerse fuera del centro de datos principal?
a) Tres
b) Dos
c) Una
d) Ninguna, basta con dos medios distintos
Respuesta correcta: c)

4. Que tipo de centro de respaldo permite asumir las operaciones en minutos gracias a la replicacion de datos en tiempo real?
a) Cold Site
b) Warm Site
c) Hot Site
d) Mirror Site
Respuesta correcta: c)"""

Tema.objects.filter(bloque__numero=4, numero=9).update(resumen_estudio=t9)
print("Tema 4.9 actualizado.")

print("\n=== TODOS LOS TEMAS DEL BLOQUE 4 ACTUALIZADOS CORRECTAMENTE ===")
