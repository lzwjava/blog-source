---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: تسريع معالجة نسخ التسجيلات الصوتية الطويلة
translated: true
type: note
---

### لماذا تستغرق المعالجة وقتًا طويلاً لتسجيلات 30 دقيقة أو ساعة واحدة؟

تم تصميم واجهة برمجة تطبيقات Google Cloud Speech-toText Batch (الإصدار 2) للعمليات غير المتزامنة طويلة المدى، خاصة مع النموذج `"long"` الذي يتعامل مع ملفات الصوت الممتدة (حتى ~1 ساعة لكل ملف). إليك السبب الذي قد يجعلها تبدو "طويلة جدًا":

- **وقت المعالجة يتناسب مع طول الصوت**: التحويل إلى نص ليس فوريًا. بالنسبة لملف صوت مدته 30 دقيقة، قد يستغرق من 5 إلى 20 دقيقة؛ أما لمدة ساعة واحدة، فقد يستغرق من 10 إلى 40 دقيقة أو أكثر. وهذا يشمل:
  - وقت الانتظار في قائمة الانتظار (إذا كان مشروعك/منطقتك مشغولاً).
  - التحويل الفعلي إلى نص (الاستدلال بواسطة نموذج الذكاء الاصطناعي، وهو كثيف الاستخدام للحوسبة للصوت الطويل).
  - المعالجة اللاحقة (مثل: الطابع الزمني للكلمات، درجات الثقة).
- **طبيعة الدُفعات**: على عكس البث المباشر (streaming)، تعمل مهام الدُفعات في الخلفية على خوادم جوجل. البرنامج النصي الخاص بك يستدعي `operation.result()`، والتي توقف التنفيذ وتنتظر، لكن العمل الحقيقي يحدث بشكل غير متزامن.
- **عوامل أخرى**:
  - تنسيق/جودة الصوت: تنسيقات مثل OGG/Opus أو M4A/AAC تحتاج إلى فك تشفير، مما يضيف عبئًا إضافيًا إذا كانت معدلات العدد (sample rates) أو القنوات غير متطابقة.
  - اختيار النموذج: النموذج `"long"` مُحسَّن للاجتماعات/البودكاست ولكنه أبطأ من النماذج الأقصر مثل `"default"` أو `"short"`.
  - الشبكة/الحصة: تحميل الملفات إلى GCS، واستدعاءات واجهة برمجة التطبيقات، وتنزيل النتائج تضيف زمن انتقال. قد تؤخر الحصص المجانية أو الطلب المرتفع المهام.
  - لا يوجد توازي مدمج: البرنامج النصي يعالج ملفًا واحدًا في كل مرة بشكل تسلسلي.

إذا كان الصوت لديك باستمرار 30+ دقيقة، فإن الإعداد الحالي ليس مثاليًا للإنجاز السريع — فهو أفضل للمعالجة غير المتصلة بالإنترنت/المجموعات الكبيرة.

### كيفية إصلاح ذلك: تقليل وقت المعالجة

للتعامل مع الصوت الطويل بشكل أسرع، المفتاح هو **تقسيم الملف إلى أجزاء أصغر** (على سبيل المثال، من 5 إلى 15 دقيقة لكل جزء). هذا يسمح بـ:
- المعالجة المتوازية (تشغيل مهام دفعات متعددة في وقت واحد).
- استخدام نماذج أسرع (مثل `"short"` أو `"default"`) لكل جزء.
- أوقات انتظار أقصر لكل مهمة (على سبيل المثال، من 1 إلى 5 دقائق لكل جزء مقابل 30+ دقيقة للملف بأكمله).

#### الخطوة 1: تقسيم ملف الصوت
استخدم **FFmpeg** (أداة مجانية لسطر الأوامر) لتقسيم الملفات دون إعادة التشفير (سريع وبدون فقدان البيانات). قم بتثبيت FFmpeg إذا لزم الأمر (مثل `brew install ffmpeg` على macOS، `apt install ffmpeg` على Linux).

