---
audio: true
generated: false
image: false
lang: ja
layout: post
title: Grokking APIのテスト
translated: true
type: post
---

- 中国発行のビザカードの使用は許可されています。

- [https://console.x.ai](https://console.x.ai)

- `grok-2-latest` モデル: 入力 2 米ドル / 100万トークン、出力 10 米ドル / 100万トークン。

コード:

```python
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.environ.get("GROK_API_KEY")
if not GROK_API_KEY:
    raise ValueError("GROK_API_KEY 環境変数が設定されていません")

url = "https://api.x.ai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {GROK_API_KEY}"
}
data = {
    "model": "grok-2-latest",
    "messages": [
        {
            "role": "user",
            "content": "AIがどのように動作するか説明してください"
        }
    ]
}

try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    json_response = response.json()
    if 'choices' in json_response and json_response['choices']:
        first_choice = json_response['choices'][0]
        if 'message' in first_choice and 'content' in first_choice['message']:
            print(first_choice['message']['content'])
        else:
            print("予期せぬ応答形式: メッセージまたはコンテンツが欠落")
    else:
        print("応答に選択肢が含まれていません")
except requests.exceptions.RequestException as e:
    print(f"APIリクエスト中にエラーが発生しました: {e}")
    if e.response:
        print(f"応答ステータスコード: {e.response.status_code}")
        print(f"応答コンテンツ: {e.response.text}")
except json.JSONDecodeError as e:
    print(f"JSON応答のデコード中にエラーが発生しました: {e}")
```