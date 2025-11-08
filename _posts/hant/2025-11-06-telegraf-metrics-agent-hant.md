---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Telegraf：開源指標收集代理
translated: true
type: note
---

Telegraf 是一款由 InfluxData 開發的開源外掛驅動代理程式，用於從各種來源收集、處理、聚合和寫入指標、日誌及其他遙測數據。它採用輕量級設計，以單一二進制檔案運行，並支援超過 300 種輸入外掛（例如用於系統統計、MySQL/PostgreSQL 等資料庫、AWS 等雲端服務，以及 Apache Kafka 等應用程式）和 50 多種輸出外掛（例如輸出至 InfluxDB、Prometheus、Kafka 或 Elasticsearch）。

### 主要特性
- **代理程式架構**：可輕鬆部署於伺服器、容器或 IoT 裝置，無需繁重的依賴項。
- **透過外掛擴展**：使用 Go 語言編寫，必要時可開發自訂外掛。
- **TICK 技術棧組成部分**：與時間序列資料庫 InfluxDB、視覺化工具 Chronograf 及告警系統 Kapacitor 無縫整合。
- **應用場景**：常見於 DevOps 領域的基礎設施監控、應用效能追蹤及 IoT 感測器數據攝取。

該工具基於 MIT 許可證免費使用並持續維護，截至 2025 年底最新穩定版本為 v1.29.x。設定說明請參閱官方文件 [telegraf.influxdata.com](https://docs.influxdata.com/telegraf/)。若此處所述的 Telegraf 與您預期的內容不符（例如指其他情境中的品牌或術語），請提供更多細節！