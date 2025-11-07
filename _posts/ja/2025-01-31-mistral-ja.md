---
audio: true
generated: false
image: false
lang: ja
layout: post
title: Mistral APIのテスト
translated: true
type: post
---

この投稿は、Mistral APIの簡単なテストです。このテストには、`mistral-small-2501`モデルを使用しています。以下のコードには、APIを呼び出し、応答を取得する方法が示されています。

```python
import os
import requests
from dotenv import load_dotenv
import argparse

load_dotenv()

def call_mistral_api(prompt, model="mistral-small-2501"):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY環境変数が設定されていません。")
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
            print(f"Mistral API Error: 無効な応答形式: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API Error: {e}")
        if e.response:
            print(f"応答ステータスコード: {e.response.status_code}")
            print(f"応答内容: {e.response.text}")
        return None

def call_codestral_api(prompt, model="codestral-latest"):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY環境変数が設定されていません。")
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
            print(f"Codestral API Error: 無効な応答形式: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Codestral API Error: {e}")
        if e.response:
            print(f"応答ステータスコード: {e.response.status_code}")
            print(f"応答内容: {e.response.text}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MistralとCodestralのAPIをテストします。")
    parser.add_argument("--type", type=str, default="mistral", choices=["mistral", "codestral"], help="呼び出すAPIの種類（mistralまたはcodestral）")
    args = parser.parse_args()

    if args.type == "mistral":
        prompt = "what's your cutting point of knowledge"
        response = call_mistral_api(prompt)
        if response:
            print(f"応答: {response}")
    elif args.type == "codestral":
        prompt = "def f("
        response = call_codestral_api(prompt, model="codestral-latest")
        if response:
            print(f"応答: {response}")
```