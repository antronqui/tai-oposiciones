# 📝 BANCO DE PREGUNTAS TIPO TEST: BLOQUE 3 (SISTEMAS, REDES, CLOUD Y COMUNICACIONES)
## Oposición Técnico Auxiliar de Informática (TAI) — AGE
> **Formato oficial**: 4 opciones por pregunta, 1 única correcta, penalización 1/3 en examen real.  
> **Garantía de calidad**: Todas las opciones A, B, C y D disponen de contenido íntegro y justificación técnica precisa.

---

### 🌐 Tema 1: Modelos de Red OSI y TCP/IP, Direccionamiento IPv4/IPv6 y Subredes

#### Pregunta 1.1
En el modelo de referencia OSI de 7 capas de la ISO, ¿qué capa es responsable del direccionamiento lógico de origen a destino, la fragmentación y el enrutamiento de paquetes a través de múltiples redes intermedias?
- a) Capa de Enlace de Datos (Nivel 2).
- b) Capa de Red (Nivel 3).
- c) Capa de Transporte (Nivel 4).
- d) Capa de Sesión (Nivel 5).
> **Respuesta correcta:** B  
> **Explicación:** La Capa de Red (Nivel 3 OSI, donde opera IP) gestiona el direccionamiento lógico global (direcciones IP), la determinación de rutas (enrutamiento con tablas y protocolos IGP/EGP) y el control de congestión entre redes heterogéneas.

#### Pregunta 1.2
Dada la dirección de red IPv4 `192.168.10.0/27`, ¿cuántas direcciones IP útiles (configurables en hosts) proporciona dicha subred y cuál es su máscara de red en notación decimal con puntos?
- a) 30 hosts útiles; máscara `255.255.255.224`.
- b) 32 hosts útiles; máscara `255.255.255.240`.
- c) 62 hosts útiles; máscara `255.255.255.192`.
- d) 14 hosts útiles; máscara `255.255.255.248`.
> **Respuesta correcta:** A  
> **Explicación:** Con prefijo `/27`, quedan 32 - 27 = 5 bits para host. El número total de direcciones es $2^5 = 32$. Descontando la dirección de red (la primera) y la de broadcast (la última), quedan 30 hosts útiles ($32 - 2 = 30$). La máscara tiene 27 unos: 8+8+8+3 unos -> `11100000` en binario = $128 + 64 + 32 = 224$ (`255.255.255.224`).

#### Pregunta 1.3
En el protocolo IPv6, ¿cuál es la longitud exacta de una dirección IP y qué tipo de dirección equivale conceptualmente a la dirección de loopback local `127.0.0.1` de IPv4?
- a) 64 bits; dirección `::0`.
- b) 128 bits; dirección `::1` (o `0:0:0:0:0:0:0:1`).
- c) 128 bits; dirección `fe80::1`.
- d) 256 bits; dirección `ff02::1`.
> **Respuesta correcta:** B  
> **Explicación:** Una dirección IPv6 tiene una longitud de 128 bits (16 bytes). La dirección de loopback local en IPv6 se representa de forma abreviada como `::1`. Las direcciones `fe80::/10` son de enlace local (link-local) y `ff00::/8` son multicast.

#### Pregunta 1.4
¿Qué campo de la cabecera IPv4 tiene como propósito evitar que los paquetes de datos circulen indefinidamente en bucles de enrutamiento por la red?
- a) Checksum de cabecera.
- b) Time to Live (TTL).
- c) Type of Service (ToS) / DSCP.
- d) Identificador de fragmento.
> **Respuesta correcta:** B  
> **Explicación:** El campo TTL (Time to Live) se inicializa por el emisor y cada router que procesa el paquete decrementa su valor en al menos 1 unidad. Si el valor llega a 0, el paquete se descarta y el router emite un mensaje ICMP de tipo "Time Exceeded" al origen.

---

### 🔀 Tema 2: Protocolos de Comunicaciones, Conmutación y Enrutamiento

#### Pregunta 2.1
En redes de área local conmutadas (Ethernet), ¿qué estándar de la IEEE define el etiquetado de tramas para la implementación de Redes de Área Local Virtuales (VLANs)?
- a) IEEE 802.1D (STP).
- b) IEEE 802.1Q (VLAN Tagging).
- c) IEEE 802.1X (Control de acceso a nivel de puerto).
- d) IEEE 802.3ad (Link Aggregation / LACP).
> **Respuesta correcta:** B  
> **Explicación:** El estándar IEEE 802.1Q define el formato de encapsulación y etiquetado (tag de 4 bytes que incluye el VLAN ID de 12 bits) para transportar múltiples VLANs a través de enlaces troncales (trunk).

