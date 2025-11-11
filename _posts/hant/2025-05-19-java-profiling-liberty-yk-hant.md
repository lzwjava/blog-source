---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 使用YourKit Java分析器分析Liberty效能
translated: true
type: note
---

WebSphere Liberty 與 YourKit Java Profiler 的整合相當順暢，因為 Liberty 本身就是一個基於 JVM 的運行環境。以下是典型的運作方式：

---

### 1. 整合原理說明

YourKit Java Profiler 不需要專門的 Liberty 外掛程式；它透過附加到 Liberty 運行的 JVM 程序來進行分析。一旦附加成功，它就能攔截方法呼叫、記憶體分配、執行緒活動及其他運行時事件。
Liberty 運行在 OpenJ9（或 HotSpot）JVM 上，因此您可以透過在 Liberty 啟動時加入 YourKit 代理程式來啟用分析功能。

---

### 2. 附加 YourKit 代理程式

主要有兩種方式：

* **啟動時附加（建議用於伺服器）**
  將 YourKit 代理程式選項加入 Liberty 的 `jvm.options` 檔案（位於 `<wlp_home>/usr/servers/<server_name>/`）。
  範例：

  ```
  -agentpath:/path/to/yourkit/bin/linux-x86-64/libyjpagent.so=port=10001,listen=all
  ```

  這樣設定後，伺服器啟動時就會載入分析器代理程式。

* **隨需（動態）附加**
  若 Liberty 已在運行中，您可以透過 YourKit 圖形介面進行附加。它會掃描正在運行的 JVM 並讓您無需重啟即可連接。此方式對生產環境除錯很有用，但需要相關權限（相同使用者 / JDK tools.jar）。

---

### 3. Liberty 環境下的分析要點

在 Liberty 上運行時，您可能需要：

* **過濾應用程式套件**，避免被 Liberty 內部程式碼干擾分析結果。
* **使用呼叫樹 / 熱點視圖**來分析緩慢的 servlet、JAX-RS 端點或 CDI bean。
* **監控 JDBC 與執行緒池**，由於 Liberty 應用程式常依賴容器管理的資源，YourKit 可追蹤 JDBC 呼叫並測量等待時間。
* **處理多應用程式情境** – 若 Liberty 託管多個應用程式，請使用 YourKit 的執行緒與類別過濾功能，將分析範圍縮小至目標應用。

---

### 4. 效能注意事項

* 分析功能必然會帶來額外負荷。在開發環境可使用完整的 CPU/記憶體分析；在生產環境建議改用*取樣*模式而非插樁模式。
* Liberty 的模組化類別載入機制有時可能導致類別名稱重複；YourKit 通常能處理此情況，但過濾時仍需留意。
* 若使用 IBM JDK 搭配 Liberty，請確保下載專為 IBM J9/OpenJ9 建置的 YourKit 代理程式，而非僅適用於 HotSpot 的版本。

---

### 5. 典型工作流程

1. 在開發機器上安裝 YourKit。
2. 修改 Liberty 的 `jvm.options` 檔案，加入代理程式路徑。
3. 啟動 Liberty。
4. 從 YourKit 圖形介面連接至 Liberty JVM（透過通訊埠或附加方式）。
5. 分析您的端點、記憶體使用狀況或執行緒鎖定情形。
6. 儲存快照以供離線分析。

---

👉 是否需要我提供在 **OpenJ9**（Liberty 的預設 JVM）上搭配 YourKit 的**逐步設定範例**，包含針對 CPU 與記憶體分析的 `jvm.options` 設定範例？