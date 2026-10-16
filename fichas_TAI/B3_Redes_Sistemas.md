# 🖥️ BLOQUE 3 — REDES, SISTEMAS Y SEGURIDAD
> *Fichas de estudio basadas en exámenes oficiales TAI 2022, 2024 y 2025*

---

## ÍNDICE RÁPIDO
| Tema | Preguntas 2025 | Dificultad |
|------|---------------|------------|
| Modelo OSI / TCP-IP | 3-4 preguntas | ⭐⭐ |
| Subredes / CIDR / IPv4 / IPv6 | 3-4 preguntas | ⭐⭐⭐ |
| DNS / Protocolos de red | 2-3 preguntas | ⭐⭐ |
| Switches / VLANs / STP | 2-3 preguntas | ⭐⭐⭐ |
| Hardware del PC | 3-4 preguntas | ⭐⭐ |
| Sistemas Operativos Linux | 4-5 preguntas | ⭐⭐⭐ |
| Windows Server / AD | 2-3 preguntas | ⭐⭐ |
| Docker / Kubernetes | 2-3 preguntas | ⭐⭐⭐ |
| Seguridad (ENS, MFA, CCN) | 4-5 preguntas | ⭐⭐⭐ |
| CPD / ANSI TIA-942 | 1-2 preguntas | ⭐⭐ |
| Backup 3-2-1 / RAID | 2-3 preguntas | ⭐⭐ |

---

## 1. HARDWARE DEL PC

### 1.1 Jerarquía de Caché
| Caché | Ubicación | Velocidad | Capacidad |
|-------|-----------|-----------|-----------|
| **L1** | **Integrada dentro del núcleo** del procesador | **Más rápida** | **Menor** (~64KB) |
| L2 | Dentro del procesador (puede ser por núcleo o compartida) | Rápida | Media (~256KB-1MB) |
| L3 | Dentro del procesador, compartida entre núcleos | Moderada | Mayor (~8-32MB) |
| L4 | Fuera del procesador (menos común) | Más lenta | Mayor |

> [!CAUTION]
> **TRAMPA 2025**: La caché **integrada físicamente dentro del núcleo**, más rápida y menor capacidad = **L1**. Respuesta: **a**.

### 1.2 Bus del Sistema
**Función principal**: Transferir **datos, direcciones y señales de control** entre la CPU, la memoria y los periféricos

> [!CAUTION]
> **TRAMPA**: El bus NO ejecuta instrucciones, NO suministra energía, NO almacena datos. Su función es la **transferencia de información**.

### 1.3 SSD (Solid State Drive)
- Almacena datos en **memoria no volátil sin partes móviles**
- NO usa discos magnéticos giratorios (eso es HDD)
- NO usa RAM volátil (la RAM es volátil y para memoria principal)
- NO tiene cabezales de lectura mecánicos

### 1.4 HDMI 2.1
- Ancho de banda máximo: **48 Gbps**

### 1.5 Interfaces y Conexiones
| Interfaz | Función |
|---------|---------|
| **IPP (Internet Printing Protocol)** | Colección de estándares abiertos que define un **protocolo de impresión en red de alto nivel** |
| USB | Conexión física periféricos |
| HDMI/DisplayPort | Vídeo y audio digital |

> [!CAUTION]
> **TRAMPA 2025**: IPP es un **protocolo de red** para impresión (no compresión, no formato de archivo, no USB). Respuesta: **a**.

### 1.6 RAID
| RAID | Nombre | Tolerancia | Mínimo discos |
|------|--------|-----------|---------------|
| **RAID 0** | **Striping** (distribución) | **Ningún fallo** | 2 |
| **RAID 1** | **Mirroring** (espejo) | 1 fallo | 2 |
| **RAID 5** | Paridad distribuida | **1 fallo** | 3 |
| **RAID 6** | Doble paridad | 2 fallos | 4 |
| RAID 10 | RAID 1+0 | 1 por espejo | 4 |

