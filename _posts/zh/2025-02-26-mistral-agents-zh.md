---
audio: false
generated: false
lang: zh
layout: post
title: Mistral AI 代理
translated: true
---

Mistral AI 代理是由大型语言模型（LLMs）驱动的自主系统，旨在根据高级指令执行复杂任务。利用先进的自然语言处理，这些代理可以理解和执行特定目标，使其适用于广泛的应用，如客户支持、数据分析、工作流自动化和编码辅助。它们可以规划、利用工具、采取行动，甚至协作以实现特定目标，提供新的自动化和智能水平。

---

## 创建代理

Mistral AI 提供两种主要方法来创建代理：**La Plateforme 代理构建器**和**代理 API**。

### 1. La Plateforme 代理构建器
代理构建器提供了一个用户友好的界面，无需广泛的技术知识即可创建代理。要创建代理：

- 导航到代理构建器：[https://console.mistral.ai/build/agents/new](https://console.mistral.ai/build/agents/new)。
- 通过选择模型、设置温度和提供可选指令来自定义代理。
- 配置完成后，代理可以通过 API 或 Le Chat 部署和访问。

### 2. 代理 API
对于开发者，代理 API 允许以编程方式创建和将代理集成到现有工作流中。以下是通过 API 创建和使用代理的示例：

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

## 自定义代理

Mistral AI 代理可以通过多种选项进行自定义以满足特定需求：

- **模型选择**：选择驱动代理的模型。选项包括：
  - "Mistral Large 2"（默认，`mistral-large-2407`）
  - "Mistral Nemo"（`open-mistral-nemo`）
  - "Codestral"（`codestral-2405`）
  - 微调模型

- **温度**：调整采样温度（在 0.0 和 1.0 之间）以控制代理响应的随机性。较高的值使输出更具创造性，而较低的值使其更加集中和确定性。

- **指令**：提供可选指令以在所有交互中强制执行特定行为。例如，您可以创建一个仅使用法语或生成不带解释的 Python 代码的代理。

### 示例：创建一个法语代理
要创建一个仅用法语回答的代理：
- 将模型设置为 "Mistral Large 2"。
- 使用指令，例如：“无论输入语言如何，始终用法语回答。”
- 提供少量示例以强化行为。

---

## 使用场景

Mistral AI 代理可以应用于各种行业和任务。一些显著的使用场景包括：

- **客户支持**：自动响应常见查询，处理常见问题并将复杂问题升级给人类代理。
- **数据分析**：创建代理以分析数据集、生成报告或根据用户输入执行计算。
- **工作流自动化**：将代理与电子邮件、CRM 系统或支付处理等工具集成，以自动化重复任务。
- **编码辅助**：设计代理以生成代码、提供调试建议或创建单元测试。

### 具体示例
- **法语代理**：配置为仅用法语回答的代理，适用于面向法语客户的企业。
- **Python 代码生成器**：生成不带解释的 Python 代码片段的代理，适用于需要快速、干净代码的开发人员。

---

## 部署

创建代理后，可以通过两种方式部署和访问：

- **API 集成**：使用 Mistral AI API 将代理集成到您的应用程序中。有关详细信息，请参阅“创建代理”部分的代码示例。
- **Le Chat**：切换选项以直接在 Mistral 的 Le Chat 平台上与代理聊天。

代理可以在组织内轻松共享，并且通过模型（如 Mistral Large 2）的高级推理能力，您可以构建涉及多个代理的复杂工作流。

---

本文档提供了一个全面的指南，帮助您了解、创建、自定义和部署 Mistral AI 代理，基于官方文档：[https://docs.mistral.ai/capabilities/agents/](https://docs.mistral.ai/capabilities/agents/)。通过利用这些工具，您可以自动化任务、提高生产力并在工作流中实现新的效率水平。有关更多详细信息，请探索 [Mistral AI 文档](https://docs.mistral.ai/capabilities/agents/)。