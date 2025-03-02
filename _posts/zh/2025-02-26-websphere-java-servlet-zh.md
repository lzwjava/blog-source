---
audio: false
generated: false
lang: zh
layout: post
title: Java Servlet 应用程序在 WebSphere Liberty Profile 上
translated: true
---

这是一个在 WebSphere Liberty Profile (WLP) 上运行非常简单的 Java Servlet 应用程序的完整指南。这个示例创建了一个基本的 Servlet，返回 "Hello World!"，并使用 `dropins` 目录将其部署到 WLP。我们假设你已经启用了 `servlet-4.0` 功能的 WLP，因为这提供了必要的 Servlet 支持。这个指南避免使用 Maven，并提供了所有必要的代码和部署步骤。

---

### 逐步指南

#### 1. 创建 Servlet 应用程序结构
手动为你的 Servlet 应用程序创建目录结构。你可以使用任何文件夹名称，但在这个示例中，我们将其称为 `SimpleServletApp`。

- **目录结构:**
  ```
  SimpleServletApp/
  ├── src/
  │   └── com/
  │       └── example/
  │           └── HelloServlet.java
  └── webapp/
      └── WEB-INF/
          └── web.xml
  ```

#### 2. 编写 Servlet 代码
在 `SimpleServletApp/src/com/example/` 中创建一个名为 `HelloServlet.java` 的文件，内容如下：

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

- **说明：** 这个 Servlet 会对 HTTP GET 请求响应 "Hello World!" 以纯文本形式。我们使用了一个简单的 `doGet` 方法，没有使用注释，以实现最大的兼容性和简化。

#### 3. 创建 `web.xml` 部署描述符
在 `SimpleServletApp/webapp/WEB-INF/` 中创建一个名为 `web.xml` 的文件，内容如下：

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

- **说明：** `web.xml` 文件将 `HelloServlet` 类映射到 `/hello` URL 模式。这是必要的，因为我们没有使用像 `@WebServlet` 这样的注释。

#### 4. 编译 Servlet
使用 `javac` 将 `HelloServlet.java` 文件编译成 `.class` 文件。你需要在类路径中包含 `javax.servlet-api` 库，这由 WLP 提供，但在编译时必须可用。

- **步骤:**
  1. 找到 WLP 安装中的 Servlet API JAR。例如，如果 WLP 安装在 `/opt/ibm/wlp`，JAR 通常在：
     ```
     /opt/ibm/wlp/dev/api/spec/com.ibm.websphere.javaee.servlet.4.0_1.0.x.jar
     ```
     具体文件名可能会根据你的 WLP 版本有所不同。
  2. 从 `SimpleServletApp` 目录运行以下命令：
     ```bash
     javac -cp "/opt/ibm/wlp/dev/api/spec/com.ibm.websphere.javaee.servlet.4.0_1.0.x.jar" src/com/example/HelloServlet.java
     ```
  3. 这将在 `SimpleServletApp/src/com/example/` 中创建 `HelloServlet.class`。

#### 5. 将应用程序打包成 WAR 文件
手动组织编译后的文件并创建 WAR 文件。

- **移动编译后的类:**
  创建 `WEB-INF/classes` 目录并移动编译后的类文件：
  ```bash
  mkdir -p webapp/WEB-INF/classes/com/example
  mv src/com/example/HelloServlet.class webapp/WEB-INF/classes/com/example/
  ```

- **创建 WAR 文件:**
  从 `SimpleServletApp` 目录，使用 `jar` 命令将 `webapp` 文件夹打包成 WAR 文件：
  ```bash
  cd webapp
  jar -cvf ../myapp.war .
  cd ..
  ```
  这将在 `SimpleServletApp` 目录中创建 `myapp.war`。

#### 6. 在 WLP 上部署 WAR 文件
使用 `dropins` 目录将 WAR 文件部署到 WLP 以实现自动部署。

- **找到 `dropins` 目录:**
  找到 WLP 服务器的 `dropins` 目录。如果 WLP 安装在 `/opt/ibm/wlp`，并且你的服务器名称为 `myServer`，路径是：
  ```
  /opt/ibm/wlp/usr/servers/myServer/dropins
  ```

- **复制 WAR 文件:**
  将 WAR 文件移动到 `dropins` 目录：
  ```bash
  cp myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
  ```

- **启动服务器（如果未运行）：**
  如果 WLP 未运行，启动它：
  ```bash
  /opt/ibm/wlp/bin/server start myServer
  ```
  如果已经运行，它将自动检测并部署 WAR 文件。

- **验证部署:**
  检查服务器日志或控制台，查找类似以下的消息：
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  日志在 `/opt/ibm/wlp/usr/servers/myServer/logs/console.log`。

#### 7. 访问应用程序
在浏览器中测试部署的 Servlet。

- **打开浏览器:**
  导航到：
  ```
  http://localhost:9080/myapp/hello
  ```
  - `9080` 是 WLP 的默认 HTTP 端口。
  - `/myapp` 是从 WAR 文件名得到的上下文根。
  - `/hello` 是在 `web.xml` 中定义的 URL 模式。

- **预期结果:**
  你应该看到：
  ```
  Hello World!
  ```
  以纯文本形式显示。

---

### 注意事项
- **没有包含 JSP：** 这个查询要求 JSP 文件，但为了保持 *非常简单*，我们专注于一个基本的 Servlet-only 应用程序。如果需要，可以添加 JSP。
- **上下文根：** 上下文根（`/myapp`）来自 WAR 文件名。重命名 `myapp.war` 可以改变它（例如，`app.war` 为 `/app`）。
- **端口号：** WLP 默认使用 `9080` 作为 HTTP 端口。如果不同，请检查你的 `server.xml`。
- **Java 版本：** 使用与 WLP 兼容的 Java 版本（例如，Java 8 或 11）。
- **故障排除：** 如果不工作，检查 `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` 中的错误，确保 WAR 文件在 `dropins` 中，并验证服务器正在运行。

---

### 总结
这个指南展示了如何：
1. 创建一个简单的 Servlet (`HelloServlet.java`) 和 `web.xml`。
2. 使用 `javac` 编译 Servlet，而不使用 Maven。
3. 手动将其打包成 WAR 文件 (`myapp.war`)。
4. 将其部署到 WLP 的 `dropins` 目录。
5. 在 `http://localhost:9080/myapp/hello` 访问 "Hello World!"。

这提供了一个简单的 Servlet 应用程序，在没有构建工具（如 Maven）的情况下运行在 WebSphere Liberty Profile 上。