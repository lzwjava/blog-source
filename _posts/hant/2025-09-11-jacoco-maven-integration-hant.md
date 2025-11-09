---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 理解 JaCoCo 與 Maven 整合
translated: true
type: note
---

明白了 — 以下將逐步說明 **您 POM 檔案中** JaCoCo 各組件的協作方式及原因。

---

# 此 POM 建立的兩種覆蓋率數據流

1. **單元測試覆蓋率（Surefire 路徑）**

* 您無需特殊配置即可綁定 JaCoCo 的 **`prepare-agent`**：

  ```xml
  <execution>
    <id>prepare-agent</id>
    <goals><goal>prepare-agent</goal></goals>
  </execution>
  ```

  這會透過 `argLine` 屬性將 `-javaagent:...org.jacoco.agent-<ver>-runtime.jar` 注入 **Surefire** 測試 JVM。
  • 預設 **destfile** 為 `${project.build.directory}/jacoco.exec`。
  • 預設 **append** 為 `true`（JaCoCo 代理在檔案已存在時會附加數據）。
  • 效果：當您在 `test` 階段執行單元測試（如有）時，覆蓋率數據會寫入 `target/jacoco.exec`。

2. **整合測試覆蓋率（Jetty 路徑）**

* 您為 IT 覆蓋率定義了 **獨立檔案**：

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
  </properties>
  ```
* 您啟動 Jetty 時使用 **專用的 JaCoCo 代理** 指向該檔案：

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
        </jvmArgs>
        ...
      </configuration>
    </execution>
  </plugin>
  ```

  • Jetty 在 **獨立的 JVM** 中運行；其代理將數據寫入 `target/jacoco-it.exec`。
  • 由於未指定 `append`，JaCoCo 預設的 `append=true` 生效 — 因此除非執行清理或設定 `append=false`，否則多次啟動 Jetty 會將數據附加至同一檔案。

---

# 生命週期流程（執行 `mvn verify` 時的過程）

1. **compile**

   * Spotless 格式化（`spotless-maven-plugin`）和 Checkstyle 檢查（`maven-checkstyle-plugin`）執行。
   * 準備您的 WAR 檔案（`maven-war-plugin`）。

2. **test (Surefire)**

   * 如有單元測試，它們會在 **`prepare-agent`** 注入的 argLine 下運行 → 覆蓋率數據寫入 `target/jacoco.exec`。

3. **pre-integration-test**

   * Jetty 以 **後台模式** 啟動：

     ```xml
     <daemon>true</daemon>
     ```

     Maven 立即恢復控制；Jetty 持續運行並附帶 JaCoCo 代理，將數據寫入 `jacoco-it.exec`。

4. **integration-test**

   * 您的 Python 測試對運行的應用程式發起請求：

     ```xml
     <plugin>
       <artifactId>exec-maven-plugin</artifactId>
       <execution>
         <id>python-integration-tests</id>
         <phase>integration-test</phase>
         <goals><goal>exec</goal></goals>
         <configuration>
           <executable>python3</executable>
           <workingDirectory>${project.parent.basedir}</workingDirectory>
           <arguments>
             <argument>-m</argument><argument>unittest</argument>
             <argument>discover</argument><argument>tests/</argument>
             <argument>-v</argument>
           </arguments>
         </configuration>
       </execution>
     </plugin>
     ```

     這些測試會觸及 Jetty，因此覆蓋率透過 Jetty JVM 的代理累積在 **`target/jacoco-it.exec`** 中。

5. **post-integration-test**

   * Jetty 被乾淨地停止：

     ```xml
     <execution>
       <id>stop-jetty</id>
       <phase>post-integration-test</phase>
       <goals><goal>stop</goal></goals>
       ...
     </execution>
     ```

6. **verify**

   * 您使用 IT 數據檔案和自訂輸出目錄生成 **獨立的 IT 報告**：

     ```xml
     <execution>
       <id>report-it</id>
       <phase>verify</phase>
       <goals><goal>report</goal></goals>
       <configuration>
         <dataFile>${jacoco.it.exec}</dataFile>
         <outputDirectory>${project.reporting.outputDirectory}/jacoco-it
         </outputDirectory>
       </configuration>
     </execution>
     ```
   * 結果：HTML 報告生成於 `target/site/jacoco-it/index.html`，僅總結 **整合** 覆蓋率（來自 Jetty）。

