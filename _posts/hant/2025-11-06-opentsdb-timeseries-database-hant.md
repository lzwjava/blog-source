---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: OpenTSDB 分散式時間序列數據庫
translated: true
type: note
---

OpenTSDB 是一款開源、分散式且可擴充的時間序列資料庫（TSDB），專為儲存、索引及查詢大量時間戳記數值資料而設計，例如來自監控系統的指標數據。它最初由 StumbleUpon（現屬 eBay）的 Benoit Sigoure 開發，旨在處理海量數據集同時保持數據粒度，其底層儲存建基於 Apache HBase，利用 HBase 的分散式特性實現跨叢集的水平擴充。

### 主要特性
- **可擴充性**：透過將數據分散到多個節點，每日可處理數十億個數據點，且不存在單點故障。
- **數據模型**：將數據儲存為鍵值對，其中鍵包含時間戳、指標名稱及標籤（例如「cpu.usage」可附帶主機與地區標籤），實現無需預定義結構的靈活查詢。
- **組件**：
  - **時間序列守護程式（TSD）**：核心伺服器，負責數據接收、查詢及 HTTP API 互動。
  - 用於數據匯入/匯出與管理的命令行工具。
- **查詢功能**：透過 API 支援類 SQL 查詢，提供時間範圍內的聚合函數（如總和、平均值），並可與 Grafana 等視覺化工具整合。
- **應用場景**：主要用於 DevOps、物聯網、金融及效能追蹤等監控與可觀測性領域，尤其適合高數據攝取率與長期保留需求的場景。

OpenTSDB 屬於輕量級方案，無需自訂儲存引擎，並在 GitHub 上持續活躍維護。雖然在大數據環境中表現強大，但部署時可能需要 HBase 專業知識，且對小型部署而言可能較耗資源。

### 參考資料
- [OpenTSDB 官方網站](https://opentsdb.net/)
- [GitHub 儲存庫](https://github.com/OpenTSDB/opentsdb)
- [Medium 上的 OpenTSDB 解析](https://medium.com/analytics-vidhya/understanding-opentsdb-a-distributed-and-scalable-time-series-database-e4efc7a3dbb7)