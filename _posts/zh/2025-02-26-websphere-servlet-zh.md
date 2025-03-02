---
audio: true
generated: false
lang: zh
layout: post
title: WebSphere Liberty Profile 中的 Servlet 版本
translated: true
---

### 理解错误

`console.log` 的错误信息指示了一个与 `spring-web-6.2.3.jar` 中的 `web-fragment.xml` 文件相关的 `DDParser ParseException`。具体来说，它指出部署描述符指定了版本 "50"（对应 Servlet 5.0），而 WebSphere Liberty Profile (WLP) 服务器当前配置为版本 "40"（Servlet 4.0）。这种不匹配的原因是：

- **Servlet 5.0** 是 Jakarta EE 9 的一部分，并且是较新版本的 Spring Boot（例如 Spring Boot 3.x，其中包括 `spring-web-6.2.3.jar`）所需的。
- **Servlet 4.0** 是 Java EE 8 的一部分，WLP 可能配置了 `javaee-8.0` 功能，不支持 Servlet 5.0。

要解决这个问题，您需要使 WLP 支持的 Servlet 版本与应用程序所需的版本一致。推荐的解决方案是通过启用 `jakartaee-9.1` 功能来更新 WLP 以支持 Servlet 5.0。

---

### 解决方案：更新 WLP 以支持 Servlet 5.0

以下是通过更新 WLP 使用 `jakartaee-9.1` 功能来解决问题的方法，该功能包括对 Servlet 5.0 的支持：

#### 1. **定位 `server.xml` 文件**
- `server.xml` 配置文件定义了 WLP 中启用的功能。
- 它通常位于服务器目录中，例如 `/opt/ibm/wlp/usr/servers/myServer/server.xml`，其中 `myServer` 是您的服务器名称。

#### 2. **编辑 `server.xml` 文件**
- 使用文本编辑器打开 `server.xml` 文件。
- 找到 `<featureManager>` 部分，该部分列出了为服务器启用的功能。它可能看起来像这样：
  ```xml
  <featureManager>
      <feature>javaee-8.0</feature>
  </featureManager>
  ```
- 将 `javaee-8.0` 功能替换为 `jakartaee-9.1` 以启用对 Servlet 5.0 的支持：
  ```xml
  <featureManager>
      <feature>jakartaee-9.1</feature>
  </featureManager>
  ```
- 保存文件。

#### 3. **在 WLP 开发模式下应用更改（如果适用）**
- 如果您在 **开发模式** 下运行 WLP（例如，使用 `wlp/bin/server run` 命令或 IDE 集成），可以按照以下方法应用更改：
  - **手动重启：**
    - 停止服务器：
      ```bash
      /opt/ibm/wlp/bin/server stop myServer
      ```
    - 再次启动服务器：
      ```bash
      /opt/ibm/wlp/bin/server start myServer
      ```
  - **开发模式热重载：**
    - 如果 WLP 以开发模式运行（例如，通过 `server run` 或 IDE），它可能会自动检测到对 `server.xml` 的更改。但是，为了确保加载新功能，建议重启。

#### 4. **验证修复**
- 重新启动服务器后，重新部署您的应用程序（例如，通过将 WAR 文件复制到 `dropins` 目录或使用您的部署方法）。
- 检查服务器日志以确认成功部署。查找类似以下的消息：
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  ```
  CWWKZ0001I: Application myapp started in X.XXX seconds.
  ```
- 访问您的应用程序（例如 `http://localhost:9080/myapp/`）以确认它没有错误地运行。

---

### 替代解决方案：降级 Spring Boot

如果将 WLP 更新到 `jakartaee-9.1` 不是一个选项（例如，由于与其他应用程序的兼容性约束），您可以将 Spring Boot 应用程序降级到与 Servlet 4.0 兼容的版本：

#### 1. **切换到 Spring Boot 2.7.x**
- Spring Boot 2.7.x 支持 Servlet 4.0（以及较早的版本，如 Servlet 3.1）。
- 更新您的 `pom.xml` 以使用 Spring Boot 2.7.x：
  ```xml
  <parent>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>2.7.18</version> <!-- 使用最新的 2.7.x 版本 -->
      <relativePath/>
  </parent>
  ```

#### 2. **重新构建和重新部署**
- 重新构建您的应用程序：
  ```bash
  mvn clean package
  ```
- 将生成的 WAR 文件重新部署到 WLP，并验证它没有错误地启动。

---

### 总结
- **错误原因：** 您的应用程序 (`spring-web-6.2.3.jar`) 需要 Servlet 5.0，但 WLP 配置为 Servlet 4.0。
- **首选修复方法：** 通过修改 `server.xml` 并重新启动服务器，将 WLP 更新为使用 `jakartaee-9.1` 功能。
- **替代修复方法：** 降级到 Spring Boot 2.7.x 以匹配 WLP 的 Servlet 4.0 支持。

首选解决方案（更新 WLP）确保您的应用程序可以使用 Spring Boot 3.x 和 Jakarta EE 9 的最新功能。按照上述步骤解决问题并成功部署您的应用程序。