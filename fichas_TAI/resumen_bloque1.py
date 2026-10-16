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
# T4: El Procedimiento Administrativo Común (Ley 39/2015)
# ============================================================

t4_resumen = """1. AMBITO DE APLICACION Y PRINCIPIOS

La Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Comun de las Administraciones Publicas (LPACAP) regula los requisitos de validez y eficacia de los actos administrativos, el procedimiento administrativo comun, y los principios que han de regir la actuacion de las Administraciones Publicas. Entro en vigor el 2 de octubre de 2016, sustituyendo a la Ley 30/1992.

Se aplica al sector publico, que comprende:
- La Administracion General del Estado (AGE)
- Las Administraciones de las Comunidades Autonomas
- Las Entidades que integran la Administracion Local
- El sector publico institucional (organismos publicos, entidades de derecho publico, sociedades mercantiles estatales)

Los principios generales que rigen la actuacion administrativa son: legalidad, responsabilidad, servicio efectivo a los ciudadanos, simplicidad, claridad, proximidad, participacion, transparencia, objetividad, economia, eficiencia y eficacia. Se reconocen tambien los principios de buena fe y de confianza legitima en las relaciones de la Administracion con los ciudadanos.

DATO CLAVE: La Ley 39/2015 regula el procedimiento administrativo. La Ley 40/2015, de Regimen Juridico del Sector Publico, regula el funcionamiento interno. Ambas son del mismo dia: 1 de octubre de 2015.

Las Administraciones Publicas se relacionan con los ciudadanos preferentemente por medios electronicos. Los sujetos obligados a relacionarse electronica­mente con la Administracion son: personas juridicas, entidades sin personalidad juridica, quienes ejerzan una actividad profesional colegiada, empleados publicos, y quienes el reglamento determine.


2. INTERESADOS EN EL PROCEDIMIENTO

Tienen la consideracion de interesados en el procedimiento administrativo:
- Quienes lo promuevan como titulares de derechos o intereses legitimos individuales o colectivos
- Los que, sin haber iniciado el procedimiento, tengan derechos que puedan resultar afectados por la decision
- Aquellos cuyos intereses legitimos, individuales o colectivos, puedan resultar afectados y se personen en el procedimiento antes de que se dicte la resolucion definitiva

La capacidad de obrar ante las Administraciones Publicas la tienen las personas fisicas con capacidad de obrar conforme a las normas civiles, las personas juridicas y los grupos de afectados, uniones y entidades sin personalidad juridica y los patrimonios independientes o autonomos cuando la Ley asi lo declare expresamente.

DATO CLAVE: Los menores de edad tienen capacidad de obrar ante las AAPP en el ejercicio de derechos e intereses cuya actuacion este permitida sin necesidad de asistencia de quien ejerza la patria potestad, tutela o curatela.

La representacion puede otorgarse mediante:
- Apoderamiento apud acta, presencial o electronico
- Acreditacion de su inscripcion en el Registro de Apoderamientos (para tramites electronicos)
- Cualquier medio valido en derecho que deje constancia fidedigna de su existencia

Los ciudadanos tienen derecho a conocer en cualquier momento el estado de tramitacion de los procedimientos, a identificar a las autoridades responsables, a obtener copia de los documentos, a no presentar documentos no exigidos o ya aportados, y a ser tratados con respeto y deferencia.


3. ACTOS ADMINISTRATIVOS: REQUISITOS Y EFICACIA

Los actos administrativos son las declaraciones de voluntad, juicio, conocimiento o deseo realizadas por las Administraciones Publicas en el ejercicio de una potestad administrativa. Para ser validos deben reunir los siguientes requisitos:
- Competencia del organo que los dicta
- Objeto licito, determinado y posible
- Causa que los justifique
- Forma adecuada (generalmente escrita y motivada)

Deben ser motivados con sucinta referencia de hechos y fundamentos de derecho los actos que: limiten derechos subjetivos o intereses legitimos, los de tramite que decidan directa o indirectamente el fondo del asunto, los que se separen del criterio seguido en actuaciones precedentes, los acuerdos de suspension, y las resoluciones de procedimientos sancionadores.

DATO CLAVE: Los actos administrativos se presumen validos y producen efectos desde la fecha en que se dictan, salvo que en ellos se disponga otra cosa. La notificacion o publicacion no afecta a la validez del acto, sino a su eficacia.

La eficacia de los actos administrativos puede demorarse cuando:
- Lo exija el contenido del acto
- Este supeditada a su notificacion o publicacion
- Este supeditada a la aprobacion o autorizacion superior

Las notificaciones deben practicarse en el plazo de diez dias desde que el acto haya sido dictado. Si se practica en lugar inadecuado o con incumplimiento de formalidades pero el interesado muestra conformidad, surtira efecto desde la fecha en que se realice. La notificacion por medio de anuncios en el Boletin Oficial del Estado (BOE) se practica cuando es imposible notificar al interesado o a su representante.

La nulidad de pleno derecho se produce en los actos que: lesionen derechos fundamentales, sean dictados por organo manifiestamente incompetente por razon de la materia o del territorio, tengan contenido imposible, sean constitutivos de infraccion penal, se dicten prescindiendo total y absolutamente del procedimiento, sean contrarios al ordenamiento juridico con perjuicio del erario o evasion de responsabilidades. La anulabilidad es la regla general para el resto de infracciones del ordenamiento.


4. PLAZOS, SILENCIO ADMINISTRATIVO Y CADUCIDAD

Los plazos en el procedimiento administrativo se computan:
- Si se senalan por dias, se entienden dias habiles, excluyendo domingos y festivos nacionales, autonomicos y locales
- Si se senalan por dias naturales, se hara constar expresamente
- Si el plazo se fija en meses o anos, computa de fecha a fecha

DATO CLAVE: La ampliacion de plazos puede acordarse de oficio o a peticion del interesado, antes del vencimiento, hasta la mitad del plazo concedido, y no puede ampliarse el plazo de interposicion de recursos.

El silencio administrativo se produce cuando la Administracion no resuelve en el plazo establecido:
- SILENCIO POSITIVO (estimatorio): regla general en procedimientos iniciados a solicitud del interesado, salvo que una norma con rango de ley o derecho comunitario establezca lo contrario, o que el procedimiento tenga como efecto la transferencia al solicitante de facultades relativas al dominio publico o al servicio publico
- SILENCIO NEGATIVO (desestimatorio): en procedimientos de impugnacion de actos y disposiciones, en procedimientos de ejercicio del derecho de peticion, y cuando la estimacion tuviera como consecuencia que se transfirieran al solicitante facultades sobre dominio o servicio publico

La caducidad del procedimiento se produce cuando, iniciado de oficio, se paraliza por causa imputable a la Administracion durante mas de un mes (en sancionadores) o durante el plazo que determine la norma. En los iniciados a solicitud del interesado, la caducidad se produce si este paraliza el procedimiento por causa a el imputable durante tres meses.

DATO CLAVE: El plazo maximo para resolver y notificar la resolucion expresa es el fijado por la norma reguladora del procedimiento. Si no lo fija, el plazo es de tres meses. La obligacion de resolver se extiende a todos los procedimientos, cualquiera que sea su forma de iniciacion.

PREGUNTAS TIPO EXAMEN INAP:

1. Segun la Ley 39/2015, el silencio administrativo en un procedimiento iniciado a solicitud del interesado sera, con caracter general:
a) Negativo
b) Positivo (CORRECTA)
c) Nulo de pleno derecho
d) Anulable

2. El plazo maximo para resolver y notificar la resolucion expresa de un procedimiento, cuando la norma no establece plazo especifico, es:
a) Un mes
b) Dos meses
c) Tres meses (CORRECTA)
d) Seis meses

3. La Ley 39/2015 entro en vigor el:
a) 1 de octubre de 2015
b) 2 de octubre de 2016 (CORRECTA)
c) 1 de enero de 2016
d) 2 de octubre de 2015

4. Cual de los siguientes supuestos da lugar a la nulidad de pleno derecho de un acto administrativo:
a) Falta de motivacion del acto
b) Actos dictados prescindiendo total y absolutamente del procedimiento legalmente establecido (CORRECTA)
c) Infraccion de normas de procedimiento que no causen indefension
d) Incompetencia jerarquica del organo que dicta el acto"""

