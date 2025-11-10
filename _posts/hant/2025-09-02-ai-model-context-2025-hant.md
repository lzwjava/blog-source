---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 2025年人工智能模型上下文窗口比較
translated: true
type: note
---

以下為您所列模型情境長度的清晰說明（不含表格）：

---

### 領先的情境長度

**Gemini-2.5-Pro**
Google 的 Gemini 2.5 Pro 提供 **1 百萬個 token** 的情境長度 — 甚至計劃很快擴展至 **2 百萬個 token**（[Google AI for Developers][1], [blog.google][2]）。這是目前所述模型中最大的。

---

### Claude 模型 (Anthropic 系列)

* **Claude‑3 Opus**（及其系列成員如 Sonnet）最初提供 **200 k tokens**，並為部分用戶提供超過 1 百萬的能力（[Reddit][3], [Wikipedia][4]）。
* 在付費方案中，情境長度維持在 **200 k+ tokens**（約 500 頁）（[Anthropic Help Center][5]）。
* **Sonnet 4** 在企業方案中提供高達 **500 k tokens**（[Anthropic Help Center][6]）。
* 並且，透過 Claude Code API，**Claude 4 Sonnet** 可能支援 **1 百萬個 tokens**（[ClaudeLog][7]）。

因此最大情境長度為：

* 標準 Claude Opus 4：約 200 k tokens。
* Sonnet 4（企業版）：最高 500 k tokens。
* 透過 API 的 Claude 4 Sonnet（Claude Code）：最高 1 百萬個 tokens。

---

### GPT-5 (OpenAI)

* OpenAI 官方聲稱 GPT‑5 的情境長度為 **256 k tokens**（[WIRED][8], [Amazon Web Services, Inc.][9], [Anthropic Help Center][10]）。
* 部分消息來源指出免費的 ChatGPT 介面支援 256 k tokens，而 API 變體可能更高 — 但尚未確認 GPT‑5 有 1M tokens（[Cinco Días][11]）。
* 社群報告提及有上限的猜測，但文件似乎確定為 256 k（[OpenAI Community][12], [Encord][13]）。

---

### 其他模型

* **Gemini-Flash** 可能與其他 Gemini 模型具有相同的大型情境長度（1 百萬以上），但針對 "Flash" 的具體細節尚未確認。
* **其他列出的模型** — 例如 "kimi-k2"、"deepseek-v3/x"、"mistral-medium"、"qwen-coder" 和 "gpt-oss" — 在我找到的資料來源中，並未顯著記載其情境長度。它們可能提供更標準的範圍（例如 <200 k），但未經明確確認。

---

### 總結

* **整體最大情境長度：** **Gemini 2.5 Pro**（1 百萬個 tokens，將擴展至 2 百萬）
* **緊隨其後：** **透過 API 的 Claude 4 Sonnet**（約 1 百萬個 tokens）
* **接著是：** **GPT-5**（約 256 k tokens）
* **隨後是：** 標準 **Claude 模型**（約 200 k tokens），而 **Sonnet 4 企業版** 則提升至 500 k tokens。

---

如果您需要任何特定模型的更深入細節，請告訴我 — 樂意協助，保證不再使用長表格！

[1]: https://ai.google.dev/gemini-api/docs/long-context?utm_source=chatgpt.com "Long context | Gemini API | Google AI for Developers"
[2]: https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/?utm_source=chatgpt.com "Gemini 2.5: Our most intelligent AI model - The Keyword"
[3]: https://www.reddit.com/r/singularity/comments/1b6e0id/claude_3_context_window_is_a_big_deal/?utm_source=chatgpt.com "Claude 3 context window is a big deal : r/singularity - Reddit"
[4]: https://en.wikipedia.org/wiki/Claude_%28language_model%29?utm_source=chatgpt.com "Claude (language model)"
[5]: https://support.anthropic.com/en/articles/7996856-what-is-the-maximum-prompt-length?utm_source=chatgpt.com "What is the maximum prompt length? | Anthropic Help Center"
[6]: https://support.anthropic.com/en/articles/11647753-understanding-usage-and-length-limits?utm_source=chatgpt.com "Understanding Usage and Length Limits | Anthropic Help Center"
[7]: https://www.claudelog.com/faqs/what-is-context-window-in-claude-code/?utm_source=chatgpt.com "What is Context Window in Claude Code"
[8]: https://www.wired.com/story/openais-gpt-5-is-here/?utm_source=chatgpt.com "OpenAI Finally Launched GPT-5. Here's Everything You ..."
[9]: https://aws.amazon.com/bedrock/anthropic/?utm_source=chatgpt.com "Anthropic's Claude in Amazon Bedrock - AWS"
[10]: https://support.anthropic.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans?utm_source=chatgpt.com "How large is the context window on paid Claude plans?"
[11]: https://cincodias.elpais.com/smartlife/lifestyle/2025-08-11/gpt-5-openai-grandes-novedades.html?utm_source=chatgpt.com "GPT-5 de OpenAI: estas son sus grandes novedades para gobernar la IA en 2025"
[12]: https://community.openai.com/t/huge-gpt-5-documentation-gap-flaw-causing-bugs-input-tokens-exceed-the-configured-limit-of-272-000-tokens/1344734?utm_source=chatgpt.com "HUGE GPT-5 DOCUMENTATION GAP/FLAW causing bugs"
[13]: https://encord.com/blog/gpt-5-a-technical-breakdown/?utm_source=chatgpt.com "GPT-5: A Technical Breakdown"