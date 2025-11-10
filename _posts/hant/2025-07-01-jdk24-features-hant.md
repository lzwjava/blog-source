---
audio: false
generated: true
lang: hant
layout: post
title: JDK 24：主要功能與更新
translated: true
type: note
---

### JDK 24 簡介

Java 開發工具包 (JDK) 24 是 Java SE（標準版）平台的功能版本，於 2025 年 3 月 18 日正式發布，作為 Java 社區進程中 JSR 399 指定的第 24 版參考實現。它延續了 Oracle 每六個月發布一次的節奏，提供了一系列強大的增強功能，以提升開發者生產力、性能和安全性。JDK 24 包含 24 項 JDK 增強提案 (JEP)，是自 2018 年基於時間的發布計劃開始以來功能數量最多的一次，使其成為 Java 演進中的重要里程碑。它是邁向 JDK 25（下一個長期支援版本，計劃於 2025 年 9 月發布）的墊腳石。[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://openjdk.org/projects/jdk/24/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### 長期支援 (LTS) 狀態

JDK 24 **並非**長期支援 (LTS) 版本。它是一個短期支援版本，僅獲得 Oracle 為期六個月的 Premier 級別支援，直至 2025 年 9 月被 JDK 25 取代。相比之下，LTS 版本（如 JDK 21（2023 年 9 月發布）和即將到來的 JDK 25（2025 年 9 月發布））則獲得至少五年的 Premier 支援，這使得它們成為企業穩定性的首選。Oracle 的 LTS 節奏每兩年進行一次，JDK 21 是最近的 LTS 版本，JDK 25 將是下一個。[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)

### 發布與穩定性

JDK 24 是一個**穩定、可供生產環境使用的版本**，已於 2025 年 3 月 18 日達到正式可用 (GA) 狀態。可供生產環境使用的二進位檔案已由 Oracle 根據 Oracle 免費條款與條件 (NFTC) 以及適用於 OpenJDK 的 GNU 通用公共許可證 (GPLv2) 提供，其他供應商的二進位檔案也將隨後推出。該版本除了 24 項 JEP 外，還包含超過 3,000 個錯誤修復和較小的增強功能，確保了通用穩定性。然而，作為一個非 LTS 版本，它主要面向渴望測試新功能的開發者，而非需要長期穩定性的企業。[](https://openjdk.org/projects/jdk/24/)[](https://www.theregister.com/2025/03/18/oracle_jdk_24/)[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)

### JDK 24 的新功能

JDK 24 引入了 24 項 JEP，分為核心庫增強、語言改進、安全功能、HotSpot JVM 優化和 Java 工具。其中，14 項是永久功能，七項是預覽功能，兩項是實驗性功能，一項是孵化器模組。以下是一些最值得注意的功能，重點關注與開發者和部署相關的部分：

1.  **Stream Gatherers (JEP 485)** - 永久
    - 通過引入 `Gatherer` 介面增強 Stream API，允許開發者為流管道定義自定義的中間操作。這使得數據轉換更加靈活，補充了現有用於終端操作的 `Collector` 介面。
    - 範例：使用 `StreamGatherers.groupBy` 按長度分組單詞。
    - 好處：簡化開發者的複雜流處理。[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

2.  **Ahead-of-Time Class Loading & Linking (JEP 483)** - 實驗性
    - 作為 Project Leyden 的一部分，此功能通過在準備階段將類預先加載和連結到快取中，來減少 Java 應用程式的啟動時間。快取在運行時被重複使用，繞過了昂貴的類加載步驟。
    - 好處：改善雲端和微服務應用的性能。[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

3.  **Compact Object Headers (JEP 450)** - 實驗性
    - 作為 Project Lilliput 的一部分，此功能將 64 位元架構上的 Java 物件標頭大小從 96–128 位元減少到 64 位元，降低了堆使用量並提高了記憶體效率。
    - 好處：減少記憶體佔用並增強數據局部性以提升性能。[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)[](https://www.happycoders.eu/java/java-24-features/)

4.  **Generational Shenandoah Garbage Collector (JEP 404)** - 永久
    - 將 Shenandoah GC 的世代模式從實驗性過渡為產品功能，通過將物件分為年輕代和年老代來提高吞吐量、負載峰值恢復能力和記憶體利用率。
    - 好處：增強對要求苛刻工作負載的性能。[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.infoworld.com/article/3846172/jdk-25-the-new-features-in-java-25.html)

5.  **Module Import Declarations (JEP 494)** - 第二個預覽
    - 簡化模組化編程，允許直接導入模組導出的所有套件，而無需 `module-info.java` 檔案（例如，`import module java.sql;`）。
    - 好處：減少輕量級應用和指令碼的開銷，有助於初學者和快速原型設計。[](https://codefarm0.medium.com/java-24-features-a-deep-dive-into-whats-coming-81e77382b39c)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

6.  **Flexible Constructor Bodies (JEP 492)** - 第三個預覽
    - 允許在建構函式中於 `super()` 或 `this()` 呼叫之前放置語句，使得欄位初始化邏輯可以更自然地放置，而無需輔助方法。
    - 好處：提高程式碼可靠性和可讀性，特別是在子類化時。[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

7.  **Key Derivation Function (KDF) API (JEP 487)** - 預覽
    - 引入了用於密碼學金鑰派生函數（如基於 HMAC 的提取與擴展以及 Argon2）的 API，支援安全密碼雜湊以及與密碼學硬體的互動。
    - 好處：增強需要進階密碼學的應用程式的安全性。[](https://www.jrebel.com/blog/whats-new-java-24)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

8.  **Permanently Disable the Security Manager (JEP 486)** - 永久
    - 移除了在 JDK 17 中已棄用的 Security Manager，因為它不再是保護 Java 應用程式的主要手段（已被基於容器的沙箱取代）。
    - 注意：依賴 Security Manager 的應用程式可能需要進行架構更改。[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

9.  **Late Barrier Expansion for G1 Garbage Collector (JEP 464)** - 永久
    - 通過將屏障擴展移至編譯管道的後期來簡化 G1 GC 的屏障實現，從而減少編譯時間並提高可維護性。
    - 好處：增強使用 G1 GC 的應用程式的性能。[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

10. **Quantum-Resistant Cryptography (JEP 452, 453)** - 預覽
    - 引入了基於模組-晶格的密鑰封裝機制 (ML-KEM) 和數位簽章演算法 (ML-DSA)，以抵禦量子計算攻擊。
    - 好處：為 Java 應用程式提供後量子安全性的未來保障。[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

11. **Scoped Values (JEP 480)** - 第四個預覽
    - 能夠在執行緒內部和跨執行緒之間比執行緒局部變數更安全地共享不可變數據，改善並行處理。
    - 好處：簡化對並行程式碼的理解。[](https://www.jrebel.com/blog/whats-new-java-24)

12. **Deprecate 32-bit x86 Port (JEP 501)** - 永久
    - 棄用 32 位元 x86 端口，計劃在 JDK 25 中移除，並以架構無關的 Zero 端口作為 32 位元系統的替代方案。
    - 好處：減少維護開銷，專注於現代架構。[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

13. **Vector API (JEP 489)** - 第九個孵化器
    - 持續完善用於 SIMD 編程的 Vector API，增強了跨通道和算術運算。
    - 好處：改善計算密集型應用的性能。[](https://www.infoq.com/news/2025/02/java-24-so-far/)

14. **Linking Run-Time Images without JMODs (JEP 493)** - 永久
    - 允許 `jlink` 工具在沒有 JMOD 檔案的情況下建立自訂運行時映像，將 JDK 大小減少約 25%。
    - 好處：提高自訂 Java 運行時的部署效率。[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### 補充說明

-   **預覽和實驗性功能**：許多功能（例如 Scoped Values、KDF API）處於預覽或實驗階段，允許開發者進行測試並提供回饋，然後它們才能在 JDK 25 或更高版本中成為永久功能。這些功能在最終確定之前可能會發生變化。[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.infoq.com/news/2025/02/java-24-so-far/)
-   **專案整合**：JDK 24 引入了 OpenJDK 專案的元素，如 Leyden（啟動優化）、Lilliput（記憶體效率）和 Panama（原生互操作性），為未來的增強奠定了基礎。[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)
-   **安全性與棄用**：像移除 Security Manager 和棄用 32 位元 x86 端口這樣的功能，反映了 Oracle 通過淘汰過時組件來實現 Java 現代化的重點。[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### 結論

JDK 24 是一個穩定、功能豐富的版本，它提升了 Java 的性能、開發者生產力和安全性。雖然它不是 LTS 版本，但其 24 項 JEP 帶來了顯著的改進，其中許多將在即將到來的 LTS 版本 JDK 25 中最終確定。開發者可以利用像 Stream Gatherers 和 Module Import Declarations 這樣的功能來獲得即時的生產力提升，而像 Compact Object Headers 和 Ahead-of-Time Class Loading 這樣的實驗性功能則標誌著 Java 正在持續為現代工作負載進行優化。對於企業使用，由於其延長的支援期，建議堅持使用 LTS 版本（如 JDK 21）或等待 JDK 25。[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

欲了解更多詳情，請訪問：
-   [Oracle JDK 24 發布說明](https://www.oracle.com)[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)
-   [OpenJDK JDK 24](https://openjdk.org)[](https://openjdk.org/projects/jdk/24/)
-   [JavaOne 2025 大會](https://www.oracle.com/javaone) 了解功能亮點[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)