# ============================================================
# T5: Personal Funcionario al Servicio de las AAPP (TREBEP)
# ============================================================

t5_resumen = """1. CLASES DE PERSONAL AL SERVICIO DE LAS ADMINISTRACIONES PUBLICAS

El Real Decreto Legislativo 5/2015, de 30 de octubre, por el que se aprueba el texto refundido de la Ley del Estatuto Basico del Empleado Publico (TREBEP), es la norma marco que regula el empleo publico en Espana. Establece los principios generales aplicables al conjunto de las relaciones de empleo publico.

El personal al servicio de las Administraciones Publicas se clasifica en:
- FUNCIONARIOS DE CARRERA: vinculados a la Administracion por una relacion estatutaria regulada por el Derecho Administrativo
- FUNCIONARIOS INTERINOS: nombrados con caracter temporal por razones de necesidad y urgencia, para ocupar plazas de funcionarios de carrera, ejecutar programas de caracter temporal, o sustituir a funcionarios
- PERSONAL LABORAL: vinculado por contrato de trabajo (fijo, por tiempo indefinido o temporal)
- PERSONAL EVENTUAL: de confianza o asesoramiento especial, nombrado y cesado libremente, cuyo cese se produce automaticamente cuando cesa la autoridad que lo nombro
- PERSONAL DIRECTIVO PROFESIONAL: que desarrolla funciones directivas profesionales en las AAPP

DATO CLAVE: Los cuerpos y escalas de funcionarios se clasifican por grupos segun la titulacion exigida para el ingreso: Grupo A (subgrupos A1 y A2), Grupo B, Grupo C (subgrupos C1 y C2) y Agrupaciones Profesionales (sin titulacion). El cuerpo TAI pertenece al Subgrupo C1 (titulo de Bachiller o equivalente).


2. ADQUISICION Y PERDIDA DE LA CONDICION DE FUNCIONARIO

La condicion de funcionario de carrera se adquiere mediante:
- Superacion del proceso selectivo
- Nombramiento por el organo competente
- Acatamiento de la Constitucion y del Estatuto de Autonomia, en su caso, y del resto del ordenamiento juridico
- Toma de posesion dentro del plazo establecido

Los sistemas selectivos para el acceso a la funcion publica son:
- OPOSICION: proceso selectivo consistente en la realizacion de una o mas pruebas de aptitud
- CONCURSO-OPOSICION: consta de una fase de concurso (valoracion de meritos) y una fase de oposicion (pruebas de aptitud); la fase de oposicion tiene caracter eliminatorio
- CONCURSO: solo valoracion de meritos (solo para promocion interna)

DATO CLAVE: Los principios rectores del acceso al empleo publico son: publicidad, transparencia, imparcialidad, profesionalidad de los miembros de los organos de seleccion, independencia y discrecionalidad tecnica, adecuacion entre el contenido de los procesos selectivos y las funciones a desempenar, y agilidad en los procesos selectivos.

La condicion de funcionario de carrera se pierde por:
- Renuncia voluntaria
- Perdida de la nacionalidad
- Jubilacion total, que puede ser: forzosa a los 65 anos (o edad establecida), voluntaria, parcial, o por incapacidad permanente
- Sancion disciplinaria de separacion del servicio
- Pena principal o accesoria de inhabilitacion absoluta o especial

Las situaciones administrativas de los funcionarios son: servicio activo, servicios especiales, servicio en otras Administraciones Publicas, excedencia (forzosa, voluntaria por interes particular, voluntaria por agrupacion familiar, voluntaria por cuidado de familiares, por violencia de genero, por violencia terrorista) y suspension de funciones.


3. DERECHOS INDIVIDUALES Y COLECTIVOS

Los derechos individuales de los funcionarios publicos comprenden:
- A la inamovilidad en la condicion de funcionario de carrera
- A la progresion en la carrera profesional y a la promocion interna
- A percibir las retribuciones y las indemnizaciones por razon del servicio
- A participar en la consecucion de los objetivos de la unidad y ser informado
- A la defensa juridica y proteccion de la Administracion en los procedimientos que se sigan ante cualquier orden jurisdiccional
- A la formacion continua y a la actualizacion permanente de sus conocimientos y capacidades profesionales
- Al descanso, con respeto a los limites maximos de la jornada y a las vacaciones periodicas retribuidas
- A permisos y licencias
- A la jubilacion
- A las prestaciones de la Seguridad Social o mutualismo administrativo
- A la libre sindicacion y a la negociacion colectiva

DATO CLAVE: Las vacaciones anuales retribuidas de los funcionarios no podran ser inferiores a 22 dias habiles por ano completo de servicio o a los dias que correspondan proporcionalmente si el tiempo de servicios prestados es menor. Se incrementan segun los anos de servicio: 23 dias a partir de 15 anos, 24 a partir de 20, 25 a partir de 25 y 26 a partir de 30.

Los derechos colectivos incluyen: libertad sindical, derecho a la negociacion colectiva, consulta y participacion en la determinacion de condiciones de trabajo, derecho de reunion, derecho a plantear conflictos colectivos y derecho de huelga.

Las retribuciones de los funcionarios se clasifican en:
- Basicas: sueldo (segun el grupo de clasificacion), trienios y pagas extraordinarias (dos al ano)
- Complementarias: complemento de destino (nivel del puesto), complemento especifico (condiciones particulares del puesto), complemento de productividad y gratificaciones por servicios extraordinarios


4. DEBERES E INCOMPATIBILIDADES

Los empleados publicos tienen los siguientes deberes:
- Ejercer con diligencia las tareas que tengan asignadas y velar por los intereses generales con sujecion al ordenamiento juridico
- Actuar con arreglo a los principios eticos de objetividad, integridad, neutralidad, responsabilidad, imparcialidad, confidencialidad, dedicacion al servicio publico, transparencia, ejemplaridad, austeridad, accesibilidad, eficacia, honradez, promocion del entorno cultural y medioambiental y respeto a la igualdad entre mujeres y hombres
- Guardar secreto de las materias clasificadas y de los datos de caracter personal
- Informar a los ciudadanos sobre las materias que tengan derecho a conocer

El regimen de incompatibilidades esta regulado por la Ley 53/1984, de incompatibilidades del personal al servicio de las Administraciones Publicas. Con caracter general, el personal al servicio de las AAPP no puede simultanear dos o mas puestos de trabajo en el sector publico, ni actividades publicas con privadas cuando estas supongan conflicto de intereses.

DATO CLAVE: Se puede compatibilizar el puesto publico con actividades privadas que no comprometan la imparcialidad o independencia del funcionario, siempre que se obtenga reconocimiento previo de compatibilidad. La dedicacion exclusiva se compensa con un complemento especifico de incompatibilidad.

El regimen disciplinario distingue entre faltas muy graves (entre ellas el incumplimiento de la Constitucion, fraude, acoso laboral), graves y leves. Las sanciones van desde el apercibimiento (faltas leves) hasta la separacion del servicio (faltas muy graves). Las faltas muy graves prescriben a los 3 anos, las graves a los 2 anos y las leves a los 6 meses.

PREGUNTAS TIPO EXAMEN INAP:

1. El cuerpo de Tecnicos Auxiliares de Informatica (TAI) de la AGE pertenece al:
a) Subgrupo A1
b) Subgrupo A2
c) Subgrupo C1 (CORRECTA)
d) Subgrupo C2

2. Cual de los siguientes sistemas de seleccion puede emplearse como unico sistema para la promocion interna en las AAPP:
a) Oposicion
b) Concurso-oposicion
c) Concurso (CORRECTA)
d) Todos los anteriores por igual

3. Las vacaciones anuales retribuidas de los funcionarios no podran ser inferiores, con caracter general, a:
a) 20 dias habiles
b) 22 dias habiles (CORRECTA)
c) 22 dias naturales
d) 30 dias naturales

4. Las faltas muy graves de los funcionarios publicos prescriben en el plazo de:
a) 6 meses
b) 1 ano
c) 2 anos
d) 3 anos (CORRECTA)"""

