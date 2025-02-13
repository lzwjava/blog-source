---
audio: true
lang: hant
layout: post
title: 使用 Tavily AI 搜尋 API
translated: true
---

[Tavily](https://tavily.com) 是一個專為 LLM 應用程式設計的 AI 搜尋 API。它通過結合網絡搜尋和 AI 處理來提供高度相關的搜尋結果。

要使用 Tavily，您需要：

1. 在 [tavily.com](https://tavily.com) 註冊 API 密鑰
2. 安裝 Python 包。

```python
import os
from tavily import TavilyClient

# 從環境變量中檢索 API 密鑰
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

if TAVILY_API_KEY is None:
    raise ValueError("未找到 API 密鑰。請設置 TAVILY_API_KEY 環境變量。")

# 使用檢索到的 API 密鑰初始化 TavilyClient
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# 發出搜尋請求
response = tavily_client.search("Leo Messi 是誰？")

# 打印回應
print(response)
```