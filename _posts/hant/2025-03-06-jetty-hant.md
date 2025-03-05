---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Jetty 內嵌 Web 伺服器
translated: true
---

要在 Java 專案中使用 `org.eclipse.jetty`，通常希望利用 Jetty 圖書館在應用程式中嵌入輕量級的網頁伺服器或 Servlet 容器。Jetty 由 Eclipse 基金會維護，是一個開源項目，允許您提供網頁內容、處理 HTTP 請求並支持功能如 Servlet 和網頁應用程式。以下是使用 Maven 作為構建工具，在 Java 應用程式中設置基本網頁伺服器的分步指南。

---

### **步驟 1：將 Jetty 依賴項添加到您的專案**
要使用 Jetty，您需要在專案中包含其圖書館。如果您使用 Maven，請將必要的依賴項添加到 `pom.xml` 文件中。對於具有 Servlet 支持的基本網頁伺服器設置，包括 `jetty-server` 和 `jetty-servlet`。以下是一個範例：

```xml
<project>
    <dependencies>
        <!-- Jetty 伺服器 -->
        <dependency>
            <groupId>org.eclipse.jetty</groupId>
            <artifactId>jetty-server</artifactId>
            <version>9.4.31.v20200723</version>
        </dependency>
        <!-- Jetty Servlet 支持 -->
        <dependency>
            <groupId>org.eclipse.jetty</groupId>
            <artifactId>jetty-servlet</artifactId>
            <version>9.4.31.v20200723</version>
        </dependency>
        <!-- Servlet API（可選，通常透過傳遞包含） -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>3.1.0</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>
</project>
```

- **`jetty-server`**：提供核心伺服器功能來處理 HTTP 請求。
- **`jetty-servlet`**：添加對 Servlet 的支持，允許您使用 Java Servlet API。
- **`javax.servlet-api`**：定義 Servlet 介面；此處明確包含以便清楚，儘管它通常由 `jetty-servlet` 透過傳遞包含。

**注意**：請檢查 [Maven 中央存儲庫](https://mvnrepository.com/artifact/org.eclipse.jetty) 以獲取最新的 Jetty 版本，並相應地更新 `<version>` 標籤。

---

### **步驟 2：創建簡單的 Jetty 伺服器**
您可以通過創建 `org.eclipse.jetty.server` 套件中的 `Server` 類的實例來以編程方式使用 Jetty。以下是兩種常見的方法：使用基本處理程序進行靜態響應或使用 Servlet 進行動態內容。

#### **選項 1：使用基本處理程序**
此範例設置一個伺服器，對所有請求響應 "Hello, World!"。

```java
import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.server.Request;
import org.eclipse.jetty.server.handler.AbstractHandler;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class SimpleJettyServer {
    public static void main(String[] args) throws Exception {
        // 創建一個在 8080 端口監聽的伺服器實例
        Server server = new Server(8080);

        // 設置處理程序來處理請求
        server.setHandler(new AbstractHandler() {
            @Override
            public void handle(String target, Request baseRequest, HttpServletRequest request, HttpServletResponse response)
                    throws IOException {
                // 設置響應屬性
                response.setContentType("text/plain");
                response.setStatus(HttpServletResponse.SC_OK);
                response.getWriter().println("Hello, World!");

                // 將請求標記為已處理
                baseRequest.setHandled(true);
            }
        });

        // 啟動伺服器
        server.start();
        server.join(); // 保持伺服器運行，直到停止
    }
}
```

- **`Server server = new Server(8080)`**：在 8080 端口上創建 Jetty 伺服器。
- **`AbstractHandler`**：一個簡單的處理程序，您在 `handle` 方法中定義如何處理請求。
- **`baseRequest.setHandled(true)`**：指示此處理程序已處理請求，防止進一步處理。

運行此代碼，然後在瀏覽器中導航到 `http://localhost:8080/` 以查看 "Hello, World!"。

#### **選項 2：使用 Servlet**
對於更複雜的應用程式，您可以使用 `ServletContextHandler` 使用 Servlet。

```java
import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletContextHandler;
import org.eclipse.jetty.servlet.ServletHolder;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class ServletJettyServer {
    public static void main(String[] args) throws Exception {
        // 創建一個在 8080 端口上的伺服器實例
        Server server = new Server(8080);

        // 創建一個 Servlet 上下文處理程序
        ServletContextHandler context = new ServletContextHandler();
        context.setContextPath("/"); // 根上下文路徑

        // 設置伺服器的處理程序
        server.setHandler(context);

        // 添加一個 Servlet 來處理請求
        context.addServlet(new ServletHolder(new HelloServlet()), "/*");

        // 啟動伺服器
        server.start();
        server.join();
    }
}

// 定義一個簡單的 Servlet
class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        response.setContentType("text/plain");
        response.setStatus(HttpServletResponse.SC_OK);
        response.getWriter().println("Hello from Jetty Servlet!");
    }
}
```

- **`ServletContextHandler`**：管理 Servlet 上下文和映射。
- **`context.addServlet`**：註冊 `HelloServlet` 以處理所有請求（`/*`）。
- **`doGet`**：定義 Servlet 對 GET 請求的行為。

運行此代碼並訪問 `http://localhost:8080/` 以查看 "Hello from Jetty Servlet!"。

---

### **步驟 3：編譯和運行**
1. 確保您的專案已使用 Maven 設置（例如，運行 `mvn compile` 以下載依賴項）。
2. 編譯並運行 Java 類（例如，`java SimpleJettyServer` 或使用 IDE 的運行功能）。
3. 通過在瀏覽器中訪問 `http://localhost:8080/` 或使用 `curl` 等工具來測試伺服器。

---

### **其他用例**
- **部署 WAR 文件**：使用 `WebAppContext` 部署網頁應用程式檔案（WAR）或目錄：
  ```java
  import org.eclipse.jetty.server.Server;
  import org.eclipse.jetty.webapp.WebAppContext;

  public class WarJettyServer {
      public static void main(String[] args) throws Exception {
          Server server = new Server(8080);
          WebAppContext webapp = new WebAppContext();
          webapp.setContextPath("/");
          webapp.setWar("path/to/your.war"); // 到您的 WAR 文件的路徑
          server.setHandler(webapp);
          server.start();
          server.join();
      }
  }
  ```
  將 `jetty-webapp` 依賴項添加到您的 `pom.xml` 以獲取此功能。

- **配置 Jetty**：以編程方式或通過 XML 配置文件調整設置，例如端口、線程池或 HTTPS（請參閱 Jetty 文檔以獲取高級設置）。

---

### **關鍵點**
- **導入**：使用 `org.eclipse.jetty.server`、`org.eclipse.jetty.servlet` 等套件中的類，根據需要導入它們。
- **靈活性**：Jetty 可以提供靜態內容、處理 Servlet、部署 WAR 文件，甚至支持 WebSockets 和 HTTP/2 等功能，使用其他模塊。
- **文檔**：有關更多詳細信息，請參閱 [官方 Jetty 文檔](https://www.eclipse.org/jetty/documentation/)。

按照這些步驟，您可以有效地使用 `org.eclipse.jetty` 在 Java 應用程式中嵌入網頁伺服器，並根據您的具體需求進行定制！