أضف دالة إلى البرنامج النصي الخاص بك لتقسيم ملف الإدخال. إليك نسخة محدثة من البرنامج النصي الخاص بك مع دمج التقسيم:

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
CHUNK_DURATION_SECS = 600  # 10 minutes per chunk; adjust as needed (e.g., 900 for 15 min)


def split_audio_file(input_file, chunk_duration_secs=CHUNK_DURATION_SECS):
    """
    Split audio file into smaller chunks using FFmpeg.
    
    Args:
        input_file: Path to input audio.
        chunk_duration_secs: Duration of each chunk in seconds.
    
    Returns:
        List of chunk file paths.
    """
    filename = os.path.basename(input_file)
    name_without_ext = os.path.splitext(filename)[0]
    dir_name = os.path.dirname(input_file)
    
    # Create temp dir for chunks
    temp_dir = tempfile.mkdtemp()
    chunk_files = []
    
    # FFmpeg command (no re-encoding for speed)
    cmd = [
        "ffmpeg", "-i", input_file,
        "-f", "segment",  # Output format
        "-segment_time", str(chunk_duration_secs),
        "-c", "copy",  # Copy streams without re-encoding
        "-map", "0",  # Map all streams
        f"{temp_dir}/{name_without_ext}_chunk_%03d.{os.path.splitext(filename)[1][1:]}",  # Output pattern
        "-y"  # Overwrite
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        # Find generated chunks
        for file in os.listdir(temp_dir):
            if file.startswith(f"{name_without_ext}_chunk_") and file.endswith(os.path.splitext(filename)[1]):
                chunk_files.append(os.path.join(temp_dir, file))
        chunk_files.sort()  # Sort by name (e.g., chunk_001, chunk_002)
        print(f"Split {filename} into {len(chunk_files)} chunks.")
        return chunk_files
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg error splitting {filename}: {e}")
        return []


def run_batch_recognize(audio_gcs_uri, output_gcs_folder, language_code="en-US"):
    """
    Transcribes an audio file using Google Cloud Speech-to-Text Batch API.
    Updated to use shorter model if audio is likely short (e.g., after splitting).
    """
    client = SpeechClient()

    filename = audio_gcs_uri.split('/')[-1]
    file_extension = filename.split('.')[-1].lower()

    # For chunks, use "short" or "default" model for speed (if <15 min)
    model = "short" if CHUNK_DURATION_SECS < 900 else "long"  # Adjust based on chunk size

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

    print(f"Starting batch recognize for {filename}...")
    operation = client.batch_recognize(request=request)
    
    # Poll for progress (see below for details)
    poll_operation_with_progress(operation, filename)
    
    response = operation.result(timeout=3 * CHUNK_DURATION_SECS)  # Shorter timeout per chunk
    print(f"Completed transcription for {filename}. Response: {response}")
    return response


def poll_operation_with_progress(operation, filename):
    """
    Poll the long-running operation and show progress.
    """
    while not operation.done():
        # Get operation metadata (if available; Speech API provides basic status)
        try:
            metadata = operation.metadata
            print(f"Progress for {filename}: State={getattr(metadata, 'state', 'Unknown')}, "
                  f"Processed={getattr(metadata, 'progress_bytes', 'N/A')} bytes")
        except Exception:
            print(f"Waiting for {filename}... (checking every 30s)")
        
        time.sleep(30)  # Poll every 30 seconds
    if operation.exception():
        raise operation.exception()


def process_audio_file(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.basename(input_file)
    if not (filename.endswith(".m4a") or filename.endswith(".ogg")):
        print(f"Error: {filename} is not a supported audio file (.m4a or .ogg).")
        return

    output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
    if os.path.exists(output_filename):
        print(f"Skipping {filename}: {output_filename} already exists.")
        return

    print(f"Processing: {filename}")

    # Determine language
    if filename.endswith("-zh.m4a") or filename.endswith("-zh.ogg"):
        language_code = "cmn-CN"
    else:
        language_code = "en-US"

    # Split into chunks if file is long (heuristic: >15 min, but you can probe duration with ffprobe)
    chunk_files = []
    if os.path.getsize(input_file) > 100 * 1024 * 1024:  # Rough check: >100MB likely long
        print(f"File is large; splitting into {CHUNK_DURATION_SECS//60}-minute chunks.")
        chunk_files = split_audio_file(input_file)
        if not chunk_files:
            print("Splitting failed; processing as single file.")
            chunk_files = [input_file]
    else:
        chunk_files = [input_file]

    storage_client = storage.Client()
    bucket = storage_client.bucket("test2x")

    all_transcripts = []  # To combine later

    for chunk_idx, chunk_file in enumerate(chunk_files):
        chunk_filename = os.path.basename(chunk_file)
        base_name = os.path.splitext(filename)[0]
        chunk_name = f"{base_name}_chunk_{chunk_idx+1:03d}"
        
        # Construct GCS paths
        gcs_audio_uri = f"gs://test2x/audio-files/{chunk_filename}"
        gcs_output_uri = f"gs://test2x/transcripts/{chunk_name}"

        # Upload chunk if needed
        blob = bucket.blob(f"audio-files/{chunk_filename}")
        if not blob.exists():
            blob.upload_from_filename(chunk_file)
            print(f"Uploaded chunk {chunk_filename} to GCS.")
        else:
            print(f"Chunk {chunk_filename} already in GCS.")

        # Transcribe
        try:
            run_batch_recognize(
                audio_gcs_uri=gcs_audio_uri,
                output_gcs_folder=gcs_output_uri,
                language_code=language_code,
            )

            # Download and collect transcript
            blobs = storage_client.list_blobs("test2x", prefix=f"transcripts/{chunk_name}")
            chunk_transcript = ""
            for b in blobs:
                if b.name.endswith(".json"):
                    local_path = os.path.join(output_dir, f"{os.path.basename(b.name)}")
                    b.download_to_filename(local_path)
                    # Parse JSON to extract text (simplified; use json module for full parsing)
                    import json
                    with open(local_path, 'r') as f:
                        data = json.load(f)
                        if 'results' in data:
                            chunk_text = ' '.join([result.get('alternatives', [{}])[0].get('transcript', '') for result in data['results']])
                            chunk_transcript += chunk_text + "\n"
                    print(f"Downloaded and parsed {b.name}")

            all_transcripts.append(chunk_transcript)

            # Clean up temp chunk if split
            if chunk_file != input_file and os.path.exists(chunk_file):
                os.remove(chunk_file)

        except Exception as e:
            print(f"Failed to process chunk {chunk_filename}: {e}")

    # Combine all transcripts into one file
    combined_text = "\n\n--- Chunk Boundary ---\n\n".join(all_transcripts)
    with open(output_filename, 'w') as f:
        f.write(combined_text)
    print(f"Combined transcript saved to {output_filename}")

    # Clean up temp dir if splitting occurred
    if chunk_files != [input_file]:
        import shutil
        shutil.rmtree(os.path.dirname(chunk_files[0]) if chunk_files else None)

    print(f"Processing complete for {filename}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process a single Voice Memo (.m4a/.ogg) file to generate transcription."
    )
    parser.add_argument(
        "--input_file",
        type=str,
        required=True,
        help="Input path for the Voice Memo file.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="assets/transcriptions",
        help="Output directory for transcriptions.",
    )
    parser.add_argument(
        "--chunk_secs",
        type=int,
        default=CHUNK_DURATION_SECS,
        help="Chunk duration in seconds (for splitting long files).",
    )

    args = parser.parse_args()
    global CHUNK_DURATION_SECS  # Allow override
    CHUNK_DURATION_SECS = args.chunk_secs

    process_audio_file(
        input_file=args.input_file,
        output_dir=args.output,
    )
```

#### التغييرات الرئيسية والفوائد:
- **التقسيم**: يستخدم FFmpeg لإنشاء أجزاء غير متداخلة (على سبيل المثال، 10 دقائق لكل جزء). بالنسبة لملف مدته ساعة واحدة، هذا يعني حوالي 6 مهام، يمكن تشغيلها بالتوازي إذا قمت بتعديل البرنامج النصي لاستخدام threading/multiprocessing (على سبيل المثال، عبر `concurrent.futures`).
- **نموذج أسرع**: يتحول إلى النموذج `"short"` للأجزاء الأقل من 15 دقيقة — تتم المعالجة أسرع بـ 2-3 مرات.
- **دمج النصوص**: يحلل مخرجات JSON ويدمجها في ملف `.txt` واحد مع حدود لتسهيل القراءة.
- **التنظيف**: يزيل الأجزاء المؤقتة والبيانات القديمة في GCS إذا لزم الأمر (أضف `blob.delete()` في حلقة).
- **طريقة الاستخدام**: شغِّل كما كان من قبل، على سبيل المثال: `python script.py --input_file long_audio.m4a --chunk_secs 600`. لعدم التقسيم، استخدم قيمة كبيرة لـ `--chunk_secs` (على سبيل المثال، 3600).

#### تحسينات أخرى:
- **المعالجة المتوازية**: إذا كان لديك العديد من الأجزاء/الملفات، استخدم `ThreadPoolExecutor` في Python لإرسال مهام `run_batch_recognize` في وقت واحد (قم بالحد إلى 5-10 لتجنب تجاوز الحصص).
- **فحص مدة الصوت**: استخدم `ffprobe` (من FFmpeg) لتقرير ديناميكيًا ما إذا كان التقسيم مطلوبًا: `ffprobe -v quiet -show_entries format=duration -of csv=p=0 input.m4a`.
- **التحويل إلى واجهة برمجة تطبيقات البث المباشر (Streaming API)**: للاستخدام التفاعلي، استخدم `recognize` المتزامن (يحد من ~1 دقيقة/ملف) أو البث المباشر للبث الحي، لكنه ليس مثاليًا لملفات الدُفعات الطويلة.
- **التكاليف/الحصص**: تحقق من حصتك في Google Cloud (تسمح Speech-to-Text بحوالي 1000 طلب/دقيقة). المهام الطويلة تستهلك رصيدًا أكثر (~$0.036/دقيقة للنموذج القياسي).
- **اختبار الأجزاء الأقصر أولاً**: ابدأ بـ `--chunk_secs 300` (5 دقائق) لمعرفة تسريع الأداء.

### عرض التقدم: استطلاع حالة العملية (Polling the Operation)

تحل الدالة المحدثة `poll_operation_with_progress()` محل `operation.result()` الحاجِز. إنها:
- تتحقق كل 30 ثانية.
- تطبع الحالة من `operation.metadata` (على سبيل المثال، الحالة مثل "RUNNING" أو "DONE"، وعدد البايتات المعالجة إذا كانت متاحة — بيانات وصفية لواجهة برمجة تطبيقات الصوت أساسية، لكنها أفضل من لا شيء).
- ترفع خطأ إذا فشلت.

للحصول على تقدم مفصل أكثر (على سبيل المثال، نسبة الإكمال)، لا توفر واجهة برمجة تطبيقات الصوت مقاييس مفصلة، لكن يمكنك:
- المراقبة عبر Google Cloud Console (صفحة العمليات لمشروعك).
- استخدام `gcloud` CLI: `gcloud alpha speech operations describe OPERATION_ID --project=graphite-ally-445108-k3`.
- بعد الاكتمال، تتضمن نتائج JSON تقدمًا غير مباشر لكل جملة عبر الطوابع الزمنية.

إذا قمت بالتقسيم، سترى تقدمًا متداخلًا من أجزاء متعددة، مما يجعله يبدو أقل "توقفًا".

إذا لم يحل هذا مشكلتك (على سبيل المثال، أخطاء محددة)، شارج سجلات/مخرجات البرنامج لمزيد من التعديلات!