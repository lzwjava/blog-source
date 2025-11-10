---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Precios de Tokens de Modelos de OpenRouter
translated: true
type: note
---

Aquí tienes el costo actual por **1 millón de tokens** (entrada → salida) de esos mismos modelos de OpenRouter. Estoy extrayendo la información directamente de la página de cada modelo:

*   **Anthropic Claude Opus 4** — **\$15 → \$75** (imágenes: \$24/K). ([OpenRouter][1])
*   **Anthropic Claude Sonnet 4** — **\$3 → \$15** (imágenes: \$4.80/K). ([OpenRouter][2])
*   **Google Gemini 2.5 Flash** — **\$0.30 → \$2.50** (imágenes: \$1.238/K). ([OpenRouter][3])
*   **Google Gemini 2.5 Pro** — **\$1.25 → \$10** (la página indica "a partir de"). ([OpenRouter][4])
*   **DeepSeek V3** — **\$0.18 → \$0.72**. ([OpenRouter][5])
*   **Moonshot Kimi K2** — **\$0.14 → \$2.49**. ([OpenRouter][6])
*   **Mistral Medium 3.1** — **\$0.40 → \$2.00**. ([OpenRouter][7])
*   **Qwen3 Coder** — **\$0.20 → \$0.80** *(nota: un nivel de precio más alto se aplica después de 128k tokens de entrada)*. ([OpenRouter][8])
*   **OpenAI GPT-OSS 120B** — **\$0.073 → \$0.29**. ([OpenRouter][9])
*   **OpenAI GPT-5** — **\$1.25 → \$10**. ([OpenRouter][10])

Consejos rápidos y advertencias:

*   Tu mapeo tiene **dos claves `deepseek-v3`**; en los diccionarios de Python, **la última sobrescribe a la primera**. Si quieres ambas rutas, de pago y `:free`, usa claves distintas (ej., `"deepseek-v3-free"` vs `"deepseek-v3"`).
*   Algunos modelos tienen rutas **`:free`** (útiles para pruebas rápidas pero con límites de tasa): ej., `qwen/qwen3-coder:free` y `moonshotai/kimi-k2:free`. ([OpenRouter][11])

Si quieres, puedo calcular el costo de solicitudes de ejemplo para tus tamaños típicos de tokens en prompt/respuesta.

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