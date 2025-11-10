---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح ملفات AAC و M4A لواجهة برمجة تطبيقات جوجل للكلام
translated: true
type: note
---

نعم — ملفك هو **AAC في حاوية M4A** (تسجيلات صوتية للآيفون). خدمة Google Speech-to-Text v2 Batch غالبًا ما تفشل في فك تشفير AAC/M4A تلقائيًا وتُرجع هذا الخطأ الدقيق. قم بتحويله إلى برنامج ترميز/حاوية مدعوم أولاً — ثم إما احتفظ بـ `AutoDetectDecodingConfig()` أو (الأفضل) حدد فك التشفير بشكل صريح.

إليك أسرع طريقة.

## الخيار أ — إصلاح بسطر واحد باستخدام `ffmpeg` (موصى به: Ogg/Opus)

ملفات صغيرة، دقة عالية، مدعوم رسميًا.

```bash
# 48 كيلوهرتز، أحادي، Opus في OGG
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -c:a libopus -b:a 48k ~/Downloads/haifeng_and_zhiwei.ogg
```

ثم شغّل البرنامج النصي على الملف الجديد:

```bash
python scripts/agent/speech_to_text_agent.py --input_file ~/Downloads/haifeng_and_zhiwei.ogg
```

## الخيار ب — FLAC بدون فقدان (مدعوم أيضًا)

أصغر من WAV؛ بدون فقدان.

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -sample_fmt s16 -c:a flac ~/Downloads/haifeng_and_zhiwei.flac
```

## الخيار ج — Linear16 WAV (أكبر ملف)

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 16000 -sample_fmt s16 -c:a pcm_s16le ~/Downloads/haifeng_and_zhiwei.wav
```

---

## تعديلات الكود (حتى لا تواجه هذه المشكلة مرة أخرى)

1. **اسمح بامتدادات أكثر** واختر اللغة من اللاحقة بنفس الطريقة.
2. **قم بتحويل الترميز تلقائيًا** إلى تنسيق مدعوم (أنا أستخدم Ogg/Opus).
3. **أخبر واجهة البرمجة (API) بالضبط ما ترسله** (فك تشفير صريح).

ضع هذا في برنامجك النصي (تغييرات بسيطة ومركزة):

```python
import subprocess
import tempfile
from pathlib import Path
from google.cloud.speech_v2.types import cloud_speech

SUPPORTED_EXTS = {".ogg", ".flac", ".wav", ".mp3"}  # mp3 مدعوم أيضًا

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

    # افضل فك التشفير الصريح — يتجنب مفاجآت "ترميز غير مدعوم"
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
        decoding_cfg = cloud_speech.AutoDetectDecodingConfig()  # ارتداد

    config = cloud_speech.RecognitionConfig(
        explicit_decoding_config=decoding_cfg,
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
        language_codes=[language_code],
        # اختياري: التجزئة، علامات الترقيم، إلخ.
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

    # تحديد اللغة حسب اللاحقة
    language_code = "cmn-CN" if src.name.endswith("-zh" + src.suffix) else "en-US"

    # التأكد من ترميز/حاوية مدعومة
    if src.suffix.lower() not in SUPPORTED_EXTS:
        print(f"Transcoding {src.name} to Ogg/Opus...")
        input_file = _transcode_to_ogg_opus(str(src))
        src = Path(input_file)

    # التحكم في المخرجات للملف المحلي .txt (يمكنك الاحتفاظ به كما هو أو الاعتماد على stem)
    output_filename = os.path.join(output_dir, f"{src.stem}.txt")
    if os.path.exists(output_filename):
        print(f"Skipping {src.name}: {output_filename} already exists.")
        return

    print(f"Processing: {src.name}")

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket("test2x")
        # احتفظ بالمجلد "audio-files/"، احتفظ باسم الملف الحقيقي مع الامتداد الجديد
        blob = bucket.blob(f"audio-files/{src.name}")
        if not blob.exists():
            blob.upload_from_filename(str(src))
            print(f"Uploaded {src.name} to GCS.")
        else:
            print(f"{src.name} already exists in GCS.")

        gcs_audio_uri = f"gs://test2x/audio-files/{src.name}"
        gcs_output_uri = f"gs://test2x/transcripts/{src.stem}"

        # اختر فك التشفير بناءً على الامتداد
        ext = src.suffix.lower()
        if ext == ".ogg":
            decoding = "ogg_opus"
        elif ext == ".flac":
            decoding = "flac"
        elif ext == ".wav":
            decoding = "linear16"
        else:
            decoding = None  # ارتداد إلى الكشف التلقائي

        run_batch_recognize(
            audio_gcs_uri=gcs_audio_uri,
            output_gcs_folder=gcs_output_uri,
            language_code=language_code,
            decoding=decoding,
        )

        print(f"File {src.name} processed.\n")

        # تنزيل ناتج النسخ JSONs
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

### لماذا هذا الحل يعمل

* تسجيلات صوت iOS → **AAC/M4A**. خدمة Batch STT v2 لا تكتشف/تفك تشفير ذلك بموثوقية.
* من خلال تحويل الترميز إلى **OGG/Opus** (أو **FLAC/WAV**) و**إخبار واجهة البرمجة (API) ببرنامج الترميز**، تتجنب خطأ "ترميز غير مدعوم" تمامًا.

### نصائح عملية

* للتسجيلات الطويلة مثل **مذكتك الصوتية الأحادية لمدة 1 ساعة و21 دقيقة**، يحافظ **OGG/Opus 48k** على الجودة مع تقليل الحجم وحركة بيانات GCS.
* حافظ على وضع الأحادي (`-ac 1`). وضع الاستريو يضاعف التكلفة فقط دون مساعدة التعرف.
* إذا كانت المحادثة بالماندرين، رمز اللغة `"cmn-CN"` مناسب لك؛ استخدم اصطلاح التسمية `"-zh.m4a"` كما تفعل حاليًا.
* إذا كنت تحتاج إلى تحديد أدوار المتحدثين، فعّل التجزئة لاحقًا؛ أصلح مسار فك التشفير أولاً.

إذا أردت، يمكنني أيضًا إضافة **تحميل تلقائي محلي → إلى GCS + إعادة تسمية** اختياري بحيث يتم قبول الإدخال `m4a` الخاص بك ولكن مع معالجته دائمًا كـ `.ogg` داخليًا خلف الكواليس.