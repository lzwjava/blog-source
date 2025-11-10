---
audio: false
generated: true
image: false
lang: ja
layout: post
title: OpenRouterモデルトークン価格ガイド
translated: true
type: note
---

以下は、現在のOpenRouterモデルの**100万トークン**あたりの正確なコストです（入力 → 出力）。各モデルのページから直接引用しています：

* **Anthropic Claude Opus 4** — **\$15 → \$75**（画像: \$24/K）。([OpenRouter][1])
* **Anthropic Claude Sonnet 4** — **\$3 → \$15**（画像: \$4.80/K）。([OpenRouter][2])
* **Google Gemini 2.5 Flash** — **\$0.30 → \$2.50**（画像: \$1.238/K）。([OpenRouter][3])
* **Google Gemini 2.5 Pro** — **\$1.25 → \$10**（ページには「〜から」と記載）。([OpenRouter][4])
* **DeepSeek V3** — **\$0.18 → \$0.72**。([OpenRouter][5])
* **Moonshot Kimi K2** — **\$0.14 → \$2.49**。([OpenRouter][6])
* **Mistral Medium 3.1** — **\$0.40 → \$2.00**。([OpenRouter][7])
* **Qwen3 Coder** — **\$0.20 → \$0.80** *（注: 128K入力トークンを超えると上位ティアが適用）*。([OpenRouter][8])
* **OpenAI GPT-OSS 120B** — **\$0.073 → \$0.29**。([OpenRouter][9])
* **OpenAI GPT-5** — **\$1.25 → \$10**。([OpenRouter][10])

簡単なヒントと注意点：

* あなたのマッピングには **`deepseek-v3`キーが2つ** あります。Pythonの辞書では**後から指定されたものが前のものを上書きします**。有料と`:free`ルートの両方を利用したい場合は、異なるキー（例: `"deepseek-v3-free"` と `"deepseek-v3"`）を使用してください。
* 一部のモデルには **`:free`** ルートがあります（簡単なテストに便利ですがレート制限あり）：例 `qwen/qwen3-coder:free` と `moonshotai/kimi-k2:free`。([OpenRouter][11])

ご希望であれば、あなたが通常使用するプロンプト/レスポンスのトークンサイズに基づいて、リクエストコストの例を計算できます。

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