---
audio: false
generated: true
image: false
lang: hi
layout: post
title: लैंगचेन के साथ ओपनराउटर का उपयोग करें
translated: true
type: note
---

आप LangChain को OpenRouter की ओर इंगित कर सकते हैं, LLM को इन्स्टेंटिएट करते समय इसके बेस URL और अपनी OpenRouter key निर्दिष्ट करके। उदाहरण के लिए:

```python
import os
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. (वैकल्पिक) env में अपनी OpenRouter key सेट करें
os.environ["OPENAI_API_KEY"] = "pk-OPENROUTER_YOUR_KEY_HERE"
# और बेस URL:
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

# 2. OpenRouter का उपयोग करने के लिए LLM को इनिशियलाइज़ करें
llm = OpenAI(
    model_name="gpt-4o",                # या "gpt-3.5-turbo" आदि।
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_type="open_router"       # LangChain को बताएं कि यह OpenRouter है
)

# 3. अपना प्रॉम्प्ट टेम्पलेट बनाएं
template = PromptTemplate(
    input_variables=["product"],
    template="उत्पाद के लिए एक छोटा सा मार्केटिंग ब्लर्ब लिखें: {product}."
)

# 4. चेन बनाएं और रन करें
chain = LLMChain(llm=llm, prompt=template)
result = chain.run({"product": "wireless noise-cancelling headphones"})
print(result)
```

**मुख्य बिंदु**

* **`openai_api_base`** को OpenRouter के API एंडपॉइंट की ओर इशारा करना चाहिए।
* **`openai_api_type="open_router"`** LangChain को बताता है कि OpenRouter के प्रोटोकॉल का उपयोग करना है।
* अपनी OpenRouter key को `openai_api_key` (या `OPENAI_API_KEY` env) के माध्यम से सप्लाई करें।

यह डिफ़ॉल्ट OpenAI.com एंडपॉइंट को OpenRouter से बदल देगा।