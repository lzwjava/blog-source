---
audio: false
generated: true
image: false
lang: hant
layout: post
title: OpenRouter 模型代幣定價指南
translated: true
type: note
---

以下是目前這些 OpenRouter 模型每 **100 萬個 token** 的準確費用（輸入 → 輸出）。我直接從每個模型的頁面獲取資料：

* **Anthropic Claude Opus 4** — **15 美元 → 75 美元**（圖片：24 美元/K）。（[OpenRouter][1]）
* **Anthropic Claude Sonnet 4** — **3 美元 → 15 美元**（圖片：4.80 美元/K）。（[OpenRouter][2]）
* **Google Gemini 2.5 Flash** — **0.30 美元 → 2.50 美元**（圖片：1.238 美元/K）。（[OpenRouter][3]）
* **Google Gemini 2.5 Pro** — **1.25 美元 → 10 美元**（頁面列示「起始價格」）。（[OpenRouter][4]）
* **DeepSeek V3** — **0.18 美元 → 0.72 美元**。（[OpenRouter][5]）
* **Moonshot Kimi K2** — **0.14 美元 → 2.49 美元**。（[OpenRouter][6]）
* **Mistral Medium 3.1** — **0.40 美元 → 2.00 美元**。（[OpenRouter][7]）
* **Qwen3 Coder** — **0.20 美元 → 0.80 美元** *（注意：超過 128k 輸入 token 後會啟用更高階層價格）*。（[OpenRouter][8]）
* **OpenAI GPT-OSS 120B** — **0.073 美元 → 0.29 美元**。（[OpenRouter][9]）
* **OpenAI GPT-5** — **1.25 美元 → 10 美元**。（[OpenRouter][10]）

快速提示與注意事項：

* 你的映射中有 **兩個 `deepseek-v3` 鍵值**；在 Python 字典中 **後面的鍵值會覆蓋前面的**。如果你想同時使用付費和 `:free` 路由，請使用不同的鍵值（例如 `"deepseek-v3-free"` 與 `"deepseek-v3"`）。
* 部分模型提供 **`:free`** 路由（適用於快速測試但有速率限制）：例如 `qwen/qwen3-coder:free` 和 `moonshotai/kimi-k2:free`。（[OpenRouter][11]）

如果你需要，我可以根據你常用的提示/回應 token 大小計算範例請求成本。

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