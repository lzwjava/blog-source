---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Capacités de la fenêtre de contexte des modèles d'IA
translated: true
type: note
---

Voici les **capacités maximales actuelles en tokens (tailles de fenêtre de contexte)** pour les modèles que vous avez listés, d'après la documentation et les annonces récentes :

---

### Modèles Anthropic

* **Claude Opus 4 / Opus 4.1**
  Offre une fenêtre de contexte de **200 000 tokens**, idéale pour le raisonnement soutenu et les workflows complexes ([Anthropic][1], [Amazon Web Services, Inc.][2]).

* **Claude Sonnet 4**
  Supporte nativement **200 000 tokens** de contexte ([Prompthub][3]).
  De plus, une **mise à niveau bêta** permet désormais un **massif 1 million de tokens** de contexte pour les utilisateurs entreprise/API ([Anthropic][4]).

---

### Modèles Mistral AI

* **Mistral Medium 3.1**
  Possède une fenêtre de contexte de **128 000 tokens** ([OpenRouter][5]).

* **Mistral Large 2**
  Supporte également une longueur de contexte de **128 000 tokens** ([Wikipedia][6]).

* **Mistral Medium (versions antérieures)**
  Auparavant, la norme était de **32 000 tokens** pour le contexte ([Clarifai][7], [Mistral AI][8]).

* **Mistral Small 3.1**
  A amélioré sa fenêtre de contexte **de 32K à 128K tokens** dans cette nouvelle version ([Wikipedia][6]).

---

### Notes supplémentaires

* Un aperçu Wikipedia confirme que **Claude 3 Opus** avait une fenêtre de contexte de **200K tokens**, avec des extensions à **1 million de tokens** dans certains cas ([Wikipedia][9]).

* **Le mécanisme d'attention à fenêtre glissante de Mistral** supporte théoriquement jusqu'à **4096 × 32 = 131 072 tokens**, ce qui correspond étroitement aux chiffres de 128K rapportés ([Hugging Face][10]).

---

### Résumé (Format concis)

* **Claude Opus 4 / 4.1** : 200 000 tokens
* **Claude Sonnet 4** : 200 000 tokens (standard), jusqu'à **1 million de tokens** (bêta/entreprise)
* **Mistral Medium 3.1** : 128 000 tokens
* **Mistral Large 2** : 128 000 tokens
* **Mistral Small 3.1** : 128 000 tokens (amélioration depuis 32K)

---

Faites-moi savoir si vous souhaitez plus de détails sur d'autres modèles ou des capacités spécifiques à l'architecture !

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