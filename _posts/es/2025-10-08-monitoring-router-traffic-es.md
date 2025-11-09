---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Monitoreo del Tráfico de Red del Router
translated: true
type: note
---

### Monitoreo de solicitudes HTTP y conexiones TCP en el router 360 Wi-Fi 6 T7

El 360 T7 ejecuta un firmware personalizado basado en Linux (no es OpenWrt completo de fábrica), por lo que las capacidades de monitoreo son limitadas en la configuración estándar en comparación con un shell de Linux completo. Con derechos de administrador (a través de la interfaz web), puedes acceder a registros básicos. Para un "hacking" más profundo, como el registro de solicitudes HTTP en tiempo real o el rastreo de conexiones TCP, el mejor enfoque ético es instalar OpenWrt (que es compatible oficialmente), habilitar SSH y usar herramientas estándar de Linux. **Advertencia: Instalar firmware personalizado anula la garantía y conlleva el riesgo de bloquear el dispositivo—haz una copia de seguridad primero y sigue las guías cuidadosamente. Solo haz esto en tu propio dispositivo.**

#### 1. **Acceso a derechos de administrador en el firmware original**
   - Conéctate al Wi-Fi del router o vía Ethernet.
   - Abre un navegador y ve a `http://ihome.360.cn` o `http://192.168.0.1` (IP por defecto).
   - Inicio de sesión: Usuario por defecto `admin`, contraseña impresa en la etiqueta del router (a menudo `admin` o una cadena única como `360XXXXXX`—revisa la pegatina en la parte inferior).
   - Una vez dentro, navega a **Sistema > Registro** o **Seguridad > Registro** para ver registros básicos del sistema y de tráfico. Esto muestra bloqueos del firewall, conexiones y alguna actividad HTTP (por ejemplo, sitios bloqueados o intrusiones), pero no detalles completos de las solicitudes HTTP.

   **Monitoreo básico vía Interfaz Web:**
   - **Registros del Sistema**: Ve eventos recientes, incluidos intentos de conexión TCP y errores. Exporta registros (puede requerir la contraseña de la etiqueta para descifrarlos).
   - **Estadísticas de Tráfico**: En **Estado > Red** o **Avanzado > Monitor de Tráfico**, puedes ver el uso de ancho de banda por dispositivo/IP, pero no a nivel granular de HTTP/TCP.
   - Limitaciones: No hay inspección de payload HTTP en tiempo real; los registros son de alto nivel y no se pueden exportar sin autenticación.

#### 2. **Monitoreo avanzado: Instalar OpenWrt para acceso Shell**
   El 360 T7 (chipset MT7981B) es compatible con las snapshots de OpenWrt 23.05+. Instalarlo otorga acceso completo a la shell root vía SSH, donde puedes ejecutar herramientas como `tcpdump` para capturas de paquetes y `logread` para registros.

   **Pasos para instalar OpenWrt (Nivel alto; Usa la Guía Oficial):**
   1. Descarga la imagen factory desde las descargas de OpenWrt (busca "Qihoo 360T7 sysupgrade.bin" o imagen factory).
   2. Haz una copia de seguridad del firmware original: En la interfaz web, ve a **Sistema > Copia de seguridad** y descarga la configuración/firmware.
   3. Cárgalo vía interfaz web: **Sistema > Actualización de Firmware**, selecciona el archivo .bin y aplica (el router se reiniciará en OpenWrt).
   4. Post-instalación: Accede a la interfaz web en `http://192.168.1.1` (interfaz LuCI), usuario `root`, sin contraseña inicialmente—establece una inmediatamente vía SSH o la interfaz de usuario.
   5. Habilita SSH: Está activado por defecto en el puerto 22. Conéctate desde tu PC: `ssh root@192.168.1.1` (usa PuTTY en Windows).

   **Mitigación de Riesgos**: Si se bloquea, usa recuperación por TFTP (mantén presionado reset durante el arranque) o consola serial (requiere adaptador UART).

