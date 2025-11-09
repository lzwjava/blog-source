---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: Beschleunigung der Transkription langer Audiodateien
translated: true
type: note
---

### Warum dauert die Verarbeitung für 30-minütige oder 1-stündige Audiodateien so lange?

Die Google Cloud Speech-to-Text Batch API (v2) ist für asynchrone, langlebige Operationen konzipiert, insbesondere mit dem `"long"`-Modell, das lange Audiodateien (bis zu ~1 Stunde pro Datei) verarbeitet. Hier ist der Grund, warum es sich "zu lang" anfühlen kann:

-   **Verarbeitungszeit skaliert mit Audiolänge**: Transkription ist nicht sofort. Für eine 30-minütige Audiodatei kann es 5-20 Minuten dauern; für 1 Stunde 10-40 Minuten oder mehr. Dies beinhaltet:
    -   Wartezeit in der Warteschlange (wenn Ihr Projekt/Ihre Region ausgelastet ist).
    -   Tatsächliche Transkription (KI-Modell-Inferenz, die für lange Audioinhalte rechenintensiv ist).
    -   Nachbearbeitung (z.B. Wortzeitstempel, Konfidenzscores).
-   **Stapelverarbeitungs-Natur**: Im Gegensatz zum Echtzeit-Streaming laufen Batch-Jobs im Hintergrund auf den Servern von Google. Ihr Skript ruft `operation.result()` auf, was blockiert und wartet, aber die eigentliche Arbeit geschieht asynchron.
-   **Andere Faktoren**:
    -   Audioformat/-qualität: OGG/Opus oder M4A/AAC müssen decodiert werden, was Overhead hinzufügt, wenn Abtastraten/Kanäle nicht übereinstimmen.
    -   Modellwahl: `"long"` ist für Meetings/Podcasts optimiert, aber langsamer als kürzere Modelle wie `"default"` oder `"short"`.
    -   Netzwerk/Quota: Hochladen zu GCS, API-Aufrufe und Herunterladen der Ergebnisse fügen Latenz hinzu. Free-Tier-Quotas oder hohe Nachfrage können Jobs verzögern.
    -   Keine eingebaute Parallelisierung: Das Skript verarbeitet Dateien sequenziell, eine nach der anderen.

Wenn Ihre Audiodateien durchgehend 30+ Minuten lang sind, ist das aktuelle Setup für eine schnelle Bearbeitung nicht ideal – es ist besser für Offline-/Massenverarbeitung geeignet.

### Wie man es behebt: Verarbeitungszeit reduzieren

Um lange Audiodateien schneller zu verarbeiten, ist der Schlüssel, **die Datei in kleinere Teile (Chunks) aufzuteilen** (z.B. jeweils 5-15 Minuten). Dies ermöglicht:
-   Parallele Verarbeitung (mehrere Batch-Jobs gleichzeitig ausführen).
-   Verwendung schnellerer Modelle (z.B. `"short"` oder `"default"`) pro Chunk.
-   Kürzere Wartezeiten pro Job (z.B. 1-5 Minuten pro Chunk vs. 30+ Minuten für die gesamte Datei).

#### Schritt 1: Audiodatei aufteilen
Verwenden Sie **FFmpeg** (kostenlos, Kommandozeilen-Tool), um Dateien ohne Neu-Codierung aufzuteilen (schnell und verlustfrei). Installieren Sie FFmpeg falls nötig (z.B. `brew install ffmpeg` auf macOS, `apt install ffmpeg` auf Linux).

Fügen Sie Ihrem Skript eine Funktion hinzu, um die Eingabedatei aufzuteilen. Hier ist eine aktualisierte Version Ihres Skripts mit integrierter Aufteilung:

