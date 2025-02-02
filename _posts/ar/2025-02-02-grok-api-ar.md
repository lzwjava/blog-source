---
audio: false
lang: ar
layout: post
title: اختبار Grok API
translated: true
---

- من الممكن استخدام بطاقة فيزا صادر عنها الصين.

- [https://console.x.ai](https://console.x.ai)

- `grok-2-latest` نموذج: مدخل 2 دولار لكل مليون علامات, خروج 10 دولار لكل مليون علامات.

الرمز:

```python
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.environ.get("GROK_API_KEY")
if not GROK_API_KEY:
    raise ValueError("GROK_API_KEY متغير بيئة غير محدد")

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
            "content": "شرح كيفية عمل الذكاء الاصطناعي"
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
            print("تنسيق الرد غير متوقع: رسالة أو محتوى مفقود")
    else:
        print("لم يتم العثور على خيارات في الرد")
except requests.exceptions.RequestException as e:
    print(f"خطأ أثناء طلب API: {e}")
    if e.response:
        print(f"رمز حالة الرد: {e.response.status_code}")
        print(f"محتوى الرد: {e.response.text}")
except json.JSONDecodeError as e:
    print(f"خطأ في تشفير الرد JSON: {e}")
```