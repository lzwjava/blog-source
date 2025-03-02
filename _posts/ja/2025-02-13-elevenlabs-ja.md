---
audio: false
generated: false
lang: ja
layout: post
title: ElevenLabs AI
translated: true
---

* 素晴らしい。サービスをテストするために$5 USDを使用しました。

* ボイスクローニングは素晴らしいです。

* 音声サンプルは以下の通りです：

* [英語](assets/audios/ElevenLabs.mp3)

* [日本語](assets/audios/ElevenLabs_1.mp3)

* [スペイン語](assets/audios/ElevenLabs_2.mp3)

```python
import os
import requests
from dotenv import load_dotenv
import argparse
import re

load_dotenv()

api_key = os.environ.get("ELEVENLABS_API_KEY")
if not api_key:
    raise ValueError("ELEVENLABS_API_KEY環境変数が設定されていません。")

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, help="音声に変換するMarkdownファイル", required=False)
parser.add_argument("--text", type=str, help="音声に変換するテキスト", required=False)
parser.add_argument("--output", type=str, help="出力ファイル名", required=True)
parser.add_argument("--voice_id", type=str, default="21m00Tcm4TlvDq8iK2G8", help="使用するボイスID")

args = parser.parse_args()

if args.file:
    try:
        with open(args.file, 'r') as f:
            content = f.read()
            # フロントマターを削除
            content = re.sub(r'---.*?---', '', content, flags=re.DOTALL)
            text = content.strip()
    except FileNotFoundError:
        print(f"エラー: ファイルが見つかりません: {args.file}")
        exit(1)
    except Exception as e:
        print(f"ファイルの読み込みエラー: {e}")
        exit(1)
elif args.text:
    text = args.text
else:
    print("エラー: --fileまたは--textを指定してください。")
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
    print(f"音声は{args.output}に保存されました")
else:
    print(f"エラー: {response.status_code} - {response.text}")
```