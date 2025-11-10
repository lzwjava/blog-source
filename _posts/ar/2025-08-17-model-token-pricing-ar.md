---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل تسعير رموز نموذج OpenRouter
translated: true
type: note
---

إليك التكلفة الحالية لنماذج OpenRouter المذكورة بالضبط لكل **1 مليون رمز** (إدخال → إخراج). أنا أستقبل المعلومات مباشرة من صفحة كل نموذج:

* **Anthropic Claude Opus 4** — **15 دولارًا → 75 دولارًا** (الصور: 24 دولارًا/ألف). ([OpenRouter][1])
* **Anthropic Claude Sonnet 4** — **3 دولارات → 15 دولارًا** (الصور: 4.80 دولار/ألف). ([OpenRouter][2])
* **Google Gemini 2.5 Flash** — **0.30 دولار → 2.50 دولار** (الصور: 1.238 دولار/ألف). ([OpenRouter][3])
* **Google Gemini 2.5 Pro** — **1.25 دولار → 10 دولارات** (الصفحة تُدرج "بدءًا من"). ([OpenRouter][4])
* **DeepSeek V3** — **0.18 دولار → 0.72 دولار**. ([OpenRouter][5])
* **Moonshot Kimi K2** — **0.14 دولار → 2.49 دولار**. ([OpenRouter][6])
* **Mistral Medium 3.1** — **0.40 دولار → 2.00 دولار**. ([OpenRouter][7])
* **Qwen3 Coder** — **0.20 دولار → 0.80 دولار** *(ملاحظة: يُطبق سعر أعلى بعد تجاوز 128 ألف رمز إدخال)*. ([OpenRouter][8])
* **OpenAI GPT-OSS 120B** — **0.073 دولار → 0.29 دولار**. ([OpenRouter][9])
* **OpenAI GPT-5** — **1.25 دولار → 10 دولارات**. ([OpenRouter][10])

نصائح سريعة وأمور需要注意:

* تحتوي تعييناتك على **مفتاحين `deepseek-v3`**؛ في قواميس Python **المفتاح اللاحق يكتب فوق السابق**. إذا كنت تريد كلًا من المسارات المدفوعة و `:free`، استخدم مفاتيح مميزة (مثل `"deepseek-v3-free"` مقابل `"deepseek-v3"`).
* بعض النماذج لديها مسارات **`:free`** (مفيدة للاختبارات السريعة ولكنها محدودة بمعدل الاستخدام): على سبيل المثال، `qwen/qwen3-coder:free` و `moonshotai/kimi-k2:free`. ([OpenRouter][11])

إذا أردت، يمكنني حساب تكاليف الطلبات النموذجية لأحجام الرموز المعتادة في المطالبات والاستجابات.

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