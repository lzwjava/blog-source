---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 最佳廉價編碼模型經由OpenRouter
translated: true
type: note
---

### 透過 OpenRouter 使用 Codex CLI 編程的最佳廉價模型

根據 2025 年最新的基準測試、用戶討論和模型排名，以下是一些在 Codex CLI 中進行編程任務時，可替代 GPT-5-Codex 的最佳且最經濟實惠的選擇。GPT-5-Codex 確實價格昂貴（根據供應商不同，通常每百萬 token 的輸入/輸出費用範圍在 20-50 美元 / 60-150 美元），因此這裡重點關注具有強大編程性能且成本效益高的選項。OpenRouter 的按使用量付費模式意味著您只需為處理的 token 付費，許多模型提供免費層級或極低的費率（每百萬 token 的輸入/輸出合計費用低於 1 美元）。

我優先考慮在 SWE-Bench、HumanEval 或 Aider 等編程基準測試中得分高，同時價格低廉或免費的模型。模型 ID 已格式化，方便您用於 `config.toml`（例如 `model = "provider/model-name"`）。關於確切的當前價格，請查閱 OpenRouter 的模型頁面，因為費率可能會有輕微波動。

#### 頂級推薦：
- **Grok Code Fast (xAI)**  
  模型 ID：`xai/grok-code-fast`  
  推薦理由：在 OpenRouter 的 LLM 編程排名中位居榜首，在速度和代理任務方面表現出色（例如，在國際信息學奧林匹克中排名第一）。基本使用通常免費，使其成為該平台上使用最多的模型。非常適合迭代式編程工作流程。  
  價格：免費或約 $0.50/$2.00 每百萬 token（輸入/輸出）。上下文：128K token。

- **Kat Coder Pro (KwaiPilot)**  
  模型 ID：`kwaipilot/kat-coder-pro:free`  
  推薦理由：專用編程模型，在 SWE-Bench Verified 上達到 73.4%，接近頂級專有模型。限時免費，非常適合複雜推理和代碼生成。  
  價格：免費（促銷期）。上下文：256K token，輸出最高 32K。

- **DeepSeek Coder V3 (DeepSeek)**  
  模型 ID：`deepseek/deepseek-coder-v3`  
  推薦理由：性價比極高，在 Aider 編程評分中約為 71%，在實現和調試方面表現強勁。論壇中常被推薦用於預算編程。  
  價格：非常便宜（約 $0.14/$0.28 每百萬）。上下文：128K token。

- **Llama 4 Maverick (Meta)**  
  模型 ID：`meta/llama-4-maverick`  
  推薦理由：免費層級中編程質量和 VS Code 集成（例如與 RooCode 等工具）的最佳選擇。在實際代碼任務中表現良好。  
  價格：提供免費層級，或低成本（約 $0.20/$0.80 每百萬）。上下文：128K token。

- **Mistral Devstral Small (Mistral)**  
  模型 ID：`mistral/devstral-small`  
  推薦理由：針對價格、高吞吐量和良好的代碼實現能力進行了優化。常與大型模型配對用於混合工作流程。  
  價格：便宜（約 $0.25/$1.00 每百萬）。上下文：128K token。

- **Qwen3 235B (Qwen)**  
  模型 ID：`qwen/qwen3-235b`  
  推薦理由：在編程基準測試中表現出色，推薦用於成本優化設置。能很好地處理大規模代碼項目。  
  價格：經濟實惠（約 $0.50/$2.00 每百萬）。上下文：128K token。

- **Gemini 2.5 Flash (Google)**  
  模型 ID：`google/gemini-2.5-flash`  
  推薦理由：排名第三，對於迭代編程快速且成本低。如果您的代碼涉及數據可視化，則非常適合多模態任務。  
  價格：便宜（約 $0.35/$1.05 每百萬）。上下文：1M token。

這些模型與 OpenAI 兼容，因此在將供應商設置為 "openrouter" 並配置您的 API 密鑰後，它們將在 Codex CLI 中無縫工作。可以先從 Grok Code Fast 或 Kat Coder 等免費模型開始測試。對於編程特定用途，請查看 SWE-Bench 分數——分數越高表示解決真實 GitHub 問題的能力越強。如果您需要更多上下文或速度，可以結合使用 OpenRouter 的路由功能，自動回退到更便宜的模型。

集成方法：在您的 `config.toml` 中，添加一個配置檔，例如 `[profiles cheap-coder]`，其中包含 `model_provider = "openrouter"` 和 `model = "上述 ID 之一"`。

[2025 年 OpenRouter 頂級 AI 模型：性能與成本指南](https://www.teamday.ai/blog/top-ai-models-openrouter-2025)  
[2025 年最佳預算編程 LLMs：DeepSeek R1 vs Gemini vs GPT](https://llmx.de/blog/budget-coding-llms-2025/)  
[在 OpenRouter 上可用於編程的最佳 LLMs 是什麼](https://medium.com/@okreitz/what-are-the-best-llms-available-on-openrouter-to-use-for-coding-with-kilo-ca04e75a84ee)  
[您可以在 OpenRouter 上使用的最佳免費 AI 模型](https://apidog.com/blog/free-ai-models/)  
[2025 年頂級 AI 編程模型](https://www.veerotech.net/blog/top-ai-coding-models-in-2025-boost-your-development-workflow-with-these-game-changers/)  
[LLM 排名 - OpenRouter](https://openrouter.ai/rankings)  
[2025 年 3 月五大 AI 編程模型](https://dev.to/apipie-ai/top-5-ai-coding-models-of-march-2025-5f04)  
[模型 - OpenRouter](https://openrouter.ai/models)  
[openrouter 上最好的編程模型是什麼？ - Reddit](https://www.reddit.com/r/RooCode/comments/1kdu7we/whats_the_best_coding_model_on_openrouter/)