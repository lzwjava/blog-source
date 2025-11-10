---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Liberty JVM 涵蓋範圍的 JaCoCo
translated: true
type: note
---

你可以做到——將 JaCoCo 附加到運行你 EAR 的 **Liberty JVM** 上。關鍵在於：JaCoCo 必須與 Liberty 位於同一個 JVM 內，而不是在你的 Python runner 中。

以下是可靠的設定方式（選擇一種）。

---

## 1) 簡單且穩健：在 JVM 退出時寫入檔案

**使用時機：** 你可以在測試後停止 Liberty 伺服器。

1. **讓代理程式 jar 可用**（在構建中一次性設定）

```xml
<!-- 將 jacoco 代理程式複製到 target/jacoco/jacocoagent.jar -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-dependency-plugin</artifactId>
  <version>3.6.1</version>
  <executions>
    <execution>
      <id>copy-jacoco-agent</id>
      <phase>prepare-package</phase>
      <goals><goal>copy</goal></goals>
      <configuration>
        <artifactItems>
          <artifactItem>
            <groupId>org.jacoco</groupId>
            <artifactId>org.jacoco.agent</artifactId>
            <version>0.8.12</version>
            <classifier>runtime</classifier>
            <destFileName>jacocoagent.jar</destFileName>
          </artifactItem>
        </artifactItems>
        <outputDirectory>${project.build.directory}/jacoco</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

2. **添加 Liberty JVM 選項**（檔案：`wlp/usr/servers/<serverName>/jvm.options`）

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=file,append=false,includes=com.myco.*,excludes=org.slf4j.*,destfile=${server.output.dir}/jacoco/jacoco-it.exec
```

* 將 `jacocoagent.jar` 放入 `wlp/usr/servers/<serverName>/jacoco/`（或任何可讀取的路徑）。
* 根據你的套件調整 `includes`/`excludes`。

3. **執行流程**

* 啟動 Liberty (`server start <serverName>`)，部署 EAR。
* 運行你的 Python `unittest`（它們會訪問端點）。
* 停止 Liberty (`server stop <serverName>`)。
  → 代理程式會寫入 `${server.output.dir}/jacoco/jacoco-it.exec`。

4. **生成報告**

* 如果你的專案是多模組的（EAR + EJB + WAR），請使用聚合 pom 和 `report-aggregate`：

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report-aggregate</goal></goals>
      <configuration>
        <dataFile>${env.SERVER_OUTPUT_DIR}/jacoco/jacoco-it.exec</dataFile>
        <includes>
          <include>com/myco/**</include>
        </includes>
      </configuration>
    </execution>
  </executions>
</plugin>
```

（或使用 `jacococli`：）

```bash
java -jar jacococli.jar report /path/to/jacoco-it.exec \
  --classfiles module1/target/classes --classfiles module2/target/classes \
  --sourcefiles module1/src/main/java --sourcefiles module2/src/main/java \
  --html target/jacoco-it-report
```

---

## 2) 無需停止 Liberty 的實時轉儲（TCP 伺服器模式）

**使用時機：** 你希望保持 Liberty 運行，並按需提取覆蓋率。

1. `jvm.options`：

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=tcpserver,address=*,port=6300,append=false,includes=com.myco.*
```

2. 運行 Liberty，執行 Python 測試，然後**轉儲**：

```bash
# 透過 TCP 提取覆蓋率並在本機寫入 .exec 檔案
java -jar jacococli.jar dump --address 127.0.0.1 --port 6300 --destfile jacoco-it.exec --reset
```

現在按照上述方式生成報告。
提示：`--reset` 會清除計數器，以便在長時間運行期間進行多次快照。

---

## 3) 容器 / CI（環境變數方式）

* 如果你在 Docker/K8s 中運行 Liberty，請掛載代理程式並設定：

  * 如上所述的 `jvm.options`，**或**
  * 包含相同 `-javaagent=...` 的 `WLP_JAVA_OPTIONS` / `JAVA_TOOL_OPTIONS` 環境變數。
* 對於具有多個 Liberty JVM 的叢集，為每個 JVM 分配不同的 TCP 端口或檔案路徑，然後**合併**：

```bash
java -jar jacococli.jar merge node1.exec node2.exec --destfile merged.exec
```

---

## 注意事項與常見問題

* **EAR 的結構對 JaCoCo 無關緊要**；它會在記憶體中對字節碼進行檢測。報告只需要你模組的**原始類別檔案**（`target/classes`）及其源碼以生成美觀的 HTML。
* 使用**最新的 JaCoCo (0.8.12+)** 以確保 Java 17/21 兼容性（Liberty 通常在 OpenJ9/HotSpot 上運行——兩者皆可）。
* 注意 `includes/excludes` 以避免計算第三方函式庫。
* 如果 `.exec` 檔案為空，你可能：

  * 忘記附加代理程式，
  * 過濾掉了你的套件，
  * 或在流量觸及程式碼之前進行了轉儲。

---

如果你分享你的 EAR 模組結構（EJB/WAR 模組和套件根目錄），我可以提供一個精確的 `report-aggregate` 配置和一個小腳本，以便：啟動 Liberty → 運行 Python 測試 → 取得轉儲 → 一鍵生成 HTML 報告。