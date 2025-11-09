---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hant
layout: post
title: 修復分支 Jetty 停止問題
translated: true
type: note
---

你實際上大部分操作都正確——出現卡住的情況幾乎總是因為**停止目標無法連接到分叉的 Jetty**（錯誤的 stopHost/port/key 範圍）或因為 **`run-forked` 意外地保持 Maven 連接**。以下是兩個可靠的解決方案，請選擇其一。

### 選項 A — 可靠模式：`jetty:start`（後台模式）+ `jetty:stop`

這完全避開了 `run-forked`，是 IT 生命週期中最穩定的方案。

**需要修改的內容**

1. 在 `pre-integration-test` 階段固定插件版本並使用帶有 `daemon=true` 的 `start` 目標。
2. 將你的 Python IT 測試保留在 `integration-test` 階段。
3. 在 `post-integration-test` 階段使用 `stop` 目標。
4. 在**兩個**執行區塊中提供*相同*的 `stopHost/stopPort/stopKey` 設定。

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <configuration>
    <httpConnector>
      <port>8080</port>
      <host>127.0.0.1</host>
    </httpConnector>
  </configuration>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>start</goal>
      </goals>
      <configuration>
        <daemon>true</daemon>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
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

**此方案為何能解決「卡住」問題**

* `daemon=true` 讓 `start` 目標立即將控制權返回給 Maven，以便你的 IT 測試可以執行。
* 匹配的 `stopHost/stopPort/stopKey` 確保 `stop` 目標能夠連接到同一個 Jetty 實例。
* 不依賴 `run-forked` 的監控線程行為。

---

### 選項 B — 保留 `run-forked`，但確保停止功能實際生效

如果你偏好使用 `run-forked`，常見的陷阱包括：

* `stopHost` 的默認值可能與子進程綁定的方式不同（IPv6 與 IPv4）。
* `stopPort/stopKey` 僅在啟動執行區塊中設定，但**未**在停止執行區塊中鏡像設定。
* 如果配置錯誤，子進程可能不會暴露停止處理程序。

**請按以下方式緊密配置：**

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>run-forked</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>

        <httpConnector>
          <host>127.0.0.1</host>
          <port>8080</port>
        </httpConnector>

        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
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

**額外的防護措施**

* 如果你的 macOS/Java 選擇了 IPv6 而停止目標使用 IPv4，請在子進程的 `jvmArgs` 中添加 `-Djava.net.preferIPv4Stack=true`：

  ```
  <jvmArgs>
    -Djava.net.preferIPv4Stack=true
    -javaagent:...
  </jvmArgs>
  ```
* 確保 `8081` 端口沒有被其他程序佔用。如果已被佔用，請將啟動和停止的端口更改為另一個空閒端口。
* 如果你的 IT 測試崩潰或卡住，`post-integration-test` 階段可能永遠不會執行；在這種情況下，請添加一個 `verify` 階段的殺死後備方案（見下文）。

---

### 可選的安全網 — 如果 `stop` 失敗，則殺死子進程

添加一個小助手，通過寫入文件的 PID 強制殺死分叉的 Jetty：

1. 在 `run-forked`/`start` 配置中：

```
<pidFile>${project.build.directory}/jetty.pid</pidFile>
```

2. 在 `post-integration-test` 之後，在 `verify` 階段添加一個 `exec-maven-plugin`，檢查 pid 文件並在進程仍然存活時強制終止它。

---

### 從你的日誌中提取的幾個小提示

* `No Spring WebApplicationInitializer types detected` 是正常的，如果你使用 `web.xml` + DispatcherServlet；這與停止卡住無關。
* 考慮將 IT 測試移至 **maven-failsafe-plugin**（綁定到 `integration-test`/`verify`），並將單元測試保留在 surefire 上。你目前的 `exec-maven-plugin` 方法有效，但 failsafe 能更好地與 IT 生命週期集成。

---

如果你需要，請貼上你的**完整** Jetty 插件區塊 + 任何 `settings.xml` 鏡像（用於本地倉庫路徑），我會為你的代碼庫量身定制精確的最小差異修改。