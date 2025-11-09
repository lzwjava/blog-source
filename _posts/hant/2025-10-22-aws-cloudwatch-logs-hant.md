---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 讀取 AWS CloudWatch 日誌
translated: true
type: note
---

### AWS CloudWatch 讀取日誌簡介
AWS CloudWatch Logs 是一項集中管理、監控和儲存來自 AWS 資源（如 EC2 執行個體、Lambda 函數或 RDS 資料庫）及應用程式日誌檔案的服務。要讀取日誌，首先需要確保日誌已傳送至 CloudWatch（例如透過 EC2 上的 CloudWatch 代理程式或其他服務的自動整合）。設定完成後，您可以透過 AWS Management Console、AWS CLI 或使用 SDK 以程式設計方式檢視日誌。

### 必要條件
- **AWS 權限**：確保您的 IAM 使用者或角色擁有 `logs:DescribeLogGroups`、`logs:DescribeLogStreams`、`logs:GetLogEvents` 和 `logs:FilterLogEvents` 權限（附加 `CloudWatchLogsReadOnlyAccess` 政策）。
- **日誌配置**：日誌必須路由至 CloudWatch。例如：
  - 在 EC2 執行個體上安裝 CloudWatch Logs 代理程式。
  - 在 Lambda 或 ECS 等服務中啟用日誌記錄。
- **AWS CLI（可選）**：若使用 CLI，請透過 `aws configure` 安裝並配置。

### 在 AWS Management Console 中檢視日誌
1. 登入 [AWS Management Console](https://console.aws.amazon.com/) 並開啟 CloudWatch 服務。
2. 在左側導覽窗格中，選擇 **Logs** > **Log groups**。
3. 選擇包含您日誌的日誌群組（例如 Lambda 日誌的 `/aws/lambda/my-function`）。
4. 在日誌流清單（所選日誌群組下方）中，選擇特定流（例如每個執行個體或執行的流）。
5. 日誌事件將載入。自訂檢視：
   - **展開事件**：點擊事件旁的箭頭展開，或切換至清單上方的 **Text** 檢視以查看純文字。
   - **篩選/搜尋**：在搜尋框中輸入篩選條件（例如 "ERROR" 僅顯示錯誤行）。
   - **時間範圍**：點擊搜尋框旁的時間選擇器。選擇 **Relative**（例如最近 1 小時）或 **Absolute**（自訂日期），並在 UTC 和本地時間之間切換。
6. 滾動瀏覽事件或按需下載。

若要跨多個流或群組進行進階查詢，請使用 **CloudWatch Logs Insights**（位於 Logs > Logs Insights）。編寫如 `fields @timestamp, @message | filter @level = "ERROR" | sort @timestamp desc` 的查詢來分析和視覺化日誌。

### 使用 AWS CLI 讀取日誌
使用以下命令以程式設計方式列出和檢索日誌。將佔位符（如 `my-log-group`）替換為您的實際名稱。

1. **列出日誌群組**：
   ```
   aws logs describe-log-groups --log-group-name-prefix my-log-group
   ```
   此命令返回中繼資料，如 ARN、保留期和儲存位元組數。

2. **列出群組中的日誌流**：
   ```
   aws logs describe-log-streams --log-group-name my-log-group --log-stream-name-prefix 2025
   ```
   按前綴篩選流（例如基於日期的名稱）並顯示建立時間和大小。

3. **從流中取得日誌事件**：
   ```
   aws logs get-log-events --log-group-name my-log-group --log-stream-name my-stream --start-time 1730137600000
   ```
   - `--start-time` 和 `--end-time`：時間範圍的 Unix 時間戳（毫秒）。
   - `--limit`：要返回的最大事件數（預設為 1,000）。
   - 輸出包括時間戳、攝取時間和訊息文字。
   - 使用回應中的 `--next-token` 進行分頁。

若要跨流進行篩選搜尋，請使用 `filter-log-events`：
```
aws logs filter-log-events --log-group-name my-log-group --filter-pattern "ERROR" --start-time 1730137600000
```

### 提示與最佳實踐
- **保留期**：日誌預設永久保留；按群組調整以管理成本（例如 30 天）。
- **成本**：檢視日誌免費，但攝取和儲存會產生費用——透過 CloudWatch 指標監控。
- **疑難排解**：若未顯示日誌，請驗證代理程式安裝或服務日誌記錄是否啟用。
- 若要進行即時監控，請在日誌模式上設定指標篩選條件或警報。

[Working with log groups and log streams - Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)  
[CloudWatch Logs examples using AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli_cloudwatch-logs_code_examples.html)  
[Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)