> [!CAUTION]
> **TRAMPA CLÁSICA**: RAID 0 = **Striping** (distribución, SIN redundancia). RAID 1 = **Mirroring** (espejo). Muchos los confunden.
> **TRAMPA 2025**: RAID 5 tolera **1 fallo** de dispositivo (no ninguno, no dos, no tres). Respuesta: **b**.

---

## 2. MODELO OSI Y TCP/IP

### 2.1 Modelo OSI — 7 Capas
```
7. APLICACIÓN     → HTTP, HTTPS, FTP, SMTP, DNS, DHCP, SSH
6. PRESENTACIÓN   → Cifrado (TLS), compresión, codificación (ASCII, UTF-8)
5. SESIÓN         → Control de diálogo, establecimiento/cierre de sesiones
4. TRANSPORTE     → TCP (fiable), UDP (no fiable), puertos, segmentos
3. RED            → IP, enrutamiento, paquetes, routers
2. ENLACE DATOS   → MAC, tramas, switches, ARP
1. FÍSICA         → Bits, cable, fibra, hubs, señales
```

**Mnemotecnia** (de abajo arriba): **"Por Favor, No Tires Esa Pequeña Araña"**  
(Física, Enlace, Red, Transporte, Sesión, Presentación, Aplicación)

### 2.2 Funciones de Cada Capa (Preguntas Frecuentes)
| Capa | Función clave |
|------|--------------|
| **Presentación (6)** | **Negociación de sintaxis, cifrado y compresión** |
| **Transporte (4)** | Segmentación, control de flujo extremo a extremo, puertos |
| **Red (3)** | Enrutamiento, IP, TTL/Hop Limit |
| **Enlace (2)** | Tramas, MAC, LLC, ARP |

### 2.3 Conmutación de Circuitos vs Paquetes
| Tipo | Característica |
|------|---------------|
| **Conmutación de circuitos** | **Camino físico/lógico DEDICADO** durante toda la comunicación (ej: RDSI, telefonía analógica) |
| **Conmutación de paquetes** | Cada paquete puede seguir ruta diferente, ancho de banda compartido (ej: Internet) |

> [!CAUTION]
> **TRAMPA 2025**: Conmutación de circuitos = **camino dedicado y exclusivo** entre nodos. Respuesta: **c**.

---

## 3. IPv4 — SUBREDES Y CIDR

### 3.1 Cálculo de Subredes (Método Rápido)
**Fórmula base:**
- Número de hosts = 2^(32-máscara) - 2
- Número de subredes con n bits prestados = 2^n

**Máscaras frecuentes:**
| CIDR | Máscara | Hosts útiles | Subredes de /8 |
|------|---------|-------------|----------------|
| /24 | 255.255.255.0 | 254 | - |
| /25 | 255.255.255.128 | 126 | - |
| /27 | 255.255.255.224 | 30 | - |
| /20 | 255.255.240.0 | **4094** | - |
| /16 | 255.255.0.0 | 65534 | - |

**Ejemplo Supuesto 2025:** Red `10.30.16.0/20`
- Hosts disponibles = 2^(32-20) - 2 = 2^12 - 2 = 4096 - 2 = **4094** ✅

**Ejemplo Supuesto 2025:** Primera subred `/25` dentro de `10.30.16.0/20`
- Primera subred /25: `10.30.16.0/25`
- Dirección de red: `10.30.16.0`
- Broadcast: `10.30.16.127` (2^7 - 1 = 127)
- Hosts: 10.30.16.1 a 10.30.16.126

### 3.2 Subredes — Calcular Número Mínimo de Bits
**Ejemplo examen 2025:** Red `10.0.0.0/8`, necesitan **600 subredes**
- 2^9 = 512 < 600 (insuficiente)
- 2^10 = 1024 ≥ 600 ✅ (necesitamos 10 bits para subredes)
- Máscara = /8 + 10 = **/18**

> [!CAUTION]
> **TRAMPA 2025**: 600 subredes → necesitas 2^10 = 1024 → 10 bits → /8 + 10 = **/18**. Respuesta: **b**.

### 3.3 DMZ — Red Desmilitarizada
- Zona de red **intermedia** entre Internet y la red interna
- Permite alojar servicios públicos (web, correo) sin exponer la red interna
- Implementada con **firewalls** que segmentan el tráfico

