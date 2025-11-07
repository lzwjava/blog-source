---
audio: true
generated: false
image: false
lang: hant
layout: post
title: 測試 Grok API
translated: true
type: post
---

- 可以使用中國發出的Visa卡。

- [https://console.x.ai](https://console.x.ai)

- `grok-2-latest` 模型: 输入 2 USD 每百萬個標記，輸出 10 USD 每百萬個標記。

程式碼：

```python
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.environ.get("GROK_API_KEY")
if not GROK_API_KEY:
    raise ValueError("GROK_API_KEY 環境變量未設置")

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
            "content": "解釋AI如何運作"
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
            print("意外的回應格式: 訊息或內容遺失")
    else:
        print("在回應中未找到選擇")
except requests.exceptions.RequestException as e:
    print(f"API 要求期間出錯: {e}")
    if e.response:
        print(f"回應狀態碼: {e.response.status_code}")
        print(f"回應內容: {e.response.text}")
except json.JSONDecodeError as e:
    print(f"解碼 JSON 回應時出錯: {e}")
```