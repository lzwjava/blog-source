---
audio: false
generated: true
lang: es
layout: post
title: Configuración de qBittorrent para Siembra y Gestión Automática de Archivos
translated: true
type: note
---

Parece que deseas configurar qBittorrent para que continúe sembrando (seeding) tus torrents mientras mueve automáticamente los archivos `.mkv` completados a `/var/www/movies` para servirlos en un servidor. A continuación, te guiaré a través de los pasos para lograr esto, asumiendo que estás usando qBittorrent en un sistema donde `/var/www/movies` es un directorio válido (por ejemplo, un servidor Linux con un servidor web como Apache o Nginx). Así es como puedes configurarlo:

---

### Guía Paso a Paso

#### 1. **Comprender la Gestión de Archivos de qBittorrent**
   - qBittorrent puede mover archivos automáticamente después de completar la descarga mientras continúa sembrando, siempre y cuando uses sus funciones integradas "Establecer ubicación" o "Mover" correctamente. Mover archivos manualmente fuera de qBittorrent (por ejemplo, mediante un explorador de archivos) interrumpirá la siembra a menos que re-dirijas qBittorrent a la nueva ubicación.

#### 2. **Configurar los Ajustes de qBittorrent**
   - Abre qBittorrent.
   - Ve a **Herramientas > Opciones** (o presiona `Alt + O`).

   ##### a) **Establecer la Ubicación de Descarga Predeterminada**
   - En la pestaña **Descargas**:
     - Establece **Ruta de guardado predeterminada** en un directorio temporal donde los archivos se descargarán inicialmente (por ejemplo, `/home/usuario/descargas` o donde tengas espacio). Aquí es donde qBittorrent almacenará los archivos mientras descarga y siembra hasta que sean movidos.
     - Asegúrate de que **Mantener archivos incompletos en** esté establecido en el mismo directorio o en uno diferente si lo prefieres (opcional).

   ##### b) **Habilitar el Movimiento Automático de Archivos**
   - Desplázate hacia abajo hasta **Cuando el torrent finalice**:
     - Marca la casilla para **Mover automáticamente las descargas completadas a**.
     - Establece la ruta a `/var/www/movies`. Esto le indica a qBittorrent que mueva los archivos `.mkv` a `/var/www/movies` una vez que la descarga se complete.
   - Importante: qBittorrent continuará sembrando desde la nueva ubicación (`/var/www/movies`) después del movimiento, por lo que no necesitas preocuparte por perder la capacidad de siembra.

   ##### c) **Opcional: Filtrar Archivos .mkv**
   - Si solo quieres que los archivos `.mkv` se muevan a `/var/www/movies` (y no otros tipos de archivos como `.txt` o `.nfo`), puedes usar la función **Ejecutar programa externo** de qBittorrent (ver Paso 3 a continuación) en lugar de la opción de movimiento automático.

   ##### d) **Límites de Siembra**
   - En la pestaña **BitTorrent** o **Descargas**:
     - Establece los límites de siembra si lo deseas (por ejemplo, sembrar hasta alcanzar una relación o tiempo determinado). Para una siembra ilimitada, establece **Relación** y **Tiempo** en `0` o desmarca los límites.
     - Esto asegura que qBittorrent mantenga subiendo tus semillas indefinidamente desde `/var/www/movies`.

   - Haz clic en **Aplicar** y **Aceptar** para guardar la configuración.

#### 3. **Alternativa: Usar "Ejecutar Programa Externo" para Más Control**
   - Si necesitas más personalización (por ejemplo, mover solo archivos `.mkv` y dejar otros sembrando desde la ubicación original), usa esto:
     - En **Opciones > Descargas**, desplázate a **Ejecutar programa externo**.
     - Marca **Ejecutar programa externo al completarse el torrent**.
     - Ingresa un comando como:
       ```
       mv "%F"/*.mkv /var/www/movies/
       ```
       - `%F` es un marcador de posición de qBittorrent para la ruta de la carpeta del contenido. Este comando mueve solo los archivos `.mkv` a `/var/www/movies`.
     - Nota: qBittorrent seguirá sembrando los archivos `.mkv` desde `/var/www/movies` después del movimiento, pero otros archivos (por ejemplo, `.torrent`, `.nfo`) permanecerán en la ubicación original y continuarán sembrando desde allí a menos que ajustes más cosas.

#### 4. **Verificar los Permisos**
   - Asegúrate de que qBittorrent tenga permisos de escritura en `/var/www/movies`:
     - En Linux, ejecuta:
       ```
       sudo chown -R <usuario-qbittorrent>:<grupo-qbittorrent> /var/www/movies
       sudo chmod -R 775 /var/www/movies
       ```
       Reemplaza `<usuario-qbittorrent>` y `<grupo-qbittorrent>` con el usuario y grupo bajo los cuales se ejecuta qBittorrent (por ejemplo, tu nombre de usuario o `qbittorrent` si es un servicio).
   - Sin los permisos adecuados, qBittorrent no podrá mover archivos a este directorio.

#### 5. **Probar la Configuración**
   - Añade un torrent con archivos `.mkv` a qBittorrent.
   - Espera a que termine de descargar.
   - Verifica que:
     - Los archivos `.mkv` se muevan a `/var/www/movies`.
     - El estado del torrent en qBittorrent cambie a **Sembrando**, y la velocidad de subida indique que todavía está compartiendo los archivos.
   - Visita `/var/www/movies` para confirmar que los archivos estén allí y sean accesibles (por ejemplo, a través de tu servidor web en `http://<ip-del-servidor>/movies`).

#### 6. **Mover Archivos Existentes Manualmente (Si es Necesario)**
   - Para torrents que ya has descargado y quieres mover a `/var/www/movies` sin interrumpir la siembra:
     - En qBittorrent, haz clic derecho en el torrent.
     - Selecciona **Establecer ubicación**.
     - Elige `/var/www/movies` y permite que qBittorrent mueva los archivos.
     - Después del movimiento, qBittorrent reanudará la siembra desde la nueva ubicación.

#### 7. **Optimizar la Configuración de Subida**
   - Para maximizar la siembra:
     - Ve a **Opciones > Velocidad**:
       - Establece **Subida** en `0` (ilimitada) o en un valor alto (por ejemplo, 80% de tu velocidad máxima de subida).
     - Ve a **Opciones > Conexión**:
       - Asegúrate de que **Habilitar reenvío de puertos UPnP / NAT-PMP** esté marcado (si tu router lo soporta) o reenvía un puerto manualmente para una mejor conectividad.
       - Aumenta **Número máximo global de espacios de subida** (por ejemplo, a 50 o 100) para permitir que más pares se conecten.

---

### Notas Clave
- **Continuidad de la Siembra**: Siempre que dejes que qBittorrent maneje el movimiento de archivos (mediante movimiento automático o "Establecer ubicación"), este actualizará su seguimiento interno y continuará sembrando desde `/var/www/movies`.
- **Acceso al Servidor Web**: Asegúrate de que tu servidor web (por ejemplo, Apache/Nginx) esté configurado para servir archivos desde `/var/www/movies`. Esto está fuera del alcance de qBittorrent pero es crítico para tu objetivo de servidor.
- **Almacenamiento**: Asegúrate de que `/var/www/movies` tenga suficiente espacio para tus archivos.

Si encuentras problemas (por ejemplo, los archivos no se mueven o la siembra se detiene), ¡házmelo saber con los detalles de tu configuración (SO, versión de qBittorrent, etc.) y afinaré la solución!