# ============================================================
# T6: El Presupuesto del Estado en España
# ============================================================

t6_resumen = """1. CONCEPTO Y PRINCIPIOS PRESUPUESTARIOS

El Presupuesto General del Estado es el instrumento fundamental de la politica economica del Gobierno. La Ley 47/2003, de 26 de noviembre, General Presupuestaria (LGP), lo define como la expresion cifrada, conjunta y sistematica de los derechos y obligaciones a liquidar durante el ejercicio por cada uno de los organos y entidades que forman parte del sector publico estatal.

La base constitucional se encuentra en el articulo 134 de la Constitucion Espanola de 1978, que establece que el Gobierno elaborara los Presupuestos Generales del Estado y las Cortes Generales los examinaran, enmendaran y aprobaran.

Los principios presupuestarios clasicos son:
- UNIVERSALIDAD: el presupuesto debe recoger todos los gastos e ingresos del Estado, sin compensaciones entre si (principio de presupuesto bruto o de no afectacion)
- UNIDAD: todos los ingresos y gastos forman un unico presupuesto (unica caja)
- ANUALIDAD: el presupuesto se elabora y aprueba para cada ejercicio economico (ano natural, del 1 de enero al 31 de diciembre)
- ESPECIALIDAD: los creditos presupuestarios son especificos en cuanto a su cuantia, finalidad y organo ejecutor
- EQUILIBRIO: el volumen total de gastos debe estar cubierto por el volumen total de ingresos
- PUBLICIDAD: el presupuesto debe ser publico y conocido por los ciudadanos

DATO CLAVE: Si los Presupuestos Generales del Estado no se aprueban antes del 1 de enero del ejercicio siguiente, quedan automaticamente prorrogados los del ejercicio anterior hasta la aprobacion de los nuevos, sin perjuicio de las modificaciones que introduzca la Ley de Presupuestos.


2. ESTRUCTURA DEL PRESUPUESTO: CLASIFICACIONES ORGANICA, FUNCIONAL Y ECONOMICA

El presupuesto de gastos se estructura mediante tres clasificaciones complementarias:

CLASIFICACION ORGANICA: agrupa los creditos segun el centro gestor responsable de su ejecucion. La estructura es:
- Seccion (ministerio o maximo organo)
- Servicio (organo subordinado con dotacion diferenciada)
- Programa

DATO CLAVE: La seccion es la unidad organica de mayor nivel en la clasificacion organica del presupuesto. Cada ministerio constituye generalmente una seccion.

CLASIFICACION FUNCIONAL O POR PROGRAMAS: agrupa los creditos segun la naturaleza de las actividades a realizar. Se estructura en:
- Grupos de funcion (un digito: ej. 1 Servicios Publicos Basicos)
- Funciones (dos digitos: ej. 13 Seguridad ciudadana)
- Subfunciones (tres digitos)
- Programas (cinco digitos)

CLASIFICACION ECONOMICA: agrupa los creditos segun la naturaleza economica del gasto. Se distingue entre:
- Operaciones corrientes: remuneracion del personal (cap. 1), gastos corrientes (cap. 2), gastos financieros (cap. 3), transferencias corrientes (cap. 4)
- Operaciones de capital: inversiones reales (cap. 6), transferencias de capital (cap. 7)
- Operaciones financieras: activos financieros (cap. 8), pasivos financieros (cap. 9)

DATO CLAVE: El capitulo 1 de la clasificacion economica (Remuneraciones del personal) es, generalmente, el mayor capitulo de gasto en los presupuestos de las Administraciones Publicas. Los capitulos 1 a 4 son operaciones corrientes; los capitulos 6 y 7, de capital; y 8 y 9, financieras.


3. EL CICLO PRESUPUESTARIO: ELABORACION, APROBACION, EJECUCION Y LIQUIDACION

El ciclo presupuestario comprende cuatro fases:

ELABORACION: El Gobierno, a traves del Ministerio de Hacienda, elabora el proyecto de Presupuestos. El proceso comienza con el establecimiento de los objetivos de politica economica, continua con la elaboracion de los escenarios presupuestarios plurianuales, la fijacion de los techos de gasto para cada ministerio y la elaboracion por cada departamento de su presupuesto. El Gobierno debe remitir el Proyecto de Ley de Presupuestos a las Cortes Generales al menos tres meses antes de la expiracion del ejercicio en curso (antes del 1 de octubre).

APROBACION: Corresponde a las Cortes Generales. El Congreso de los Diputados tiene prioridad. Las enmiendas que supongan aumento de creditos o disminucion de ingresos requieren conformidad del Gobierno. Una vez aprobado por ambas Camaras, es sancionado y promulgado por el Rey.

DATO CLAVE: El plazo para que el Gobierno envie el Proyecto de Ley de Presupuestos al Congreso es antes del 1 de octubre (al menos tres meses antes del inicio del ejercicio siguiente).

EJECUCION: Es la fase en la que se materializan los ingresos y gastos presupuestados. Para la ejecucion del presupuesto de gastos existen cuatro fases:
- AUTORIZACION O APROBACION del gasto (acto por el que el organo competente acuerda la realizacion del gasto)
- DISPOSICION O COMPROMISO (acto por el que se acuerda la realizacion de un gasto determinado con un tercero)
- RECONOCIMIENTO Y LIQUIDACION DE LA OBLIGACION (reconocimiento del derecho del acreedor)
- ORDENACION DEL PAGO (emision de la orden de pago)

LIQUIDACION: Cierre del ejercicio presupuestario al 31 de diciembre. Los creditos no gastados quedan anulados, con algunas excepciones (creditos incorporables). La Cuenta General del Estado recoge la liquidacion del presupuesto y es elaborada por la Intervencion General de la Administracion del Estado (IGAE).


4. CONTROL INTERNO (IGAE) Y EXTERNO (TRIBUNAL DE CUENTAS)

CONTROL INTERNO - LA IGAE: La Intervencion General de la Administracion del Estado es el organo de control interno del sector publico estatal, dependiente del Ministerio de Hacienda. Ejerce sus funciones con plena autonomia respecto a las autoridades y demas entidades cuya gestion controla. Sus funciones comprenden:
- FUNCION INTERVENTORA: control previo de legalidad de todos los actos que reconocen derechos y aprueban gastos, comprometen fondos y ordenan pagos
- CONTROL FINANCIERO: verificacion posterior del funcionamiento de los servicios, organismos y entidades
- AUDITORIA PUBLICA: examen sistematico y objetivo de las operaciones financieras y de gestion
- CONTABILIDAD PUBLICA: llevanza de la contabilidad del Estado y elaboracion de la Cuenta General

DATO CLAVE: La funcion interventora es la modalidad de control que se ejerce con caracter PREVIO a la realizacion del gasto. El control financiero permanente y la auditoria publica son controles a POSTERIORI.

CONTROL EXTERNO - TRIBUNAL DE CUENTAS: Es el supremo organo fiscalizador de las cuentas y de la gestion economica del Estado y del sector publico. Depende directamente de las Cortes Generales. Sus funciones son:
- FUNCION FISCALIZADORA: examen y comprobacion de la Cuenta General del Estado y de las demas cuentas del sector publico
- FUNCION JURISDICCIONAL: enjuicia la responsabilidad contable en la que incurren quienes tienen a su cargo el manejo de caudales o efectos publicos

DATO CLAVE: El Tribunal de Cuentas tiene doble naturaleza: es un organo fiscalizador (externo al ejecutivo, dependiente de las Cortes) y un organo jurisdiccional (juzga la responsabilidad contable). Sus miembros (12 Consejeros) son elegidos por las Cortes Generales por un periodo de 9 anos.

PREGUNTAS TIPO EXAMEN INAP:

1. Segun el principio presupuestario de especialidad, los creditos del presupuesto son especificos en cuanto a:
a) Su importe y finalidad unicamente
b) Su cuantia, finalidad y el organo ejecutor (CORRECTA)
c) Su organo ejecutor y ejercicio economico
d) Su finalidad y el ejercicio economico

2. El Gobierno debe remitir el Proyecto de Ley de Presupuestos Generales del Estado a las Cortes Generales:
a) Antes del 1 de julio
b) Antes del 1 de septiembre
c) Antes del 1 de octubre (CORRECTA)
d) Antes del 1 de noviembre

3. La Intervencion General de la Administracion del Estado (IGAE) es el organo de:
a) Control externo del sector publico estatal, dependiente del Tribunal de Cuentas
b) Control externo del sector publico estatal, dependiente de las Cortes Generales
c) Control interno del sector publico estatal, dependiente del Ministerio de Hacienda (CORRECTA)
d) Control interno y externo del sector publico estatal

4. A cual de los siguientes capitulos de la clasificacion economica corresponden las "Inversiones reales":
a) Capitulo 4
b) Capitulo 5
c) Capitulo 6 (CORRECTA)
d) Capitulo 7"""

