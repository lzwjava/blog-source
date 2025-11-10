---
audio: false
generated: true
image: false
lang: de
layout: post
title: Behebung von AAC M4A für die Google Speech API
translated: true
type: note
---

Ja—deine Datei ist **AAC in einem M4A-Container** (iPhone-Sprachmemos). Google Speech-to-Text v2 Batch scheitert oft daran, AAC/M4A automatisch zu dekodieren und gibt genau diesen Fehler zurück. Konvertiere sie zuerst in einen unterstützten Codec/Container—behalte dann entweder `AutoDetectDecodingConfig()` bei oder (besser) gib das Decoding explizit an.

Hier ist der schnellste Weg.

## Option A — Einzeiler mit `ffmpeg` (empfohlen: Ogg/Opus)

Kleine Dateien, hohe Genauigkeit, offiziell unterstützt.

```bash
# 48 kHz, mono, Opus in OGG
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -c:a libopus -b:a 48k ~/Downloads/haifeng_and_zhiwei.ogg
```

Führe dann dein Skript mit der neuen Datei aus:

```bash
python scripts/agent/speech_to_text_agent.py --input_file ~/Downloads/haifeng_and_zhiwei.ogg
```

## Option B — Verlustfreies FLAC (auch unterstützt)

Kleiner als WAV; verlustfrei.

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -sample_fmt s16 -c:a flac ~/Downloads/haifeng_and_zhiwei.flac
```

## Option C — Linear16 WAV (größte Datei)

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 16000 -sample_fmt s16 -c:a pcm_s16le ~/Downloads/haifeng_and_zhiwei.wav
```

---

## Code-Anpassungen (damit dir das nie wieder passiert)

1. **Erlaube mehr Dateiendungen** und wähle die Sprache anhand der Endung auf die gleiche Weise aus.
2. **Transkodiere automatisch** in ein unterstütztes Format (ich verwende Ogg/Opus).
3. **Sage der API genau, was du sendest** (explizites Decoding).

Füge dies in dein Skript ein (minimale, fokussierte Änderungen):

