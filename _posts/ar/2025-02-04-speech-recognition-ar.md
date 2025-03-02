---
audio: true
generated: true
lang: ar
layout: post
title: التعرف على الكلام في الوقت الحقيقي
translated: true
---

يقوم هذا الكود بلغة بايثون بتنفيذ التعرف على الكلام في الوقت الحقيقي باستخدام واجهة برمجة تطبيقات Google Cloud Speech-to-Text و مكتبة PyAudio.  يقوم الكود بالتقاط الصوت من الميكروفون، ويبثه إلى واجهة برمجة تطبيقات Speech-to-Text، ويطبع النص المُنسخ. تتعامل فئة `MicrophoneStream` مع إدخال الصوت، وتقوم الدالة `main` بإعداد عميل التعرف على الكلام ومعالجة تدفق الصوت.


```python
import os
import argparse
import io
import sys
import time

from google.cloud import speech

import pyaudio
from six.moves import queue


# معلمات تسجيل الصوت
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


class MicrophoneStream(object):
    """يفتح دفق تسجيل كمولد يُنتج أجزاء الصوت."""
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # إنشاء واجهة صوتية باستخدام PyAudio
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # تدعم واجهة البرمجة حاليًا الصوت أحادي القناة فقط (مونو)
            # https://goo.gl/z726ff
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            # تشغيل دفق الصوت بشكل غير متزامن لملء كائن المخزن المؤقت.
            # هذا ضروري حتى لا يفيض المخزن المؤقت لجهاز الإدخال
            # بينما يقوم مؤشر ترابط الاتصال بطلبات الشبكة، إلخ.
            stream_callback=self._fill_buffer,
        )
        self.closed = False
        self._buff = queue.Queue()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """جمع البيانات باستمرار من دفق الصوت، في المخزن المؤقت."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self, record_seconds):
        start_time = time.time()
        while not self.closed and time.time() - start_time < record_seconds:
            # استخدام دالة get() المُحجزة للتأكد من وجود جزء واحد على الأقل من
            # البيانات، وإيقاف التكرار إذا كان الجزء فارغًا، مما يشير إلى
            # نهاية دفق الصوت.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # الآن استهلك أي بيانات أخرى لا تزال مُخزنة مؤقتًا.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data)

    def close(self):
        self.closed = True
        # إرسال إشارة إلى المولد لإنهاء عمله حتى لا
        # تحجب طريقة التعرف على البث في العميل عملية الإنهاء.
        self._buff.put(None)
        self._audio_stream.close()
        self._audio_interface.terminate()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()


def main(record_seconds=10, language_code='en-US'):
    # انظر http://g.co/cloud/speech/docs/languages
    # للحصول على قائمة باللغات المدعومة.
    # language_code = 'en-US'  # وسم لغة BCP-47

    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code,
        model="latest_long",
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config,
        interim_results=True)

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator(record_seconds)
        requests = (speech.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests)

        # الآن، استخدام استجابات النسخ.
        transcript = ""
        for response in responses:
            print(response)
            # بمجرد الانتهاء من النسخ، اطبع النتيجة.
            for result in response.results:
                if result.is_final:
                    alternative = result.alternatives[0]
                    transcript += alternative.transcript + " "
        print(u'Transcript: {}'.format(transcript))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="التعرف على الكلام في الوقت الحقيقي مع مدة قابلة للتعديل.")
    parser.add_argument('--duration', type=int, default=10, help="مدة التسجيل بالثواني.")
    parser.add_argument('--language_code', type=str, default='en-US', help="رمز اللغة للنسخ.")
    args = parser.parse_args()
    print("من فضلك تحدث...")
    main(record_seconds=args.duration, language_code=args.language_code)

```
