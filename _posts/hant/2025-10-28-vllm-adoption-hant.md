---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: AI 供應商採用 vLLM
translated: true
type: note
---

### AI 供應商使用 vLLM 的情況

vLLM 是一個開源推理引擎，常被推薦用於高效提供開源權重模型服務。然而，其在生產服務中的採用情況各不相同。以下是根據現有資訊整理的分析：

| 供應商/模型 | 是否在生產環境中使用 vLLM？ | 詳細資訊 |
|---------------|---------------------------|---------|
| **Claude (Anthropic)** | 否 | Anthropic 依賴專有基礎設施來提供 Claude 模型服務。vLLM 支援模擬 Anthropic API 的本地或第三方部署，但無證據顯示其內部使用 vLLM。 |
| **OpenAI (GPT 模型)** | 否 | OpenAI 使用自訂的內部服務系統進行規模化優化。vLLM 支援 OpenAI 相容的 API 用於本地推理，但 OpenAI 的生產環境並未基於 vLLM。 |
| **Minimax AI** | 否 | MiniMax 開源了如 MiniMax-M1/M2 等模型，並因效能考量推薦用戶部署時使用 vLLM。其核心生產 API 未確認使用 vLLM；可能使用分支版本或自訂設定。 |
| **Kimi (Moonshot AI)** | 否 | Moonshot 推薦自託管 Kimi-K2 時使用 vLLM，其 Checkpoint-Engine 工具也整合了 vLLM 以進行權重更新。然而，其生產推理可能在使用 SGLang 或 TensorRT-LLM 等引擎的同時，結合了專有優化技術。 |
| **DeepSeek AI** | 是 | DeepSeek 開源了一個直接基於 vLLM 構建的自訂推理引擎，並融入了其研究中的優化技術。該引擎用於 DeepSeek-V3 和 R1 等模型，且對 vLLM 專案有貢獻。 |

### 參考資料
- [DeepSeek 開源基於 vLLM 的自訂推理引擎](https://www.ainews.com/p/deepseek-open-sources-custom-inference-engine-built-on-vllm)
- [DeepSeek 開源推理引擎之路](https://news.ycombinator.com/item?id=43682088)
- [MiniMax-M1 混合架構與 vLLM 的結合](https://blog.vllm.ai/2025/06/30/minimax-m1.html)
- [Kimi K2：開放式代理智能](https://moonshotai.github.io/Kimi-K2/)
- [OpenAI 相容伺服器 - vLLM](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)
- [支援 Anthropic API `/v1/messages` 端點 · 議題 #21313 · vllm-project/vllm](https://github.com/vllm-project/vllm/issues/21313)