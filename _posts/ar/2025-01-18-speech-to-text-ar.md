---
audio: true
lang: ar
layout: post
title: Google Cloud Speech-to-Text
translated: true
---

لقد قمت مؤخرًا بتجربة واجهة برمجة التطبيقات (API) الخاصة بتحويل الكلام إلى نص من Google Cloud. فيما يلي دالة Python استخدمتها لإجراء عملية النسخ.

```python
import os
import json
import time
import argparse
from google.cloud import speech
from pydub import AudioSegment
import tempfile

# دليل الإخراج الثابت
OUTPUT_DIRECTORY = "assets/transcriptions"


def speech_to_text(audio_file, output_filename):
    print(f"جاري إنشاء النسخ لـ: {output_filename}")
    try:
        client = speech.SpeechClient()

        # تحميل ملف الصوت باستخدام pydub لتحديد المعلمات
        audio_segment = AudioSegment.from_file(audio_file)
        sample_rate = audio_segment.frame_rate
        channels = audio_segment.channels

        # تحديد الترميز بناءً على امتداد الملف
        file_extension = os.path.splitext(audio_file)[1].lower()
        if file_extension == '.mp3':
            encoding = speech.RecognitionConfig.AudioEncoding.MP3
        elif file_extension in ['.wav', '.wave']:
            encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16
        elif file_extension == '.flac':
            encoding = speech.RecognitionConfig.AudioEncoding.FLAC
        else:
            print(f"تنسيق الملف غير مدعوم: {file_extension}")
            return

        # تكوين التعرف
        config = speech.RecognitionConfig(
            encoding=encoding,
            sample_rate_hertz=sample_rate,
            audio_channel_count=channels,
            language_code="en-US",  # تعيين بناءً على منطقك
        )

        with open(audio_file, "rb") as f:
            audio_content = f.read()

        audio = speech.RecognitionAudio(content=audio_content)

        # تنفيذ عملية التعرف على الكلام طويلة المدى
        try:
            operation = client.long_running_recognize(config=config, audio=audio)
            response = operation.result(timeout=300)  # تعديل المهلة حسب الحاجة
        except Exception as e:
            print(f"حدث خطأ أثناء النسخ: {e}")
            return
        
        print(response.results)

        transcription = ""
        for result in response.results:
            transcription += result.alternatives[0].transcript + "\n"

        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(transcription)
        print(f"تم كتابة النسخ إلى {output_filename}")

    except Exception as e:
        print(f"حدث خطأ أثناء إنشاء النسخ لـ {output_filename}: {e}")


def process_audio_files(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    all_audio_files = [f for f in os.listdir(input_dir) if f.endswith(('.mp3', '.wav', '.m4a'))]
    total_files = len(all_audio_files)
    print(f"إجمالي ملفات الصوت التي سيتم معالجتها: {total_files}")

    if total_files == 0:
        print(f"لم يتم العثور على ملفات صوتية في الدليل '{input_dir}'.")
        return

    files_processed = 0


    for filename in all_audio_files:
        audio_file_path = os.path.join(input_dir, filename)
        output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
        if os.path.exists(output_filename):
            print(f"تخطي {filename}: {output_filename} موجود بالفعل.")
            continue
        print(f"\nمعالجة {files_processed + 1}/{total_files}: {filename}")
        try:
            # تحديد اللغة بناءً على لاحقة اسم الملف
            if filename.endswith('-zh.mp3') or filename.endswith('-zh.wav') or filename.endswith('-zh.m4a'):
                language_code = "cmn-CN"
            else:
                language_code = "en-US"

            # تحديث التكوين في speech_to_text إذا لزم الأمر
            # للتبسيط، سنقوم بتعيين language_code في التكوين داخل speech_to_text

            speech_to_text(
                audio_file=audio_file_path,
                output_filename=output_filename,
            )
            files_processed += 1
            print(f"تمت معالجة الملف {files_processed}/{total_files}.\n")
        except Exception as e:
            print(f"فشل في معالجة {filename}: {e}")
            continue

    print(f"اكتملت المعالجة! تمت معالجة {files_processed}/{total_files} ملفات.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="معالجة ملفات الصوت لإنشاء نسخ.")
    parser.add_argument('--input_dir', type=str, default="assets/audios", help="دليل الإدخال لملفات الصوت.")


    args = parser.parse_args()


    process_audio_files(
        input_dir=args.input_dir,
        output_dir=OUTPUT_DIRECTORY,
    )
```