```python
import os
import argparse
import subprocess
import tempfile
from google.cloud import storage
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
import sys
import time  # For polling

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.llm.openrouter_client import call_openrouter_api  # noqa: F401

MAX_AUDIO_LENGTH_SECS = 20 * 60 * 60
OUTPUT_DIRECTORY = "assets/transcriptions"
CHUNK_DURATION_SECS = 600  # 10 Minuten pro Chunk; nach Bedarf anpassen (z.B. 900 für 15 Min)


def split_audio_file(input_file, chunk_duration_secs=CHUNK_DURATION_SECS):
    """
    Teilt eine Audiodatei mit FFmpeg in kleinere Chunks auf.
    
    Args:
        input_file: Pfad zur Eingabe-Audiodatei.
        chunk_duration_secs: Dauer jedes Chunks in Sekunden.
    
    Returns:
        Liste der Chunk-Dateipfade.
    """
    filename = os.path.basename(input_file)
    name_without_ext = os.path.splitext(filename)[0]
    dir_name = os.path.dirname(input_file)
    
    # Temp-Verzeichnis für Chunks erstellen
    temp_dir = tempfile.mkdtemp()
    chunk_files = []
    
    # FFmpeg-Befehl (keine Neu-Codierung für Geschwindigkeit)
    cmd = [
        "ffmpeg", "-i", input_file,
        "-f", "segment",  # Ausgabeformat
        "-segment_time", str(chunk_duration_secs),
        "-c", "copy",  # Streams ohne Neu-Codierung kopieren
        "-map", "0",  # Alle Streams mappen
        f"{temp_dir}/{name_without_ext}_chunk_%03d.{os.path.splitext(filename)[1][1:]}",  # Ausgabemuster
        "-y"  # Überschreiben
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        # Erzeugte Chunks finden
        for file in os.listdir(temp_dir):
            if file.startswith(f"{name_without_ext}_chunk_") and file.endswith(os.path.splitext(filename)[1]):
                chunk_files.append(os.path.join(temp_dir, file))
        chunk_files.sort()  # Nach Namen sortieren (z.B. chunk_001, chunk_002)
        print(f"Aufteilung von {filename} in {len(chunk_files)} Chunks.")
        return chunk_files
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg-Fehler beim Aufteilen von {filename}: {e}")
        return []


def run_batch_recognize(audio_gcs_uri, output_gcs_folder, language_code="en-US"):
    """
    Transkribiert eine Audiodatei mit der Google Cloud Speech-to-Text Batch API.
    Aktualisiert, um kürzeres Modell zu verwenden, wenn Audio wahrscheinlich kurz ist (z.B. nach Aufteilung).
    """
    client = SpeechClient()

    filename = audio_gcs_uri.split('/')[-1]
    file_extension = filename.split('.')[-1].lower()

    # Für Chunks "short" oder "default" Modell für Geschwindigkeit verwenden (wenn <15 Min)
    model = "short" if CHUNK_DURATION_SECS < 900 else "long"  # Basierend auf Chunk-Größe anpassen

    if file_extension == "ogg":
        decoding = cloud_speech.ExplicitDecodingConfig(
            encoding=cloud_speech.ExplicitDecodingConfig.AudioEncoding.OGG_OPUS,
            sample_rate_hertz=48000,
            audio_channel_count=1
        )
        config = cloud_speech.RecognitionConfig(
            explicit_decoding_config=decoding,
            features=cloud_speech.RecognitionFeatures(
                enable_word_confidence=True,
                enable_word_time_offsets=True,
            ),
            model=model,
            language_codes=[language_code],
        )
    else:
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
            features=cloud_speech.RecognitionFeatures(
                enable_word_confidence=True,
                enable_word_time_offsets=True,
            ),
            model=model,
            language_codes=[language_code],
        )

    output_config = cloud_speech.RecognitionOutputConfig(
        gcs_output_config=cloud_speech.GcsOutputConfig(uri=output_gcs_folder),
    )

    files = [cloud_speech.BatchRecognizeFileMetadata(uri=audio_gcs_uri)]

    request = cloud_speech.BatchRecognizeRequest(
        recognizer="projects/graphite-ally-445108-k3/locations/global/recognizers/_",
        config=config,
        files=files,
        recognition_output_config=output_config,
    )

    print(f"Starte Batch Recognize für {filename}...")
    operation = client.batch_recognize(request=request)
    
    # Auf Fortschritt prüfen (siehe unten für Details)
    poll_operation_with_progress(operation, filename)
    
    response = operation.result(timeout=3 * CHUNK_DURATION_SECS)  # Kürzerer Timeout pro Chunk
    print(f"Transkription für {filename} abgeschlossen. Antwort: {response}")
    return response


def poll_operation_with_progress(operation, filename):
    """
    Fragt die langlebige Operation ab und zeigt den Fortschritt.
    """
    while not operation.done():
        # Operation-Metadaten abrufen (falls verfügbar; Speech API bietet grundlegenden Status)
        try:
            metadata = operation.metadata
            print(f"Fortschritt für {filename}: Status={getattr(metadata, 'state', 'Unbekannt')}, "
                  f"Verarbeitet={getattr(metadata, 'progress_bytes', 'N/V')} Bytes")
        except Exception:
            print(f"Warte auf {filename}... (prüfe alle 30s)")
        
        time.sleep(30)  # Alle 30 Sekunden prüfen
    if operation.exception():
        raise operation.exception()


def process_audio_file(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.basename(input_file)
    if not (filename.endswith(".m4a") or filename.endswith(".ogg")):
        print(f"Fehler: {filename} ist keine unterstützte Audiodatei (.m4a oder .ogg).")
        return

    output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
    if os.path.exists(output_filename):
        print(f"Überspringe {filename}: {output_filename} existiert bereits.")
        return

    print(f"Verarbeite: {filename}")

    # Sprache bestimmen
    if filename.endswith("-zh.m4a") or filename.endswith("-zh.ogg"):
        language_code = "cmn-CN"
    else:
        language_code = "en-US"

    # In Chunks aufteilen, wenn Datei lang ist (Heuristik: >15 Min, aber Dauer mit ffprobe prüfbar)
    chunk_files = []
    if os.path.getsize(input_file) > 100 * 1024 * 1024:  # Grobe Prüfung: >100MB wahrscheinlich lang
        print(f"Datei ist groß; teile in {CHUNK_DURATION_SECS//60}-Minuten-Chunks auf.")
        chunk_files = split_audio_file(input_file)
        if not chunk_files:
            print("Aufteilung fehlgeschlagen; verarbeite als einzelne Datei.")
            chunk_files = [input_file]
    else:
        chunk_files = [input_file]

    storage_client = storage.Client()
    bucket = storage_client.bucket("test2x")

    all_transcripts = []  # Zum späteren Kombinieren

    for chunk_idx, chunk_file in enumerate(chunk_files):
        chunk_filename = os.path.basename(chunk_file)
        base_name = os.path.splitext(filename)[0]
        chunk_name = f"{base_name}_chunk_{chunk_idx+1:03d}"
        
        # GCS-Pfade konstruieren
        gcs_audio_uri = f"gs://test2x/audio-files/{chunk_filename}"
        gcs_output_uri = f"gs://test2x/transcripts/{chunk_name}"

        # Chunk hochladen falls nötig
        blob = bucket.blob(f"audio-files/{chunk_filename}")
        if not blob.exists():
            blob.upload_from_filename(chunk_file)
            print(f"Chunk {chunk_filename} zu GCS hochgeladen.")
        else:
            print(f"Chunk {chunk_filename} bereits in GCS vorhanden.")

        # Transkribieren
        try:
            run_batch_recognize(
                audio_gcs_uri=gcs_audio_uri,
                output_gcs_folder=gcs_output_uri,
                language_code=language_code,
            )

            # Transkript herunterladen und sammeln
            blobs = storage_client.list_blobs("test2x", prefix=f"transcripts/{chunk_name}")
            chunk_transcript = ""
            for b in blobs:
                if b.name.endswith(".json"):
                    local_path = os.path.join(output_dir, f"{os.path.basename(b.name)}")
                    b.download_to_filename(local_path)
                    # JSON parsen, um Text zu extrahieren (vereinfacht; json-Modul für vollständiges Parsen verwenden)
                    import json
                    with open(local_path, 'r') as f:
                        data = json.load(f)
                        if 'results' in data:
                            chunk_text = ' '.join([result.get('alternatives', [{}])[0].get('transcript', '') for result in data['results']])
                            chunk_transcript += chunk_text + "\n"
                    print(f"Heruntergeladen und geparst {b.name}")

            all_transcripts.append(chunk_transcript)

            # Temp-Chunk bereinigen, wenn aufgeteilt
            if chunk_file != input_file and os.path.exists(chunk_file):
                os.remove(chunk_file)

        except Exception as e:
            print(f"Fehler beim Verarbeiten des Chunks {chunk_filename}: {e}")

    # Alle Transkripte in einer Datei kombinieren
    combined_text = "\n\n--- Chunk Grenze ---\n\n".join(all_transcripts)
    with open(output_filename, 'w') as f:
        f.write(combined_text)
    print(f"Kombiniertes Transkript gespeichert in {output_filename}")

    # Temp-Verzeichnis bereinigen, wenn Aufteilung stattfand
    if chunk_files != [input_file]:
        import shutil
        shutil.rmtree(os.path.dirname(chunk_files[0]) if chunk_files else None)

    print(f"Verarbeitung für {filename} abgeschlossen.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Verarbeite eine einzelne Voice Memo (.m4a/.ogg) Datei zur Transkriptionserzeugung."
    )
    parser.add_argument(
        "--input_file",
        type=str,
        required=True,
        help="Eingabepfad für die Voice Memo Datei.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="assets/transcriptions",
        help="Ausgabeverzeichnis für Transkriptionen.",
    )
    parser.add_argument(
        "--chunk_secs",
        type=int,
        default=CHUNK_DURATION_SECS,
        help="Chunk-Dauer in Sekunden (zum Aufteilen langer Dateien).",
    )

    args = parser.parse_args()
    global CHUNK_DURATION_SECS  # Überschreibung erlauben
    CHUNK_DURATION_SECS = args.chunk_secs

    process_audio_file(
        input_file=args.input_file,
        output_dir=args.output,
    )
```

