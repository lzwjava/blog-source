---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修復 DeepSeek 工具呼叫衝突
translated: true
type: note
---

您遇到的是**工具呼叫驗證錯誤**。目前正在 Claude Code 流程中使用 DeepSeek（OpenAI 風格），但該流程預期的是 Anthropic 風格的工具訊息。有兩種安全的解決方法：

* **將所有 Claude Code 工作路由至 Anthropic（透過代理）**
* **當您使用 DeepSeek 時，請關閉工具功能**（使其僅返回純文字）並抑制推理串流

以下是一個已更新的單檔案配置，可同時實現這兩點。請直接貼上使用：

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

這個配置的作用：

* Claude Code 路徑（`default/background/think`）會導向 **透過 `anthropic-proxy` 使用的 Anthropic**，從而確保工具使用正常運作
* DeepSeek 仍可使用，但設定了 `"tool_choice":"none"` 和 `"reasoning.exclude": true`，因此不會發出可能破壞您 IDE 代理的工具呼叫或思考區塊
* 您仍然可以明確選擇 DeepSeek（例如用於純聊天或草稿撰寫），它會透過 OpenRouter 乾淨地路由

如果您仍然看到「無效的工具參數」錯誤，這表示某些層面*仍然*允許 DeepSeek 發出工具呼叫。在這種情況下，請確保您的運行器確實遵守每個模型的 `params` 設定。如果無法做到，請僅在停用工具的環境中使用 DeepSeek，或將 `default` 切換回 `openai/gpt-5-mini`，並將 DeepSeek 保留用於手動的「無工具」設定檔。