---
audio: false
generated: true
image: false
lang: hant
layout: post
title: GreptimeDB：統一時間序列數據庫
translated: true
type: note
---

### GreptimeDB 概覽
GreptimeDB 是一款開源、雲原生、分散式的時間序列數據庫，主要為可觀測性數據（包括指標、日誌和追蹤）而設計。它將這些數據類型統一整合至單一數據庫中，能夠在龐大規模（高達 PB 級）下實現亞秒級查詢回應的實時洞察。該數據庫專為高效處理高基數數據而構建，支援透過 SQL、PromQL 及串流處理進行查詢。其針對物聯網、邊緣計算及雲端環境進行了優化，並可無縫整合至 Prometheus、OpenTelemetry 和 Grafana 等工具中。

### 基礎架構
GreptimeDB 採用雲原生架構，將計算與儲存分離，透過利用物件儲存（如 AWS S3 或 Azure Blob）實現數據持久化，從而達成彈性擴展與成本效益。此設計相較傳統區塊儲存，可降低 3 至 5 倍的儲存成本，同時透過快取及列式格式等優化維持高效能。

關鍵組件包括：
- **Metasrv**：中央元數據伺服器，負責管理數據庫結構描述、資料表資訊及數據分佈（分片）。它監控 datanode 的健康狀態、更新路由表，並確保叢集可靠性。在叢集模式下，需至少三個節點以實現高可用性。
- **Frontend**：無狀態層，負責處理傳入請求、進行身份驗證、將協定（如 MySQL、PostgreSQL、REST API）轉譯為內部 gRPC，並根據 metasrv 的指引將查詢路由至 datanodes。其可水平擴展以應對增加的負載。
- **Datanodes**：負責儲存和處理數據區域（分片）。它們執行讀寫操作、管理本地快取，並回傳結果。數據持久化儲存於物件儲存中，以確保耐用性與可擴展性。

互動流程：請求經由 frontend 進入，frontend 向 metasrv 查詢路由資訊後，將請求轉發至相關的 datanodes 進行處理與回應。此架構支援獨立模式（所有組件整合於單一二進位檔中，適用於本地或嵌入式使用）或叢集模式（對 Kubernetes 友好，適用於生產環境）。

儲存細節：採用專為時間序列數據定制的日誌結構合併樹（LSM），並透過預寫式日誌（WAL）確保耐用性。數據按時間分區，以 Parquet 格式壓縮，並快取於多層系統中（寫入快取用於近期數據，具 LRU 淘汰機制的讀取快取用於歷史數據，以及元數據快取）。此設計有效緩解物件儲存的延遲問題，實現熱數據的亞毫秒級低延遲查詢，並透過預取機制高效處理冷數據。可靠性功能包括多副本儲存、校驗和及跨區域複製。

### 技術堆疊與產品
- **以 Rust 編寫**：是的，整個數據庫均以 Rust 實作，以實現高效能、記憶體安全與效率。其利用 Apache DataFusion 和 Arrow 等函式庫進行向量化執行與平行處理，並透過 SIMD 指令優化 CPU 使用率。
- **GitHub 上的開源專案**：完全開源，採用 Apache 2.0 許可證，託管於 https://github.com/GreptimeTeam/greptimedb。截至 2025 年，該專案處於測試階段，預計於 2025 年中達到正式可用。專案積極維護，定期發佈版本（例如 2025 年 4 月的 v0.14），重點開發全文索引及雙引擎支援等功能。社群參與包括外部貢獻者，並已有早期採用者於生產環境中使用。
- **GreptimeDB Cloud**：基於開源核心構建的完全託管、無伺服器雲端服務，提供按用量計價、自動擴展及零運維負擔。其具備企業級功能，如增強安全性、高可用性及專業支援，同時支援多雲物件儲存。雲端版本與開源版本的關聯在於，其針對大規模、業務關鍵的用例進行擴展，並提供相同的統一 API 以便遷移。

### 創新與工作品質
GreptimeDB 在可觀測性領域的創新之處在於，將指標、日誌和追蹤統一至單一數據庫中，減少了傳統多工具堆疊（例如取代 Prometheus + Loki + Jaeger 的組合）的複雜性。其計算與儲存分離的設計，在 Kubernetes 環境中實現了「無限擴展」能力，能夠處理極高基數數據而不降低效能，並透過物件儲存整合與智能快取，實現高達 50 倍的運維/儲存成本降低。Rust 的實作帶來了卓越的可靠性與速度，基準測試顯示其表現優於競爭對手：在 ClickHouse 的 JSONBench 中，冷啟動排名第一，熱啟動排名第四；在攝取吞吐量、查詢延遲及資源效率方面（例如在 TSBS 測試中快 6 倍），均優於 InfluxDB、Elasticsearch 和 Grafana Mimir。豐富的索引功能（倒排、全文、向量）及原生 OpenTelemetry 支援，進一步增強了其在實時物聯網與監控場景中的優勢。

總體而言，團隊表現出色：該專案自 2022 年作為新進者，已發展成為具實際應用案例的穩健解決方案（例如用於 Poizon 的可觀測性及 OB Cloud 的日誌管理）。活躍的開發進度、正面的社群回饋及強勁的基準測試結果，均顯示其專注於效能、成本與可用性的高品質工程實踐。儘管仍處於測試階段，其發展軌跡表明，它有望在雲原生數據庫領域產生更廣泛的影響。

[Greptime 官方網站](https://greptime.com/)  
[GreptimeDB 文件 - 架構](https://docs.greptime.com/user-guide/concepts/architecture)  
[GreptimeDB GitHub 儲存庫](https://github.com/GreptimeTeam/greptimedb)  
[GreptimeDB 儲存架構深度解析](https://greptime.com/blogs/2025-03-26-greptimedb-storage-architecture)  
[GreptimeDB 與競爭對手基準測試](https://medium.com/@greptime/comprehensive-benchmark-report-how-greptimedb-stacks-up-against-influxdb-elasticsearch-69ce97cf6acb)  
[GreptimeDB v0.14 發佈](https://greptime.com/blogs/2025-04-27-greptimedb-version-released-index-flow-trace)  
[在 Poizon 擴展可觀測性](https://medium.com/@greptime/scaling-observability-at-poizon-building-a-cost-effective-and-real-time-monitoring-architecture-07a42e217c02)