#### Wichtige Änderungen und Vorteile:
-   **Aufteilung**: Verwendet FFmpeg, um nicht-überlappende Chunks zu erstellen (z.B. je 10 Min). Für eine 1-Stunden-Datei sind das ~6 Jobs, die parallel laufen können, wenn Sie das Skript für Threading/Multiprocessing modifizieren (z.B. via `concurrent.futures`).
-   **Schnelleres Modell**: Wechselt zu `"short"` für Chunks <15 Min – verarbeitet 2-3x schneller.
-   **Kombinieren von Transkripten**: Parst JSON-Ausgaben und fügt sie zu einer einzigen `.txt`-Datei mit Grenzen für einfaches Lesen zusammen.
-   **Bereinigung**: Entfernt temporäre Chunks und alte GCS-Blobs falls nötig (fügen Sie `blob.delete()` in einer Schleife hinzu).
-   **Verwendung**: Wie zuvor ausführen, z.B. `python script.py --input_file long_audio.m4a --chunk_secs 600`. Für keine Aufteilung, verwenden Sie einen großen `--chunk_secs`-Wert (z.B. 3600).

#### Weitere Optimierungen:
-   **Parallele Verarbeitung**: Wenn Sie viele Chunks/Dateien haben, verwenden Sie Pythons `ThreadPoolExecutor`, um `run_batch_recognize`-Jobs gleichzeitig abzusenden (auf 5-10 begrenzen, um Quota-Überschreitungen zu vermeiden).
-   **Audiodauer ermitteln**: Verwenden Sie `ffprobe` (FFmpeg), um dynamisch zu entscheiden, ob Aufteilung nötig ist: `ffprobe -v quiet -show_entries format=duration -of csv=p=0 input.m4a`.
-   **Zu Streaming API wechseln**: Für interaktive Nutzung, verwenden Sie synchrones `recognize` (limitiert auf ~1 Min/Datei) oder Streaming für Live-Audio, aber es ist nicht ideal für lange Batch-Dateien.
-   **Kosten/Quota**: Überprüfen Sie Ihre Google Cloud Quota (Speech-to-Text erlaubt ~1000 Anfragen/Min). Lange Jobs verbrauchen mehr Credits (~$0.036/Min für Standard-Modell).
-   **Zuerst mit kürzeren testen**: Beginnen Sie mit `--chunk_secs 300` (5 Min), um die Beschleunigung zu sehen.