# ============================================================
# T7: Políticas de Igualdad de Género, Violencia de Género y LGTBIQ+
# ============================================================

t7_resumen = """1. PRINCIPIO DE IGUALDAD DE TRATO Y NO DISCRIMINACION

La Ley Organica 3/2007, de 22 de marzo, para la igualdad efectiva de mujeres y hombres (LOI), es la norma de referencia en materia de igualdad de genero. Transpone al ordenamiento espanol diversas directivas comunitarias y establece el marco normativo para la igualdad formal y real entre mujeres y hombres.

El principio de igualdad de trato y no discriminacion entre mujeres y hombres supone la ausencia de toda discriminacion, directa o indirecta, por razon de sexo en los ambitos educativo, economico, cultural y social, en particular en lo que se refiere al empleo, formacion profesional y condiciones de trabajo.

Se distingue entre:
- DISCRIMINACION DIRECTA: situacion en que una persona es tratada de manera menos favorable por razon de su sexo que otra en situacion comparable
- DISCRIMINACION INDIRECTA: situacion en que una disposicion, criterio o practica aparentemente neutros pone a personas de un sexo en desventaja particular con respecto a personas del otro

DATO CLAVE: La LO 3/2007 fue aprobada el 22 de marzo de 2007. Introduce en Espana, entre otras medidas, el permiso de paternidad y obliga a las empresas de mas de 250 trabajadores a elaborar planes de igualdad.

La ley introduce el principio de transversalidad (mainstreaming de genero): la perspectiva de genero debe integrarse en todas las politicas, planes, programas y actuaciones de las AAPP. Crea la figura del principio de presencia equilibrada, que exige que en los nombramientos y designaciones de organos colegiados y puestos directivos se cuente con una representacion de cada sexo que, como minimo, alcance el cuarenta por ciento.


2. PLANES DE IGUALDAD EN LAS ADMINISTRACIONES PUBLICAS

La Administracion General del Estado aprobara periodicamente un Plan para la Igualdad de sus empleados y empleadas que establecera los objetivos a alcanzar en materia de promocion de la igualdad de trato y oportunidades en el empleo publico, las estrategias o medidas a adoptar para su consecucion y los sistemas de seguimiento y evaluacion.

Los planes de igualdad son un conjunto ordenado de medidas adoptadas para alcanzar la igualdad de trato y oportunidades entre mujeres y hombres. En las empresas privadas, son obligatorios para las empresas con 50 o mas trabajadores.

DATO CLAVE: La LO 3/2007 crea la Delegacion del Gobierno para la Violencia de Genero y el Instituto de la Mujer. Tambien crea unidades de igualdad en cada Ministerio y una Comision Interministerial de Igualdad.

Medidas especificas para las AAPP en materia de igualdad:
- Protocolo de actuacion frente al acoso sexual y al acoso por razon de sexo en el empleo publico
- Evaluacion del impacto de genero en los proyectos normativos
- Estadisticas e informacion con datos desagregados por sexo
- Acciones formativas en materia de igualdad


3. MEDIDAS CONTRA LA VIOLENCIA DE GENERO: RECURSOS Y PROTOCOLOS

La Ley Organica 1/2004, de 28 de diciembre, de Medidas de Proteccion Integral contra la Violencia de Genero (LOVG) establece medidas de proteccion integral para prevenir, sancionar y erradicar la violencia que, como manifestacion de la discriminacion, la situacion de desigualdad y las relaciones de poder de los hombres sobre las mujeres, se ejerce sobre estas por parte de quienes sean o hayan sido sus conyuges o de quienes esten o hayan estado ligados a ellas por relaciones similares de afectividad.

La ley abarca la violencia fisica y psicologica, incluidas las agresiones a la libertad sexual, las amenazas, las coacciones o la privacion arbitraria de libertad.

DATO CLAVE: La LO 1/2004 crea el Juzgado de Violencia sobre la Mujer (JVM), la Delegacion del Gobierno para la Violencia de Genero y el Observatorio Estatal de Violencia sobre la Mujer. Las ordenes de proteccion se dictan por el Juzgado de Instruccion o el JVM.

Medidas de proteccion y recursos:
- Orden de proteccion: medida cautelar que puede incluir alejamiento, prohibition de comunicaciones y suspension de la patria potestad
- VioGen: sistema de seguimiento integral en los casos de violencia de genero del Ministerio del Interior
- ATENPRO: servicio de atencion y proteccion para victimas
- Telafono de atencion: 016 (gratuito y sin rastro en factura)
- Recuperacion economica: ayudas de la Seguridad Social, Renta Activa de Insercion (RAI)

Las victimas de violencia de genero tienen derechos laborales especificos como empleadas publicas: reduccion o reordenacion del tiempo de trabajo, movilidad geografica, excedencia por motivos de violencia de genero (computable a efectos de antiguedad), suspension con reserva del puesto de trabajo.


4. LEY 4/2023 PARA LA IGUALDAD REAL Y EFECTIVA DE LAS PERSONAS LGTBI

La Ley 4/2023, de 28 de febrero, para la igualdad real y efectiva de las personas lesbianas, gays, trans, bisexuales e intersexuales (Ley LGTBI), supone el primer reconocimiento legal en Espana de derechos especificos para las personas LGTBI en todos los ambitos de la vida publica.

Principios fundamentales de la ley:
- Igualdad de trato y no discriminacion por orientacion e identidad sexual, expresion de genero y caracteristicas sexuales
- Accion positiva para promover la igualdad real
- Transversalidad de las politicas LGTBI en todas las politicas publicas
- Participacion de las personas LGTBI en el diseno, seguimiento y evaluacion de las politicas

DATO CLAVE: La Ley 4/2023 fue aprobada el 28 de febrero de 2023 y entro en vigor el 2 de marzo de 2023. Incluye la autodeterminacion de genero para personas trans mayores de 16 anos sin necesidad de informe medico, y para menores de 16 anos con autorizacion judicial.

En el ambito del empleo publico, la ley obliga a las AAPP con mas de 50 empleados a elaborar Planes LGTBI con medidas concretas para garantizar la igualdad y no discriminacion. Crea el Consejo Participativo de las Personas LGTBI como organo de participacion social y el Centro Estatal de Recursos para la igualdad de las personas LGTBI.

Se prohibe expresamente la realizacion y financiacion publica de terapias de conversion, tratamientos o practicas que pretendan modificar la orientacion sexual o la identidad de genero de las personas. Las infracciones se clasifican en leves, graves y muy graves, con sanciones de hasta 150.000 euros para las infracciones muy graves.

PREGUNTAS TIPO EXAMEN INAP:

1. La Ley Organica 1/2004 de medidas de proteccion integral contra la violencia de genero fue aprobada el:
a) 22 de marzo de 2007
b) 28 de diciembre de 2004 (CORRECTA)
c) 28 de febrero de 2023
d) 1 de enero de 2005

2. El principio de presencia equilibrada establecido en la LO 3/2007 exige que en los organos colegiados y puestos directivos cada sexo este representado en al menos:
a) El 25 por ciento
b) El 33 por ciento
c) El 40 por ciento (CORRECTA)
d) El 50 por ciento

3. El telefono de atencion a victimas de violencia de genero establecido por la LO 1/2004 es:
a) 112
b) 016 (CORRECTA)
c) 900 100 009
d) 010

4. Segun la Ley 4/2023, las AAPP con mas de cuantos empleados estan obligadas a elaborar Planes LGTBI:
a) 50 (CORRECTA)
b) 100
c) 250
d) 500"""

