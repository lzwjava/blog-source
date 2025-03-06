---
audio: false
generated: false
lang: hant
layout: post
title: 智能人工服務
translated: true
---

這個 Python 腳本使用 API 鑰匙和命令行參數與 Jina AI 服務進行互動。它支持兩個主要任務：從 URL 获取內容和執行搜索查詢。腳本從環境變量中獲取 Jina API 鑰匙，確保安全訪問服務。它使用 `requests` 庫進行 HTTP 请求，並使用 `base64` 解碼搜索查詢。然後，腳本打印來自 Jina AI 服務的回應。

```python
import os
import requests
from dotenv import load_dotenv
import argparse
import base64

load_dotenv()

api_key = os.environ.get("JINA_API_KEY")
if not api_key:
    raise ValueError("JINA_API_KEY 環境變量未設置。")

parser = argparse.ArgumentParser()
parser.add_argument("--job", type=str, choices=['url', 'search'], help="要執行的任務 (url 或 search)", required=True)
parser.add_argument("--input", type=str, help="任務的輸入", required=True)
args = parser.parse_args()

if args.job == 'url':
    url = f'https://r.jina.ai/{args.input}'
    headers = {'Authorization': f'Bearer {api_key}'}
    print(f"URL: {url}")
    print(f"Headers: {headers}")
    response = requests.get(url, headers=headers)
    print(response.text)

elif args.job == 'search':
    question = base64.b64decode(args.input).decode('utf-8', errors='ignore')
    url = f'https://s.jina.ai/{question}'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'X-Engine': 'direct',
        'X-Retain-Images': 'none'
    }
    print(f"URL: {url}")
    print(f"Headers: {headers}")
    response = requests.get(url, headers=headers)
    print(response.text)

else:
    print("請指定 --job url 或 --job search")
```