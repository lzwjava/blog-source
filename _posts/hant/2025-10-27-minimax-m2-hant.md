---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: MiniMax M2 開源人工智能模型
translated: true
type: note
---

### 什麼是 MiniMax M2？

MiniMax M2 是中國人工智能公司 MiniMax AI 最新發佈的開源大型語言模型（LLM），該公司專注於文本、音頻、圖像和視頻的基礎模型。此模型於數小時前（截至 2025 年 10 月 27 日）推出，採用混合專家（MoE）架構，專為編程和智能代理工作流程優化——設想能自主規劃、執行工具並處理複雜任務（如全端開發、數據分析或多步驟研究）的自主人工智能代理。它並非像 GPT 或 Claude 那樣的通用模型，但在端到端編程和代理應用方面表現卓越，並能與 Claude Code、Cursor 或瀏覽器/終端解釋器等工具無縫整合。

關鍵規格：
- **參數量**：總計 2300 億，但僅激活 100 億（以提升效率）。
- **上下文長度**：最高 128K tokens。
- **部署**：於 Hugging Face 以 MIT 許可證提供；支援 SGLang 和 vLLM 等框架供自行部署。
- **存取方式**：透過 MiniMax Agent（agent.minimax.io）提供免費 API 試用至 2025 年 11 月 7 日。付費 API 定價為每百萬輸入 tokens 0.30 美元、每百萬輸出 tokens 1.20 美元——約為 Claude 3.5 Sonnet 成本的 8%。

該模型採用「交錯思考」方法（使用 `