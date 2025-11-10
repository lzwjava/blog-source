---
audio: false
generated: true
image: false
lang: ja
layout: post
title: AIモデルコンテキストウィンドウ比較2025
translated: true
type: note
---

以下は、あなたが挙げたモデルのコンテキストウィンドウサイズについて、表を使わずに明確にまとめたものです：

---

### 主要なコンテキストウィンドウ

**Gemini-2.5-Pro**
GoogleのGemini 2.5 Proは、**100万トークン**のコンテキストウィンドウを提供しており、さらに**200万トークン**へと近々拡大する計画です（[Google AI for Developers][1], [blog.google][2]）。これは現在、挙げられたモデルの中で最大です。

---

### Claude モデル (Anthropic ファミリー)

*   **Claude-3 Opus**（およびSonnetなどのファミリーモデル）は、当初**20万トークン**を提供し、選択されたユーザー向けには100万トークンを超える能力を持っていました（[Reddit][3], [Wikipedia][4]）。
*   有料プランでは、コンテキストウィンドウは**20万トークン以上**（約500ページ分）を維持しています（[Anthropic Help Center][5]）。
*   Enterpriseプランにおける**Sonnet 4**は、最大**50万トークン**を提供します（[Anthropic Help Center][6]）。
*   また、Claude Code API経由では、**Claude 4 Sonnet**が**100万トークン**をサポートする可能性があります（[ClaudeLog][7]）。

したがって、最大コンテキストは以下の通りです：

*   標準的な Claude Opus 4: ~20万トークン
*   Sonnet 4 (Enterprise): 最大50万トークン
*   API経由 (Claude Code) の Claude 4 Sonnet: 最大100万トークン

---

### GPT-5 (OpenAI)

*   OpenAIは、GPT-5のコンテキストウィンドウを**25万6千トークン**と公式に述べています（[WIRED][8], [Amazon Web Services, Inc.][9], [Anthropic Help Center][10]）。
*   無料のChatGPTインターフェースは25万6千トークンをサポートするが、APIバリアントではより高い数値になる可能性があるとする情報源もあります—しかし、GPT-5における100万トークンの確認はありません（[Cinco Días][11]）。
*   コミュニティの報告では上限値に関する推測がありますが、ドキュメントでは25万6千トークンで落ち着いているようです（[OpenAI Community][12], [Encord][13]）。

---

### その他のモデル

*   **Gemini-Flash**は、おそらく他のGeminiモデルと同じ大きなコンテキストウィンドウ（100万以上）を持っていると考えられますが、「Flash」に関する具体的な詳細は確認されていません。
*   **その他に挙げられたモデル**—「kimi-k2」、「deepseek-v3/x」、「mistral-medium」、「qwen-coder」、「gpt-oss」など—は、私が見つけた情報源ではコンテキストウィンドウサイズについて顕著に文書化されていません。おそらく、より標準的な範囲（例：<20万トークン）を提供していると考えられますが、明確な確認はありません。

---

### まとめ

*   **全体で最大のコンテキストウィンドウ:** **Gemini 2.5 Pro** (100万トークン、200万トークンへ拡大予定)
*   **僅差で次点:** **API経由の Claude 4 Sonnet** (~100万トークン)
*   **その次:** **GPT-5** (~25万6千トークン)
*   **続いて:** 標準的な**Claudeモデル** (~20万トークン)、**Sonnet 4 Enterprise**は50万トークンに向上

---

特定のモデルについてさらに詳しい情報が必要でしたら、お知らせください—長い表なしで喜んでお手伝いします！

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