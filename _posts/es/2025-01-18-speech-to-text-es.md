---
audio: false
generated: false
image: false
lang: es
layout: post
title: Transcripción en Google Cloud
translated: true
type: post
---

Recientemente experimenté con la API de Speech-to-Text de Google Cloud. A continuación, presento una función en Python que utilicé para realizar la transcripción.

```python
import os
import argparse
from google.cloud import storage

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

MAX_AUDIO_LENGTH_SECS = 8 * 60 * 60
OUTPUT_DIRECTORY = "assets/transcriptions"


def run_batch_recognize(audio_gcs_uri, output_gcs_folder, language_code="en-US"):
    """
    Transcribe un archivo de audio utilizando la API Batch de Speech-to-Text de Google Cloud.

    Args:
        audio_gcs_uri: URI de GCS del archivo de audio.
        output_gcs_folder: URI de GCS de la carpeta para almacenar la transcripción.
        language_code: Código de idioma para la transcripción (por ejemplo, "en-US", "cmn-CN").
    """
    client = SpeechClient()

    config = cloud_speech.RecognitionConfig(
        auto_decoding_config={},
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
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
    operation = client.batch_recognize(request=request)

    print("Esperando a que la operación se complete...")
    response = operation.result(timeout=3 * MAX_AUDIO_LENGTH_SECS)
    print(response)


def process_audio_files(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    all_audio_files = [f for f in os.listdir(input_dir) if f.endswith(('.mp3', '.wav', '.m4a'))]
    total_files = len(all_audio_files)
    print(f"Total de archivos de audio a procesar: {total_files}")

    if total_files == 0:
        print(f"No se encontraron archivos de audio en el directorio '{input_dir}'.")
        return

    files_processed = 0

    for filename in all_audio_files:
        audio_file_path = os.path.join(input_dir, filename)
        output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
        if os.path.exists(output_filename):
            print(f"Omitiendo {filename}: {output_filename} ya existe.")
            continue
        print(f"\nProcesando {files_processed + 1}/{total_files}: {filename}")
        try:
            # Determinar el idioma basado en el sufijo del nombre del archivo
            if filename.endswith('-zh.mp3') or filename.endswith('-zh.wav') or filename.endswith('-zh.m4a'):
                language_code = "cmn-CN"
            else:
                language_code = "en-US"

            # Construir URIs de GCS
            gcs_audio_uri = f"gs://test2x/audio-files/{filename}"  # Reemplaza con tu bucket y carpeta
            gcs_output_uri = f"gs://test2x/transcripts/{os.path.splitext(filename)[0]}" # Reemplaza con tu bucket y carpeta
            
            # Subir el archivo a GCS si no existe
            # Esta parte no está implementada, necesitarías agregar código para subir el archivo a GCS
            # Por ejemplo, utilizando la biblioteca google-cloud-storage

            storage_client = storage.Client()
            bucket = storage_client.bucket("test2x")
            blob = bucket.blob(f"audio-files/{filename}")
            if not blob.exists():
                blob.upload_from_filename(audio_file_path)
                print(f"Subido {filename} a GCS.")
            else:
                print(f"{filename} ya existe en GCS.")


            run_batch_recognize(
                audio_gcs_uri=gcs_audio_uri,
                output_gcs_folder=gcs_output_uri,
                language_code=language_code
            )
            files_processed += 1
            print(f"Archivo {files_processed}/{total_files} procesado.\n")

            # Descargar la transcripción
            output_gcs_uri_json = f"{gcs_output_uri}/{os.path.splitext(filename)[0]}_transcript_*.json"
            
            blobs = storage_client.list_blobs("test2x", prefix=f"transcripts/{os.path.splitext(filename)[0]}")
            
            for blob in blobs:
                if blob.name.endswith(".json"):
                    local_output_path = os.path.join(output_dir, os.path.basename(blob.name))
                    blob.download_to_filename(local_output_path)
                    print(f"Descargado {blob.name} a {local_output_path}")


        except Exception as e:
            print(f"Error al procesar {filename}: {e}")
            continue

    print(f"¡Procesamiento completado! {files_processed}/{total_files} archivos procesados.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesa archivos de audio para generar transcripciones.")
    parser.add_argument('--input_dir', type=str, default="assets/audios", help="Directorio de entrada para los archivos de audio.")

    args = parser.parse_args()

    process_audio_files(
        input_dir=args.input_dir,
        output_dir=OUTPUT_DIRECTORY,
    )

```

Resultado. Modificado para mostrar una muestra de la salida JSON, con algunos valores eliminados por brevedad. El JSON completo contendrá información más detallada.

```json
{
    "results": [
        {
            "alternatives": [
                {
                    "transcript": "Here's To The Crazy Ones The Misfits the Rebels the troublemakers the round pegs in the square holes the ones who see things differently they're not fond of rules and they have no respect for the status quo",
                    "confidence": 0.95684826,
                    "words": [
                        {
                            "startOffset": "1s",
                            "endOffset": "4.200s",
                            "word": "Here's",
                            "confidence": 0.8265989
                        },
                        {
                            "startOffset": "4.200s",
                            "endOffset": "4.400s",
                            "word": "To",
                            "confidence": 0.9994259
                        },
                        {
                            "startOffset": "4.400s",
                            "endOffset": "4.400s",
                            "word": "The",
                            "confidence": 0.9994259
                        },
                        {
                            "startOffset": "4.400s",
                            "endOffset": "4.900s",
                            "word": "Crazy",
                            "confidence": 0.9975712
                        },
                        {
                            "startOffset": "4.900s",
                            "endOffset": "5.100s",
                            "word": "Ones",
                            "confidence": 0.9904002
                        },
                        {
                            "startOffset": "5.100s",
                            "endOffset": "6.700s",
                            "word": "The",
                            "confidence": 0.9994307
                        },
                        {
                            "startOffset": "6.700s",
                            "endOffset": "7.200s",
                            "word": "Misfits",
                            "confidence": 0.9352707
                        },
                        {
                            "startOffset": "7.200s",
                            "endOffset": "8.400s",
                            "word": "the",
                            "confidence": 0.99881697
                        },
                        {
                            "startOffset": "8.400s",
                            "endOffset": "8.800s",
                            "word": "Rebels",
                            "confidence": 0.9900544
                        },
                        {
                            "startOffset": "8.800s",
                            "endOffset": "10.300s",
                            "word": "the",
                            "confidence": 0.99904335
                        }                        
                    ]
                }
            ],
            "resultEndOffset": "23.780s",
            "languageCode": "en-us"
        }
    ]
}
```