---
audio: false
generated: true
lang: zh
layout: post
title: JNDI 数据源配置在 WebSphere Liberty
translated: true
---

要确定一个 EAR Java 程序是否使用在 WebSphere Liberty 中 `server.xml` 文件中定义的数据源，你需要验证应用程序是否通过一个对应于服务器配置中（特别是 `server.xml` 文件或其包含的任何文件）配置的数据源的 JNDI（Java Naming and Directory Interface）名称来访问数据源。以下是一个逐步指南，帮助你确认这一点：

### 第 1 步：确定应用程序使用的 JNDI 名称
首先，找出 EAR 应用程序使用的 JNDI 名称来查找其数据源。在作为 EAR 文件部署的 Java EE 应用程序中，这可以在多个地方指定：

- **部署描述符**：检查应用程序的部署描述符，例如 `web.xml`（用于 Web 模块）或 `ejb-jar.xml`（用于 EJB 模块），查找 `<resource-ref>` 元素。该元素声明了应用程序用来访问数据源的资源引用。例如：

  ```xml
  <resource-ref>
      <res-ref-name>jdbc/myDataSource</res-ref-name>
      <res-type>javax.sql.DataSource</res-type>
      <res-auth>Container</res-auth>
  </resource-ref>
  ```

  在这种情况下，应用程序使用 JNDI 名称 `java:comp/env/jdbc/myDataSource` 查找数据源。

- **绑定文件**：在 WebSphere Liberty 中，部署描述符中的资源引用可能通过绑定文件（如 `ibm-web-bnd.xml`（用于 Web 模块）或 `ibm-ejb-jar-bnd.xml`（用于 EJB））绑定到服务器中定义的实际 JNDI 名称。查找 `<resource-ref>` 绑定，例如：

  ```xml
  <resource-ref name="jdbc/myDataSource" binding-name="jdbc/actualDataSource"/>
  ```

  在这种情况下，应用程序的引用 `jdbc/myDataSource` 被映射到服务器的 JNDI 名称 `jdbc/actualDataSource`。

- **应用程序代码**：如果你有访问源代码的权限，搜索 JNDI 查找或注解：
  - **JNDI 查找**：查找类似以下的代码：

    ```java
    Context ctx = new InitialContext();
    DataSource ds = (DataSource) ctx.lookup("java:comp/env/jdbc/myDataSource");
    ```

    这表明 JNDI 名称为 `java:comp/env/jdbc/myDataSource`。

  - **注解**：在现代 Java EE 应用程序中，可能会使用 `@Resource` 注解，例如：

    ```java
    @Resource(name = "jdbc/myDataSource")
    private DataSource ds;
    ```

    这也指向 `java:comp/env/jdbc/myDataSource`。

如果不存在绑定文件，代码或部署描述符中的 JNDI 名称（例如 `jdbc/myDataSource`）可能直接对应于服务器配置中预期的名称。

### 第 2 步：检查 `server.xml` 配置
一旦你确定了应用程序使用的 JNDI 名称（直接或通过绑定），检查 WebSphere Liberty 的 `server.xml` 文件（以及通过 `<include>` 元素包含的任何配置文件）中的匹配数据源定义。`server.xml` 中的数据源通常使用 `<dataSource>` 元素定义，例如：

```xml
<dataSource id="myDataSource" jndiName="jdbc/myDataSource">
    <jdbcDriver libraryRef="myDBLib"/>
    <properties url="jdbc:mysql://localhost:3306/mydb" user="user" password="pass"/>
</dataSource>
```

- 查找 `jndiName` 属性（例如 `jdbc/myDataSource`）。
- 将其与应用程序使用的 JNDI 名称（例如 `jdbc/myDataSource` 或绑定名称如 `jdbc/actualDataSource`）进行比较。

如果 JNDI 名称匹配，则应用程序使用 `server.xml` 中定义的数据源。

### 第 3 步：解释结果
- **匹配找到**：如果应用程序使用的 JNDI 名称对应于 `server.xml`（或包含的文件）中的 `<dataSource>` 元素，则 EAR Java 程序使用 `server.xml` 数据源。
- **无匹配**：如果 `server.xml` 中没有匹配的 JNDI 名称，应用程序可能没有使用服务器定义的数据源。它可能会以编程方式创建自己的数据源（例如，使用 JDBC 驱动程序直接使用 URL、用户名和密码），尽管这种情况在受管理的环境（如 WebSphere Liberty）中不常见且不推荐。

### 附加考虑
- **包含的配置文件**：如果 `server.xml` 使用 `<include>` 元素（例如 `<include location="datasources.xml"/>`），检查这些文件中的数据源定义。
- **默认行为**：如果没有绑定文件覆盖 JNDI 名称，应用程序可能假设资源引用名称（例如 `jdbc/myDataSource`）与 `server.xml` 中的数据源匹配。
- **服务器日志或工具**：虽然这不是配置检查的一部分，你也可以查看服务器日志或使用 WebSphere Liberty Admin Center 来查看哪些数据源与应用程序关联，尽管这更多的是运行时验证。

### 结论
要确认 EAR Java 程序是否使用 WebSphere Liberty 中的 `server.xml` 数据源：
1. 确定应用程序使用的 JNDI 名称（通过部署描述符、绑定文件或代码）。
2. 验证该 JNDI 名称是否与 `server.xml` 或其包含的文件中定义的数据源匹配。

如果有匹配，应用程序依赖于 `server.xml` 数据源；否则，它可能使用替代方法。