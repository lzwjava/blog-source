---
audio: false
generated: true
lang: hant
layout: post
title: Java API 適用於 RESTful Web Services
translated: true
---

要使用 `javax.ws.rs`，即 Java API for RESTful web services（通常稱為 JAX-RS），您需要按照一系列步驟設置您的項目、定義 RESTful 資源、配置應用程序並部署它。JAX-RS 允許您創建遵循 REST 架構風格的 Web 服務，使用註解來定義端點並處理 HTTP 請求。以下是一個全面的指南來幫助您開始：

---

### **1. 設置您的項目**
要使用 `javax.ws.rs`，您需要包含 JAX-RS API 和一個實現（因為 `javax.ws.rs` 是一個規範，而不是運行時）。一個流行的實現是 Jersey。如果您使用 Maven，請將必要的依賴項添加到您的 `pom.xml`：

#### **依賴項**
```xml
<!-- JAX-RS API -->
<dependency>
    <groupId>javax.ws.rs</groupId>
    <artifactId>javax.ws.rs-api</artifactId>
    <version>2.1.1</version>
</dependency>

<!-- Jersey 實現（包括核心依賴項） -->
<dependency>
    <groupId>org.glassfish.jersey.bundles</groupId>
    <artifactId>jaxrs-ri</artifactId>
    <version>2.34</version>
</dependency>

<!-- 可選：使用 Jackson 支持 JSON -->
<dependency>
    <groupId>org.glassfish.jersey.media</groupId>
    <artifactId>jersey-media-json-jackson</artifactId>
    <version>2.34</version>
</dependency>
```

- `javax.ws.rs-api` 提供核心 JAX-RS 注釋和類。
- `jaxrs-ri` 綁定包含 Jersey 實現及其依賴項。
- `jersey-media-json-jackson` 模塊（可選）添加 JSON 串行化/反串行化支持。

確保您的項目設置了 servlet 容器（例如 Tomcat）或 Java EE 伺服器，因為 JAX-RS 應用程序通常在這些環境中運行。或者，您可以使用輕量級伺服器如 Grizzly 運行獨立（稍後會有更多資訊）。

---

### **2. 創建 RESTful 資源**
JAX-RS 中的 RESTful 服務使用註解 `@Path` 和 HTTP 方法註解（如 `@GET`、`@POST` 等）來定義。以下是一個簡單資源的範例：

#### **範例：HelloResource.java**
```java
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/hello")
public class HelloResource {

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String sayHello() {
        return "Hello, World!";
    }
}
```

- **`@Path("/hello")`**：指定此資源的 URI 路徑（例如 `http://localhost:8080/api/hello`）。
- **`@GET`**：指示此方法處理 HTTP GET 請求。
- **`@Produces(MediaType.TEXT_PLAIN)`**：指定響應將是純文本。

當對 `/hello` 發出 GET 請求時，此方法返回 `"Hello, World!"`。

---

### **3. 配置 JAX-RS 應用程序**
您需要告訴 JAX-RS 運行時要包含哪些資源。這可以通過創建一個擴展 `javax.ws.rs.core.Application` 的應用程序配置類來完成。

#### **範例：MyApplication.java**
```java
import javax.ws.rs.ApplicationPath;
import javax.ws.rs.core.Application;
import java.util.HashSet;
import java.util.Set;

@ApplicationPath("/api")
public class MyApplication extends Application {

    @Override
    public Set<Class<?>> getClasses() {
        Set<Class<?>> classes = new HashSet<>();
        classes.add(HelloResource.class);
        return classes;
    }
}
```

- **`@ApplicationPath("/api")`**：定義所有資源的基礎 URI 路徑（例如 `/api/hello`）。
- **`getClasses()`**：返回應包含在應用程序中的資源類集合。

在現代 servlet 容器（Servlet 3.0+）中，這種基於註解的配置通常足夠，您可能不需要 `web.xml` 文件。

---

