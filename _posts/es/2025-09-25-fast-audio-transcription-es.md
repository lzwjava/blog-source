---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast:free
title: Aceleración del Procesamiento de Transcripción de Audio Largo
translated: true
type: note
---

### ¿Por qué el procesamiento es tan largo para audio de 30 minutos o 1 hora?

La API por lotes Google Cloud Speech-to-Text (v2) está diseñada para operaciones asincrónicas de larga duración, especialmente con el modelo `"long"`, que maneja archivos de audio extensos (hasta ~1 hora por archivo). He aquí por qué puede parecer "demasiado largo":

-   **El Tiempo de Procesamiento Escala con la Duración del Audio**: La transcripción no es instantánea. Para un archivo de audio de 30 minutos, podría tomar de 5 a 20 minutos; para 1 hora, de 10 a 40 minutos o más. Esto incluye:
    -   Tiempo de encolamiento (si tu proyecto/región está ocupado).
    -   Transcripción real (inferencia del modelo de IA, que es intensiva en computación para audio largo).
    -   Post-procesamiento (ej.: marcas de tiempo de palabras, puntuaciones de confianza).
-   **Naturaleza por Lotes**: A diferencia del streaming en tiempo real, los trabajos por lotes se ejecutan en segundo plano en los servidores de Google. Tu script llama a `operation.result()`, que se bloquea y espera, pero el trabajo real ocurre de forma asincrónica.
-   **Otros Factores**:
    -   Formato/calidad del audio: OGG/Opus o M4A/AAC necesitan decodificación, lo que añade sobrecarga si las frecuencias de muestreo/canales no coinciden.
    -   Elección del modelo: `"long"` está optimizado para reuniones/podcasts pero es más lento que modelos más cortos como `"default"` o `"short"`.
    -   Red/Cuota: Subir a GCS, las llamadas a la API y descargar los resultados añaden latencia. Las cuotas del nivel gratuito o la alta demanda pueden retrasar los trabajos.
    -   No Hay Paralelismo Integrado: El script procesa un archivo a la vez de forma secuencial.

Si tu audio tiene consistentemente 30+ minutos, la configuración actual no es ideal para una respuesta rápida; es mejor para procesamiento offline/masivo.

### Cómo Solucionarlo: Reducir el Tiempo de Procesamiento

Para manejar audio largo más rápido, la clave es **dividir el archivo en fragmentos más pequeños** (ej.: de 5 a 15 minutos cada uno). Esto permite:
-   Procesamiento paralelo (ejecutar múltiples trabajos por lotes concurrentemente).
-   Usar modelos más rápidos (ej.: `"short"` o `"default"`) por fragmento.
-   Tiempos de espera más cortos por trabajo (ej.: 1-5 minutos por fragmento vs. 30+ minutos para el archivo completo).

#### Paso 1: Dividir el Archivo de Audio
Usa **FFmpeg** (gratuito, herramienta de línea de comandos) para dividir archivos sin recodificar (rápido y sin pérdidas). Instala FFmpeg si es necesario (ej.: `brew install ffmpeg` en macOS, `apt install ffmpeg` en Linux).

Añade una función a tu script para dividir el archivo de entrada. Aquí hay una versión actualizada de tu script con la división integrada:

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
CHUNK_DURATION_SECS = 600  # 10 minutos por fragmento; ajustar según sea necesario (ej., 900 para 15 min)


