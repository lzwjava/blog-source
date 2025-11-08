---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GitHub Copilot 擴充功能更新摘要
translated: true
type: note
---

### GitHub Copilot Extension for VS Code (版本 1.388.0)

GitHub Copilot 擴充套件 1.388.0 版本於 2025 年 10 月 24 日發佈。這似乎是一個主要針對穩定性和相容性改進的小型更新，特別是針對最新 VS Code 版本 (1.105)。市集或 GitHub 部落格中未公開詳細的具體發佈說明，但用戶回報指出修復了一些問題，例如在行內生成期間出現的不必要程式碼插入，以及中止建議時出現的額外標籤補全。它與近期 Copilot 功能無縫整合，包括增強型代理模式和模型選擇。

#### 近 6 個月主要更新（2025 年 5 月至 10 月）
GitHub Copilot 的主要增強功能通常與每月 VS Code 發佈一同宣佈。以下是此期間該擴充套件及相關功能的重要更新摘要：

- **2025 年 10 月 (VS Code 1.105 / 擴充套件 ~1.388)**：
  - OpenAI Codex 整合現已在 VS Code Insiders 中提供給 Copilot Pro+ 訂閱者使用，可在編輯器中直接進行進階程式碼合成。
  - 新的「任務控制」介面，用於跨工作階段指派、引導和追蹤 Copilot 編碼代理任務。
  - 代理工作階段視圖擴展以支援 GitHub Copilot CLI，用於管理本地和雲端代理。

- **2025 年 9 月 (VS Code 1.104 / 擴充套件 ~1.38x)**：
  - 實驗性 GitHub Copilot-SWE 模型推廣至 VS Code Insiders，該模型針對程式碼編輯、重構和小型轉換進行了優化。它以任務為導向，可在任何聊天模式下工作；建議使用詳細提示以獲得最佳效果。
  - 改進了終端機錯誤的行內聊天，提供更好的解釋和修復方案。

- **2025 年 8 月 (VS Code 1.103 / 擴充套件 ~1.37x)**：
  - 增強了提交訊息建議，具備多行上下文感知能力，並與 @workspace 整合以生成整個專案結構。
  - 輕量級行內聊天升級，實現更快速的互動，無需開啟完整視圖。

- **2025 年 7 月 (VS Code 1.102 / 擴充套件 ~1.36x)**：
  - 透過單一提示更好地協調多檔案編輯，分析專案結構以實現一致的變更。
  - 棄用舊型號（部分 Claude、OpenAI 和 Gemini 變體），轉而使用更新、更快速的選項，如 GPT-4.1。

- **2025 年 6 月 (VS Code 1.101 / 擴充套件 ~1.35x)**：
  - 引入提示和指令檔案，用於透過可重複使用的指南和組織知識自訂 Copilot 的行為。
  - 擴展 GitHub Pull Requests 整合：直接從 VS Code 視圖將 PR/問題分配給 Copilot，並新增「Copilot on My Behalf」查詢以進行追蹤。

- **2025 年 5 月 (VS Code 1.100 / 擴充套件 ~1.34x)**：
  - 代理模式新增 Model Context Protocol (MCP) 支援，允許為第三方模型使用自訂 API 金鑰。
  - 由 OpenAI GPT-4.1 和 Anthropic Claude Sonnet 提供動力的更快速代理編輯，特別適用於大型檔案。
  - 儲存庫搜尋改進，用於語意程式碼發現和整個程式碼庫的建議。

這些更新強調了代理工作流程、模型效能以及與 VS Code 生態系統的無縫整合。有關完整的擴充套件歷史記錄，請查閱 VS Code 市集。主要公告通常與 VS Code 的每月更新週期相關聯。

[GitHub Copilot in VS Code gets upgraded](https://github.blog/changelog/2025-10-28-github-copilot-in-visual-studio-code-gets-upgraded/)  
[Copilot-SWE model rolling out to Visual Studio Code Insiders](https://github.blog/changelog/2025-09-22-copilot-swe-model-rolling-out-to-visual-studio-code-insiders/)  
[GitHub Copilot in VS Code April release (v1.100)](https://github.blog/changelog/2025-05-08-github-copilot-in-vs-code-april-release-v1-100/)  
[GitHub Copilot in VS Code March release (v1.99)](https://github.blog/changelog/2025-04-03-github-copilot-in-vs-code-march-release-v1-99/)  
[September 2025 (version 1.105) - Visual Studio Code](https://code.visualstudio.com/updates)  
[GitHub Copilot Marketplace Page](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)