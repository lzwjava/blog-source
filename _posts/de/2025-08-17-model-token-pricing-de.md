---
audio: false
generated: true
image: false
lang: de
layout: post
title: OpenRouter Modell-Token-Preisübersicht
translated: true
type: note
---

Hier sind die aktuellen Kosten für genau diese OpenRouter-Modelle pro **1 Million Tokens** (Eingabe → Ausgabe). Ich beziehe die Daten direkt von der jeweiligen Modellseite:

*   **Anthropic Claude Opus 4** — **15 \$ → 75 \$** (Bilder: 24 \$/K). ([OpenRouter][1])
*   **Anthropic Claude Sonnet 4** — **3 \$ → 15 \$** (Bilder: 4,80 \$/K). ([OpenRouter][2])
*   **Google Gemini 2.5 Flash** — **0,30 \$ → 2,50 \$** (Bilder: 1,238 \$/K). ([OpenRouter][3])
*   **Google Gemini 2.5 Pro** — **1,25 \$ → 10 \$** (die Seite listet "starting at" auf). ([OpenRouter][4])
*   **DeepSeek V3** — **0,18 \$ → 0,72 \$**. ([OpenRouter][5])
*   **Moonshot Kimi K2** — **0,14 \$ → 2,49 \$**. ([OpenRouter][6])
*   **Mistral Medium 3.1** — **0,40 \$ → 2,00 \$**. ([OpenRouter][7])
*   **Qwen3 Coder** — **0,20 \$ → 0,80 \$** *(Hinweis: Ein höherer Tarif greift nach 128k Eingabe-Tokens)*. ([OpenRouter][8])
*   **OpenAI GPT-OSS 120B** — **0,073 \$ → 0,29 \$**. ([OpenRouter][9])
*   **OpenAI GPT-5** — **1,25 \$ → 10 \$**. ([OpenRouter][10])

Schnelle Tipps & Fallstricke:

*   Deine Mapping-Datei enthält **zwei `deepseek-v3`-Schlüssel**; in Python-Dictionaries **überschreibt der spätere den früheren**. Wenn du sowohl bezahlte als auch `:free`-Routen verwenden möchtest, verwende eindeutige Schlüssel (z.B. `"deepseek-v3-free"` vs. `"deepseek-v3"`).
*   Einige Modelle bieten **`:free`**-Routen (nützlich für schnelle Tests, aber ratenbeschränkt): z.B. `qwen/qwen3-coder:free` und `moonshotai/kimi-k2:free`. ([OpenRouter][11])

Wenn du möchtest, kann ich die Beispielkosten für eine Anfrage basierend auf deiner typischen Prompt-/Antwort-Tokengröße berechnen.

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