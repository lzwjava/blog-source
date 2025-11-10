---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修復 DeepSeek Claude 代碼架構不匹配問題
translated: true
type: note
---

簡短回答：結構描述不符。

Claude Code「使用 Anthropic 語法」（它預期 Anthropic-Messages 風格的工具調用，如 `tool_use` / `tool_result` 區塊）。而 OpenRouter 上的 DeepSeek V3.1「使用 OpenAI 語法」（它採用 OpenAI 風格的 `tool_calls` / 函數調用）。若您的 Claude Code 路由在未轉換請求/回應的情況下將任務轉發給 DeepSeek V3.1，則助理的工具調用訊息將無法解析——您會在代理嘗試規劃/執行工具或串流輸出時立即看到錯誤。（[Anthropic][1]、[OpenRouter][2]、[DeepSeek API 文檔][3]）

解決方法（快速修復）：

1. 使用路由器的轉換器
   在您的 Claude Code 路由器中啟用 OpenRouter↔︎Anthropic 請求/回應轉換器，以便雙向映射 `tool_calls` ⇄ `tool_use`。熱門的社群路由器明確支援此功能；請檢查其「請求/回應轉換」章節與範例設定。（[GitHub][4]、[ClaudeLog][5]）

2. 選擇正確的模型代稱
   DeepSeek V3.1 有特定的 OpenRouter 代稱（例如 V3.1/V3 系列條目）。錯誤或過時代稱也可能在串流或工具階段引發錯誤。請確認 OpenRouter 的 DeepSeek 頁面上顯示的確切模型 ID，並在路由映射中使用。（[OpenRouter][6]）

3. 保持在「聊天」模式（非「推理器」），除非已映射其欄位
   若嘗試使用會串流特殊推理欄位的推理變體，您的路由器必須轉譯它們——否則 Claude Code 將無法處理。建議使用標準聊天模型，或停用額外的「思考」輸出，直到您的轉換器能處理為止。（DeepSeek 的文檔強調 OpenAI 風格的函數調用；這正是您應映射的目標。）（[DeepSeek API 文檔][3]）

4. 更新至最新路由器版本
   近期的社群版本已針對非 Anthropic 供應商加入相容性調整；請在測試前升級。（[GitHub][4]）

為何僅發生在 V3.1
V3.1 預設強化了代理/工具調用功能。這提高了您的 Claude Code 流程遇到未轉譯工具訊息的機率，而這正是結構描述不符問題發生的關鍵點。（[DeepSeek API 文檔][7]）

若您提供確切的錯誤訊息，我可以指出應放入設定的具體轉換器程式碼片段。

[1]: https://www.anthropic.com/engineering/claude-code-best-practices?utm_source=chatgpt.com "Claude Code：代理編碼最佳實踐"
[2]: https://openrouter.ai/docs/features/tool-calling?utm_source=chatgpt.com "工具與函數調用"
[3]: https://api-docs.deepseek.com/guides/function_calling?utm_source=chatgpt.com "函數調用"
[4]: https://github.com/musistudio/claude-code-router?utm_source=chatgpt.com "musistudio/claude-code-router"
[5]: https://claudelog.com/claude-code-mcps/claude-code-router/?utm_source=chatgpt.com "Claude Code 路由器"
[6]: https://openrouter.ai/models?q=deepseek&utm_source=chatgpt.com "模型：'deepseek'"
[7]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 發布"