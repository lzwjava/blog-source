---
audio: false
generated: true
lang: es
layout: post
title: Un Problema de Infuse
translated: true
type: note
---

El error "Failed to open input stream in demuxing stream" en Infuse normalmente indica que la aplicación no puede acceder o procesar correctamente el archivo de video que intentas reproducir en streaming. Dado que estás transmitiendo archivos `.mkv` desde tu servidor Nginx (por ejemplo, `http://192.168.1.27/movies/yourfile.mkv`) y funciona con VLC pero no con Infuse, el problema podría deberse a problemas de red, compatibilidad de archivos o peculiaridades específicas de Infuse. Aquí te explicamos cómo solucionarlo:

### 1. Verificar la conectividad de red
Infuse a menudo muestra este error debido a interrupciones o configuraciones incorrectas de la red.
- **Probar la accesibilidad**: Desde tu iPad (o donde sea que se esté ejecutando Infase), asegúrate de que la URL funcione:
  - Abre Safari y ve a `http://192.168.1.27/movies/`. Deberías ver la lista de archivos.
  - Toca `yourfile.mkv`—puede que no se reproduzca, pero confirma que el enlace es accesible.
- **Hacer ping al servidor**: En tu iPad, usa una aplicación como **Network Ping Lite** (gratuita en la App Store) para hacer ping a `192.168.1.27`. Si falla, revisa tu Wi-Fi o el firewall del servidor.
- **Comprobar el firewall**: En tu servidor Ubuntu:
  ```bash
  sudo ufw status
  ```
  Asegúrate de que el puerto 80 esté abierto (`80/tcp ALLOW`). Si no lo está:
  ```bash
  sudo ufw allow 80
  sudo systemctl restart nginx
  ```

### 2. Reiniciar Infuse y el dispositivo
Los fallos temporales pueden causar este error.
- **Cerrar Infuse**: Presiona dos veces el botón de inicio (o desliza el dedo hacia arriba en los iPad más nuevos) y desliza Infuse para cerrarlo.
- **Reabrir**: Inicia Infuse e intenta la transmisión de nuevo.
- **Reiniciar el iPad**: Mantén presionado el botón de encendido, desliza para apagar y luego reinicia. Prueba de nuevo.

### 3. Comprobar la compatibilidad del archivo
Aunque Infuse admite `.mkv`, el error podría estar relacionado con los códecs o la estructura del archivo.
- **Probar otro archivo**: Sube un `.mkv` pequeño y que funcione correctamente (por ejemplo, codificado con video H.264 y audio AAC) a `/var/www/movies/`:
  ```bash
  sudo mv /path/to/testfile.mkv /var/www/movies/
  sudo chown www-data:www-data /var/www/movies/testfile.mkv
  sudo chmod 644 /var/www/movies/testfile.mkv
  ```
  Intenta transmitir `http://192.168.1.27/movies/testfile.mkv` en Infuse.
- **Comprobar códecs**: Dado que VLC lo reproduce, es probable que el archivo se pueda transmitir, pero Infuse podría tener problemas con códecs poco comunes (por ejemplo, VP9, Opus). Usa VLC en tu Mac para inspeccionarlo:
  - Abre el `.mkv`, presiona `Cmd + I` (Herramientas > Información del Códec) y anota los códecs de video/audio.
  - Si no es H.264/AAC, vuelve a codificarlo con HandBrake (gratuito, handbrake.fr):
    - Carga el `.mkv`, selecciona video "H.264 (x264)" y audio "AAC", luego convierte.

### 4. Ajustar la configuración de Nginx
Es posible que Infuse necesite cabeceras o configuraciones específicas para una transmisión sin problemas.
- **Actualizar la configuración**: Edita tu archivo de Nginx (por ejemplo, `/etc/nginx/sites-enabled/default`):
  ```nginx
  server {
      listen 80;
      server_name 192.168.1.27 localhost;

      location /movies/ {
          alias /var/www/movies/;
          autoindex on;
          add_header Accept-Ranges bytes;  # Asegura que funcionen las solicitudes de rango
          add_header Content-Disposition "inline";  # Ayuda a la transmisión
      }
  }
  ```
- **Recargar**:
  ```bash
  sudo nginx -t
  sudo systemctl reload nginx
  ```
- **Por qué**: `Accept-Ranges` asegura que Infuse pueda solicitar partes del archivo (crítico para la transmisión).

### 5. Enviar un informe de diagnóstico
Los desarrolladores de Infuse sugieren esto para problemas persistentes.
- **Pasos**:
  1. En Infuse, ve a **Configuración > General**.
  2. Toca **Enviar informe de diagnóstico**.
  3. Anota el código que te da.
  4. Visita el [Foro de la Comunidad de Firecore](https://community.firecore.com/), publica el código y describe tu configuración (Nginx, `.mkv`, transmisión HTTP).
- **Por qué**: Ellos pueden identificar si es un error o un problema de configuración.

### 6. Solución alternativa
Si Infuse sigue fallando:
- **Usar VLC**: Quédate con VLC for Mobile en tu iPad (ya que funciona de forma fiable).
- **Cambiar de aplicación**: Prueba **nPlayer** o **PlayerXtreme** (App Store) con la misma URL.

### Causa probable
Dado que VLC lo transmite bien, probablemente sea un problema de red o el manejo más estricto que hace Infuse de la transmisión HTTP. El ajuste de Nginx (paso 4) y un archivo de prueba (paso 3) suelen resolver esto. Si no, el informe de diagnóstico lo aclarará.

¡Déjame saber qué ves después de probar esto—especialmente cualquier error en los registros o el código de diagnóstico