---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 停用 Claude Code 快取
translated: true
type: note
---

在 **Claude Code** 中，這段程式碼片段

```json
"cache_control": {
  "type": "ephemeral"
}
```

表示模型產生的回應（或成品）**不會被快取以供重複使用**。

### 存在原因

通常情況下，Claude Code（及其他 Anthropic SDK）可能會快取回應，以便在您再次發送相同提示時加快處理速度。但當您設定 `"cache_control": { "type": "ephemeral" }` 時，即是在告訴 API：

* **不要將此結果儲存在快取中**
* 如果後續出現相同的請求，**不要重複使用**該結果
* 將回應視為**短暫存在**——僅限本次呼叫使用

### 使用時機

這在以下情況特別有用：

* 您的請求包含**敏感或個人資料**，不希望被快取
* 您正在發送**一次性查詢**，這類查詢無法從重複使用中受益
* 您希望每次都能獲得**全新的輸出**，即使請求內容完全相同

簡而言之，`"ephemeral"` 使得 Claude 的輸出成為*暫時性*的——僅在本次互動中有效，不會在不同呼叫之間進行快取。

您是否還需要我解釋這與 Claude Code 中預設 `cache_control` 行為的差異（例如 `type: "default"`、`"none"` 與 `"ephemeral"` 的區別）？