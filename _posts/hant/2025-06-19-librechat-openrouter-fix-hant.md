---
audio: false
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: 修復LibreChat OpenRouter模型錯誤
translated: true
type: note
---

此錯誤發生於使用 **LibreChat** 並以 **OpenRouter** 作為後端時，所選模型（如 `gpt-5-chat` 或類似型號）無法使用或未正確路由。以下是問題分析與解決方法：

---

## **錯誤發生原因**
- **OpenRouter** 作為各類 AI 模型的代理服務，但並非所有模型都預設可用或啟用。
- 錯誤訊息 `404 未找到支援工具使用的端點` 表示您選擇的模型（`gpt-5-chat`）可能：
  - 不受 OpenRouter 支援
  - 未在 LibreChat 設定中配置
  - 需要其他供應商或 API 金鑰

---

## **解決方法**

### 1. **檢查 OpenRouter 可用模型**
- 前往 [OpenRouter 模型列表](https://openrouter.ai/models) 查看可用模型。
- 截至目前，`gpt-5-chat` 並非官方 OpenAI 模型（最新為 GPT-4o）。若您原意是使用 GPT-4，請改用 `openai/gpt-4` 或類似模型。

### 2. **更新 LibreChat 配置**
- 在 LibreChat 中前往 **設定** > **模型選擇**。
- 選擇 **受 OpenRouter 支援** 的模型（例如 `openai/gpt-4`、`mistralai/mistral-7b` 等）。
- 若需直接使用 OpenAI，請將 **API 供應商** 切換為 **OpenAI** 而非 OpenRouter。

### 3. **驗證 API 金鑰**
- 確認您擁有有效的 **OpenRouter API 金鑰**（若使用 OpenRouter）或 **OpenAI API 金鑰**（若使用 OpenAI）。
- 在 LibreChat 的 **設定** > **API 金鑰** 中添加金鑰。

### 4. **重新啟動 LibreChat**
- 變更設定後，請重新啟動 LibreChat 以套用變更。

### 5. **查閱 LibreChat 文件**
- 參考 [LibreChat 的 OpenRouter 設定指南](https://github.com/danny-avila/LibreChat#openrouter) 獲取詳細說明。

---

## **替代方案**
- 若需使用 OpenAI 模型，請將供應商設為 **OpenAI** 並選擇 `gpt-4`、`gpt-4o` 或 `gpt-3.5-turbo`。
- 若需使用 OpenRouter，請從其 [支援列表](https://openrouter.ai/models) 中挑選模型。

---