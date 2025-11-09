---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 進階 Kusto 查詢語言範例
translated: true
type: note
---

Kusto 查詢語言 (KQL) 是用於查詢 Azure 服務（如 Azure Data Explorer 和 Azure Monitor）中大數據集的強大工具。以下是結合了多種運算符、函數及進階功能（如時間序列分析、異常檢測、數據透視和用戶自定義函數）的複雜範例。這些範例取材自真實場景，例如分析風暴事件或銷售數據。每個範例均包含查詢語句及簡要說明。

### 1. 時間序列數據中的異常檢測
此查詢從指標表中匯總每日平均值，並使用序列分解來識別異常，適合用於監控日誌或遙測數據中的異常模式。

```
TableName
| make-series Metric = avg(Value) on Timestamp step 1d
| extend Anomalies = series_decompose_anomalies(Metric)
```

### 2. 用於參數化篩選和匯總的用戶自定義函數
此處定義了一個可重複使用的函數，用於按地區和閾值篩選銷售數據，然後計算總額 — 適用於 Azure Data Explorer 儀表板中的動態報告。

```
let CalculateSales = (region: string, minSales: int) {
    SalesData
    | where Region == region and Sales > minSales
    | summarize TotalSales = sum(Sales)
};
CalculateSales("North America", 1000)
```

### 3. 透視匯總數據以進行交叉表分析
此查詢按類別和地區匯總值，然後將地區透視為列以便於比較，常見於商業智能查詢中。

```
TableName
| summarize Total = sum(Value) by Category, Region
| evaluate pivot(Region, sum(Total))
```

### 4. 時間序列指標間的相關性分析
使用風暴事件數據，此查詢為兩個指標創建每日序列並計算它們的相關性，以揭示兩者之間的關係，例如財產損失與死亡人數之間的關聯。

```
StormEvents
| make-series PropertyDamage = avg(DamageProperty), Fatalities = avg(Fatalities) on BeginTime step 1d
| extend Correlation = series_correlation(PropertyDamage, Fatalities)
```

### 5. 事件分析中的篩選、頂部選擇和持續時間計算
此查詢篩選德克薩斯州的洪水事件，按損失金額選擇前 5 名，並添加計算後的持續時間列 — 非常適用於 Azure Sentinel 中的事件響應。

```
StormEvents
| where State == 'TEXAS' and EventType == 'Flood'
| top 5 by DamageProperty
| project StartTime, EndTime, Duration = EndTime - StartTime, DamageProperty
```

### 6. 使用 Let 語句進行靜態值映射以轉換數據
定義一個字典來映射來源類型，篩選事件，並投影友好名稱 — 有助於標準化日誌中的分類數據。

```
let sourceMapping = dynamic(
  {
    "Emergency Manager" : "Public",
    "Utility Company" : "Private"
  });
StormEvents
| where Source == "Emergency Manager" or Source == "Utility Company"
| project EventId, Source, FriendlyName = sourceMapping[Source]
```

這些範例可直接在 Azure Data Explorer 網頁界面或 Log Analytics 中運行。如需更多資訊，請探索官方範例庫。

[Kusto 查詢語言 (KQL) 全面指南](https://medium.com/@danushidk507/comprehensive-guide-to-kusto-query-language-kql-from-beginner-to-advanced-8dff3bd7568e)  
[教程：學習常見的 Kusto 查詢語言運算符](https://learn.microsoft.com/en-us/kusto/query/tutorials/learn-common-operators?view=microsoft-fabric)