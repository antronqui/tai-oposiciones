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
# TEMA 1: Arquitectura de ordenadores
# ============================================================
t1 = """1. CONCEPTO Y VISION GENERAL

La arquitectura de ordenadores define la organizacion logica y fisica de un sistema informatico: como se relacionan sus componentes para ejecutar instrucciones. El modelo de referencia dominante es la arquitectura von Neumann (1945), en la que CPU, memoria y dispositivos de E/S comparten un bus comun. Los tres recursos fundamentales son la Unidad Central de Proceso (CPU), la memoria y el subsistema de entrada/salida.

DATO CLAVE: La arquitectura von Neumann almacena datos e instrucciones en la misma memoria. La arquitectura Harvard (usada en microcontroladores) los separa en memorias distintas.

2. COMPONENTES DE LA CPU

La CPU (Central Processing Unit) es el cerebro del ordenador. Se compone de:

- Unidad Aritmetico-Logica (ALU): ejecuta operaciones aritmeticas (suma, resta, multiplicacion, division) y logicas (AND, OR, NOT, XOR). Opera sobre operandos tomados de los registros.
- Unidad de Control (UC): interpreta las instrucciones del programa y genera las senales de control que coordinan el resto de componentes. Contiene el decodificador de instrucciones y el secuenciador.
- Registros: memoria ultrarapida integrada en la CPU. Tipos principales: Contador de Programa (PC/IP) que apunta a la siguiente instruccion; Registro de Instruccion (IR) que almacena la instruccion en curso; Acumulador (ACC) para resultados de la ALU; Registro de Estado o Flags (PSW) con bits de condicion (cero, acarreo, desbordamiento, signo); Registros de proposito general (EAX, EBX... en x86; R0-R31 en ARM).
- Reloj del sistema: genera pulsos que sincronizan las operaciones. La frecuencia se mide en GHz.

DATO CLAVE: El PC (Program Counter) contiene la direccion de memoria de la PROXIMA instruccion a ejecutar. Tras fetch, se incrementa automaticamente.

3. CICLO DE INSTRUCCION

Cada instruccion pasa por varias fases que forman el ciclo de instruccion (o ciclo fetch-decode-execute):

- FETCH (Busqueda): la UC copia el contenido del PC al MAR (Memory Address Register), accede a memoria, carga la instruccion en el MBR (Memory Buffer Register) y la transfiere al IR. Incrementa el PC.
- DECODE (Decodificacion): la UC interpreta el codigo de operacion (opcode) del IR y determina que operacion se va a realizar y cuales son los operandos.
- FETCH OPERANDS (Busqueda de operandos): si la instruccion requiere datos en memoria, se buscan. Si estan en registros, ya estan disponibles.
- EXECUTE (Ejecucion): la ALU realiza la operacion. La UC genera las senales de control adecuadas.
- WRITE-BACK (Escritura de resultado): el resultado se escribe en el registro destino o en memoria.

DATO CLAVE: El ciclo basico es FETCH - DECODE - EXECUTE. El pipeline permite solapar estas fases para distintas instrucciones simultaneamente, aumentando el rendimiento.

4. JERARQUIA DE MEMORIA

La jerarquia de memoria organiza los distintos tipos de almacenamiento segun velocidad, capacidad y coste (a mayor velocidad, menor capacidad y mayor coste):

- Registros: integrados en la CPU. Velocidad: <1 ns. Capacidad: decenas de bytes.
- Cache L1: dentro del nucleo del procesador. Velocidad: 1-5 ns. Capacidad: 32-128 KB por nucleo. Separada en L1i (instrucciones) y L1d (datos).
- Cache L2: dentro o muy proxima al nucleo. Velocidad: 5-15 ns. Capacidad: 256 KB - 1 MB.
- Cache L3: compartida entre nucleos. Velocidad: 20-50 ns. Capacidad: 4-64 MB.
- RAM (DRAM): memoria principal. Velocidad: 50-100 ns. Capacidad: 4-256 GB. Volatil.
- Almacenamiento secundario: SSD (microsegundos) o HDD (milisegundos). No volatil. Capacidad: TB.
- Almacenamiento terciario: cintas magneticas, almacenamiento optico. Muy lento, alta capacidad.

DATO CLAVE: El principio de localidad justifica la cache: localidad temporal (un dato usado recientemente se usara de nuevo pronto) y localidad espacial (si se accede a un dato, pronto se accedera a datos adyacentes).

5. BUSES DEL SISTEMA

Un bus es un conjunto de lineas de comunicacion compartidas. Los buses principales son:

- Bus de datos: transfiere datos entre componentes. Su anchura (8, 16, 32, 64 bits) determina cuantos bits se transfieren en cada ciclo.
- Bus de direcciones: la CPU coloca la direccion de memoria o dispositivo al que quiere acceder. Su anchura determina el espacio de direccionamiento (32 bits = 4 GB maximo de RAM direccionable).
- Bus de control: transporta senales de control: lectura/escritura, reloj, interrupciones, reset, habilitacion de bus.

La arquitectura moderna usa buses especializados de alta velocidad: PCIe (tarjetas graficas, SSD NVMe), DMI/QPI entre CPU y chipset, DDR5 para la RAM.

DATO CLAVE: Un bus de direcciones de 32 bits puede direccionar 2^32 = 4.294.967.296 posiciones de memoria (4 GB). Por eso los sistemas de 32 bits no pueden usar mas de 4 GB de RAM sin extensiones como PAE.

6. PROCESADORES MODERNOS

Los procesadores actuales incorporan multiples tecnicas de mejora del rendimiento:

- Multinucleo (multi-core): varios nucleos de procesamiento independientes en el mismo chip. Permiten paralelismo real. Ejemplo: Intel Core i7 con 8 nucleos.
- Hyperthreading / SMT (Simultaneous Multithreading): cada nucleo fisico presenta dos nucleos logicos al SO, aprovechando unidades funcionales ociosas. Un i7 con 8 nucleos fisicos ofrece 16 hilos logicos.
- Pipeline: division del ciclo de instruccion en etapas que se solapan. Un pipeline de 5 etapas puede procesar hasta 5 instrucciones simultaneamente (en distintas fases). Problemas: hazards de datos, de control (saltos) y estructurales.
- Ejecucion fuera de orden (Out-of-Order, OoO): la CPU reordena instrucciones para evitar esperas por dependencias de datos.
- Prediccion de saltos (Branch Prediction): anticipa el resultado de instrucciones de bifurcacion para no vaciar el pipeline en caso de salto.
- SIMD (Single Instruction, Multiple Data): una sola instruccion opera sobre multiples datos en paralelo. Extensiones: MMX, SSE, SSE2, AVX, AVX-512 (Intel/AMD). Clave para multimedia, IA y calculo cientifico.
- Overclocking: aumento artificial de la frecuencia del reloj por encima de la especificacion del fabricante.

DATO CLAVE: SIMD permite a una instruccion AVX-512 procesar 512 bits (16 floats de 32 bits) simultaneamente, acelerando operaciones vectoriales y matriciales drasticamente.

PREGUNTAS TIPO EXAMEN INAP:

1. En la arquitectura von Neumann, ?que componente contiene la direccion de la proxima instruccion a ejecutar?
   a) Registro de instruccion (IR)
   b) Contador de programa (PC)  [CORRECTA]
   c) Acumulador (ACC)
   d) Registro de estado (PSW)

2. ?Cual es la funcion del bus de direcciones?
   a) Transportar datos entre la CPU y la memoria
   b) Indicar la direccion de memoria o dispositivo al que se accede  [CORRECTA]
   c) Generar senales de reloj para sincronizar componentes
   d) Controlar las operaciones de lectura y escritura

3. ?Que tecnica permite a un procesador ejecutar varias instrucciones en distintas fases de forma simultanea?
   a) Multithreading
   b) SIMD
   c) Pipeline  [CORRECTA]
   d) Cache L3

4. Un bus de direcciones de 32 bits puede direccionar como maximo:
   a) 2 GB
   b) 4 GB  [CORRECTA]
   c) 8 GB
   d) 16 GB
"""

Tema.objects.filter(bloque__numero=2, numero=1).update(resumen_estudio=t1)
print("Tema 2.1 actualizado.")

