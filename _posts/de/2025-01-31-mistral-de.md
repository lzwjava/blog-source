---
audio: true
generated: false
lang: de
layout: post
title: Testen der Mistral API
translated: true
---

Dieser Beitrag ist ein schneller Test der Mistral-API. Ich verwende das `mistral-small-2501`-Modell für diesen Test. Der untenstehende Code zeigt, wie man die API aufruft und eine Antwort erhält.

```python
import os
import requests
from dotenv import load_dotenv
import argparse

load_dotenv()

def call_mistral_api(prompt, model="mistral-small-2501"):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Fehler: Die Umgebungvariable MISTRAL_API_KEY ist nicht gesetzt.")
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
            print(f"Mistral API Fehler: Ungültiges Antwortformat: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API Fehler: {e}")
        if e.response:
            print(f"Response Statuscode: {e.response.status_code}")
            print(f"Response Inhalt: {e.response.text}")
        return None

def call_codestral_api(prompt, model="codestral-latest"):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Fehler: Die Umgebungvariable MISTRAL_API_KEY ist nicht gesetzt.")
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
            print(f"Codestral API Fehler: Ungültiges Antwortformat: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Codestral API Fehler: {e}")
        if e.response:
            print(f"Response Statuscode: {e.response.status_code}")
            print(f"Response Inhalt: {e.response.text}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mistral- und Codestral-APIs testen.")
    parser.add_argument("--type", type=str, default="mistral", choices=["mistral", "codestral"], help="Art der aufzurufenden API (mistral oder codestral)")
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