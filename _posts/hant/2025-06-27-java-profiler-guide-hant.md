---
audio: false
generated: true
lang: hant
layout: post
title: 精通YourKit Java Profiler：完整指南
translated: true
type: note
---

# YourKit Java Profiler 全面指南

YourKit Java Profiler 是一款功能強大的專業工具，專為協助開發人員與效能工程師分析及優化 Java 應用程式效能而設計。它能深入洞察 CPU 使用率、記憶體配置、執行緒活動等，成為診斷 Java 應用程式效能瓶頸與記憶體洩漏的必備工具。本指南將全面介紹 YourKit Java Profiler，包含其功能特色、設定方式、使用技巧與最佳實踐。

## 目錄
1. [YourKit Java Profiler 簡介](#yourkit-java-profiler-簡介)
2. [主要功能特色](#主要功能特色)
3. [系統需求與安裝](#系統需求與安裝)
4. [設定 YourKit Java Profiler](#設定-yourkit-java-profiler)
5. [使用 YourKit Java Profiler](#使用-yourkit-java-profiler)
6. [效能分析最佳實踐](#效能分析最佳實踐)
7. [應用場景](#應用場景)
8. [與開發工具整合](#與開發工具整合)
9. [授權與支援](#授權與支援)
10. [常見問題排解](#常見問題排解)
11. [結論](#結論)

## YourKit Java Profiler 簡介
YourKit Java Profiler 是由 YourKit LLC 開發的專業級效能分析工具，專為監控與優化執行於 Java EE 和 Java SE 平台上的 Java 應用程式效能而設計。開發人員廣泛使用此工具來識別效能瓶頸、記憶體洩漏、執行緒同步問題與低效程式碼。該分析器支援本地與遠端分析，適用於開發、測試與生產環境。憑藉其低負載設計、使用者友善介面與先進分析工具，YourKit 成為 Java 開發人員提升應用程式效能的首選工具。

## 主要功能特色
YourKit Java Profiler 提供完整的功能套件來診斷與優化 Java 應用程式。以下為主要功能特色：

### CPU 效能分析
- **呼叫樹與熱點分析**：透過呼叫樹或熱點清單視覺化方法執行時間，識別 CPU 密集型方法
- **火焰圖**：提供呼叫堆疊的視覺化呈現，快速定位效能瓶頸
- **智能假設分析**：無需重新分析即可評估潛在的效能改進
- **取樣與追蹤模式**：可選擇取樣模式（低負載）或追蹤模式（詳細分析），平衡效能與精確度

### 記憶體分析
- **物件堆積分析**：遍歷物件圖，檢查物件屬性，識別記憶體洩漏
- **記憶體保留路徑**：了解物件為何持續佔用記憶體，優化物件生命週期
- **快照比對**：比對記憶體快照，追蹤記憶體使用隨時間的變化
- **反混淆支援**：還原經過 ProGuard 或 Zelix KlassMaster 等工具混淆的原始類別、方法與欄位名稱

### 執行緒分析
- **執行緒活動視覺化**：監控執行緒狀態，偵測阻塞執行緒，分析同步問題
- **死結偵測**：自動識別死結並提供相關執行緒與監視器的詳細資訊
- **凍結執行緒檢視**：識別因長時間等待或潛在死結而處於非活動狀態的執行緒

### 例外分析
- **例外分析**：偵測與分析執行期間拋出的例外，包括因過度拋出例外導致的隱藏效能問題
- **例外火焰圖**：視覺化例外發生情況，識別問題區域

### 資料庫與 I/O 分析
- **SQL 與 NoSQL 支援**：分析 MongoDB、Cassandra 與 HBase 等資料庫的查詢，識別慢速查詢
- **HTTP 請求分析**：結合執行緒狀態與 HTTP 請求，了解請求處理效能
- **I/O 操作**：偵測低效 I/O 操作，優化資源使用

### 效能檢查
- **40+ 內建檢查項目**：自動識別常見問題，如洩漏的 webapps、重複物件、未關閉的 SQL 語句與低效集合
- **自訂檢查**：建立自訂探針以收集應用程式特定的效能數據

### 遙測與效能圖表
- **即時監控**：即時追蹤 CPU、記憶體、垃圾回收（GC）等指標
- **可自訂介面**：自訂 UI 以聚焦相關效能數據

### 整合與自動化
- **IDE 外掛**：與 Eclipse、IntelliJ IDEA 和 NetBeans 無縫整合，實現一鍵分析
- **命令列工具**：自動化分析任務，與 CI/CD 管道（如 Jenkins、TeamCity）整合
- **API 支援**：使用可擴展 API 以程式化方式管理分析模式與擷取快照

### 遠端分析
- **SSH 通道**：以最低設定安全地分析遠端應用程式
- **雲端與容器支援**：分析雲端、容器與叢集環境（如 Docker）中的應用程式

## 系統需求與安裝
### 系統需求
- **支援平台**：Windows、macOS、Linux、Solaris、FreeBSD（arm32、arm64、ppc64le、x64、x86）
- **Java 版本**：支援 Java 8 至 Java 24
- **JDK 需求**：需 JDK 1.5 或更新版本以執行分析器
- **硬體**：最低 2 GB RAM（大型應用程式建議 4 GB 或以上）

### 安裝步驟
1. **下載**：從官方網站（https://www.yourkit.com/java/profiler/download/）取得最新版 YourKit Java Profiler，提供 15 天免費試用
2. **安裝**：
   - **Windows**：執行安裝程式並依提示操作
   - **Linux/Solaris**：從安裝目錄執行 `yjp.sh` 腳本（`<YourKit Home>/bin/yjp.sh`）
   - **macOS**：解壓縮下載的應用程式並點擊圖示
3. **驗證安裝**：執行 `java -agentpath:<完整代理程式庫路徑> -version` 確認分析器代理程式正確載入

## 設定 YourKit Java Profiler
### 啟用分析功能
要分析 Java 應用程式，必須將 YourKit 分析器代理程式附加至 JVM。可手動操作或透過 IDE 整合完成。

#### 手動設定
1. **定位代理程式庫**：
   - 代理程式庫位於 `<YourKit Home>/bin/<平台>/libyjpagent.so`（Linux）或 `libyjpagent.dll`（Windows）
2. **設定 JVM**：
   - 將代理程式加入 JVM 啟動命令：
     ```bash
     java -agentpath:<完整代理程式庫路徑> YourMainClass
     ```
   - Linux 範例：
     ```bash
     java -agentpath:/home/user/yjp-2025.3/bin/linux-x86-64/libyjpagent.so YourMainClass
     ```
   - 可選參數：
     - `onexit=memory,dir=<路徑>`：在結束時擷取記憶體快照
     - `usedmem=70`：當記憶體使用達 70% 時觸發快照
3. **驗證代理程式載入**：
   - 檢查控制台輸出訊息，如 `[YourKit Java Profiler 2025.3] Profiler agent is listening on port 10001`

#### IDE 整合
1. 透過相應的外掛市集為您的 IDE（Eclipse、IntelliJ IDEA 或 NetBeans）安裝 YourKit 外掛
2. 設定外掛指向 YourKit 安裝目錄
3. 使用 IDE 的分析選項啟動附帶 YourKit 的應用程式

#### 遠端分析
1. **確保 SSH 存取**：需要對遠端伺服器的 SSH 存取權限
2. **複製代理程式**：
   - 將相應的代理程式庫複製到遠端伺服器
   - Docker 範例：
     ```bash
     docker cp libyjpagent.so <容器ID>:/path/to/agent
     ```
3. **啟動應用程式**：
   - 在遠端伺服器的 JVM 啟動命令中加入代理程式
4. **連接分析器 UI**：
   - 開啟 YourKit Profiler UI 並選擇「Profile remote Java server or application」
   - 輸入遠端主機與連接埠（預設：10001）或使用 SSH 通道
   - 測試連線並連接至應用程式

## 使用 YourKit Java Profiler
### 開始分析工作階段
1. **啟動分析器 UI**：
   - Windows：從開始功能表啟動
   - Linux/Solaris：執行 `<YourKit Home>/bin/yjp.sh`
   - macOS：點擊 YourKit Java Profiler 圖示
2. **連接至應用程式**：
   - 本地應用程式會顯示在「Monitor Applications」清單中
   - 遠端應用程式需按上述方式設定連線
3. **選擇分析模式**：
   - 從工具列選擇 CPU、記憶體或例外分析
   - 使用取樣模式進行低負載 CPU 分析，或追蹤模式進行詳細分析

### 分析 CPU 效能
1. **開始 CPU 分析**：
   - 從工具列選擇所需的分析模式（取樣或追蹤）
   - 結果會顯示在呼叫樹、火焰圖或方法清單等檢視中
2. **解讀結果**：
   - **呼叫樹**：顯示方法呼叫鏈與執行時間
   - **火焰圖**：以視覺化方式突顯 CPU 密集型方法
   - **熱點分析**：列出消耗最多 CPU 時間的方法
3. **使用觸發器**：根據高 CPU 使用率或特定方法呼叫自動開始分析

### 分析記憶體使用
1. **開始記憶體分析**：
   - 啟用記憶體分析以追蹤物件配置與垃圾回收
2. **檢查物件堆積**：
   - 遍歷物件圖以識別保留物件
   - 使用保留路徑尋找記憶體洩漏
3. **比對快照**：
   - 在不同時間點擷取快照並進行比對，識別記憶體增長情況

### 執行緒與死結分析
1. **監控執行緒**：
   - 檢視執行緒狀態，識別阻塞或凍結的執行緒
   - 檢查「Deadlocks」分頁以進行自動死結偵測
2. **分析監視器**：
   - 使用 Monitors 分頁檢查等待與阻塞事件
   - 使用 Monitor Flame Graph 視覺化競爭情況

### 例外與資料庫分析
1. **例外分析**：
   - 啟用例外分析以追蹤拋出的例外
   - 使用 Exception Tree 或 Flame Graph 分析例外模式
2. **資料庫分析**：
   - 監控 SQL/NoSQL 查詢以識別慢速或低效查詢
   - 結合執行緒狀態將資料庫呼叫與應用程式效能關聯

### 擷取與分析快照
1. **擷取快照**：
   - 使用 UI 或命令列工具：
     ```bash
     java -jar <YourKit Home>/lib/yjp-controller-api-redist.jar localhost 10001 capture-performance-snapshot
     ```
   - 快照預設儲存於 `<user home>/Snapshots`
2. **分析快照**：
   - 在 YourKit UI 中開啟快照進行離線分析
   - 匯出 HTML、CSV 或 XML 格式報告以供分享

## 效能分析最佳實踐
1. **最小化負載**：
   - 在生產環境使用取樣模式進行 CPU 分析以降低負載
   - 在高負載下避免啟用不必要的功能，如 J2EE 分析
2. **確保分析時長充足**：
   - 擷取足夠長時間的數據以識別間歇性問題，但避免過度收集數據
3. **聚焦關鍵指標**：
   - 優先關注 CPU 密集型方法、記憶體洩漏與執行緒競爭
4. **使用快照進行比對**：
   - 定期擷取與比對快照以追蹤效能變化
5. **善用自動化**：
   - 使用命令列工具與 CI/CD 管道整合，實現持續效能監控
6. **先在預備環境測試**：
   - 在生產環境使用前，先在預備環境練習分析以了解其影響

## 應用場景
- **效能優化**：識別與優化 CPU 密集型方法或慢速資料庫查詢
- **記憶體洩漏偵測**：尋找不必要保留在記憶體中的物件，優化垃圾回收
- **執行緒同步**：解決多執行緒應用程式中的死結與競爭問題
- **生產環境監控**：使用低負載分析在生產環境監控應用程式，不造成顯著效能影響
- **CI/CD 整合**：在建置管道中自動化效能測試，及早發現回歸問題

## 與開發工具整合
- **IDE 外掛**：YourKit 與 Eclipse、IntelliJ IDEA 和 NetBeans 整合，實現一鍵分析並可從分析結果導航至原始碼
- **CI/CD 工具**：支援 Jenkins、Bamboo、TeamCity、Gradle、Maven、Ant 與 JUnit 以實現自動化分析
- **Docker**：使用優化的代理程式二進位檔分析 Docker 容器中的應用程式
- **雲端環境**：使用 SSH 或 AWS CLI 整合分析 AWS、Azure 或其他雲端平台上的應用程式

## 授權與支援
- **授權選項**：
  - 個人或團隊使用的商業授權
  - 提供 15 天免費試用
  - 非商業開源專案免費授權
  - 教育與科學機構優惠授權
- **支援服務**：
  - 豐富線上文件：`<YourKit Home>/docs/help/index.html`
  - 透過論壇與電郵提供社群支援
  - 開源專案免費支援

## 常見問題排解
1. **代理程式載入失敗**：
   - 驗證代理程式路徑與相容性（例如 64 位元 JVM 使用 64 位元代理程式）
   - 檢查控制台錯誤訊息並參考排解指南
2. **分析負載過高**：
   - 切換至取樣模式進行 CPU 分析
   - 停用不必要的功能，如 J2EE 分析
3. **遠端分析連線問題**：
   - 確保 SSH 存取與正確的連接埠設定（預設：10001）
   - 檢查防火牆設定允許分析器通訊
4. **快照分析問題**：
   - 確保有足夠磁碟空間儲存快照
   - 使用 YourKit UI 開啟快照而非第三方工具

## 結論
YourKit Java Profiler 是一款多功能且強大的工具，用於診斷與優化 Java 應用程式效能。其完整的功能套件、低負載設計與對各種環境的支援，使其非常適合開發人員與效能工程師使用。透過遵循本指南中的設定與使用指引，您能有效運用 YourKit 來識別與解決效能瓶頸、記憶體洩漏與執行緒問題，最終提升 Java 應用程式的回應速度與擴展性。

如需更詳細資訊，請參考官方 YourKit 文件 https://www.yourkit.com/docs/java/，或透過 15 天免費試用獲取實務經驗。

---
**資料來源**：
- YourKit 官方網站：https://www.yourkit.com[](https://www.yourkit.com/java/profiler/)[](https://www.yourkit.com/java/profiler/features/)[](https://www.yourkit.com/)
- DevOpsSchool：https://www.devopsschool.com[](https://www.devopsschool.com/blog/what-is-yourkit-java-profiler-and-use-cases-of-yourkit-java-profiler/)
- Baeldung：https://www.baeldung.com[](https://www.baeldung.com/java-profilers)
- Jahia：https://www.jahia.com[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)[](https://www.jahia.com/fr/blog/analyzingsystemperformancewit)
- YourKit 文件：https://www.yourkit.com/docs/java/[](https://www.yourkit.com/docs/java-profiler/latest/help/enabling-profiling-manually.jsp)[](https://www.yourkit.com/docs/java-profiler/latest/help/cpu_profiling.jsp)[](https://www.yourkit.com/docs/java-profiler/latest/help/connect-to-profiled-application.jsp)
- MuleSoft 文件：https://docs.mulesoft.com[](https://docs.mulesoft.com/mule-runtime/latest/profiling-mule)