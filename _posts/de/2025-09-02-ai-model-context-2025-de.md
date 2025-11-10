---
audio: false
generated: true
image: false
lang: de
layout: post
title: Vergleich von Kontextfenstern KI-Modelle 2025
translated: true
type: note
---

Hier ist eine übersichtlichere Darstellung – ohne Tabelle – der Kontextfenstergrößen der von Ihnen aufgeführten Modelle:

---

### Führende Kontextfenster

**Gemini-2.5-Pro**
Googles Gemini 2.5 Pro bietet ein **1 Millionen Token** großes Kontextfenster – und plant sogar, dies bald auf **2 Millionen Token** zu erweitern ([Google AI for Developers][1], [blog.google][2]). Dies ist derzeit das größte unter den genannten Modellen.

---

### Claude-Modelle (Anthropic-Familie)

* **Claude‑3 Opus** (und Familie wie Sonnet) boten zunächst **200 k Token**, mit Fähigkeiten, die für ausgewählte Nutzer 1 Million übersteigen ([Reddit][3], [Wikipedia][4]).
* Auf kostenpflichtigen Plänen bleibt das Kontextfenster bei **200 k+ Token** (etwa 500 Seiten) ([Anthropic Help Center][5]).
* **Sonnet 4** auf Enterprise-Plänen bietet bis zu **500 k Token** ([Anthropic Help Center][6]).
* Und über die Claude Code API kann **Claude 4 Sonnet** **1 Millionen Token** unterstützen ([ClaudeLog][7]).

Zusammenfassung der maximalen Kontextgröße:

* Standard Claude Opus 4: \~200 k Token.
* Sonnet 4 (Enterprise): bis zu 500 k Token.
* Claude 4 Sonnet via API (Claude Code): bis zu 1 Million Token.

---

### GPT-5 (OpenAI)

* OpenAI gibt offiziell ein **256 k Token** großes Kontextfenster für GPT‑5 an ([WIRED][8], [Amazon Web Services, Inc.][9], [Anthropic Help Center][10]).
* Einige Quellen deuten darauf hin, dass die kostenlose ChatGPT-Oberfläche 256 k Token unterstützt, während API-Varianten höher gehen könnten – aber es gibt keine bestätigten 1M Token für GPT‑5 ([Cinco Días][11]).
* Community-Berichte erwähnen eine spekulative Obergrenze, aber die Dokumentation scheint sich auf 256 k zu belaufen ([OpenAI Community][12], [Encord][13]).

---

### Andere Modelle

* **Gemini-Flash** hat wahrscheinlich das gleiche große Kontextfenster wie andere Gemini-Modelle (1 Million+), aber die Details speziell für "Flash" sind nicht bestätigt.
* **Andere aufgeführte Modelle** – wie „kimi-k2“, „deepseek-v3/x“, „mistral-medium“, „qwen-coder“ und „gpt-oss“ – sind in den von mir gefundenen Quellen nicht prominent in Bezug auf die Kontextfenstergröße dokumentiert. Wahrscheinlich bieten sie eher Standardbereiche (z. B. <200 k) an, allerdings ohne ausdrückliche Bestätigung.

---

### Fazit

* **Größtes Kontextfenster insgesamt:** **Gemini 2.5 Pro** (1 Million Token, Erweiterung auf 2 Millionen geplant)
* **Knapper Zweitplatzierter:** **Claude 4 Sonnet via API** (\~1 Million Token)
* **Danach:** **GPT-5** (\~256 k Token)
* **Gefolgt von:** Standard-**Claude-Modellen** (\~200 k Token), wobei **Sonnet 4 Enterprise** auf 500 k Token erhöht.

---

Lassen Sie mich wissen, wenn Sie tiefergehende Details zu einem bestimmten Modell wünschen – ich helfe gerne ohne lange Tabellen, versprochen!

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