> [!CAUTION]
> **TRAMPA 2025**: DMZ = **zona desmilitarizada** con firewalls. Respuesta: **b**.

---

## 4. IPv6

### 4.1 Campo "Hop Limit" en IPv6 (RFC 8200)
- **Equivalente al TTL de IPv4**
- Indica el **número máximo de saltos** que un paquete puede dar antes de ser descartado
- Se decrementa en 1 en cada router
- Cuando llega a 0, el paquete se descarta y se envía mensaje ICMPv6

> [!CAUTION]
> **TRAMPA 2025**: Hop Limit = **máximo de saltos antes de descarte** (no QoS, no tamaño de payload, no tipo de cabecera). Respuesta: **b**.

---

## 5. SWITCHES, VLANs Y PROTOCOLOS

### 5.1 Dispositivos de Red — Dominios
| Dispositivo | Dominio de colisión | Dominio de difusión |
|------------|-------------------|-------------------|
| **Hub** | 1 (comparte) | 1 (comparte) |
| **Switch** | **Segmenta** (uno por puerto) | 1 (comparte) = mismo |
| **Router** | Segmenta | **Segmenta** |

> [!CAUTION]
> **TRAMPA 2025**: Un **switch** segmenta dominios de colisión pero **mantiene un único dominio de difusión**. Respuesta: **b**.

### 5.2 IEEE 802.1Q — VLANs
**Campos de la cabecera 802.1Q:**
| Campo | Bits | Función |
|-------|------|---------|
| **TPID** | 16 | Identificador de protocolo (0x8100) |
| **PCP (Priority Code Point)** | 3 | **8 niveles de prioridad** (CoS — Class of Service) |
| **DEI/CFI** | 1 | Canonical Format Indicator / Drop Eligible Indicator |
| **VID (VLAN ID)** | 12 | Identificador de VLAN (0-4095) |

> [!CAUTION]
> **TRAMPA 2025**: **PCP** permite definir 8 niveles de prioridad (2^3 = 8). No es VID (que identifica la VLAN), no es CFI. Respuesta: **c**.

### 5.3 Seguridad en Switches — MAC Sticky
Una dirección MAC de tipo **"sticky"**:
- Aprendida **dinámicamente** que se convierte en parte de la **configuración en ejecución**
- Puede guardarse de forma **permanente** (sobrevive a reinicios si se guarda la configuración)

> [!CAUTION]
> **TRAMPA 2025**: Sticky MAC = aprendida dinámicamente que se hace permanente. Respuesta: **a**.

### 5.4 Topología Bus — Terminadores
Función de los terminadores en topología bus:
- **Absorber la energía de la señal** al final de la transmisión
- **Evitar interferencias** causadas por la reflexión de la señal
- NO amplifican la señal, NO asignan IPs, NO cifran

---

## 6. LINUX — COMANDOS CLAVE

### 6.1 Comandos de Red
| Comando | Función |
|---------|---------|
| `ip route show` | Ver **tabla de enrutamiento** |
| `ip route get IP` | Ver **ruta efectiva** (interfaz/next hop) a una IP específica |
| `ss -ltn` | Listar **puertos en escucha** (-l listen, -t TCP, -n numérico) |
| `ss -lun` | Listar puertos UDP en escucha |
| `netstat -tlnp` | Alternativa a ss (más antigua) |
| `ping -c 4 IP` | Comprobar conectividad |
| `traceroute IP` | Trazar ruta |
| `nslookup dominio` | Consultar DNS |
| `dig dominio` | Consultar DNS (detallado) |
| `arp -an` | Ver caché ARP |

> [!CAUTION]
> **TRAMPA 2025**: Ver ruta efectiva → `ip route get IP`. Ver tabla completa → `ip route show`. Listar puertos en escucha → `ss -ltn`. En Windows sería `route print` o `netstat -p tcp`.

