---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修復Claude代碼DeepSeek配置路由
translated: true
type: note
---

明白了。你的配置正在將 **Claude Code 的 Anthropic 風格流量** 發送到 **OpenRouter 的 OpenAI 風格端點** 以使用 DeepSeek V3.1。當 Claude Code（IDE 代理）嘗試執行 tools/plan/stream 時，訊息結構對不上 → 出現錯誤。

以下是一個清晰的連接方式，讓 **Anthropic 模型** 仍然使用 Anthropic 風格的網關，而 **DeepSeek V3.1**（OpenAI 風格）則保持在 `/chat/completions` 端點。我將展示你可以直接貼上的確切編輯內容。

---

### 1) 驗證 DeepSeek V3.1 的 slug

OpenRouter 的聊天模型 slug 是：

```
deepseek/deepseek-chat-v3.1
```

（這是指令/聊天模型——有別於「基礎」模型。）（[OpenRouter][1]）

---

### 2) 為 Claude Code 添加一個 Anthropic 格式的代理

Claude Code 期望 **Anthropic Messages**（`/messages`，`tool_use` 區塊）。最簡單的解決方法是運行一個小型代理來轉換 Anthropic→OpenAI（OpenRouter）並轉換回來。有一個現成的：**maxnowack/anthropic-proxy**。像這樣啟動它（環境變數是你的 OpenRouter 金鑰）：

```bash
OPENROUTER_API_KEY=YOUR_KEY npx anthropic-proxy
```

它會在本地監聽並為你轉換結構。（[GitHub][2]）

現在，添加一個**第二個供應商**，將 Claude Code 的流量指向該代理。

#### 🔧 用這些重點更改替換你的 JSON

**添加此供應商（保持你當前的 `openrouter` 供應商不變）：**

```json
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
```

**保持你現有的 OpenRouter 供應商不變（對於 DeepSeek 和其他 OpenAI 結構的模型，使用 `/chat/completions` 是正確的）。** OpenRouter 規範化為 OpenAI 相容的結構，並支援推理代幣、工具等額外功能。（[OpenRouter][3]）

---

### 3) 將模型路由到正確的供應商

將 Anthropic 模型指向 **anthropic-proxy**；將 DeepSeek/GPT/Gemini/Qwen 指向 **openrouter**。

你可以直接放入的路由器區塊範例：

```json
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
```

> 如果你的路由器不支援 `overrides` 映射，等效的做法是：在你的應用程式中創建獨立的「設定檔」（例如，「Claude Code via anthropic-proxy」與「General chat via openrouter」），並根據每個操作選擇設定檔。

---

### 4) 避免 DeepSeek 上的推理串流衝突（可選但更安全）

DeepSeek V3.1 支援 **「思考」代幣**。許多包裝器如果在串流中途出現這些內容會出錯。在 OpenRouter 上，你可以透過請求標誌**排除推理**。如果你的路由器允許你設定每個模型的參數，請附加：

```json
"params": {
  "reasoning": { "exclude": true }
}
```

（或 `include_reasoning: false`，取決於你的路由器的參數命名）。這可以防止 `