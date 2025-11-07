---
audio: false
generated: false
image: false
lang: de
layout: post
title: Konversations-Audio-Generierung
translated: true
type: post
---

Inspiriert von einem YouTube-Video, das eine Diskussion über DeepSeek-V3 zeigte, habe ich mit KI-generierten Gesprächen experimentiert. Mein Ziel ist es, realistische Audio-Dialoge mit Google Text-to-Speech und ffmpeg für die Audio-Generierung und -Verkettung zu erstellen. Der folgende Code skizziert meinen aktuellen Ansatz, um ein natürliches Hin-und-Her-Gespräch zu simulieren.

## Prompt

> Erstelle ein natürliches und ausführliches Gespräch zwischen zwei Experten, A und B, mit mindestens 100 Wechseln. Die Experten sollten ein spezifisches Thema ausführlich diskutieren, wobei das Gespräch hin und her fließen sollte. Beide Teilnehmer sollten Fragen stellen, Einblicke teilen und die Nuancen des Themas erkunden. Das Format sollte wie folgt aussehen:

```json
[
    {
      "speaker": "A",
      "line": "Hey, ich habe in letzter Zeit viel über Machine Learning (ML), Deep Learning (DL) und GPT gehört. Kannst du mir das erklären?"
    },
    {
      "speaker": "B",
      "line": "Klar! Fangen wir mit den Grundlagen an. Machine Learning ist ein Bereich der Informatik, in dem Systeme aus Daten lernen, um ihre Leistung zu verbessern, ohne explizit programmiert zu werden. Stell es dir so vor, als würdest du einem Computer beibringen, Muster zu erkennen."
    }
]
```

## Code

```python
import os
import json
import random
import subprocess
from google.cloud import texttospeech
import tempfile
import time
import argparse

# Fester Ausgabepfad für Gespräche
OUTPUT_DIRECTORY = "assets/conversations"
INPUT_DIRECTORY = "scripts/conversation"

def text_to_speech(text, output_filename, voice_name=None):
    print(f"Generiere Audio für: {output_filename}")
    try:
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)
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
                print(f"Audioinhalt wurde in {output_filename} geschrieben")
                return True
            except Exception as e:
                print(f"Fehler bei Versuch {attempt}: {e}")
                if attempt == retries:
                    print(f"Audio-Generierung nach {retries} Versuchen fehlgeschlagen.")
                    return False
                wait_time = 2 ** attempt
                print(f"Warte {wait_time} Sekunden, bevor erneut versucht wird...")
                time.sleep(wait_time)
    except Exception as e:
        print(f"Ein Fehler ist bei der Audio-Generierung für {output_filename} aufgetreten: {e}")
        return False

def process_conversation(filename):
    filepath = os.path.join(INPUT_DIRECTORY, filename)
    output_filename = os.path.join(OUTPUT_DIRECTORY, os.path.splitext(filename)[0] + ".mp3")

    if os.path.exists(output_filename):
        print(f"Audio-Datei existiert bereits: {output_filename}")
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            conversation = json.load(f)
    except Exception as e:
        print(f"Fehler beim Laden der Gesprächsdatei {filename}: {e}")
        return

    temp_files = []
    
    voice_options = ["en-US-Journey-D", "en-US-Journey-F", "en-US-Journey-O"]
    voice_name_A = random.choice(voice_options)
    voice_name_B = random.choice(voice_options)
    while voice_name_A == voice_name_B:
        voice_name_B = random.choice(voice_options)

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
            print(f"Audio-Generierung für Zeile {idx+1} von {filename} fehlgeschlagen")
            # Bereinige temporäre Dateien
            for temp_file_to_remove in temp_files:
                if os.path.exists(temp_file_to_remove):
                    os.remove(temp_file_to_remove)
            return

    if not temp_files:
        print(f"Kein Audio für {filename} generiert")
        return

    # Verkettung mit ffmpeg
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
        print(f"Audio erfolgreich zu {output_filename} verkettet")
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Audio-Verkettung: {e.stderr.decode()}")
    finally:
        os.remove(concat_file)
        for temp_file in temp_files:
            os.remove(temp_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verarbeite Konversations-JSON-Dateien, um Audio zu generieren.")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    for filename in os.listdir(INPUT_DIRECTORY):
        if filename.endswith(".json"):
            process_conversation(filename)
```

## Cover

```bash
ffmpeg -i deepseek.jpg -vf "crop=854:480" deepseek_480p_cropped.jpg
```

## Video

```bash
ffmpeg -loop 1 -i deepseek.jpg -i deepseek.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -shortest output_video.mp4
```