# ============================================================
# TEMA 2: Representacion y codificacion de la informacion
# ============================================================
t2 = """1. SISTEMAS DE NUMERACION

Un sistema de numeracion es un conjunto de simbolos y reglas para representar cantidades. Los mas relevantes en informatica son:

- Binario (base 2): digitos 0 y 1. Es el sistema nativo del hardware digital.
- Octal (base 8): digitos 0-7. Cada digito octal equivale a 3 bits.
- Decimal (base 10): digitos 0-9. Sistema cotidiano.
- Hexadecimal (base 16): digitos 0-9 y A-F. Cada digito hex equivale a 4 bits (nibble).

Conversiones clave:
- Decimal a binario: divisiones sucesivas entre 2, leer restos de abajo a arriba.
- Binario a hexadecimal: agrupar bits de 4 en 4 desde la derecha. Ejemplo: 10111100 -> 1011|1100 -> B|C -> 0xBC.
- Hexadecimal a binario: cada digito hex se convierte en 4 bits. 0xBC -> 1011 1100.
- Binario a octal: agrupar bits de 3 en 3 desde la derecha.

DATO CLAVE: 1 byte = 8 bits. 1 nibble = 4 bits = 1 digito hexadecimal. La conversion entre binario y hexadecimal es directa e inmediata por la potencia de 2 (2^4 = 16).

2. REPRESENTACION DE ENTEROS

Para enteros sin signo, la representacion binaria directa es suficiente. Para enteros con signo existen varios metodos:

- Signo y magnitud: el bit mas significativo (MSB) representa el signo (0=positivo, 1=negativo). Problema: dos representaciones del cero (+0 y -0). Con n bits: rango [-(2^(n-1)-1), +(2^(n-1)-1)].
- Complemento a 1 (C1): para negar un numero, se invierten todos los bits. Ejemplo: +5 = 0101 -> -5 = 1010. Sigue teniendo doble cero.
- Complemento a 2 (C2): para negar, se invierten todos los bits y se suma 1. Es el metodo estandar en todos los procesadores modernos. Con n bits: rango [-(2^(n-1)), +(2^(n-1)-1)]. Con 8 bits: [-128, +127]. El cero tiene representacion unica.

Ejemplo C2 con 8 bits: +12 = 00001100. Negar: 11110011 + 1 = 11110100 = -12.

DATO CLAVE: El complemento a 2 es el estandar para representar enteros con signo. Con 8 bits el rango es [-128, +127]; con 16 bits es [-32768, +32767]; con 32 bits es [-2.147.483.648, +2.147.483.647].

3. ARITMETICA BINARIA

Reglas de suma binaria: 0+0=0; 0+1=1; 1+0=1; 1+1=0 (acarreo 1); 1+1+1=1 (acarreo 1).

La resta en complemento a 2 se realiza sumando el complemento a 2 del sustraendo: A - B = A + (-B).

Multiplicacion binaria: similar a la decimal pero mas simple (solo productos de 0 y 1, desplazamientos).

Desbordamiento (overflow): ocurre cuando el resultado de una operacion no cabe en el numero de bits disponible. En suma de numeros con signo, hay overflow si dos positivos dan negativo o dos negativos dan positivo. El flag Overflow (V u OV) del registro de estado indica esta condicion.

DATO CLAVE: El overflow en aritmetica con signo (C2) se detecta cuando los acarreos de entrada y salida del bit de signo difieren. El flag Carry (C) indica desbordamiento en aritmetica sin signo.

4. CODIFICACION DE CARACTERES

Para representar texto en binario se usan tablas de codificacion:

- ASCII (American Standard Code for Information Interchange): 7 bits, 128 caracteres. Incluye letras latinas, digitos, puntuacion y caracteres de control. ASCII extendido usa 8 bits (256 caracteres) con variantes regionales (ISO 8859-1 para Europa occidental, que incluye la e acentuada y la ene).
- Unicode: estandar universal que asigna un punto de codigo unico (code point) a cada caracter de cualquier escritura del mundo. Actualmente mas de 140.000 caracteres. Los puntos de codigo se expresan como U+XXXX.
- UTF-8: codificacion de Unicode de longitud variable (1 a 4 bytes). Compatible con ASCII (los 128 primeros caracteres usan 1 byte). Es la codificacion dominante en Internet y en Linux/macOS. Un caracter espanol como la 'e acentuada' ocupa 2 bytes en UTF-8.
- UTF-16: codificacion de 2 o 4 bytes. Usada internamente por Windows y Java. Menos eficiente que UTF-8 para texto predominantemente latino.
- UTF-32: codificacion de longitud fija, 4 bytes por caracter. Simple pero derrochadora en espacio.

DATO CLAVE: UTF-8 es compatible hacia atras con ASCII: los 128 primeros caracteres (U+0000 a U+007F) se codifican en 1 byte identico a ASCII. Es el estandar de facto en la web (HTML5 obliga UTF-8).

5. REPRESENTACION MULTIMEDIA

Imagenes digitales:
- Imagen de mapa de bits (raster): formada por pixeles. Cada pixel tiene un valor de color. Profundidad de color: 1 bit (B/N), 8 bits (256 colores/escala grises), 24 bits (True Color: 8 bits R, 8 bits G, 8 bits B = 16,7 millones de colores), 32 bits (con canal alfa de transparencia). Formatos: BMP (sin compresion), PNG (compresion sin perdida), JPEG (compresion con perdida), GIF (256 colores, animacion).
- Imagen vectorial: definida por formulas matematicas (curvas de Bezier, lineas). Escalable sin perdida. Formatos: SVG, EPS, AI.
- Resolucion: pixeles por pulgada (PPI/DPI). A mayor resolucion, mayor calidad y mayor tamano de archivo.

Audio digital:
- Muestreo (sampling): se toman muestras de la onda sonora a intervalos regulares. Frecuencia de muestreo: 44.100 Hz (CD), 48.000 Hz (DVD/profesional).
- Cuantificacion: cada muestra se representa con un numero de bits (profundidad de bits). 16 bits (CD), 24 bits (studio).
- Teorema de Nyquist: la frecuencia de muestreo debe ser al menos el doble de la maxima frecuencia a reproducir. Para audio humano (20 Hz - 20 kHz), se necesitan al menos 40 kHz; de ahi los 44,1 kHz del CD.
- Formatos: WAV (sin compresion), MP3 (compresion con perdida, hasta 10:1), FLAC (compresion sin perdida), AAC.

Video digital:
- Secuencia de imagenes (frames) a una tasa de fotogramas (fps): 24 fps (cine), 25 fps (PAL), 30/60 fps (TV/videojuegos).
- Compresion: codecs como H.264/AVC, H.265/HEVC, AV1 reducen el tamano explotando redundancia temporal (diferencias entre frames) y espacial.
- Contenedores: MP4, MKV, AVI agrupan video, audio y subtitulos.

DATO CLAVE: El teorema de Nyquist establece que la frecuencia de muestreo minima debe ser el DOBLE de la frecuencia maxima de la senal. Para audio CD: 44.100 Hz de muestreo para reproducir hasta 22.050 Hz (limite perceptible humano ~20 kHz).

PREGUNTAS TIPO EXAMEN INAP:

1. ?Cual es el rango de representacion de enteros con signo en complemento a 2 usando 8 bits?
   a) [-127, +127]
   b) [-128, +127]  [CORRECTA]
   c) [-128, +128]
   d) [-256, +255]

2. La codificacion UTF-8 tiene la propiedad de ser compatible con:
   a) EBCDIC
   b) ISO 8859-1
   c) ASCII de 7 bits  [CORRECTA]
   d) Unicode UTF-32

3. Para convertir el numero binario 10110111 a hexadecimal, el resultado es:
   a) 0xA7
   b) 0xB7  [CORRECTA]
   c) 0xC3
   d) 0xB6

4. El teorema de Nyquist establece que para digitalizar correctamente una senal se necesita una frecuencia de muestreo:
   a) Igual a la frecuencia maxima de la senal
   b) Al menos el doble de la frecuencia maxima  [CORRECTA]
   c) Al menos diez veces la frecuencia maxima
   d) La mitad de la frecuencia maxima de la senal
"""

Tema.objects.filter(bloque__numero=2, numero=2).update(resumen_estudio=t2)
print("Tema 2.2 actualizado.")

