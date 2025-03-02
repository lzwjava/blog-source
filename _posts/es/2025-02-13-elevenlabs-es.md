---
audio: false
generated: true
lang: es
layout: post
title: Once you've provided the input text, I can translate it to Spanish.
translated: true
---

* Genial. Usé $5 USD para probar el servicio.

* La clonación de voz es excelente.

* Muestras de audio a continuación:

* [Inglés](assets/audios/ElevenLabs.mp3)

* [Japonés](assets/audios/ElevenLabs_1.mp3)

* [Español](assets/audios/ElevenLabs_2.mp3)

```python
import os
import requests
from dotenv import load_dotenv
import argparse
import re

load_dotenv()

api_key = os.environ.get("ELEVENLABS_API_KEY")
if not api_key:
    raise ValueError("La variable de entorno ELEVENLABS_API_KEY no está configurada.")

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, help="Archivo Markdown para convertir a voz", required=False)
parser.add_argument("--text", type=str, help="Texto para convertir a voz", required=False)
parser.add_argument("--output", type=str, help="Nombre del archivo de salida", required=True)
parser.add_argument("--voice_id", type=str, default="21m00Tcm4TlvDq8iK2G8", help="ID de voz a usar")

args = parser.parse_args()

if args.file:
    try:
        with open(args.file, 'r') as f:
            content = f.read()
            # Eliminar front matter
            content = re.sub(r'---.*?---', '', content, flags=re.DOTALL)
            text = content.strip()
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado: {args.file}")
        exit(1)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        exit(1)
elif args.text:
    text = args.text
else:
    print("Error: Debe especificar --file o --text.")
    exit(1)

url = f"https://api.elevenlabs.io/v1/text-to-speech/{args.voice_id}"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": api_key
}

data = {
  "text": text,
  "model_id": "eleven_flash_v2_5",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    with open(args.output, 'wb') as f:
        f.write(response.content)
    print(f"Audio guardado en {args.output}")
else:
    print(f"Error: {response.status_code} - {response.text}")
```