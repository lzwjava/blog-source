---
audio: true
lang: hant
layout: post
title: 對話音頻生成
translated: true
---

我一直在探索AI生成對話的能力，特別是在觀看了一段展示DeepSeek-V3討論的YouTube視頻後。這讓我開始思考如何創建類似的音頻對話。我開發了一個使用Google Text-to-Speech和ffmpeg來生成和拼接音頻片段，模擬自然來回對話的過程。以下是我正在開發的代碼。

## 提示

```
創建一個自然且深入的對話，兩位專家A和B之間至少進行100輪對話。專家們應該深入討論一個特定主題，對話應來回流暢。兩位參與者應提出問題、分享見解並探討主題的細微差別。格式如下：

[
    {
      "speaker": "A",
      "line": "嘿，我最近聽到很多關於機器學習（ML）、深度學習（DL）和GPT的討論。你能為我解釋一下嗎？"
    },
    {
      "speaker": "B",
      "line": "當然！我們從基礎開始。機器學習是計算機科學的一個領域，系統通過數據學習以提高性能，而無需明確編程。你可以把它看作是教計算機識別模式。"
    }
]
```

## 代碼

```python
import os
import json
import random
import subprocess
from google.cloud import texttospeech
import tempfile
import time
import argparse

# 固定輸出對話的目錄
OUTPUT_DIRECTORY = "assets/conversations"
INPUT_DIRECTORY = "scripts/conversation"

def text_to_speech(text, output_filename, voice_name=None):
    print(f"生成音頻：{output_filename}")
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
                print(f"音頻內容已寫入 {output_filename}")
                return True
            except Exception as e:
                print(f"第{attempt}次嘗試出錯：{e}")
                if attempt == retries:
                    print(f"在{retries}次嘗試後仍未能生成音頻。")
                    return False
                wait_time = 2 ** attempt
                print(f"等待{wait_time}秒後重試...")
                time.sleep(wait_time)
    except Exception as e:
        print(f"生成音頻時出錯 {output_filename}: {e}")
        return False

def process_conversation(filename):
    filepath = os.path.join(INPUT_DIRECTORY, filename)
    output_filename = os.path.join(OUTPUT_DIRECTORY, os.path.splitext(filename)[0] + ".mp3")

    if os.path.exists(output_filename):
        print(f"音頻文件已存在：{output_filename}")
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            conversation = json.load(f)
    except Exception as e:
        print(f"加載對話文件 {filename} 時出錯：{e}")
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
            print(f"未能生成 {filename} 的第{idx+1}行音頻")
            # 清理臨時文件
            for temp_file_to_remove in temp_files:
                if os.path.exists(temp_file_to_remove):
                    os.remove(temp_file_to_remove)
            return

    if not temp_files:
        print(f"未生成 {filename} 的音頻")
        return

    # 使用ffmpeg拼接
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
        print(f"成功拼接音頻到 {output_filename}")
    except subprocess.CalledProcessError as e:
        print(f"拼接音頻時出錯：{e.stderr.decode()}")
    finally:
        os.remove(concat_file)
        for temp_file in temp_files:
            os.remove(temp_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="處理對話JSON文件以生成音頻。")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    for filename in os.listdir(INPUT_DIRECTORY):
        if filename.endswith(".json"):
            process_conversation(filename)
```

## 封面

```bash
ffmpeg -i deepseek.jpg -vf "crop=854:480" deepseek_480p_cropped.jpg
```

## 視頻

```bash
ffmpeg -loop 1 -i deepseek.jpg -i deepseek.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -shortest output_video.mp4
```