---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hant
layout: post
title: 理解 JaCoCo 執行數據檔案
translated: true
type: note
---

這是一份實用且涵蓋所有必要資訊的概要說明。

# 什麼是 `jacoco-it.exec`？

* 這是在**整合測試**期間產生的 **JaCoCo 執行資料檔案**。
* 「`-it`」只是一種**命名慣例**（源自 `jacoco-maven-plugin` 的 *report-integration* 目標和 Failsafe 階段）。單元測試通常輸出到 `jacoco.exec`，而整合測試則輸出到 `jacoco-it.exec`。
* 您可以擁有多個 `.exec` 檔案（按模組、按階段、按執行），並在後續**合併**它們以產生單一的涵蓋率報告。

典型的 Maven 設定：

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <executions>
    <!-- for unit tests -->
    <execution>
      <id>prepare-agent</id>
      <goals><goal>prepare-agent</goal></goals>
    </execution>
    <!-- for integration tests -->
    <execution>
      <id>prepare-agent-integration</id>
      <goals><goal>prepare-agent-integration</goal></goals>
    </execution>
    <execution>
      <id>report</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
    </execution>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report-integration</goal></goals>
    </execution>
  </executions>
</plugin>
```

這通常會寫入 `target/jacoco.exec`（單元測試）和 `target/jacoco-it.exec`（整合測試）。

# `.exec` 檔案內包含什麼？

* **僅包含探針命中次數**，並按類別進行索引。
* 具體來說：對於每個載入的類別，JaCoCo 會計算一個**ID**（基於位元組碼）並儲存一個**探針的布林陣列**（記錄哪些指令/分支已被執行）。
* 它還儲存了**工作階段 ID** 和時間戳記。
* **它*不*包含類別位元組碼、方法名稱、行號或原始碼**。這些結構資訊是在您執行 `jacoco:report` 以呈現 HTML/XML 時，後續從您的**類別檔案**和**原始碼**中獲取的。

這意味著：

* 如果在產生 `.exec` 檔案後，您的類別發生變更，該檔案可能不再匹配（ID 將無法對齊）。請務必針對產生 exec 檔案時**完全相同的建置版本**的類別檔案來產生報告。

# 它是否包含類別結構資訊？

* **不包含。** 沒有方法資訊、沒有行號、沒有原始碼。
* 它是一個緊湊的、二進位制的、按類別劃分的**命中圖**。報告步驟會讀取您的**已編譯類別**（以及可選的原始碼），將這些命中對應到套件、類別、方法、行和分支。

# 當透過 `-javaagent` 附加時，它會被更新嗎？

簡短回答：**會**，但有一些細節：

* 當您使用代理啟動 JVM 時，它會**即時**檢測類別，並**在記憶體中**記錄探針命中次數。
* 代理會寫入到 `destfile`：

  * **在 JVM 退出時**（對於 `output=file`，這是預設行為），或
  * 當您明確執行**傾印**（透過 TCP/JMX/API）時，或
  * 當設定 `append=true` 時，它會**附加/合併**到現有檔案，而不是覆蓋它。

常用的代理選項：

```bash
-javaagent:/path/to/org.jacoco.agent.jar=\
destfile=/path/to/jacoco-it.exec,\
append=true,\
output=file
```

其他有用的模式：

* `output=tcpserver`（監聽一個端口；您可以連接並觸發傾印）
* `output=tcpclient`（推送到伺服器）
* `jmx=true`（暴露一個 JMX MBean 來進行傾印/重置）
* 程式化方式：`org.jacoco.agent.rt.RT.getAgent().dump(/*reset*/ true|false)`

關於「更新」的注意事項：

* 使用 `output=file` **且** `append=true` 時，**每次傾印**都會將探針陣列合併到現有檔案中（命中次數的邏輯 OR 運算）。
* 沒有 `append=true` 時，下一次寫入會在傾印/退出時**覆蓋**該檔案。
* 如果您有多個 **JVM**（微服務、分叉測試），請將每個 JVM 指向**不同的檔案**，或使用 TCP/JMX 集中收集，然後再進行合併。

# 典型工作流程

**整合測試階段 (Failsafe)：**

* Maven 將代理附加到整合測試的 JVM，並設定 `destfile=target/jacoco-it.exec`。
* 最後，執行 `jacoco:report-integration`，它會讀取：

  * `target/jacoco-it.exec`（命中次數）
  * `target/classes`（結構）
  * `src/main/java`（可選，用於原始碼行號）
* 輸出：僅針對*整合測試*的 HTML/XML/CSV 涵蓋率報告。

**合併多次執行：**

```bash
# 透過 Maven
mvn jacoco:merge -Djacoco.destFile=target/merged.exec \
  -Djacoco.dataFileList="target/jacoco.exec,target/jacoco-it.exec,other.exec"
# 然後
mvn jacoco:report -Djacoco.dataFile=target/merged.exec
```

# 實際常見問題與技巧

* **匹配建置版本**：針對產生 `.exec` 檔案時**相同的已編譯類別**來產生報告。
* **平行分叉**：當平行執行測試或多個 JVM 時，避免多個寫入者寫入同一個檔案，除非設定 `append=true` 且您能接受並行附加（更安全的做法是每個 JVM 使用一個檔案，然後再合併）。
* **長時間運行的服務**：啟用 **TCP/JMX** 或呼叫執行時 API 來**定期傾印**；不要等待程序退出。
* **類別載入器隔離**：某些應用伺服器會載入同一個類別兩次；JaCoCo 會透過類別 ID 進行去重複化，但在複雜的容器中需要注意。
* **離線檢測**是存在的，但 **javaagent** 方法通常更簡單且更穩健。

---

## 對您問題的直接回答

* **「什麼是 `jacoco-it.exec`？」**
  這是在**整合測試**期間擷取的執行資料檔案（探針命中次數）。它只是一個命名慣例；功能上它與 `jacoco.exec` 格式相同。

* **「它是否包含類別結構資訊？」**
  **不包含。** 它僅儲存按類別劃分的**探針命中陣列**和工作階段元資料。類別/方法/行號資訊是在報告步驟期間，從您的已編譯類別/原始碼中獲取的。

* **「當透過 `-javaagent` 附加時，它會被更新嗎？」**
  **會。** 使用 `output=file` 時，代理會在 **JVM 退出時**或**按需求**（TCP/JMX/API）寫入。使用 `append=true` 時，它會與任何現有檔案**合併**；不使用時，它會**覆蓋**。對於多 JVM 運行，請使用單獨的檔案或遠端傾印，並在後續**合併**。