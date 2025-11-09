---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: SuperCLUE：中文大型語言模型基準測試
translated: true
type: note
---

SuperCLUE 是一個旨在評估中文大型語言模型（LLMs）的綜合基準測試套件。它基於原有的 CLUE（中文語言理解評估）基準，擴展至評估 LLMs 的高階能力，而不僅限於小型模型。SuperCLUE 由 CLUEbenchmark 團隊開發——該團隊是由清華大學等機構研究人員及中國 AI 生態圈企業共同協作的成果——於 2023 年首次推出，旨在解決中文 LLMs 在國際標準評估中的不足之處。

### 主要特點
- **重點領域**：從四個主要象限評估模型：
  - 語言理解與生成（例如：閱讀理解、摘要生成）
  - 專業技能與知識（例如：數學推理、編程）
  - 智能代理能力（例如：工具使用、規劃）
  - 安全性（例如：偏見檢測、倫理對齊）
- **結構**：劃分為 12 項核心任務，包含如 SuperCLUE-Math6 等多步驟數學題數據集
- **目的**：協助追蹤中國 AI 發展進程，突顯與全球模型（如 GPT 系列）相比的優勢（例如：文化細微處理）與差距
- **更新**：截至 2025 年中，該基準被用於定期檢視，排行榜顯示如 Qwen 和 GLM 等中文模型與國際模型的差距正在縮小

此基準為開源項目並持續維護，評估結果通常透過 arXiv 論文與 GitHub 分享。

[SuperCLUE：一個綜合性中文大型語言模型基準](https://arxiv.org/abs/2307.15020)  
[SuperCLUE GitHub 儲存庫](https://github.com/CLUEbenchmark/SuperCLUE)  
[ChinAI：SuperCLUE 基準——2025 年中檢視](https://chinai.substack.com/p/chinai-324-superclue-large-model)