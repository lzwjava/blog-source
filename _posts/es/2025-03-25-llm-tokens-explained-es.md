---
audio: false
generated: true
image: false
lang: es
layout: post
title: Tokens de LLM Explicados de Forma Sencilla
translated: true
type: note
---

Excelente pregunta — los tokens en las APIs de LLM pueden ser un poco confusos al principio. Permíteme explicarlo claramente.

---

## Qué son los tokens

* Un **token** es la unidad más pequeña de texto que procesa el modelo.
* **No es exactamente una palabra**. Los tokens suelen ser partes de palabras, palabras completas, signos de puntuación o incluso espacios, dependiendo del idioma y del tokenizador.
* Los LLM (como los modelos GPT de OpenAI) dividen el texto en tokens usando un **tokenizador** predefinido.

Por ejemplo:

* `"gato"` → 1 token
* `"gatos"` → podría dividirse como `"gat"` + `"os"` → 2 tokens
* `"Eres guapo."` → se dividiría en algo como `"Er"`, `"es"`, `" guapo"`, `"."` → **4 tokens**

Así que los tokens son **unidades sub-léxicas**, optimizadas para que el modelo pueda manejar muchos idiomas y palabras raras de manera eficiente.

---

## Por qué importan los tokens en las APIs

1. **Facturación** – La mayoría de las APIs de LLM cobran por tokens (entrada + salida).
2. **Límites** – Los modelos tienen límites máximos de tokens (por ejemplo, GPT-4 Turbo 128k significa hasta 128,000 tokens en total para entrada + salida).
3. **Eficiencia** – Quieres minimizar los tokens al enviar prompts para reducir costos y mantenerte dentro de los límites.

---

## Cómo manejar los tokens en la práctica

* **Estimar tokens**: Una regla aproximada es \~4 caracteres por token en inglés. Así, un ensayo en inglés de 1,000 palabras (≈5,000 caracteres) son \~1,200–1,300 tokens.
* **Verificar tokens con precisión**: La mayoría de los SDKs (como `tiktoken` en Python para OpenAI) te permiten contar tokens antes de enviar.
* **Optimizar prompts**:

  * Eliminar espacios en blanco/palabras innecesarias.
  * Usar instrucciones concisas.
  * Resumir el contexto en lugar de volcar texto sin procesar.

---

## Ejemplo

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
text = "Eres guapo."
tokens = enc.encode(text)
print(tokens)        # lista de IDs de tokens
print(len(tokens))   # número de tokens
```

Esto daría como resultado algo como `[9125, 3938, 13]` → 3 tokens (dependiendo de la versión exacta del tokenizador).

---

✅ Entonces: **tokens ≠ palabras**. Son los bloques de construcción que ve el LLM. `"Eres guapo."` son aproximadamente 3–4 tokens, no 2 palabras.

---

¿Quieres que te muestre **cómo contar tokens con tu propio texto (por ejemplo, transcripciones, ensayos, código)** para que puedas ver el costo/límites antes de llamar a la API?