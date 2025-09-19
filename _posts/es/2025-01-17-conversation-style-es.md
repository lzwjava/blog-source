---
audio: false
generated: false
image: false
lang: es
layout: post
title: Generación de Audio para Conversaciones
translated: true
---

Inspirado por un video de YouTube que presentaba una discusión sobre DeepSeek-V3, he estado experimentando con conversaciones generadas por IA. Mi objetivo es crear diálogos de audio realistas utilizando Google Text-to-Speech y ffmpeg para la generación y concatenación de audio. El siguiente código describe mi enfoque actual para simular una conversación natural de ida y vuelta.

## Indicación

> Crea una conversación natural y extensa entre dos expertos, A y B, con al menos 100 turnos. Los expertos deben discutir un tema específico en profundidad, con la conversación fluyendo de un lado a otro. Ambos participantes deben hacer preguntas, compartir ideas y explorar los matices del tema. El formato debe ser el siguiente:

```json
[
    {
      "speaker": "A",
      "line": "Oye, he estado escuchando mucho sobre Machine Learning (ML), Deep Learning (DL) y GPT últimamente. ¿Puedes explicármelo?"
    },
    {
      "speaker": "B",
      "line": "¡Claro! Comencemos con lo básico. Machine Learning es un campo de la informática donde los sistemas aprenden de los datos para mejorar su rendimiento sin ser programados explícitamente. Piensa en ello como enseñar a una computadora a reconocer patrones."
    }
]
```

## Código

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
        voice = texttospeech.VoiceSelectionParams(language_code="en-US", name=voice_name)
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            effects_profile_id=["small-bluetooth-speaker-class-device"]
        )
        
        reintentos = 5
        for intento in range(1, reintentos + 1):
            try:
                response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
                with open(output_filename, 'wb') as out:
                    out.write(response.audio_content)
                print(f"Contenido de audio escrito en {output_filename}")
                return True
            except Exception as e:
                print(f"Error en el intento {intento}: {e}")
                if intento == reintentos:
                    print(f"Fallo al generar audio después de {reintentos} intentos.")
                    return False
                tiempo_espera = 2 ** intento
                print(f"Reintentando en {tiempo_espera} segundos...")
                time.sleep(tiempo_espera)
    except Exception as e:
        print(f"Ocurrió un error al generar audio para {output_filename}: {e}")
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

    archivos_temporales = []
    
    opciones_voz = ["en-US-Journey-D", "en-US-Journey-F", "en-US-Journey-O"]
    voz_A = random.choice(opciones_voz)
    voz_B = random.choice(opciones_voz)
    while voz_A == voz_B:
        voz_B = random.choice(opciones_voz)

    for idx, linea_datos in enumerate(conversacion):
        speaker = linea_datos.get("speaker")
        linea = linea_datos.get("line")
        if not linea:
            continue
        archivo_temporal = os.path.join(OUTPUT_DIRECTORY, f"temp_{idx}.mp3")
        archivos_temporales.append(archivo_temporal)
        
        voz_nombre = None
        if speaker == "A":
            voz_nombre = voz_A
        elif speaker == "B":
            voz_nombre = voz_B
        
        if not text_to_speech(linea, archivo_temporal, voice_name=voz_nombre):
            print(f"Fallo al generar audio para la línea {idx+1} de {filename}")
            # Limpiar archivos temporales
            for archivo_a_eliminar in archivos_temporales:
                if os.path.exists(archivo_a_eliminar):
                    os.remove(archivo_a_eliminar)
            return

    if not archivos_temporales:
        print(f"No se generó audio para {filename}")
        return

    # Concatenar usando ffmpeg
    archivo_concat = os.path.join(OUTPUT_DIRECTORY, "concat.txt")
    with open(archivo_concat, 'w') as f:
        for archivo_temporal in archivos_temporales:
            f.write(f"file '{os.path.abspath(archivo_temporal)}'\n")
    
    try:
        subprocess.run(
            ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', archivo_concat, '-c', 'copy', output_filename],
            check=True,
            capture_output=True
        )
        print(f"Audio concatenado exitosamente en {output_filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error al concatenar audio: {e.stderr.decode()}")
    finally:
        os.remove(archivo_concat)
        for archivo_temporal in archivos_temporales:
            os.remove(archivo_temporal)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesa archivos JSON de conversación para generar audio.")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    for filename in os.listdir(INPUT_DIRECTORY):
        if filename.endswith(".json"):
            process_conversation(filename)
```

## Portada

```bash
ffmpeg -i deepseek.jpg -vf "crop=854:480" deepseek_480p_cropped.jpg
```

## Video

```bash
ffmpeg -loop 1 -i deepseek.jpg -i deepseek.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -shortest output_video.mp4
```