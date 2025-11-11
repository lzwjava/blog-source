---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Jetty 嵌入網頁伺服器
translated: true
type: note
---

要在 Java 專案中使用 `org.eclipse.jetty`，通常需要利用 Jetty 函式庫在應用程式中嵌入輕量級網頁伺服器或 servlet 容器。Jetty 由 Eclipse Foundation 維護，是一個開放原始碼專案，可讓您提供網頁內容、處理 HTTP 請求，並支援 servlet 和網頁應用程式等功能。以下是以 Maven 作為建置工具的逐步指南，協助您開始使用 `org.eclipse.jetty` 在 Java 應用程式中設定基本網頁伺服器。

---

### **步驟 1：將 Jetty 相依性加入專案**
要使用 Jetty，您需要在專案中包含其函式庫。若使用 Maven，請將必要的相依性加入 `pom.xml` 檔案。對於具有 servlet 支援的基本網頁伺服器設定，請包含 `jetty-server` 和 `jetty-servlet`。以下為範例：

```xml
<project>
    <dependencies>
        <!-- Jetty Server -->
        <dependency>
            <groupId>org.eclipse.jetty</groupId>
            <artifactId>jetty-server</artifactId>
            <version>9.4.31.v20200723</version>
        </dependency>
        <!-- Jetty Servlet Support -->
        <dependency>
            <groupId>org.eclipse.jetty</groupId>
            <artifactId>jetty-servlet</artifactId>
            <version>9.4.31.v20200723</version>
        </dependency>
        <!-- Servlet API (optional, often included transitively) -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>3.1.0</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>
</project>
```

- **`jetty-server`**：提供處理 HTTP 請求的核心伺服器功能。
- **`jetty-servlet`**：增加對 servlet 的支援，讓您能使用 Java Servlet API。
- **`javax.servlet-api`**：定義 servlet 介面；此處明確包含以確保清晰度，但通常會由 `jetty-servlet` 傳遞性引入。

**注意**：請查閱 [Maven Central Repository](https://mvnrepository.com/artifact/org.eclipse.jetty) 以取得最新 Jetty 版本，並相應更新 `<version>` 標籤。

---

### **步驟 2：建立簡易 Jetty 伺服器**
您可以透過程式設計方式使用 Jetty，方法是建立 `org.eclipse.jetty.server` 套件中 `Server` 類別的實例。以下是兩種常見方法：使用基本處理器提供靜態回應，或使用 servlet 提供動態內容。

#### **選項 1：使用基本處理器**
此範例設定一個伺服器，對所有請求回應 "Hello, World!"。

```java
import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.server.Request;
import org.eclipse.jetty.server.handler.AbstractHandler;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class SimpleJettyServer {
    public static void main(String[] args) throws Exception {
        // 建立監聽 8080 埠的伺服器實例
        Server server = new Server(8080);

        // 設定處理器來處理請求
        server.setHandler(new AbstractHandler() {
            @Override
            public void handle(String target, Request baseRequest, HttpServletRequest request, HttpServletResponse response)
                    throws IOException {
                // 設定回應屬性
                response.setContentType("text/plain");
                response.setStatus(HttpServletResponse.SC_OK);
                response.getWriter().println("Hello, World!");

                // 標記請求已處理
                baseRequest.setHandled(true);
            }
        });

        // 啟動伺服器
        server.start();
        server.join(); // 保持伺服器運行直到停止
    }
}
```

- **`Server server = new Server(8080)`**：在 8080 埠建立 Jetty 伺服器。
- **`AbstractHandler`**：一個簡易處理器，您可在 `handle` 方法中定義如何處理請求。
- **`baseRequest.setHandled(true)`**：表示此處理器已處理請求，防止進一步處理。

執行此程式碼，然後在瀏覽器中開啟 `http://localhost:8080/` 即可看到 "Hello, World!"。

#### **選項 2：使用 Servlet**
對於更複雜的應用程式，您可以使用 servlet 搭配 `ServletContextHandler`。

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
        // 在 8080 埠建立伺服器實例
        Server server = new Server(8080);

        // 建立 servlet 上下文處理器
        ServletContextHandler context = new ServletContextHandler();
        context.setContextPath("/"); // 根上下文路徑

        // 為伺服器設定處理器
        server.setHandler(context);

        // 加入 servlet 來處理請求
        context.addServlet(new ServletHolder(new HelloServlet()), "/*");

        // 啟動伺服器
        server.start();
        server.join();
    }
}

// 定義簡易 servlet
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

- **`ServletContextHandler`**：管理 servlet 上下文和映射。
- **`context.addServlet`**：註冊 `HelloServlet` 以處理所有請求 (`/*`)。
- **`doGet`**：定義 servlet 對 GET 請求的行為。

執行此程式碼並訪問 `http://localhost:8080/` 即可看到 "Hello from Jetty Servlet!"。

---

### **步驟 3：編譯與執行**
1. 確保您的專案已設定 Maven（例如執行 `mvn compile` 以下載相依性）。
2. 編譯並執行 Java 類別（例如 `java SimpleJettyServer` 或使用 IDE 的執行功能）。
3. 透過在瀏覽器中訪問 `http://localhost:8080/` 或使用 `curl` 等工具測試伺服器。

---

### **其他使用情境**
- **部署 WAR 檔案**：使用 `WebAppContext` 部署網頁應用程式封存檔（WAR）或目錄：
  ```java
  import org.eclipse.jetty.server.Server;
  import org.eclipse.jetty.webapp.WebAppContext;

  public class WarJettyServer {
      public static void main(String[] args) throws Exception {
          Server server = new Server(8080);
          WebAppContext webapp = new WebAppContext();
          webapp.setContextPath("/");
          webapp.setWar("path/to/your.war"); // 您的 WAR 檔案路徑
          server.setHandler(webapp);
          server.start();
          server.join();
      }
  }
  ```
  為此功能，請在 `pom.xml` 中加入 `jetty-webapp` 相依性。

- **設定 Jetty**：透過程式設計或 XML 設定檔案調整埠號、執行緒池或 HTTPS 等設定（進階設定請參閱 Jetty 文件）。

---

### **重點提示**
- **匯入**：根據需要從 `org.eclipse.jetty.server`、`org.eclipse.jetty.servlet` 等套件匯入類別。
- **靈活性**：Jetty 可提供靜態內容、處理 servlet、部署 WAR 檔案，甚至透過附加模組支援 WebSockets 和 HTTP/2。
- **文件**：更多詳細資訊，請參閱 [官方 Jetty 文件](https://www.eclipse.org/jetty/documentation/)。

遵循這些步驟，您就能有效使用 `org.eclipse.jetty` 在 Java 應用程式中嵌入網頁伺服器，並根據特定需求進行調整！