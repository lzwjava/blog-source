---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide de configuration du proxy multi-modèle mis à jour
translated: true
type: note
---

Voici votre configuration mise à jour—ajoutez-la à votre config :

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
    "default": "openrouter,openai/gpt-5-mini",
    "background": "openrouter,google/gemini-2.5-flash",
    "think": "openrouter,qwen/qwen3-coder",
    "longContext": "openrouter,moonshotai/kimi-k2",
    "longContextThreshold": 2000,
    "webSearch": "openrouter,mistralai/mistral-medium-3.1",
    "overrides": {
      "anthropic/claude-sonnet-4": "anthropic-proxy,anthropic/claude-sonnet-4",
      "anthropic/claude-3.5-sonnet": "anthropic-proxy,anthropic/claude-3.5-sonnet",
      "anthropic/claude-3.7-sonnet:thinking": "anthropic-proxy,anthropic/claude-3.7-sonnet:thinking",
      "anthropic/claude-opus-4": "anthropic-proxy,anthropic/claude-opus-4",
      "deepseek/deepseek-chat-v3.1": "openrouter,deepseek/deepseek-chat-v3.1"
    }
  }
}
```

Si votre runner expose un flag pour supprimer les flux de raisonnement sur DeepSeek (parfois appelé `reasoning.exclude` ou similaire), activez-le pour `deepseek/deepseek-chat-v3.1` pour éviter les problèmes d'analyse de l'interface utilisateur.