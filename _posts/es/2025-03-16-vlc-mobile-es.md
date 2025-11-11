---
audio: false
generated: true
lang: es
layout: post
title: Transmisión de archivos MKV en iPad con VLC Mobile y otras aplicaciones
translated: true
type: note
---

Para transmitir tus archivos `.mkv` desde tu servidor Nginx (por ejemplo, `http://192.168.1.27/movies/`) en tu iPad sin descargarlos por completo, necesitarás una aplicación que admita transmisión HTTP y reproducción de `.mkv`. iPadOS no maneja bien los archivos `.mkv` de forma nativa en Safari o la aplicación Archivos, por lo que un reproductor multimedia de terceros es el camino a seguir. Así es como puedes lograr esa "magia" en tu iPad:

### Aplicaciones Recomendadas para Transmitir `.mkv` en iPad
#### 1. VLC for Mobile (Gratuita, Mejor Opción)
VLC está disponible en iPadOS y funciona de manera similar a la versión para Mac, admitiendo transmisión HTTP con solicitudes de rango.
- **Instalar**:
  1. Abre la **App Store** en tu iPad.
  2. Busca **VLC for Mobile**.
  3. Toca **Obtener** (o el icono de la nube si lo has instalado antes), luego autentícate con tu Apple ID si se solicita.
- **Transmitir**:
  1. Abre la aplicación **VLC**.
  2. Toca la pestaña **Network** (icono de cono) en la parte inferior.
  3. Selecciona **Open Network Stream**.
  4. Ingresa `http://192.168.1.27/movies/tuarchivo.mkv`.
  5. Toca **Open Network Stream** (o el botón de reproducción).
- **Por qué funciona**: VLC almacena en búfer la transmisión, permitiéndote reproducir y buscar sin descargar el archivo completo.

#### 2. nPlayer (De Pago, Opción Premium)
nPlayer es un reproductor multimedia potente con excelente soporte para `.mkv` y capacidades de transmisión.
- **Instalar**:
  1. Abre la **App Store**.
  2. Busca **nPlayer** (cuesta alrededor de $8.99, pero hay una versión lite gratuita con anuncios).
  3. Toca **Obtener** o **Comprar**, luego instálalo.
- **Transmitir**:
  1. Abre **nPlayer**.
  2. Toca el icono **+** o la opción **Network**.
  3. Selecciona **Add URL** o **HTTP/HTTPS**.
  4. Ingresa `http://192.168.1.27/movies/tuarchivo.mkv`.
  5. Toca **Play**.
- **Por qué funciona**: Admite códecs avanzados y transmisión fluida; gran interfaz de usuario para iPad.

#### 3. Infuse (Gratuita con Compras In-App)
Infuse es otra opción popular para transmitir y reproducir archivos `.mkv`, con una interfaz elegante.
- **Instalar**:
  1. Abre la **App Store**.
  2. Busca **Infuse**.
  3. Toca **Obtener** (el nivel gratuito funciona para la transmisión básica; la actualización a Pro es opcional).
- **Transmitir**:
  1. Abre **Infuse**.
  2. Toca **Add Files** > **Via URL**.
  3. Ingresa `http://192.168.1.27/movies/tuarchivo.mkv`.
  4. Toca **Add** o **Play**.
- **Por qué funciona**: Transmite por HTTP y maneja bien los `.mkv`; las funciones Pro (como AirPlay) son opcionales.

### Pasos para Comenzar
1. **Conéctate a la Misma Red**:
   - Asegúrate de que tu iPad esté en la misma red Wi-Fi que tu servidor Nginx (por ejemplo, `192.168.1.x`).
   - Prueba la conectabilidad: Abre Safari en tu iPad y ve a `http://192.168.1.27/movies/`. Deberías ver la lista de archivos (incluso si Safari no puede reproducir `.mkv`).

2. **Elige una Aplicación**:
   - **VLC** es gratuita y confiable—comienza aquí.
   - Instálala desde la App Store como se describió.

3. **Ingresa la URL**:
   - Usa la URL exacta de tu archivo `.mkv` (por ejemplo, `http://192.168.1.27/movies/tuarchivo.mkv`).
   - Puedes copiar el enlace desde el listado de archivos en Safari y pegarlo en la aplicación.

4. **Reproduce y Disfruta**:
   - La aplicación transmitirá el video. Puedes pausar, buscar o ajustar la reproducción sin descargar el archivo completo.

### Solución de Problemas
- **Falla la Conexión**: Si el iPad no puede alcanzar `192.168.1.27`, asegúrate de que el firewall del servidor permita el puerto 80 (`sudo ufw allow 80`) y de que el iPad esté en la misma LAN.
- **Buffering**: Una Wi-Fi lenta puede causar retrasos—acércate al router o verifica la velocidad de tu red.
- **Problemas de Códec**: Si el `.mkv` no se reproduce, podría usar un códec no compatible (por ejemplo, VP9). VLC maneja la mayoría, pero podrías recodificar con HandBrake a H.264/AAC para una compatibilidad más amplia.
- **Error Tipográfico en la URL**: Verifica dos veces la IP y la ruta—`http://192.168.1.27/movies/tuarchivo.mkv` debe coincidir con tu configuración.

### Extra: Navegar y Seleccionar
Dado que `autoindex on;` te da un listado de directorio:
- Abre Safari en tu iPad, ve a `http://192.168.1.27/movies/`, toca un enlace de archivo y luego copia la URL.
- Pégala en VLC/nPlayer/Infuse para transmitir.

Con **VLC for Mobile**, tendrás esa "magia" en tu iPad en poco tiempo—¡transmitiendo tus archivos `.mkv` sin esfuerzo! Avísame si necesitas ayuda para configurarlo.