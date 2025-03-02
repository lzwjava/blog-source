---
audio: false
generated: true
lang: ja
layout: post
title: Mistral関数呼び出し
translated: true
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
        print("エラー: MISTRAL_API_KEY環境変数が設定されていません。")
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
                        "description": "指定された場所の現在の天気を取得",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {
                                    "type": "string",
                                    "description": "都市と州、例：サンフランシスコ、CA",
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

    print(f"Mistral API URL: {url}")
    print(f"Mistral API Headers: {headers}")
    print(f"Mistral API Data: {data}")
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
                print(f"ツール呼び出し: {tool_calls}")
                return tool_calls # 処理のためにツール呼び出しを返す
            else:
                print(f"Mistral API エラー: 無効な応答形式: {response_json}")
                return None
        else:
            print(f"Mistral API エラー: 無効な応答形式: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API エラー: {e}")
        if e.response:
            print(f"応答ステータスコード: {e.response.status_code}")
            print(f"応答コンテンツ: {e.response.text}")
        return None

def call_codestral_api(prompt, model="codestral-latest"):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("エラー: MISTRAL_API_KEY環境変数が設定されていません。")
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
    print(f"Codestral API URL: {url}")
    print(f"Codestral API Headers: {headers}")
    print(f"Codestral API Data: {json.dumps(data)}")
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(response_json)
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            return content
        else:
            print(f"Codestral API エラー: 無効な応答形式: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Codestral API エラー: {e}")
        if e.response:
            print(f"応答ステータスコード: {e.response.status_code}")
            print(f"応答コンテンツ: {e.response.text}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MistralとCodestralのAPIをテストします。")
    parser.add_argument("--type", type=str, default="mistral", choices=["mistral", "codestral"], help="呼び出すAPIの種類（mistralまたはcodestral）")
    parser.add_argument("--function_calling", action="store_true", help="Mistral APIの関数呼び出しを有効にする")
    args = parser.parse_args()

    if args.type == "mistral":
        prompt = "ロンドンの天気はどうですか？"
        response = call_mistral_api(prompt, use_function_calling=args.function_calling)
        if response:
            print(f"応答: {response}")
    elif args.type == "codestral":
        prompt = "def f("
        response = call_codestral_api(prompt, model="codestral-latest")
        if response:
            print(f"応答: {response}")
```