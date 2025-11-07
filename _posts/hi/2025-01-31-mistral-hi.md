---
audio: true
generated: false
image: false
lang: hi
layout: post
title: Mistral API ko Test Karna
translated: true
type: post
---

यह पोस्ट Mistral API के तेज़ टेस्ट का एक नमूना है। मैं इस टेस्ट के लिए `mistral-small-2501` मॉडल का उपयोग कर रहा हूँ। नीचे दी गई कोड दिखाती है कि API को कैसे कॉल किया जाए और जवाब प्राप्त किया जाए।

```python
import os
import requests
from dotenv import load_dotenv
import argparse

load_dotenv()

def call_mistral_api(prompt, model="mistral-small-2501"):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY पर्यावरण परिवर्तन नहीं सेट है।")
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
            print(f"Mistral API Error: अवैध प्रतिक्रिया स्वरूप: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API Error: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None

def call_codestral_api(prompt, model="codestral-latest"):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY पर्यावरण परिवर्तन नहीं सेट है।")
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
            print(f"Codestral API Error: अवैध प्रतिक्रिया स्वरूप: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Codestral API Error: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mistral और Codestral APIs का परीक्षण करें।")
    parser.add_argument("--type", type=str, default="mistral", choices=["mistral", "codestral"], help="को कॉल किया जाए API का प्रकार (mistral या codestral)")
    args = parser.parse_args()

    if args.type == "mistral":
        prompt = "what's your cutting point of knowledge"
        response = call_mistral_api(prompt)
        if response:
            print(f"Response: {response}")
    elif args.type == "codestral":
        prompt = "def f("
        response = call_codestral_api(prompt, model="codestral-latest")
        if response:
            print(f"Response: {response}")
```