# ============================================================
# T8: Transparencia, Acceso a la Información Pública y Buen Gobierno
# ============================================================

t8_resumen = """1. PRINCIPIOS DE BUEN GOBIERNO Y REGIMEN SANCIONADOR

La Ley 19/2013, de 9 de diciembre, de Transparencia, Acceso a la Informacion Publica y Buen Gobierno (LTAIBG), tiene un triple objeto: ampliar y reforzar la transparencia de la actividad publica, reconocer y garantizar el derecho de acceso a la informacion publica y establecer las obligaciones de buen gobierno a las que han de someterse los responsables publicos, asi como las consecuencias de su incumplimiento.

El buen gobierno regula las obligaciones eticas y de actuacion que deben cumplir los altos cargos y asimilados del Gobierno y del sector publico estatal. Se articulan principios de:
- PRINCIPIOS DE ACTUACION: transparencia, imparcialidad, objetividad, ejercicio de la autoridad al servicio del interes general
- PRINCIPIOS ETICOS: actuar con transparencia, honestidad e integridad; abstenerse en asuntos en que tengan un interes personal; no aceptar regalos que puedan condicionar el ejercicio de sus funciones
- PRINCIPIOS DE GESTION: actuar con austeridad, eficacia, eficiencia y economia

DATO CLAVE: La Ley 19/2013 entro en vigor de manera escalonada: las obligaciones de publicidad activa y el Titulo II de Buen Gobierno entraron en vigor el 10 de diciembre de 2014. El derecho de acceso a la informacion publica entro en vigor para la AGE el mismo dia, y para CCAA y Entidades Locales en el plazo de dos anos.

El regimen sancionador en materia de buen gobierno clasifica las infracciones en:
- MUY GRAVES: incumplimiento de los principios eticos y de conducta que hubieran supuesto condena penal o sancion administrativa firme por infraccion grave; gestion de asuntos personales con informacion privilegiada; uso de los bienes o recursos publicos en beneficio personal; ocultar situaciones de conflicto de interes
- GRAVES: induccion o tolerancia de conductas que supongan infraccion leve
- LEVES: incumplimiento de principios eticos sin caracter grave o muy grave

Las sanciones en materia de buen gobierno pueden incluir la declaracion de incumplimiento y su publicacion, destititucion en los cargos directivos, y devolucion de cantidades indebidamente percibidas.


2. PUBLICIDAD ACTIVA: INFORMACION INSTITUCIONAL, ORGANIZATIVA Y ECONOMICA

La publicidad activa obliga a las Administraciones Publicas a difundir proactivamente, de forma periodica y actualizada, informacion relevante, sin necesidad de que el ciudadano la solicite. La informacion debe ser clara, estructurada y comprensible y publicarse en el Portal de Transparencia.

Las obligaciones de publicidad activa se agrupan en tres categorias:
- INFORMACION INSTITUCIONAL, ORGANIZATIVA Y DE PLANIFICACION: funciones de los organos administrativos, normativa aplicable, estructura organizativa con organigramas y datos de contacto, planes y programas con el grado de cumplimiento y evaluacion
- INFORMACION DE RELEVANCIA JURIDICA: directrices, instrucciones, acuerdos, circulares; anteproyectos de ley y proyectos de decretos legislativos; proyectos de reglamentos; memorias e informes incluidos en los expedientes de elaboracion de normas
- INFORMACION ECONOMICA, PRESUPUESTARIA Y ESTADISTICA: presupuestos con descripcion de las principales partidas y su estado de ejecucion; cuentas anuales; retribuciones de los maximos responsables; resoluciones de autorizacion de actividades privadas de altos cargos; declaraciones anuales de bienes y actividades; contratos (con datos del adjudicatario y cuantia); convenios suscritos; encomiendas de gestion; subvenciones y ayudas concedidas

DATO CLAVE: La informacion publicada en el Portal de Transparencia debe ser veraz, actualizada, accesible y comprensible. La ley no exige que se publiquen todos los datos, sino la informacion que sea relevante para garantizar la transparencia de la actividad publica.


3. DERECHO DE ACCESO A LA INFORMACION PUBLICA

El derecho de acceso a la informacion publica es el derecho de todas las personas a acceder a la informacion publica, entendida como los contenidos o documentos que obren en poder de los sujetos obligados por la ley y que hayan sido elaborados o adquiridos en el ejercicio de sus funciones.

Sujetos obligados: todas las Administraciones Publicas, las entidades que integran la Administracion Local, las instituciones del Estado (Congreso, Senado, Tribunal Constitucional, Tribunal de Cuentas, etc.), las corporaciones de derecho publico, y los partidos politicos, organizaciones sindicales y empresariales y entidades privadas que perciban ayudas o subvenciones publicas en determinadas cuantias.

DATO CLAVE: Puede solicitar informacion cualquier persona, sin necesidad de motivar la solicitud, aunque la motivacion puede ser tenida en cuenta en la ponderacion del interes publico frente a los limites. El plazo de resolucion es de UN MES, prorrogable por otro mes mas cuando el volumen o la complejidad lo requieran.

Limites al derecho de acceso (articulo 14 de la Ley 19/2013):
- La seguridad nacional
- La defensa
- Las relaciones exteriores
- La seguridad publica
- La prevencion, investigacion y sancion de los ilicitos penales, administrativos o disciplinarios
- La igualdad de las partes en los procesos judiciales
- Las funciones administrativas de vigilancia, inspeccion y control
- Los intereses economicos y comerciales
- La politica economica y monetaria
- La proteccion del medio ambiente
- La proteccion de datos personales

Si la solicitud es denegada, el interesado puede presentar reclamacion ante el Consejo de Transparencia y Buen Gobierno (CTBG), previo o sustitutivo del recurso contencioso-administrativo.


4. EL PORTAL DE TRANSPARENCIA Y EL CONSEJO DE TRANSPARENCIA Y BUEN GOBIERNO

El PORTAL DE TRANSPARENCIA es el instrumento a traves del cual la AGE cumple con sus obligaciones de publicidad activa. Es un punto de acceso electronico desde el que los ciudadanos pueden acceder a la informacion publica de forma centralizada. Su administracion corresponde al Ministerio de la Presidencia, Relaciones con las Cortes y Memoria Democratica.

El CONSEJO DE TRANSPARENCIA Y BUEN GOBIERNO (CTBG) es el organismo independiente creado por la Ley 19/2013 para promover la cultura de la transparencia, controlar el cumplimiento de las obligaciones de publicidad activa, salvaguardar el ejercicio del derecho de acceso a la informacion publica y garantizar la observancia de las disposiciones de buen gobierno.

DATO CLAVE: El CTBG es un organismo publico independiente, con personalidad juridica propia y plena capacidad de obrar. Adscrito al Ministerio de Hacienda, su Presidente es nombrado por el Consejo de Ministros por un periodo de 5 anos, entre personas de reconocido prestigio y competencia profesional. El cargo es irrevocable salvo en los supuestos establecidos por ley.

El CTBG tiene competencias para:
- Resolver las reclamaciones por denegacion del acceso a la informacion publica
- Promover la transparencia en la actividad publica
- Evaluar el grado de aplicacion de la ley
- Asesorar a las AAPP en materia de transparencia
- Aplicar el regimen sancionador en materia de buen gobierno

PREGUNTAS TIPO EXAMEN INAP:

1. El plazo para resolver las solicitudes de acceso a la informacion publica establecido en la Ley 19/2013 es:
a) 15 dias habiles, prorrogables por otros 15
b) Un mes, prorrogable por otro mes mas (CORRECTA)
c) Tres meses, sin posibilidad de prorroga
d) 20 dias naturales, prorrogables por otros 20

2. El Consejo de Transparencia y Buen Gobierno esta adscrito a:
a) La Presidencia del Gobierno
b) El Ministerio de Justicia
c) El Ministerio de Hacienda (CORRECTA)
d) Las Cortes Generales

3. La Ley 19/2013 fue aprobada el:
a) 9 de diciembre de 2013 (CORRECTA)
b) 10 de diciembre de 2013
c) 9 de octubre de 2013
d) 1 de enero de 2014

4. Cual de los siguientes supuestos NO constituye un limite al derecho de acceso a la informacion publica segun el articulo 14 de la Ley 19/2013:
a) La seguridad nacional
b) La proteccion del medio ambiente
c) Los intereses economicos y comerciales
d) El interes personal del solicitante (CORRECTA)"""

