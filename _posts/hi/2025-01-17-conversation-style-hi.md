---
audio: false
generated: false
lang: hi
layout: post
title: संवाद ऑडियो जनरेशन
translated: true
---

DeepSeek-V3 के बारे में एक YouTube वीडियो से प्रेरित होकर, मैं AI-जनित वार्तालापों के साथ प्रयोग कर रहा हूँ। मेरा लक्ष्य Google Text-to-Speech और ffmpeg का उपयोग करके यथार्थवादी ऑडियो संवाद बनाना है। निम्नलिखित कोड मेरे वर्तमान दृष्टिकोण को दर्शाता है जो एक प्राकृतिक आगे-पीछे वार्तालाप का अनुकरण करता है।

## प्रॉम्प्ट

> दो विशेषज्ञों, A और B, के बीच एक प्राकृतिक और विस्तृत वार्तालाप बनाएं, जिसमें कम से कम 100 बारी हों। विशेषज्ञों को किसी विशिष्ट विषय पर गहराई से चर्चा करनी चाहिए, जिसमें वार्तालाप आगे-पीछे बहता रहे। दोनों प्रतिभागियों को प्रश्न पूछने, अंतर्दृष्टि साझा करने और विषय की बारीकियों का पता लगाना चाहिए। प्रारूप निम्नलिखित होना चाहिए:

```json
[
    {
      "speaker": "A",
      "line": "हे, मैंने हाल ही में Machine Learning (ML), Deep Learning (DL), और GPT के बारे में बहुत कुछ सुना है। क्या आप मुझे इसे समझा सकते हैं?"
    },
    {
      "speaker": "B",
      "line": "ज़रूर! चलिए मूल बातों से शुरू करते हैं। Machine Learning कंप्यूटर विज्ञान का एक क्षेत्र है जहां सिस्टम डेटा से सीखकर अपने प्रदर्शन को सुधारते हैं बिना स्पष्ट रूप से प्रोग्राम किए गए। इसे एक कंप्यूटर को पैटर्न पहचानने के लिए सिखाने के रूप में सोचें।"
    }
]
```

## कोड

```python
import os
import json
import random
import subprocess
from google.cloud import texttospeech
import tempfile
import time
import argparse

# वार्तालापों के लिए निश्चित आउटपुट डायरेक्टरी
OUTPUT_DIRECTORY = "assets/conversations"
INPUT_DIRECTORY = "scripts/conversation"

def text_to_speech(text, output_filename, voice_name=None):
    print(f"ऑडियो जनरेट कर रहा हूँ: {output_filename}")
    try:
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)
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
                print(f"ऑडियो सामग्री {output_filename} में लिखी गई")
                return True
            except Exception as e:
                print(f"प्रयास {attempt} पर त्रुटि: {e}")
                if attempt == retries:
                    print(f"{retries} प्रयासों के बाद ऑडियो जनरेट करने में विफल।")
                    return False
                wait_time = 2 ** attempt
                print(f"{wait_time} सेकंड में पुनः प्रयास कर रहा हूँ...")
                time.sleep(wait_time)
    except Exception as e:
        print(f"{output_filename} के लिए ऑडियो जनरेट करते समय एक त्रुटि हुई: {e}")
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
        print(f"वार्तालाप फ़ाइल {filename} लोड करने में त्रुटि: {e}")
        return

    temp_files = []
    
    voice_options = ["en-US-Journey-D", "en-US-Journey-F", "en-US-Journey-O"]
    voice_name_A = random.choice(voice_options)
    voice_name_B = random.choice(voice_options)
    while voice_name_A == voice_name_B:
        voice_name_B = random.choice(voice_options)

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
            print(f"{filename} की लाइन {idx+1} के लिए ऑडियो जनरेट करने में विफल")
            # अस्थायी फ़ाइलों को साफ़ करें
            for temp_file_to_remove in temp_files:
                if os.path.exists(temp_file_to_remove):
                    os.remove(temp_file_to_remove)
            return

    if not temp_files:
        print(f"{filename} के लिए कोई ऑडियो जनरेट नहीं हुआ")
        return

    # ffmpeg का उपयोग करके संयोजन
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
        print(f"ऑडियो को सफलतापूर्वक संयोजित करके {output_filename} में सहेजा गया")
    except subprocess.CalledProcessError as e:
        print(f"ऑडियो संयोजित करने में त्रुटि: {e.stderr.decode()}")
    finally:
        os.remove(concat_file)
        for temp_file in temp_files:
            os.remove(temp_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ऑडियो जनरेट करने के लिए वार्तालाप JSON फ़ाइलों को प्रोसेस करें।")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    for filename in os.listdir(INPUT_DIRECTORY):
        if filename.endswith(".json"):
            process_conversation(filename)
```

## कवर

```bash
ffmpeg -i deepseek.jpg -vf "crop=854:480" deepseek_480p_cropped.jpg
```

## वीडियो

```bash
ffmpeg -loop 1 -i deepseek.jpg -i deepseek.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -shortest output_video.mp4
```