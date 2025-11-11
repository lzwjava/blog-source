---
audio: false
generated: true
lang: hant
layout: post
title: GitHub Actions 定時排程
translated: true
type: note
---

是的，可以透過在 GitHub Actions 中使用 cron 排程來設定 GitHub 工作流程每日執行一次。

### 說明
GitHub Actions 允許您透過工作流程自動化儲存庫中的任務，這些工作流程定義在 `.github/workflows` 目錄中的 YAML 檔案。其中一種觸發工作流程的方式是使用 `schedule` 事件，它採用類似 cron 的語法來指定工作流程的執行時間。GitHub Actions 中的 cron 語法遵循標準的 POSIX 格式，包含五個欄位：分鐘、小時、月份中的日期、月份和星期中的日期。

要讓工作流程每日執行一次，您可以使用如 `0 0 * * *` 的 cron 表達式，這表示「每日 UTC 時間 00:00 執行」。其分解如下：
- **分鐘 (0)**：每小時的第 0 分鐘
- **小時 (0)**：00:00（午夜）UTC
- **月份中的日期 (*)**：每月的每一天
- **月份 (*)**：每個月
- **星期中的日期 (*)**：每週的每一天

### 範例設定
以下是一個每日執行一次的 GitHub Actions 工作流程設定範例：

```yaml
name: Daily Workflow
on:
  schedule:
    - cron: '0 0 * * *'
jobs:
  example-job:
    runs-on: ubuntu-latest
    steps:
      - name: Print message
        run: echo "This runs once a day!"
```

此工作流程將於每日 UTC 時間午夜執行。

### 關鍵注意事項
- **時區**：排程以 UTC 時間運行，因此如果您需要根據本地時區在特定時間執行，請調整 cron 表達式。
- **預設分支**：除非另有指定，排程工作流程預設在儲存庫的預設分支（例如 `main` 或 `master`）上運行。
- **可靠性**：雖然 GitHub Actions 會盡量在指定時間運行工作流程，但由於基礎設施負載，偶爾可能出現輕微延遲（這種情況較為罕見）。
- **使用限制**：對於免費的 GitHub 帳戶，Actions 的使用存在限制（例如每月執行分鐘數），但單次每日運行通常都在這些限制範圍內。

### 結論
透過在工作流程檔案中正確設定 cron 表達式，GitHub Actions 確實可以每日執行一次工作流程。因此，您的問題答案是**肯定的**。