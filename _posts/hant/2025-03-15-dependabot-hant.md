---
audio: false
generated: true
lang: hant
layout: post
title: 移除 Dependabot
translated: true
type: note
---

要從 GitHub Actions 中移除 Dependabot，你需要停用其建立會觸發工作流程的拉取請求功能，並可選擇性地移除任何與 Dependabot 相關的自訂工作流程。以下是實現此目標的步驟。請注意，我假設您查詢中的 "dependant bot" 指的是 Dependabot——GitHub 中用於依賴項管理的常用工具。

---

### 步驟 1：停用 Dependabot 版本更新
Dependabot 版本更新會自動建立拉取請求以保持你的依賴項處於最新狀態。這些拉取請求可能會觸發 GitHub Actions 工作流程。要停用此功能：

- **找到設定檔**：檢查你的儲存庫中 `.github` 目錄下是否存在名為 `dependabot.yml` 的檔案。
- **刪除檔案**：如果該檔案存在，請刪除 `dependabot.yml` 檔案並提交此變更。這將阻止 Dependabot 為版本更新建立拉取請求。
- **驗證**：如果不存在 `dependabot.yml` 檔案，則版本更新功能已被停用。

---

### 步驟 2：停用 Dependabot 安全更新
Dependabot 安全更新會產生拉取請求以修復依賴項中的漏洞，這些請求同樣可能觸發 GitHub Actions 工作流程。要關閉此功能：

- **前往儲存庫設定**：在你的 GitHub 儲存庫中，點擊 **Settings** 標籤。
- **導航至安全設定**：滾動至 **Security & analysis**（或 **Code security and analysis**，具體取決於你的 GitHub 介面）。
- **停用安全更新**：找到 **Dependabot security updates** 並點擊 **Disable**。

這將阻止 Dependabot 為安全修復建立拉取請求。

---

### 步驟 3：（可選）移除自訂的 Dependabot 相關工作流程
如果你曾設定專門用於處理 Dependabot 拉取請求的 GitHub Actions 工作流程（例如自動合併、標籤管理或使用 Dependabot 元數據），你可能需要清理這些設定：

- **檢查工作流程檔案**：查看 `.github/workflows` 目錄中的 YAML 檔案。
- **識別 Dependabot 邏輯**：搜尋包含 `if: github.event.pull_request.user.login == 'dependabot[bot]'` 等條件或使用 `dependabot/fetch-metadata` 等操作的程式碼。
- **移除或修改**：刪除這些工作流程，或調整它們以移除 Dependabot 特定邏輯，然後提交變更。

此步驟是可選的，因為完成步驟 1 和 2 後，Dependabot 將不再建立新的拉取請求，這意味著現有工作流程不會再被 Dependabot 觸發。然而，移除這些工作流程可確保徹底清理。

---

### 補充說明
- **現有拉取請求**：停用 Dependabot 不會關閉它已建立的現有拉取請求。這些請求若被更新，仍可能觸發工作流程。如有需要，你可以手動關閉它們。
- **Dependabot 警報**：如果你還想停止漏洞通知（與 GitHub Actions 無直接關聯），請前往 **Settings > Security & analysis** 並停用 **Dependabot alerts**。此為可選操作，與工作流程觸發無關。

---

### 結果
完成步驟 1 和 2 後，Dependabot 將不再在你的儲存庫中建立拉取請求，從而有效「移除」其對 GitHub Actions 的影響。如果你曾為 Dependabot 自訂工作流程，步驟 3 將確保所有相關自動化設定都被清除。你的 GitHub Actions 現在將僅基於其他事件運行，不再受 Dependabot 影響。