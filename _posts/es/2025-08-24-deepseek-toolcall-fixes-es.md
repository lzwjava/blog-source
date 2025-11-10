---
audio: false
generated: true
image: false
lang: es
layout: post
title: Corrección de Conflictos en Llamadas a Herramientas de DeepSeek
translated: true
type: note
---

Estás experimentando un **error de validación de llamadas a herramientas**. Se está utilizando DeepSeek (estilo OpenAI) en un flujo de Claude Code que espera mensajes de herramientas al estilo Anthropic. Dos soluciones seguras:

* **Dirige todo el trabajo de Claude Code a Anthropic (a través del proxy)**.
* **Cuando *sí* uses DeepSeek, desactiva las herramientas** (para que solo devuelva texto plano) y suprime los flujos de razonamiento.

Aquí tienes una configuración de un solo archivo actualizada que hace ambas cosas. Pégala tal cual:

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

Lo que esto hace:

* Las rutas de Claude Code (`default/background/think`) van a **Anthropic a través de `anthropic-proxy`**, por lo que el uso de herramientas funciona.
* DeepSeek permanece disponible, pero con `"tool_choice":"none"` y `"reasoning.exclude": true`, por lo que no emitirá llamadas a herramientas o fragmentos de razonamiento que rompan tu agente del IDE.
* Todavía puedes seleccionar DeepSeek explícitamente (por ejemplo, para chat plano o redacción), y se enrutará limpiamente a través de OpenRouter.

Si aún ves "Parámetros de herramienta no válidos", significa que alguna capa *todavía* está permitiendo que DeepSeek emita una llamada a herramienta. En ese caso, asegúrate de que tu ejecutor realmente respete los `params` por modelo. Si no es así, configura tu uso de DeepSeek solo en contextos donde las herramientas estén deshabilitadas, o cambia `default` de nuevo a `openai/gpt-5-mini` y reserva DeepSeek para un perfil manual "sin herramientas".