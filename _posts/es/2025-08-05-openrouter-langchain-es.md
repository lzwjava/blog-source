---
audio: false
generated: true
image: false
lang: es
layout: post
title: Usar OpenRouter con LangChain
translated: true
type: note
---

Puedes dirigir LangChain a OpenRouter especificando su URL base y tu clave de OpenRouter cuando instancies el LLM. Por ejemplo:

```python
import os
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. (Opcional) establece tu clave de OpenRouter en las variables de entorno
os.environ["OPENAI_API_KEY"] = "pk-OPENROUTER_YOUR_KEY_HERE"
# y la URL base:
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

# 2. Inicializa el LLM para usar OpenRouter
llm = OpenAI(
    model_name="gpt-4o",                # o "gpt-3.5-turbo", etc.
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_type="open_router"       # indica a LangChain que es OpenRouter
)

# 3. Crea tu plantilla de prompt
template = PromptTemplate(
    input_variables=["product"],
    template="Escribe una breve descripción de marketing para el producto: {product}."
)

# 4. Construye y ejecuta la cadena
chain = LLMChain(llm=llm, prompt=template)
result = chain.run({"product": "auriculares inalámbricos con cancelación de ruido"})
print(result)
```

**Puntos clave**

* **`openai_api_base`** debe apuntar al endpoint de la API de OpenRouter.
* **`openai_api_type="open_router"`** le indica a LangChain que utilice el protocolo de OpenRouter.
* Proporciona tu clave de OpenRouter mediante `openai_api_key` (o la variable de entorno `OPENAI_API_KEY`).

Esto reemplazará el endpoint predeterminado de OpenAI.com por OpenRouter.