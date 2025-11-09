---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Apache DataFusion Comet 加速 Spark
translated: true
type: note
---

### Apache DataFusion Comet

Apache DataFusion Comet 是 Apache 軟體基金會旗下的一個開源項目，作為 Apache Spark 的高效能加速器。該項目基於 Apache DataFusion 查詢引擎構建，旨在提升 Spark 工作負載的效能——例如加速資料處理與洞察獲取——同時只需在標準商用硬體上運行。整合過程無需修改程式碼，還能加速涉及 Spark 的 Apache Iceberg 與 Parquet 掃描操作。

#### 主要特性
- **效能提升**：為查詢帶來顯著加速效果。例如在 100 GB Parquet 資料上執行 22 項 TPC-H 查詢的基準測試顯示，整體效能提升 2.2 倍（在單個 8 核執行器上從 687 秒縮短至 302 秒）。項目指南中亦提供可重現的 TPC-DS 基準測試結果。
- **硬體效率**：支援現成商用硬體，無需配備昂貴的 GPU 或 FPGA。
- **無縫相容**：與受支援的 Apache Spark 版本完全相容，可輕鬆整合至現有環境。
- **深度 DataFusion 整合**：運用 DataFusion 執行引擎實現最佳化效能。
- **社群驅動**：採用 Apache 2.0 許可協議，擁有活躍社群支援錯誤修復、功能開發與文件維護。

該項目持續積極維護，提供入門指南、貢獻者指引及 Slack 與 Discord 等社群頻道。

更多詳情（包含透過 datafusion.apache.org 文件的安裝方式與基準測試）請查閱程式庫。

[Apache DataFusion Comet GitHub 程式庫](https://github.com/apache/datafusion-comet)