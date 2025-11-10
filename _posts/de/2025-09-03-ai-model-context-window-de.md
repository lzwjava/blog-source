---
audio: false
generated: true
image: false
lang: de
layout: post
title: Kontextfensterkapazitäten von KI-Modellen
translated: true
type: note
---

Hier sind die **aktuellen maximalen Token-Kapazitäten (Kontextfenstergrößen)** für die von Ihnen aufgeführten Modelle, basierend auf aktueller Dokumentation und Ankündigungen:

---

### Anthropic-Modelle

* **Claude Opus 4 / Opus 4.1**
  Bietet ein Kontextfenster von **200.000 Token**, ideal für anhaltendes Reasoning und komplexe Workflows ([Anthropic][1], [Amazon Web Services, Inc.][2]).

* **Claude Sonnet 4**
  Unterstützt ebenfalls nativ **200.000 Token** an Kontext ([Prompthub][3]).
  Zusätzlich ermöglicht ein **Beta-Upgrade** nun ein **massives Kontextfenster von 1 Million Token** für Enterprise-/API-Nutzer ([Anthropic][4]).

---

### Mistral AI-Modelle

* **Mistral Medium 3.1**
  Verfügt über ein Kontextfenster von **128.000 Token** ([OpenRouter][5]).

* **Mistral Large 2**
  Unterstützt ebenfalls eine **Kontextlänge von 128.000 Token** ([Wikipedia][6]).

* **Mistral Medium (frühere Versionen)**
  Zuvor lag der Standard für den Kontext bei **32.000 Token** ([Clarifai][7], [Mistral AI][8]).

* **Mistral Small 3.1**
  Hat sein Kontextfenster in dieser neueren Version **von 32K auf 128K Token** erweitert ([Wikipedia][6]).

---

### Zusätzliche Anmerkungen

* Eine Wikipedia-Übersicht bestätigt, dass **Claude 3 Opus** ein **200K Token** Kontextfenster hatte, mit Erweiterungen auf **1 Million Token** in bestimmten Fällen ([Wikipedia][9]).

* **Mistrals Sliding-Window-Attention-Mechanismus** unterstützt theoretisch bis zu **4096 × 32 = 131.072 Token**, was eng mit den berichteten 128K-Werten übereinstimmt ([Hugging Face][10]).

---

### Zusammenfassung (Kompaktes Format)

* **Claude Opus 4 / 4.1**: 200.000 Token
* **Claude Sonnet 4**: 200.000 Token (Standard), bis zu **1 Million Token** (Beta/Enterprise)
* **Mistral Medium 3.1**: 128.000 Token
* **Mistral Large 2**: 128.000 Token
* **Mistral Small 3.1**: 128.000 Token (Upgrade von 32K)

---

Lassen Sie mich wissen, wenn Sie weitere Details zu anderen Modellen oder architekturspezifischen Fähigkeiten wünschen!

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