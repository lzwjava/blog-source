---
audio: false
generated: true
lang: hant
layout: post
title: 為何卡夫卡如此快速
translated: true
type: note
---

### 重點摘要
- 影片《系統設計：Kafka 為何如此快速？》似乎透過其架構與設計選擇來解釋 Apache Kafka 的高速效能。
- 研究指出 Kafka 的效能提升得益於僅追加日誌、零拷貝原則、批次處理及高效能分區機制。
- 現有證據傾向認為 Kafka 的高速特性源自其分散式事件串流平台設計，其中包含生產者、代理伺服器與消費者等關鍵組件。

### 引言
本篇網誌文章基於 ByteByteGo 的 YouTube 影片《系統設計：Kafka 為何如此快速？》內容，旨在將影片洞察轉化為書面形式以便閱讀與參考。Apache Kafka 以在即時資料處理方面的高效能著稱，本文將深入探討其背後的運作原理，讓初學者也能輕鬆理解。

### Kafka 核心組件
Apache Kafka 作為分散式事件串流平台，包含三大核心組件：
- **生產者**：將資料傳送至 Kafka 主題的應用程式
- **代理伺服器**：儲存與管理資料的伺服器，確保資料複製與分散
- **消費者**：從主題讀取並處理資料的應用程式

此結構使 Kafka 能高效處理大量資料，從而實現高速傳輸。

### 架構分層與效能優化
Kafka 架構分為兩大層級：
- **運算層**：包含生產者、消費者與串流處理的 API，負責協調互動
- **儲存層**：由代理伺服器組成，負責主題與分區的資料儲存管理，並進行效能優化

關鍵優化技術包括：
- **僅追加日誌**：以順序寫入方式將資料添加至檔案末端，速度遠勝隨機寫入
- **零拷貝原則**：直接將資料從生產者傳輸至消費者，降低 CPU 負載
- **批次處理**：以批次方式處理資料，減少單筆記錄的系統開銷
- **非同步複製**：主節點代理伺服器可同時處理請求與副本更新，確保可用性不失效能
- **分區機制**：將資料分散至多個分區實現平行處理，提升整體吞吐量

這些設計選擇在 ByteByteGo 的支援文章《[Kafka 為何如此快速？運作原理剖析](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)》中有詳細說明，正是 Kafka 在速度與擴展性方面表現卓越的關鍵。

### 資料流與記錄結構
當生產者傳送記錄至代理伺服器時，會經過驗證、追加至磁碟上的提交日誌，並進行複製以確保持久性，最終在確認提交後通知生產者。此流程針對順序 I/O 進行優化，從而提升效能。

每筆記錄包含：
- 時間戳記：事件建立時間
- 鍵值：用於分區與排序
- 數值：實際資料內容
- 標頭：選用元資料

如網誌文章所述，此結構確保了資料處理效率，並促成 Kafka 的高速表現。

---

### 調查筆記：Apache Kafka 效能深度解析

本節將對 Apache Kafka 的效能進行全面探討，延伸自 ByteByteGo 影片《系統設計：Kafka 為何如此快速？》的內容，並參考額外資源以確保完整理解。分析結構涵蓋 Kafka 的架構、組件與具體優化措施，輔以詳細說明與範例增強清晰度。

#### 背景與情境
Apache Kafka 作為分散式事件串流平台，以其處理高吞吐量、低延遲資料串流的能力聞名，已成為現代資料架構的重要組件。該影片於 2022 年 6 月 29 日發布，屬於系統設計系列影片之一，旨在闡釋 Kafka 的高速運作原理——這個主題在資料串流需求呈指數級成長的背景下顯得尤為重要。本分析參考了 ByteByteGo 的詳細網誌文章《[Kafka 為何如此快速？運作原理剖析](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)》，該文章對影片內容進行了補充並提供額外見解。

#### Kafka 核心組件與架構
Kafka 的速度根基於其核心組件：
- **生產者**：產生並傳送事件至 Kafka 主題的應用程式或系統，例如產生使用者互動事件的網路應用程式
- **代理伺服器**：組成叢集的伺服器，負責儲存資料、管理分區與處理複製，典型設定會包含多個代理伺服器以實現容錯與擴展性
- **消費者**：訂閱主題以讀取與處理事件的應用程式，例如處理即時資料的分析引擎

此架構將 Kafka 定位為事件串流平台，採用「事件」而非「訊息」的術語，使其有別於傳統訊息佇列。正如網誌文章所述，這種設計體現在事件具不可變性，並在分區內依偏移量排序的特性。

| 組件           | 角色                                                                 |
|----------------|----------------------------------------------------------------------|
| 生產者         | 傳送事件至主題，啟動資料流                                           |
| 代理伺服器     | 儲存管理資料，處理複製作業，並服務消費者                             |
| 消費者         | 從主題讀取並處理事件，實現即時分析功能                               |

網誌文章包含位於[此網址](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png)的架構圖，展示叢集模式下生產者、代理伺服器與消費者間的互動關係。

