---
audio: false
generated: true
lang: es
layout: post
title: Métodos de extracción de subtítulos de videos de YouTube
translated: true
type: note
---

Para obtener todos los subtítulos de un video de YouTube, sigue estos pasos, dependiendo de tus necesidades y si prefieres un método manual o automatizado. Ten en cuenta que los subtítulos deben estar disponibles para el video (ya sean generados automáticamente o cargados por el creador).

### Método Manual (Usando la función de transcripción integrada de YouTube)
1. **Abre el Video**: Ve a YouTube en un navegador web y navega hasta el video deseado.
2. **Verifica los Subtítulos**: Haz clic en el video para pausarlo. Busca un ícono "CC" (Closed Captions) cerca de la esquina inferior derecha del reproductor. Si es visible, los subtítulos están disponibles.
3. **Accede a la Transcripción**:
   - Desplázate hacia abajo a la descripción del video y haz clic en "Mostrar más".
   - Encuentra y haz clic en "Mostrar transcripción" (si está disponible). Esto abre un panel de transcripción a la derecha del video con marcas de tiempo y texto.
4. **Alternar Marcas de Tiempo**: Haz clic en los tres puntos verticales en la parte superior derecha del panel de transcripción y selecciona "Alternar marcas de tiempo" para mostrar u ocultar las marcas de tiempo, según tu preferencia.
5. **Copia la Transcripción**:
   - Desplázate hasta el final de la transcripción, haz clic y mantén presionado después de la última palabra, luego arrastra hasta la parte superior para resaltar todo el texto.
   - Presiona `Ctrl + C` (Windows) o `Command + C` (Mac) para copiar.
6. **Pega y Guarda**: Abre un editor de texto (por ejemplo, Bloc de notas, TextEdit o Word), pega el texto con `Ctrl + V` o `Command + V`, y guárdalo como un archivo `.txt` o en tu formato preferido.