# ============================================================
# T9: Protección de Datos Personales (RGPD y LOPDGDD)
# ============================================================

t9_resumen = """1. PRINCIPIOS DEL TRATAMIENTO DE DATOS PERSONALES

El Reglamento (UE) 2016/679 del Parlamento Europeo y del Consejo, de 27 de abril de 2016, relativo a la proteccion de las personas fisicas en lo que respecta al tratamiento de datos personales y a la libre circulacion de estos datos (RGPD), es de aplicacion directa en todos los Estados miembros de la UE desde el 25 de mayo de 2018. En Espana se complementa con la Ley Organica 3/2018, de 5 de diciembre, de Proteccion de Datos Personales y garantia de los derechos digitales (LOPDGDD).

El RGPD define dato personal como toda informacion sobre una persona fisica identificada o identificable (el interesado). Quedan fuera de su ambito: los datos de personas fallecidas, los datos anonimizados y los datos de personas juridicas.

Los principios del tratamiento de datos personales (articulo 5 RGPD) son:
- LICITUD, LEALTAD Y TRANSPARENCIA: el tratamiento debe ser licito, leal y transparente
- LIMITACION DE LA FINALIDAD: los datos deben recogerse con fines determinados, explicitos y legitimos, y no seran tratados de manera incompatible con dichos fines
- MINIMIZACION DE DATOS: los datos tratados deben ser adecuados, pertinentes y limitados a lo necesario en relacion con los fines del tratamiento
- EXACTITUD: los datos deben ser exactos y actualizados
- LIMITACION DEL PLAZO DE CONSERVACION: los datos no deben conservarse mas tiempo del necesario para los fines del tratamiento
- INTEGRIDAD Y CONFIDENCIALIDAD: tratamiento de forma que se garantice la seguridad adecuada de los datos
- RESPONSABILIDAD PROACTIVA (ACCOUNTABILITY): el responsable del tratamiento es responsable del cumplimiento de los principios y debe poder demostrarlo

DATO CLAVE: El RGPD es aplicable desde el 25 de mayo de 2018. La LOPDGDD fue aprobada el 5 de diciembre de 2018 y adapta el ordenamiento espanol al RGPD. El RGPD tiene aplicacion directa; no necesita transposicion.

Las bases juridicas que legitiman el tratamiento de datos (articulo 6 RGPD) son: consentimiento del interesado, ejecucion de un contrato, cumplimiento de una obligacion legal, proteccion de intereses vitales, cumplimiento de una mision de interes publico, e interes legitimo del responsable o de un tercero.


2. DERECHOS DEL INTERESADO

El RGPD reconoce un catalogo de derechos a los interesados que pueden ejercerse frente al responsable del tratamiento:

- DERECHO DE ACCESO (articulo 15): el interesado tiene derecho a obtener confirmacion de si se estan tratando datos que le conciernen y, en tal caso, a obtener una copia de dichos datos y diversa informacion sobre el tratamiento
- DERECHO DE RECTIFICACION (articulo 16): el interesado tiene derecho a obtener la rectificacion de datos inexactos o incompletos
- DERECHO DE SUPRESION o "derecho al olvido" (articulo 17): el interesado tiene derecho a obtener la supresion de sus datos cuando ya no sean necesarios para los fines para los que fueron recogidos, retire el consentimiento, o el tratamiento sea ilicito, entre otras causas
- DERECHO A LA LIMITACION DEL TRATAMIENTO (articulo 18): el interesado puede solicitar que el tratamiento quede restringido, por ejemplo mientras se verifica la exactitud de los datos
- DERECHO A LA PORTABILIDAD DE DATOS (articulo 20): el interesado tiene derecho a recibir sus datos en un formato estructurado, de uso comun y lectura mecanica, y a transmitirlos a otro responsable; solo aplica cuando el tratamiento se basa en el consentimiento o un contrato y se realiza por medios automatizados
- DERECHO DE OPOSICION (articulo 21): el interesado puede oponerse al tratamiento de sus datos en cualquier momento por motivos relacionados con su situacion particular, cuando el tratamiento se base en el interes publico o el interes legitimo

DATO CLAVE: El derecho a la portabilidad solo se aplica cuando el tratamiento se basa en el consentimiento o en un contrato, y se realiza por medios automatizados. No aplica cuando el tratamiento es necesario para el cumplimiento de una mision de interes publico o en el ejercicio de poderes publicos.

El plazo para responder a las solicitudes de ejercicio de derechos es de UN MES desde la recepcion de la solicitud, prorrogable por dos meses mas en casos complejos o con gran numero de solicitudes (con notificacion al interesado en el primer mes).


3. RESPONSABLE Y ENCARGADO DEL TRATAMIENTO

El RGPD distingue dos figuras principales en el tratamiento de datos:

RESPONSABLE DEL TRATAMIENTO: persona fisica o juridica, autoridad publica, servicio u otro organismo que, solo o junto con otros, determine los fines y medios del tratamiento de datos personales. Es quien decide el QUE y el COMO del tratamiento.

ENCARGADO DEL TRATAMIENTO: persona fisica o juridica, autoridad publica, servicio u otro organismo que trate datos personales por cuenta del responsable. Actua siempre bajo las instrucciones del responsable y debe garantizar las medidas de seguridad adecuadas.

DATO CLAVE: La relacion entre responsable y encargado debe formalizarse mediante un CONTRATO o acto juridico vinculante que establezca el objeto, duracion, naturaleza y finalidad del tratamiento, el tipo de datos personales y categorias de interesados y las obligaciones y derechos del responsable.

El DELEGADO DE PROTECCION DE DATOS (DPD o DPO, por sus siglas en ingles) es la figura creada por el RGPD para supervisar el cumplimiento de la normativa en materia de proteccion de datos. Su designacion es obligatoria para:
- Autoridades u organismos publicos (en todo caso)
- Entidades que realicen tratamientos que requieran observacion habitual y sistematica de interesados a gran escala
- Entidades que traten a gran escala categorias especiales de datos o datos relativos a condenas e infracciones penales

El DPD puede ser un empleado del responsable o actuar en el marco de un contrato de servicios. Debe contar con conocimientos especializados del Derecho y la practica en materia de proteccion de datos. El responsable no puede darle instrucciones respecto al ejercicio de sus funciones, y no puede ser sancionado ni destituido por el ejercicio de estas.

El RGPD introduce la obligacion de notificar las violaciones de seguridad (brechas de datos) a la autoridad de control en el plazo de 72 HORAS desde que se tenga constancia de la misma, y al interesado cuando sea probable que entranen un alto riesgo para sus derechos y libertades.


4. LA AGENCIA ESPANOLA DE PROTECCION DE DATOS (AEPD)

La Agencia Espanola de Proteccion de Datos (AEPD) es la autoridad de control independiente encargada de velar por el cumplimiento de la normativa de proteccion de datos en Espana. Es un ente de derecho publico, con personalidad juridica propia y plena capacidad publica y privada. Actua con plena independencia de los poderes publicos en el ejercicio de sus funciones.

DATO CLAVE: La AEPD fue creada por la Ley Organica 5/1992 (LORTAD), antecedente de la LOPDGDD. Con la LOPDGDD de 2018, la AEPD se convierte en la autoridad de control prevista en el RGPD para Espana. Su director es nombrado por el Gobierno mediante Real Decreto, previa convocatoria publica, por un periodo de 5 anos, renovable por una vez.

Las funciones principales de la AEPD son:
- Supervisar y controlar la aplicacion del RGPD y la LOPDGDD
- Atender las reclamaciones formuladas por los interesados
- Investigar posibles infracciones de la normativa
- Imponer sanciones administrativas en caso de infraccion
- Emitir informes y dictamenes en materia de proteccion de datos
- Promover la sensibilizacion y comprension del publico en materia de proteccion de datos
- Cooperar con otras autoridades de control de la UE (en el marco del Comite Europeo de Proteccion de Datos)

El regimen sancionador del RGPD distingue dos niveles de multas administrativas:
- Infracciones menos graves: multas de hasta 10.000.000 EUR o el 2% del volumen de negocio anual mundial total del ejercicio financiero anterior (si es superior)
- Infracciones mas graves: multas de hasta 20.000.000 EUR o el 4% del volumen de negocio anual mundial total del ejercicio financiero anterior (si es superior)

DATO CLAVE: Las sanciones maximas del RGPD son de 20 millones de euros o el 4% del volumen de negocio anual mundial. En Espana, la LOPDGDD adapta estas sanciones y establece un sistema de graduacion especifico para las AAPP, que reciben apercibimiento en lugar de multa economica, aunque la infraccion se publicara en el BOE.

PREGUNTAS TIPO EXAMEN INAP:

1. Cual de los siguientes derechos del RGPD solo es aplicable cuando el tratamiento se basa en el consentimiento o un contrato y se realiza por medios automatizados:
a) Derecho de acceso
b) Derecho de rectificacion
c) Derecho de oposicion
d) Derecho a la portabilidad (CORRECTA)

2. El plazo para notificar una violacion de seguridad de datos a la autoridad de control, segun el RGPD, es de:
a) 24 horas
b) 48 horas
c) 72 horas (CORRECTA)
d) 7 dias

3. La designacion del Delegado de Proteccion de Datos (DPD) es obligatoria para:
a) Solo para empresas privadas con mas de 250 empleados
b) Todas las empresas con mas de 50 empleados
c) Todas las autoridades u organismos publicos (CORRECTA)
d) Solo para las empresas que traten datos de menores

4. Segun la LOPDGDD, cuando la AEPD impone una sancion a una Administracion Publica, esta consistira en:
a) Multa de hasta 20 millones de euros
b) Multa del 2% del presupuesto anual
c) Apercibimiento con publicacion en el BOE (CORRECTA)
d) Suspension de actividades durante 30 dias"""