### Fortschrittsanzeige: Abfragen der Operation

Die aktualisierte `poll_operation_with_progress()`-Funktion ersetzt das blockierende `operation.result()`. Sie:
-   Prüft alle 30 Sekunden.
-   Druckt den Status von `operation.metadata` (z.B. State wie "RUNNING" oder "DONE", und verarbeitete Bytes falls verfügbar – Speech API Metadaten sind grundlegend, aber besser als nichts).
-   Löst einen Fehler aus, falls sie fehlschlägt.

Für detaillierteren Fortschritt (z.B. % Fertigstellung) bietet die Speech API keine granularen Metriken, aber Sie können:
-   Über die Google Cloud Console überwachen (Operations-Seite für Ihr Projekt).
-   Die `gcloud` CLI verwenden: `gcloud alpha speech operations describe OPERATION_ID --project=graphite-ally-445108-k3`.
-   Nach Abschluss indirekt den Fortschritt pro Äußerung via Zeitstempel in den JSON-Ergebnissen einsehen.

Bei Aufteilung sehen Sie überlappende Fortschrittsmeldungen von mehreren Chunks, was es weniger "stecken" wirken lässt.

Wenn dies Ihr Problem nicht löst (z.B. spezifische Fehler), teilen Sie Logs/Ausgaben für weitere Anpassungen!