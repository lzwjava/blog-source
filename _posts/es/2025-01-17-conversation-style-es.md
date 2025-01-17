---
audio: true
lang: es
layout: post
title: Generación de Audio de Conversación
translated: true
---

He estado explorando las capacidades de las conversaciones generadas por IA, especialmente después de ver un video de YouTube que mostraba una discusión sobre DeepSeek-V3. Esto me hizo pensar en cómo crear conversaciones de audio similares. He desarrollado un proceso utilizando Google Text-to-Speech y ffmpeg para generar y concatenar clips de audio, simulando un diálogo natural de ida y vuelta. A continuación, se muestra el código en el que he estado trabajando.

Prompt:

```
Haz una conversación más natural y extendida entre dos expertos, A y B, discutiendo DeepSeek-V3 en detalle. La conversación fluye de un lado a otro, con ambos participantes haciendo preguntas, compartiendo ideas y profundizando en los aspectos técnicos del modelo. La conversación está estructurada para cubrir la arquitectura, el entrenamiento, el rendimiento y las direcciones futuras de DeepSeek-V3.


[
    {
      "speaker": "A",
      "line": "Hola, he estado escuchando mucho sobre Machine Learning (ML), Deep Learning (DL) y GPT últimamente. ¿Puedes explicármelo?"
    },
    {
      "speaker": "B",
      "line": "¡Claro! Comencemos con lo básico. Machine Learning es un campo de la informática en el que los sistemas aprenden de los datos para mejorar su rendimiento sin ser programados explícitamente. Piensa en ello como enseñar a una computadora a reconocer patrones."
    }
]
```

Código:

```python
import os
import json
import random
import subprocess
from google.cloud import texttospeech
import tempfile
import time
import argparse

# Directorio de salida fijo para las conversaciones
OUTPUT_DIRECTORY = "assets/conversations"
INPUT_DIRECTORY = "scripts/conversation"

def text_to_speech(text, output_filename, voice_name=None):
    print(f"Generando audio para: {output_filename}")
    try:
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)
        if not voice_name:
            voice_name = random.choice(["en-US-Journey-D", "en-US-Journey-F", "en-US-Journey-O"])
        voice = texttospeech.VoiceSelectionParams(language_code="en-US", name=voice_name)
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            effects_profile_id=["small-bluetooth-speaker-class-device"]
        )
        
        retries = 5
        for attempt in range(1, retries + 1):
            try:
                response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
                with open(output_filename, 'wb') as out:
                    out.write(response.audio_content)
                print(f"Contenido de audio escrito en {output_filename}")
                return True
            except Exception as e:
                print(f"Error en el intento {attempt}: {e}")
                if attempt == retries:
                    print(f"No se pudo generar el audio después de {retries} intentos.")
                    return False
                wait_time = 2 ** attempt
                print(f"Reintentando en {wait_time} segundos...")
                time.sleep(wait_time)
    except Exception as e:
        print(f"Ocurrió un error al generar el audio para {output_filename}: {e}")
        return False

def process_conversation(filename):
    filepath = os.path.join(INPUT_DIRECTORY, filename)
    output_filename = os.path.join(OUTPUT_DIRECTORY, os.path.splitext(filename)[0] + ".mp3")

    if os.path.exists(output_filename):
        print(f"El archivo de audio ya existe: {output_filename}")
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            conversation = json.load(f)
    except Exception as e:
        print(f"Error al cargar el archivo de conversación {filename}: {e}")
        return

    temp_files = []
    
    voice_name_A = random.choice(["en-US-Wavenet-D", "en-US-Wavenet-E", "en-US-Wavenet-F"])
    voice_name_B = random.choice(["en-US-Studio-O", "en-US-Studio-M", "en-US-Studio-Q"])

    for idx, line_data in enumerate(conversation):
        speaker = line_data.get("speaker")
        line = line_data.get("line")
        if not line:
            continue
        temp_file = os.path.join(OUTPUT_DIRECTORY, f"temp_{idx}.mp3")
        temp_files.append(temp_file)
        
        voice_name = None
        if speaker == "A":
            voice_name = voice_name_A
        elif speaker == "B":
            voice_name = voice_name_B
        
        if not text_to_speech(line, temp_file, voice_name=voice_name):
            print(f"No se pudo generar el audio para la línea {idx+1} de {filename}")
            # Limpiar archivos temporales
            for temp_file_to_remove in temp_files:
                if os.path.exists(temp_file_to_remove):
                    os.remove(temp_file_to_remove)
            return

    if not temp_files:
        print(f"No se generó audio para {filename}")
        return

    # Concatenar usando ffmpeg
    concat_file = os.path.join(OUTPUT_DIRECTORY, "concat.txt")
    with open(concat_file, 'w') as f:
        for temp_file in temp_files:
            f.write(f"file '{os.path.abspath(temp_file)}'\n")
    
    try:
        subprocess.run(
            ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', concat_file, '-c', 'copy', output_filename],
            check=True,
            capture_output=True
        )
        print(f"Audio concatenado exitosamente en {output_filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error al concatenar el audio: {e.stderr.decode()}")
    finally:
        os.remove(concat_file)
        for temp_file in temp_files:
            os.remove(temp_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesa archivos JSON de conversación para generar audio.")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    for filename in os.listdir(INPUT_DIRECTORY):
        if filename.endswith(".json"):
            process_conversation(filename)
```