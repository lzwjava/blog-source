---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 強制執行三十分鐘構建間隔
translated: true
type: note
---

### 修改工作流程以強制構建間隔為 30 分鐘

為確保您的 Jekyll 部署工作流程不會執行過於頻繁（即連續執行之間至少間隔 30 分鐘），您可以在 `build` 作業的早期階段添加一個條件式步驟。此步驟將查詢 GitHub API 以獲取此工作流程最近一次成功執行的時間戳。如果當前觸發時間在該次執行完成後的 30 分鐘內，作業將提前退出並顯示訊息（跳過構建）。

此方法：
- 使用 GitHub REST API（無需外部工具）。
- 僅檢查**成功**的先前執行（狀態："completed"，結論："success"）。
- 計算時間差（以秒為單位）並與 1800（30 分鐘）進行比較。
- 適用於您現有的 push 和 `workflow_dispatch` 觸發器。
- 不會干擾並行設定（該設定處理重疊的執行）。

#### 更新的 YAML 程式碼片段
將此新步驟插入到 `build` 作業中的「Checkout Repository」步驟之後。其餘工作流程保持不變。

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      TELEGRAM_BOT_API_KEY: ${{ secrets.TELEGRAM_BOT_API_KEY }}
      OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Enforce 30-Minute Build Gap
        id: cooldown
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # 獲取此工作流程最近一次成功的執行
          RUNS_RESPONSE=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
            -H "Accept: application/vnd.github.v3+json" \
            "https://api.github.com/repos/${{ github.repository }}/actions/workflows/${{ github.workflow_ref }}/runs?status=completed&conclusion=success&per_page=1&sort=timestamp&direction=desc")

          # 提取最近一次成功執行的 completed_at 時間戳（ISO 8601 格式）
          LAST_COMPLETED_AT=$(echo "$RUNS_RESPONSE" | jq -r '.[0].completed_at // empty')
          
          if [ -z "$LAST_COMPLETED_AT" ] || [ "$LAST_COMPLETED_AT" = "null" ]; then
            echo "No previous successful run found. Proceeding with build."
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

          # 將時間戳轉換為 Unix 秒數以便比較
          CURRENT_TIME=$(date -u +%s)
          LAST_TIME=$(date -d "$LAST_COMPLETED_AT" +%s)
          TIME_DIFF=$((CURRENT_TIME - LAST_TIME))

          echo "Last successful run completed at: $LAST_COMPLETED_AT (diff: ${TIME_DIFF}s)"

          if [ $TIME_DIFF -lt 1800 ]; then  # 1800 秒 = 30 分鐘
            echo "Build skipped: Less than 30 minutes since last successful run."
            echo "skip_build=true" >> $GITHUB_OUTPUT
            exit 0
          else
            echo "Sufficient time gap. Proceeding with build."
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

      # 如果冷卻檢查失敗，則跳過整個構建（在後續步驟中添加此條件，或將構建步驟包裝在 if 中）
      - name: Set up Python 3.13.2
        if: steps.cooldown.outputs.skip_build != 'true'
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      # ...（在此之後的所有剩餘步驟上重複 'if: steps.cooldown.outputs.skip_build != 'true'' 條件）
```

#### 關鍵更改說明
1. **API 查詢**：
   - 使用 `curl` 呼叫 GitHub Actions API 端點以獲取工作流程執行。
   - 篩選 `status=completed` 和 `conclusion=success` 以僅獲取已完成的成功執行。
   - 限制為 `per_page=1` 並按 `timestamp desc` 排序以獲取最近的一次。
   - 提取 `completed_at`（上次執行的確切結束時間）。

2. **時間計算**：
   - 使用 `date` 將當前時間和上次完成時間轉換為 Unix 時間戳。
   - 計算時間差（以秒為單位）。
   - 如果 `< 1800` 秒，則設定 `skip_build=true` 並提前退出步驟。

3. **條件式執行**：
   - 在**每個後續步驟**中添加 `if: steps.cooldown.outputs.skip_build != 'true'`（例如 Python 設定、安裝依賴項，一直到同步構建的站點）。
   - 這確保如果冷卻觸發，作業在 GitHub UI 中報告「skipped」，但仍記錄原因。

4. **處理的邊緣情況**：
   - 沒有先前的執行：繼續執行（首次構建）。
   - 先前執行失敗/進行中：忽略它們並繼續執行。
   - API 錯誤：預設繼續執行（安全預設值）。
   - `jq` 已預先安裝在 `ubuntu-latest` 上，因此無需額外設定。

#### 測試更改
- 將此提交到您的 `main` 分支（它將觸發工作流程）。
- 觸發多次快速推送/dispatches：30 分鐘內的第二次應跳過。
- 監控作業日誌中的「Build skipped」訊息。
- 如果您想調整間隔（例如 1 小時），請將 `1800` 更改為 `3600`。

#### 替代方案
- **排程觸發器**：如果您希望*定期*每 30 分鐘構建一次（無論推送與否），請將此添加到 `on:` 部分：
  ```yaml
  schedule:
    - cron: '*/30 * * * *'  # 每 30 分鐘
  ```
  但這不會對推送觸發器強制執行間隔——如果需要，可以與冷卻步驟一起使用。
- **自訂 Action**：為了可重用性，將冷卻邏輯包裝在可重用的工作流程或複合 Action 中。
- **限制**：此方法檢查執行完成時間，而非開始時間。如果先前的執行仍在運行超過 30 分鐘，並行設定無論如何都會取消它。

如果這不符合您的確切意圖（例如，您意指*至少*每 30 分鐘排程一次），請提供更多詳細資訊！