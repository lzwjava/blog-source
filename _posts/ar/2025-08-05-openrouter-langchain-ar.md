---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دمج OpenRouter مع LangChain
translated: true
type: note
---

يمكنك توجيه LangChain إلى OpenRouter عن طريق تحديد عنوان URL الأساسي ومفتاح OpenRouter عند إنشاء كائن LLM. على سبيل المثال:

```python
import os
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. (اختياري) ضبط مفتاح OpenRouter في البيئة
os.environ["OPENAI_API_KEY"] = "pk-OPENROUTER_YOUR_KEY_HERE"
# والعنوان الأساسي:
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

# 2. تهيئة LLM لاستخدام OpenRouter
llm = OpenAI(
    model_name="gpt-4o",                # أو "gpt-3.5-turbo" إلخ.
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_type="open_router"       # إخبار LangChain بأنه OpenRouter
)

# 3. إنشاء قالب النص التوجيهي
template = PromptTemplate(
    input_variables=["product"],
    template="Write a short marketing blurb for the product: {product}."
)

# 4. بناء وتشغيل السلسلة
chain = LLMChain(llm=llm, prompt=template)
result = chain.run({"product": "wireless noise-cancelling headphones"})
print(result)
```

**النقاط الرئيسية**

* **`openai_api_base`** يجب أن يشير إلى نقطة نهاية API الخاصة بـ OpenRouter.
* **`openai_api_type="open_router"`** يخبر LangChain باستخدام بروتوكول OpenRouter.
* قم بتوفير مفتاح OpenRouter عبر `openai_api_key` (أو متغير البيئة `OPENAI_API_KEY`).

هذا سيستبدل نقطة نهاية OpenAI.com الافتراضية بـ OpenRouter.