# ============================================================
# TEMA 3: Sistemas Operativos: concepto, funciones, tipos
# ============================================================
t3 = """1. CONCEPTO Y FUNCIONES DEL SISTEMA OPERATIVO

El Sistema Operativo (SO) es el software de base que actua de intermediario entre el hardware y las aplicaciones de usuario. Sus funciones principales son:

- Gestion de procesos: creacion, planificacion y terminacion de procesos.
- Gestion de memoria: asignacion y liberacion de memoria a procesos.
- Gestion de almacenamiento: organizacion de archivos y directorios (sistema de ficheros).
- Gestion de E/S: control de dispositivos mediante drivers.
- Seguridad y proteccion: control de acceso a recursos.
- Interfaz de usuario: CLI (interfaz de linea de comandos) o GUI (interfaz grafica).

DATO CLAVE: El SO proporciona una maquina virtual sobre el hardware. Los programas no acceden directamente al hardware sino a traves del SO mediante llamadas al sistema (system calls).

2. ESTRUCTURA DEL SO: NUCLEO Y LLAMADAS AL SISTEMA

El nucleo (kernel) es la parte central y mas privilegiada del SO. Tipos de kernel:

- Kernel monolitico: todo el SO ejecuta en modo privilegiado (kernel space). Ejemplo: Linux. Ventaja: eficiencia. Desventaja: un fallo puede tumbar todo el sistema.
- Microkernel: solo las funciones esenciales (gestion de procesos, IPC, memoria basica) estan en kernel space. El resto (drivers, sistemas de ficheros) son servicios en espacio de usuario. Ejemplo: Mach, QNX, MINIX. Ventaja: mayor estabilidad y seguridad.
- Kernel hibrido: compromiso entre los dos anteriores. Ejemplo: Windows NT (incluye elementos en kernel por rendimiento), macOS/XNU.

El espacio de direcciones se divide en:
- Espacio de usuario (user space): donde ejecutan las aplicaciones, con privilegios limitados.
- Espacio de kernel (kernel space): donde ejecuta el nucleo, con acceso total al hardware.

Las llamadas al sistema (system calls o syscalls) son la interfaz controlada que permite a los procesos de usuario solicitar servicios al kernel. Ejemplos: open(), read(), write(), fork(), exec(), exit() en POSIX.

DATO CLAVE: La transicion de user space a kernel space se realiza mediante una interrupcion software (trap o syscall). Es un mecanismo de proteccion que evita que las aplicaciones accedan directamente al hardware.

3. GESTION DE PROCESOS

Un proceso es un programa en ejecucion. Cada proceso tiene: espacio de direcciones, codigo, datos, pila y el PCB (Process Control Block) con su estado, registros, ID, prioridad y recursos asignados.

Estados de un proceso:
- Nuevo (New): el proceso esta siendo creado.
- Listo (Ready): en cola, esperando tiempo de CPU.
- En ejecucion (Running): la CPU esta ejecutando sus instrucciones. Solo puede haber uno por nucleo.
- Bloqueado/En espera (Waiting/Blocked): esperando un evento (E/S, semaforo).
- Terminado (Terminated): el proceso ha finalizado.

Algoritmos de planificacion (scheduling):
- FCFS (First Come, First Served): no expropiativo. Simple, pero puede causar el problema del convoy (procesos cortos esperan detras de uno largo). Tiempo de espera promedio alto.
- SJF (Shortest Job First): favorece los procesos mas cortos. Optimo en tiempo de espera promedio, pero requiere conocer los tiempos de ejecucion (irrealista en la practica). Puede causar inanicion (starvation) de procesos largos.
- Round Robin (RR): expropiativo. Cada proceso recibe un quantum de tiempo. Justo. El rendimiento depende del tamano del quantum.
- Por prioridad: se elige el proceso de mayor prioridad. Puede causar inanicion; se resuelve con envejecimiento (aging).
- Multilevel Queue / Multilevel Feedback Queue: varias colas con distintas politicas.

Sincronizacion y condicion de carrera: cuando varios procesos acceden a recursos compartidos, pueden producirse condiciones de carrera. Se resuelven con mecanismos de sincronizacion: mutex (exclusion mutua), semaforos (Dijkstra, operaciones P/wait y V/signal), monitores. El interbloqueo (deadlock) ocurre cuando un conjunto de procesos se bloquean mutuamente esperando recursos. Condiciones de Coffman: exclusion mutua, retencion y espera, no expropiacion, espera circular.

DATO CLAVE: Round Robin es el algoritmo mas usado en SO de proposito general. El quantum tipico es 10-100 ms. Con quantum muy pequeno, el overhead de los cambios de contexto (context switch) degrada el rendimiento.

4. GESTION DE MEMORIA

Tecnicas principales:

- Paginacion: la memoria fisica se divide en marcos (frames) de tamano fijo y la memoria logica del proceso en paginas del mismo tamano. La tabla de paginas mapea paginas a marcos. Elimina la fragmentacion externa pero produce fragmentacion interna (la ultima pagina no siempre se llena). TLB (Translation Lookaside Buffer): cache de traducciones de paginas en la CPU para acelerar el acceso.
- Segmentacion: la memoria del proceso se divide en segmentos logicos de tamano variable (codigo, datos, pila). Refleja la estructura logica del programa. Produce fragmentacion externa.
- Memoria virtual: permite que los procesos usen mas memoria de la fisicamente disponible. Las paginas no activas se almacenan en disco (swap/paginacion en disco). Mecanismo: fallo de pagina (page fault) -> el SO carga la pagina del disco al marco libre. Algoritmos de reemplazo de pagina: FIFO, LRU (Least Recently Used), OPT (optimo, teorico).

DATO CLAVE: La paginacion elimina la fragmentacion EXTERNA (toda la memoria libre es aprovechable) pero produce fragmentacion INTERNA (el ultimo marco de un proceso puede no estar lleno). La segmentacion es lo contrario.

5. SISTEMAS DE FICHEROS

Un sistema de ficheros organiza y gestiona el almacenamiento de datos en dispositivos. Estructuras: directorio raiz, directorios, ficheros, metadatos (nombre, tamano, permisos, fechas, propietario).

- FAT32 (File Allocation Table): usa una tabla FAT para mapear los clusteres del disco. Limite de tamano de archivo: 4 GB. Compatible con todos los SO. Sin journaling.
- NTFS (New Technology File System): sistema de ficheros de Windows desde NT. Soporta ficheros de gran tamano (teoricamente 16 EB), permisos ACL, compresion, cifrado (EFS), journaling (log de transacciones para recuperacion ante fallos). Limite practico de volumen: 256 TB.
- ext4: sistema de ficheros estandar de Linux. Journaling, extents, soporte de volumenes hasta 1 EB y ficheros hasta 16 TB. Mejora a ext3 con mayor rendimiento y menor fragmentacion.
- Journaling: tecnica de registro previo de transacciones. Antes de modificar el sistema de ficheros, se anota la operacion en un journal (registro). Si se produce un fallo, el SO puede recuperar la consistencia releyendo el journal. Tres modos en ext4: writeback (solo metadatos en journal), ordered (datos escritos antes de metadatos), data (datos y metadatos en journal).

DATO CLAVE: FAT32 tiene un limite de 4 GB por fichero (tamano maximo del campo de tamano en la FAT: 32 bits = 2^32 bytes = 4 GB). Este es el motivo por el que pendrives FAT32 no admiten ficheros ISO grandes.

6. GESTION DE ENTRADA/SALIDA

- Drivers (controladores de dispositivo): modulos del SO que conocen las particularidades de cada dispositivo. Implementan una interfaz estandar para el kernel.
- DMA (Direct Memory Access): permite a los dispositivos de E/S transferir datos directamente a/desde RAM sin intervenir la CPU, que solo se ocupa de iniciar y finalizar la transferencia.
- Spooling (Simultaneous Peripheral Operations On-Line): tecnica que usa disco como buffer intermedio para dispositivos lentos (ej: cola de impresion). Permite desacoplar la produccion de datos de la impresion.
- Buffering: uso de memoria intermedia para compensar diferencias de velocidad entre productor y consumidor de datos.
- Interrupciones: mecanismo por el que un dispositivo senaliza a la CPU que ha completado una operacion. La CPU interrumpe su tarea, atiende la interrupcion (ISR - Interrupt Service Routine) y reanuda lo que hacia.

DATO CLAVE: El DMA libera a la CPU durante las transferencias de datos masivas. Sin DMA, la CPU tendria que leer y escribir cada byte individualmente (modo programado o polling), desperdiciando ciclos.

PREGUNTAS TIPO EXAMEN INAP:

1. ?En que estado pasa un proceso cuando solicita una operacion de E/S y debe esperar su completacion?
   a) Listo (Ready)
   b) Terminado (Terminated)
   c) En ejecucion (Running)
   d) Bloqueado (Waiting/Blocked)  [CORRECTA]

2. ?Que tipo de fragmentacion elimina la paginacion respecto a la segmentacion?
   a) Fragmentacion interna
   b) Fragmentacion externa  [CORRECTA]
   c) Fragmentacion logica
   d) Fragmentacion de pagina

3. ?Cual es el limite de tamano de fichero en un sistema de ficheros FAT32?
   a) 2 GB
   b) 4 GB  [CORRECTA]
   c) 8 GB
   d) Sin limite

4. ?Que tecnica permite a los dispositivos transferir datos a la RAM sin intervencion activa de la CPU?
   a) Spooling
   b) Buffering
   c) DMA (Direct Memory Access)  [CORRECTA]
   d) Polling
"""

Tema.objects.filter(bloque__numero=2, numero=3).update(resumen_estudio=t3)
print("Tema 2.3 actualizado.")

