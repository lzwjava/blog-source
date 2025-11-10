---
audio: false
generated: true
image: false
lang: ja
layout: post
title: AIモデルのコンテキストウィンドウ容量
translated: true
type: note
---

以下に、最近のドキュメントと発表に基づいてリストアップされたモデルの**現在の最大トークン容量（コンテキストウィンドウサイズ）**を示します。

---

### Anthropic モデル

* **Claude Opus 4 / Opus 4.1**
  **200,000トークン**のコンテキストウィンドウを提供し、持続的な推論と複雑なワークフローに理想的です ([Anthropic][1], [Amazon Web Services, Inc.][2])。

* **Claude Sonnet 4**
  ネイティブで**200,000トークン**のコンテキストをサポートします ([Prompthub][3])。
  さらに、**ベータ版アップグレード**により、エンタープライズ/APIユーザー向けに**大規模な100万トークン**のコンテキストが可能になりました ([Anthropic][4])。

---

### Mistral AI モデル

* **Mistral Medium 3.1**
  **128,000トークン**のコンテキストウィンドウを持ちます ([OpenRouter][5])。

* **Mistral Large 2**
  **128,000トークン**のコンテキスト長をサポートします ([Wikipedia][6])。

* **Mistral Medium (以前のバージョン)**
  以前は、コンテキストの標準は**32,000トークン**でした ([Clarifai][7], [Mistral AI][8])。

* **Mistral Small 3.1**
  この新しいバージョンで、コンテキストウィンドウを**32Kから128Kトークンにアップグレード**しました ([Wikipedia][6])。

---

### 補足事項

* Wikipediaの概要によると、**Claude 3 Opus**は**200Kトークン**のコンテキストウィンドウを持ち、特定の場合では**100万トークン**まで拡張されました ([Wikipedia][9])。

* **Mistralのスライディングウィンドウアテンション機構**は、理論上**4096 × 32 = 131,072トークン**までサポート可能であり、報告されている128Kの数値とほぼ一致します ([Hugging Face][10])。

---

### 概要 (簡潔な形式)

* **Claude Opus 4 / 4.1**: 200,000 トークン
* **Claude Sonnet 4**: 200,000 トークン (標準)、**100万トークン**まで (ベータ/エンタープライズ)
* **Mistral Medium 3.1**: 128,000 トークン
* **Mistral Large 2**: 128,000 トークン
* **Mistral Small 3.1**: 128,000 トークン (32Kからアップグレード)

---

他のモデルやアーキテクチャ固有の機能について、さらに詳細が必要な場合はお知らせください。

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