#### 3. **Monitoreo en OpenWrt (vía SSH Shell)**
   Una vez conectado por SSH como root, el router actúa como un sistema Linux mínimo. Instala paquetes si es necesario vía `opkg update && opkg install tcpdump` (el almacenamiento integrado es de 128MB, así que mantenlo ligero).

   - **Listar todas las conexiones TCP actuales (Vista estática):**
     ```
     ss -tunap
     ```
     - Muestra sockets TCP establecidos/en escucha, puertos, procesos (ej., `tcp ESTAB 0 0 192.168.1.1:80 192.168.1.100:54321 users:(("uhttpd",pid=1234,fd=3))`).
     - Para tiempo real: `watch -n 1 'ss -tunap'`.

   - **Captura de tráfico TCP en tiempo real:**
     Instala si es necesario: `opkg update && opkg install tcpdump`.
     ```
     tcpdump -i any tcp -n -v
     ```
     - `-i any`: Todas las interfaces (br-lan para LAN, eth0.2 para WAN).
     - Filtrar HTTP: `tcpdump -i any tcp port 80 -n -v -A` (`-A` muestra el payload ASCII para cabeceras/solicitudes HTTP).
     - Guardar en archivo: `tcpdump -i any tcp -w /tmp/capture.pcap` (descarga vía SCP: `scp root@192.168.1.1:/tmp/capture.pcap .`).
     - Para HTTPS (puerto 443), ten en cuenta que los payloads están cifrados—usa Wireshark offline para el análisis.

   - **Monitorear registros de solicitudes HTTP:**
     - Registros del sistema (incluye el servidor web si se usa uhttpd): `logread | grep uhttpd` o `logread -f` para tiempo real.
     - Habilita el registro detallado de HTTP: Edita `/etc/config/uhttpd` (configuración del servidor web), añade `option log_file '/var/log/uhttpd.log'`, luego `/etc/init.d/uhttpd restart`. Sigue en tiempo real: `tail -f /var/log/uhttpd.log` (muestra solicitudes GET/POST, IPs, URLs).
     - Para HTTP completo de la red: Usa `tcpdump` como arriba, o instala `ngrep` (`opkg install ngrep`): `ngrep -d any 'GET|POST|HTTP' -O /tmp/http.pcap`.

   - **Registros del Firewall/Conexiones:**
     - Habilita el registro en reglas: `uci set firewall.@rule[0].log='1'; uci commit; /etc/init.d/firewall restart`.
     - Ver: `logread | grep fw` (muestra conexiones TCP aceptadas/bloqueadas).

#### Consejos para "Hacking" Ético
- **Seguridad**: Después de la configuración, cambia la contraseña de root (`passwd`), deshabilita la autenticación por contraseña en `/etc/ssh/sshd_config` para que sea solo por clave, y restringe el firewall SSH solo a la LAN.
- **Rendimiento**: El T7 tiene 256MB de RAM—evita capturas pesadas a largo plazo para prevenir falta de memoria (OOM).
- **Revertir al firmware original**: Descarga el firmware oficial del sitio de 360, cárgalo vía sysupgrade de OpenWrt (con `--force` si es necesario).
- Prueba en un entorno seguro; para análisis con GUI, transfiere el .pcap al PC vía SCP y ábrelo en Wireshark.

Esto otorga una visibilidad integral. Si la interfaz de usuario original es suficiente para lo básico, quédate allí para evitar la instalación de firmware personalizado.

[OpenWrt Techdata: Qihoo 360T7](https://openwrt.org/toh/hwdata/qihoohardware/qihoohardware_360t7)  
[Manual 360 T7U (Sección de Registros)](https://ipc-pr-cdn.jia.360.cn/ipc-pr/luyouqiT7U.pdf)  
[Guía de Registros de OpenWrt](https://openwrt.org/docs/guide-user/base-system/log.essentials)  
[Foro 360: Exportación de Registros](https://bbs.360.cn/forum-7007-1.html)