# ============================================================
# TEMA 4: Sistemas Operativos Windows y Linux
# ============================================================
t4 = """1. ARQUITECTURA DE WINDOWS

Microsoft Windows usa un kernel hibrido (Windows NT). La arquitectura se divide en:

- Modo kernel: HAL (Hardware Abstraction Layer), kernel de NT, ejecutivos (gestion de objetos, memoria, E/S, seguridad) y drivers.
- Modo usuario: subsistemas de entorno (Win32/64, POSIX legacy), procesos de sistema (lsass, services.exe) y aplicaciones.

Versiones clave en el ambito empresarial: Windows Server 2019, Windows Server 2022, Windows 11 (cliente).

DATO CLAVE: La HAL (Hardware Abstraction Layer) de Windows aisla el kernel del hardware especifico, facilitando la portabilidad del SO a distintas plataformas de hardware.

2. ACTIVE DIRECTORY Y GPO

Active Directory (AD) es el servicio de directorio de Microsoft para redes Windows. Proporciona autenticacion (Kerberos), autorizacion y administracion centralizada.

Componentes de AD:
- Dominio: unidad administrativa basica. Contiene objetos (usuarios, equipos, grupos).
- Unidad Organizativa (OU): contenedor dentro del dominio para organizar objetos y aplicar politicas.
- Arbol: conjunto de dominios con un espacio de nombres DNS comun y contiguo.
- Bosque (Forest): coleccion de arboles con confianza transitiva entre dominios.
- Controlador de Dominio (DC): servidor con AD DS instalado. Autentica a los usuarios.
- Catalogo Global (GC): indice de todos los objetos del bosque para busquedas rapidas.

GPO (Group Policy Objects): objetos que contienen configuraciones de politicas aplicadas a usuarios y/o equipos dentro de un dominio o OU. Se gestionan con la Consola de Administracion de Directivas de Grupo (GPMC). Las GPO se aplican en orden: Local -> Sitio -> Dominio -> OU (LSDOU), con las mas especificas ganando precedencia.

DATO CLAVE: El protocolo de autenticacion estandar en Active Directory es Kerberos (puerto 88). Para equipos legacy o fuera del dominio se usa NTLM. Kerberos usa tickets (TGT emitido por el KDC) para autenticacion.

3. POWERSHELL

PowerShell es la shell y lenguaje de scripting de Microsoft, basada en el framework .NET. Trabaja con objetos (no solo texto como bash). Los comandos se llaman cmdlets con formato Verbo-Sustantivo.

Cmdlets esenciales:
- Get-Process, Stop-Process, Start-Process: gestion de procesos.
- Get-Service, Start-Service, Stop-Service, Restart-Service: gestion de servicios.
- Get-ADUser, New-ADUser, Set-ADUser, Remove-ADUser: gestion de usuarios en AD (modulo ActiveDirectory).
- Get-EventLog / Get-WinEvent: consulta de registros de eventos.
- Get-Item, Set-Item, Copy-Item, Remove-Item: gestion del sistema de ficheros.
- Invoke-Command: ejecutar comandos en equipos remotos (WinRM).

DATO CLAVE: PowerShell usa el pipeline (|) para pasar OBJETOS entre cmdlets, a diferencia de bash que pasa texto plano. Esto permite manipular propiedades directamente: Get-Process | Where-Object {$_.CPU -gt 100} | Select-Object Name, CPU.

4. ARQUITECTURA DE LINUX

Linux es un kernel monolitico modular (permite cargar/descargar modulos en tiempo real sin reiniciar). Creado por Linus Torvalds en 1991, licencia GPL. Las distribuciones (distros) empaquetan el kernel con software adicional.

Principales familias de distribuciones:
- Debian: base de Ubuntu, Linux Mint. Gestor de paquetes APT/dpkg. Formato .deb.
- Red Hat (RHEL): base de CentOS, Fedora, Rocky Linux, AlmaLinux. Gestor de paquetes YUM/DNF. Formato .rpm. RHEL es la referencia en entornos empresariales y la AGE.
- SUSE (SLES): orientada a empresa. Gestor de paquetes ZYpper/RPM.
- Arch Linux: rolling release, AUR. Para usuarios avanzados.

Estructura de directorios (FHS - Filesystem Hierarchy Standard):
- /: raiz del sistema.
- /bin, /usr/bin: binarios de usuario esenciales.
- /sbin, /usr/sbin: binarios de administracion del sistema.
- /etc: ficheros de configuracion del sistema.
- /var: datos variables (logs en /var/log, colas de impresion, bases de datos).
- /home: directorios personales de usuarios.
- /tmp: ficheros temporales.
- /proc: sistema de ficheros virtual con informacion del kernel y procesos.
- /dev: ficheros de dispositivo.
- /mnt, /media: puntos de montaje.

DATO CLAVE: En Linux, TODO es un fichero: los dispositivos (/dev/sda), los procesos (/proc/PID), los sockets, las tuberias (pipes). Este principio de diseno unifica el acceso a recursos mediante la misma interfaz de E/S.

5. GESTION DE USUARIOS Y PERMISOS

Linux usa un modelo de permisos basado en usuario (owner), grupo (group) y otros (others). Cada fichero tiene permisos de lectura (r=4), escritura (w=2) y ejecucion (x=1) para cada categoria.

- chmod: cambia los permisos. Formato simbolico: chmod u+x fichero. Formato octal: chmod 755 fichero (rwxr-xr-x).
- chown: cambia propietario y/o grupo. chown usuario:grupo fichero.
- chgrp: cambia solo el grupo.
- sudo: ejecuta un comando con privilegios de root.
- Ficheros clave: /etc/passwd (usuarios), /etc/shadow (contrasenas hasheadas), /etc/group (grupos).

Permisos especiales: SUID (Set User ID, bit 4000): el ejecutable corre con los permisos del propietario; SGID (bit 2000): hereda el grupo del directorio; Sticky bit (bit 1000): solo el propietario puede borrar sus ficheros en un directorio compartido (ejemplo: /tmp).

Windows usa ACLs (Access Control Lists) gestionadas con icacls o desde las propiedades de seguridad del fichero. Cada entrada en la ACL (ACE, Access Control Entry) especifica un usuario/grupo y los permisos (leer, escribir, ejecutar, control total, etc.).

DATO CLAVE: chmod 755 otorga: propietario=rwx (7), grupo=r-x (5), otros=r-x (5). chmod 644 es el tipico para ficheros de texto: propietario=rw- (6), grupo=r-- (4), otros=r-- (4).

6. SERVICIOS DE RED Y COPIAS DE SEGURIDAD

Servicios principales en Windows Server:
- DNS: resolucion de nombres. Servicio DNS de Windows Server. Configuracion en /etc/hosts o DNS Manager.
- DHCP: asignacion dinamica de IPs. Consola DHCP Manager.
- IIS (Internet Information Services): servidor web de Microsoft. Soporte HTTP/HTTPS, ASP.NET, FTP.
- Active Directory Certificate Services (AD CS): autoridad de certificacion.

Servicios equivalentes en Linux:
- DNS: bind9 (named). Configuracion en /etc/named.conf y zonas en /var/named/.
- DHCP: isc-dhcp-server (dhcpd). Configuracion en /etc/dhcp/dhcpd.conf.
- Servidor web: Apache (httpd) o Nginx. Configuracion en /etc/apache2/ o /etc/nginx/.
- SSH: servidor OpenSSH (sshd). Configuracion en /etc/ssh/sshd_config.

Copias de seguridad:
- Completa (full): copia todos los datos. Mas lenta y ocupa mas espacio.
- Incremental: copia solo los cambios desde la ultima copia (completa o incremental). Rapida, pero restaurar requiere la completa + todas las incrementales.
- Diferencial: copia los cambios desde la ultima copia COMPLETA. Restauracion mas rapida que incremental (solo completa + ultima diferencial).
- Herramientas Windows: Windows Server Backup, vssadmin (Volume Shadow Copy), robocopy.
- Herramientas Linux: rsync, tar, Bacula, Amanda.

DATO CLAVE: La estrategia de backup 3-2-1: 3 copias de los datos, en 2 tipos de soporte diferentes, con 1 copia en ubicacion externa (offsite). Es el estandar recomendado por organismos de seguridad como el CCN-CERT.

PREGUNTAS TIPO EXAMEN INAP:

1. ?En que orden se aplican las GPO de Active Directory, de menos a mas especifica?
   a) Dominio -> Sitio -> OU -> Local
   b) Local -> Sitio -> Dominio -> OU  [CORRECTA]
   c) OU -> Dominio -> Sitio -> Local
   d) Local -> Dominio -> Sitio -> OU

2. ?Que protocolo usa Active Directory para la autenticacion de usuarios en un dominio Windows?
   a) NTLM
   b) LDAP
   c) Kerberos  [CORRECTA]
   d) RADIUS

3. En Linux, ?que hace el comando chmod 644 sobre un fichero?
   a) rwxr--r--
   b) rw-rw-rw-
   c) rw-r--r--  [CORRECTA]
   d) rwxrwxr-x

4. En una estrategia de backups, ?que tipo de copia contiene solo los cambios desde la ultima copia COMPLETA?
   a) Incremental
   b) Diferencial  [CORRECTA]
   c) Espejo (mirror)
   d) Snapshot
"""

Tema.objects.filter(bloque__numero=2, numero=4).update(resumen_estudio=t4)
print("Tema 2.4 actualizado.")

