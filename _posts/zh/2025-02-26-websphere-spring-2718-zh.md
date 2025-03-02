---
audio: false
generated: false
lang: zh
layout: post
title: Spring Boot 2.7.18 在 WebSphere Liberty Profile
translated: true
---

在使用 Spring Boot 2.7.18 将应用程序部署到 WebSphere Liberty Profile (WLP) 时，按照提供的指南进行操作，好消息是不需要对 `DemoApplication` 类或 `SpringBootServletInitializer` 的使用进行任何更改。Spring Boot 2.7.18 是 2.7.x 系列中的一个补丁版本，这意味着它包括了错误修复和小的改进，但没有引入会影响指南中描述的标准 WAR 部署配置的重大更改。下面，我将解释为什么会这样，并确认该设置仍然完全兼容。

---

### 理解设置
指南通过以下方式配置 Spring Boot 应用程序以在 WLP 上作为 WAR 文件部署：

1. **扩展 `SpringBootServletInitializer`：**
   - `DemoApplication` 类扩展 `SpringBootServletInitializer` 以启用到外部 servlet 容器（如 WLP）的部署。这个类是必要的，因为虽然 Spring Boot 默认作为包含嵌入式服务器的独立 JAR 运行，但部署到 WLP 需要与其 servlet 容器集成。
   - 重写 `configure` 方法以指定应用程序源，确保应用程序在外部容器中正确引导。

   这是指南中的代码：
   ```java
   package com.example.demo;

   import org.springframework.boot.SpringApplication;
   import org.springframework.boot.autoconfigure.SpringBootApplication;
   import org.springframework.boot.builder.SpringApplicationBuilder;
   import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;

   @SpringBootApplication
   public class DemoApplication extends SpringBootServletInitializer {

       @Override
       protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
           return application.sources(DemoApplication.class);
       }

       public static void main(String[] args) {
           SpringApplication.run(DemoApplication.class, args);
       }
   }
   ```

2. **打包为 WAR 文件：**
   - `pom.xml` 指定 `<packaging>war</packaging>`，并将 `spring-boot-starter-tomcat` 依赖项标记为 `<scope>provided</scope>`，以排除嵌入式 Tomcat 服务器，而是依赖 WLP 的 servlet 容器。

3. **部署到 WLP：**
   - WAR 文件放置在 WLP 的 `dropins` 目录中以进行自动部署，WLP 的 `javaee-8.0` 功能提供 Servlet 4.0 支持，这与 Spring Boot 的要求兼容。

---

### 为什么在 Spring Boot 2.7.18 中不需要更改
Spring Boot 2.7.18 是 2.7.x 系列的一部分，显著的部署机制或 API 更改通常发生在主要版本之间（例如，2.x 到 3.x），而不是在次要或补丁版本中。以下是详细分析：

#### 1. 与 `SpringBootServletInitializer` 的兼容性
- **目的：** `SpringBootServletInitializer` 仍然是 2.x 系列中配置 Spring Boot 应用程序进行 WAR 部署的标准方法。它通过提供一个钩子来设置应用程序上下文，与外部 servlet 容器集成。
- **在 2.7.18 中的稳定性：** Spring Boot 2.7.18 中没有 `SpringBootServletInitializer` 的弃用或替代。主要更改，例如转向 Jakarta EE（替换 Java EE API），发生在 Spring Boot 3.x 中，这也需要 Java 17。由于 2.7.18 保持在 2.x 系列中并使用 Java EE，`DemoApplication` 中的现有实现仍然有效且未更改。

#### 2. Servlet 容器兼容性
- **Spring Boot 要求：** Spring Boot 2.7.x 需要 Servlet 3.1 或更高版本。指南使用 WLP 并启用 `javaee-8.0` 功能，其中包含 Servlet 4.0——一个更新的规范。这确保了完全兼容。
- **在 2.7.18 中没有更改：** 补丁版本如 2.7.18 不会更改 servlet 兼容性或引入新要求，这些要求会影响 `SpringBootServletInitializer` 与 WLP 的交互方式。

#### 3. 依赖和打包配置
- **Tomcat 作为 `provided`：** 指南在 `pom.xml` 中正确将 `spring-boot-starter-tomcat` 设置为 `<scope>provided</scope>`，确保嵌入式 Tomcat 被排除在 WAR 文件之外。这是外部容器 WAR 部署的标准做法，并在 2.7.18 中保持不变。
- **Maven 配置：** 打包类型（`war`）和依赖项设置与 Spring Boot 2.7.x 约定一致，并且不需要特定于 2.7.18 的更新。

#### 4. WLP 部署特定信息
- **dropins 目录：** WLP 的 `dropins` 部署机制不受 Spring Boot 版本的影响，因为它依赖于 WAR 文件结构和 servlet 规范，这两者在 2.7.18 中保持兼容。
- **上下文根和端口：** 上下文根（例如 `/myapp`）和默认端口（例如 `9080`）由 WLP 和 WAR 文件名称确定，而不是 Spring Boot 的版本，因此它们保持不变。

#### 5. 可能的新功能或弃用
- **发布说明考虑：** Spring Boot 2.7.x 发布说明（包括 2.7.18）通常涵盖依赖项更新、安全修复和小的增强，但没有影响 WAR 部署或 `SpringBootServletInitializer`。例如，2.7.18 中没有引入新的注释或配置方法来替换现有方法。
- **与 3.x 对比：** 相比之下，Spring Boot 3.x 采用 Jakarta EE，可能需要调整（例如不同的基类或更新的 servlet API），但 2.7.18 不会过渡到这些更改。

---

### 结论
对于 Spring Boot 2.7.18，指南中所示的 `DemoApplication` 类和 `SpringBootServletInitializer` 的使用不需要任何修改。配置完全兼容：

- WAR 打包和部署到 WLP。
- WLP 中的 `javaee-8.0` 功能（Servlet 4.0）。
- Spring Boot 2.7.x 的 servlet 和部署要求。

您可以按照指南中的精确步骤和代码进行操作——使用 Spring Boot 2.7.18 而不是通用的 2.7.x 版本——并期望应用程序在 WLP 上成功部署和运行，返回 `http://localhost:9080/myapp/` 的 "Hello World!"。不需要额外的配置、属性更改或代码调整。