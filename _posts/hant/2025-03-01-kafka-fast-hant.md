---
audio: false
lang: hant
layout: post
title: 為什麼 Kafka 這麼快
translated: true
---

### 主要要點
- 影片「系統設計：為什麼 Kafka 這麼快？」似乎通過其架構和設計選擇來解釋 Apache Kafka 的速度。
- 研究表明，Kafka 的性能得益於追加日誌、零拷貝原則、批處理和高效分區。
- 證據顯示，Kafka 的速度源於其分佈式事件流平台設計，關鍵組件包括生產者、代理和消費者。

### 介紹
本博客文章基於 ByteByteGo 的 YouTube 影片「系統設計：為什麼 Kafka 這麼快？」的內容，旨在將其見解轉化為書面格式，以便更容易閱讀和參考。Apache Kafka 以其在實時數據處理中的高性能而聞名，本文探討了其速度背後的原因，使其對於新手更加易於理解。

### Kafka 的核心組件
Apache Kafka 作為一個分佈式事件流平台，具有三個主要組件：
- **生產者**：將數據發送到 Kafka 主題的應用程序。
- **代理**：存儲和管理數據，確保複製和分佈。
- **消費者**：從主題讀取和處理數據的應用程序。

這種結構使 Kafka 能夠高效處理大量數據，從而提高其速度。

### 架構層和性能優化
Kafka 的架構分為兩層：
- **計算層**：包括生產者、消費者和流處理的 API，促進交互。
- **存儲層**：由代理組成，管理主題和分區中的數據存儲，優化性能。

關鍵優化包括：
- **追加日誌**：將數據順序寫入文件末尾，比隨機寫入更快。
- **零拷貝原則**：直接將數據從生產者傳輸到消費者，減少 CPU 開銷。
- **批處理**：以批次處理數據以降低每條記錄的開銷。
- **非同步複製**：允許主代理在副本更新時處理請求，確保可用性而不影響性能。
- **分區**：將數據分佈到多個分區以進行並行處理和高吞吐量。

這些設計選擇，詳細說明在 ByteByteGo 的支持博客文章中（[為什麼 Kafka 這麼快？它是如何工作的？](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)），解釋了 Kafka 在速度和可擴展性方面的卓越表現。

### 數據流和記錄結構
當生產者將記錄發送到代理時，它會被驗證、追加到磁盤上的提交日誌，並進行複製以保證持久性，生產者在提交後會收到通知。這個過程優化了順序 I/O，提高了性能。

每條記錄包括：
- 時間戳：事件創建的時間。
- 鍵：用於分區和排序。
- 值：實際數據。
- 標頭：可選的元數據。

這種結構，如博客文章所述，確保了高效的數據處理，並有助於 Kafka 的速度。

---

### 調查筆記：詳細分析 Apache Kafka 的性能

本節提供了對 Apache Kafka 性能的全面探討，擴展了 ByteByteGo 的影片「系統設計：為什麼 Kafka 這麼快？」的內容，並引用了其他資源以確保全面理解。分析結構涵蓋了 Kafka 的架構、組件和具體優化，並提供了詳細的說明和示例以便於理解。

#### 背景和上下文
Apache Kafka 作為一個分佈式事件流平台，以其能夠處理高吞吐量、低延遲的數據流而聞名，成為現代數據架構的重要組成部分。該影片於 2022 年 6 月 29 日發布，是系統設計播放列表的一部分，旨在解釋 Kafka 為什麼這麼快，這是一個重要話題，因為數據流需求的指數增長。本分析基於 ByteByteGo 的詳細博客文章（[為什麼 Kafka 這麼快？它是如何工作的？](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)），該文章補充了影片內容並提供了額外的見解。

#### Kafka 的核心組件和架構
Kafka 的速度始於其核心組件：
- **生產者**：這些是生成並將事件發送到 Kafka 主題的應用程序或系統。例如，網絡應用程序可能會生成用戶交互事件。
- **代理**：這些是組成集群的服務器，負責存儲數據、管理分區和處理複製。典型設置可能包括多個代理以實現容錯和可擴展性。
- **消費者**：訂閱主題以讀取和處理事件的應用程序，例如實時數據分析引擎。

架構將 Kafka 定位為一個事件流平台，使用「事件」而不是「消息」，區別於傳統的消息隊列。這在其設計中體現出來，事件是不可變的，並按偏移量在分區中排序，如博客文章所述。

| 組件       | 角色                                                                 |
|------------|----------------------------------------------------------------------|
| 生產者    | 將事件發送到主題，啟動數據流。                                    |
| 代理      | 存儲和管理數據，處理複製，並為消費者提供服務。                     |
| 消費者    | 從主題讀取和處理事件，使實時分析成為可能。                         |

博客文章包含一個圖表，位於 [這個 URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png)，說明了這種架構，顯示了生產者、代理和消費者在集群模式下的交互。