# ============================================================
# TEMA 5: Arquitectura de redes: modelo OSI y TCP/IP
# ============================================================
t5 = """1. NECESIDAD DE UN MODELO EN CAPAS

Para que sistemas heterogeneos puedan comunicarse, es necesario estandarizar los protocolos de comunicacion. El modelo en capas descompone el problema de la comunicacion en subproblemas independientes, cada uno resuelto por una capa que ofrece servicios a la capa superior y se apoya en la capa inferior.

2. MODELO OSI (Open Systems Interconnection)

El modelo OSI de ISO (1984) define 7 capas. Es un modelo de referencia conceptual, no una implementacion:

- Capa 7 - APLICACION: interfaz entre las aplicaciones y la red. Protocolos: HTTP, HTTPS, FTP, SMTP, DNS, DHCP, SNMP, Telnet, SSH.
- Capa 6 - PRESENTACION: traduccion de formatos de datos, cifrado/descifrado, compresion. Ejemplos: SSL/TLS (negociacion), JPEG, MPEG, ASCII/EBCDIC.
- Capa 5 - SESION: establece, mantiene y finaliza sesiones de comunicacion entre aplicaciones. Protocolos: NetBIOS, RPC, SIP (parcialmente).
- Capa 4 - TRANSPORTE: comunicacion extremo a extremo, control de flujo y errores. Protocolos: TCP (orientado a conexion, fiable), UDP (no orientado a conexion, rapido). Unidad: segmento (TCP) / datagrama (UDP).
- Capa 3 - RED: enrutamiento y direccionamiento logico. Protocolos: IP (IPv4, IPv6), ICMP, IGMP, ARP (debatible, algunos modelos lo ubican en capa 2). Equipos: router. Unidad: paquete.
- Capa 2 - ENLACE DE DATOS: transmision fiable entre nodos adyacentes, control de acceso al medio (MAC). Protocolos: Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11), PPP. Equipos: switch, bridge. Unidad: trama (frame).
- Capa 1 - FISICA: transmision de bits por el medio fisico. Voltajes, frecuencias, conectores, cables. Equipos: hub, repetidor. Unidad: bit.

Mnemotecnico ascendente (de capa 1 a 7): "Fisicos De Red Transportan Sesiones Para Aplicar".

DATO CLAVE: Las capas 1-4 son capas de transporte (orientadas a la red). Las capas 5-7 son capas de aplicacion (orientadas al usuario). En la practica, TCP/IP fusiona las capas 5, 6 y 7 del OSI en una sola capa de aplicacion.

3. PILA TCP/IP (DoD o Internet Model)

La pila TCP/IP (desarrollada por DARPA) es el modelo real de Internet, con 4 capas:

- Capa de APLICACION: equivale a las capas 5+6+7 del OSI. Protocolos: HTTP/HTTPS, DNS, DHCP, FTP, SMTP, POP3, IMAP, SSH, SNMP.
- Capa de TRANSPORTE: equivale a la capa 4 OSI. TCP y UDP.
- Capa de INTERNET (Red): equivale a la capa 3 OSI. IP (IPv4, IPv6), ICMP, ARP.
- Capa de ACCESO A LA RED (Enlace): equivale a las capas 1+2 OSI. Ethernet, Wi-Fi, etc.

Comparativa OSI vs TCP/IP: OSI tiene 7 capas (modelo teorico); TCP/IP tiene 4 capas (modelo practico). Las capas de sesion y presentacion del OSI estan integradas en la capa de aplicacion de TCP/IP.

DATO CLAVE: El modelo TCP/IP NO tiene capas de sesion ni de presentacion separadas. Estas funciones las implementan las propias aplicaciones o los protocolos de aplicacion (ej: TLS maneja la presentacion/cifrado).

4. CAPA DE RED: IP, ICMP, ARP Y ENRUTAMIENTO

El protocolo IP (Internet Protocol) proporciona un servicio de entrega de paquetes no orientado a conexion y sin garantias (best-effort). Cada paquete se enruta de forma independiente.

ICMP (Internet Control Message Protocol): protocolo de control y diagnostico. Mensajes: Echo Request/Reply (ping), Destination Unreachable, Time Exceeded (TTL agotado, usado por traceroute).

ARP (Address Resolution Protocol): resuelve direcciones IP en direcciones MAC dentro de una red local. Cuando un host quiere enviar a una IP local, hace broadcast ARP pidiendo la MAC correspondiente.

Protocolos de enrutamiento:
- RIP (Routing Information Protocol): protocolo de vector de distancia. Metrica: numero de saltos (hop count). Maximo 15 saltos (16 = infinito/inalcanzable). RIPv2 soporta CIDR. Simple pero poco escalable.
- OSPF (Open Shortest Path First): protocolo de estado de enlace. Metrica: coste (basado en ancho de banda). Usa el algoritmo de Dijkstra. Apropiado para redes grandes. Sin limite de saltos.
- BGP (Border Gateway Protocol): protocolo de enrutamiento entre sistemas autonomos (AS) de Internet. Protocolo de vector de ruta. Es el protocolo de enrutamiento de Internet.

DATO CLAVE: RIP usa como metrica el numero de SALTOS y tiene un maximo de 15. OSPF usa el COSTE (inverso del ancho de banda) y el algoritmo SPF de Dijkstra. BGP es el protocolo de enrutamiento de Internet entre proveedores (ISPs).

5. CAPA DE TRANSPORTE: TCP Y UDP

TCP (Transmission Control Protocol):
- Orientado a conexion: establece conexion mediante el handshake de 3 vias (SYN -> SYN-ACK -> ACK) antes de enviar datos.
- Fiable: garantiza la entrega ordenada y sin duplicados mediante numeros de secuencia y acuses de recibo (ACK).
- Control de flujo: mecanismo de ventana deslizante (sliding window) para no saturar al receptor.
- Control de congestion: algoritmos Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery.
- Cierre de conexion: handshake de 4 vias (FIN, FIN-ACK, FIN, FIN-ACK).

UDP (User Datagram Protocol):
- Sin conexion: no establece conexion previa. Menor latencia.
- No fiable: no garantiza entrega, orden ni ausencia de duplicados.
- Sin control de flujo ni congestion.
- Usos: streaming de video/audio (toleran perdidas), DNS (consultas cortas), DHCP, VoIP, videojuegos en tiempo real.

DATO CLAVE: TCP garantiza entrega FIABLE y ORDENADA mediante ACKs y numeros de secuencia, al coste de mayor latencia. UDP es rapido y ligero pero sin garantias. El three-way handshake TCP es: SYN (cliente) -> SYN+ACK (servidor) -> ACK (cliente).

6. CAPA DE APLICACION: PROTOCOLOS PRINCIPALES

Protocolos y puertos que hay que memorizar:

- HTTP: puerto 80 (TCP). Protocolo de transferencia de hipertexto. Sin cifrado.
- HTTPS: puerto 443 (TCP). HTTP sobre TLS/SSL. Cifrado asimetrico para el handshake, simetrico para los datos.
- DNS: puerto 53 (UDP y TCP). Resolucion de nombres de dominio.
- DHCP: puertos 67 (servidor) y 68 (cliente) UDP. Asignacion dinamica de IPs.
- FTP: puertos 20 (datos) y 21 (control) TCP. Transferencia de ficheros. Sin cifrado.
- SFTP: puerto 22 TCP. FTP seguro sobre SSH.
- SMTP: puerto 25 (entre servidores) / 587 (cliente-servidor con autenticacion) TCP. Envio de correo.
- POP3: puerto 110 (143 IMAP) TCP. Recepcion de correo.
- SSH: puerto 22 TCP. Acceso remoto seguro (cifrado).
- Telnet: puerto 23 TCP. Acceso remoto sin cifrado (obsoleto).
- SNMP: puerto 161 UDP. Monitorizacion y gestion de red.
- RDP: puerto 3389 TCP. Remote Desktop Protocol (Windows).

DATO CLAVE: Puertos fundamentales para el examen: HTTP=80, HTTPS=443, SSH=22, FTP=21/20, SMTP=25, DNS=53, DHCP=67/68, RDP=3389, Telnet=23.

PREGUNTAS TIPO EXAMEN INAP:

1. En el modelo OSI, ?en que capa opera un switch (conmutador)?
   a) Capa 1 (Fisica)
   b) Capa 2 (Enlace de datos)  [CORRECTA]
   c) Capa 3 (Red)
   d) Capa 4 (Transporte)

2. ?Cual es la secuencia correcta del handshake de tres vias de TCP?
   a) SYN -> ACK -> SYN-ACK
   b) SYN -> SYN-ACK -> ACK  [CORRECTA]
   c) ACK -> SYN -> SYN-ACK
   d) SYN-ACK -> SYN -> ACK

3. ?Que protocolo de enrutamiento usa el algoritmo de Dijkstra y la metrica de coste basada en ancho de banda?
   a) RIP
   b) BGP
   c) OSPF  [CORRECTA]
   d) EIGRP

4. El protocolo UDP se usa preferentemente en aplicaciones de streaming porque:
   a) Garantiza la entrega ordenada de los paquetes
   b) Tiene menor latencia al no requerir conexion previa ni retransmisiones  [CORRECTA]
   c) Implementa control de congestion avanzado
   d) Cifra los datos en la capa de transporte
"""

Tema.objects.filter(bloque__numero=2, numero=5).update(resumen_estudio=t5)
print("Tema 2.5 actualizado.")

