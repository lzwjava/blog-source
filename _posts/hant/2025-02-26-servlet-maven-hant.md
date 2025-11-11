---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Maven 的 Java Servlet 應用程式
translated: true
type: note
---

這是一份完整指南，將教你如何使用 Maven 建構專案，並透過 Liberty Maven 外掛程式部署，在 WebSphere Liberty Profile (WLP) 上建立並部署一個簡單的 Java Servlet 應用程式。本範例將建立一個基礎 Servlet，當存取時會回傳 "Hello World!"，並使用 Maven 將其建構為 WAR 檔案後部署到 WLP。我們假設你已設定好 WLP 並啟用了 `servlet-4.0` 功能，因為這提供了必要的 Servlet 支援。

---

## 逐步指南

### 1. 建立 Maven 專案結構
首先設定標準的 Maven 網頁應用程式結構。你可以手動建立或使用 Maven 生成。

- **目錄結構：**
  ```
  SimpleServletApp/
  ├── pom.xml
  └── src/
      └── main/
          ├── java/
          │   └── com/
          │       └── example/
          │           └── HelloServlet.java
          └── webapp/
              └── WEB-INF/
                  └── web.xml
  ```

- **可選的 Maven 生成方式：**
  執行以下指令來建立結構，然後根據需要進行調整：
  ```bash
  mvn archetype:generate -DgroupId=com.example -DartifactId=simple-servlet-app -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
  ```
  這會建立一個基礎的 webapp 結構，你將在後續步驟中進行修改。

### 2. 編寫 Servlet 程式碼
在 `src/main/java/com/example/` 目錄下建立一個名為 `HelloServlet.java` 的檔案，內容如下：

```java
package com.example;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        resp.setContentType("text/plain");
        resp.getWriter().write("Hello World!");
    }
}
```

- **說明：** 這個 Servlet 會回應 HTTP GET 請求，並回傳純文字 "Hello World!"。它使用簡單的 `doGet` 方法，並為了與明確的 `web.xml` 配置相容而避免使用註解。

### 3. 建立 `web.xml` 部署描述檔
在 `src/main/webapp/WEB-INF/` 目錄下建立一個名為 `web.xml` 的檔案，內容如下：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
    <servlet>
        <servlet-name>HelloServlet</servlet-name>
        <servlet-class>com.example.HelloServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>HelloServlet</servlet-name>
        <url-pattern>/hello</url-pattern>
    </servlet-mapping>
</web-app>
```

- **說明：** `web.xml` 檔案定義了 `HelloServlet` 類別，並將其映射到 `/hello` URL 模式。由於我們沒有使用 `@WebServlet` 註解，因此這是必要的。

### 4. 配置 Maven `pom.xml`
在 `SimpleServletApp/` 目錄下建立或更新 `pom.xml`，內容如下：

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>simple-servlet-app</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <properties>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
    </properties>

    <dependencies>
        <!-- Servlet API (由 WLP 提供) -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Maven WAR Plugin 用於建構 WAR 檔案 -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <finalName>myapp</finalName>
                </configuration>
            </plugin>
            <!-- Liberty Maven Plugin 用於部署 -->
            <plugin>
                <groupId>io.openliberty.tools</groupId>
                <artifactId>liberty-maven-plugin</artifactId>
                <version>3.3.4</version>
                <configuration>
                    <installDirectory>/opt/ibm/wlp</installDirectory>
                    <serverName>myServer</serverName>
                    <appsDirectory>dropins</appsDirectory>
                    <looseApplication>false</looseApplication>
                    <stripVersion>true</stripVersion>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

- **說明：**
  - **座標：** 使用 `groupId`、`artifactId` 和 `version` 定義專案。`packaging` 設定為 `war` 表示這是一個網頁應用程式。
  - **屬性：** 將 Java 8 設定為原始碼和目標版本。
  - **相依性：** 包含 Servlet API，其範圍為 `provided`，因為它在執行時由 WLP 提供。
  - **Maven WAR Plugin：** 使用 `<finalName>` 將 WAR 檔案名稱設定為 `myapp.war`。
  - **Liberty Maven Plugin：** 配置部署到位於 `/opt/ibm/wlp` 的 Liberty 伺服器，伺服器名稱為 `myServer`，並部署到 `dropins` 目錄。

### 5. 建構專案
在 `SimpleServletApp/` 目錄下，使用 Maven 建構 WAR 檔案：

```bash
mvn clean package
```

- **結果：** 這會編譯 Servlet，將其與 `web.xml` 一起打包到 `target/myapp.war` 中，並準備進行部署。

### 6. 在 WebSphere Liberty 上部署並執行
確保你的 Liberty 伺服器 (`myServer`) 已設定並啟用 `servlet-4.0` 功能。檢查你的 `server.xml` 中是否有：
```xml
<featureManager>
    <feature>servlet-4.0</feature>