**Nota**: Este método solo funciona en el sitio web de YouTube, no en la aplicación móvil.[](https://www.wikihow.com/Download-YouTube-Video-Subtitles)

### Para Creadores de Contenido (Descargando subtítulos de tu propio video)
Si eres el propietario del video, puedes descargar los subtítulos directamente desde YouTube Studio:
1. **Inicia sesión en YouTube Studio**: Ve a [studio.youtube.com](https://studio.youtube.com).
2. **Selecciona el Video**: Haz clic en "Contenido" en el menú de la izquierda, luego elige el video.
3. **Accede a los Subtítulos**: Haz clic en "Subtítulos" en el menú de la izquierda, luego selecciona el idioma.
4. **Descarga los Subtítulos**: Haz clic en el menú de tres puntos junto a la pista de subtítulos y selecciona "Descargar". Elige un formato como `.srt`, `.vtt` o `.sbv`.
5. **Edita o Usa**: Abre el archivo descargado en un editor de texto o un editor de subtítulos (por ejemplo, Aegisub) para su uso posterior.

**Nota**: Solo puedes descargar archivos de subtítulos para videos en los canales que gestionas.[](https://ito-engineering.screenstepslive.com/s/ito_fase/a/1639680-how-do-i-download-a-caption-file-from-youtube)

### Método Automatizado (Usando herramientas de terceros)
Si necesitas subtítulos en un formato específico (por ejemplo, `.srt`) o para videos de los que no eres propietario, usa una herramienta de terceros confiable:
1. **Elige una Herramienta**: Las opciones populares incluyen:
   - **DownSub**: Una herramienta en línea gratuita para descargar subtítulos.
   - **Notta**: Ofrece transcripción y descarga de subtítulos con alta precisión.[](https://www.notta.ai/en/blog/download-subtitles-from-youtube)
   - **4K Download**: Una aplicación de escritorio para extracción de subtítulos.[](https://verbit.ai/captioning/a-guide-to-downloading-subtitles-and-captions-from-youtube-enhancing-accessibility-and-user-experience/)
2. **Copia la URL del Video**: Abre el video de YouTube, haz clic en "Compartir" debajo del video y copia la URL.
3. **Usa la Herramienta**:
   - Pega la URL en el campo de entrada de la herramienta.
   - Selecciona el idioma y formato deseado (por ejemplo, `.srt`, `.txt`).
   - Haz clic en "Descargar" o "Extraer" y guarda el archivo.
4. **Verifica**: Abre el archivo para asegurarte de su precisión, ya que los subtítulos generados automáticamente pueden contener errores.

**Precaución**: Usa herramientas confiables para evitar riesgos de seguridad. Algunas herramientas pueden tener anuncios o requerir pago para funciones avanzadas.[](https://gotranscript.com/blog/how-to-download-subtitles-from-youtube)

### Usando la API de YouTube (Para desarrolladores)
Para extracción masiva de subtítulos o integración en aplicaciones, usa la YouTube Data API:
1. **Configura el Acceso a la API**: Crea un proyecto en la [Google Cloud Console](https://console.cloud.google.com), habilita la YouTube Data API v3 y obtén una clave API.
2. **Listar Pistas de Subtítulos**: Usa el endpoint `captions.list` para recuperar las pistas de subtítulos disponibles para un video. Ejemplo:
   ```
   GET https://www.googleapis.com/youtube/v3/captions?part=snippet&videoId=VIDEO_ID&key=API_KEY
   ```
3. **Descargar Subtítulos**: Usa el endpoint `captions.download` para obtener una pista de subtítulos específica. Ejemplo:
   ```
   GET https://www.googleapis.com/youtube/v3/captions/CAPTION_ID?tfmt=srt&key=API_KEY
   ```
4. **Limitaciones**:
   - Solo puedes descargar subtítulos de tus propios videos a menos que el propietario del video los haya hecho públicamente accesibles.
   - El uso de la API tiene límites de cuota (aproximadamente 200 unidades por descarga de subtítulos).[](https://developers.google.com/youtube/v3/docs/captions)[](https://stackoverflow.com/questions/73863672/how-can-i-get-captions-of-a-youtube-video-and-display-it-separately)
5. **Alternativa**: Algunos desarrolladores extraen la URL de texto con tiempo (por ejemplo, `https://www.youtube.com/api/timedtext?...`) del código fuente de la página del video, pero esto es poco confiable, puede violar los términos de servicio de YouTube y conlleva el riesgo de bloqueo de IP.[](https://stackoverflow.com/questions/73863672/how-can-i-get-captions-of-a-youtube-video-and-display-it-separately)

### Consejos Adicionales
- **Selección de Idioma**: Si los subtítulos están disponibles en varios idiomas, selecciona tu idioma preferido desde la configuración de "Subtítulos/CC" o el menú desplegable de la transcripción.[](https://riverside.fm/blog/youtube-transcription)
- **Subtítulos Generados Automáticamente**: Estos pueden tener errores debido a acentos, ruido de fondo o audio complejo. Revísalos y edítalos si la precisión es crítica.[](https://support.google.com/youtube/answer/6373554?hl=en)
- **Accesibilidad**: Los subtítulos mejoran la accesibilidad para espectadores sordos o con problemas de audición y mejoran el SEO al hacer que el contenido sea buscable.[](https://www.descript.com/blog/article/transcript-of-youtube-videos)
- **¿No hay subtítulos disponibles?**: Si al video le faltan subtítulos, considera usar servicios de transcripción como Rev o Notta para generar una transcripción del audio.[](https://www.rev.com/resources/how-to-download-youtube-subtitles-as-text-files)[](https://www.notta.ai/en/blog/download-subtitles-from-youtube)

### Limitaciones
- No todos los videos tienen subtítulos, especialmente si el creador los deshabilitó o si la subtitulación automática de YouTube no es compatible con el idioma o la calidad del audio.[](https://support.google.com/youtube/answer/6373554?hl=en)
- La aplicación móvil de YouTube no admite la visualización de transcripciones, pero puedes habilitar los subtítulos mediante el botón "CC".[](https://riverside.fm/blog/youtube-transcription)
- Algunas herramientas de terceros o métodos de API pueden no funcionar para subtítulos generados automáticamente o videos restringidos.[](https://stackoverflow.com/questions/9611397/how-to-extract-closed-caption-transcript-from-youtube-video)

Si necesitas subtítulos para un video específico o en un formato particular, ¡avísame y puedo guiarte más!