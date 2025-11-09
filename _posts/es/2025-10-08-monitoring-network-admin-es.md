---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Monitoreo de Actividad de Red con Derechos de Administrador
translated: true
type: note
---

### Monitoreo de Peticiones HTTP y Conexiones TCP con Derechos de Administrador

Asumiendo que estás trabajando en un sistema tipo Linux/Unix (por ejemplo, Ubuntu, CentOS) con privilegios de root/administrador, puedes monitorear la actividad de la red de forma ética para resolución de problemas, auditoría de seguridad o pentesting. **Importante: Solo haz esto en sistemas que sean tuyos o para los que tengas permiso explícito—el monitoreo no autorizado es ilegal.** Me centraré en herramientas de línea de comandos, que son ligeras y no requieren interfaz gráfica.

#### 1. **Monitorear Todas las Conexiones TCP**
   Utiliza herramientas integradas como `ss` (reemplazo moderno de `netstat`) o `tcpdump` para captura en tiempo real. Estas muestran conexiones activas, puertos y procesos.

   - **Listar todas las conexiones TCP actuales (vista estática):**
     ```
     sudo ss -tunap
     ```
     - `-t`: Solo TCP.
     - `-u`: UDP si se necesita (pero pediste TCP).
     - `-n`: Puertos numéricos (sin resolución DNS).
     - `-a`: Todos los estados (established, listening, etc.).
     - `-p`: Mostrar procesos propietarios.
     Ejemplo de salida:
     ```
     tcp   ESTAB  0      0      192.168.1.10:80     10.0.0.5:54321    users:(("nginx",pid=1234,fd=5))
     ```
     Solo para sockets en escucha: `sudo ss -tlnp`.

   - **Monitoreo en tiempo real con watch:**
     ```
     watch -n 1 'sudo ss -tunap'
     ```
     Se actualiza cada segundo.

   - **Capturar tráfico TCP en vivo (a nivel de paquete):**
     Instala `tcpdump` si no está presente: `sudo apt update && sudo apt install tcpdump` (Debian/Ubuntu) o `sudo yum install tcpdump` (RHEL/CentOS).
     ```
     sudo tcpdump -i any tcp -n -v
     ```
     - `-i any`: Todas las interfaces.
     - `-n`: Sin resolución de nombres.
     - `-v`: Verboso.
     Añade `port 80 or port 443` para filtrar HTTP/HTTPS: `sudo tcpdump -i any tcp port 80 or tcp port 443 -n -v -A` (`-A` para el payload en ASCII, para ver cabeceras HTTP).

     Guarda en un archivo para análisis posterior: `sudo tcpdump -i any tcp -w capture.pcap`.

#### 2. **Monitorear Registros de Peticiones HTTP**
   Los registros HTTP dependen de tu servidor web (Apache, Nginx, etc.). Si no hay un servidor web en ejecución, usa la captura de red (anterior) para inspeccionar el tráfico HTTP. Para registros específicos del servidor:

   - **Apache (httpd):**
     Los registros típicamente están en `/var/log/apache2/access.log` (Ubuntu) o `/var/log/httpd/access_log` (CentOS).
     ```
     sudo tail -f /var/log/apache2/access.log
     ```
     - Muestra peticiones en tiempo real: IP, marca de tiempo, método (GET/POST), URL, código de estado.
     Línea de ejemplo: `192.168.1.100 - - [08/Oct/2025:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234`.

     Para todos los registros: `sudo grep "GET\|POST" /var/log/apache2/access.log | less`.

   - **Nginx:**
     Registros en `/var/log/nginx/access.log`.
     ```
     sudo tail -f /var/log/nginx/access.log
     ```
     Formato similar a Apache.

   - **Si no hay servidor web (rastreo HTTP general):**
     Usa `tcpdump` como antes con `-A` para volcar payloads HTTP, o instala `ngrep` para coincidencia con regex:
     ```
     sudo apt install ngrep  # Instalar si es necesario
     sudo ngrep -d any 'GET|POST|HTTP' -O http_capture.pcap
     ```
     Esto filtra y registra métodos HTTP.

   - **Avanzado: Configurar un proxy transparente para registro completo.**
     Instala el proxy Squid: `sudo apt install squid`.
     Configura `/etc/squid/squid.conf` para registrar todo el HTTP (añade `access_log /var/log/squid/access.log squid`).
     Redirige el tráfico via iptables: `sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 3128`.
     Luego haz tail del registro de Squid: `sudo tail -f /var/log/squid/access.log`.

#### Consejos para "Hacking" (Pentesting Ético)
- **Combina herramientas:** Conecta la salida de `tcpdump` a `grep` para patrones específicos, ej., `sudo tcpdump -i any tcp port 80 -A | grep "User-Agent"`.
- **Visualiza con Wireshark:** Para análisis con GUI, instala Wireshark (`sudo apt install wireshark`), ejecuta como root y abre tu archivo `.pcap`.
- **Refuerzo de seguridad:** Después del monitoreo, borra los registros si son sensibles: `sudo truncate -s 0 /var/log/access.log`.
- **Nota multiplataforma:** En Windows (con admin), usa `netstat -anob` para TCP y el Visor de Eventos para registros. En macOS, `netstat -an` y `tcpdump`.

Esta configuración te da una visibilidad completa sin herramientas externas. Prueba primero en una máquina virtual.

[Página del Manual del Comando Linux ss](https://man7.org/linux/man-pages/man8/ss.8.html)  
[Tutorial de Tcpdump](https://www.tcpdump.org/manpages/tcpdump.1.html)  
[Formato del Registro de Acceso de Apache](https://httpd.apache.org/docs/2.4/logs.html)