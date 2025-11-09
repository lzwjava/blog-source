---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: WebSphere WAS 中的熱部署
translated: true
type: note
---

### 理解 WebSphere Application Server (WAS) 中的熱部署與熱交換

熱部署（亦稱為熱重載或熱交換）是一種開發技術，允許您更新並部署應用程式的變更（例如程式碼、配置或資源），而無需完整重啟應用程式伺服器。這在迭代開發週期中尤其寶貴，因為頻繁的程式碼變更（例如修復錯誤、調整邏輯或更新 UI 元素）若因冗長的伺服器啟動時間而受阻，將會拖慢開發速度，特別是在像 IBM WebSphere Application Server (WAS) 這樣的企業環境中。重啟 WAS 實例可能需要數分鐘甚至更長時間（對於大型應用程式而言），這會中斷工作流程和測試。

您提供的片段聚焦於在 WAS 中實現更快迭代的實用策略，強調「展開式」WAR 部署和用於增強熱交換的工具。我將逐步分解說明，解釋概念、運作方式、其限制以及實作提示。

#### 1. 部署為「展開式」WAR（解壓縮部署）
WAR（Web Application Archive）檔案本質上是一個壓縮套件，包含您的 Web 應用程式資源：JSP、servlet、Java 類別、靜態檔案（HTML/CSS/JS）、函式庫（JAR）和配置檔案（例如 web.xml）。預設情況下，WAR 以**封裝式**（壓縮）檔案形式部署，WAS 將其視為不可變更 — 任何變更都需要重新封裝並重新部署整個歸檔檔案。

**展開式 WAR** 指的是在部署前將 WAR 檔案解壓縮（解壓縮）為目錄結構。這允許在伺服器的檔案系統上直接修改單個檔案或子目錄，而無需觸及整個歸檔檔案。

**為何它能實現更快迭代：**
- **檔案層級更新：** 您可以編輯單個 JSP 或 Java 類別檔案，WAS 可以偵測並僅重新載入該元件。
- **無需重新封裝：** 避免重複壓縮/解壓縮大型 WAR 檔案的額外負擔。
- **與熱重載協同作用：** 使伺服器更容易監控並重新整理已變更的檔案。

**如何在 WAS 中部署展開式 WAR：**
- **使用管理主控台：**
  1. 登入 WAS Integrated Solutions Console（通常位於 `http://localhost:9060/ibm/console`）。
  2. 導覽至 **Applications > New Application > New Enterprise Application**。
  3. 不要選擇封裝的 WAR 檔案，而是指向您解壓縮 WAR 的根目錄（例如 `/path/to/myapp.war/` — 注意尾隨斜線表示它是一個目錄）。
  4. 完成部署精靈，確保「Deploy Web services」和其他選項符合您的應用程式。
- **使用 wsadmin（指令碼工具）：**
  ```bash
  wsadmin.sh -c "AdminApp.install('/path/to/myapp', '[ -MapWebModToVH [[myapp .* default_host.* virtual_host ]]]')"
  ```
  將 `/path/to/myapp` 替換為您的展開式目錄。
- **開發伺服器（例如 Liberty Profile）：** 為了更輕量的測試，使用 Open Liberty（一個 WAS 變體）搭配 `server start`，並將您的展開式應用程式放置在 `dropins` 資料夾中以實現自動部署。

**最佳實踐：**
- 使用原始碼控制工具（例如 Git）將變更從您的 IDE 同步到展開式目錄。
- 監控磁碟空間，因為展開式部署會消耗更多儲存空間。
- 在生產環境中，堅持使用封裝式 WAR 以確保安全性和一致性 — 熱部署主要用於開發/測試。

一旦以展開式部署，WAS 的內建機制就可以啟動以進行部分熱重載。

#### 2. WAS 的內建熱重載支援
WAS 原生支援對某些元件進行熱重載而無需完整重啟，但功能有限。這依賴於伺服器的**檔案輪詢**機制，WAS 會定期掃描展開式部署目錄以尋找變更（可透過 JVM 參數配置，例如 `-DwasStatusCheckInterval=5` 表示每 5 秒檢查一次）。