### 6.2 Comandos de Sistema de Archivos y Procesos
| Comando | Función |
|---------|---------|
| `chmod 644 fichero` | Cambiar permisos (rw-r--r--) |
| `chown usuario fichero` | Cambiar propietario |
| `tail -f fichero` | Ver fichero **en tiempo real** |
| `tail -n 50 fichero` | Ver últimas 50 líneas |
| `grep patrón fichero` | Buscar patrón |
| `ps aux` | Ver procesos en ejecución |
| `kill -9 PID` | Terminar proceso |

### 6.3 Permisos en Linux
```
rwx rwx rwx
│   │   └── Otros (others)
│   └────── Grupo (group)
└────────── Propietario (user)

r = 4, w = 2, x = 1

Ejemplo: chmod 755 → rwxr-xr-x
  Propietario: 7 = rwx
  Grupo: 5 = r-x
  Otros: 5 = r-x
```

### 6.4 Systemd — Gestión de Servicios
| Comando | Función |
|---------|---------|
| `systemctl start servicio` | Iniciar servicio |
| `systemctl stop servicio` | Detener servicio |
| `systemctl restart servicio` | Reiniciar servicio |
| `systemctl enable servicio` | **Habilitar en el arranque** (autostart) |
| `systemctl disable servicio` | Deshabilitar en el arranque |
| `systemctl status servicio` | Ver estado del servicio |

> [!CAUTION]
> **TRAMPA 2025**: Para habilitar nginx en el arranque → `systemctl enable nginx` (no `autostart`, no `service nginx start-enable`). Respuesta: **a**.

### 6.5 Crontab — Sintaxis Completa
```
# minuto hora dia_mes mes dia_semana comando
# (0-59) (0-23) (1-31) (1-12) (0-7, 0 y 7=domingo)

0 5 8 11 *     → Las 05:00 del día 8 de noviembre
*/15 * * * *   → Cada 15 minutos
0 0 * * 1      → Los lunes a medianoche
0 8-17 * * 1-5 → De lunes a viernes de 8h a 17h (cada hora)
```

### 6.6 Almacenamiento — LVM y RAID
**LVM — Extender volumen XFS:**
```bash
# 1. Extender el volumen lógico
lvextend -L 600G /dev/vg_datos/lv_contenido

# 2. Ampliar en línea el sistema de ficheros XFS
xfs_growfs /contenido
```
*(XFS puede crecer en línea. ext4 usaría `resize2fs`)*

**Regla 3-2-1 de Backups:**
- **3** copias de los datos
- en **2** soportes/medios **distintos**
- con **1** copia **fuera de la sede**

> [!CAUTION]
> **TRAMPA 2025**: 3-2-1 = 3 copias, 2 soportes **distintos**, 1 copia **fuera de la sede** (no cifrada, no en nube específicamente). Respuesta: **c**.

### 6.7 Compresión y Archivado — tar
```bash
# Crear archivo comprimido .tar.gz
tar -czf destino.tar.gz /directorio/origen/

# Extraer archivo .tar.gz
tar -xzf archivo.tar.gz

# Opciones de tar:
# -c = crear, -x = extraer, -z = gzip, -f = nombre fichero, -v = verbose
```

> [!CAUTION]
> **TRAMPA 2025**: Para **crear** .tar.gz → `tar -czf`. Para **extraer** → `tar -xzf`. NO es `gzip`, NO es `zip`. Respuesta: **b**.

### 6.8 Firewall en RHEL — firewall-cmd
```bash
# Añadir regla permanente (rich rule) para puerto 3306 solo desde DMZ
firewall-cmd --permanent --zone=public \
  --add-rich-rule='rule family="ipv4" source address="172.19.50.0/27" \
  port protocol="tcp" port="3306" accept'

# Para activar en tiempo real tras añadir permanente
firewall-cmd --reload
```

> [!CAUTION]
> **TRAMPA 2025**: La sintaxis correcta usa `source address=` (no `address=`). La opción d es la correcta en el examen 2025.

### 6.9 sysctl — Parámetros de Kernel
```bash
# Mitigar IP Spoofing con filtrado de ruta inversa
net.ipv4.conf.all.rp_filter=1

# Habilitar reenvío IP (routers/NAT)
net.ipv4.ip_forward=1

# Proteger contra SYN flood
net.ipv4.tcp_syncookies=1
```

