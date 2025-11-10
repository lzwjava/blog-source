---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Maven Tomcat 插件問題解決方案
translated: true
type: note
---

你在自己的日誌中已經找到了關鍵線索：

> `[INFO] Skipping non-war project`

沒有任何啟動動作，是因為 **tomcat7-maven-plugin 只會執行以 WAR 格式封裝的 webapp**，且需符合傳統的 `src/main/webapp` 目錄結構。你的專案目前幾乎肯定是以 JAR 格式封裝，所以該外掛在構建完成後就直接退出了。

這裡還有第二個陷阱：你正在運行 **Tomcat 11**（使用 Jakarta `jakarta.*` API），但你的依賴項是 **Spring 5.2.x**（使用 `javax.*`）。這種不匹配意味著，即使 Tomcat 啟動了，直接部署到 Tomcat 11 也會在未經遷移的情況下失敗。對於 Spring 5，請使用 Tomcat 9（javax）；或者將應用程式升級至 Spring 6/Jakarta 以兼容 Tomcat 10/11。

以下是幾條清晰的解決路徑——選擇其中一條即可正常運行：

### 路徑 1 — 保留 Spring 5，使用 Jetty 外掛在本地運行（最快）

無需 WAR；適合快速開發。

1. 添加外掛：

   ```xml
   <plugin>
     <groupId>org.eclipse.jetty</groupId>
     <artifactId>jetty-maven-plugin</artifactId>
     <version>9.4.54.v20240208</version>
   </plugin>
   ```
2. 運行：

   ```bash
   mvn jetty:run -Djetty.port=8080
   ```

此方法使用 `javax.*`，與 Spring 5 匹配。

### 路徑 2 — 保留 Spring 5，構建 WAR 檔案，並使用 Tomcat7 外掛

1. 在 `pom.xml` 中設定 WAR 封裝格式：

   ```xml
   <packaging>war</packaging>
   ```
2. 確保 webapp 目錄結構存在：

   ```
   src/main/webapp/
   src/main/webapp/WEB-INF/web.xml   # 如果你有 Servlet 3 初始化器，此檔案可選
   ```
3. （可選）添加外掛配置：

   ```xml
   <plugin>
     <groupId>org.apache.tomcat.maven</groupId>
     <artifactId>tomcat7-maven-plugin</artifactId>
     <version>2.2</version>
     <configuration>
       <path>/</path>
       <port>8080</port>
     </configuration>
   </plugin>
   ```
4. 運行：

   ```bash
   mvn tomcat7:run            # 用於展開式 webapp
   # 或
   mvn package && mvn tomcat7:run-war
   ```

### 路徑 3 — 保留 Spring 5，部署到獨立的 Tomcat 9

此方法無需更改程式碼即可匹配 `javax.*`。

```bash
brew install tomcat@9
/opt/homebrew/opt/tomcat@9/bin/catalina start
```

構建並將你的 WAR 檔案放入 `.../tomcat@9/libexec/webapps/` 目錄。

### 路徑 4 — 將應用程式升級至 Spring 6/Jakarta，繼續使用 Tomcat 11

如果你想使用現代版的 Tomcat：

* 升級至 Spring Framework 6.x / Spring Boot 3.x。
* 將 import 語句從 `javax.*` 更改為 `jakarta.*`。
* 之後即可正常使用 Tomcat 10/11。

---

#### 為何 `mvn tomcat7:run` 顯示成功但「沒有任何動靜」

* Maven 階段成功完成，但外掛檢測到**非 WAR 封裝格式**，因此它**沒有啟動**內嵌的 Tomcat。這正是「Skipping non-war project」的含義。

---

如果你告訴我你傾向於選擇哪條路徑，我可以提供對應的完整 `pom.xml` 和所需的最簡檔案（包括一個簡單的控制器以及如何透過 `http://localhost:8080/hello` 訪問它）。