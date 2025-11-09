---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Claude Haiku 4.5 快速高效人工智能
translated: true
type: note
---

Claude Haiku 4.5 是 Anthropic 於 2025 年 10 月 16 日發布的最新小型 AI 模型。它專為速度與效率而設計，非常適合即時應用場景，例如聊天機械人、客戶服務代理和編程輔助。這款模型提供接近前沿模型的性能——在編程、電腦操作和代理工作流程等任務上，可媲美甚至超越舊版模型如 Claude Sonnet 4——同時速度顯著更快（超過兩倍）且成本更低（約三分之一）。

### 主要特性與功能
- **高速與低延遲**：針對互動場景（如配對編程或多代理系統）中的快速回應進行優化
- **擅長編程與工具操作**：在 SWE-bench（73.3% 分數）和 Terminal-Bench（約 41%）等基準測試中表現卓越，能處理檔案編輯或終端指令等複雜任務
- **多模型工作流程**：可與大型模型（如 Claude Sonnet 4.5）搭配使用，由大型模型規劃任務，Haiku 4.5 並行執行子任務
- **安全優先**：這是 Anthropic 迄今最安全的模型，有害輸出率低，歸類於 AI 安全等級 2（比前沿模型的等級 3 限制更少）。其行為失準情況甚至比 Sonnet 4.5 更少

與前代模型（Claude 3.5 Haiku）相比，它的對齊度與能力更高，可作為直接替換方案。它並非 Anthropic 絕對最新的前沿模型——那是由兩週前發布的 Claude Sonnet 4.5 擔綱——但 Haiku 4.5 是他們最新的小型模型，適合日常使用的成本效益升級方案。

### 定價與可用性
- **定價**：每百萬輸入 token 1 美元，每百萬輸出 token 5 美元
- **存取方式**：立即透過 Claude API（代號 `claude-haiku-4-5`）、Anthropic 應用程式、Amazon Bedrock、Google Vertex AI 及 GitHub Copilot 等整合向所有用戶開放

[介紹 Claude Haiku 4.5](https://www.anthropic.com/news/claude-haiku-4-5)  
[Anthropic 推出 Claude Haiku 4.5](https://www.cnbc.com/2025/10/15/anthropic-claude-haiku-4-5-ai.html)  
[AWS 上的 Claude Haiku 4.5](https://aws.amazon.com/about-aws/whats-new/2025/10/claude-4-5-haiku-anthropic-amazon-bedrock)