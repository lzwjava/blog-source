---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 人工智能模型上下文窗口容量
translated: true
type: note
---

以下是您所列模型的**當前最大 token 容量（上下文窗口大小）**，基於近期文件與公告：

---

### Anthropic 模型

* **Claude Opus 4 / Opus 4.1**
  提供 **200,000 tokens** 的上下文窗口，非常適合持續推理與複雜工作流程（[Anthropic][1]、[Amazon Web Services, Inc.][2]）。

* **Claude Sonnet 4**
  同樣原生支援 **200,000 tokens** 的上下文（[Prompthub][3]）。
  此外，**測試版升級**現為企業/API 用戶提供**高達 100 萬 tokens** 的龐大上下文容量（[Anthropic][4]）。

---

### Mistral AI 模型

* **Mistral Medium 3.1**
  具有 **128,000 tokens** 的上下文窗口（[OpenRouter][5]）。

* **Mistral Large 2**
  同樣支援 **128,000 tokens** 的上下文長度（[Wikipedia][6]）。

* **Mistral Medium (早期版本)**
  先前標準上下文為 **32,000 tokens**（[Clarifai][7]、[Mistral AI][8]）。

* **Mistral Small 3.1**
  在此新版本中，其上下文窗口**從 32K 升級至 128K tokens**（[Wikipedia][6]）。

---

### 補充說明

* 一份 Wikipedia 概述確認 **Claude 3 Opus** 具有 **200K token** 上下文窗口，並在某些情況下可擴展至 **100 萬 tokens**（[Wikipedia][9]）。

* **Mistral 的滑動窗口注意力機制**理論上支援高達 **4096 × 32 = 131,072 tokens**，這與報告的 128K 數字非常接近（[Hugging Face][10]）。

---

### 總結 (簡潔格式)

* **Claude Opus 4 / 4.1**：200,000 tokens
* **Claude Sonnet 4**：200,000 tokens (標準)，最高可達 **100 萬 tokens** (測試版/企業版)
* **Mistral Medium 3.1**：128,000 tokens
* **Mistral Large 2**：128,000 tokens
* **Mistral Small 3.1**：128,000 tokens (從 32K 升級)

---

如果您需要其他模型或架構特定功能的更多詳細資訊，請告訴我！

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