### **4. 處理不同的 HTTP 方法和參數**
JAX-RS 提供註解來處理各種 HTTP 方法、媒體類型和參數。

#### **範例：處理 POST 請求**
```java
import javax.ws.rs.POST;
import javax.ws.rs.Consumes;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@POST
@Consumes(MediaType.APPLICATION_JSON)
public Response createItem(MyItem item) {
    // 邏輯處理項目
    return Response.status(Response.Status.CREATED).build();
}
```

- **`@POST`**：處理 HTTP POST 請求。
- **`@Consumes(MediaType.APPLICATION_JSON)`**：預期 JSON 输入，該輸入將反序列化為 `MyItem` 對象。
- **`Response`**：返回 201 Created 狀態。

#### **範例：路徑參數**
```java
import javax.ws.rs.PathParam;
import javax.ws.rs.Path;

@GET
@Path("/{id}")
@Produces(MediaType.APPLICATION_JSON)
public MyItem getItem(@PathParam("id") String id) {
    // 邏輯檢索 ID 的項目
    return new MyItem(id);
}
```

- **`@Path("/{id}")`**：定義路徑參數（例如 `/hello/123`）。
- **`@PathParam("id")`**：從 URI 中注入 `id` 值。

#### **範例：查詢參數**
```java
import javax.ws.rs.QueryParam;

@GET
@Produces(MediaType.APPLICATION_JSON)
public List<MyItem> getItems(@QueryParam("category") String category) {
    // 邏輯根據類別篩選項目
    return itemList;
}
```

- **`@QueryParam("category")`**：從查詢字符串中檢索 `category` 值（例如 `/hello?category=books`）。

---

### **5. 部署應用程序**
您可以在 servlet 容器（如 Tomcat）中部署 JAX-RS 應用程序：

1. 將項目打包為 WAR 文件（例如使用 `mvn package`）。
2. 將 WAR 文件部署到您的容器。
3. 在配置的 URI（例如 `http://localhost:8080/your-app/api/hello`）訪問您的服務。

或者，對於開發或獨立使用，您可以使用 Jersey 以 Grizzly 程序運行應用程序：

#### **範例：獨立主程序**
```java
import org.glassfish.jersey.grizzly2.httpserver.GrizzlyHttpServerFactory;
import org.glassfish.jersey.server.ResourceConfig;
import java.net.URI;

public class Main {
    public static void main(String[] args) {
        URI baseUri = URI.create("http://localhost:8080/api/");
        ResourceConfig config = new ResourceConfig(HelloResource.class);
        GrizzlyHttpServerFactory.createHttpServer(baseUri, config);
        System.out.println("Server running at " + baseUri);
    }
}
```

這將啟動一個 HTTP 伺服器而不需要完整的 servlet 容器。

---

### **6. 額外功能**
- **異常處理**：使用 `ExceptionMapper` 來優雅地處理異常。
  ```java
  import javax.ws.rs.NotFoundException;
  import javax.ws.rs.core.Response;
  import javax.ws.rs.ext.ExceptionMapper;
  import javax.ws.rs.ext.Provider;

  @Provider
  public class NotFoundExceptionMapper implements ExceptionMapper<NotFoundException> {
      @Override
      public Response toResponse(NotFoundException exception) {
          return Response.status(Response.Status.NOT_FOUND).build();
      }
  }
  ```
- **依賴注入**：使用 `@Context` 注入對象（如 `UriInfo`）或依賴於實現的 DI 框架（例如 Jersey 中的 HK2）。
- **測試**：使用 Postman 或 Jersey 測試框架來測試您的端點。

---

### **總結**
要使用 `javax.ws.rs`，請在項目中包含 JAX-RS API 和實現（如 Jersey），使用註解定義資源類的路徑和 HTTP 方法，通過 `Application` 子類或 `web.xml` 配置應用程序，並將其部署到 servlet 容器或獨立運行。這使您能夠高效地使用 Java 構建 RESTful Web 服務。