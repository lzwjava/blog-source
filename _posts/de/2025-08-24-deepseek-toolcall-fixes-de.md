---
audio: false
generated: true
image: false
lang: de
layout: post
title: Behebung von DeepSeek-Tool-Konflikten
translated: true
type: note
---

Du erhältst einen **Tool-Call-Validierungsfehler**. DeepSeek (OpenAI-Stil) wird in einem Claude Code-Flow verwendet, der Anthropic-stilige Tool-Nachrichten erwartet. Zwei sichere Lösungen:

* **Leite alle Claude Code-Arbeiten an Anthropic weiter (über den Proxy)**.
* **Wenn du DeepSeek *tatsächlich* verwendest, schalte die Tools aus** (damit es nur Klartext zurückgibt) und unterdrücke die Reasoning-Streams.

Hier ist eine aktualisierte Single-File-Konfiguration, die beides macht. Füge sie unverändert ein:

```json
{
  "PROXY_URL": "http://127.0.0.1:7890",
  "LOG": true,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "",
      "models": [
        "moonshotai/kimi-k2",
        "anthropic/claude-sonnet-4",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.7-sonnet:thinking",
        "anthropic/claude-opus-4",
        "google/gemini-2.5-flash",
        "google/gemini-2.5-pro",
        "deepseek/deepseek-chat-v3-0324",
        "deepseek/deepseek-chat-v3.1",
        "deepseek/deepseek-r1",
        "mistralai/mistral-medium-3.1",
        "qwen/qwen3-coder",
        "openai/gpt-oss-120b",
        "openai/gpt-5",
        "openai/gpt-5-mini",
        "x-ai/grok-3-mini"
      ],
      "transformer": {
        "use": ["openrouter"]
      },
      "params": {
        "deepseek/deepseek-chat-v3.1": {
          "tool_choice": "none",
          "reasoning": { "exclude": true }
        },
        "deepseek/deepseek-r1": {
          "tool_choice": "none",
          "reasoning": { "exclude": true }
        }
      }
    },
    {
      "name": "anthropic-proxy",
      "api_base_url": "http://127.0.0.1:3000/v1/messages",
      "api_key": "",
      "models": [
        "anthropic/claude-sonnet-4",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.7-sonnet:thinking",
        "anthropic/claude-opus-4"
      ]
    }
  ],
  "Router": {
    "default": "anthropic-proxy,anthropic/claude-sonnet-4",
    "background": "anthropic-proxy,anthropic/claude-sonnet-4",
    "think": "anthropic-proxy,anthropic/claude-sonnet-4",
    "longContext": "openrouter,moonshotai/kimi-k2",
    "longContextThreshold": 2000,
    "webSearch": "openrouter,mistralai/mistral-medium-3.1",
    "overrides": {
      "deepseek/deepseek-chat-v3.1": "openrouter,deepseek/deepseek-chat-v3.1",
      "deepseek/deepseek-r1": "openrouter,deepseek/deepseek-r1",
      "google/gemini-2.5-flash": "openrouter,google/gemini-2.5-flash",
      "google/gemini-2.5-pro": "openrouter,google/gemini-2.5-pro",
      "qwen/qwen3-coder": "openrouter,qwen/qwen3-coder",
      "openai/gpt-5-mini": "openrouter,openai/gpt-5-mini"
    }
  }
}
```

Was das bewirkt:

* Claude Code-Pfade (`default/background/think`) gehen zu **Anthropic über `anthropic-proxy`**, sodass die Tool-Nutzung funktioniert.
* DeepSeek bleibt verfügbar, aber mit `"tool_choice":"none"` und `"reasoning.exclude": true`, sodass es keine Tool-Aufrufe oder Denk-Chunks ausgibt, die deinen IDE-Agenten beschädigen.
* Du kannst DeepSeek weiterhin explizit auswählen (z.B. für einfachen Chat oder das Verfassen von Entwürfen), und es wird sauber über OpenRouter geroutet.

Wenn du weiterhin "Invalid tool parameters" siehst, bedeutet das, dass eine Ebene *immer noch* zulässt, dass DeepSeek einen Tool-Aufruf ausgibt. Stelle in diesem Fall sicher, dass dein Runner die model-spezifischen `params` tatsächlich respektiert. Falls nicht, setze deine DeepSeek-Nutzung nur in Kontexten ein, in denen Tools deaktiviert sind, oder stelle `default` wieder auf `openai/gpt-5-mini` zurück und reserviere DeepSeek für ein manuelles "No-Tools"-Profil.