#### 層次架構：計算和存儲
Kafka 的架構分為：
- **計算層**：通過 API 促進通信：
  - **生產者 API**：用於應用程序發送事件。
  - **消費者 API**：用於讀取事件。
  - **Kafka Connect API**：與外部系統（如數據庫）集成。
  - **Kafka Streams API**：支持流處理，例如為主題（如「訂單」）創建 KStream，使用 Serdes 進行序列化，並使用 ksqlDB 進行流處理作業，並通過 REST API。提供的示例是訂閱「訂單」，按產品聚合，並將其發送到「按產品訂單」以進行分析。
- **存儲層**：由集群中的 Kafka 代理組成，數據組織在主題和分區中。主題類似於數據庫表，分區分佈在節點上，確保可擴展性。分區中的事件按偏移量排序，不可變，追加日誌，刪除被視為事件，增強寫入性能。

博客文章詳細說明了這一點，指出代理管理分區、讀取、寫入和複製，並包含一個圖表，位於 [這個 URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png)，說明了複製，例如「訂單」中的分區 0 具有三個副本：主代理在代理 1 上（偏移量 4），副本在代理 2 上（偏移量 2）和代理 3 上（偏移量 3）。

| 層次           | 描述                                                                 |
|----------------|-----------------------------------------------------------------------------|
| 計算層         | 交互 API：生產者、消費者、連接、流和 ksqlDB。                     |
| 存儲層         | 集群中的代理，主題/分區分佈，事件按偏移量排序。                     |

#### 控制和數據平面
- **控制平面**：管理集群元數據，歷史上使用 Zookeeper，現在已被 KRaft 模塊取代，選定代理上的控制器。這一簡化消除了 Zookeeper，使配置更加簡單，並通過特殊主題使元數據傳播更加高效，如博客文章所述。
- **數據平面**：處理數據複製，過程中副本發出 FetchRequest，主代理發送數據，並在某個偏移量之前提交記錄，確保一致性。分區 0 的偏移量 2、3 和 4 的示例突出了這一點，並包含一個圖表，位於 [這個 URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png)。

#### 記錄結構和代理操作
每條記錄，即事件的抽象，包括：
- 時間戳：創建時。
- 鍵：用於排序、共存和保留，對分區至關重要。
- 值：數據內容。
- 標頭：可選的元數據。

鍵和值是字節數組，使用 Serdes 編碼/解碼，確保靈活性。代理操作包括：
- 生產者請求到達套接字接收緩衝區。
- 網絡線程將其移動到共享請求隊列。
- I/O 線程驗證 CRC，將其追加到提交日誌（磁盤段，包含數據和索引）。
- 請求存儲在 purgatory 中進行複製。
- 响應排隊，網絡線程通過套接字發送緩衝區。

這個過程，優化了順序 I/O，如博客文章所述，並包含圖表說明流程，對 Kafka 的速度有顯著貢獻。

| 記錄組件 | 目的                                                                 |
|----------|-------------------------------------------------------------------------|
| 時間戳  | 記錄事件創建的時間。                                             |
| 鍵      | 確保排序、共存和保留以進行分區。                               |
| 值      | 包含實際數據內容。                                             |
| 標頭    | 可選的元數據以提供額外信息。                                   |

#### 性能優化
幾個設計決策增強了 Kafka 的速度：
- **追加日誌**：將數據順序寫入文件末尾，最小化磁盤尋道時間，類似於在日記末尾添加條目，比在中間插入更快。
- **零拷貝原則**：直接將數據從生產者傳輸到消費者，減少 CPU 開銷，就像將箱子從卡車移到倉庫而不拆開，節省時間。
- **批處理**：以批次處理數據降低每條記錄的開銷，提高效率。
- **非同步複製**：主代理在副本更新時處理請求，確保可用性而不影響性能。
- **分區**：將數據分佈到分區以進行並行處理，增加吞吐量，這是處理大數據量的關鍵因素。

這些優化，如博客文章所述，是 Kafka 實現高吞吐量和低延遲的原因，使其適合實時應用。

#### 結論和額外見解
Apache Kafka 的速度是其精心設計的架構和性能優化的結果，利用追加日誌、零拷貝原則、批處理、非同步複製和高效分區。本分析基於影片並補充了博客文章，提供了全面的視角，意外地深入，對於期望簡單概述的人來說，揭示了設計選擇的微妙平衡，使 Kafka 成為數據流的領導者。

博客文章還提供了 7 天的免費試用，以獲取完整的檔案，可通過 [這個訂閱鏈接](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80)訪問，為有興趣的人提供更多資源。

這種詳細的探討確保了全面理解，與影片的意圖一致，即教育 Kafka 的性能，並基於從各種來源收集的研究和見解，確保準確性和深度。

#### 關鍵引用
- [系統設計：為什麼 Kafka 這麼快？YouTube 影片](https://www.youtube.com/watch?v=UNUz1-msbOM)
- [為什麼 Kafka 這麼快？它是如何工作的？ByteByteGo 博客文章](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)
- [Kafka 架構圖 ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png)
- [Kafka 復制圖 ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png)
- [Kafka 代理操作圖 ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png)
- [ByteByteGo 訂閱 Kafka 文章](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80)