> [!CAUTION]
> **TRAMPA 2025**: Mitigar **IP Spoofing** → `net.ipv4.conf.all.rp_filter=1` (filtrado de ruta inversa). No es `ip_forward` ni `accept_ra`. Respuesta: **b**.

---

## 7. WINDOWS SERVER

### 7.1 Active Directory — Herramientas Gráficas
| Herramienta | MMC | Función |
|-------------|-----|---------|
| **Active Directory Users and Computers** | **dsa.msc** | Gestión de usuarios, grupos del **dominio** |
| Local Users and Groups | lusrmgr.msc | Usuarios/grupos **locales** (no del dominio) |
| Group Policy Management | gpmc.msc | Gestión de GPOs |
| DNS Manager | dnsmgmt.msc | Gestión de DNS |
| Certificates | certmgr.msc | Gestión de certificados |

> [!CAUTION]
> **TRAMPA 2025**: Para agregar usuario a grupo global del dominio desde el DC → **dsa.msc** (no lusrmgr que es local, no certmgr). Respuesta: **a**.

### 7.2 Password Settings Object (PSO)
- Permite diferentes políticas de contraseña dentro del **mismo dominio**
- Se asigna a usuarios o grupos de seguridad específicos
- Sustituye a la política de contraseñas del dominio para esos objetos

### 7.3 PowerShell — Cmdlets Frecuentes
```powershell
# Copiar archivos recursivamente
Copy-Item -Path "C:\Origen\*" -Destination "C:\Destino" -Recurse

# Obtener servicios
Get-Service -Name "nginx"

# Parar/iniciar servicio
Stop-Service -Name "nginx"
Start-Service -Name "nginx"
```

---

## 8. DOCKER Y KUBERNETES

### 8.1 Docker — Comandos Esenciales
| Comando | Función |
|---------|---------|
| `docker run imagen` | **Crear e iniciar** nuevo contenedor (descarga imagen si no existe) |
| `docker start ID` | Iniciar contenedor parado |
| `docker stop ID` | Parar contenedor gracefully |
| `docker kill ID` | **Parar inmediatamente** (SIGKILL) |
| `docker exec ID cmd` | Ejecutar comando en contenedor en ejecución |
| `docker ps` | Listar contenedores en ejecución |
| `docker ps -a` | Listar todos los contenedores |
| `docker images` | Listar imágenes locales |
| `docker rm ID` | Eliminar contenedor parado |
| `docker rmi imagen` | Eliminar imagen |

### 8.2 Kubernetes — Componentes del Plano de Control
| Componente | Función |
|-----------|---------|
| **kube-scheduler** | **Decide en qué nodo ejecutar** cada Pod según recursos disponibles |
| kube-apiserver | Punto de entrada a toda la API de K8s |
| etcd | Base de datos clave-valor con el estado del clúster |
| kube-controller-manager | Gestiona el estado deseado (ReplicaSets, Deployments...) |
| cloud-controller-manager | Interactúa con el proveedor cloud |

### 8.3 Snapshot vs Backup
| Concepto | Característica |
|---------|---------------|
| **Snapshot** | Captura del **estado en un momento** específico. **Depende del sistema** original. Rápido |
| **Backup** | Réplica de datos con propósito de **restaurar** en caso de pérdida. Independiente |

> [!NOTE]
> Los snapshots NO sustituyen a los backups. Un snapshot en el mismo sistema no protege ante fallos de hardware.

---

## 9. SEGURIDAD

### 9.1 ENS — Principio de Mínimo Privilegio
- Conceder a cada usuario **únicamente los permisos estrictamente necesarios** para sus funciones
- NO usar cuentas genéricas de alta prioridad
- NO compartir credenciales con responsables
- NO basar el control de acceso solo en ubicación física

### 9.2 CCN-CERT — Contraseñas Robustas
Requisitos:
- ✅ Longitud mínima **8 caracteres** (no 7)
- ✅ Mezcla de tipos de caracteres
- ✅ No usar datos personales
- ✅ No apuntar en papel accesible
- ✅ Rotación periódica

