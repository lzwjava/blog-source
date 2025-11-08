---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: WebSphere 應用伺服器核心組件
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) 核心概念

IBM WebSphere Application Server 採用階層式結構來組織和管理分散式環境中的伺服器。這種結構可實現集中管理、擴展性、負載平衡和高可用性。以下是核心組件：**cell**、**cluster**、**node** 和 **server**。

- **Cell**：分散式 WAS 環境中的頂層邏輯容器。它將一個或多個節點分組到單一管理域中，由 Deployment Manager（一種特殊的伺服器實例）進行管理。Cell 共享通用的配置存儲庫、安全設置和資源（如 JMS 總線）。Cell 支援在整個拓撲中執行集中任務，例如應用程式部署和使用者身份驗證。在基礎（獨立）設置中，一個 cell 可能僅包含一個節點。

- **Cluster**：一個或多個應用程式伺服器（通常跨多個節點）的邏輯分組，它們協同工作以實現工作負載管理。Cluster 支援水平擴展、負載平衡和故障轉移——例如，如果一台伺服器故障，流量將路由到其他伺服器。在 cluster 層級定義的資源（如應用程式或數據源）會自動傳播到所有成員伺服器。Cluster 是 cell 範圍的，意味著它們存在於單一 cell 內。

- **Node**：代表託管一個或多個伺服器的實體機器（或在某些情況下為一組機器）的邏輯表示。每個節點運行一個 Node Agent 進程，該進程負責與 Deployment Manager 通信、同步配置以及管理伺服器生命週期（啟動/停止進程）。節點定義了 clustering 的邊界，並被聯邦到 cell 中。

- **Server**：基本的運行時單元——一個應用程式伺服器的實例，用於託管和執行 J2EE/Java EE 應用程式（例如 servlet、EJB、Web 服務）。伺服器可以是獨立的，也可以是節點/cluster 的一部分。有不同類型的伺服器：用於應用程式的應用程式伺服器、用於 cell 管理的 Deployment Manager 和用於節點協調的 Node Agent。

### 拓撲與階層結構

WAS 拓撲採用階層式設計，專為分散式管理而設計：

1. **Cell（頂層）**：涵蓋整個管理域。包含：
   - 一個 Deployment Manager（用於集中控制）。
   - 一個或多個節點（通過 Deployment Manager 聯邦）。
   - 零個或多個 cluster（跨節點）。

2. **Node（中層）**：屬於單一 cell。每個節點：
   - 運行在一個主機機器上。
   - 包含一個 Node Agent。
   - 託管一個或多個伺服器。
   - 作為資源範圍的邊界（例如，cluster 不能跨不同 cell 的節點）。

3. **Server（基礎層）**：在節點內運行。它們：
   - 可以是獨立的（在基礎設置中）或 clustered。
   - 最多屬於一個 cluster。
   - 處理實際的應用程式工作負載。

**視覺化階層結構**（簡化版）：
```
Cell
├── Deployment Manager
├── Node 1
│   ├── Node Agent
│   ├── Server A
│   └── Server B
├── Node 2
│   ├── Node Agent
│   ├── Server C
│   └── Server D
└── Cluster X (members: Server B, Server C, Server D)
```

- **通信流程**：Deployment Manager 將配置同步到 Node Agent，後者管理伺服器。對於 Web 流量，外部負載平衡器（例如 IBM HTTP Server）將請求路由到 cluster 成員。
- **擴展**：向 cell 添加節點/伺服器以實現增長；cluster 實現跨節點的冗餘。
- **最佳實踐**：將相關環境（開發/測試/生產）保留在單獨的 cell 中。較大的 cell 簡化管理，但增加了升級的複雜性。

這種結構支援從單伺服器設置到具有數百台伺服器的企業級部署的所有內容。

### 參考資料
- [WebSphere Concepts: Cell, Node, Cluster, Server](https://itdevworld.wordpress.com/2009/05/03/websphere-concepts-cell-node-cluster-server/)
- [How to Divide a WebSphere Topology into Cells](https://veithen.io/2013/11/04/divide-websphere-topology-into-cells.html)
- [IBM Docs: Introduction to Clusters](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=servers-introduction-clusters)