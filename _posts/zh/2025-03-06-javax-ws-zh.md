---
audio: false
generated: true
lang: zh
layout: post
title: Java RESTful Web服务API
translated: true
---

要使用 `javax.ws.rs`，即 Java API for RESTful Web Services（通常称为 JAX-RS），你需要按照一系列步骤设置项目、定义 RESTful 资源、配置应用程序并部署它。JAX-RS 允许你创建遵循 REST 架构风格的 Web 服务，使用注解来定义端点并处理 HTTP 请求。以下是一个全面的指南，帮助你入门：

---

### **1. 设置项目**
要使用 `javax.ws.rs`，你需要包含 JAX-RS API 和一个实现（因为 `javax.ws.rs` 是一个规范，而不是运行时）。一个流行的实现是 Jersey。如果你使用 Maven，将必要的依赖项添加到你的 `pom.xml` 中：

#### **依赖项**
```xml
<!-- JAX-RS API -->
<dependency>
    <groupId>javax.ws.rs</groupId>
    <artifactId>javax.ws.rs-api</artifactId>
    <version>2.1.1</version>
</dependency>

<!-- Jersey 实现（包括核心依赖项） -->
<dependency>
    <groupId>org.glassfish.jersey.bundles</groupId>
    <artifactId>jaxrs-ri</artifactId>
    <version>2.34</version>
</dependency>

<!-- 可选：使用 Jackson 支持 JSON -->
<dependency>
    <groupId>org.glassfish.jersey.media</groupId>
    <artifactId>jersey-media-json-jackson</artifactId>
    <version>2.34</version>
</dependency>
```

- `javax.ws.rs-api` 提供了核心的 JAX-RS 注解和类。
- `jaxrs-ri` 束包含了 Jersey 实现及其依赖项。
- `jersey-media-json-jackson` 模块（可选）添加了 JSON 序列化/反序列化的支持。

确保你的项目设置了一个 servlet 容器（例如 Tomcat）或一个 Java EE 服务器，因为 JAX-RS 应用程序通常在这样的环境中运行。或者，你可以使用轻量级服务器如 Grizzly 独立运行（稍后会有更多介绍）。

---

### **2. 创建 RESTful 资源**
JAX-RS 中的 RESTful 服务使用注解 `@Path` 和 HTTP 方法注解（如 `@GET`、`@POST` 等）来定义资源类。以下是一个简单资源的示例：

#### **示例：HelloResource.java**
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

- **`@Path("/hello")`**：指定了这个资源的 URI 路径（例如 `http://localhost:8080/api/hello`）。
- **`@GET`**：表示这个方法处理 HTTP GET 请求。
- **`@Produces(MediaType.TEXT_PLAIN)`**：指定响应将是纯文本。

当对 `/hello` 发出 GET 请求时，这个方法返回 `"Hello, World!"`。

---

### **3. 配置 JAX-RS 应用程序**
你需要告诉 JAX-RS 运行时包含哪些资源。可以通过创建一个扩展 `javax.ws.rs.core.Application` 的应用程序配置类来实现。

#### **示例：MyApplication.java**
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

- **`@ApplicationPath("/api")`**：定义了所有资源的基础 URI 路径（例如 `/api/hello`）。
- **`getClasses()`**：返回应包含在应用程序中的资源类集合。

在现代 servlet 容器（Servlet 3.0+）中，这种基于注解的配置通常是足够的，你可能不需要 `web.xml` 文件。

---

### **4. 处理不同的 HTTP 方法和参数**
JAX-RS 提供了注解来处理各种 HTTP 方法、媒体类型和参数。

#### **示例：处理 POST 请求**
```java
import javax.ws.rs.POST;
import javax.ws.rs.Consumes;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@POST
@Consumes(MediaType.APPLICATION_JSON)
public Response createItem(MyItem item) {
    // 处理 item 的逻辑
    return Response.status(Response.Status.CREATED).build();
}
```

- **`@POST`**：处理 HTTP POST 请求。
- **`@Consumes(MediaType.APPLICATION_JSON)`**：期望 JSON 输入，将其反序列化为 `MyItem` 对象。
- **`Response`**：返回 201 Created 状态。

#### **示例：路径参数**
```java
import javax.ws.rs.PathParam;
import javax.ws.rs.Path;

@GET
@Path("/{id}")
@Produces(MediaType.APPLICATION_JSON)
public MyItem getItem(@PathParam("id") String id) {
    // 根据 ID 检索 item 的逻辑
    return new MyItem(id);
}
```

- **`@Path("/{id}")`**：定义了路径参数（例如 `/hello/123`）。
- **`@PathParam("id")`**：从 URI 中注入 `id` 值。

#### **示例：查询参数**
```java
import javax.ws.rs.QueryParam;

@GET
@Produces(MediaType.APPLICATION_JSON)
public List<MyItem> getItems(@QueryParam("category") String category) {
    // 根据类别过滤 item 的逻辑
    return itemList;
}
```

- **`@QueryParam("category")`**：从查询字符串中检索 `category` 值（例如 `/hello?category=books`）。

---

### **5. 部署应用程序**
你可以在 servlet 容器如 Tomcat 中部署你的 JAX-RS 应用程序：

1. 将项目打包为 WAR 文件（例如使用 `mvn package`）。
2. 将 WAR 文件部署到容器中。
3. 在配置的 URI（例如 `http://localhost:8080/your-app/api/hello`）访问你的服务。

或者，对于开发或独立使用，你可以使用 Jersey 和 Grizzly 以编程方式运行应用程序：

#### **示例：独立主程序**
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

这将启动一个不需要完整 servlet 容器的 HTTP 服务器。

---

### **6. 额外功能**
- **异常处理**：使用 `ExceptionMapper` 优雅地处理异常。
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
- **依赖注入**：使用 `@Context` 注入对象如 `UriInfo` 或依赖实现的 DI 框架（例如 Jersey 中的 HK2）。
- **测试**：使用 Postman 或 Jersey 测试框架来测试你的端点。

---

### **总结**
要使用 `javax.ws.rs`，在项目中包含 JAX-RS API 和实现（如 Jersey），定义使用注解的资源类来定义路径和 HTTP 方法，通过 `Application` 子类或 `web.xml` 配置应用程序，并将其部署到 servlet 容器或独立运行。这使你能够高效地使用 Java 构建 RESTful Web 服务。