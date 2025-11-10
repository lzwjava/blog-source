---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Python API 測試指南之 JaCoCo
translated: true
type: note
---

好問題——這是一個典型的 **Java 程式碼覆蓋率工具**（JaCoCo）與 **非 Java 測試框架**（例如使用 Python `unittest` 呼叫你的 REST 端點）之間的整合問題。

---

### 為什麼 JaCoCo 能與 JUnit 協作，卻無法直接與 Python 測試配合

* JaCoCo 透過將 **Java 代理程式**（`-javaagent:jacocoagent.jar`）附加到 JVM 來運作。
* 當你的測試在 **同一個 JVM 內** 執行時（例如 JUnit、TestNG 等），JaCoCo 能夠偵測到哪些類別和方法被載入/執行，並生成詳細的覆蓋率報告。
* 如果你使用 Python `unittest` + `requests` 來呼叫你的 API 端點，你是在 **從 JVM 外部** 對 **運行中的伺服器** 進行測試。
  這意味著 JaCoCo 無法自動偵測到覆蓋率，除非伺服器進程本身已附加了代理程式。

---

### 如何透過 JaCoCo 與 Python 測試獲得準確的覆蓋率

你無需轉用 JUnit。你仍然可以使用 JaCoCo，但必須 **將代理程式附加到運行你的大型 Java 專案（伺服器）的 JVM**，而不是附加到測試執行器。

1. **使用 JaCoCo 代理程式運行你的 Java 應用程式**
   將代理程式加入你的 Java 伺服器啟動指令中：

   ```bash
   java -javaagent:/path/to/jacocoagent.jar=destfile=jacoco-it.exec,output=file,append=false \
        -jar myserver.jar
   ```

   這將在你的 Python 測試呼叫端點時收集執行資料（`jacoco-it.exec`）。

2. **正常運行你的 Python 測試**

   ```bash
   python -m unittest discover tests/
   ```

   由於伺服器已附加代理程式並在運行中，所有透過 HTTP 請求觸及的類別和方法都會被記錄下來。

3. **關閉伺服器**
   `.exec` 檔案將被寫入並儲存。

4. **生成覆蓋率報告**
   使用 Maven 插件或 CLI 將 `.exec` 檔案轉換為 HTML/XML 報告：

   ```bash
   mvn jacoco:report -Djacoco.dataFile=jacoco-it.exec
   ```

   或使用 CLI：

   ```bash
   java -jar jacococli.jar report jacoco-it.exec \
        --classfiles target/classes \
        --sourcefiles src/main/java \
        --html report
   ```

---

### 使用 JaCoCo 的兩種測試模式

* **單元測試（在 JVM 內使用 JUnit）：** 可與 Maven 插件（`prepare-agent` + `report`）開箱即用。
* **整合測試（外部客戶端如 Python）：** 需要啟動附加了代理程式的 JVM，然後將 `.exec` 資料合併回報告中。

---

### 關於你的 log4j 想法

透過統計每個檔案的日誌語句來計算覆蓋率是非常粗略的：

* 並非每個方法都會記錄日誌。
* 日誌無法涵蓋條件判斷或分支。
* 覆蓋率不可靠。

相比之下，JaCoCo 能測量 **類別、方法、行和分支覆蓋率**——精細度更高。

---

✅ **答案：** 是的，即使你的測試使用 Python，你絕對可以採用 JaCoCo 的方法。關鍵在於 **將 JaCoCo 附加到受測的 Java 進程（你的伺服器）**，而不是測試執行器。然後在事後生成報告。這樣你就能獲得與使用 JUnit 時相同的方法級和分支級覆蓋率。

---

需要我為你草擬一個 **Maven 配置範例**，設定一個用於 JaCoCo「整合測試」的特別設定檔，讓你能夠一鍵運行伺服器、用 Python 測試進行呼叫，然後生成覆蓋率報告嗎？