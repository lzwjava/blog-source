---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Correction des fichiers AAC M4A pour l'API Google Speech
translated: true
type: note
---

Oui — votre fichier est en **AAC dans un conteneur M4A** (Mémos vocaux iPhone). Google Speech-to-Text v2 Batch échoue souvent à décoder automatiquement les fichiers AAC/M4A et renvoie cette erreur exacte. Convertissez-le d'abord vers un codec/conteneur pris en charge — puis conservez `AutoDetectDecodingConfig()` ou (mieux) spécifiez le décodage explicitement.

Voici la solution la plus rapide.

## Option A — Correction en une ligne avec `ffmpeg` (recommandée : Ogg/Opus)

Petits fichiers, grande précision, officiellement pris en charge.

```bash
# 48 kHz, mono, Opus dans OGG
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -c:a libopus -b:a 48k ~/Downloads/haifeng_and_zhiwei.ogg
```

Puis exécutez votre script sur le nouveau fichier :

```bash
python scripts/agent/speech_to_text_agent.py --input_file ~/Downloads/haifeng_and_zhiwei.ogg
```

## Option B — FLAC sans perte (également pris en charge)

Plus petit que WAV ; sans perte.

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -sample_fmt s16 -c:a flac ~/Downloads/haifeng_and_zhiwei.flac
```

## Option C — Linear16 WAV (fichier le plus volumineux)

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 16000 -sample_fmt s16 -c:a pcm_s16le ~/Downloads/haifeng_and_zhiwei.wav
```

---

## Ajustements du code (pour ne plus jamais rencontrer ce problème)

1.  **Autorisez plus d'extensions** et détectez la langue par le suffixe de la même manière.
2.  **Transcodez automatiquement** vers un format pris en charge (j'utilise Ogg/Opus).
3.  **Indiquez exactement à l'API ce que vous envoyez** (décodage explicite).

Intégrez ceci dans votre script (modifications minimales et ciblées) :

```python
import subprocess
import tempfile
from pathlib import Path
from google.cloud.speech_v2.types import cloud_speech

SUPPORTED_EXTS = {".ogg", ".flac", ".wav", ".mp3"}  # mp3 est également pris en charge

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

    # Préfère un décodage explicite — évite les mauvaises surprises de "unsupported encoding"
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
        decoding_cfg = cloud_speech.AutoDetectDecodingConfig()  # solution de repli

    config = cloud_speech.RecognitionConfig(
        explicit_decoding_config=decoding_cfg,
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
        language_codes=[language_code],
        # Optionnel : diarisation, ponctuation, etc.
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

    # Détermine la langue par le suffixe
    language_code = "cmn-CN" if src.name.endswith("-zh" + src.suffix) else "en-US"

    # Garantit un encodage/conteneur pris en charge
    if src.suffix.lower() not in SUPPORTED_EXTS:
        print(f"Transcoding {src.name} to Ogg/Opus...")
        input_file = _transcode_to_ogg_opus(str(src))
        src = Path(input_file)

    # Gestion de la sortie pour votre fichier .txt local (vous pouvez le garder tel quel ou le baser sur le stem)
    output_filename = os.path.join(output_dir, f"{src.stem}.txt")
    if os.path.exists(output_filename):
        print(f"Skipping {src.name}: {output_filename} already exists.")
        return

    print(f"Processing: {src.name}")

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket("test2x")
        # Conserve le dossier "audio-files/", conserve le vrai nom de fichier avec la nouvelle extension
        blob = bucket.blob(f"audio-files/{src.name}")
        if not blob.exists():
            blob.upload_from_filename(str(src))
            print(f"Uploaded {src.name} to GCS.")
        else:
            print(f"{src.name} already exists in GCS.")

        gcs_audio_uri = f"gs://test2x/audio-files/{src.name}"
        gcs_output_uri = f"gs://test2x/transcripts/{src.stem}"

        # Choisit le décodage en fonction de l'extension
        ext = src.suffix.lower()
        if ext == ".ogg":
            decoding = "ogg_opus"
        elif ext == ".flac":
            decoding = "flac"
        elif ext == ".wav":
            decoding = "linear16"
        else:
            decoding = None  # revient à la détection automatique

        run_batch_recognize(
            audio_gcs_uri=gcs_audio_uri,
            output_gcs_folder=gcs_output_uri,
            language_code=language_code,
            decoding=decoding,
        )

        print(f"File {src.name} processed.\n")

        # Télécharge les JSON de transcription
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

### Pourquoi cela fonctionne

*   Mémos vocaux iOS → **AAC/M4A**. Batch STT v2 ne détecte/décode pas cela de manière fiable.
*   En transcodant vers **OGG/Opus** (ou **FLAC/WAV**) et en **indiquant le codec à l'API**, vous évitez complètement l'erreur “unsupported encoding”.

### Conseils pratiques

*   Pour les enregistrements longs comme votre **memo vocal mono de 1h21m**, **OGG/Opus 48k** maintient la qualité tout en réduisant la taille et l'egress GCS.
*   Gardez le mono (`-ac 1`). La stéréo double simplement le coût sans aider à la reconnaissance.
*   Si la conversation est en mandarin, votre code `"cmn-CN"` est correct ; utilisez la convention de nommage `"-zh.m4a"` comme vous le faites déjà.
*   Si vous avez besoin de tours de parole, activez la diarisation plus tard ; corrigez d'abord le problème de décodage.

Si vous voulez, je peux aussi ajouter un **téléchargement automatique optionnel local → GCS + renommage** pour que votre entrée `m4a` soit acceptée mais toujours traitée comme un `.ogg` interne en arrière-plan.