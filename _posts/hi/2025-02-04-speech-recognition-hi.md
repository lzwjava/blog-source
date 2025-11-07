---
audio: true
generated: false
image: false
lang: hi
layout: post
title: वास्तविक समय भाषण पहचान
translated: true
type: post
---

यह पाइथन कोड Google क्लाउड स्पीच-टू-टेक्स्ट API और PyAudio लाइब्रेरी का उपयोग करके वास्तविक समय भाषण पहचान को कार्यान्वित करता है। यह माइक्रोफ़ोन से ऑडियो कैप्चर करता है, इसे स्पीच-टू-टेक्स्ट API पर स्ट्रीम करता है, और ट्रांसक्राइब्ड टेक्स्ट प्रिंट करता है। `MicrophoneStream` क्लास ऑडियो इनपुट को संभालता है, और `main` फ़ंक्शन स्पीच पहचान क्लाइंट सेट करता है और ऑडियो स्ट्रीम को संसाधित करता है।


```python
import os
import argparse
import io
import sys
import time

from google.cloud import speech

import pyaudio
from six.moves import queue


# ऑडियो रिकॉर्डिंग पैरामीटर
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


class MicrophoneStream(object):
    """ऑडियो चंक उत्पन्न करने वाले जनरेटर के रूप में रिकॉर्डिंग स्ट्रीम खोलता है।"""
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # PyAudio का उपयोग करके ऑडियो इंटरफ़ेस बनाएँ
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # API वर्तमान में केवल 1-चैनल (मोनो) ऑडियो का समर्थन करता है
            # https://goo.gl/z726ff
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            # बफ़र ऑब्जेक्ट को भरने के लिए ऑडियो स्ट्रीम को अतुल्यकालिक रूप से चलाएँ।
            # यह आवश्यक है ताकि कॉलिंग थ्रेड नेटवर्क अनुरोध आदि बनाते समय इनपुट डिवाइस का बफ़र ओवरफ़्लो न हो।
            stream_callback=self._fill_buffer,
        )
        self.closed = False
        self._buff = queue.Queue()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """बफ़र में, ऑडियो स्ट्रीम से लगातार डेटा एकत्र करें।"""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self, record_seconds):
        start_time = time.time()
        while not self.closed and time.time() - start_time < record_seconds:
            # यह सुनिश्चित करने के लिए ब्लॉकिंग get() का उपयोग करें कि कम से कम एक चंक डेटा है, और यदि चंक None है, तो पुनरावृत्ति को रोकें, जो ऑडियो स्ट्रीम के अंत को इंगित करता है।
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # अब जो भी अन्य डेटा अभी भी बफ़र किया गया है, उसे उपभोग करें।
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
        # जनरेटर को समाप्त करने के लिए संकेत दें ताकि क्लाइंट की स्ट्रीमिंग पहचान विधि प्रक्रिया समाप्ति को अवरुद्ध न करे।
        self._buff.put(None)
        self._audio_stream.close()
        self._audio_interface.terminate()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()


def main(record_seconds=10, language_code='en-US'):
    # समर्थित भाषाओं की सूची के लिए http://g.co/cloud/speech/docs/languages देखें।
    # language_code = 'en-US'  # एक BCP-47 भाषा टैग

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

        # अब, ट्रांसक्रिप्शन प्रतिक्रियाओं का उपयोग करें।
        transcript = ""
        for response in responses:
            print(response)
            # ट्रांसक्रिप्शन हो जाने के बाद, परिणाम प्रिंट करें।
            for result in response.results:
                if result.is_final:
                    alternative = result.alternatives[0]
                    transcript += alternative.transcript + " "
        print(u'Transcript: {}'.format(transcript))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="समायोज्य अवधि के साथ वास्तविक समय भाषण पहचान।")
    parser.add_argument('--duration', type=int, default=10, help="सेकंड में रिकॉर्डिंग की अवधि।")
    parser.add_argument('--language_code', type=str, default='en-US', help="ट्रांसक्रिप्शन के लिए भाषा कोड।")
    args = parser.parse_args()
    print("कृपया बोलें...")
    main(record_seconds=args.duration, language_code=args.language_code)

```
