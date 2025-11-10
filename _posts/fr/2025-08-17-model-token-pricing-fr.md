---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide des Prix des Jetons de Modèle OpenRouter
translated: true
type: note
---

Voici le coût actuel de ces modèles OpenRouter exacts pour **1 million de jetons** (entrée → sortie). Je me base directement sur la page de chaque modèle :

* **Anthropic Claude Opus 4** — **15 \$ → 75 \$** (images : 24 \$ / K). ([OpenRouter][1])
* **Anthropic Claude Sonnet 4** — **3 \$ → 15 \$** (images : 4,80 \$ / K). ([OpenRouter][2])
* **Google Gemini 2.5 Flash** — **0,30 \$ → 2,50 \$** (images : 1,238 \$ / K). ([OpenRouter][3])
* **Google Gemini 2.5 Pro** — **1,25 \$ → 10 \$** (la page indique « à partir de »). ([OpenRouter][4])
* **DeepSeek V3** — **0,18 \$ → 0,72 \$**. ([OpenRouter][5])
* **Moonshot Kimi K2** — **0,14 \$ → 2,49 \$**. ([OpenRouter][6])
* **Mistral Medium 3.1** — **0,40 \$ → 2,00 \$**. ([OpenRouter][7])
* **Qwen3 Coder** — **0,20 \$ → 0,80 \$** *(note : un tarif supérieur s'applique au-delà de 128k jetons d'entrée)*. ([OpenRouter][8])
* **OpenAI GPT-OSS 120B** — **0,073 \$ → 0,29 \$**. ([OpenRouter][9])
* **OpenAI GPT-5** — **1,25 \$ → 10 \$**. ([OpenRouter][10])

Conseils rapides et pièges :

* Votre mapping a **deux clés `deepseek-v3`** ; dans les dictionnaires Python, **la dernière écrase la première**. Si vous voulez à la fois des routes payantes et `:free`, utilisez des clés distinctes (par exemple, `"deepseek-v3-free"` vs `"deepseek-v3"`).
* Certains modèles ont des routes **`:free`** (utiles pour des tests rapides mais avec des limites de débit) : par exemple, `qwen/qwen3-coder:free` et `moonshotai/kimi-k2:free`. ([OpenRouter][11])

Si vous le souhaitez, je peux calculer des exemples de coût par requête pour vos tailles typiques de jetons de prompt/réponse.

[1]: https://openrouter.ai/anthropic/claude-opus-4 "OpenRouter"
[2]: https://openrouter.ai/anthropic/claude-sonnet-4 "OpenRouter"
[3]: https://openrouter.ai/google/gemini-2.5-flash "OpenRouter"
[4]: https://openrouter.ai/google/gemini-2.5-pro "OpenRouter"
[5]: https://openrouter.ai/deepseek/deepseek-chat "OpenRouter"
[6]: https://openrouter.ai/moonshotai/kimi-k2 "OpenRouter"
[7]: https://openrouter.ai/mistralai/mistral-medium-3.1 "OpenRouter"
[8]: https://openrouter.ai/qwen/qwen3-coder "OpenRouter"
[9]: https://openrouter.ai/openai/gpt-oss-120b?utm_source=chatgpt.com "gpt-oss-120b - API, Providers, Stats"
[10]: https://openrouter.ai/openai/gpt-5?utm_source=chatgpt.com "GPT-5 - API, Providers, Stats"
[11]: https://openrouter.ai/qwen/qwen3-coder%3Afree?utm_source=chatgpt.com "Qwen3 Coder (free) - API, Providers, Stats"