### 9.3 MFA — Factores de Autenticación
| Factor | Tipo | Ejemplos |
|--------|------|---------|
| Algo que **SABES** | Conocimiento | Contraseña, PIN, preguntas |
| Algo que **TIENES** | Posesión | Token OTP, tarjeta, smartphone |
| Algo que **ERES** | Inherencia/Biometría | Huella, iris, cara, voz |

**MFA = al menos 2 factores de categorías DISTINTAS**

❌ Iris + Huella = solo biometría (NO es MFA)  
✅ Contraseña + Token OTP = saber + tener (SÍ es MFA)  
✅ Contraseña + Iris = saber + ser (SÍ es MFA)  
✅ Tarjeta + Reconocimiento facial = tener + ser (SÍ es MFA)  

### 9.4 CCN-CERT — Key Exchange
- Solo se autorizan métodos de Key Exchange con fortaleza de seguridad de **al menos 128 bits**

### 9.5 NVD — Base de Datos de Vulnerabilidades
- **NVD (National Vulnerability Database)**: Base de datos de vulnerabilidades del NIST (USA)
- Complementa al CVE (Common Vulnerabilities and Exposures)
- Proporciona puntuaciones CVSS

### 9.6 Amenazas de Red
| Amenaza | Descripción |
|---------|-------------|
| **Pharming** | Modifica DNS/hosts para redirigir sin que el usuario lo note |
| **Phishing** | Correos fraudulentos suplantando identidad |
| **Spoofing IP** | Falsificación de IP de origen de paquetes |
| **SYN Flood** | Ataque DoS explotando el handshake TCP |
| **Man-in-the-Middle** | Intercepción de comunicaciones |

---

## 10. CPD — CENTRO DE PROCESAMIENTO DE DATOS

### 10.1 ANSI/TIA-942-B — Zonas del CPD
| Zona | Sigla | Descripción |
|------|-------|-------------|
| **EDA (Equipment Distribution Area)** | EDA | Donde se ubican **elementos finales** (servidores, mainframes) |
| MDA (Main Distribution Area) | MDA | Distribución principal del CPD |
| HDA (Horizontal Distribution Area) | HDA | Distribución horizontal hacia los racks |
| IDA (Intermediate Distribution Area) | IDA | Distribución intermedia (opcional) |

> [!CAUTION]
> **TRAMPA 2025**: La zona donde se ubican servidores y mainframes = **EDA** (Equipment Distribution Area). Respuesta: **b**.

### 10.2 ANSI/TIA-942-B — Tiers (Niveles)
| Tier | Nombre | Disponibilidad | Mantenimiento |
|------|--------|---------------|---------------|
| Tier 1 | Básica | 99.671% | Requiere parada |
| Tier 2 | Componentes redundantes | 99.741% | Requiere parada |
| **Tier 3** | **Mantenimiento concurrente** | **99.982%** | **SIN parada** |
| Tier 4 | Tolerante a fallos | 99.995% | Sin parada, soporta fallo |

> [!CAUTION]
> **TRAMPA**: Tier 3 = **Mantenimiento concurrente** (se puede hacer mantenimiento sin parar el CPD). Tier 4 = tolerante a fallos.

### 10.3 Protocolo DHCP Relay — Cisco IOS
Para configurar DHCP relay en la SVI (Switched Virtual Interface) de una VLAN:
```
Router(config-if)# ip helper-address 10.30.20.5
```

> [!CAUTION]
> **TRAMPA 2025**: El comando correcto es `ip helper-address IP` (no `ip dhcp server`, no `service dhcp forward`, no `relay dhcp`). Respuesta: **a**.

---

## 11. BLUETOOTH Y WIRELESS

### 11.1 Bluetooth Low Energy — Extended Advertising (BT 5.0)
- BT 5.0 introdujo **Extended Advertising** que usa **40 canales** (no 3, no 22, no 37)