</featureManager>
```

使用 Liberty Maven 外掛程式部署並執行應用程式：

```bash
mvn liberty:run
```

- **過程說明：**
  - 在前景啟動 Liberty 伺服器（如果尚未執行）。
  - 自動將 `myapp.war` 部署到 `dropins` 目錄。
  - 保持伺服器執行直到手動停止。

- **驗證部署：** 尋找類似以下的日誌訊息：
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  日誌通常位於 `/opt/ibm/wlp/usr/servers/myServer/logs/console.log`。

### 7. 存取應用程式
開啟瀏覽器並導航至：

```
http://localhost:9080/myapp/hello
```

- **預期輸出：**
  ```
  Hello World!
  ```

- **URL 解析：**
  - `9080`：WLP 的預設 HTTP 端口。
  - `/myapp`：來自 WAR 檔案名稱 (`myapp.war`) 的上下文根。
  - `/hello`：來自 `web.xml` 的 URL 模式。

### 8. 停止伺服器
由於 `mvn liberty:run` 在前景執行伺服器，請在終端機中按下 `Ctrl+C` 來停止它。

---

## 注意事項
- **先決條件：**
  - Maven 必須已安裝並在你的系統上配置好。
  - Liberty 必須安裝在 `/opt/ibm/wlp`，且伺服器實例 `myServer` 必須存在。如果你的設定不同（例如 `/usr/local/wlp` 或 `defaultServer`），請調整 `pom.xml` 中的 `installDirectory` 和 `serverName`。
  - `servlet-4.0` 功能必須在 `server.xml` 中啟用。

- **替代部署方式：**
  - 若要分開建構和部署：
    ```bash
    mvn clean package
    mvn liberty:deploy
    ```
    如有需要，手動啟動伺服器：
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **端口配置：** 如果你的 Liberty 伺服器使用不同的 HTTP 端口，請檢查 `server.xml` 中的 `<httpEndpoint>` 並相應調整 URL。

- **上下文根：** 重新命名 `pom.xml` 中的 `<finalName>`（例如 `<finalName>app</finalName>`）以將上下文根更改為 `/app`。

- **疑難排解：**
  - 如果部署失敗，請驗證 `pom.xml` 中的 `installDirectory` 和 `serverName`。
  - 檢查 `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` 中的錯誤日誌。
  - 確保使用 Java 8 或更高版本，並與 `maven.compiler` 設定相符。

---

## 總結
本指南示範如何：
1. 使用簡單的 Servlet (`HelloServlet.java`) 和 `web.xml` 設定 Maven 專案。
2. 在 `pom.xml` 中配置 Servlet API、Maven WAR 外掛程式和 Liberty Maven 外掛程式。
3. 使用 `mvn clean package` 將應用程式建構為 `myapp.war`。
4. 使用 `mvn liberty:run` 將其部署並執行在 WLP 上。
5. 在 `http://localhost:9080/myapp/hello` 存取 "Hello World!"。

這提供了一個基於 Maven 的精簡方法，用於在 WebSphere Liberty Profile 上開發和部署 Servlet 應用程式。

---