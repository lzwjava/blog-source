---
audio: false
generated: true
image: false
lang: es
layout: post
title: Capacidades de Ventana de Contexto en Modelos de IA
translated: true
type: note
---

Aquí están las **capacidades máximas actuales de tokens (tamaños de ventana de contexto)** para los modelos que has listado, basado en documentación y anuncios recientes:

---

### Modelos de Anthropic

* **Claude Opus 4 / Opus 4.1**
  Ofrece una ventana de contexto de **200,000 tokens**, ideal para razonamiento sostenido y flujos de trabajo complejos ([Anthropic][1], [Amazon Web Services, Inc.][2]).

* **Claude Sonnet 4**
  También soporta **200,000 tokens** de contexto de forma nativa ([Prompthub][3]).
  Adicionalmente, una **actualización beta** ahora habilita un **masivo 1 millón de tokens** de contexto para usuarios empresariales/de API ([Anthropic][4]).

---

### Modelos de Mistral AI

* **Mistral Medium 3.1**
  Tiene una ventana de contexto de **128,000 tokens** ([OpenRouter][5]).

* **Mistral Large 2**
  También soporta una longitud de contexto de **128,000 tokens** ([Wikipedia][6]).

* **Mistral Medium (versiones anteriores)**
  Anteriormente, el estándar era **32,000 tokens** para el contexto ([Clarifai][7], [Mistral AI][8]).

* **Mistral Small 3.1**
  Actualizó su ventana de contexto **de 32K a 128K tokens** en esta versión más nueva ([Wikipedia][6]).

---

### Notas Adicionales

* Una descripción general de Wikipedia confirma que **Claude 3 Opus** tenía una ventana de contexto de **200K tokens**, con expansiones a **1 millón de tokens** en ciertos casos ([Wikipedia][9]).

* **El mecanismo de atención de ventana deslizante de Mistral** teóricamente soporta hasta **4096 × 32 = 131,072 tokens**, lo que se alinea estrechamente con las cifras de 128K reportadas ([Hugging Face][10]).

---

### Resumen (Formato Conciso)

* **Claude Opus 4 / 4.1**: 200,000 tokens
* **Claude Sonnet 4**: 200,000 tokens (estándar), hasta **1 millón de tokens** (beta/empresa)
* **Mistral Medium 3.1**: 128,000 tokens
* **Mistral Large 2**: 128,000 tokens
* **Mistral Small 3.1**: 128,000 tokens (actualizado desde 32K)

---

¡Házme saber si deseas más detalles sobre otros modelos o capacidades específicas de arquitectura!

* [The Verge](https://www.theverge.com/ai-artificial-intelligence/757998/anthropic-just-made-its-latest-move-in-the-ai-coding-wars?utm_source=chatgpt.com)
* [Tom's Guide](https://www.tomsguide.com/ai/anthropic-looks-to-beat-gpt-5-and-grok-4-with-this-one-major-upgrade?utm_source=chatgpt.com)

[1]: https://www.anthropic.com/claude/opus?utm_source=chatgpt.com "Claude Opus 4.1"
[2]: https://aws.amazon.com/bedrock/anthropic/?utm_source=chatgpt.com "Anthropic's Claude in Amazon Bedrock"
[3]: https://www.prompthub.us/blog/the-complete-guide-to-claude-opus-4-and-claude-sonnet-4?utm_source=chatgpt.com "The Complete Guide to Claude Opus 4 and Claude Sonnet 4"
[4]: https://www.anthropic.com/news/1m-context?utm_source=chatgpt.com "Claude Sonnet 4 now supports 1M tokens of context"
[5]: https://openrouter.ai/mistralai/mistral-medium-3.1?utm_source=chatgpt.com "Mistral Medium 3.1 - API, Providers, Stats"
[6]: https://en.wikipedia.org/wiki/Mistral_AI?utm_source=chatgpt.com "Mistral AI"
[7]: https://clarifai.com/mistralai/completion/models/mistral-medium?utm_source=chatgpt.com "mistral-medium model | Clarifai - The World's AI"
[8]: https://mistral.ai/news/mistral-large?utm_source=chatgpt.com "Au Large"
[9]: https://en.wikipedia.org/wiki/Claude_%28language_model%29?utm_source=chatgpt.com "Claude (language model)"
[10]: https://huggingface.co/docs/transformers/en/model_doc/mistral?utm_source=chatgpt.com "Mistral"