# ============================================================
# TEMA 6: Direccionamiento IPv4/IPv6, subnetting y CIDR
# ============================================================
t6 = """1. DIRECCIONAMIENTO IPv4

Una direccion IPv4 es un numero de 32 bits representado en notacion decimal punteada: cuatro octetos separados por puntos (ej: 192.168.1.100). Cada octeto toma valores de 0 a 255.

Clases de direcciones IPv4 (sistema clasico, anterior al CIDR):
- Clase A: primer bit = 0. Rango: 1.0.0.0 - 126.255.255.255. Mascara: /8 (255.0.0.0). 126 redes, ~16 millones de hosts por red.
- Clase B: primeros bits = 10. Rango: 128.0.0.0 - 191.255.255.255. Mascara: /16 (255.255.0.0). 16.384 redes, ~65.534 hosts.
- Clase C: primeros bits = 110. Rango: 192.0.0.0 - 223.255.255.255. Mascara: /24 (255.255.255.0). ~2 millones de redes, 254 hosts por red.
- Clase D: primeros bits = 1110. Rango: 224.0.0.0 - 239.255.255.255. Multicast.
- Clase E: reservada para investigacion. 240.0.0.0 - 255.255.255.255.

Direcciones especiales:
- 127.0.0.0/8: loopback (127.0.0.1 = localhost).
- 0.0.0.0: host actual (en contexto de routing: cualquier red).
- 255.255.255.255: broadcast limitado.
- Direcciones privadas (RFC 1918, no enrutables en Internet): 10.0.0.0/8, 172.16.0.0/12 (172.16-31.x.x), 192.168.0.0/16.
- 169.254.0.0/16: APIPA (Automatic Private IP Addressing), cuando DHCP falla.

DATO CLAVE: Las direcciones privadas RFC 1918 son: 10.0.0.0/8 (Clase A), 172.16.0.0/12 (Clase B), 192.168.0.0/16 (Clase C). No son enrutables en Internet y requieren NAT para salir.

2. SUBNETTING Y CIDR

El subnetting divide una red en subredes mas pequenas tomando bits del campo de host para crear el campo de subred.

CIDR (Classless Inter-Domain Routing, RFC 1519): elimina el sistema de clases. La mascara de red se expresa como prefijo /n, donde n es el numero de bits a 1 en la mascara.

Formulas clave:
- Numero de subredes = 2^s (donde s = bits tomados del campo de host).
- Numero de hosts utilizables por subred = 2^h - 2 (donde h = bits de host restantes; se restan 2 por la direccion de red y el broadcast).
- Ejemplo: Red 192.168.1.0/24, dividir en 4 subredes. Se necesitan 2 bits (2^2=4). Nueva mascara: /26 (255.255.255.192). Hosts por subred: 2^6 - 2 = 62.

Subredes resultantes de 192.168.1.0/26:
- 192.168.1.0/26: red .0, broadcast .63, hosts .1-.62.
- 192.168.1.64/26: red .64, broadcast .127, hosts .65-.126.
- 192.168.1.128/26: red .128, broadcast .191, hosts .129-.190.
- 192.168.1.192/26: red .192, broadcast .255, hosts .193-.254.

DATO CLAVE: La formula de hosts utilizables es 2^h - 2. Se restan 2: la primera direccion es la direccion de RED (identificador de subred) y la ultima es el BROADCAST. Ninguna se puede asignar a un host.

3. NAT (Network Address Translation)

NAT traduce direcciones IP en los paquetes al pasar por un router, permitiendo que multiples dispositivos con IPs privadas compartan una unica IP publica.

Tipos de NAT:
- NAT estatico (SNAT, Static NAT): mapeo fijo de una IP privada a una IP publica. Util para servidores internos accesibles desde Internet.
- NAT dinamico: el router tiene un pool de IPs publicas y asigna una a cada conexion saliente dinamicamente.
- PAT (Port Address Translation) / NAT con sobrecarga (Overload) / Masquerading: multiples IPs privadas se mapean a una sola IP publica usando distintos puertos. Es el tipo de NAT mas comun en routers domesticos y empresariales. Permite que miles de dispositivos compartan una IP publica.
- DNAT (Destination NAT): reescribe la IP de destino. Se usa para redireccion de puertos (port forwarding): permite que trafico externo llegue a servidores internos.

DATO CLAVE: PAT (Port Address Translation) es la forma mas comun de NAT. Usa combinaciones IP:Puerto para distinguir las conexiones de multiples clientes internos que comparten una sola IP publica.

4. DIRECCIONAMIENTO IPv6

IPv6 fue desarrollado para solucionar el agotamiento de direcciones IPv4. Sus caracteristicas:

- Longitud: 128 bits (frente a 32 bits de IPv4). 2^128 = ~3,4 x 10^38 direcciones.
- Notacion: 8 grupos de 4 digitos hexadecimales separados por dos puntos. Ejemplo: 2001:0db8:85a3:0000:0000:8a2e:0370:7334.
- Simplificacion: se puede omitir los ceros a la izquierda en cada grupo y reemplazar uno o mas grupos de 0000 consecutivos por :: (solo una vez por direccion).
- Sin broadcast: usa multicast y anycast en su lugar.
- Sin NAT obligatorio (por diseno): cada dispositivo tiene IP publica unica.
- Autoconfiguacion: SLAAC (Stateless Address Autoconfiguration) permite a los dispositivos configurar su propia IP IPv6 basandose en el prefijo anunciado por el router y su MAC (EUI-64).

Tipos de direcciones IPv6:
- Unicast global: equivalente a IPv4 publica. Prefijo: 2000::/3.
- Unicast local de enlace (Link-local): automaticamente configurada, valida solo en el enlace local. Prefijo: FE80::/10.
- Unicast local unica (Unique Local): equivalente a IPv4 privada. Prefijo: FC00::/7.
- Multicast: un paquete a multiples destinos de un grupo. Prefijo: FF00::/8.
- Anycast: misma direccion en multiples nodos; el paquete se entrega al mas cercano.
- Loopback: ::1 (equivalente a 127.0.0.1 en IPv4).

Coexistencia IPv4/IPv6: mecanismos de transicion:
- Doble pila (Dual Stack): el dispositivo tiene simultaneamente una IP IPv4 y una IPv6.
- Tunneling: encapsula paquetes IPv6 dentro de paquetes IPv4 (6to4, Teredo, ISATAP).
- Traduccion (NAT64/DNS64): permite a hosts IPv6 comunicarse con servidores IPv4.

DATO CLAVE: La direccion de loopback IPv6 es ::1 (equivalente a 127.0.0.1). La direccion de link-local comienza siempre por FE80::/10 y se configura automaticamente en todas las interfaces con IPv6.

5. EQUIPOS DE INTERCONEXION

- Hub (concentrador): dispositivo de capa 1. Retransmite todos los bits recibidos por todos los puertos (broadcast electrico). Dominio de colision unico. Obsoleto.
- Switch (conmutador): dispositivo de capa 2. Aprende las MACs de los dispositivos por puerto (tabla CAM). Reenvio selectivo de tramas. Cada puerto es un dominio de colision separado.
- Router (enrutador): dispositivo de capa 3. Conecta redes distintas. Usa tablas de enrutamiento para reenviar paquetes basandose en la IP destino.
- Firewall: dispositivo de seguridad (capa 3-7 segun el tipo). Filtra el trafico segun politicas. Puede ser hardware o software.
- Punto de Acceso Wi-Fi (AP, Access Point): permite a dispositivos inalambricos conectarse a la red cableada. Opera en capa 2. Un AP puede ser modo bridge (transparente) o modo router (con NAT).
- Gateway: dispositivo que conecta redes con protocolos distintos. Puede operar en cualquier capa.
- Proxy: intermediario entre clientes y servidores, puede cachear contenido y filtrar.

DATO CLAVE: Un switch divide los dominios de COLISION (cada puerto es un dominio), pero todos los puertos del switch forman parte del mismo dominio de BROADCAST. Un router separa tanto los dominios de colision como los de broadcast.

PREGUNTAS TIPO EXAMEN INAP:

1. ?Cuantos hosts utilizables tiene una subred /26?
   a) 64
   b) 62  [CORRECTA]
   c) 30
   d) 126

2. ?Cual de las siguientes es una direccion IP privada segun RFC 1918?
   a) 172.32.0.1
   b) 192.169.0.1
   c) 172.20.0.1  [CORRECTA]
   d) 126.0.0.1

3. ?Cual es la longitud en bits de una direccion IPv6?
   a) 32 bits
   b) 64 bits
   c) 128 bits  [CORRECTA]
   d) 256 bits

4. ?Que tipo de NAT permite que multiples hosts con IPs privadas compartan una unica IP publica usando diferentes puertos?
   a) NAT estatico
   b) NAT dinamico
   c) PAT (Port Address Translation)  [CORRECTA]
   d) DNAT (Destination NAT)
"""

Tema.objects.filter(bloque__numero=2, numero=6).update(resumen_estudio=t6)
print("Tema 2.6 actualizado.")

