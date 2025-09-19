---
audio: true
generated: false
image: false
lang: hi
layout: post
title: Grook API Test करना
translated: true
---

- चीन जारी वीसा कार्ड का उपयोग करना ठीक है।

- [https://console.x.ai](https://console.x.ai)

- `grok-2-latest` मॉडल: प्रती 2 मिलियन टोकन के लिए 2 डॉलर इन्पुट, प्रती 10 मिलियन टोकन के लिए 10 डॉलर आउटपुट।

कोड:

```python
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.environ.get("GROK_API_KEY")
if not GROK_API_KEY:
    raise ValueError("GROK_API_KEY पर्यावरण विकल्प नहीं सेट है")

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
            "content": "Explain how AI works"
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
            print("अनपेक्षित उत्तर फ़ॉर्मेट: सन्देश या सामग्री अभाव में")
    else:
        print("उत्तर में कोई विकल्प नहीं मिला")
except requests.exceptions.RequestException as e:
    print(f"एपीआई अनुरोध के दौरान एक त्रुटि: {e}")
    if e.response:
        print(f"उत्तर स्थिति कोड: {e.response.status_code}")
        print(f"उत्तर सामग्री: {e.response.text}")
except json.JSONDecodeError as e:
    print(f"जेएसओएन उत्तर को डिकोड करने में त्रुटि: {e}")
```