---
audio: false
generated: true
image: false
lang: hant
layout: post
title: OpenRouter 與直接 API 成本比較
translated: true
type: note
---

是的，使用 OpenRouter API 存取相同模型通常比直接使用 DeepSeek、Mistral、Google（Gemini）或 xAI（Grok）等供應商的官方 API 成本更高。OpenRouter 聲稱會直接傳遞底層供應商的定價，不在推理成本上加價，但他們會收取額外費用從而增加總體開支：

- 透過標準支付方式購買點數時收取 5.5% 手續費（最低 0.80 美元），加密貨幣支付則額外增加 5% 費用
- 即使您自備支援供應商的 API 金鑰（BYOK），OpenRouter 仍會從您的點數中扣除 5% 費用（基於其預估模型成本）

這些費用實際上使 OpenRouter 比直接使用貴出 5-5.5%，另加固定最低收費（取決於使用量與支付方式）。直接存取可避免這些額外費用，因為您只需支付供應商的 token 費率。

### 成本比較範例
以下是根據現有定價數據的粗略比較（以每百萬 token 美元計；請注意費率可能因模型版本、時段、快取或區域而異——請務必查閱官方網站獲取最新資訊）。OpenRouter 的基礎 token 費率與供應商保持一致（直接傳遞），但會疊加上述費用。

- **DeepSeek**：
  - 直接存取：輸入約 0.14–0.55 美元（快取命中/未命中），輸出約 1.10–2.19 美元（因模型與折扣時段而異）
  - OpenRouter：相同基礎費率 + 5–5.5% 手續費

- **Mistral**：
  - 直接存取：輸入約 2.00 美元（Large 2 模型），輸出約 6.00 美元（基於混合費率估算；舊版模型如 Small 約為輸入 0.15 美元/輸出 0.50 美元）
  - OpenRouter：相同基礎費率 + 5–5.5% 手續費

- **Gemini（Google）**：
  - 直接存取：費率因模型差異甚大（例如 Gemini 1.5 Pro：輸入 1.25–2.50 美元，輸出 5.00–10.00 美元；Gemini 1.5 Flash：輸入 0.075–0.15 美元，輸出 0.30–0.60 美元）
  - OpenRouter：相同基礎費率 + 5–5.5% 手續費（Google 可能支援 BYOK）

- **Grok（xAI）**：
  - 有關 Grok API 定價與存取的詳細資訊，請造訪 https://x.ai/api。根據公開資訊，Grok-3/Grok-4 費率約為輸入 3.00 美元/輸出 15.00 美元，Grok-3-mini 則為輸入 0.30 美元/輸出 0.50 美元
  - OpenRouter：相同基礎費率 + 5–5.5% 手續費（xAI 通常未提及 BYOK）

若您的使用量屬於高頻率，這些百分比費用會快速累積。對於低用量或測試場景，差異可能不大，但直接存取仍更經濟實惠。OpenRouter 的價值在於其統一 API 與路由功能，這些便利性或許能合理化額外成本。

[OpenRouter 常見問答](https://openrouter.ai/docs/faq)  
[DeepSeek API 定價](https://api-docs.deepseek.com/quick_start/pricing)  
[Mistral AI 定價](https://mistral.ai/pricing)  
[Google Gemini API 定價](https://ai.google.dev/pricing)  
[xAI API](https://x.ai/api)  
[Mistral Large 2 分析報告](https://artificialanalysis.ai/models/mistral-large-2)  
[DeepSeek 定價指南](https://team-gpt.com/blog/deepseek-pricing/)