---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Claude API 2025 收費詳解
translated: true
type: note
---

以下是 Anthropic Claude 各模型 API 使用費用的清晰說明——不使用表格，僅以簡潔易讀的文字呈現：

---

### Claude Sonnet 4

* **輸入 token：** 每百萬個收費 3 美元
* **輸出 token：** 每百萬個收費 15 美元
* **可用折扣：** 透過提示快取最高可享 **9 折** 優惠，批量處理最高可享 **5 折** 優惠。（[custom.typingmind.com][1]、[Reddit][2]、[Anthropic][3]、[Anthropic][4]）

---

### Claude 3.5 Sonnet（現已棄用）

* **輸入 token：** 每百萬個收費 3 美元
* **輸出 token：** 每百萬個收費 15 美元
* **批量與快取費率：** 與其他 Sonnet 版本相同的分層系統：批量輸入 1.50 美元，批量輸出 7.50 美元，5 分鐘快取命中 0.30 美元。（[Anthropic 文檔][5]）

---

### Claude 3.7 Sonnet

* **基礎定價：** 與 3.5 版本完全相同——輸入每百萬個 3 美元，輸出每百萬個 15 美元——包括使用混合「思考」模式時。（[Reddit][6]、[Anthropic 文檔][5]）

---

### Claude Opus 4

* **輸入 token：** 每百萬個收費 15 美元
* **輸出 token：** 每百萬個收費 75 美元
* **批量與快取折扣：** 批量輸入為 7.50 美元；批量輸出為 37.50 美元；快取命中成本為 1.50 美元。（[Anthropic][7]、[Amazon Web Services, Inc.][8]、[Anthropic 文檔][5]、[Wikipedia][9]）

---

### 快速總結

* **所有 Sonnet 變體（3.5、3.7、4）：** 輸入每百萬個 3 美元 / 輸出每百萬個 15 美元，批量處理和快取可享更深度折扣。
* **Opus 4：** 費率顯著更高，為每百萬個 15 / 75 美元，但針對深度推理、長時間任務和更高性能進行了優化。

---

### 補充見解

* **模型演進：** Claude 3.5 Sonnet 在 2024 年 6 月推出時，為編碼能力樹立了新標竿，但儘管性能提升，2025 年 2 月的 3.7 版本和 2025 年 5 月的 Sonnet 4 定價保持不變。（[Business Insider][10]、[Anthropic][7]、[Anthropic 文檔][5]、[Wikipedia][11]）
* **使用場景對應：** 若您的工作負載以對話為主或屬高流量型，Sonnet 模型能提供卓越的性價比。對於極度複雜的任務或長時間的代理工作流程，Opus 或混合使用兩者的策略可能更有效率。

---

如果您需要基於特定 token 數量的成本範例、快取比較，或選擇模型的指引，請隨時告知——我很樂意為您詳細說明！

[1]: https://custom.typingmind.com/tools/estimate-llm-usage-costs/claude-3.5-sonnet?utm_source=chatgpt.com "Anthropic claude-3.5-sonnet API 定價計算器"
[2]: https://www.reddit.com/r/ClaudeAI/comments/1jclyjp/can_anthropic_keep_up_with_those_pricing/?utm_source=chatgpt.com "Anthropic 能跟上這些定價嗎？: r/ClaudeAI"
[3]: https://www.anthropic.com/news/claude-3-5-sonnet?utm_source=chatgpt.com "介紹 Claude 3.5 Sonnet"
[4]: https://www.anthropic.com/claude/sonnet?utm_source=chatgpt.com "Claude Sonnet 4"
[5]: https://docs.anthropic.com/en/docs/about-claude/pricing?utm_source=chatgpt.com "定價"
[6]: https://www.reddit.com/r/ClaudeAI/comments/1ixtyj0/sonnet_37_x_cline_costs_are_skyrocketing/?utm_source=chatgpt.com "Sonnet 3.7 x Cline：成本飆升？: r/ClaudeAI"
[7]: https://www.anthropic.com/news/claude-3-7-sonnet?utm_source=chatgpt.com "Claude 3.7 Sonnet 與 Claude Code"
[8]: https://aws.amazon.com/marketplace/pp/prodview-h2mamlwah46ym?utm_source=chatgpt.com "AWS Marketplace: Claude 3.5 Sonnet (Amazon Bedrock 版)"
[9]: https://zh.wikipedia.org/wiki/Claude_%28%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%29?utm_source=chatgpt.com "Claude (語言模型)"
[10]: https://www.businessinsider.com/anthropic-ai-breakthrough-vibe-coding-revolution-2025-7?utm_source=chatgpt.com "『兆元問題』：Anthropic 如何讓 AI 在編碼上如此出色？"
[11]: https://en.wikipedia.org/wiki/Claude_%28language_model%29?utm_source=chatgpt.com "Claude (語言模型)"