---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Rust在大數據領域的潛力
translated: true
type: note
---

### Rust 適用於大數據 (#rust2018)

**作者：** Andy Grove  
**發佈日期：** 2018年1月28日  

這篇部落格文章是「#rust2018」倡議的一部分，是一篇前瞻性的文章，作者在其中分享了他對 Rust 在未來一年中角色的願景。Andy Grove 是一位一直使用 Apache Spark 構建分散式資料處理系統的開發者，他認為 Rust 因其在記憶體安全、效能和可預測性方面的核心優勢，具有顛覆大數據處理的潛力，而無需面對像 Java 這類語言中常見的垃圾回收或運行時開銷問題。

#### Rust 在大數據中的關鍵論點
Grove 從他接觸 Rust 的經歷開始講起：幾年前由一位同事介紹，並在參加了 2016 年的 RustConf 後被深深吸引。他讚揚 Rust 能夠消除常見的安全漏洞（如緩衝區溢位），同時提供類似 C 語言的速度。對於伺服器端工作，他特別強調了像 *futures* 和 *tokio* 這樣的 crate，用於構建可擴展的異步應用程式。但他真正的熱情在於大數據領域，Rust 可以在這裡解決現有工具中的痛點。

在他的日常工作中，Grove 使用 Apache Spark，它已成為分散式資料處理的首選工具，但最初只是一個簡單的學術項目，並通過卓越的工程修復進行了擴展。早期的 Spark 面臨以下問題：
- **Java 序列化開銷**：節點之間的資料洗牌速度慢且記憶體密集。
- **垃圾回收 (GC) 停頓**：這些導致效能不可預測，引發「記憶體不足」錯誤，需要不斷進行調優。

Spark 的「Project Tungsten」（約於 2014 年啟動）通過以下方式緩解了這些問題：
- 將資料以二進位格式（例如 Parquet 這樣的列式格式）儲存在堆外記憶體，以繞過 GC。
- 使用全階段程式碼生成，通過位元組碼優化 CPU 執行。

這些改變將瓶頸從 JVM 的特性轉移到了原始 CPU 的限制上，證明了效能提升來自於低層級的效率，而非高層級的抽象。

Grove 提出了一個大膽的假設：如果 Spark 從一開始就是用 Rust 構建的，即使是一個基礎的實現也能從一開始就確保效能和可靠性。Rust 的所有權模型確保了記憶體安全而無需 GC，避免了序列化膨脹和不穩定的停頓。不再需要調整 JVM 參數——只有可預測的快速執行。他認為這是 Rust 的「獨特機會」，可以超越像 Spark 這樣的現有技術，尤其是在資料量爆炸性增長的時代。

#### DataFusion 項目
為了將這一願景付諸實踐，Grove 啟動了 **DataFusion**，這是一個用 Rust 編寫的開源查詢引擎原型。在撰寫本文時（2018年初），它處於 alpha 階段，但已經展示了以下功能：
- 一個 **DataFrame API**，用於載入 Parquet 檔案並執行如篩選、連接和聚合等操作（範例：[parquet_dataframe.rs](https://github.com/andygrove/datafusion/blob/master/examples/parquet_dataframe.rs)）。
- 一個 **SQL API**，用於對相同資料進行聲明式查詢（範例：[parquet_sql.rs](https://github.com/andygrove/datafusion/blob/master/examples/parquet_sql.rs)）。

他計劃在 2018 年的空閒時間繼續開發，以提升他的 Rust 技能並構建一些有用的東西。他邀請社群貢獻，並指向該儲存庫：[github.com/apache/arrow-datafusion](https://github.com/apache/arrow-datafusion)。

#### 更新（截至 2024 年 5 月）
文章包含了一個回顧性的補充說明了 DataFusion 的發展：
- 於 2019 年 2 月捐贈給 Apache Arrow。
- Ballista（分散式執行層）於 2019 年 7 月宣布：[宣布 Ballista](https://andygrove.io/2019/07/announcing-ballista/)。
- 自行出版的書籍 *How Query Engines Work*（2020 年 2 月）闡釋了 DataFusion/Ballista 的內部原理：[Leanpub 連結](https://leanpub.com/how-query-engines-work)。
- Ballista 於 2021 年 4 月捐贈給 Apache Arrow。
- Apple 於 2024 年 3 月捐贈了 **DataFusion Comet**，以通過基於 Rust 的加速來增強 Spark：[Arrow 部落格](https://arrow.apache.org/blog/2024/03/06/comet-donation/) 和 [GitHub](https://github.com/apache/datafusion-comet)。
- Grove 於 2024 年 4 月加入 Apple，從事 Comet 的工作。
- DataFusion 於 2024 年 5 月畢業成為頂級 Apache 項目：[Arrow 部落格](https://arrow.apache.org/blog/2024/05/07/datafusion-tlp/)。

Grove 最後鼓勵讀者通過他的書籍深入了解查詢引擎，並將 Rust 定位為資料密集型應用的遊戲規則改變者。

[Rust 適用於大數據 (#rust2018)](https://andygrove.io/2018/01/rust-is-for-big-data/)