---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 使用 LangChain 與 OpenRouter
translated: true
type: note
---

你可以透過在實例化 LLM 時指定其基礎 URL 和你的 OpenRouter 金鑰，將 LangChain 指向 OpenRouter。例如：

```python
import os
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. （可選）在環境變數中設定你的 OpenRouter 金鑰
os.environ["OPENAI_API_KEY"] = "pk-OPENROUTER_YOUR_KEY_HERE"
# 以及基礎 URL：
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

# 2. 初始化使用 OpenRouter 的 LLM
llm = OpenAI(
    model_name="gpt-4o",                # 或 "gpt-3.5-turbo" 等
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_type="open_router"       # 告知 LangChain 這是 OpenRouter
)

# 3. 建立你的提示模板
template = PromptTemplate(
    input_variables=["product"],
    template="為以下產品撰寫簡短的市場推廣文案：{product}。"
)

# 4. 建立並執行鏈
chain = LLMChain(llm=llm, prompt=template)
result = chain.run({"product": "無線降噪耳機"})
print(result)
```

**關鍵要點**

* **`openai_api_base`** 必須指向 OpenRouter 的 API 端點。
* **`openai_api_type="open_router"`** 告知 LangChain 使用 OpenRouter 的通訊協定。
* 透過 `openai_api_key`（或 `OPENAI_API_KEY` 環境變數）提供你的 OpenRouter 金鑰。

這將用 OpenRouter 取代預設的 OpenAI.com 端點。