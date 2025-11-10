---
audio: false
generated: true
image: false
lang: hant
layout: post
title: JaCoCo 輸出檔案使用與分析
translated: true
type: note
---

好問題——讓我們來拆解當你運行 Java 或 Spring Boot 應用程式時，JaCoCo 的 `destfile` 是如何工作的。

### 1. `destfile` 是什麼

`destfile` 是 JaCoCo Java 代理（`jacocoagent.jar`）的一個參數，用於告訴代理**將執行數據寫入何處**。
預設情況下，它通常是 `jacoco.exec`，但你可以明確設定：

```bash
-javaagent:jacocoagent.jar=destfile=/path/to/jacoco.exec
```

### 2. 寫入的內容是什麼

當你的 Spring Boot 應用程式附帶 JaCoCo 代理運行時，代理會對你的類別位元組碼進行插樁。
在執行過程中，JaCoCo 會記錄覆蓋率資訊，例如：

* 哪些類別和方法被載入
* 哪些行被執行
* 分支覆蓋率（例如是否同時執行了 `if`/`else` 路徑等）

這些運行時的覆蓋率數據會儲存在記憶體中，並定期刷新到由 `destfile` 定義的檔案中。

所以是的——JVM 透過 JaCoCo 代理，會將函數和行級的執行資訊寫入該檔案。

### 3. 分析如何進行

`.exec` 檔案本身**並非人類可讀的**。它只是二進位的覆蓋率數據。
在你的應用程式執行結束後，你通常會運行一個報告任務（例如 Maven 的 `jacoco:report` 或 Gradle 的 `jacocoTestReport`），該任務會：

* 讀取 `destfile` 數據
* 讀取你編譯後的 `.class` 檔案和原始碼
* 生成 HTML、XML 或 CSV 格式的覆蓋率報告

這一步驟才是你看到百分比、著色的程式碼行等內容的時候。

### 4. 運行時與報告時

* **運行時：** 代理將執行記錄到記憶體中，並轉儲到 `destfile`。
* **報告時：** 你使用 JaCoCo 工具（Maven、Gradle、CLI 或 Ant）來解讀該 `.exec` 檔案並生成可讀報告。

因此，`destfile` 本身**只是原始的執行數據**——直到你運行報告步驟時才會被分析。

---

👉 簡而言之：是的，當你的 Spring Boot 應用程式附帶 JaCoCo 代理運行時，關於方法和行的覆蓋率資訊會被保存到 `destfile` 中。之後，JaCoCo 報告工具會使用它（連同類別/原始碼檔案）來生成人類易讀的報告。

你需要我進一步示範這在 Spring Boot 中如何逐步運作嗎（例如 Maven 配置 + 運行 + 報告生成）？