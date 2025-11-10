---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Amp：先進人工智能編碼工具
translated: true
type: note
---

Sourcegraph 的 Amp 是一款智能編碼工具，專為開發者充分發揮先進 AI 模型能力而設計。其獨特之處在於：

- **無限制 Token 使用**：有別於其他限制 token 用量的 AI 編碼工具，Amp 無限制地使用頂級模型（如 Claude Sonnet 4），能實現高品質程式碼生成與複雜任務執行，讓嚴肅的開發工作更具成本效益。[](https://ampcode.com/manual)[](https://www.stackhawk.com/blog/secure-code-with-amp-by-sourcegraph/)

- **無縫整合**：Amp 以 VS Code 擴充功能（兼容 Cursor、Windsurf 及 VSCodium 等分支版本）及 CLI 工具模式運作，無需更換介面即可融入現有工作流程，並支援企業環境中的代理伺服器與自訂憑證。[](https://ampcode.com/manual)[](https://www.npmjs.com/package/%40sourcegraph/amp)

- **協作功能**：透過執行緒共享與排行榜機制，Amp 讓團隊能共同協作、重複使用成功工作流程並追蹤採用情況，有效促進團隊合作與生產力提升。[](https://sourcegraph.com/amp)[](https://ampcode.com/manual)

- **情境管理**：Amp 能智能選取相關程式碼片段作為情境參考，避免 token 用量膨脹的同時確保 AI 獲得足夠資訊來生成精準程式碼，此特性使其有別於 Sourcegraph 舊版產品 Cody 需讀取整個程式庫的運作方式。[](https://zoltanbourne.substack.com/p/early-preview-of-amp-the-new-ai-coding)[](https://www.reddit.com/r/cursor/comments/1kpin6e/tried_amp_sourcegraphs_new_ai_coding_agent_heres/)

- **安全防護**：Amp 具備指令白名單功能，可控制 AI 能執行的 CLI 指令並儲存於專案設定中，同時配備自動敏感資訊遮蔽機制防止資料外洩，更支援企業用戶的零資料保留政策。[](https://zoltanbourne.substack.com/p/early-preview-of-amp-the-new-ai-coding)[](https://ampcode.com/security)

- **強大自動化**：Amp 能處理自主推理、全面程式碼編輯與複雜任務，據稱可為部分用戶完成 70-80% 的編碼工作。其「待辦事項」即時更新功能更提供動態進度追蹤，大幅提升使用體驗。[](https://ainativedev.io/news/sourcegraphs-amp-dropped)[](https://medium.com/%40jonathanaraney/1-month-with-amp-vs-1-year-with-cursor-15572fca36ee)

- **企業導向**：Amp Enterprise 提供單一登入、批量折扣與發票支付等企業採購方案，適合組織大規模部署。其設計能配合 AI 加速開發趨勢擴展，並整合 StackHawk 等安全工具進行漏洞檢測。[](https://sourcegraph.com/pricing)[](https://www.stackhawk.com/blog/secure-code-with-amp-by-sourcegraph/)

- **社群好評**：開發者特別讚賞 Amp 的速度、準確性與任務完成效率，普遍認為表現超越 Cursor 或 Claude Code 等競爭產品。用戶對其注重成果品質與體貼的 UX 設計（如「待辦事項」功能）給予高度評價。[](https://sourcegraph.com/amp)[](https://ampcode.com/)

不過有用戶指出其基點數的定價模式可能所費不貲，成本與 LLM 使用量及網路搜索等附加工具連動。例如有用戶回報生成 2,000 行程式碼即花費 4 美元。[](https://www.reddit.com/r/ClaudeAI/comments/1ll0kow/sourcegraph_cody_discontinued_replaced_by_cody/)

Amp 現可於 ampcode.com 註冊使用，新用戶可獲 10 美元免費點數（企業版入門用戶另享 30 美元額外點數）。詳細定價請參閱 https://x.ai/grok 或聯絡 amp-billing-help@sourcegraph.com。[](https://ampcode.com/manual)[](https://sourcegraph.com/blog/changes-to-cody-free-pro-and-enterprise-starter-plans)