# ============================================================
# Actualización de la base de datos
# ============================================================

temas_a_actualizar = [
    {
        "numero": 4,
        "titulo_contiene": "Procedimiento",
        "resumen": t4_resumen
    },
    {
        "numero": 5,
        "titulo_contiene": "funcionario",
        "resumen": t5_resumen
    },
    {
        "numero": 6,
        "titulo_contiene": "presupuesto",
        "resumen": t6_resumen
    },
    {
        "numero": 7,
        "titulo_contiene": "Igualdad",
        "resumen": t7_resumen
    },
    {
        "numero": 8,
        "titulo_contiene": "Transparencia",
        "resumen": t8_resumen
    },
    {
        "numero": 9,
        "titulo_contiene": "Proteccion de Datos",
        "resumen": t9_resumen
    },
]

print("Iniciando actualizacion de resumenes_estudio del Bloque I TAI...")

for item in temas_a_actualizar:
    try:
        # Buscar por numero de tema
        qs = Tema.objects.filter(bloque__numero=1, numero=item["numero"])
        if not qs.exists():
            # Intentar por titulo
            qs = Tema.objects.filter(bloque__numero=1, titulo__icontains=item["titulo_contiene"])

        if qs.exists():
            tema = qs.first()
            tema.resumen_estudio = item["resumen"]
            tema.save(update_fields=["resumen_estudio"])
            print(f"  [OK] T{item['numero']} - '{tema.titulo[:60]}...' actualizado.")
        else:
            print(f"  [WARN] No se encontro el Tema {item['numero']} ({item['titulo_contiene']}). Omitido.")
    except Exception as e:
        print(f"  [ERROR] Tema {item['numero']}: {e}")

print("\nProceso completado. Verifica los temas en el panel de administracion.")
