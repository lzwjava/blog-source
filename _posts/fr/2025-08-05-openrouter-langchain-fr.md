---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Utiliser OpenRouter avec LangChain
translated: true
type: note
---

Vous pouvez diriger LangChain vers OpenRouter en spécifiant son URL de base et votre clé OpenRouter lors de l'instanciation du LLM. Par exemple :

```python
import os
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. (Optionnellement) définissez votre clé OpenRouter dans les variables d'environnement
os.environ["OPENAI_API_KEY"] = "pk-OPENROUTER_YOUR_KEY_HERE"
# et l'URL de base :
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

# 2. Initialisez le LLM pour utiliser OpenRouter
llm = OpenAI(
    model_name="gpt-4o",                # ou "gpt-3.5-turbo" etc.
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_type="open_router"       # indique à LangChain qu'il s'agit d'OpenRouter
)

# 3. Créez votre modèle de prompt
template = PromptTemplate(
    input_variables=["product"],
    template="Write a short marketing blurb for the product: {product}."
)

# 4. Construisez et exécutez la chaîne
chain = LLMChain(llm=llm, prompt=template)
result = chain.run({"product": "wireless noise-cancelling headphones"})
print(result)
```

**Points clés**

* **`openai_api_base`** doit pointer vers le point de terminaison de l'API d'OpenRouter.
* **`openai_api_type="open_router"`** indique à LangChain d'utiliser le protocole d'OpenRouter.
* Fournissez votre clé OpenRouter via `openai_api_key` (ou la variable d'environnement `OPENAI_API_KEY`).

Cela remplacera le point de terminaison par défaut d'OpenAI.com par celui d'OpenRouter.