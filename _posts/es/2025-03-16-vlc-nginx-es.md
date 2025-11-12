---
audio: false
generated: true
lang: es
layout: post
title: Transmisión de Archivos MKV desde Nginx con VLC
translated: true
type: note
---

Dado que tienes un servidor Nginx sirviendo archivos `.mkv` (por ejemplo, en `http://192.168.1.27/movies/`) y quieres verlos desde un Mac sin descargar el archivo completo, lo que buscas es **transmitir** (hacer streaming) los videos. Nginx puede servir archivos de manera que admita solicitudes de rango HTTP (lo cual hace por defecto), permitiendo que los reproductores multimedia transmitan en lugar de descargar completamente. Aquí te explicamos cómo hacerlo, junto con herramientas adecuadas para macOS.

### Prerrequisitos
- Tu configuración de Nginx (ej., `alias /var/www/movies/; autoindex on;`) funciona correctamente y `http://192.168.1.27/movies/` lista los archivos.
- Los archivos `.mkv` son accesibles a través de la red (probado desde otra máquina).

### Herramientas para Transmitir Archivos `.mkv` en macOS
Necesitas un reproductor multimedia que admita transmisión vía HTTP y maneje bien los archivos `.mkv`. Estas son las mejores opciones:

#### 1. VLC Media Player (Gratuito, Recomendado)
VLC es un reproductor versátil y de código abierto que admite la transmisión de archivos `.mkv` a través de HTTP sin descargar el archivo completo (utiliza solicitudes de rango).
- **Instalar**:
  - Descárgalo desde [videolan.org](https://www.videolan.org/vlc/).
  - Instálalo en tu Mac.
- **Transmitir**:
  1. Abre VLC.
  2. Presiona `Cmd + N` (o ve a `Archivo > Abrir Red`).
  3. Ingresa la URL, ej., `http://192.168.1.27/movies/tuarchivo.mkv`.
  4. Haz clic en `Abrir`.
- **Por qué funciona**: VLC almacena en búfer solo lo necesario, permitiéndote buscar y reproducir sin descargar el archivo completo.

#### 2. IINA (Gratuito, Nativo de macOS)
IINA es un reproductor moderno, específico para macOS, con excelente soporte para `.mkv` y capacidades de transmisión.
- **Instalar**:
  - Descárgalo desde [iina.io](https://iina.io/) o `brew install iina` (con Homebrew).
- **Transmitir**:
  1. Abre IINA.
  2. Presiona `Cmd + U` (o `Archivo > Abrir URL`).
  3. Ingresa `http://192.168.1.27/movies/tuarchivo.mkv`.
  4. Haz clic en `Aceptar`.
- **Por qué funciona**: Ligero, admite transmisión HTTP y se integra muy bien con macOS.

#### 3. QuickTime Player (Integrado, Soporte Limitado)
El reproductor predeterminado de macOS, QuickTime Player, puede transmitir algunos formatos, pero el soporte para `.mkv` es irregular sin códecs adicionales.
- **Pruébalo**:
  1. Abre QuickTime Player.
  2. Presiona `Cmd + U` (o `Archivo > Abrir Ubicación`).
  3. Ingresa `http://192.168.1.27/movies/tuarchivo.mkv`.
  4. Haz clic en `Abrir`.
- **Advertencia**: Si no funciona, instala Perian (un paquete de códecs antiguo) o usa VLC/IINA en su lugar.

#### 4. Navegador (Safari/Chrome, Más Simple)
Los navegadores modernos pueden transmitir archivos `.mkv` directamente si están codificados con códecs compatibles (ej., video H.264, audio AAC).
- **Cómo**:
  1. Abre Safari o Chrome en tu Mac.
  2. Ve a `http://192.168.1.27/movies/`.
  3. Haz clic en `tuarchivo.mkv`.
- **Por qué funciona**: Los navegadores utilizan etiquetas de video HTML5 y solicitudes de rango para la transmisión.
- **Limitación**: Si el `.mkv` utiliza códecs no compatibles (ej., VP9, Opus), no se reproducirá—recurre a VLC o IINA.

### Asegurar que Nginx Admite la Transmisión
Nginx maneja las solicitudes de rango por defecto, lo que permite la transmisión. Para confirmar:
- Verifica que tu configuración no lo desactive (ej., que no haya `limit_rate` o cabeceras personalizadas bloqueando rangos).
- Prueba con VLC o IINA—si puedes buscar (ej., saltar a 5 minutos), la transmisión está funcionando.

### Flujo de Trabajo Recomendado
1. **Usa VLC** (es el más confiable):
   - Instala VLC.
   - Abre `http://192.168.1.27/movies/tuarchivo.mkv` vía `Cmd + N`.
   - Reproduce, pausa o busca según sea necesario.
2. **Navegación de Directorios**:
   - Visita `http://192.168.1.27/movies/` en Safari/Chrome para ver la lista de archivos (gracias a `autoindex on;`).
   - Copia la URL de `tuarchivo.mkv` y pégala en VLC o IINA.

### Resolución de Problemas
- **Problemas de Búfer**: Una red lenta o archivos `.mkv` grandes podrían causar retrasos—asegúrate de que tu LAN sea estable (ej., que el Wi-Fi no se esté cayendo).
- **Errores de Códec**: Si VLC dice "formato no soportado", el `.mkv` podría usar códecs poco comunes—intenta recodificarlo con HandBrake a H.264/AAC.
- **Conexión Rechazada**: Revisa la configuración del firewall en el servidor (`sudo ufw allow 80` o equivalente).

Con VLC o IINA, estarás transmitiendo tus archivos `.mkv` desde tu Mac en poco tiempo sin tener que descargarlos completamente. ¡Avísame si tienes algún problema!

---

Instalar VLC en un Mac es sencillo. Aquí tienes una guía rápida para configurarlo y poder transmitir tus archivos `.mkv` desde tu servidor Nginx:

### Método 1: Descargar desde el Sitio Web Oficial
1. **Visita el Sitio Web de VLC**:
   - Abre tu navegador (ej., Safari o Chrome).
   - Ve a [https://www.videolan.org/vlc/](https://www.videolan.org/vlc/).

2. **Descarga VLC**:
   - Haz clic en el botón **Download VLC**. Debería detectar automáticamente tu macOS y ofrecer la versión correcta (ej., VLC 3.0.20 actualmente).
   - Obtendrás un archivo `.dmg` (ej., `vlc-3.0.20.dmg`).

3. **Instala VLC**:
   - Abre el archivo `.dmg` descargado (generalmente en tu carpeta `Descargas`).
   - Arrastra el icono de VLC a la carpeta **Aplicaciones** como se indica en la ventana.
   - Cierra la ventana del `.dmg y expúlsalo (haz clic derecho en el icono del disco en tu escritorio o en el Finder y selecciona "Expulsar").

4. **Ejecuta VLC**:
   - Ve a tu carpeta **Aplicaciones** (ej., a través del Finder o Spotlight con `Cmd + Espacio`, luego escribe "Aplicaciones").
   - Haz doble clic en **VLC**.
   - Si macOS lo bloquea ("desarrollador no identificado"), haz clic derecho en VLC, selecciona **Abrir**, luego haz clic en **Abrir** en el cuadro de diálogo.

5. **Transmite tu Archivo**:
   - Abre VLC.
   - Presiona `Cmd + N` (o `Archivo > Abrir Red`).
   - Ingresa `http://192.168.1.27/movies/tuarchivo.mkv`.
   - Haz clic en **Abrir**.

### Método 2: Instalar via Homebrew (Terminal)
Si prefieres la línea de comandos y tienes Homebrew instalado:
1. **Instala Homebrew** (si aún no lo tienes):
   - Abre Terminal.
   - Ejecuta:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Sigue las instrucciones.

2. **Instala VLC**:
   - En Terminal:
     ```bash
     brew install vlc
     ```

3. **Ejecuta VLC**:
   - Inícialo desde Terminal con:
     ```bash
     open -a VLC
     ```
   - O encuéntralo en **Aplicaciones** como `VLC.app`.

4. **Transmite**:
   - Igual que arriba: `Cmd + N`, ingresa tu URL y reproduce.

### Verificar la Instalación
- Una vez instalado, VLC debería aparecer en tu carpeta **Aplicaciones**.
- Pruébalo primero con un archivo local (arrastra un `.mkv` a VLC) para asegurarte de que funciona, luego intenta transmitir `http://192.168.1.27/movies/tuarchivo.mkv`.

### Resolución de Problemas
- **La Descarga Falla**: Usa un enlace espejo del sitio de VLC si la descarga principal es lenta.
- **Aviso de Seguridad**: Si macOS lo bloquea, ve a `Configuración del Sistema > Seguridad y Privacidad > General` y haz clic en **Abrir de Todas Formas**.
- **No Reproduce**: Asegúrate de que la URL es correcta y tu servidor es accesible (`ping 192.168.1.27` desde Terminal).

¡Eso es todo! VLC debería estar ahora listo en tu Mac para transmitir tus archivos `.mkv`. ¡Avísame si necesitas ayuda con el siguiente paso!