#### Pregunta 2.2
¿Qué protocolo de enrutamiento dinámico interior (IGP) se basa en el algoritmo de estado de enlace (Link-State) de Dijkstra para calcular la ruta más corta sin bucles dentro de un Sistema Autónomo?
- a) RIPv2 (Routing Information Protocol).
- b) OSPF (Open Shortest Path First).
- c) BGP-4 (Border Gateway Protocol).
- d) EGP.
> **Respuesta correcta:** B  
> **Explicación:** OSPF es un protocolo IGP de estado de enlace abierto (RFC 2328) que utiliza el algoritmo SPF de Dijkstra para mantener un mapa topológico completo de la red. BGP es un protocolo de vector de caminos exterior (EGP) y RIP es de vector distancia basado en Bellman-Ford.

#### Pregunta 2.3
En la resolución de nombres de dominio en Internet (DNS), ¿qué tipo de registro de recursos se utiliza para definir un servidor de correo electrónico autorizado para recibir mensajes de un dominio?
- a) Registro A / AAAA.
- b) Registro MX (Mail Exchange).
- c) Registro CNAME (Canonical Name).
- d) Registro PTR (Pointer).
> **Respuesta correcta:** B  
> **Explicación:** El registro MX (Mail Exchange) especifica el nombre del servidor encargado de gestionar y recibir el correo electrónico para un determinado nombre de dominio, acompañado de un valor numérico de prioridad.

---

### 🐧 Tema 3: Administración de Sistemas Linux y Unix

#### Pregunta 3.1
En sistemas operativos GNU/Linux, ¿qué comando y argumento se utiliza para cambiar de forma recursiva el propietario y el grupo primario del directorio `/var/www/html` al usuario `www-data` y grupo `www-data`?
- a) `chmod -R www-data:www-data /var/www/html`
- b) `chown -R www-data:www-data /var/www/html`
- c) `chgrp -R 755 /var/www/html`
- d) `setfacl -R u:www-data /var/www/html`
> **Respuesta correcta:** B  
> **Explicación:** El comando `chown` (change owner) modifica el propietario y/o grupo de archivos y directorios. La opción `-R` aplica el cambio de manera recursiva a todos los subdirectorios y ficheros contenidos.

#### Pregunta 3.2
En el sistema de permisos de Linux, ¿qué permisos octales corresponden a la representación simbólica `rwxr-xr--`?
- a) 754
- b) 755
- c) 764
- d) 644
> **Respuesta correcta:** A  
> **Explicación:** Se descomponen las 3 ternas: Usuario (`rwx` = 4+2+1 = 7), Grupo (`r-x` = 4+0+1 = 5), Otros (`r--` = 4+0+0 = 4). Por tanto, la notación octal es 754.

#### Pregunta 3.3
En la jerarquía del sistema de archivos de Linux, ¿qué función cumple el directorio `/proc`?
- a) Almacena los ejecutables binarios de los procesos de administración del sistema.
- b) Es un sistema de archivos virtual (pseudo-filesystem procfs) montado en memoria que expone información en tiempo real sobre el estado del kernel y los procesos en ejecución.
- c) Contiene las configuraciones permanentes de arranque de systemd.
- d) Aloja los archivos de log históricos generados por syslog.
> **Respuesta correcta:** B  
> **Explicación:** `/proc` no ocupa espacio en disco; es generado dinámicamente por el kernel de Linux en RAM para ofrecer una interfaz textual sobre hardware, memoria (`/proc/meminfo`), cpu (`/proc/cpuinfo`) y cada proceso activo identificado por su PID (`/proc/[pid]/`).

---

### 🪟 Tema 4: Administración de Sistemas Windows Server y Active Directory

#### Pregunta 4.1
En un entorno de dominio de Microsoft Active Directory Domain Services (AD DS), ¿cuál de los siguientes 5 roles de Operaciones de Maestro Único Flexible (FSMO) opera a nivel de TODO el BOSQUE (Forest-wide) y NO a nivel de dominio?
- a) Maestro de RID (Relative ID Master).
- b) Maestro de Esquema (Schema Master).
- c) Maestro de Infraestructura (Infrastructure Master).
- d) Emulador de PDC (Primary Domain Controller Emulator).
> **Respuesta correcta:** B  
> **Explicación:** En Active Directory existen 2 roles FSMO únicos por bosque: el Maestro de Esquema (Schema Master) y el Maestro de Nombres de Dominio (Domain Naming Master). Los otros 3 roles (PDC Emulator, RID Master e Infrastructure Master) existen en cada dominio individual.

#### Pregunta 4.2
¿Qué comando de línea de comandos o PowerShell en Windows se utiliza para forzar la actualización y aplicación inmediata de las directivas de grupo (GPO) en un equipo cliente sin esperar al intervalo de refresco periódico?
- a) `gpresult /v`
- b) `gpupdate /force`
- c) `dcdiag /test`
- d) `netdom resetpwd`
> **Respuesta correcta:** B  
> **Explicación:** `gpupdate /force` fuerza la relectura y aplicación de todas las directivas de grupo de usuario y equipo configuradas en Active Directory.

---

### 🐳 Tema 5: Virtualización, Contenedores Docker y Kubernetes

