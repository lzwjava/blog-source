---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Résoudre les Conflits d'Appels d'Outils DeepSeek
translated: true
type: note
---

Vous rencontrez une **erreur de validation d'appel d'outil**. DeepSeek (style OpenAI) est utilisé dans un flux Claude Code qui attend des messages d'outil de style Anthropic. Deux corrections sûres :

* **Acheminer tout le travail Claude Code vers Anthropic (via le proxy)**.
* **Lorsque vous utilisez DeepSeek, désactivez les outils** (pour qu'il ne renvoie que du texte brut) et supprimez les flux de raisonnement.

Voici une configuration monofichier mise à jour qui fait les deux. Collez-la telle quelle :

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

Ce que cela fait :

* Les chemins Claude Code (`default/background/think`) vont vers **Anthropic via `anthropic-proxy`**, donc l'utilisation d'outils fonctionne.
* DeepSeek reste disponible, mais avec `"tool_choice":"none"` et `"reasoning.exclude": true`, donc il n'émettra pas d'appels d'outils ou de blocs de raisonnement qui cassent votre agent IDE.
* Vous pouvez toujours choisir DeepSeek explicitement (par exemple, pour du chat simple ou de la rédaction), et il sera acheminé proprement via OpenRouter.

Si vous voyez toujours "Invalid tool parameters", cela signifie qu'une couche *autorise toujours* DeepSeek à émettre un appel d'outil. Dans ce cas, assurez-vous que votre exécuteur respecte bien les `params` par modèle. Si ce n'est pas le cas, définissez votre utilisation de DeepSeek uniquement dans des contextes où les outils sont désactivés, ou remettez `default` sur `openai/gpt-5-mini` et réservez DeepSeek pour un profil manuel "sans outils".