# ============================================================
# TEMA 7: Tecnologias y estandares LAN/WLAN
# ============================================================
t7 = """1. ETHERNET (IEEE 802.3)

Ethernet es el estandar dominante para redes de area local (LAN) cableadas, definido por IEEE 802.3. Originalmente desarrollado por Xerox/DEC/Intel en la decada de 1970 y estandarizado en 1983.

Mecanismo de acceso al medio: CSMA/CD (Carrier Sense Multiple Access with Collision Detection):
- Carrier Sense: antes de transmitir, el nodo escucha el medio para saber si esta libre.
- Multiple Access: todos los nodos comparten el mismo medio.
- Collision Detection: si dos nodos transmiten simultaneamente, detectan la colision y paran. Emiten una senal de atasco (jam signal) y esperan un tiempo aleatorio antes de reintentar (algoritmo de backoff exponencial binario). CSMA/CD solo aplica a Ethernet HALF-DUPLEX. El Ethernet moderno con switches es full-duplex y no tiene colisiones.

Trama Ethernet II (formato dominante):
- Preambulo: 7 bytes de sincronizacion (10101010...) + SFD (1 byte: 10101011).
- MAC Destino: 6 bytes.
- MAC Origen: 6 bytes.
- EtherType/Longitud: 2 bytes. Indica el protocolo encapsulado (0x0800 = IPv4, 0x86DD = IPv6, 0x0806 = ARP).
- Datos (payload): 46-1500 bytes.
- FCS (Frame Check Sequence): 4 bytes. CRC para deteccion de errores.

Direccion MAC: identificador unico de 48 bits grabado en la tarjeta de red. Se representa en hexadecimal: XX:XX:XX:XX:XX:XX. Los primeros 3 bytes son el OUI (identificador del fabricante).

Categorias de cable UTP (par trenzado sin apantallar):
- Cat5e: hasta 1 Gbps a 100 metros. El mas extendido.
- Cat6: hasta 10 Gbps a 55 metros (10 Gbps a 100m con Cat6A). Mayor diametro y separacion entre pares.
- Cat6A (Augmented): hasta 10 Gbps a 100 metros. Apantallamiento mejorado.
- Cat7/8: para centros de datos, velocidades de 10-40 Gbps.

Velocidades Ethernet: 10 Mbps (10Base-T), 100 Mbps (Fast Ethernet, 100Base-TX), 1 Gbps (GbE, 1000Base-T), 10 Gbps (10GbE), 25/40/100 Gbps en centros de datos.

DATO CLAVE: La MTU (Maximum Transmission Unit) de Ethernet es 1500 bytes (tamano maximo del campo de datos de la trama). Con Jumbo Frames (9000 bytes), disponible en switches de centros de datos.

2. WI-FI (IEEE 802.11)

Wi-Fi es el nombre comercial del estandar IEEE 802.11 para redes inalambricas de area local (WLAN). Gestionado por la Wi-Fi Alliance.

Evolucion de los estandares:
- 802.11b (1999): 2,4 GHz, hasta 11 Mbps. Obsoleto.
- 802.11a (1999): 5 GHz, hasta 54 Mbps. Menos interferencias que 2,4 GHz.
- 802.11g (2003): 2,4 GHz, hasta 54 Mbps. Compatible con 11b.
- 802.11n (2009) / Wi-Fi 4: 2,4 y 5 GHz, hasta 600 Mbps. Introduce MIMO (Multiple Input Multiple Output).
- 802.11ac (2013) / Wi-Fi 5: solo 5 GHz, hasta 6,9 Gbps. MU-MIMO, canales de 80/160 MHz, beamforming.
- 802.11ax (2019) / Wi-Fi 6: 2,4 y 5 GHz (y 6 GHz en Wi-Fi 6E), hasta 9,6 Gbps. OFDMA, BSS Coloring, mejora en entornos densos.
- Wi-Fi 7 (802.11be): 2,4/5/6 GHz, hasta 46 Gbps. Multi-Link Operation (MLO).

Mecanismo de acceso: CSMA/CA (Collision Avoidance, en lugar de CD):
- En entornos inalambricos no se puede detectar colisiones durante la transmision.
- El nodo espera un tiempo aleatorio (backoff) y si el canal sigue libre, transmite.
- Opcionalmente usa RTS/CTS (Request To Send / Clear To Send) para reservar el canal.
- Problema del nodo oculto: dos nodos que no se "ven" entre si pero si al AP pueden colisionar. RTS/CTS lo mitiga.

DATO CLAVE: Ethernet usa CSMA/CD (deteccion de colision); Wi-Fi usa CSMA/CA (evitacion de colision) porque en el medio inalambrico no es posible detectar colisiones mientras se transmite.

3. SEGURIDAD EN REDES INALAMBRICAS

- WEP (Wired Equivalent Privacy, 1997): primer protocolo de seguridad Wi-Fi. Usa RC4 con claves de 64/128 bits. Completamente roto desde 2001. OBSOLETO Y PROHIBIDO.
- WPA (Wi-Fi Protected Access, 2003): solucion de emergencia. Usa TKIP (Temporal Key Integrity Protocol) con RC4, pero con claves dinamicas. Mejorado pero con vulnerabilidades. OBSOLETO.
- WPA2 (2004): estandar actual de facto durante muchos anos. Usa CCMP (Counter Mode CBC-MAC Protocol) basado en AES-128. Dos modos: Personal (PSK, clave precompartida) y Enterprise (autenticacion 802.1X con servidor RADIUS).
- WPA3 (2018): mejora de WPA2. Usa SAE (Simultaneous Authentication of Equals) para reemplazar PSK, resistente a ataques de diccionario offline. Cifrado de 192 bits en modo Enterprise. Forward Secrecy perfecto.

Vulnerabilidades notables: KRACK (2017, ataque a WPA2 en el handshake de 4 vias), PMKID (ataque offline a WPA2-PSK), redes abiertas (sin cifrado). Para redes empresariales se recomienda WPA2/WPA3-Enterprise con 802.1X.

DATO CLAVE: WPA2 con CCMP/AES es el minimo recomendado. WPA3 es el estandar actual. WEP esta completamente roto y no debe usarse jamas. El CCND del CCN-CERT categoriza WEP y WPA-TKIP como inaceptables.

4. SWITCHES: FUNCIONAMIENTO Y TECNOLOGIAS

El switch (conmutador) opera en capa 2 (Enlace de datos). Su funcionamiento:

1. Aprendizaje: cuando recibe una trama, registra la MAC de origen y el puerto en la tabla CAM (Content Addressable Memory).
2. Forwarding: si la MAC de destino esta en la tabla CAM, reenvio la trama solo por el puerto correspondiente (unicast).
3. Flooding: si la MAC de destino es desconocida, retransmite la trama por todos los puertos excepto el de origen (como un hub, pero solo hasta aprender la MAC).
4. Filtrado: no retransmite tramas al mismo segmento de origen.

VLANs (Virtual LANs, IEEE 802.1Q):
- Permiten segmentar logicamente una red fisica en varias redes virtuales aisladas.
- El etiquetado 802.1Q agrega un campo de 4 bytes a la trama Ethernet con el VLAN ID (12 bits, valores 1-4094).
- Puertos de acceso (access): conectados a dispositivos finales, pertenecen a una VLAN.
- Puertos troncales (trunk): entre switches o switch-router, transportan tramas de multiples VLANs etiquetadas.
- Inter-VLAN routing: para que dos VLANs se comuniquen se necesita un router (o switch de capa 3).

STP (Spanning Tree Protocol, IEEE 802.1D):
- Evita los bucles en redes con enlaces redundantes. Un bucle de capa 2 causaria tormentas de broadcast que colapsarian la red.
- Elige un switch raiz (Root Bridge) con el menor Bridge ID (prioridad + MAC).
- Bloquea los puertos redundantes que causarian bucles, manteniendo una topologia de arbol sin ciclos.
- Variantes: RSTP (Rapid STP, 802.1w, convergencia mas rapida), MSTP (Multiple STP, 802.1s, una instancia STP por VLAN).

DATO CLAVE: STP (Spanning Tree Protocol) evita los bucles de capa 2 bloqueando puertos redundantes. Sin STP, un bucle provoca una tormenta de broadcast que satura el switch y tumba la red.

PREGUNTAS TIPO EXAMEN INAP:

1. ?Que estandar IEEE define las redes Wi-Fi de la generacion Wi-Fi 6?
   a) IEEE 802.11ac
   b) IEEE 802.11n
   c) IEEE 802.11ax  [CORRECTA]
   d) IEEE 802.11be

2. ?Que protocolo de seguridad Wi-Fi usa CCMP basado en AES-128?
   a) WEP
   b) WPA-TKIP
   c) WPA2  [CORRECTA]
   d) WPA3-SAE

3. ?Que funcion tiene el protocolo STP (Spanning Tree Protocol) en una red con switches?
   a) Asignar IPs dinamicamente a los dispositivos de la red
   b) Evitar bucles en la capa de enlace bloqueando puertos redundantes  [CORRECTA]
   c) Segmentar la red en VLANs independientes
   d) Cifrar el trafico entre switches en una red troncal

4. ?Cual es la MTU (Maximum Transmission Unit) estandar de Ethernet?
   a) 576 bytes
   b) 1024 bytes
   c) 1500 bytes  [CORRECTA]
   d) 9000 bytes
"""

Tema.objects.filter(bloque__numero=2, numero=7).update(resumen_estudio=t7)
print("Tema 2.7 actualizado.")

