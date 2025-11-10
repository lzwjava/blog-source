---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修復 Copilot 聊天驗證錯誤
translated: true
type: note
---

該錯誤通常意味著 **GitHub Copilot Chat** 無法找到有效的驗證令牌，因此無法與 Copilot 服務通訊。
這不是編碼錯誤 — 這是 **驗證/配置** 問題。

以下是根據您使用 Copilot Chat 的位置逐步解決方法：

---

### 1. 確保您已使用啟用 Copilot 的帳戶登入

* 在 **VS Code** 或 **JetBrains** IDE 中：

  1. 開啟命令選擇區 (**Ctrl+Shift+P** / **Cmd+Shift+P**)。
  2. 搜尋 **「GitHub: Sign in」**。
  3. 按照登入流程操作（它將開啟瀏覽器進行授權）。
  4. 確保您登入的帳戶擁有 **有效的 GitHub Copilot 訂閱**。
* 在 **Neovim CLI** (`copilot.vim` 或 `copilot.lua`) 中：

  * 執行 `:Copilot sign in` 並在瀏覽器中跟隨連結。

---

### 2. 檢查 GitHub Copilot Chat 是否已啟用

* 在 VS Code 中：

  * 前往 **擴充功能** → 搜尋「GitHub Copilot Chat」→ 確保它已安裝並啟用。
  * 設定 → 搜尋「Copilot Chat: Enabled」→ 將其開啟。

---

### 3. 重新整理驗證令牌

有時令牌會過期或遺失（特別是當您更改網路、更新 IDE 或切換帳戶時）。

* VS Code：

  1. 命令選擇區 → **「GitHub Copilot: Sign out」**。
  2. 然後再次 **「GitHub Copilot: Sign in」**。
* CLI：

  * 刪除令牌檔案（例如 `~/.config/github-copilot/hosts.json`）並重新登入。

---

### 4. 檢查網路 / 防火牆限制

* 如果您使用企業 VPN 或防火牆，GitHub Copilot 可能被阻止訪問其 API。
* 允許訪問 `github.com`、`api.githubcopilot.com` 和 `copilot-proxy.githubusercontent.com`。

---

### 5. 更新您的 IDE 和 Copilot 擴充功能

* 過時的 VS Code 或 Copilot 擴充功能版本有時會導致此問題。
* 更新兩者，然後重新啟動您的 IDE。

---

💡 如果您修復了驗證但仍然看到錯誤，GitHub Copilot Chat 還需要 **Copilot Chat 功能訪問權限** — 某些帳戶擁有 Copilot 編碼功能，但 **沒有 Chat** 功能，除非在設定中明確啟用。

---

如果您需要，我可以提供 **確切的 VS Code 命令序列** 來完全重設 Copilot Chat 的驗證，以便它重新提示您。您希望我準備這個嗎？