---
audio: false
generated: true
image: false
lang: hant
layout: post
title: GitHub Copilot API 橋接器
translated: true
type: note
---

您已進入 **ericc-ch/copilot-api**，這是一個將 **GitHub Copilot** 轉變為本地 API 伺服器的 GitHub 專案，兼容 **OpenAI** 和 **Anthropic**（例如 Claude）API。

以下為清晰說明——無需表格，直接講解：

---

### 這是什麼？

* 這是一個**逆向工程代理**，讓您能透過熟悉的 OpenAI 風格端點（如 `/v1/chat/completions`、`/v1/models` 和 `/v1/embeddings`）與 GitHub Copilot 互動。您亦可使用 Anthropic 兼容端點，例如 `/v1/messages`（[GitHub][1]）。

* 本質上，這讓支援 OpenAI 或 Anthropic API 的工具（如 Claude Code）能使用 GitHub Copilot 作為其後端（[GitHub][1]）。

---

### 主要功能

* **OpenAI 與 Anthropic 兼容性**：運作方式與真實的 OpenAI 或 Anthropic API 相同（[GitHub][1]）。
* **Claude Code 整合**：準備好透過 `--claude-code` 標記接入 Claude Code（[GitHub][1]）。
* **使用量儀表板**：透過內建網頁界面監控您的 Copilot API 使用量與配額（[GitHub][1]）。
* **速率限制與審核控制**：包含速率限制（`--rate-limit`）、自動等待（`--wait`）、手動審核（`--manual`）和除錯（顯示 token）選項——有助於避開 GitHub 的濫用偵測系統（[GitHub][1]）。
* **支援多種 Copilot 方案**：個人、企業或組織帳戶皆可使用（[GitHub][1]）。

---

### 設定與使用

* **先決條件**：您需要 Bun（≥ 1.2.x）和 GitHub Copilot 訂閱（[GitHub][1]）。
* **安裝選項**：

  * **Docker**：

    ```bash
    docker build -t copilot-api .
    docker run -p 4141:4141 -v $(pwd)/copilot-data:/root/.local/share/copilot-api copilot-api
    ```

    或透過 `GH_TOKEN` 直接傳入您的 GitHub token（[GitHub][1]）。
  * **npx**：

    ```bash
    npx copilot-api@latest start --port 8080
    ```

    或僅執行 `npx copilot-api@latest auth` 進行身份驗證（[GitHub][1]）。
* **指令結構**：

  * `start`：啟動 API 伺服器（如需驗證會自動處理）。
  * `auth`：觸發 GitHub 登入，但不運行伺服器。
  * `check-usage`：在終端機中輸出當前 Copilot 使用量。
  * `debug`：顯示診斷資訊（版本、驗證狀態等），可選用 `--json` 輸出（[GitHub][1]）。

---

### 實際使用回饋

Reddit 用戶分享意見：

> 「此專案讓您能將 copilot 轉為 openai 兼容端點。」（[Reddit][2]）
> 「這是一個極佳的專案，可讓您的…」（[Reddit][3]）

---

### 重要注意事項

* **非官方且無支援**：此**並非** GitHub 官方產品，可能隨時失效（[GitHub][1]）。
* **濫用偵測風險**：大量或自動化使用可能觸發 GitHub 的濫用保護機制，導致您的 Copilot 存取權限被暫停（[GitHub][1]）。
* **潛在速率限制問題**：部分用戶回報如 `421 Misdirected Request` 等錯誤，維護者已暫停開發以進行調查（[GitHub][4]）。

---

### 總結（無需表格）

* **功能**：將 GitHub Copilot 暴露為類似 OpenAI/Anthropic API 的服務。
* **重要性**：讓 Copilot 能在預期使用這些 API 的工具（如 Claude Code）中運作。
* **使用方法**：透過 Docker 或 npx 安裝；執行指令以啟動、驗證或監控使用量。
* **謹慎使用**：雖方便但屬非官方項目，GitHub 的速率限制或安全防護可能影響大量使用。

---

如需協助設定，或想了解如何將其整合至特定專案或工具，請隨時告知！

[1]: https://github.com/ericc-ch/copilot-api?utm_source=chatgpt.com "ericc-ch/copilot-api"
[2]: https://www.reddit.com/r/ChatGPTCoding/comments/1m6cqac/how_to_use_your_github_copilot_subscription_with/?utm_source=chatgpt.com "How to use your GitHub Copilot subscription with Claude ..."
[3]: https://www.reddit.com/r/ClaudeAI/comments/1lc21gk/using_github_copilot_as_a_provider_for_claude_code/?utm_source=chatgpt.com "Using GitHub Copilot as a provider for Claude Code"
[4]: https://github.com/ericc-ch/copilot-api/issues/7?utm_source=chatgpt.com "Issue #7 · ericc-ch/copilot-api - 421 Misdirected Request"