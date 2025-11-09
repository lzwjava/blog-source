---
audio: false
date: 2025-09-08
generated: true
image: false
lang: hant
layout: post
title: 單一JVM整合涵蓋策略
translated: true
type: note
---

你不需要運行 Jetty 兩次或為每個模組建立獨立的 JaCoCo `.exec` 檔案。只需在單一 JVM 上使用一個代理程式，該 JVM 負責提供你的 WAR 檔案，即可將**該 JVM 載入的所有類別**（包括 `PlaygroundUtils`）的覆蓋率記錄到**一個共享的 exec 檔案**中。然後每個模組都可以透過指向同一個 exec 檔案來生成自己的報告。對於大型反應器（10 個以上模組），這種方式能整潔地擴展。

以下是針對你的程式庫的具體、精簡計劃及可直接使用的編輯內容。

---

## 策略

1. **在父層級使用單一共享的 IT exec 檔案。**
   只需啟動 Jetty **一次**，並使用 JaCoCo 進行檢測，寫入 `../target/it-coverage/jacoco-it.exec`（一個父層級範圍的路徑）。
2. **執行一次你的外部 Python 測試。**
   它們會訪問已部署的應用程式；代理程式會記錄所有載入類別（web + 函式庫）的命中情況。
3. **生成每個模組的報告**，每個模組都指向共享的 `jacoco-it.exec`。
   即使 `PlaygroundUtils` 沒有測試，它也會獲得一份報告——它將共享的 exec 檔案映射到自己的 `target/classes`。
4. （可選）**同時在父層級使用 `report-aggregate` 生成一個聚合 HTML 報告**，或者僅保留每個模組的報告。

只有當你真正擁有**多個 JVM**（例如，多個微服務）時，你才需要多個 exec 檔案和一個 `jacoco:merge` 步驟。對於你當前的單一 JVM（Jetty）建置，保持使用一個 exec 檔案即可。

---

## 確切編輯內容

### 1) 父層級 `pom.xml` (PlaygroundLib)

添加共享屬性，以便每個模組都能引用同一個 exec 檔案：

```xml
<properties>
  <!-- ... 你現有的版本 ... -->
  <it.coverage.dir>${project.basedir}/target/it-coverage</it.coverage.dir>
  <jacoco.it.exec>${it.coverage.dir}/jacoco-it.exec</jacoco.it.exec>
  <!-- 切換每個模組的 IT 報告生成 -->
  <it.report.skip>false</it.report.skip>
</properties>
```

（可選）如果你想要在父層級有一個單一的**聚合** HTML 報告，添加此執行區塊：

```xml
<build>
  <pluginManagement>
    <!-- 保留你現有的區塊 -->
  </pluginManagement>

  <plugins>
    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>it-aggregate-report</id>
          <phase>verify</phase>
          <goals>
            <goal>report-aggregate</goal>
          </goals>
          <configuration>
            <!-- 使用由 Jetty 運行產生的共享 IT exec -->
            <dataFile>${jacoco.it.exec}</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

> 如果你的 JaCoCo 版本在 `report-aggregate` 上拒絕 `<dataFile>`，請跳過此可選區塊，並依賴下面每個模組的報告。你以後隨時可以添加一個小的「覆蓋率」聚合模組來執行 `merge` + `report`。

---

### 2) `PlaygroundWeb/pom.xml`

將 Jetty 代理程式指向**父層級**的 exec 路徑並啟用附加模式：

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.parent.basedir}/target/it-coverage/jacoco-it.exec,append=true,includes=org.lzw.*
        </jvmArgs>
        <httpConnector>
          <port>8080</port>
          <host>127.0.0.1</host>
        </httpConnector>
        <webApp><contextPath>/</contextPath></webApp>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals><goal>stop</goal></goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

更新你在 `PlaygroundWeb` 中的 `jacoco:report`，使其讀取**同一個**共享的 exec：

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
      <configuration>
        <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
        <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

你現有的執行 `python -m unittest discover tests -v` 的 Exec Maven Plugin 是完美的——保持原樣即可。

---

### 3) `PlaygroundUtils/pom.xml`

添加一個**僅生成報告**的執行區塊，使其可以將共享的 exec 映射到自己的類別：

```xml
<build>
  <plugins>
    <!-- 保留你現有的插件 -->

    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>report-it</id>
          <phase>verify</phase>
          <goals><goal>report</goal></goals>
          <configuration>
            <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
            <skip>${it.report.skip}</skip>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

此模組從不啟動 Jetty 或執行 Python；它只消費共享的 exec 檔案和它自己的 `target/classes`。如果在測試期間，任何 `PlaygroundUtils` 類別被 web 應用程式使用，它們將會顯示覆蓋率。如果它們沒有被執行，則覆蓋率為 0%——這是正確的信號。

---

## 如何運行它

從程式庫根目錄執行：

```bash
mvn -pl PlaygroundWeb -am clean verify
```

建置順序會編譯兩個模組，啟動帶有代理程式的 Jetty 一次，運行你的 Python 測試，停止 Jetty，然後生成：

* `PlaygroundWeb/target/site/jacoco-it/index.html`
* `PlaygroundUtils/target/site/jacoco-it/index.html`
* 如果你啟用了 `report-aggregate`，可選地，在父層級下還會有一個聚合報告。

---

## 當你擁有 10 個模組時

* 如果所有 10 個模組最終都在**同一個 WAR/JVM** 中，請保持**單一共享 exec** 模式。每個模組添加一個指向共享 exec 的 `report` 執行區塊。你仍然只需啟動 Jetty 一次並執行 Python 一次。

* 如果你有**多個 JVM**（例如，獨立的服務），請為每個 JVM 提供自己的 `destfile`（例如，`it-coverage/serviceA.exec`、`serviceB.exec`），然後在父層級運行：

  ```xml
  <plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
      <execution>
        <id>merge-it</id>
        <phase>post-integration-test</phase>
        <goals><goal>merge</goal></goals>
        <configuration>
          <destFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</destFile>
          <files>
            <file>${project.basedir}/target/it-coverage/serviceA.exec</file>
            <file>${project.basedir}/target/it-coverage/serviceB.exec</file>
            <!-- 根據需要添加更多 -->
          </files>
        </configuration>
      </execution>

      <execution>
        <id>aggregate-report</id>
        <phase>verify</phase>
        <goals><goal>report-aggregate</goal></goals>
        <configuration>
          <dataFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</dataFile>
          <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
        </configuration>
      </execution>
    </executions>
  </plugin>
  ```

* 如果你想限制雜訊，請在代理程式行中設置 `includes=org.lzw.*`（已顯示）或添加 `excludes` 以過濾第三方函式庫。

---

## 你當前痛苦的原因

* 你之前建立了**每個模組的 exec 檔案**，因此你覺得被迫重新運行帶有不同代理程式的 Jetty 來填充每個檔案。這是不必要的。代理程式不關心一個類別「屬於」哪個模組——它記錄任何載入的類別。將 exec 集中管理，並讓每個模組的 `report` 指向它。

---

## 快速檢查清單

* 在父層級下有一個**共享的** `${jacoco.it.exec}`。
* Jetty 啟動**一次**，使用 `append=true` 和 `includes=org.lzw.*`。
* Python 測試運行**一次**。
* 每個模組都有一個讀取共享 exec 的 `jacoco:report`。
* 可選的父層級 `report-aggregate`，用於生成單一的頂層 HTML 報告。

這應該能使你的設定更簡單且更具擴展性。如果你需要，我可以根據這些變更，為你當前的 POM 檔案生成確切的差異內容。