---
audio: false
generated: true
image: false
lang: hi
layout: post
title: ओपनराउटर मॉडल टोकन मूल्य निर्धारण मार्गदर्शिका
translated: true
type: note
---

यहाँ उन ठीक-ठीक OpenRouter मॉडल्स की वर्तमान लागत **10 लाख टोकन्स** के लिए है (इनपुट → आउटपुट)। मैं सीधे हर मॉडल के पेज से यह जानकारी ले रहा हूँ:

* **Anthropic Claude Opus 4** — **\$15 → \$75** (इमेज: \$24/K). ([OpenRouter][1])
* **Anthropic Claude Sonnet 4** — **\$3 → \$15** (इमेज: \$4.80/K). ([OpenRouter][2])
* **Google Gemini 2.5 Flash** — **\$0.30 → \$2.50** (इमेज: \$1.238/K). ([OpenRouter][3])
* **Google Gemini 2.5 Pro** — **\$1.25 → \$10** (पेज पर "starting at" लिखा है). ([OpenRouter][4])
* **DeepSeek V3** — **\$0.18 → \$0.72**. ([OpenRouter][5])
* **Moonshot Kimi K2** — **\$0.14 → \$2.49**. ([OpenRouter][6])
* **Mistral Medium 3.1** — **\$0.40 → \$2.00**. ([OpenRouter][7])
* **Qwen3 Coder** — **\$0.20 → \$0.80** *(नोट: 128k इनपुट टोकन्स के बाद उच्चतर टियर लागू होता है)*. ([OpenRouter][8])
* **OpenAI GPT-OSS 120B** — **\$0.073 → \$0.29**. ([OpenRouter][9])
* **OpenAI GPT-5** — **\$1.25 → \$10**. ([OpenRouter][10])

त्वरित सुझाव और ध्यान देने योग्य बातें:

* आपकी मैपिंग में **दो `deepseek-v3` कीज़** हैं; Python डिक्शनरी में **बाद वाला की पहले वाले को ओवरराइट कर देता है**। अगर आपको भुगतान वाले और `:free` रूट दोनों चाहिए, तो अलग-अलग कीज़ का इस्तेमाल करें (जैसे, `"deepseek-v3-free"` बनाम `"deepseek-v3"`)।
* कुछ मॉडल्स में **`:free`** रूट होते हैं (त्वरित टेस्ट के लिए उपयोगी लेकिन रेट-लिमिटेड): उदाहरण के लिए, `qwen/qwen3-coder:free` और `moonshotai/kimi-k2:free`. ([OpenRouter][11])

अगर आप चाहें, तो मैं आपके सामान्य प्रॉम्प्ट/रिस्पॉन्स टोकन आकारों के लिए उदाहरण अनुरोध लागत की गणना कर सकता हूँ।

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