**WAS 開箱即用支援的內容：**
- **JSP（JavaServer Pages）：**
  - JSP 在首次存取時會動態編譯成 servlet。如果您在展開式 WAR 中修改了 JSP 檔案，WAS 可以偵測到變更、重新編譯並重新載入該 servlet。
  - **運作方式：** 在 `ibm-web-ext.xmi`（位於 WEB-INF 下）中將 `reloadInterval` 設為較低的值（例如 1 秒）以進行頻繁檢查。或者使用全域設定：**Servers > Server Types > WebSphere application servers > [您的伺服器] > Java and Process Management > Process definition > Java Virtual Machine > Custom properties**，並設定 `com.ibm.ws.webcontainer.invokefilterscompatibility=true`。
  - **限制：** 僅適用於未被積極快取的 JSP。具有包含或標籤的複雜 JSP 可能需要模組重啟。
- **某些 Java 類別（servlet 和 EJB）：**
  - 對於展開式部署，如果個別類別檔案位於 WEB-INF/classes 或 lib 目錄中，WAS 可以重新載入它們。
  - **運作方式：** 在部署描述符中或透過主控台啟用「Application reload」：**Applications > [您的應用程式] > Manage Modules > [模組] > Reload behavior > Reload enabled**。
  - 這會觸發**模組層級重載**，比完整應用程式重啟更快，但仍會卸載/重新載入整個模組（例如您的 Web 應用程式）。

**內建支援的限制：**
- **非真正的熱交換：** 對核心應用程式邏輯的變更（例如修改運行中 servlet 類別中的方法）若沒有卸載舊的類別載入器則不會生效。您可能會看到 `ClassNotFoundException` 或陳舊的程式碼。
- **狀態遺失：** 工作階段、單例或資料庫連線可能會重設。
- **IBM JDK 特殊性：** WAS 通常使用 IBM 的 JDK，其在類別重新載入方面與 OpenJDK/HotSpot 相比有其特殊性。
- **不支援結構性變更：** 新增類別、變更方法簽章或更新註解需要重啟。
- **效能開銷：** 頻繁的輪詢可能會在開發中耗用資源。

對於基本的 UI 調整（JSP 編輯）或簡單的類別更新，這已經足夠且免費。但對於「完整熱交換」— 您可以在執行中編輯運行中的程式碼而無需任何重載 — 您需要第三方工具。

#### 3. 完整熱交換解決方案
要實現無縫的程式碼變更（例如在附加偵錯程式的 IDE 如 Eclipse 或 IntelliJ 中編輯方法主體，並立即看到應用），請使用能修補 JVM 類別載入和檢測的外掛程式。

**選項 1：JRebel（付費外掛程式）**
- **它是什麼：** 來自 Perforce（前身為 ZeroTurnaround）的商業工具，提供 Java 應用程式的全面熱交換功能。它在啟動時檢測您的位元組碼，允許重新載入類別、資源，甚至框架特定的變更（例如 Spring bean、Hibernate 實體）。
- **為何在 WAS 中使用它：**
  - 與 WAS 深度整合，包括對展開式 WAR、OSGi 套件和 IBM JDK 的支援。
  - 處理複雜情境，例如變更方法簽章或新增欄位（超越標準 JVMTI 熱交換限制）。
  - **功能：** 自動偵測來自您 IDE 的變更；無需手動重新部署；保留應用程式狀態。
- **如何設定：**
  1. 從官方網站下載 JRebel 並安裝為 Eclipse/IntelliJ 外掛程式。
  2. 為您的專案生成 `rebel.xml` 配置檔案（自動生成或手動）。
  3. 將 JVM 參數新增到您的 WAS 伺服器：`-javaagent:/path/to/jrebel.jar`（代理 JAR 的完整路徑）。
  4. 在偵錯模式下啟動 WAS（`-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=8000`）。
  5. 附加您的 IDE 偵錯程式並編輯程式碼 — JRebel 即時同步變更。
- **成本：** 訂閱制（個人約每年 400 美元/使用者；企業授權有所不同）。提供免費試用。
- **優點：** 可靠、使用者友好、出色的 WAS 支援。
- **缺點：** 付費；每個專案都需要設定。

