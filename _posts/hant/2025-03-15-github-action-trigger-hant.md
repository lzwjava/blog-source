---
audio: false
generated: true
lang: hant
layout: post
title: 觸發 GitHub Actions
translated: true
type: note
---

是的，GitHub Action 確實可以觸發另一個 GitHub Action，儘管並非直接觸發。GitHub Actions 工作流程通常由特定事件觸發，例如推送、拉取請求或排程，但有幾種間接方法可以讓一個工作流程觸發另一個。以下是主要的實現方式：

---

### 1. 使用 `workflow_dispatch` 事件
您可以透過 GitHub API 以程式設計方式觸發配置為監聽 `workflow_dispatch` 事件的工作流程。

- **運作原理**：第一個工作流程透過 API 呼叫來觸發第二個工作流程。
- **範例**：
  ```yaml
  name: 觸發其他工作流程
  on: [push]
  jobs:
    觸發:
      runs-on: ubuntu-latest
      steps:
        - name: 觸發工作流程
          run: |
            curl -X POST \
              -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
              -H "Accept: application/vnd.github.v3+json" \
              https://api.github.com/repos/<擁有者>/<倉庫>/actions/workflows/<工作流程_id>/dispatches \
              -d '{"ref": "main"}'
  ```
  請將 `<擁有者>`、`<倉庫>` 和 `<工作流程_id>` 替換為您的倉庫詳細資訊和目標工作流程的 ID。第二個工作流程的配置中必須包含 `on: [workflow_dispatch]`。

---

### 2. 使用 Repository Dispatch 事件
一個工作流程可以透過 GitHub API 發送自訂的 repository dispatch 事件，另一個工作流程可以監聽並響應該事件。

- **運作原理**：第一個工作流程透過 GitHub API 發送 repository dispatch 事件，第二個工作流程則響應該事件。
- **範例**：
  - 第一個工作流程（發送事件）：
    ```yaml
    name: 發送 Dispatch 事件
    on: [push]
    jobs:
      發送-dispatch:
        runs-on: ubuntu-latest
        steps:
          - name: 發送 Dispatch
            run: |
              curl -X POST \
                -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
                -H "Accept: application/vnd.github.v3+json" \
                https://api.github.com/repos/<擁有者>/<倉庫>/dispatches \
                -d '{"event_type": "custom_event"}'
    ```
  - 第二個工作流程（由事件觸發）：
    ```yaml
    name: 由 Dispatch 觸發
    on:
      repository_dispatch:
        types: [custom_event]
    jobs:
      響應:
        runs-on: ubuntu-latest
        steps:
          - name: 響應事件
            run: echo "由 custom_event 觸發"
    ```

---

### 3. 透過 Git 事件觸發
一個工作流程可以透過產生 Git 事件（例如建立提交或開啟拉取請求）來觸發另一個工作流程，第二個工作流程則設定為響應該事件。

- **運作原理**：第一個工作流程修改倉庫（例如透過推送提交），觸發設定為響應該事件（例如 `on: [push]`）的第二個工作流程。
- **範例**：
  ```yaml
  name: 建立提交
  on: [push]
  jobs:
    建立-提交:
      runs-on: ubuntu-latest
      steps:
        - name: 簽出
          uses: actions/checkout@v2
        - name: 建立檔案
          run: echo "新檔案" > newfile.txt
        - name: 提交並推送
          run: |
            git config user.name "GitHub Action"
            git config user.email "action@github.com"
            git add newfile.txt
            git commit -m "新增檔案"
            git push
  ```
  這可能會觸發另一個設定為在 `push` 事件時執行的工作流程。

---

### 關鍵注意事項
- **權限**：用於 API 呼叫的 GitHub token 必須具有足夠的權限來觸發工作流程或發送 dispatch 事件。
- **速率限制**：請注意 GitHub 的 API 速率限制，特別是對於頻繁執行的工作流程。
- **避免循環觸發**：透過添加條件來防止工作流程無休止地相互觸發，避免無限循環。
- **配置**：確保目標工作流程正確設定以監聽預期的事件。

---

### 結論
雖然 GitHub Actions 未提供直接呼叫另一個工作流程的機制，但您可以透過使用 `workflow_dispatch`、repository dispatch 事件或 Git 事件（如提交或拉取請求）來間接實現。這些方法讓您能夠根據需求有效地鏈接或觸發工作流程。