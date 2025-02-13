---
audio: false
lang: hant
layout: post
title: 十一實驗室人工智慧
translated: true
---

* 很好。我用了 5 美元來測試這項服務。

* 聲音克隆非常好。

* 下面是音頻樣本：

* [英文](assets/audios/ElevenLabs.mp3)

* [日文](assets/audios/ElevenLabs_1.mp3)

* [西班牙文](assets/audios/ElevenLabs_2.mp3)

```python
import os
import requests
from dotenv import load_dotenv
import argparse
import re

load_dotenv()

api_key = os.environ.get("ELEVENLABS_API_KEY")
if not api_key:
    raise ValueError("ELEVENLABS_API_KEY 環境變量未設置。")

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, help="要轉換為語音的 Markdown 文件", required=False)
parser.add_argument("--text", type=str, help="要轉換為語音的文本", required=False)
parser.add_argument("--output", type=str, help="輸出文件名", required=True)
parser.add_argument("--voice_id", type=str, default="21m00Tcm4TlvDq8iK2G8", help="要使用的聲音 ID")

args = parser.parse_args()

if args.file:
    try:
        with open(args.file, 'r') as f:
            content = f.read()
            # 移除前置信息
            content = re.sub(r'---.*?---', '', content, flags=re.DOTALL)
            text = content.strip()
    except FileNotFoundError:
        print(f"錯誤：文件未找到：{args.file}")
        exit(1)
    except Exception as e:
        print(f"讀取文件時出錯：{e}")
        exit(1)
elif args.text:
    text = args.text
else:
    print("錯誤：必須指定 --file 或 --text。")
    exit(1)

url = f"https://api.elevenlabs.io/v1/text-to-speech/{args.voice_id}"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": api_key
}

data = {
  "text": text,
  "model_id": "eleven_flash_v2_5",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    with open(args.output, 'wb') as f:
        f.write(response.content)
    print(f"音頻已保存到 {args.output}")
else:
    print(f"錯誤：{response.status_code} - {response.text}")
```