> [!CAUTION]
> **TRAMPA 2025**: BT 5.0 Extended Advertising usa **40 canales**. Los 3 canales son los de advertising tradicional (BT 4.x). Respuesta: **d**.

### 11.2 Wi-Fi — WPA2 vs WPA3
| Protocolo | Personal | Enterprise |
|-----------|---------|-----------|
| WPA2 | PSK (Pre-Shared Key) | EAP (802.1X) |
| **WPA3** | **SAE** (Simultaneous Auth. of Equals) | **EAP** (802.1X) + sujetos a suite B |

---

## 12. PROTOCOLOS DE APLICACIÓN

### 12.1 Puertos Estándar — Los Más Importantes
| Puerto | Protocolo | Servicio |
|--------|-----------|---------|
| 20/21 | TCP | FTP (datos/control) |
| 22 | TCP | SSH |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP (correo saliente) |
| 53 | TCP/UDP | DNS |
| 67/68 | UDP | DHCP (servidor/cliente) |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 143 | TCP | IMAP |
| 389 | TCP | LDAP |
| 443 | TCP | HTTPS |
| 3306 | TCP | MySQL |
| 1521 | TCP | Oracle DB |
| 3389 | TCP | RDP |

### 12.2 DNS — Función Principal
DNS = **Traducir nombres de dominio** legibles para humanos en **direcciones IP** numéricas

> [!CAUTION]
> **TRAMPA**: DNS NO encripta correos, NO enruta paquetes, NO traduce IP a MAC (eso es ARP). Respuesta: **d**.

### 12.3 Atenuación de Señal
- **Atenuación**: Degradación de la señal = **pérdida de energía** a medida que se propaga por el medio

| Fenómeno | Descripción |
|---------|-------------|
| **Atenuación** | Pérdida de energía de la señal |
| Distorsión de retardo | Señales llegan con diferente retardo según frecuencia |
| Diafonía (crosstalk) | Interferencia entre cables adyacentes |
| Ruido térmico | Interferencia generada por el calor |

---

## 13. RESUMEN DE RESPUESTAS — SUPUESTO II (CPD SGTIC) 2025

### TAI-P Modelo A — Supuesto II
| Preg | Tema | Respuesta |
|------|------|-----------|
| 1 | Subred 10.30.16.0/25 | **d** (red .0, broadcast .127) |
| 2 | Hosts en /20 | **c** (4094 hosts) |
| 3 | DHCP relay Cisco IOS | **a** (ip helper-address) |
| 4 | Tabla enrutamiento RHEL | **c** (ip route show) |
| 5 | Nginx autostart systemd | **a** (systemctl enable nginx) |
| 6 | Docker kill contenedor | **a** (docker kill 3f7) |
| 7 | Ruta efectiva a IP | **b** (ip route get 10.30.20.30) |
| 8 | Puertos en escucha RHEL | **d** (ss -ltn) |
| 9 | Estrategia 3-2-1 | **c** (3 copias, 2 soportes distintos, 1 fuera sede) |
| 10 | tar -czf backup | **b** |
| 11 | AD dsa.msc | **a** |
| 12 | PowerShell Copy-Item -Recurse | **c** |

### Preguntas de Reserva
| Preg | Tema | Respuesta |
|------|------|-----------|
| 1 | firewall-cmd rich-rule | **d** |
| 2 | sysctl rp_filter IP spoofing | **b** |
| 3 | LVM XFS ampliación | **c** (lvextend + xfs_growfs) |

---

## 14. TABLA COMPARATIVA — HARDWARE Y PROTOCOLOS

### Velocidades de Interfaces
| Interfaz | Velocidad |
|---------|----------|
| HDMI 1.4 | 10.2 Gbps |
| HDMI 2.0 | 18 Gbps |
| **HDMI 2.1** | **48 Gbps** |
| USB 3.0 | 5 Gbps |
| USB 3.1 | 10 Gbps |
| USB4 | 40 Gbps |
| Ethernet Gigabit | 1 Gbps |
| 10GbE | 10 Gbps |

---

*Última actualización: Octubre 2026 — Basado en exámenes oficiales TAI 2022, 2024, 2025*
