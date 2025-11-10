---
audio: false
generated: true
image: false
lang: ja
layout: post
title: OpenRouterとLangChainの活用
translated: true
type: note
---

LangChainをOpenRouterに向けるには、LLMをインスタンス化する際にそのベースURLとOpenRouterキーを指定します。例:

```python
import os
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. (オプション) 環境変数にOpenRouterキーを設定
os.environ["OPENAI_API_KEY"] = "pk-OPENROUTER_YOUR_KEY_HERE"
# ベースURLも設定:
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

# 2. OpenRouterを使用するLLMを初期化
llm = OpenAI(
    model_name="gpt-4o",                # または "gpt-3.5-turbo" など
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_type="open_router"       # LangChainにOpenRouterであることを伝える
)

# 3. プロンプトテンプレートを作成
template = PromptTemplate(
    input_variables=["product"],
    template="製品の短いマーケティング紹介文を書いてください: {product}."
)

# 4. チェーンを構築して実行
chain = LLMChain(llm=llm, prompt=template)
result = chain.run({"product": "wireless noise-cancelling headphones"})
print(result)
```

**重要なポイント**

* **`openai_api_base`** はOpenRouterのAPIエンドポイントを指している必要があります
* **`openai_api_type="open_router"`** はLangChainにOpenRouterのプロトコルを使用するように伝えます
* OpenRouterキーは `openai_api_key`（または `OPENAI_API_KEY` 環境変数）で指定します

これにより、デフォルトのOpenAI.comエンドポイントがOpenRouterに置き換えられます。