> 注意：如果您還需要 **單元測試** 報告，可以添加另一個 `jacoco:report` 執行階段，指向預設的 `target/jacoco.exec` 並輸出至 `target/site/jacoco` — 從而保持單元測試與 IT 報告分離。

---

# 關於 `.exec` 檔案的「新建或替換？」問題

* **JaCoCo 代理預設為 `append=true`**。

  * 對於 **單元測試**，檔案是 `target/jacoco.exec`。當您重複執行 `mvn verify` 而 **不執行 `clean`** 時，數據可能會在不同運行間附加。
  * 對於 **Jetty IT**，您的 `jvmArgs` 未覆寫 `append`，因此 `target/jacoco-it.exec` 也 **預設附加**。

**最佳實踐**（避免混合舊數據）：

* 執行 `mvn clean verify`，**或** 在 Jetty 代理行中添加 `append=false`：

  ```xml
  -javaagent:...org.jacoco.agent-...-runtime.jar=destfile=${jacoco.it.exec},append=false
  ```
* 若需刻意合併多個 `.exec` 檔案，請在 `jacoco:report` 之前使用 `jacoco:merge`。

---

# 您原始 XML 中各相關區塊的功能說明（按參考）

* **IT 檔案位置**

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
    <it.report.skip>false</it.report.skip>
  </properties>
  ```

  定義整合覆蓋率的儲存位置。`it.report.skip` 已宣告但尚未接入報告執行階段（見下方提示）。

* **單元測試代理（Surefire 路徑）**

  ```xml
  <plugin>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
      <execution>
        <id>prepare-agent</id>
        <goals><goal>prepare-agent</goal></goals>
      </execution>
      ...
    </executions>
  </plugin>
  ```

* **Jetty 搭配 JaCoCo 用於 IT**

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <jvmArgs>
      -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
    </jvmArgs>
    ...
  </plugin>
  ```

* **Jetty 運行時的 Python 整合測試**

  ```xml
  <plugin>
    <artifactId>exec-maven-plugin</artifactId>
    <execution>
      <id>python-integration-tests</id>
      <phase>integration-test</phase>
      <goals><goal>exec</goal></goals>
      ...
    </execution>
  </plugin>
  ```

* **在 verify 階段生成 IT 覆蓋率報告**

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

---

# 實用提示 / 小幅改進

* **避免過時的 IT 數據**
  在 Jetty 代理中添加 `append=false`（如上所示），或始終執行 `mvn clean verify`。

* **接入您的 `it.report.skip` 開關**
  若需透過屬性跳過 IT 報告生成：

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <skip>${it.report.skip}</skip>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

* **保持單元測試與 IT 報告分離**
  您已將 IT 報告分離至 `site/jacoco-it`。若還需要單元測試報告，可添加另一個 `jacoco:report`（不覆寫 `dataFile`）並寫入 `site/jacoco`。

* **多模組注意事項**
  此模組本地設定僅報告 **PlaygroundWeb** 的覆蓋率。若後續需要 **合併** 視圖，請使用 `jacoco:merge`（合併 `.exec` 檔案）和/或從父 `pom`（`packaging=pom`）使用 `report-aggregate`（JaCoCo 0.8.8+）。

---

# 簡要總結

* **單元測試** → `prepare-agent` 將 JaCoCo 注入 Surefire JVM → `target/jacoco.exec`。
* **整合測試** → Jetty 使用專用 JaCoCo 代理啟動 → `target/jacoco-it.exec`。
* **報告** → 在 `verify` 階段，`jacoco:report` 僅將 **IT** 覆蓋率呈現於 `target/site/jacoco-it`。
* **檔案行為** → JaCoCo **預設附加數據**；建議使用 `mvn clean verify` 或 `append=false` 以避免混合運行數據。