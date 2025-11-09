---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Kusto 查詢語言入門指南
translated: true
type: note
---

### 開始使用 Azure 中的 KQL (Kusto 查詢語言)

KQL 是一種功能強大的唯讀查詢語言，專為分析 Azure 服務（如 Azure Data Explorer、Azure Monitor (Log Analytics) 和 Microsoft Sentinel）中的大量結構化、半結構化和非結構化數據而設計。它直觀、基於管道（使用 `|` 進行數據流傳輸），並針對大數據場景（如日誌分析、遙測和威脅檢測）進行了優化。以下是使用它的逐步指南。

#### 先決條件
- 擁有有效的 Azure 訂閱，並可訪問相關服務（例如 Azure Data Explorer 叢集、Log Analytics 工作區或 Sentinel 實例）。
- 適當的權限：至少對數據庫、表格或工作區具有讀取權限。
- 基本熟悉數據概念（如表格和篩選）會有所幫助，但 KQL 對初學者友好。
- 可選：安裝 Azure Data Explorer 應用程式或使用網頁 UI 快速開始——最初無需編碼環境。

#### 步驟 1：選擇運行查詢的位置
KQL 可在多個 Azure 服務中運行。從適合您數據源的服務開始：
- **Azure Data Explorer**：非常適合大數據探索。訪問網頁 UI：[dataexplorer.azure.com](https://dataexplorer.azure.com/)。選擇一個叢集和數據庫，然後打開查詢編輯器。
- **Azure Monitor / Log Analytics**：用於日誌和指標。在 Azure 入口網站 (portal.azure.com) 中，前往 **Monitor > Logs**，選擇一個工作區，然後使用查詢編輯器。
- **Microsoft Sentinel**：用於安全分析。在 Azure 入口網站中，導航至 **Microsoft Sentinel > Logs** 在您的工作區中。
- **其他選項**：Microsoft Fabric（通過 KQL 查詢編輯器）或與 Power BI 等工具集成以進行可視化。

數據按層次結構組織：數據庫 > 表格 > 欄位。查詢是唯讀的；使用管理命令（以 `.` 開頭）進行架構變更。

#### 步驟 2：理解基本語法
KQL 查詢是以分號 (`;`) 分隔的純文本語句。它們使用數據流模型：
- 以表格名稱開頭（例如 `StormEvents`）。
- 通過管道 (`|`) 將數據傳輸給運算符進行篩選、聚合等。
- 以輸出（如 `count` 或 `summarize`）結束。
- 對名稱/運算符區分大小寫；如果需要，請將關鍵字用 `['keyword']` 括起來。

一個簡單的查詢結構：
```
TableName
| where Condition
| summarize Count = count() by GroupByColumn
```

管理命令（非查詢）以 `.` 開頭（例如 `.show tables` 以列出表格）。

#### 步驟 3：編寫並運行您的第一個查詢
1. 在您選擇的服務中打開查詢編輯器（例如 Azure Data Explorer 網頁 UI）。
2. 輸入一個基本查詢。使用示例數據的示例（StormEvents 表格，在大多數環境中可用）：
   ```
   StormEvents
   | where StartTime between (datetime(2007-11-01) .. datetime(2007-12-01))
   | where State == "FLORIDA"
   | count
   ```
   - 這會篩選出 2007 年 11 月在佛羅里達州的風暴並返回計數（例如 28）。
3. 點擊 **Run** 執行。結果以表格形式顯示；使用 UI 可視化為圖表或導出。
4. 迭代：添加運算符，如 `project`（選擇欄位）、`summarize`（聚合）或 `extend`（添加計算欄位）。

首先學習的常用運算符：
- `where`：篩選行（例如 `| where Level == "Error"`）。
- `summarize`：聚合（例如 `| summarize avg(Duration) by User`）。
- `join`：合併表格。
- `search`：跨表格全文搜索。

#### 步驟 4：探索進階功能和最佳實踐
- **時間序列和分析**：使用函數如 `make-series` 進行趨勢分析或 `detect-anomalies` 進行異常檢測。
- **可視化**：在編輯器中切換到網格/圖表視圖。導出到 Power BI 以創建儀表板。
- **性能提示**：邏輯排序運算符（早期篩選），使用 `take 100` 限制結果，並在小型數據集上測試。
- **常見用例**：
  - **日誌分析**：查詢應用程式中的錯誤（`| where Level == "Error" | take 50`）。
  - **安全狩獵**：在 Sentinel 中搜索威脅（`search "suspicious login"`）。
  - **數據探索**：匯總指標（`| summarize count() by bin(TimeGenerated, 1h)`）。

#### 疑難排解
- 錯誤？在編輯器中檢查語法（它會突出顯示問題）。確保表格/欄位名稱完全匹配。
- 沒有數據？確認您的工作區已攝取日誌或使用示例數據集。
- 通過 Azure 入口網站或文檔中的互動式教程了解更多信息。

如需動手實踐，請在 Azure Data Explorer 中加載示例數據並進行實驗。

[參考資料]  
[Kusto 查詢語言 (KQL) 概述](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/)  
[編寫並運行您的第一個 KQL 查詢](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/tutorial?pivots=azuredataexplorer-cluster)  
[常用 KQL 運算符](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/tutorial?pivots=azuredataexplorer-cluster&tabs=beginner)