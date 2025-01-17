---
audio: true
lang: de
layout: post
title: Google Cloud Speech-to-Text
translated: true
---

Ich habe kürzlich mit der Speech-to-Text API von Google Cloud experimentiert. Im Folgenden finden Sie eine Python-Funktion, die ich zur Transkription verwendet habe.

```python
import os
import json
import time
import argparse
from google.cloud import speech
from pydub import AudioSegment
import tempfile

# Fester Ausgabeverzeichnis
OUTPUT_DIRECTORY = "assets/transcriptions"


def speech_to_text(audio_file, output_filename):
    print(f"Generiere Transkription für: {output_filename}")
    try:
        client = speech.SpeechClient()

        # Lade die Audiodatei mit pydub, um Parameter zu bestimmen
        audio_segment = AudioSegment.from_file(audio_file)
        sample_rate = audio_segment.frame_rate
        channels = audio_segment.channels

        # Bestimme die Kodierung basierend auf der Dateiendung
        file_extension = os.path.splitext(audio_file)[1].lower()
        if file_extension == '.mp3':
            encoding = speech.RecognitionConfig.AudioEncoding.MP3
        elif file_extension in ['.wav', '.wave']:
            encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16
        elif file_extension == '.flac':
            encoding = speech.RecognitionConfig.AudioEncoding.FLAC
        else:
            print(f"Nicht unterstütztes Dateiformat: {file_extension}")
            return

        # Konfiguriere die Erkennung
        config = speech.RecognitionConfig(
            encoding=encoding,
            sample_rate_hertz=sample_rate,
            audio_channel_count=channels,
            language_code="en-US",  # Setze basierend auf deiner Logik
        )

        with open(audio_file, "rb") as f:
            audio_content = f.read()

        audio = speech.RecognitionAudio(content=audio_content)

        # Führe die langlaufende Spracherkennung durch
        try:
            operation = client.long_running_recognize(config=config, audio=audio)
            response = operation.result(timeout=300)  # Passe das Timeout nach Bedarf an
        except Exception as e:
            print(f"Fehler während der Transkription: {e}")
            return
        
        print(response.results)

        transcription = ""
        for result in response.results:
            transcription += result.alternatives[0].transcript + "\n"

        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(transcription)
        print(f"Transkription geschrieben in {output_filename}")

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten während der Generierung der Transkription für {output_filename}: {e}")


def process_audio_files(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    all_audio_files = [f for f in os.listdir(input_dir) if f.endswith(('.mp3', '.wav', '.m4a'))]
    total_files = len(all_audio_files)
    print(f"Gesamtzahl der zu verarbeitenden Audiodateien: {total_files}")

    if total_files == 0:
        print(f"Keine Audiodateien im Verzeichnis '{input_dir}' gefunden.")
        return

    files_processed = 0


    for filename in all_audio_files:
        audio_file_path = os.path.join(input_dir, filename)
        output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
        if os.path.exists(output_filename):
            print(f"Überspringe {filename}: {output_filename} existiert bereits.")
            continue
        print(f"\nVerarbeite {files_processed + 1}/{total_files}: {filename}")
        try:
            # Bestimme die Sprache basierend auf dem Dateinamen-Suffix
            if filename.endswith('-zh.mp3') or filename.endswith('-zh.wav') or filename.endswith('-zh.m4a'):
                language_code = "cmn-CN"
            else:
                language_code = "en-US"

            # Aktualisiere die Konfiguration in speech_to_text, falls nötig
            # Der Einfachheit halber setzen wir die language_code in der Konfiguration innerhalb von speech_to_text

            speech_to_text(
                audio_file=audio_file_path,
                output_filename=output_filename,
            )
            files_processed += 1
            print(f"Datei {files_processed}/{total_files} verarbeitet.\n")
        except Exception as e:
            print(f"Fehler bei der Verarbeitung von {filename}: {e}")
            continue

    print(f"Verarbeitung abgeschlossen! {files_processed}/{total_files} Dateien verarbeitet.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verarbeite Audiodateien, um Transkriptionen zu generieren.")
    parser.add_argument('--input_dir', type=str, default="assets/audios", help="Eingabeverzeichnis für Audiodateien.")


    args = parser.parse_args()


    process_audio_files(
        input_dir=args.input_dir,
        output_dir=OUTPUT_DIRECTORY,
    )
```