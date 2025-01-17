---
audio: true
lang: hi
layout: post
title: संवाद ऑडियो जनरेशन
translated: true
---

प्रॉम्प्ट:

```
इस PDF के बारे में कम से कम 100 राउंड की बातचीत करें और सभी विवरणों को कवर करें, इस PDF के बारे में JSON फॉर्मेट में जानकारी दें।


[
    {
      "speaker": "A",
      "line": "हे, मैंने हाल ही में Machine Learning (ML), Deep Learning (DL), और GPT के बारे में बहुत कुछ सुना है। क्या आप मुझे इसे समझा सकते हैं?"
    },
    {
      "speaker": "B",
      "line": "ज़रूर! चलिए बुनियादी बातों से शुरू करते हैं। Machine Learning कंप्यूटर विज्ञान का एक क्षेत्र है जहां सिस्टम डेटा से सीखते हैं और बिना स्पष्ट रूप से प्रोग्राम किए अपने प्रदर्शन में सुधार करते हैं। इसे ऐसे समझें कि कंप्यूटर को पैटर्न पहचानना सिखाया जा रहा है।"
    }
]
```

कोड:

```python
import os
import json
import random
import subprocess
from google.cloud import texttospeech
import tempfile
import time
import argparse

# बातचीत के लिए निश्चित आउटपुट डायरेक्टरी
OUTPUT_DIRECTORY = "assets/conversations"
INPUT_DIRECTORY = "scripts/conversation"

def text_to_speech(text, output_filename, voice_name=None):
    print(f"ऑडियो जेनरेट कर रहे हैं: {output_filename}")
    try:
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)
        if not voice_name:
            voice_name = random.choice(["en-US-Journey-D", "en-US-Journey-F", "en-US-Journey-O"])
        voice = texttospeech.VoiceSelectionParams(language_code="en-US", name=voice_name)
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            effects_profile_id=["small-bluetooth-speaker-class-device"]
        )
        
        retries = 5
        for attempt in range(1, retries + 1):
            try:
                response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
                with open(output_filename, 'wb') as out:
                    out.write(response.audio_content)
                print(f"ऑडियो कंटेंट {output_filename} में लिखा गया")
                return True
            except Exception as e:
                print(f"प्रयास {attempt} पर त्रुटि: {e}")
                if attempt == retries:
                    print(f"{retries} प्रयासों के बाद ऑडियो जेनरेट करने में विफल।")
                    return False
                wait_time = 2 ** attempt
                print(f"{wait_time} सेकंड में पुनः प्रयास कर रहे हैं...")
                time.sleep(wait_time)
    except Exception as e:
        print(f"{output_filename} के लिए ऑडियो जेनरेट करते समय एक त्रुटि हुई: {e}")
        return False

def process_conversation(filename):
    filepath = os.path.join(INPUT_DIRECTORY, filename)
    output_filename = os.path.join(OUTPUT_DIRECTORY, os.path.splitext(filename)[0] + ".mp3")

    if os.path.exists(output_filename):
        print(f"ऑडियो फ़ाइल पहले से मौजूद है: {output_filename}")
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            conversation = json.load(f)
    except Exception as e:
        print(f"बातचीत फ़ाइल {filename} लोड करने में त्रुटि: {e}")
        return

    temp_files = []
    
    voice_name_A = random.choice(["en-US-Wavenet-D", "en-US-Wavenet-E", "en-US-Wavenet-F"])
    voice_name_B = random.choice(["en-US-Studio-O", "en-US-Studio-M", "en-US-Studio-Q"])

    for idx, line_data in enumerate(conversation):
        speaker = line_data.get("speaker")
        line = line_data.get("line")
        if not line:
            continue
        temp_file = os.path.join(OUTPUT_DIRECTORY, f"temp_{idx}.mp3")
        temp_files.append(temp_file)
        
        voice_name = None
        if speaker == "A":
            voice_name = voice_name_A
        elif speaker == "B":
            voice_name = voice_name_B
        
        if not text_to_speech(line, temp_file, voice_name=voice_name):
            print(f"{filename} की लाइन {idx+1} के लिए ऑडियो जेनरेट करने में विफल")
            # अस्थायी फ़ाइलों को साफ़ करें
            for temp_file_to_remove in temp_files:
                if os.path.exists(temp_file_to_remove):
                    os.remove(temp_file_to_remove)
            return

    if not temp_files:
        print(f"{filename} के लिए कोई ऑडियो जेनरेट नहीं हुआ")
        return

    # ffmpeg का उपयोग करके ऑडियो को जोड़ें
    concat_file = os.path.join(OUTPUT_DIRECTORY, "concat.txt")
    with open(concat_file, 'w') as f:
        for temp_file in temp_files:
            f.write(f"file '{os.path.abspath(temp_file)}'\n")
    
    try:
        subprocess.run(
            ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', concat_file, '-c', 'copy', output_filename],
            check=True,
            capture_output=True
        )
        print(f"ऑडियो को सफलतापूर्वक {output_filename} में जोड़ा गया")
    except subprocess.CalledProcessError as e:
        print(f"ऑडियो जोड़ने में त्रुटि: {e.stderr.decode()}")
    finally:
        os.remove(concat_file)
        for temp_file in temp_files:
            os.remove(temp_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="बातचीत JSON फ़ाइलों को ऑडियो जेनरेट करने के लिए प्रोसेस करें।")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    for filename in os.listdir(INPUT_DIRECTORY):
        if filename.endswith(".json"):
            process_conversation(filename)
```