#### 分層架構：運算與儲存
Kafka 架構劃分為：
- **運算層**：透過 API 協調通訊：
  - **生產者 API**：供應用程式傳送事件使用
  - **消費者 API**：實現事件讀取功能
  - **Kafka Connect API**：與資料庫等外部系統整合
  - **Kafka Streams API**：支援串流處理，例如為「訂單」主題建立包含序列化/反序列化的 KStream，以及透過 REST API 執行 ksqlDB 串流處理任務。具體範例包括訂閱「訂單」主題、按產品聚合資料，並將結果傳送至「ordersByProduct」主題供分析使用
- **儲存層**：由叢集中的 Kafka 代理伺服器組成，資料按主題與分區組織。主題類似資料庫表格，分區則分散於各節點確保擴展性。分區內的事件按偏移量排序，具不可變性與僅追加特性，刪除操作亦被視為事件處理，從而提升寫入效能

網誌文章詳細說明了這些特性，指出代理伺服器負責管理分區、讀寫操作與複製流程，並提供位於[此網址](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png)的複製機制示意圖，例如「訂單」主題的 Partition 0 包含三個副本：主節點位於 Broker 1（偏移量 4），跟隨節點分別位於 Broker 2（偏移量 2）與 Broker 3（偏移量 3）。

| 層級           | 說明                                                                 |
|----------------|----------------------------------------------------------------------|
| 運算層         | 互動用 API：生產者、消費者、Connect、Streams 與 ksqlDB              |
| 儲存層         | 叢集中的代理伺服器，主題/分區分散式儲存，事件按偏移量排序            |

#### 控制平面與資料平面
- **控制平面**：管理叢集中繼資料，早期採用 Zookeeper，現已由 KRaft 模組取代，在選定代理伺服器上運行控制器。此簡化設計消除了對 Zookeeper 的依賴，如網誌文章所述，透過特殊主題實現更簡易的配置與更高效的中繼資料傳播
- **資料平面**：處理資料複製流程，跟隨節點發送 FetchRequest 請求，主節點傳送資料，並在特定偏移量前提交記錄以確保一致性。Partition 0 偏移量 2、3、4 的範例即說明此機制，相關示意圖位於[此網址](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png)

#### 記錄結構與代理伺服器運作
每筆記錄（事件的抽象表示）包含：
- 時間戳記：建立時間
- 鍵值：用於排序、同址存放與保留策略，對分區至關重要
- 數值：資料內容
- 標頭：選用元資料

鍵值與數值均以位元組陣列形式存在，透過序列化/反序列化機制進行編解碼，確保靈活性。代理伺服器運作流程包含：
- 生產者請求進入通訊端接收緩衝區
- 網路執行緒將請求移入共享請求佇列
- I/O 執行緒驗證 CRC，追加至提交日誌（包含資料與索引的磁碟區段）
- 請求暫存於待複製區等待複製
- 回應進入佇列，由網路執行緒透過通訊端發送緩衝區傳送

此流程針對順序 I/O 進行優化，網誌文章中有詳細說明與流程示意圖，正是促成 Kafka 高速表現的關鍵因素。

| 記錄組件        | 用途                                                                 |
|-----------------|----------------------------------------------------------------------|
| 時間戳記        | 記錄事件建立時間                                                     |
| 鍵值            | 確保排序、同址存放與保留策略，用於分區                               |
| 數值            | 包含實際資料內容                                                     |
| 標頭            | 提供額外資訊的選用元資料                                             |

#### 效能優化措施
多項設計決策提升 Kafka 速度：
- **僅追加日誌**：順序寫入檔案末端，最小化磁碟尋道時間，如同在日記本末頁添加條目，遠比在文件中間插入快速
- **零拷貝原則**：直接將資料從生產者傳輸至消費者，降低 CPU 負載，如同將貨箱從卡車直接運至倉庫，無需拆箱節省時間
- **批次處理**：以批次形式處理資料，降低單筆記錄的系統開銷，提升效率
- **非同步複製**：主節點代理伺服器在處理請求的同時更新副本，確保可用性不影響效能
- **分區機制**：將資料分散至多個分區實現平行處理，提升吞吐量，是處理大量資料的關鍵因素

如網誌文章所探討，這些優化措施使 Kafka 實現高吞吐量與低延遲，特別適合即時應用場景。

#### 結論與補充見解
Apache Kafka 的高速效能源自其精心設計的架構與效能優化措施，包括僅追加日誌、零拷貝原則、批次處理、非同步複製與高效分區機制。本分析基於影片內容並輔以網誌文章補充，提供了全面視角，對於預期簡單概述的讀者而言，其深度解析可能超出預期，揭示了使 Kafka 成為資料串流領域領導者的精妙設計平衡。

網誌文章同時提供 7 天免費試閱完整檔案庫，可透過[此訂閱連結](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80)取得，為有興趣的讀者提供更多資源。

此詳細探討確保完整理解，符合影片旨在教育 Kafka 效能知識的初衷，並參考多方來源的研究與見解，保證準確性與深度。

#### 主要參考文獻
- [《系統設計：Kafka 為何如此快速？》YouTube 影片](https://www.youtube.com/watch?v=UNUz1-msbOM)
- [《Kafka 為何如此快速？運作原理剖析》ByteByteGo 網誌文章](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)
- [Kafka 架構圖 ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png)
- [Kafka 複製機制圖 ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png)
- [Kafka 代理伺服器運作圖 ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png)
- [ByteByteGo 電子報訂閱（Kafka 文章）](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80)