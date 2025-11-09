---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 透過 Cron 實現自動化 Git 同步
translated: true
type: note
---

要在一部筆記型電腦的 Git 推送後，自動同步更新到另一部筆記型電腦上相同儲存庫的克隆副本（無需手動執行 `git pull`），你不能單靠 Git 本身實現跨機器的即時「自動」更新——Git 的設計本質上是基於拉取操作的。不過，你可以在第二部筆記型電腦上設定排程任務，定期從遠端（在你的案例中是 GitHub）獲取並合併變更。這對於像你這樣的個人設定來說，是最簡單可靠的方式。

以下是在你的 Mac 上操作的方法（既然你使用的是 MacBook Air）。我們將使用 `cron` 進行排程，因為它是內建且輕量的。假設兩部筆記型電腦都克隆了 `github.com:lzwjava/blog-source`，並且你位於 `main` 分支。

### 步驟 1：確保第二部筆記型電腦的儲存庫設定正確
在第二部筆記型電腦上：
1. 導航至你的儲存庫：`cd /path/to/blog-source`
2. 確認它追蹤了遠端：`git remote -v`（應顯示 `origin` 為你的 GitHub 儲存庫）。
3. 如果沒有，請添加：`git remote add origin git@github.com:lzwjava/blog-source.git`
4. 獲取當前狀態：`git fetch origin`
5. 切換到 main 分支：`git checkout main`
6. 設定上游分支：`git branch --set-upstream-to=origin/main main`

測試手動拉取：`git pull origin main`。它應該會像你的輸出那樣運作。

### 步驟 2：建立自動拉取的腳本
建立一個簡單的 shell 腳本，以安全地處理拉取操作（它會獲取更新、檢查衝突，並在乾淨的情況下拉取）。

1. 在你的儲存庫根目錄中，建立 `auto-pull.sh`：
   ```bash:disable-run
   #!/bin/bash
   cd "$(dirname "$0")"  # 切換到儲存庫目錄
   git fetch origin
   if git diff HEAD origin/main --quiet; then
       git pull origin main
       echo "自動拉取完成：$(date)"
   else
       echo "警告：偵測到本地變更。跳過拉取。請手動解決：$(date)"
       # 可選：發送電子郵件或通知（見下文）
   fi
   ```

2. 使其可執行：`chmod +x auto-pull.sh`

這個腳本：
- 在不合併的情況下獲取更新。
- 檢查你的本地分支是否乾淨（無未提交的變更）。
- 僅在安全時拉取；否則發出警告。

### 步驟 3：使用 Cron 進行排程
Cron 會定期執行任務。我們將每 5 分鐘執行一次（可根據需要調整，例如每小時）。

1. 開啟 crontab 編輯器：`crontab -e`（如果提示，使用 nano：`nano ~/.crontab`）。

2. 在末尾添加這一行（每 5 分鐘一次）：
   ```
   */5 * * * * /path/to/blog-source/auto-pull.sh >> /path/to/blog-source/pull-log.txt 2>&1
   ```
   - 將 `/path/to/blog-source` 替換為你的實際儲存庫路徑（例如 `~/blog-source`）。
   - `>> pull-log.txt` 會將輸出記錄到檔案中，以便除錯。

3. 儲存並退出（在 nano 中按 Ctrl+O、Enter、Ctrl+X）。
4. 驗證：`crontab -l`（應顯示你的行）。
5. 測試：等待 5 分鐘，或再次執行 `crontab -e` 暫時添加 `* * * * *`（每分鐘一次），然後還原。

Cron 以你的使用者身份執行，因此它會尊重你用於 GitHub 認證的 SSH 金鑰（如你的拉取輸出所示）。

### 可選增強功能
- **處理衝突/通知**：如果腳本偵測到問題，可添加通知。編輯 `auto-pull.sh` 並附加：
  ```bash
  # 如果出現警告，發送 macOS 通知
  osascript -e 'display notification "因本地變更而跳過 Git 拉取" with title "部落格儲存庫同步"'
  ```
- **在推送時執行（從第一部筆記型電腦）**：若要實現更接近「推送式」的同步，可在第一部筆記型電腦上使用 GitHub Actions。建立 `.github/workflows/sync.yml`：
  ```yaml
  name: Auto Sync
  on: [push]
  jobs:
    sync:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - name: Notify (e.g., via webhook to second laptop)
          run: curl -X POST https://your-second-laptop-webhook-endpoint  # 在第二部筆記型電腦上設定簡單的伺服器
  ```
  但這需要在第二部機器上運行一個監聽器（例如透過 ngrok + 一個小型 Flask 應用），對於大多數情況來說過於複雜。
- **頻率權衡**：對於部落格儲存庫，每 5 分鐘一次是合適的。若需即時同步，可考慮在終端機中使用 `watch` 工具（`watch -n 300 git pull`），但 cron 是無需手動操作的方式。
- **代理備註**：你的輸出顯示了 HTTP/HTTPS 代理——cron 會繼承這些設定，因此拉取操作應能正常運作。

現在，當你從第一部筆記型電腦推送（`git push origin main`）時，第二部筆記型電腦會每 5 分鐘自動同步一次。檢查 `pull-log.txt` 以查看歷史記錄。

如果你在 cron 中遇到認證/代理問題，可在腳本中添加 `export HTTP_PROXY=http://127.0.0.1:7890` 等設定。若另一部筆記型電腦使用 Windows，請改用「工作排程器」。