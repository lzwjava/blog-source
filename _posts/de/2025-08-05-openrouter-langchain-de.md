---
audio: false
generated: true
image: false
lang: de
layout: post
title: OpenRouter mit LangChain
translated: true
type: note
---

Sie können LangChain auf OpenRouter verweisen, indem Sie dessen Basis-URL und Ihren OpenRouter-Schlüssel bei der Instanziierung des LLM angeben. Zum Beispiel:

```python
import os
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. (Optional) Setzen Sie Ihren OpenRouter-Schlüssel in die Umgebungsvariablen
os.environ["OPENAI_API_KEY"] = "pk-OPENROUTER_YOUR_KEY_HERE"
# und die Basis-URL:
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

# 2. Initialisieren Sie das LLM für die Verwendung von OpenRouter
llm = OpenAI(
    model_name="gpt-4o",                # oder "gpt-3.5-turbo" etc.
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_type="open_router"       # teilt LangChain mit, dass es OpenRouter ist
)

# 3. Erstellen Sie Ihre Prompt-Vorlage
template = PromptTemplate(
    input_variables=["product"],
    template="Schreiben Sie einen kurzen Marketing-Text für das Produkt: {product}."
)

# 4. Bauen Sie die Chain und führen Sie sie aus
chain = LLMChain(llm=llm, prompt=template)
result = chain.run({"product": "kabellose Noise-Cancelling-Kopfhörer"})
print(result)
```

**Wichtige Punkte**

*   **`openai_api_base`** muss auf den OpenRouter-API-Endpunkt zeigen.
*   **`openai_api_type="open_router"`** teilt LangChain mit, das OpenRouter-Protokoll zu verwenden.
*   Geben Sie Ihren OpenRouter-Schlüssel über `openai_api_key` an (oder die `OPENAI_API_KEY` Umgebungsvariable).

Dadurch wird der standardmäßige OpenAI.com-Endpunkt durch OpenRouter ersetzt.