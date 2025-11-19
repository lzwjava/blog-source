---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GitHub Actions 定時任務使用 UTC 時間
translated: true
type: note
---

**GitHub Actions 排程工作流程（使用 `on: schedule:` 觸發器並配合 cron 語法）一律以 UTC（協調世界時）解讀 cron 時間。**

工作流程 YAML 中並無內建支援直接指定其他時區。若您希望任務在特定本地時間執行（例如上午 9:00 PST），您必須將其轉換為對應的 UTC 時間，並據此編寫 cron 表達式。

### 官方文件重點摘要：
- 排程工作流程使用 POSIX cron 語法，並在特定的 **UTC 時間** 執行。
- 範例：`cron: '0 5 * * *'` 會於每日 UTC 時間上午 5:00 執行（非您的本地時間）。

此機制多年來保持一致，直至 2025 年末仍維持現狀——`schedule` 事件並未內建時區參數（這點與 GitHub 其他功能如 Dependabot 有所不同）。

[觸發工作流程的事件 - GitHub 文件](https://docs.github.com/zh-tw/actions/using-workflows/events-that-trigger-workflows#schedule)  
[GitHub Actions 的工作流程語法 - GitHub 文件](https://docs.github.com/zh-tw/actions/using-workflows/workflow-syntax-for-github-actions#on-schedule)