**選項 2：DCEVM + HotSwapAgent（免費替代方案）**
- **它是什麼：** 一個用於進階熱交換的開源組合。
  - **DCEVM（Dynamic Code Evolution VM）：** 一個修改過的 JVM，擴展了 HotSpot 的 JVMTI（Java Virtual Machine Tool Interface）以允許更積極的類別重新定義（例如新增/移除方法、變更階層結構）。
  - **HotSwapAgent：** 一個建構在 DCEVM 之上的代理，提供用於自動類別重新載入的 IDE 整合。
- **為何在 WAS 中使用它：**
  - 免費且功能強大，用於開發，模仿 JRebel 的功能。
  - 支援方法主體變更、資源更新，甚至某些框架重載（透過外掛程式）。
- **與 WAS 的 IBM JDK 的相容性注意事項：**
  - WAS 通常隨附 IBM 的 J9 JDK，其**不原生支援 DCEVM**（DCEVM 是 HotSpot 特定的）。
  - **解決方法：** 在開發時切換到 OpenJDK/HotSpot（例如透過 `setInitial.sh` 中的 `JAVA_HOME` 覆寫或 Liberty 的 `jvm.options`）。徹底測試 — IBM JDK 的垃圾回收和安全功能可能有所不同。
  - 在生產環境中，切換回 IBM JDK；這僅用於開發。
- **如何設定：**
  1. **安裝 DCEVM：**
     - 從 GitHub 下載 DCEVM 修補程式 JAR（例如 `dcevm-11.0.0+7-full.jar` 用於 JDK 11+）。
     - 執行：`java -jar dcevm.jar /path/to/your/jdk/jre/lib/server/jvm.dll server`（Windows）或 Linux 的等效指令（`libjvm.so`）。
     - 這會修補您的 JDK 的 JVM 二進位檔 — 請先備份！
  2. **安裝 HotSwapAgent：**
     - 從 GitHub 下載 `hotswap-agent.jar`。
     - 新增到 WAS JVM 參數：`-XXaltjvm=dcevm -XX:+TraceClassLoading -javaagent:/path/to/hotswap-agent.jar=DCEVM`（加上任何外掛程式，例如 `=hotswap-spring` 用於 Spring）。
  3. **IDE 整合：**
     - 為 IntelliJ/Eclipse 安裝 HotSwapAgent 外掛程式。
     - 使用上述偵錯參數啟動 WAS。
     - 在 IDE 中編輯並儲存程式碼 — 代理會自動重新載入。
  4. **測試相容性：**
     - 執行冒煙測試：部署一個簡單的 servlet，編輯一個方法（例如新增一行日誌），呼叫端點，並驗證變更無需重啟。
     - 檢查日誌中是否有錯誤，例如 `HotSwap failed: method limit reached`（DCEVM 對每個類別的變更次數有限制）。
- **優點：** 免費、可自訂（透過 Spring、CDI 等的外掛程式）、社群支援。
- **缺點：** 設定繁瑣；與非標準 JVM 可能存在不穩定性；僅限於 HotSpot（仔細測試 IBM JDK 切換）；不如 JRebel 精緻。

#### 何時使用哪種方案
- **展開式 WAR + 內建重載：** 用於早期開發中的快速 JSP/靜態檔案調整。
- **JRebel：** 如果預算允許且您需要企業級的可靠性。
- **DCEVM + HotSwapAgent：** 用於免費的完整熱交換，但需分配時間進行 JVM 相容性測試。

總而言之，這些技術將 WAS 從一個重量級伺服器轉變為更敏捷的開發環境，將迭代時間從數分鐘縮短到數秒。從展開式 WAR 開始以獲得立竿見影的效果，然後根據需要疊加工具。如果您遇到特定錯誤，請分享更多詳細資訊以進行疑難排解。

**參考資料：**  
[JRebel Documentation for WebSphere](https://www.jrebel.com/products/jrebel/tutorials/deploy-jrebel-websphere)  
[DCEVM GitHub Repo](https://github.com/dcevm/dcevm)  
[HotSwapAgent GitHub Repo](https://github.com/HotswapProjects/HotswapAgent)  
[IBM Knowledge Center: WebSphere Hot Deployment](https://www.ibm.com/docs/en/was/9.0.5?topic=applications-hot-deployment)