---
audio: false
generated: false
lang: hant
layout: post
title: Mistral AI 代理
translated: true
---

Mistral AI Agents 是由大型語言模型（LLMs）驅動的自主系統，旨在根據高層指令執行複雜任務。利用先進的自然語言處理技術，這些代理可以理解和執行具體目標，使其適合廣泛應用，如客戶支持、數據分析、工作流自動化和編碼協助。它們可以規劃、利用工具、採取行動，甚至協作以實現具體目標，提供新的自動化和智能水平。

---

## 創建代理

Mistral AI 提供兩種主要方法來創建代理：**La Plateforme Agent Builder** 和 **Agent API**。

### 1. La Plateforme Agent Builder
Agent Builder 提供一個用戶友好的界面，無需廣泛的技術知識即可創建代理。要創建代理：

- 導航到 Agent Builder：[https://console.mistral.ai/build/agents/new](https://console.mistral.ai/build/agents/new)。
- 通過選擇模型、設置溫度和提供可選指令來自定義代理。
- 配置完成後，代理可以部署並通過 API 或 Le Chat 訪問。

### 2. Agent API
對於開發者，Agent API 允許以編程方式創建代理並將其集成到現有的工作流中。以下是通過 API 創建和使用代理的示例：

#### Python 示例
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

#### JavaScript 示例
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

## 自定義代理

Mistral AI 代理可以通過多種選項進行自定義以滿足具體需求：

- **模型選擇**：選擇驅動代理的模型。選項包括：
  - "Mistral Large 2"（默認，`mistral-large-2407`）
  - "Mistral Nemo"（`open-mistral-nemo`）
  - "Codestral"（`codestral-2405`）
  - 微調模型

- **溫度**：調整採樣溫度（在 0.0 和 1.0 之間）以控制代理回應的隨機性。較高的值使輸出更具創意，而較低的值使其更集中和確定性。

- **指令**：提供可選指令以在所有交互中強制執行特定行為。例如，您可以創建一個僅說法語或生成不帶解釋的 Python 代碼的代理。

### 示例：創建一個說法語的代理
要創建一個僅以法語回應的代理：
- 將模型設置為 "Mistral Large 2"。
- 使用指令，例如："無論輸入語言如何，始終以法語回應。"
- 提供少量示例以強化行為。

---

## 使用案例

Mistral AI 代理可以應用於各種行業和任務。一些顯著的使用案例包括：

- **客戶支持**：自動回應常見查詢，處理常見問題並將複雜問題升級給人工代理。
- **數據分析**：創建代理以分析數據集、生成報告或根據用戶輸入執行計算。
- **工作流自動化**：將代理與電子郵件、CRM 系統或支付處理等工具集成，以自動化重複任務。
- **編碼協助**：設計代理以生成代碼、提供調試建議或創建單元測試。

### 具體示例
- **說法語的代理**：配置為僅以法語回應的代理，適用於針對法語客戶的企業。
- **Python 代碼生成器**：生成不帶解釋的 Python 代碼片段的代理，適合需要快速、乾淨代碼的開發人員。

---

## 部署

創建代理後，可以通過兩種方式部署和訪問：

- **API 集成**：使用 Mistral AI API 將代理集成到您的應用程序中。有關詳細信息，請參閱 "創建代理" 部分的代碼示例。
- **Le Chat**：切換選項以直接在 Mistral 的 Le Chat 平台上與代理聊天。

代理可以在組織內輕鬆共享，並且通過像 Mistral Large 2 這樣的模型的先進推理能力，您可以構建涉及多個代理的複雜工作流。

---

本文檔提供了理解、創建、自定義和部署 Mistral AI 代理的全面指南，基於 [https://docs.mistral.ai/capabilities/agents/](https://docs.mistral.ai/capabilities/agents/) 的官方文檔。通過利用這些工具，您可以自動化任務、提高生產力並在工作流中實現新的效率水平。有關更多詳細信息，請探索 [Mistral AI 文檔](https://docs.mistral.ai/capabilities/agents/)。