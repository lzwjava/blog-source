---
audio: false
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: 修復LibreChat OpenRouter網絡搜尋錯誤
translated: true
type: note
---

使用 LibreChat 與 OpenRouter 的網路搜尋功能時出現 **「404 未找到支援工具使用的端點」** 錯誤是已知問題。以下是問題成因與解決方法：

---

## **問題成因**
- **並非所有 OpenRouter 上的模型都支援「工具使用」功能**（如網路搜尋、函數呼叫等）——僅部分模型支援。若選擇了不支援工具的模型，就會出現此 404 錯誤。
- OpenRouter 要求使用者**必須明確選擇支援工具/函數呼叫的模型**，才能正常使用網路搜尋等功能。
- LibreChat 的配置若未正確設定，也可能覆寫端點導致路由問題。

---

## **解決方法**

### 1. **選擇支援工具的模型**
- 前往 [OpenRouter 模型列表](https://openrouter.ai/models)，在側邊欄**勾選「tools」篩選條件**。只有標註工具支援的模型才能相容 LibreChat 的網路搜尋功能。
- 推薦模型：尋找標註支援「function calling」或「tools」的模型（例如部分 GPT-4、Claude 或其他進階模型版本）。

### 2. **更新 LibreChat 配置**
- **請勿在配置中使用 `OPENROUTER_API_KEY`**，否則可能覆寫 OpenAI 端點引發衝突。
- 在 `librechat.yaml` 中，請確認 OpenRouter 端點配置正確，且未被「Ignored Providers」封鎖或受「Allowed Providers」限制。

### 3. **解除供應商限制**
- 於 OpenRouter 設定中**解除所有「Ignored Providers」封鎖**，並**清空「Allowed Providers」**，確保 LibreChat 能存取所有可用端點。

### 4. **重啟 LibreChat**
- 完成上述調整後，請重啟 LibreChat 以套用新設定。

---

## **問題仍未解決？**
- 請查閱 [LibreChat 自訂端點說明文件](https://www.librechat.ai/docs/quick_start/custom_endpoints)瞭解進階設定。
- 若問題持續存在，可嘗試切換至官方 OpenAI API（若具備存取權限）或其他支援工具使用的服務供應商。