---
audio: false
generated: true
lang: es
layout: post
title: Crear Videos Educativos con Python
translated: true
type: note
---

Para crear videos educativos cortos con fondo negro y subtítulos sincronizados con audio generado a partir de texto usando la API de DeepSeek y la API de Google Cloud Text-to-Speech, puedes usar Python para orquestar el proceso. A continuación, se muestra una guía paso a paso y un script de Python que logra esto. El script hará lo siguiente:
1. Usar la API de DeepSeek para generar o refinar un guion (asumiendo que proporcionas el contenido educativo).
2. Usar la API de Google Cloud Text-to-Speech para convertir el guion en audio.
3. Usar una biblioteca como `moviepy` para crear un video con un fondo negro y subtítulos sincronizados con el audio.

### Prerrequisitos
- **Clave de API de DeepSeek**: Regístrate en [DeepSeek](https://api-docs.deepseek.com/) y obtén una clave de API.
- **API de Google Cloud Text-to-Speech**:
  - Configura un proyecto de Google Cloud y habilita la API de Text-to-Speech.
  - Crea una cuenta de servicio y descarga el archivo JSON de credenciales.
  - Instala la biblioteca cliente de Google Cloud Text-to-Speech: `pip install google-cloud-texttospeech`.
- **Bibliotecas de Python**:
  - Instala las bibliotecas requeridas: `pip install openai moviepy requests`.
- **FFmpeg**: Asegúrate de que FFmpeg esté instalado para que `moviepy` pueda manejar la renderización de video (descárgalo desde el [sitio web de FFmpeg](https://ffmpeg.org/) o instálalo mediante el administrador de paquetes).

### Pasos
1. **Generar o Refinar el Guion con la API de DeepSeek**: Usa DeepSeek para crear o pulir el guion educativo, asegurándote de que sea conciso y adecuado para un video de 1 minuto.
2. **Convertir Texto a Audio con Google Cloud Text-to-Speech**: Divide el guion en párrafos, genera audio para cada uno y guárdalos como archivos de audio separados.
3. **Crear Video con MoviePy**: Genera un video con un fondo negro, muestra los subtítulos para cada párrafo sincronizados con el audio y combínalos en un video final de 1 minuto.

### Script de Python
El siguiente script asume que tienes un archivo de texto con el contenido educativo (párrafos) y genera un video con un fondo negro y subtítulos.

```python
import os
from openai import OpenAI
from google.cloud import texttospeech
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips
import requests

# Configurar variables de entorno
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ruta/a/tu/archivo-de-credenciales-google.json"  # Actualiza con la ruta de tu archivo de credenciales
DEEPSEEK_API_KEY = "tu_clave_api_deepseek"  # Actualiza con tu clave de API de DeepSeek

# Inicializar el cliente de DeepSeek
deepseek_client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

# Función para refinar el guion con DeepSeek
def refine_script_with_deepseek(script):
    prompt = f"""
    Eres un escritor de guiones experto para videos educativos. Refina el siguiente guion para que sea conciso, claro y atractivo para un video educativo de 1 minuto. Asegúrate de que sea adecuado para narración hablada y que encaje en 60 segundos cuando se habla a un ritmo natural. Divide el guion en 2-3 párrafos cortos para mostrar como subtítulos. Devuelve el guion refinado como una lista de párrafos.

    Guion original:
    {script}

    Formato de salida:
    ["párrafo 1", "párrafo 2", "párrafo 3"]
    """
    response = deepseek_client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )
    refined_script = eval(response.choices[0].message.content)  # Convertir cadena a lista
    return refined_script

# Función para generar audio para cada párrafo usando Google Cloud Text-to-Speech
def generate_audio(paragraphs, output_dir="audio"):
    client = texttospeech.TextToSpeechClient()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    audio_files = []
    for i, paragraph in enumerate(paragraphs):
        synthesis_input = texttospeech.SynthesisInput(text=paragraph)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Wavenet-D"  # Una voz en inglés de sonido natural
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        audio_file = os.path.join(output_dir, f"paragraph_{i+1}.mp3")
        with open(audio_file, "wb") as out:
            out.write(response.audio_content)
        audio_files.append(audio_file)
    return audio_files

# Función para crear video con subtítulos y fondo negro
def create_video(paragraphs, audio_files, output_file="educational_video.mp4"):
    clips = []
    for i, (paragraph, audio_file) in enumerate(zip(paragraphs, audio_files)):
        # Crear clip de texto para los subtítulos
        text_clip = TextClip(
            paragraph,
            fontsize=40,
            color="white",
            font="Arial",
            size=(1280, 720),  # Resolución HD estándar
            method="caption",
            align="center"
        )
        # Cargar audio y obtener su duración
        audio_clip = AudioFileClip(audio_file)
        duration = audio_clip.duration
        # Establecer la duración del clip de texto para que coincida con el audio
        text_clip = text_clip.set_duration(duration)
        # Crear clip de fondo negro
        bg_clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=duration)
        # Combinar texto y fondo
        video_clip = CompositeVideoClip([bg_clip, text_clip.set_position("center")])
        # Añadir audio al clip de video
        video_clip = video_clip.set_audio(audio_clip)
        clips.append(video_clip)
    
    # Concatenar todos los clips
    final_clip = concatenate_videoclips(clips)
    # Escribir el video final
    final_clip.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")
    final_clip.close()
    for clip in clips:
        clip.close()

# Función principal
def main():
    # Guion de entrada de ejemplo (reemplaza con tu contenido educativo)
    input_script = """
    Machine learning is a field of artificial intelligence that allows computers to learn from data without being explicitly programmed. It involves algorithms that identify patterns and make predictions. Applications include image recognition, natural language processing, and more. This technology is transforming industries like healthcare and finance.
    """
    
    # Paso 1: Refinar el guion con DeepSeek
    refined_paragraphs = refine_script_with_deepseek(input_script)
    print("Guion Refinado:", refined_paragraphs)
    
    # Paso 2: Generar audio para cada párrafo
    audio_files = generate_audio(refined_paragraphs)
    print("Archivos de audio generados:", audio_files)
    
    # Paso 3: Crear video con subtítulos y fondo negro
    create_video(refined_paragraphs, audio_files)
    print("Video creado: educational_video.mp4")

if __name__ == "__main__":
    main()

```

### Cómo Usar
1. **Configurar Credenciales**:
   - Reemplaza `"ruta/a/tu/archivo-de-credenciales-google.json"` con la ruta a tu archivo JSON de cuenta de servicio de Google Cloud.
   - Reemplaza `"tu_clave_api_deepseek"` con tu clave de API de DeepSeek.
2. **Preparar el Guion de Entrada**:
   - Modifica la variable `input_script` en la función `main()` con tu contenido educativo. El guion debe ser una sola cadena con el texto completo que quieres convertir en video.
3. **Ejecutar el Script**:
   - Guarda el script como `create_educational_video.py` y ejecútalo con `python create_educational_video.py`.
   - El script hará lo siguiente:
     - Refinará el guion usando la API de DeepSeek para asegurarse de que sea conciso y esté dividido en 2-3 párrafos.
     - Generará archivos de audio MP3 para cada párrafo usando Google Cloud Text-to-Speech.
     - Creará un video con un fondo negro, mostrando cada párrafo como subtítulos sincronizados con su audio correspondiente.
4. **Salida**:
   - El video final se guardará como `educational_video.mp4` en el mismo directorio que el script.
   - Los archivos de audio para cada párrafo se guardarán en el directorio `audio`.

### Notas
- **API de DeepSeek**: El script usa el modelo `deepseek-chat` para refinar el guion. Asegúrate de que tu clave de API sea válida y de que tengas créditos suficientes. La API de DeepSeek se usa aquí para estructurar el guion para la narración de video, ya que sobresale en la generación y optimización de texto.
- **Google Cloud Text-to-Speech**: El script usa la voz `en-US-Wavenet-D` para una narración en inglés de sonido natural. Puedes cambiar la voz modificando el parámetro `name` en `VoiceSelectionParams` (consulta la documentación de Google Cloud Text-to-Speech para otras opciones de voz).
- **MoviePy**: El video se crea en resolución 1280x720 (HD). Puedes ajustar el parámetro `size` en `TextClip` y `ColorClip` para diferentes resoluciones.
- **Sincronización**: El script asegura que los subtítulos estén sincronizados con el audio estableciendo la duración del clip de texto para que coincida con la duración del audio. Para un video de 1 minuto, el prompt de DeepSeek impone un guion conciso.
- **Dependencias**: Asegúrate de que FFmpeg esté instalado y sea accesible en la PATH de tu sistema para que `moviepy` funcione correctamente.

### Ejemplo de Salida
Si tu guion de entrada trata sobre machine learning, el guion refinado podría verse así:
```
["Machine learning, a branch of AI, enables computers to learn from data.", 
 "It uses algorithms to find patterns and predict outcomes.", 
 "Applications include image recognition and healthcare innovations."]
```
- Cada párrafo genera un archivo de audio (por ejemplo, `paragraph_1.mp3`, `paragraph_2.mp3`, etc.).
- El video final muestra un fondo negro con subtítulos en blanco que aparecen secuencialmente, sincronizados con la narración de audio.

Este enfoque es simple, rentable y produce videos educativos de aspecto profesional adecuados para plataformas como YouTube o sitios web educativos. Si necesitas más personalización (por ejemplo, fuentes diferentes, estilos de subtítulos o efectos adicionales), ¡avísame!