---
audio: false
generated: true
lang: hant
layout: post
title: GitHub Actions 並行設定
translated: true
type: note
---

您目前的 GitHub Actions 工作流程配置已設定 `cancel-in-progress: false`，這意味著它*不應該*取消 `gh-pages` 並行群組中正在執行的任務。如果任務仍然被取消，可能是其他問題或配置錯誤導致此行為。以下是驗證和修復問題的步驟：

### 1. **確認並行設定**
您的配置看起來正確，可防止任務取消：

```yaml
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
```

- **功能說明**：`concurrency` 鍵與 `cancel-in-progress: false` 確保同一 `gh-pages` 群組的多個工作流程運行可以同時進行，而不會互相取消。
- **放置位置**：確保此 `concurrency` 區塊定義在**工作流程層級**（YAML 文件的頂層，不在任務或步驟內）。例如：

```yaml
name: 部署到 GitHub Pages
on:
  push:
    branches: [ main ]
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      # 您的步驟在此
```

如果 `concurrency` 區塊放置不當（例如在任務內部），將無法按預期工作。如有需要，請將其移至頂層。

### 2. **檢查衝突的並行設定**
- **多個工作流程**：如果您有多個與 `gh-pages` 分支互動的工作流程（例如獨立的 YAML 文件），請確保*所有*相關工作流程都設有 `cancel-in-progress: false`。只要有一個工作流程設為 `cancel-in-progress: true`（或缺少 `concurrency` 設定），就可能取消其他工作流程的任務。
- **儲存庫設定**：檢查是否有任何儲存庫層級設定或第三方 GitHub Actions 強制執行取消操作。例如，某些 CI/CD 整合或自定義動作可能會覆蓋並行行為。

### 3. **驗證工作流程觸發器**
如果觸發器配置錯誤或存在競爭條件，任務可能看似被「取消」。請檢查工作流程的 `on` 部分：
- 確保工作流程僅在預期時觸發（例如 `on: push: branches: [ main ]` 或 `on: pull_request`）。
- 如果定義了多個觸發器（例如 `push` 和 `pull_request`），可能會產生重疊的運行。必要時為不同的觸發器使用唯一的 `concurrency.group` 名稱，例如：

```yaml
concurrency:
  group: 'gh-pages-${{ github.event_name }}'
  cancel-in-progress: false
```

這會為 `push` 和 `pull_request` 事件創建獨立的並行群組，防止它們互相干擾。

### 4. **檢查 GitHub Actions 日誌**
- 前往 GitHub 儲存庫中的 **Actions** 標籤，檢閱被取消任務的日誌。
- 查找指示任務被取消原因的消息（例如「因並行而被取消」或其他原因，如超時、手動取消或失敗）。
- 如果日誌提到並行問題，請仔細檢查所有涉及 `gh-pages` 分支的工作流程是否都設有 `cancel-in-progress: false`。

### 5. **處理手動取消**
如果有人透過 GitHub UI 手動取消工作流程運行，無論 `cancel-in-progress: false` 的設定如何，都會停止該運行中的所有任務。請確保您的團隊了解除非必要，否則不要手動取消運行。

### 6. **考慮工作流程依賴關係**
如果任務因早期步驟的依賴關係或失敗而被取消：
- 檢查工作流程中的 `needs` 關鍵字。如果一個任務失敗，依賴的任務可能會被跳過或取消。
- 使用 `if: always()` 確保即使早期任務失敗，後續任務仍會運行：

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # 建置步驟
  deploy:
    needs: build
    if: always()
    runs-on: ubuntu-latest
    steps:
      # 部署步驟
```

### 7. **使用最小化工作流程進行測試**
如果問題仍然存在，請創建一個最小化的測試工作流程來隔離問題：

```yaml
name: 測試並行性
on:
  push:
    branches: [ main ]
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
jobs:
  test-job:
    runs-on: ubuntu-latest
    steps:
      - name: 睡眠模擬長時間任務
        run: sleep 60
      - name: 打印訊息
        run: echo "任務完成！"
```

推送多個提交以觸發並行運行，並驗證任務是否在未被取消的情況下完成。

### 8. **檢查 GitHub Actions 狀態**
在極少數情況下，GitHub Actions 可能出現平台範圍的問題。請檢查 [GitHub 狀態頁面](https://www.githubstatus.com/) 或 X 上有關 GitHub Actions 中斷的最新貼文。

### 9. **除錯提示**
- 添加一個步驟來記錄工作流程運行 ID 和並行群組以進行除錯：

```yaml
steps:
  - name: 記錄運行詳情
    run: echo "運行 ID: ${{ github.run_id }}, 並行群組: ${{ github.workflow }}-${{ github.event_name }}"
```

- 如果需要，使用 GitHub Actions API 以程式方式檢查運行中的工作流程（需要進階設定）。

### 如果仍然無法運作
如果任務仍然被取消：
- 請分享完整的工作流程 YAML 文件，以及 GitHub Actions 日誌中取消訊息的截圖或描述。
- 請告知您是否使用特定的 actions（例如 `actions/checkout`、`peaceiris/actions-gh-pages`），或者您是否有多个與 `gh-pages` 互動的工作流程。

這將有助於準確定位問題。請告訴我如何進一步協助您！