# ============================================================
# TEMA 8: Seguridad en redes: cortafuegos, VPN, IDS/IPS
# ============================================================
t8 = """1. CORTAFUEGOS (FIREWALL)

Un cortafuegos (firewall) es un sistema de seguridad que controla y filtra el trafico de red entre segmentos, aplicando un conjunto de reglas o politicas. Actua como barrera entre redes de distinta confianza.

Tipos de cortafuegos segun su funcionamiento:

- Filtrado de paquetes (Packet Filtering): opera en capa 3 (Red) y capa 4 (Transporte). Inspeccion cabecera a cabecera: IP origen/destino, puerto, protocolo. Sin estado (stateless). Simple y rapido, pero vulnerable a spoofing y fragmentacion. Implementado en routers con ACLs.

- Cortafuegos de estado (Stateful Firewall): mantiene una tabla de conexiones activas (tabla de estados). Puede distinguir paquetes pertenecientes a una conexion legitima de paquetes fraudulentos. Opera en capas 3-4. Es el tipo de firewall mas extendido.

- Cortafuegos de aplicacion (Application Layer Firewall / Proxy Firewall / Next-Generation Firewall, NGFW): opera hasta capa 7 (Aplicacion). Inspeccion profunda de paquetes (DPI, Deep Packet Inspection). Puede identificar aplicaciones independientemente del puerto, filtrar contenido, detectar malware. Ejemplos: Palo Alto Networks, Fortinet FortiGate, Cisco Firepower.

- WAF (Web Application Firewall): cortafuegos especifico para aplicaciones web. Protege contra OWASP Top 10: SQL injection, XSS, CSRF, etc.

DMZ (Zona Desmilitarizada): segmento de red intermedio entre la red interna (trusted) e Internet (untrusted). Aloja servidores publicos (web, correo, DNS) expuestos a Internet, aislando la red interna en caso de compromiso del servidor en la DMZ. Se implementa con dos firewalls (o un firewall con tres interfaces).

DATO CLAVE: El firewall de estado (stateful) es superior al filtrado de paquetes porque mantiene el CONTEXTO de la conexion: permite respuestas a conexiones establecidas desde dentro sin abrir puertos permanentemente hacia dentro.

2. REDES PRIVADAS VIRTUALES (VPN)

Una VPN crea un canal de comunicacion seguro y cifrado sobre una red publica (Internet), permitiendo que los extremos se comuniquen como si estuvieran en la misma red privada.

Protocolos VPN:

- IPsec (Internet Protocol Security): opera en capa 3. Suite de protocolos para autenticacion e integridad (AH, Authentication Header) y confidencialidad (ESP, Encapsulating Security Payload). Dos modos: modo transporte (solo el payload IP se cifra, la cabecera IP original se mantiene, usado entre hosts) y modo tunel (todo el paquete IP original se encapsula en un nuevo paquete IP, usado entre gateways). Usa IKE (Internet Key Exchange) para la negociacion de claves.

- SSL/TLS VPN: opera en capa de aplicacion sobre TLS. No requiere cliente especial en muchos casos (puede usar un navegador). Mas flexible que IPsec para usuarios remotos. Ejemplos: OpenVPN (usa SSL/TLS), Cisco AnyConnect.

- OpenVPN: VPN de codigo abierto basada en OpenSSL/TLS. Muy extendida, flexible, funciona sobre UDP (puerto 1194 por defecto) o TCP.

- WireGuard: VPN moderna, minimalista y de alto rendimiento. Codigo mas pequeno que OpenVPN e IPsec, mayor seguridad por superficie de ataque reducida.

- PPTP: obsoleto. Vulnerabilidades graves. No debe usarse.

- L2TP/IPsec: L2TP (Layer 2 Tunneling Protocol) proporciona el tunel; IPsec proporciona el cifrado. Ampliamente soportado.

Tipos de VPN por topologia:
- Site-to-Site (red a red): conecta dos redes enteras a traves de Internet. Tipicamente entre sedes de una empresa. Implementada con routers o firewalls VPN en cada extremo.
- Remote Access (acceso remoto / cliente-a-sitio): un usuario remoto se conecta a la red corporativa desde cualquier lugar. Requiere cliente VPN en el dispositivo del usuario.

DATO CLAVE: IPsec en MODO TUNEL cifra TODO el paquete IP original (cabecera + datos) y lo encapsula en un nuevo paquete. Se usa entre gateways (site-to-site). En MODO TRANSPORTE, solo se cifra el payload, se mantiene la cabecera original; se usa entre hosts extremo a extremo.

3. SISTEMAS DE DETECCION Y PREVENCION DE INTRUSOS (IDS/IPS)

Un IDS (Intrusion Detection System) monitoriza el trafico de red o el sistema en busca de actividades maliciosas o anomalas y genera alertas. No bloquea el trafico.

Un IPS (Intrusion Prevention System) ademas de detectar, puede bloquear activamente el trafico malicioso en tiempo real. Se situa en linea (inline) en el flujo de trafico.

Clasificacion por ubicacion:
- NIDS/NIPS (Network-based): monitoriza el trafico de red. Se coloca en puntos estrategicos de la red (detras del firewall, en la DMZ).
- HIDS/HIPS (Host-based): monitoriza la actividad en un host concreto: llamadas al sistema, accesos a ficheros, integridad del sistema. Ejemplo: OSSEC, Tripwire.

Metodos de deteccion:
- Basada en firmas (signature-based): compara el trafico con una base de datos de patrones de ataques conocidos. Alta precision, bajas falsas alarmas, pero no detecta ataques nuevos (zero-day). Requiere actualizacion constante de la base de firmas.
- Basada en anomalias (anomaly-based / behavior-based): establece una linea base del comportamiento normal y alerta ante desviaciones. Puede detectar ataques nuevos, pero genera mas falsos positivos. Variante: basada en estadisticas, machine learning.

Falsos positivos y falsos negativos:
- Falso positivo: alerta generada para trafico legitimo. Reduce la confianza en el sistema.
- Falso negativo: ataque real no detectado. El mas peligroso.

Ejemplos de IDS/IPS de codigo abierto: Snort (basado en firmas, muy extendido), Suricata (multihilo, firmas y anomalias), Zeek (analisis de trafico de red).

DATO CLAVE: La diferencia clave entre IDS e IPS es que el IDS es PASIVO (detecta y alerta) y el IPS es ACTIVO (detecta, alerta y bloquea). El IPS se situa IN-LINE en el trafico; el IDS puede conectarse a un puerto SPAN/mirror del switch.

4. PROTOCOLOS DE ACCESO REMOTO

- SSH (Secure Shell): protocolo de acceso remoto seguro en capa de aplicacion. Puerto TCP 22. Proporciona cifrado de la sesion (evita eavesdropping), autenticacion por clave publica o contrasena, integridad (HMAC). Reemplaza a Telnet (inseguro, puerto 23). Permite ademas tunneling de puertos y transferencia de ficheros (SCP, SFTP).

- RDP (Remote Desktop Protocol): protocolo propietario de Microsoft para acceso remoto a escritorios Windows. Puerto TCP 3389 (tambien UDP 3389). Soporta cifrado TLS. Puede ser objetivo de ataques de fuerza bruta y exploits (BlueKeep, EternalBlue). Es critico restringir el acceso al puerto 3389 mediante VPN o firewall.

- SFTP (SSH File Transfer Protocol): transferencia segura de ficheros sobre SSH. No es FTP sobre SSL; es un subsistema SSH completamente distinto. Puerto 22.

- SCP (Secure Copy Protocol): copia segura de ficheros entre hosts usando SSH. Puerto 22. Mas simple que SFTP, sin capacidad de gestion de directorios.

- FTPS (FTP Secure): FTP sobre SSL/TLS. Puerto 990 (modo implicito) o 21 (modo explicito con STARTTLS). Distinto de SFTP.

- Telnet: acceso remoto sin cifrado. Puerto TCP 23. Completamente OBSOLETO en entornos de produccion.

- VNC (Virtual Network Computing): protocolo de escritorio remoto multiplataforma. Usa el protocolo RFB. Por defecto sin cifrado (se recomienda tunelizar por SSH).

DATO CLAVE: Puertos de acceso remoto criticos para el examen: SSH=22, Telnet=23, RDP=3389, FTP=21, SFTP=22 (sobre SSH). El CCN-CERT recomienda deshabilitar Telnet y usar siempre SSH con autenticacion por clave publica.

5. BUENAS PRACTICAS Y ARQUITECTURA DE SEGURIDAD

Principio de defensa en profundidad: aplicar multiples capas de seguridad, de modo que si una falla, las demas continuan protegiendo.

Principio de minimo privilegio: los usuarios y procesos deben tener solo los permisos minimos necesarios para su funcion.

Segmentacion de red: dividir la red en zonas con diferente nivel de confianza (Internet, DMZ, red corporativa, red de gestion) separadas por firewalls.

Monitorizacion y logs: los registros de eventos (logs) de firewalls, IDS/IPS y sistemas son fundamentales para la deteccion y forense. SIEM (Security Information and Event Management): plataforma que centraliza, correlaciona y analiza logs de multiples fuentes.

Zero Trust: modelo de seguridad que asume que no se puede confiar en ningun usuario o dispositivo por defecto, ni siquiera dentro de la red corporativa. Verificacion continua de identidad y estado del dispositivo. Microsegmentacion.

DATO CLAVE: La DMZ (Zona Desmilitarizada) es el segmento de red que aloja servidores accesibles desde Internet (web, correo, DNS) aislando la red interna. Si un servidor de la DMZ es comprometido, el atacante NO tiene acceso directo a la red interna.

PREGUNTAS TIPO EXAMEN INAP:

1. ?Que diferencia existe entre un IDS y un IPS?
   a) El IDS cifra el trafico y el IPS no
   b) El IDS detecta y alerta; el IPS detecta, alerta y bloquea activamente  [CORRECTA]
   c) El IDS actua en capa 7 y el IPS en capa 3
   d) El IPS solo detecta ataques conocidos por firmas; el IDS detecta anomalias

2. ?En que modo de IPsec se cifra todo el paquete IP original, incluyendo la cabecera?
   a) Modo transporte
   b) Modo tunel  [CORRECTA]
   c) Modo AH (Authentication Header)
   d) Modo ESP en texto claro

3. ?Cual es el puerto TCP estandar del protocolo SSH?
   a) 21
   b) 23
   c) 22  [CORRECTA]
   d) 3389

4. Un firewall de estado (stateful) es superior al filtrado de paquetes estatico porque:
   a) Opera exclusivamente en la capa de aplicacion (capa 7)
   b) Mantiene el contexto de las conexiones activas para distinguir trafico legitimo  [CORRECTA]
   c) No requiere definir reglas de acceso
   d) Cifra todo el trafico que pasa a traves de el
"""

Tema.objects.filter(bloque__numero=2, numero=8).update(resumen_estudio=t8)
print("Tema 2.8 actualizado.")

print("\n=== BLOQUE II COMPLETO: 8 temas actualizados correctamente ===")
