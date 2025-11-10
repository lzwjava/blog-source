---
audio: false
generated: true
image: false
lang: de
layout: post
title: Behebung der DeepSeek-Claude-Code-Schema-Diskrepanz
translated: true
type: note
---

Kurze Antwort: Schema-Konflikt.

Claude Code „spricht Anthropic“ (er erwartet Anthropic-Messages-artige Tool-Nutzung wie `tool_use` / `tool_result` Blöcke). DeepSeek V3.1 auf OpenRouter „spricht OpenAI“ (es gibt OpenAI-artige `tool_calls` / Function Calling aus). Wenn Ihr Claude Code Router eine Aufgabe an DeepSeek V3.1 weiterleitet, ohne die Anfrage/Antwort zu transformieren, werden die Tool-Calling-Nachrichten des Assistenten nicht geparst – und Sie sehen Fehler genau dann, wenn der Agent versucht, Tools zu planen/auszuführen oder die Ausgabe zu streamen. ([Anthropic][1], [OpenRouter][2], [DeepSeek API Docs][3])

Was zu tun ist (schnelle Lösungen):

1.  Nutzen Sie die Transformer des Routers
    Aktivieren Sie die OpenRouter↔︎Anthropic Request/Response-Transformer in Ihrem Claude Code Router, damit `tool_calls` ⇄ `tool_use` in beide Richtungen gemappt werden. Der beliebte Community-Router unterstützt dies explizit; prüfen Sie dessen Abschnitt „Request/Response Transformation“ und die Beispielkonfigurationen. ([GitHub][4], [ClaudeLog][5])

2.  Wählen Sie den korrekten Model-Slug
    DeepSeek V3.1 hat spezifische OpenRouter-Slugs (z.B. die V3.1/V3 Family Einträge). Ein falscher oder veralteter Slug kann ebenfalls Fehler während der Streaming- oder Tool-Phasen verursachen. Verifizieren Sie die exakte Model-ID, die auf der DeepSeek-Seite von OpenRouter angezeigt wird, und verwenden Sie diese in Ihrer Router-Zuordnung. ([OpenRouter][6])

3.  Bleiben Sie in „chat“ (nicht „reasoner“), es sei denn, Sie haben dessen Felder gemappt
    Wenn Sie eine Reasoning-Variante ausprobieren, die spezielle Reasoning-Felder streamt, muss Ihr Router diese übersetzen – sonst wird Claude Code scheitern. Bevorzugen Sie das Standard-Chat-Model oder deaktivieren Sie die zusätzliche „Thinking“-Ausgabe, bis Ihr Transformer damit umgehen kann. (Die Docs von DeepSeek betonen OpenAI-artiges Function Calling; genau das sollten Sie mappen.) ([DeepSeek API Docs][3])

4.  Aktualisieren Sie auf die neueste Router-Version
    Kürzliche Community-Builds haben Kompatibilitäts-Anpassungen für nicht-Anthropic-Provider hinzugefügt; führen Sie ein Upgrade durch, bevor Sie testen. ([GitHub][4])

Warum das nur bei V3.1 passiert
V3.1 hat standardmäßig stärkeres Agent/Tool-Calling hinzugefügt. Das erhöht die Wahrscheinlichkeit, dass Ihr Claude Code-Flow auf die nicht-transformierten Tool-Nachrichten trifft, was genau der Punkt ist, an dem der Schema-Konflikt zuschlägt. ([DeepSeek API Docs][7])

Wenn Sie den exakten Fehlertext teilen, kann ich auf den genauen Transformer-Ausschnitt verweisen, den Sie in Ihre Konfiguration einfügen müssen.

[1]: https://www.anthropic.com/engineering/claude-code-best-practices?utm_source=chatgpt.com "Claude Code: Best practices for agentic coding"
[2]: https://openrouter.ai/docs/features/tool-calling?utm_source=chatgpt.com "Tool & Function Calling"
[3]: https://api-docs.deepseek.com/guides/function_calling?utm_source=chatgpt.com "Function Calling"
[4]: https://github.com/musistudio/claude-code-router?utm_source=chatgpt.com "musistudio/claude-code-router"
[5]: https://claudelog.com/claude-code-mcps/claude-code-router/?utm_source=chatgpt.com "Claude Code Router"
[6]: https://openrouter.ai/models?q=deepseek&utm_source=chatgpt.com "Models: 'deepseek'"
[7]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 Release"