def split_audio_file(input_file, chunk_duration_secs=CHUNK_DURATION_SECS):
    """
    Divide un archivo de audio en fragmentos más pequeños usando FFmpeg.
    
    Args:
        input_file: Ruta al audio de entrada.
        chunk_duration_secs: Duración de cada fragmento en segundos.
    
    Returns:
        Lista de rutas de los archivos fragmentados.
    """
    filename = os.path.basename(input_file)
    name_without_ext = os.path.splitext(filename)[0]
    dir_name = os.path.dirname(input_file)
    
    # Crear directorio temporal para los fragmentos
    temp_dir = tempfile.mkdtemp()
    chunk_files = []
    
    # Comando FFmpeg (sin recodificar para velocidad)
    cmd = [
        "ffmpeg", "-i", input_file,
        "-f", "segment",  # Formato de salida
        "-segment_time", str(chunk_duration_secs),
        "-c", "copy",  # Copiar streams sin recodificar
        "-map", "0",  # Mapear todos los streams
        f"{temp_dir}/{name_without_ext}_chunk_%03d.{os.path.splitext(filename)[1][1:]}",  # Patrón de salida
        "-y"  # Sobrescribir
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        # Encontrar los fragmentos generados
        for file in os.listdir(temp_dir):
            if file.startswith(f"{name_without_ext}_chunk_") and file.endswith(os.path.splitext(filename)[1]):
                chunk_files.append(os.path.join(temp_dir, file))
        chunk_files.sort()  # Ordenar por nombre (ej., chunk_001, chunk_002)
        print(f"Dividido {filename} en {len(chunk_files)} fragmentos.")
        return chunk_files
    except subprocess.CalledProcessError as e:
        print(f"Error de FFmpeg al dividir {filename}: {e}")
        return []


def run_batch_recognize(audio_gcs_uri, output_gcs_folder, language_code="en-US"):
    """
    Transcribe un archivo de audio usando Google Cloud Speech-to-Text Batch API.
    Actualizado para usar un modelo más corto si el audio es probablemente corto (ej., después de dividir).
    """
    client = SpeechClient()

    filename = audio_gcs_uri.split('/')[-1]
    file_extension = filename.split('.')[-1].lower()

    # Para fragmentos, usar modelo "short" o "default" para velocidad (si <15 min)
    model = "short" if CHUNK_DURATION_SECS < 900 else "long"  # Ajustar basado en el tamaño del fragmento

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

    print(f"Iniciando reconocimiento por lotes para {filename}...")
    operation = client.batch_recognize(request=request)
    
    # Sondeo para progreso (ver más abajo para detalles)
    poll_operation_with_progress(operation, filename)
    
    response = operation.result(timeout=3 * CHUNK_DURATION_SECS)  # Timeout más corto por fragmento
    print(f"Transcripción completada para {filename}. Respuesta: {response}")
    return response


def poll_operation_with_progress(operation, filename):
    """
    Sondea la operación de larga duración y muestra el progreso.
    """
    while not operation.done():
        # Obtener metadatos de la operación (si están disponibles; Speech API proporciona un estado básico)
        try:
            metadata = operation.metadata
            print(f"Progreso para {filename}: Estado={getattr(metadata, 'state', 'Desconocido')}, "
                  f"Procesado={getattr(metadata, 'progress_bytes', 'N/A')} bytes")
        except Exception:
            print(f"Esperando por {filename}... (verificando cada 30s)")
        
        time.sleep(30)  # Sondeo cada 30 segundos
    if operation.exception():
        raise operation.exception()


def process_audio_file(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.basename(input_file)
    if not (filename.endswith(".m4a") or filename.endswith(".ogg")):
        print(f"Error: {filename} no es un archivo de audio soportado (.m4a o .ogg).")
        return

    output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
    if os.path.exists(output_filename):
        print(f"Omitiendo {filename}: {output_filename} ya existe.")
        return

    print(f"Procesando: {filename}")

    # Determinar el idioma
    if filename.endswith("-zh.m4a") or filename.endswith("-zh.ogg"):
        language_code = "cmn-CN"
    else:
        language_code = "en-US"

    # Dividir en fragmentos si el archivo es largo (heurístico: >15 min, pero se puede sondear la duración con ffprobe)
    chunk_files = []
    if os.path.getsize(input_file) > 100 * 1024 * 1024:  # Comprobación aproximada: >100MB probablemente largo
        print(f"El archivo es grande; dividiendo en fragmentos de {CHUNK_DURATION_SECS//60} minutos.")
        chunk_files = split_audio_file(input_file)
        if not chunk_files:
            print("La división falló; procesando como archivo único.")
            chunk_files = [input_file]
    else:
        chunk_files = [input_file]

    storage_client = storage.Client()
    bucket = storage_client.bucket("test2x")

    all_transcripts = []  # Para combinar luego

    for chunk_idx, chunk_file in enumerate(chunk_files):
        chunk_filename = os.path.basename(chunk_file)
        base_name = os.path.splitext(filename)[0]
        chunk_name = f"{base_name}_chunk_{chunk_idx+1:03d}"
        
        # Construir rutas GCS
        gcs_audio_uri = f"gs://test2x/audio-files/{chunk_filename}"
        gcs_output_uri = f"gs://test2x/transcripts/{chunk_name}"

        # Subir fragmento si es necesario
        blob = bucket.blob(f"audio-files/{chunk_filename}")
        if not blob.exists():
            blob.upload_from_filename(chunk_file)
            print(f"Fragmento {chunk_filename} subido a GCS.")
        else:
            print(f"El fragmento {chunk_filename} ya está en GCS.")

        # Transcribir
        try:
            run_batch_recognize(
                audio_gcs_uri=gcs_audio_uri,
                output_gcs_folder=gcs_output_uri,
                language_code=language_code,
            )

            # Descargar y recopilar la transcripción
            blobs = storage_client.list_blobs("test2x", prefix=f"transcripts/{chunk_name}")
            chunk_transcript = ""
            for b in blobs:
                if b.name.endswith(".json"):
                    local_path = os.path.join(output_dir, f"{os.path.basename(b.name)}")
                    b.download_to_filename(local_path)
                    # Parsear JSON para extraer texto (simplificado; usar módulo json para un análisis completo)
                    import json
                    with open(local_path, 'r') as f:
                        data = json.load(f)
                        if 'results' in data:
                            chunk_text = ' '.join([result.get('alternatives', [{}])[0].get('transcript', '') for result in data['results']])
                            chunk_transcript += chunk_text + "\n"
                    print(f"Descargado y analizado {b.name}")

            all_transcripts.append(chunk_transcript)

            # Limpiar fragmento temporal si se dividió
            if chunk_file != input_file and os.path.exists(chunk_file):
                os.remove(chunk_file)

        except Exception as e:
            print(f"Error al procesar el fragmento {chunk_filename}: {e}")

    # Combinar todas las transcripciones en un archivo
    combined_text = "\n\n--- Límite del Fragmento ---\n\n".join(all_transcripts)
    with open(output_filename, 'w') as f:
        f.write(combined_text)
    print(f"Transcripción combinada guardada en {output_filename}")

    # Limpiar directorio temporal si ocurrió una división
    if chunk_files != [input_file]:
        import shutil
        shutil.rmtree(os.path.dirname(chunk_files[0]) if chunk_files else None)

    print(f"Procesamiento completado para {filename}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Procesa un único archivo de Memo de Voz (.m4a/.ogg) para generar la transcripción."
    )
    parser.add_argument(
        "--input_file",
        type=str,
        required=True,
        help="Ruta de entrada para el archivo de Memo de Voz.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="assets/transcriptions",
        help="Directorio de salida para las transcripciones.",
    )
    parser.add_argument(
        "--chunk_secs",
        type=int,
        default=CHUNK_DURATION_SECS,
        help="Duración del fragmento en segundos (para dividir archivos largos).",
    )

    args = parser.parse_args()
    global CHUNK_DURATION_SECS  # Permitir anulación
    CHUNK_DURATION_SECS = args.chunk_secs

    process_audio_file(
        input_file=args.input_file,
        output_dir=args.output,
    )
```

#### Cambios Clave y Beneficios:
-   **División**: Usa FFmpeg para crear fragmentos no superpuestos (ej.: 10 min cada uno). Para un archivo de 1 hora, son ~6 trabajos, que pueden ejecutarse en paralelo si modificas para usar hilos/multiprocesamiento (ej.: mediante `concurrent.futures`).
-   **Modelo Más Rápido**: Cambia a `"short"` para fragmentos <15 min—procesa 2-3x más rápido.
-   **Combinación de Transcripciones**: Analiza las salidas JSON y las fusiona en un único archivo `.txt` con límites para una fácil lectura.
-   **Limpieza**: Elimina fragmentos temporales y blobs GCS antiguos si es necesario (añade `blob.delete()` en un bucle).
-   **Uso**: Ejecuta como antes, ej., `python script.py --input_file long_audio.m4a --chunk_secs 600`. Para no dividir, usa un `--chunk_secs` grande (ej.: 3600).

#### Otras Optimizaciones:
-   **Procesamiento Paralelo**: Si tienes muchos fragmentos/archivos, usa `ThreadPoolExecutor` de Python para enviar trabajos `run_batch_recognize` concurrentemente (limita a 5-10 para evitar exceder cuotas).
-   **Sondear la Duración del Audio**: Usa `ffprobe` (FFmpeg) para decidir dinámicamente si se necesita dividir: `ffprobe -v quiet -show_entries format=duration -of csv=p=0 input.m4a`.
-   **Cambiar a la API de Streaming**: Para uso interactivo, usa `recognize` síncrono (límite ~1 min/archivo) o streaming para en vivo, pero no es ideal para archivos largos por lotes.
-   **Costos/Cuotas**: Verifica tu cuota de Google Cloud (Speech-to-Text permite ~1000 req/min). Los trabajos largos consumen más créditos (~$0.036/min para el modelo estándar).
-   **Probar Primero con Archivos Más Cortos**: Comienza con `--chunk_secs 300` (5 min) para ver la aceleración.

### Mostrar el Progreso: Sondear la Operación

La función actualizada `poll_operation_with_progress()` reemplaza el bloqueante `operation.result()`. Esta:
-   Verifica cada 30 segundos.
-   Imprime el estado desde `operation.metadata` (ej.: estado como "RUNNING" o "DONE", y bytes procesados si están disponibles—los metadatos de Speech API son básicos, pero es mejor que nada).
-   Lanza un error si falla.

Para un progreso más detallado (ej.: % completado), la Speech API no proporciona métricas granulares, pero puedes:
-   Monitorear mediante Google Cloud Console (página de Operaciones para tu proyecto).
-   Usar la CLI `gcloud`: `gcloud alpha speech operations describe OPERATION_ID --project=graphite-ally-445108-k3`.
-   Después de la finalización, los resultados JSON incluyen indirectamente el progreso por utterance a través de las marcas de tiempo.

Si se divide, verás progreso intercalado de múltiples fragmentos, haciendo que se sienta menos "atascado".

Si esto no resuelve tu problema (ej.: errores específicos), ¡comparte los registros/salida para más ajustes