```python
import subprocess
import tempfile
from pathlib import Path
from google.cloud.speech_v2.types import cloud_speech

SUPPORTED_EXTS = {".ogg", ".flac", ".wav", ".mp3"}  # mp3 wird auch unterstützt

def _transcode_to_ogg_opus(src_path: str) -> str:
    src = Path(src_path)
    dst = src.with_suffix(".ogg")
    cmd = [
        "ffmpeg", "-y",
        "-i", str(src),
        "-vn",
        "-ac", "1",
        "-ar", "48000",
        "-c:a", "libopus",
        "-b:a", "48k",
        str(dst),
    ]
    subprocess.run(cmd, check=True)
    return str(dst)

def run_batch_recognize(audio_gcs_uri, output_gcs_folder, language_code="en-US", decoding="ogg_opus"):
    client = SpeechClient()

    # Bevorzuge explizites Decoding – vermeidet "unsupported encoding"-Überraschungen
    if decoding == "ogg_opus":
        decoding_cfg = cloud_speech.ExplicitDecodingConfig(
            ogg_opus=cloud_speech.OggOpusDecodingConfig()
        )
    elif decoding == "flac":
        decoding_cfg = cloud_speech.ExplicitDecodingConfig(
            flac=cloud_speech.FlacDecodingConfig()
        )
    elif decoding == "linear16":
        decoding_cfg = cloud_speech.ExplicitDecodingConfig(
            linear16=cloud_speech.Linear16DecodingConfig()
        )
    else:
        decoding_cfg = cloud_speech.AutoDetectDecodingConfig()  # Fallback

    config = cloud_speech.RecognitionConfig(
        explicit_decoding_config=decoding_cfg,
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
        language_codes=[language_code],
        # Optional: Diarisierung, Interpunktion, etc.
        # speech_adaptation=...
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
    print("Waiting for operation to complete...")
    response = client.batch_recognize(request=request).result(timeout=3 * MAX_AUDIO_LENGTH_SECS)
    print(response)

def process_audio_file(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    src = Path(input_file)
    if not src.exists():
        print(f"Error: {src} does not exist.")
        return

    # Sprache anhand der Endung bestimmen
    language_code = "cmn-CN" if src.name.endswith("-zh" + src.suffix) else "en-US"

    # Stelle einen unterstützten Encoding/Container sicher
    if src.suffix.lower() not in SUPPORTED_EXTS:
        print(f"Transcoding {src.name} to Ogg/Opus...")
        input_file = _transcode_to_ogg_opus(str(src))
        src = Path(input_file)

    # Output-Gating für deine lokale .txt (kannst du so belassen oder vom Stammnamen ableiten)
    output_filename = os.path.join(output_dir, f"{src.stem}.txt")
    if os.path.exists(output_filename):
        print(f"Skipping {src.name}: {output_filename} already exists.")
        return

    print(f"Processing: {src.name}")

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket("test2x")
        # Behalte Ordner "audio-files/", behalte echten Dateinamen mit neuer Endung
        blob = bucket.blob(f"audio-files/{src.name}")
        if not blob.exists():
            blob.upload_from_filename(str(src))
            print(f"Uploaded {src.name} to GCS.")
        else:
            print(f"{src.name} already exists in GCS.")

        gcs_audio_uri = f"gs://test2x/audio-files/{src.name}"
        gcs_output_uri = f"gs://test2x/transcripts/{src.stem}"

        # Wähle Decoding basierend auf der Dateiendung
        ext = src.suffix.lower()
        if ext == ".ogg":
            decoding = "ogg_opus"
        elif ext == ".flac":
            decoding = "flac"
        elif ext == ".wav":
            decoding = "linear16"
        else:
            decoding = None  # Fallback zu Autodetect

        run_batch_recognize(
            audio_gcs_uri=gcs_audio_uri,
            output_gcs_folder=gcs_output_uri,
            language_code=language_code,
            decoding=decoding,
        )

        print(f"File {src.name} processed.\n")

        # Lade die Transkriptions-JSONs herunter
        blobs = storage_client.list_blobs("test2x", prefix=f"transcripts/{src.stem}")
        for b in blobs:
            if b.name.endswith(".json"):
                local_output_path = os.path.join(output_dir, os.path.basename(b.name))
                b.download_to_filename(local_output_path)
                print(f"Downloaded {b.name} to {local_output_path}")

    except Exception as e:
        print(f"Failed to process {src.name}: {e}")

    print(f"Processing complete for {src.name}.")
```

### Warum das funktioniert

* iOS-Sprachmemos → **AAC/M4A**. Batch STT v2 erkennt/dekodiert das nicht zuverlässig.
* Durch Transkodieren zu **OGG/Opus** (oder **FLAC/WAV**) und **dem expliziten Angeben des Codecs gegenüber der API**, umgehst du den "unsupported encoding"-Fehler komplett.

### Praktische Tipps

* Für lange Aufnahmen wie deine **1h21m Mono-Sprachmemo** erhält **OGG/Opus 48k** die Qualität, während Größe und GCS-Datenausstoß verringert werden.
* Bleib bei Mono (`-ac 1`). Stereo verdoppelt nur die Kosten, ohne die Erkennung zu verbessern.
* Wenn die Unterhaltung auf Mandarin ist, ist dein `"cmn-CN"` Code in Ordnung; verwende die `"-zh.m4a"`-Namenskonvention, wie du es bereits tust.
* Wenn du Sprecherwechsel benötigst, aktiviere später die Diarisierung; repariere zuerst den Decodierungspfad.

Falls du möchtest, kann ich auch optionales **automatisches Hochladen von lokal → GCS + Umbenennen** hinzufügen, sodass deine `m4a`-Eingabe akzeptiert wird, aber intern immer als `.ogg` verarbeitet wird.