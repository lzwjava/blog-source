---
audio: true
lang: hi
layout: post
title: Google Cloud Speech-to-Text
translated: true
---

मैंने हाल ही में Google Cloud के Speech-to-Text API के साथ प्रयोग किया। निम्नलिखित एक Python फ़ंक्शन है जिसका उपयोग मैंने ट्रांसक्रिप्शन करने के लिए किया।

```python
import os
import json
import time
import argparse
from google.cloud import speech
from pydub import AudioSegment
import tempfile

# निश्चित आउटपुट डायरेक्टरी
OUTPUT_DIRECTORY = "assets/transcriptions"


def speech_to_text(audio_file, output_filename):
    print(f"ट्रांसक्रिप्शन जनरेट कर रहा हूँ: {output_filename}")
    try:
        client = speech.SpeechClient()

        # ऑडियो फ़ाइल को pydub के साथ लोड करें ताकि पैरामीटर निर्धारित किए जा सकें
        audio_segment = AudioSegment.from_file(audio_file)
        sample_rate = audio_segment.frame_rate
        channels = audio_segment.channels

        # फ़ाइल एक्सटेंशन के आधार पर एन्कोडिंग निर्धारित करें
        file_extension = os.path.splitext(audio_file)[1].lower()
        if file_extension == '.mp3':
            encoding = speech.RecognitionConfig.AudioEncoding.MP3
        elif file_extension in ['.wav', '.wave']:
            encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16
        elif file_extension == '.flac':
            encoding = speech.RecognitionConfig.AudioEncoding.FLAC
        else:
            print(f"असमर्थित फ़ाइल प्रारूप: {file_extension}")
            return

        # रिकग्निशन कॉन्फ़िगर करें
        config = speech.RecognitionConfig(
            encoding=encoding,
            sample_rate_hertz=sample_rate,
            audio_channel_count=channels,
            language_code="en-US",  # अपने तर्क के आधार पर सेट करें
        )

        with open(audio_file, "rb") as f:
            audio_content = f.read()

        audio = speech.RecognitionAudio(content=audio_content)

        # लंबे समय तक चलने वाली स्पीच रिकग्निशन करें
        try:
            operation = client.long_running_recognize(config=config, audio=audio)
            response = operation.result(timeout=300)  # टाइमआउट को आवश्यकतानुसार समायोजित करें
        except Exception as e:
            print(f"ट्रांसक्रिप्शन के दौरान त्रुटि: {e}")
            return
        
        print(response.results)

        transcription = ""
        for result in response.results:
            transcription += result.alternatives[0].transcript + "\n"

        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(transcription)
        print(f"ट्रांसक्रिप्शन {output_filename} में लिखा गया।")

    except Exception as e:
        print(f"{output_filename} के लिए ट्रांसक्रिप्शन जनरेट करते समय एक त्रुटि हुई: {e}")


def process_audio_files(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    all_audio_files = [f for f in os.listdir(input_dir) if f.endswith(('.mp3', '.wav', '.m4a'))]
    total_files = len(all_audio_files)
    print(f"प्रोसेस करने के लिए कुल ऑडियो फ़ाइलें: {total_files}")

    if total_files == 0:
        print(f"'{input_dir}' डायरेक्टरी में कोई ऑडियो फ़ाइल नहीं मिली।")
        return

    files_processed = 0


    for filename in all_audio_files:
        audio_file_path = os.path.join(input_dir, filename)
        output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
        if os.path.exists(output_filename):
            print(f"{filename} को छोड़ रहा हूँ: {output_filename} पहले से मौजूद है।")
            continue
        print(f"\nप्रोसेस कर रहा हूँ {files_processed + 1}/{total_files}: {filename}")
        try:
            # फ़ाइलनाम सफ़िक्स के आधार पर भाषा निर्धारित करें
            if filename.endswith('-zh.mp3') or filename.endswith('-zh.wav') or filename.endswith('-zh.m4a'):
                language_code = "cmn-CN"
            else:
                language_code = "en-US"

            # यदि आवश्यक हो तो speech_to_text में कॉन्फ़िग अपडेट करें
            # सरलता के लिए, हम speech_to_text में language_code को कॉन्फ़िग में सेट करेंगे

            speech_to_text(
                audio_file=audio_file_path,
                output_filename=output_filename,
            )
            files_processed += 1
            print(f"फ़ाइल {files_processed}/{total_files} प्रोसेस की गई।\n")
        except Exception as e:
            print(f"{filename} को प्रोसेस करने में विफल: {e}")
            continue

    print(f"प्रोसेसिंग पूर्ण! {files_processed}/{total_files} फ़ाइलें प्रोसेस की गईं।")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ट्रांसक्रिप्शन जनरेट करने के लिए ऑडियो फ़ाइलों को प्रोसेस करें।")
    parser.add_argument('--input_dir', type=str, default="assets/audios", help="ऑडियो फ़ाइलों के लिए इनपुट डायरेक्टरी।")


    args = parser.parse_args()


    process_audio_files(
        input_dir=args.input_dir,
        output_dir=OUTPUT_DIRECTORY,
    )
```