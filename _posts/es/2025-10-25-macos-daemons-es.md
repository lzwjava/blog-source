---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Procesos Daemon Predeterminados de macOS
translated: true
type: note
---

### Procesos Daemon Predeterminados en macOS

En macOS, los procesos daemon son servicios en segundo plano que se ejecutan sin una interfaz de usuario, típicamente iniciándose en el arranque o bajo demanda. Son gestionados por **launchd**, el framework de inicialización y gestión de servicios del sistema (PID 1). Los daemons se diferencian de los agentes: los daemons se ejecutan como root/a nivel del sistema (antes del inicio de sesión), mientras que los agentes se ejecutan por usuario (después del inicio de sesión).

Los daemons predeterminados del sistema se definen en archivos de lista de propiedades (.plist) ubicados en `/System/Library/LaunchDaemons/`. Típicamente hay alrededor de 300–350 de estos en una instalación estándar (por ejemplo, 339 en macOS 10.14 Mojave), cubriendo todo desde redes y seguridad hasta gestión de hardware. Los daemons instalados por el usuario o de terceros van en `/Library/LaunchDaemons/`.

#### Cómo Ver los Daemons Predeterminados
Para listar todos los daemons (y agentes) cargados en la Terminal:
- `sudo launchctl list` (muestra daemons y agentes a nivel del sistema).
- `launchctl list` (muestra solo agentes específicos del usuario).

Para un listado completo del directorio: `ls /System/Library/LaunchDaemons/` (no requiere sudo, pero los archivos son de solo lectura).

Estos comandos muestran columnas como PID, estado y etiqueta (por ejemplo, `com.apple.timed`).

#### El Daemon "timed"
Mencionaste específicamente "timed", que se refiere a **com.apple.timed** (el Daemon de Sincronización de Tiempo). Este es un daemon central del sistema introducido en macOS High Sierra (10.13) para reemplazar el proceso más antiguo `ntpd`.

- **Propósito**: Sincroniza automáticamente el reloj del sistema del Mac con servidores NTP (Network Time Protocol) para garantizar precisión, consultándolos cada 15 minutos. Esto asegura una cronometría precisa para registros, certificados y operaciones de red.
- **Cómo funciona**: Es lanzado por launchd desde `/System/Library/LaunchDaemons/com.apple.timed.plist`, y se ejecuta como el usuario `_timed` (en los grupos `_timed` y `_sntpd`). Utiliza la llamada al sistema `settimeofday` para ajustar el reloj basándose en las respuestas del servidor. La configuración está en `/etc/ntpd.conf` (servidores NTP) y el estado se almacena en caché en `/var/db/timed/com.apple.timed.plist`.
- **Relacionado**: Se vincula a Configuración del Sistema > General > Fecha y Hora > "Establecer fecha y hora automáticamente". Si está desactivado, timed no sincronizará. Para configuraciones avanzadas (por ejemplo, necesidades de alta precisión), herramientas como Chrony pueden reemplazarlo, pero se debe desactivar timed.

Si tu reloj se desvía, verifica problemas de red o bloqueos del firewall en NTP (puerto UDP 123).

#### Otros Daemons Predeterminados Comunes ("etc.")
Aquí hay una tabla de algunos daemons predeterminados del sistema que se ejecutan con frecuencia, agrupados por función. Esto no es exhaustivo (hay cientos), pero cubre los esenciales. Las etiquetas son de los nombres de archivo .plist.

| Categoría       | Etiqueta del Daemon           | Descripción |
|----------------|-------------------------------|-------------|
| **Sistema Central** | `com.apple.launchd`          | El proceso launchd en sí; inicia todos los demás. |
| **Tiempo y Sincronización** | `com.apple.timed`             | Sincronización de tiempo NTP (como se indicó arriba). |
| **Gestión de Usuarios** | `com.apple.opendirectoryd`   | Maneja cuentas de usuario/grupo y servicios de directorio. |
| **Gestión de Usuarios** | `com.apple.accounts`         | Gestiona cuentas de usuario y autenticación. |
| **Redes** | `com.apple.mDNSResponder`    | Bonjour/mDNS para descubrimiento de red local (por ejemplo, AirDrop). |
| **Redes** | `com.apple.nesessionmanager` | Gestión de extensiones de red y VPN. |
| **Bluetooth/Inalámbrico** | `com.apple.bluetoothd`      | Manejo de dispositivos Bluetooth. |
| **iCloud/Sincronización** | `com.apple.cloudd`            | Sincronización de datos y servicios de iCloud. |
| **Seguridad**   | `com.apple.securityd`        | Gestión del llavero y credenciales (a menudo también como agente). |
| **Actualizaciones**    | `com.apple.softwareupdated`  | Maneja las actualizaciones de software y descargas de catálogos. |
| **Hardware**   | `com.apple.kextd`             | Carga y gestión de extensiones del kernel. |
| **Registro**    | `com.apple.systemnotificationd` | Notificaciones del sistema y registro. |
| **MDM (si está habilitado)** | `com.apple.mdmclient`     | Cliente de Mobile Device Management para configuraciones empresariales. |

Estos se ejecutan continuamente o por eventos para mantener estable macOS. Si uno se comporta mal (por ejemplo, uso alto de CPU), puedes descargarlo temporalmente con `sudo launchctl unload /System/Library/LaunchDaemons/com.apple.example.plist`, pero evita modificar archivos del sistema.

Para una lista completa y actual en tu Mac (a partir de octubre de 2025, probablemente macOS 15 Sequoia o posterior), ejecuta los comandos anteriores—las versiones evolucionan ligeramente con las actualizaciones.

#### Referencias
- [The macOS Process Journey — “timed” (Time Sync Daemon)](https://medium.com/@boutnaru/the-macos-process-journey-timed-time-sync-daemon-4898c8185b4b)
- [Daemons and Agents could be slowing down your Mac](https://appleinsider.com/inside/macos/tips/daemons-and-agents-could-be-slowing-down-your-mac)
- [What files are included in the /System/Library/LaunchAgents and /System/Library/LaunchDaemons](https://apple.stackexchange.com/questions/361029/what-files-are-included-in-the-system-library-launchagents-and-system-library)
- [Script management with launchd in Terminal on Mac](https://support.apple.com/guide/terminal/script-management-with-launchd-apdc6c1077b-5d5d-4d35-9c19-60f2397b2369/mac)
- [How to show all running launchctl daemons/agents?](https://apple.stackexchange.com/questions/134817/how-to-show-all-running-launchctl-daemons-agents)