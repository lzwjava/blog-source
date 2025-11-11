---
audio: false
generated: true
lang: hant
layout: post
title: Mistral AI 代理
translated: true
type: note
---

Mistral AI 代理是基於大型語言模型（LLM）的自動化系統，專為執行複雜任務而設計，能根據高階指令運作。這些代理運用先進的自然語言處理技術，能夠理解並實現特定目標，適用於多種應用場景，例如客戶支援、數據分析、工作流程自動化及編程輔助。它們具備規劃能力、能運用工具、採取行動，甚至協作達成特定目標，提供全新層級的自動化與智能解決方案。

---

## 建立代理

Mistral AI 提供兩種主要方式建立代理：**La Plateforme 代理建構器**與**代理 API**。

### 1. La Plateforme 代理建構器
代理建構器提供直觀的用戶介面，無需深厚技術背景即可建立代理。建立步驟如下：

- 前往代理建構器：[https://console.mistral.ai/build/agents/new](https://console.mistral.ai/build/agents/new)
- 自訂代理：選擇模型、設定溫度參數，並可選擇性提供指令
- 設定完成後，代理可透過 API 或 Le Chat 進行部署與存取

### 2. 代理 API
開發者可透過代理 API，以程式化方式建立代理並整合至現有工作流程。以下為使用 API 建立與操作代理的範例：

#### Python 範例
```python
import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

chat_response = client.agents.complete(
    agent_id="your-agent-id",
    messages=[{"role": "user", "content": "What is the best French cheese?"}],
)
print(chat_response.choices[0].message.content)
```

#### JavaScript 範例
```javascript
import { Mistral } from '@mistralai/mistralai';

const apiKey = process.env.MISTRAL_API_KEY;
const client = new Mistral({ apiKey: apiKey });

const chatResponse = await client.agents.complete({
    agentId: "your-agent-id",
    messages: [{ role: 'user', content: 'What is the best French cheese?' }],
});
console.log('Chat:', chatResponse.choices[0].message.content);
```

---

## 自訂代理

Mistral AI 代理可透過以下選項進行客製化，以符合特定需求：

- **模型選擇**：選擇驅動代理的模型。選項包括：
  - "Mistral Large 2"（預設值，`mistral-large-2407`）
  - "Mistral Nemo"（`open-mistral-nemo`）
  - "Codestral"（`codestral-2405`）
  - 微調模型

- **溫度參數**：調整取樣溫度（範圍 0.0 至 1.0）以控制代理回應的隨機性。數值越高輸出越具創造性，數值越低則越專注與確定。

- **指令設定**：提供選擇性指令以規範所有互動中的特定行為。例如可建立僅用法語交談，或直接生成 Python 代碼不解釋的代理。

### 範例：建立法語專用代理
建立僅用法語回應的代理：
- 將模型設為 "Mistral Large 2"
- 使用指令如：「無論輸入為何種語言，一律用法語回應」
- 提供少量範例以強化行為模式

---

## 應用場景

Mistral AI 代理可應用於各產業與任務，重要應用場景包括：

- **客戶支援**：自動回應常見查詢、處理常見問題，並將複雜問題轉交真人客服
- **數據分析**：建立能分析數據集、生成報告或根據用戶輸入執行計算的代理
- **工作流程自動化**：整合電子郵件、CRM 系統或支付處理等工具，自動化重複性任務
- **編程輔助**：設計能生成代碼、提供除錯建議或建立單元測試的代理

### 具體範例
- **法語專用代理**：設定僅用法語回應的代理，適用於服務法語客群的企業
- **Python 代碼生成器**：直接輸出 Python 代碼片段的代理，適合需要快速獲取簡潔代碼的開發者

---

## 部署方式

代理建立後可透過兩種方式部署與存取：

- **API 整合**：使用 Mistral AI API 將代理整合至應用程式，詳見「建立代理」章節的程式範例
- **Le Chat**：啟用選項後可直接在 Mistral 的 Le Chat 平台與代理對話

代理可輕鬆在組織內共享，搭配 Mistral Large 2 等模型的進階推理能力，更能建立涉及多個代理的複雜工作流程。

---

本文件提供理解、建立、自訂與部署 Mistral AI 代理的完整指南，內容基於官方文件 [https://docs.mistral.ai/capabilities/agents/](https://docs.mistral.ai/capabilities/agents/)。透過運用這些工具，您可自動化任務、提升生產力，並為工作流程開創更高效率。更多詳細資訊請參閱 [Mistral AI 官方文件](https://docs.mistral.ai/capabilities/agents/)。