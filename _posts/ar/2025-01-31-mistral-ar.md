---
audio: true
generated: false
image: false
lang: ar
layout: post
title: إختبار API مستريل
translated: true
---

هذا المنشور هو اختبار سريع لAPI Mistral. أنا أستخدم نموذج `mistral-small-2501` لهذا الاختبار. الكود أدناه يوضح كيفية استدعاء API وحصول على إجابة.

```python
import os
import requests
from dotenv import load_dotenv
import argparse

load_dotenv()

def call_mistral_api(prompt, model="mistral-small-2501"):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("خطأ: لم يتم تعيين المتغير البيئي MISTRAL_API_KEY.")
        return None

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(response_json)
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            return content
        else:
            print(f"خطأ في API Mistral: صيغة الإجابة غير صحيحة: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"خطأ في API Mistral: {e}")
        if e.response:
            print(f"رمز حالة الإجابة: {e.response.status_code}")
            print(f"محتوى الإجابة: {e.response.text}")
        return None

def call_codestral_api(prompt, model="codestral-latest"):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("خطأ: لم يتم تعيين المتغير البيئي MISTRAL_API_KEY.")
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
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(response_json)
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            return content
        else:
            print(f"خطأ في API Codestral: صيغة الإجابة غير صحيحة: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"خطأ في API Codestral: {e}")
        if e.response:
            print(f"رمز حالة الإجابة: {e.response.status_code}")
            print(f"محتوى الإجابة: {e.response.text}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="اختبار APIs Mistral و Codestral.")
    parser.add_argument("--type", type=str, default="mistral", choices=["mistral", "codestral"], help="نوع API لاستدعائه (mistral أو codestral)")
    args = parser.parse_args()

    if args.type == "mistral":
        prompt = "ما هو نقطة القطع لديك من المعرفة"
        response = call_mistral_api(prompt)
        if response:
            print(f"الإجابة: {response}")
    elif args.type == "codestral":
        prompt = "def f("
        response = call_codestral_api(prompt, model="codestral-latest")
        if response:
            print(f"الإجابة: {response}")
```