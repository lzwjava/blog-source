---
audio: false
generated: true
image: false
lang: es
layout: post
title: Corrección de AAC M4A para la API de Google Speech
translated: true
type: note
---

Sí—tu archivo es **AAC en un contenedor M4A** (Grabaciones de Voz del iPhone). Google Speech-to-Text v2 Batch a menudo falla al decodificar automáticamente AAC/M4A y devuelve ese error exacto. Convierte primero a un códec/contenedor compatible—luego mantén `AutoDetectDecodingConfig()` o (mejor) especifica la decodificación explícitamente.

Aquí está la solución más rápida.

## Opción A — Solución de una línea con `ffmpeg` (recomendada: Ogg/Opus)

Archivos pequeños, gran precisión, oficialmente compatible.

```bash
# 48 kHz, mono, Opus en OGG
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -c:a libopus -b:a 48k ~/Downloads/haifeng_and_zhiwei.ogg
```

Luego ejecuta tu script en el nuevo archivo:

```bash
python scripts/agent/speech_to_text_agent.py --input_file ~/Downloads/haifeng_and_zhiwei.ogg
```

## Opción B — FLAC sin pérdida (también compatible)

Más pequeño que WAV; sin pérdida.

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -sample_fmt s16 -c:a flac ~/Downloads/haifeng_and_zhiwei.flac
```

## Opción C — Linear16 WAV (archivo más grande)

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 16000 -sample_fmt s16 -c:a pcm_s16le ~/Downloads/haifeng_and_zhiwei.wav
```

---

## Ajustes de código (para que nunca más te encuentres con esto)

1. **Permite más extensiones** y selecciona el idioma por sufijo de la misma manera.
2. **Transcodifica automáticamente** a un formato compatible (yo uso Ogg/Opus).
3. **Indica a la API exactamente lo que estás enviando** (decodificación explícita).

Incorpora esto en tu script (cambios mínimos y enfocados):

```python
import subprocess
import tempfile
from pathlib import Path
from google.cloud.speech_v2.types import cloud_speech

SUPPORTED_EXTS = {".ogg", ".flac", ".wav", ".mp3"}  # mp3 también es compatible

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

    # Prefiere la decodificación explícita — evita sorpresas de "codificación no compatible"
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
        decoding_cfg = cloud_speech.AutoDetectDecodingConfig()  # alternativa

    config = cloud_speech.RecognitionConfig(
        explicit_decoding_config=decoding_cfg,
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
        language_codes=[language_code],
        # Opcional: diarización, puntuación, etc.
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
    print("Esperando a que la operación se complete...")
    response = client.batch_recognize(request=request).result(timeout=3 * MAX_AUDIO_LENGTH_SECS)
    print(response)

def process_audio_file(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    src = Path(input_file)
    if not src.exists():
        print(f"Error: {src} no existe.")
        return

    # Decide el idioma por sufijo
    language_code = "cmn-CN" if src.name.endswith("-zh" + src.suffix) else "en-US"

    # Asegura una codificación/contenedor compatible
    if src.suffix.lower() not in SUPPORTED_EXTS:
        print(f"Transcodificando {src.name} a Ogg/Opus...")
        input_file = _transcode_to_ogg_opus(str(src))
        src = Path(input_file)

    # Salida de control para tu .txt local (puedes mantenerlo tal cual o basarlo en el stem)
    output_filename = os.path.join(output_dir, f"{src.stem}.txt")
    if os.path.exists(output_filename):
        print(f"Omitiendo {src.name}: {output_filename} ya existe.")
        return

    print(f"Procesando: {src.name}")

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket("test2x")
        # Mantén la carpeta "audio-files/", mantén el nombre de archivo real con la nueva extensión
        blob = bucket.blob(f"audio-files/{src.name}")
        if not blob.exists():
            blob.upload_from_filename(str(src))
            print(f"Subido {src.name} a GCS.")
        else:
            print(f"{src.name} ya existe en GCS.")

        gcs_audio_uri = f"gs://test2x/audio-files/{src.name}"
        gcs_output_uri = f"gs://test2x/transcripts/{src.stem}"

        # Elige la decodificación basada en la extensión
        ext = src.suffix.lower()
        if ext == ".ogg":
            decoding = "ogg_opus"
        elif ext == ".flac":
            decoding = "flac"
        elif ext == ".wav":
            decoding = "linear16"
        else:
            decoding = None  # recurrir a la autodetección

        run_batch_recognize(
            audio_gcs_uri=gcs_audio_uri,
            output_gcs_folder=gcs_output_uri,
            language_code=language_code,
            decoding=decoding,
        )

        print(f"Archivo {src.name} procesado.\n")

        # Descarga los JSONs de la transcripción
        blobs = storage_client.list_blobs("test2x", prefix=f"transcripts/{src.stem}")
        for b in blobs:
            if b.name.endswith(".json"):
                local_output_path = os.path.join(output_dir, os.path.basename(b.name))
                b.download_to_filename(local_output_path)
                print(f"Descargado {b.name} a {local_output_path}")

    except Exception as e:
        print(f"Error al procesar {src.name}: {e}")

    print(f"Procesamiento completado para {src.name}.")
```

### Por qué esto funciona

* Grabaciones de Voz de iOS → **AAC/M4A**. Batch STT v2 no detecta/decodifica eso de forma fiable.
* Al transcodificar a **OGG/Opus** (o **FLAC/WAV**) e **indicarle a la API el códec**, evitas por completo el error de "codificación no compatible".

### Consejos prácticos

* Para grabaciones largas como tu **grabación de voz mono de 1h21m**, **OGG/Opus 48k** mantiene la calidad mientras reduce el tamaño y el egress de GCS.
* Mantén mono (`-ac 1`). El estéreo solo duplica el costo sin ayudar al reconocimiento.
* Si la conversación es en mandarín, tu código `"cmn-CN"` está bien; usa la convención de nomenclatura `"-zh.m4a"` como ya haces.
* Si necesitas turnos de hablante, habilita la diarización más tarde; arregla primero la ruta de decodificación.

Si quieres, también puedo añadir una **subida automática opcional local → GCS + renombrado** para que tu entrada `m4a` sea aceptada pero siempre procesada como un `.ogg` interno detrás de escena.