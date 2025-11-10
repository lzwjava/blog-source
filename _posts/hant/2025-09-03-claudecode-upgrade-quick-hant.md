---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 立即快速升級Claude代碼
translated: true
type: note
---

如果你想**升級 Claude Code**（Anthropic 推出的命令行編碼代理），以下是操作步驟——讓你能順利使用最新功能，例如學習模式與自訂子代理。

---

### 如何升級 Claude Code

1. **檢查當前版本**
   執行：

   ```
   claude --version
   ```

   這可查看你目前運行的版本。

2. **透過 npm 更新**
   最簡單的升級方式是：

   ```
   npm install -g @anthropic-ai/claude-code@latest
   ```

   這會從 npm 下載最新版本。
   Reddit 用戶回報此舉修復了錯誤並提升了響應速度。有人寫道：

   > 「更新到最新版本 (1.0.18) 後，簡直是天壤之別——感覺更聰明且反應更快。」
   > ([Reddit][1], [Anthropic][2])

3. **或者，使用原生安裝程式 (Beta)**
   若你偏好獨立二進位檔案（而非 npm），可嘗試：

   ```
   curl -fsSL https://claude.ai/install.sh | bash -s latest
   ```

   （Windows 用戶請使用 PowerShell 版本）
   ([Anthropic][3])

4. **驗證更新**
   安裝完成後，重啟終端機並再次執行 `claude --version` 以確認新版本已啟用。

5. **疑難排解安裝問題**
   若遇到問題，可先嘗試解除安裝：

   ```
   npm uninstall -g @anthropic-ai/claude-code
   npm install -g @anthropic-ai/claude-code
   ```

   部分用戶發現此順序能解決更新異常。([Anthropic][4], [Reddit][1], [Anthropic][5], [The Verge][6])

---

### 近期更新有哪些新功能？

#### 學習模式

Anthropic 近期在 Claude Code 中新增了兩種學習風格：**「解釋型」**與**「學習型」**。這些模式能幫助你理解生成程式碼背後的邏輯，而非僅提供解決方案。啟用方式如下：

1. 確保已更新 Claude Code。
2. 在 Claude Code 工作階段中執行 `/output-styles`。
3. 選擇 **預設**、**解釋型** 或 **學習型** 風格。
   此功能於 **2025 年 8 月 14 日** 推出。([Tom's Guide][7])

#### 自訂子代理

Claude Code 現支援 **子代理**——專為特定任務（例如錯誤修復、重構程式碼、文件編寫）量身打造的專屬 AI 助手。你可為每個子代理設定不同的系統提示、工具權限與上下文視窗。
設定步驟如下：

1. 執行 `/agents`
2. 選擇「建立新代理」（可設為用戶層級或專案層級）
3. 定義其行為、允許使用的工具並儲存設定
   子代理有助於保持工作流程更清晰、專注且具情境感知能力。([Anthropic][8])

---

### 快速回顧（無表格，僅清晰步驟）

* **升級方式**：

  ```
  npm install -g @anthropic-ai/claude-code@latest
  ```

  或使用原生安裝指令 `curl | bash -s latest`。

* **啟用學習模式**：

  * 完成更新
  * 在 Claude Code 中：執行 `/output-styles` 並選擇模式。

* **建立子代理**：

  * 在 Claude Code 中：執行 `/agents`
  * 自訂工具存取權限、系統提示與行為設定。

---

### 總結

升級 Claude Code 十分簡單——使用 npm 或原生安裝程式，確認已更新至最新版本，接著探索新的**學習模式**與**子代理**功能。這些新增功能將 Claude Code 從單純的編碼助手，轉變為更像開發工作流程中的教學夥伴與能動協作者。

若你需要協助建立第一個子代理或有效運用學習模式，我很樂意為你逐步講解！

[1]: https://www.reddit.com/r/ClaudeAI/comments/1l8gbfo/dont_forget_to_update_your_claude_cli_it_makes_a/?utm_source=chatgpt.com "Don't forget to update your Claude CLI! It makes a huge ..."
[2]: https://www.anthropic.com/solutions/agents?utm_source=chatgpt.com "Claude Agents | Intelligent AI Solutions \ Anthropic"
[3]: https://docs.anthropic.com/en/docs/claude-code/quickstart?utm_source=chatgpt.com "Quickstart - Claude Code"
[4]: https://docs.anthropic.com/en/docs/claude-code/settings?utm_source=chatgpt.com "Claude Code settings"
[5]: https://docs.anthropic.com/en/docs/claude-code/overview?utm_source=chatgpt.com "Claude Code overview"
[6]: https://www.theverge.com/2024/11/25/24305774/anthropic-model-context-protocol-data-sources?utm_source=chatgpt.com "Anthropic launches tool to connect AI systems directly to datasets"
[7]: https://www.tomsguide.com/ai/claudes-new-learning-modes-take-on-chatgpts-study-mode-heres-what-they-do?utm_source=chatgpt.com "Claude's new 'learning modes' take on ChatGPT's Study Mode - here's what they do"
[8]: https://docs.anthropic.com/en/docs/claude-code/sub-agents?utm_source=chatgpt.com "Subagents"