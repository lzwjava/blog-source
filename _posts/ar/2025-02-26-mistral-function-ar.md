---
audio: false
generated: true
lang: ar
layout: post
title: استدعاء وظيفة ميسترال
translated: true
type: note
---

```python
import os
import requests
from dotenv import load_dotenv
import argparse
import json

load_dotenv()

def call_mistral_api(prompt, model="mistral-small-2501", use_function_calling=False):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("خطأ: متغير البيئة MISTRAL_API_KEY غير مضبوط.")
        return None
    
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    if use_function_calling:
        data = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "name": "get_current_weather",
                        "description": "احصل على الطقس الحالي في موقع معين",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {
                                    "type": "string",
                                    "description": "المدينة والولاية، مثال: San Francisco, CA",
                                },
                                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                            },
                            "required": ["location"],
                        },
                    }
                }
            ],
            "tool_choice": "auto",
        }
    else:
        data = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

    print(f"رابط Mistral API: {url}")
    print(f"رؤوس Mistral API: {headers}")
    print(f"بيانات Mistral API: {data}")
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(response_json)
        if response_json and response_json['choices']:
            choice = response_json['choices'][0]
            if 'message' in choice and 'content' in choice['message']:
                content = choice['message']['content']
                return content
            elif 'message' in choice and 'tool_calls' in choice['message']:
                tool_calls = choice['message']['tool_calls']
                print(f"استدعاءات الأدوات: {tool_calls}")
                return tool_calls # إرجاع استدعاءات الأدوات للمعالجة
            else:
                print(f"خطأ في Mistral API: تنسيق استجابة غير صالح: {response_json}")
                return None
        else:
            print(f"خطأ في Mistral API: تنسيق استجابة غير صالح: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"خطأ في Mistral API: {e}")
        if e.response:
            print(f"رمز حالة الاستجابة: {e.response.status_code}")
            print(f"محتوى الاستجابة: {e.response.text}")
        return None

def call_codestral_api(prompt, model="codestral-latest"):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("خطأ: متغير البيئة MISTRAL_API_KEY غير مضبوط.")
        return None
    
    url = "https://api.mistral.ai/v1/fim/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "prompt": prompt,
        "suffix": "return a + b",
        "max_tokens": 64,
        "temperature": 0
    }
    print(f"رابط Codestral API: {url}")
    print(f"رؤوس Codestral API: {headers}")
    print(f"بيانات Codestral API: {json.dumps(data)}")
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(response_json)
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            return content
        else:
            print(f"خطأ في Codestral API: تنسيق استجابة غير صالح: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"خطأ في Codestral API: {e}")
        if e.response:
            print(f"رمز حالة الاستجابة: {e.response.status_code}")
            print(f"محتوى الاستجابة: {e.response.text}")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="اختبر Mistral و Codestral APIs.")
    parser.add_argument("--type", type=str, default="mistral", choices=["mistral", "codestral"], help="نوع API للاتصال به (mistral أو codestral)")
    parser.add_argument("--function_calling", action="store_true", help="تفعيل استدعاء الدوال لـ Mistral API")
    args = parser.parse_args()

    if args.type == "mistral":
        prompt = "ما هو حال الطقس في لندن؟"
        response = call_mistral_api(prompt, use_function_calling=args.function_calling)
        if response:
            print(f"الاستجابة: {response}")
    elif args.type == "codestral":
        prompt = "def f("
        response = call_codestral_api(prompt, model="codestral-latest")
        if response:
            print(f"الاستجابة: {response}")
```