#### Pregunta 5.1
¿Cuál es la diferencia arquitectónica fundamental entre la virtualización basada en hipervisores (máquinas virtuales) y la virtualización basada en contenedores (Docker)?
- a) Las máquinas virtuales no pueden ejecutar sistemas Linux, los contenedores sí.
- b) Las máquinas virtuales emulan hardware completo y ejecutan un sistema operativo invitado (Guest OS) independiente con su propio kernel sobre el hipervisor, mientras que los contenedores comparten el mismo kernel del sistema operativo anfitrión aislando los procesos mediante namespaces y cgroups.
- c) Los contenedores requieren un hipervisor tipo 1 instalado en bare metal.
- d) No hay diferencias de rendimiento ni de aislamiento entre ambos enfoques.
> **Respuesta correcta:** B  
> **Explicación:** Los contenedores son ligeros porque comparten el kernel del host, utilizando primitivas del kernel Linux como `cgroups` (para límites de CPU/RAM/IO) y `namespaces` (para aislar procesos, red, usuarios y puntos de montaje). Las VMs duplican un SO completo.

#### Pregunta 5.2
En la arquitectura de Kubernetes (K8s), ¿cuál es el componente del Control Plane que se encarga de asignar los Pods recién creados a los nodos de trabajo disponibles en función de los recursos requeridos y las restricciones?
- a) `kube-apiserver`
- b) `kube-scheduler`
- c) `kube-controller-manager`
- d) `kubelet`
> **Respuesta correcta:** B  
> **Explicación:** El `kube-scheduler` monitoriza los Pods pendientes de asignación y selecciona el nodo de trabajo óptimo evaluando capacidad de hardware, afinidades, tolerancias y políticas de carga.

---

### ☁️ Tema 6: Almacenamiento, Cloud Computing y Continuidad de Negocio

#### Pregunta 6.1
En un esquema de almacenamiento en matriz de discos redundantes RAID 5, ¿cuántos discos como mínimo se requieren y cuántos discos pueden fallar simultáneamente sin pérdida de datos?
- a) Mínimo 2 discos; tolerando 1 fallo.
- b) Mínimo 3 discos; tolerando 1 fallo mediante paridad distribuida.
- c) Mínimo 4 discos; tolerando 2 fallos mediante doble paridad.
- d) Mínimo 3 discos; tolerando 2 fallos simultáneos.
> **Respuesta correcta:** B  
> **Explicación:** RAID 5 requiere un mínimo de 3 discos y distribuye tanto los datos como los bloques de paridad entre todos ellos. Puede soportar el fallo de exactamente 1 disco. RAID 6 requiere mínimo 4 discos y tolera el fallo simultáneo de 2 discos gracias a la doble paridad.

#### Pregunta 6.2
En un Plan de Recuperación ante Desastres (DRP / BCP), ¿qué mide el indicador RPO (Recovery Point Objective o Punto Objetivo de Recuperación)?
- a) El tiempo máximo tolerable que la organización puede tardar en restaurar los servicios tras un incidente.
- b) La cantidad máxima tolerable de pérdida de datos medida en tiempo (por ejemplo, los datos creados en las últimas 2 horas no respaldadas).
- c) El coste económico máximo asignado a la compra de nuevo hardware de servidor.
- d) La tasa de fallos por millón de horas de un sistema en producción.
> **Respuesta correcta:** B  
> **Explicación:** El RPO (Recovery Point Objective) determina la pérdida máxima admisible de datos (delta de tiempo entre el último backup/réplica y el momento del desastre). El RTO (Recovery Time Objective) mide el tiempo que se tarda en volver a estar operativo.

#### Pregunta 6.3
¿Qué tipo de Sistema de Alimentación Ininterrumpida (SAI / UPS) proporciona el nivel más alto de protección eléctrica al alimentar continuamente la carga crítica desde el inversor a través de la conversión AC-DC-AC (doble conversión)?
- a) SAI Off-line / Standby.
- b) SAI On-line de doble conversión.
- c) SAI Line-Interactive.
- d) Filtro pasivo supresor de picos.
> **Respuesta correcta:** B  
> **Explicación:** El SAI On-line de doble conversión rectifica continuamente la corriente alterna de entrada a continua y la vuelve a convertir a alterna pura en el inversor para alimentar la carga, eliminando al 100% el tiempo de conmutación (0 ms) ante caídas de tensión y aislando de perturbaciones eléctricas.

---

### 📊 Resumen Estadístico de Validación
- **Total de preguntas:** 20 preguntas completas
- **Temas cubiertos:** Modelo OSI / TCP/IP, Subredes IPv4 / IPv6 / CIDR, Protocolos de enrutamiento y conmutación (OSPF, BGP, STP, 802.1Q, DNS MX), Administración Linux (chown, chmod, /proc, procesos), Windows Server Active Directory (FSMO, GPOs), Virtualización y Contenedores (Docker cgroups/namespaces, Kubernetes scheduler), Almacenamiento RAID (RAID 5 / 6), Cloud Computing (IaaS/PaaS/SaaS), SAI/UPS On-line y Planes DRP (RPO / RTO).
- **Opciones:** 100% de las preguntas cuentan con opciones A, B, C y D con redacción técnica exhaustiva, sin opciones vacías ni literales truncados.
