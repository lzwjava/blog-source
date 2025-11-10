---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 最佳轉錄清理指南型號
translated: true
type: note
---

絕佳應用場景。針對**需要嚴格格式且「杜絕多餘閒聊」的長篇逐字稿整理**，以下是在 OpenRouter 上目前最適合的解決方案，按使用情境分類。

**快速＋經濟的實用首選（英文/中文，長文件）：DeepSeek-V3.1**
擅長遵循指令，支援 128k 上下文長度，可根據需求開啟或關閉「思考」模式以平衡速度與精準度。在刪除贅詞與保持說話者標籤一致性方面，具備優秀的雙語處理能力。（[DeepSeek API 文檔][1], [OpenRouter][2]）

**中文為主的訪談與口語內容：Kimi K2 Instruct**
Moonshot 的 K2（混合專家模型）對中文俚語與語境掌握流暢，特別適合以中文為主的逐字稿，同時能保留專業術語原貌。（[OpenRouter][3]）

**編輯指令遵循度最高：Claude Sonnet (3.7/4)**
Anthropic 的 Sonnet 系列極擅長「僅輸出潤飾後文本，不含任何詮釋」，且對意義改動傾向保守——完美契合您對步驟清單的嚴格要求。若可用請優先選用 Sonnet 4；3.7 版本同樣表現出色。（[OpenRouter][4]）

**超長對話或單次全域處理：GPT-5**
當需要處理極長上下文且力求降低幻覺風險時，GPT-5 是 OpenRouter 上前沿模型中最穩健的選擇（標示支援極長上下文；具備強大致力與編輯能力）。適用於馬拉松式逐字稿或最終的「全域潤飾」階段。（[OpenRouter][5]）

**同樣強勁，但需留意成本結構：Gemini 2.5 Pro**
在邏輯推理與長上下文編輯方面非常可靠。雖適合用於文本潤飾，但請根據您的供應商路徑注意定價/配額限制。（[OpenRouter][6]）

---

### 實務調度方案（無表格版）

* **≤128k tokens，中英混合，速度優先：** DeepSeek-V3.1（非思考模式）。僅在段落結構混亂時切換至思考模式。（[DeepSeek API 文檔][1]）
* **主要為中文逐字稿：** Kimi K2 Instruct。（[OpenRouter][3]）
* **嚴格「編輯」行為（無註解）、法律/金融語調：** Claude Sonnet。（[OpenRouter][4]）
* **巨型檔案或最終單次全域潤飾：** GPT-5。（[OpenRouter][5]）

---

### 讓流程更穩健的快速程式碼調整

* **實現模型可選功能**：加入 `--model` 命令行參數；預設為 `deepseek-v3.1`。
* **依大小/語言自動路由**：偵測 token 數量與中文比例；中文為主時選 K2，龐大輸入時選 GPT-5，嚴格編輯模式時選 Claude。
* **思考模式開關**（DeepSeek）：在您的 OpenRouter 呼叫中增加參數，針對困難段落設定 `reasoning.enabled`。（[DeepSeek API 文檔][1]）
* **修復小錯誤**：移除殘留的 `print(".1f")`；並擴展說話者標籤的正則表達式，以允許 `A：`（全形冒號）及無空格變體。
* **防護機制**：若長度差異 >10%，自動重試並加入「勿刪減內容」提醒；若未偵測到 `A:`/`B:` 標籤，自動重試並加入「請標記說話者」提示。

如果您需要，我可以立即改寫您的腳本，加入 `--model` 參數與智能路由邏輯。

[1]: https://api-docs.deepseek.com/quick_start/pricing?utm_source=chatgpt.com "Models & Pricing"
[2]: https://openrouter.ai/deepseek/deepseek-chat-v3.1?utm_source=chatgpt.com "DeepSeek V3.1 - API, Providers, Stats"
[3]: https://openrouter.ai/moonshotai/kimi-k2?utm_source=chatgpt.com "Kimi K2 - API, Providers, Stats"
[4]: https://openrouter.ai/anthropic/claude-3.7-sonnet?utm_source=chatgpt.com "Claude 3.7 Sonnet - API, Providers, Stats"
[5]: https://openrouter.ai/openai/gpt-5?utm_source=chatgpt.com "GPT-5 - API, Providers, Stats"
[6]: https://openrouter.ai/google/gemini-2.5-pro?utm_source=chatgpt.com "Gemini 2.5 Pro - API, Providers, Stats"