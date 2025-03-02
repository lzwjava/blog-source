---
audio: true
generated: false
lang: zh
layout: post
title: WebSphere Liberty Profile 部署故障排除
translated: true
---

当你尝试访问你的 Spring Boot 应用程序 `http://localhost:9080/myapp/` 时，在 WebSphere Liberty Profile (WLP) 上遇到“上下文根未找到”错误，这表明 WLP 没有成功在预期的上下文根 (`/myapp`) 下部署你的应用程序。这个问题通常是由于部署配置、服务器设置或 WAR 文件本身的问题引起的。以下是一个全面的指南，帮助你排查和解决这个问题。

---

### 理解问题
“上下文根未找到”错误意味着 WLP 无法找到部署在 `/myapp` 的应用程序。通常，当你将一个名为 `myapp.war` 的 WAR 文件放置在 WLP 的 `dropins` 目录中时，它应该自动部署在上下文根 `/myapp`，使其可在 `http://localhost:9080/myapp/` 访问。由于这没有发生，我们需要调查部署失败的原因。

---

### 排查步骤

#### 1. **检查服务器日志以获取部署消息**
首先，确认 WLP 是否部署了你的应用程序。

- **定位日志：**
  - 如果你的服务器名称为 `myServer`，检查日志：
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/messages.log
    ```
    或
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/console.log
    ```
  - 如果使用默认服务器，将 `myServer` 替换为 `defaultServer`。

- **查找部署确认：**
  - 你应该看到类似的消息：
    ```
    [AUDIT   ] CWWKT0016I: Web 应用程序可用 (default_host): http://localhost:9080/myapp/
    ```
    这表明应用程序已部署并可用。
  - 此外，查找：
    ```
    CWWKZ0001I: 应用程序 myapp 在 X.XXX 秒内启动。
    ```
    这确认应用程序已成功启动。

- **操作：**
  - 如果这些消息不存在，应用程序没有部署。查找日志中的任何 `ERROR` 或 `WARNING` 消息，这些消息可能会指出原因（例如，缺少功能、文件权限或启动失败）。
  - 如果你看到 Spring Boot 启动日志（例如，Spring Boot 横幅），应用程序正在加载，问题可能与上下文根或 URL 映射有关。

#### 2. **验证 WAR 文件的位置和权限**
确保 WAR 文件正确放置在 `dropins` 目录中，并且对 WLP 可访问。

- **检查路径：**
  - 对于名为 `myServer` 的服务器，WAR 文件应该在：
    ```
    /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
  - 如果使用 `defaultServer`，相应调整：
    ```
    /opt/ibm/wlp/usr/servers/defaultServer/dropins/myapp.war
    ```

- **验证权限：**
  - 确保 WLP 进程对文件具有读取权限。在类 Unix 系统上，运行：
    ```bash
    ls -l /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
    文件应该是可读的（例如，`rw-r--r--`）。

- **操作：**
  - 如果文件丢失或放置错误，将其复制到正确的 `dropins` 目录：
    ```bash
    cp target/myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
    ```
  - 如果需要，修复权限：
    ```bash
    chmod 644 /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```

#### 3. **确认 `dropins` 监控在 `server.xml` 中**
WLP 的 `dropins` 目录默认情况下是启用的，但自定义配置可能会禁用它。

- **检查 `server.xml`：**
  - 打开服务器配置文件：
    ```
    /opt/ibm/wlp/usr/servers/myServer/server.xml
    ```
  - 查找 `applicationMonitor` 元素：
    ```xml
    <applicationMonitor updateTrigger="polled" pollingRate="5s" dropins="dropins" />
    ```
    这确认 WLP 每 5 秒监控 `dropins` 目录以查找新应用程序。

- **操作：**
  - 如果不存在，在 `<server>` 标签内添加上述行，或者确保没有覆盖配置禁用 `dropins`。
  - 更改后重启服务器：
    ```bash
    /opt/ibm/wlp/bin/server stop myServer
    /opt/ibm/wlp/bin/server start myServer
    ```

#### 4. **确保启用所需功能**
WLP 需要特定功能来部署 Spring Boot WAR 文件，例如 Servlet 支持。

- **检查 `server.xml`：**
  - 验证 `featureManager` 部分包括：
    ```xml
    <featureManager>
        <feature>javaee-8.0</feature>
    </featureManager>
    ```
    `javaee-8.0` 功能包括 Servlet 4.0，与 Spring Boot 兼容。或者，至少应该存在 `servlet-4.0`。

- **操作：**
  - 如果缺失，添加功能并重启服务器。

#### 5. **验证 WAR 文件结构**
损坏或结构不正确的 WAR 文件可能会阻止部署。

- **检查 WAR：**
  - 解压 WAR 文件以验证其内容：
    ```bash
    unzip -l myapp.war
    ```
  - 查找：
    - `WEB-INF/classes/com/example/demo/HelloController.class`（你的控制器类）。
    - `WEB-INF/lib/` 包含 Spring Boot 依赖项（例如，`spring-web-x.x.x.jar`）。

- **操作：**
  - 如果结构不正确，重新构建 WAR：
    ```bash
    mvn clean package
    ```
    确保你的 `pom.xml` 设置 `<packaging>war</packaging>`，并将 `spring-boot-starter-tomcat` 标记为 `<scope>provided</scope>`。

#### 6. **通过 `apps` 目录进行替代部署**
如果 `dropins` 失败，尝试通过 `apps` 目录显式部署应用程序。

- **步骤：**
  - 移动 WAR 文件：
    ```bash
    mv /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war /opt/ibm/wlp/usr/servers/myServer/apps/
    ```
  - 编辑 `server.xml` 以添加：
    ```xml
    <application id="myapp" name="myapp" type="war" location="${server.config.dir}/apps/myapp.war">
        <context-root>/myapp</context-root>
    </application>
    ```
  - 重启服务器：
    ```bash
    /opt/ibm/wlp/bin/server restart myServer
    ```

- **再次测试：**
  - 访问 `http://localhost:9080/myapp/`。如果成功，问题出在 `dropins` 上。

#### 7. **验证服务器状态**
确保服务器正常运行。

- **检查状态：**
  ```bash
  /opt/ibm/wlp/bin/server status myServer
  ```
  - 如果已停止，启动它：
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **测试 WLP 本身：**
  - 访问 `http://localhost:9080/`。如果 WLP 正在运行，你将看到一个欢迎页面（除非被覆盖）。如果失败，则存在更广泛的服务器问题。

---

### 解决方案
要修复“上下文根未找到”错误：

1. **从这里开始：**
   - 检查服务器日志（`messages.log` 或 `console.log`）以获取部署消息或错误。
   - 确保 `myapp.war` 在 `dropins` 目录中，并且具有适当的权限。

2. **下一步：**
   - 验证 `server.xml` 启用 `javaee-8.0` 功能并监控 `dropins`。
   - 如果未解决，通过 `apps` 目录部署，并在 `server.xml` 中添加显式 `<application>` 配置。

3. **最终验证：**
   - 更改后重启 WLP，访问 `http://localhost:9080/myapp/`。如果部署成功，你应该看到“Hello World!”。

通过遵循这些步骤，你将确定问题是否与服务器配置、WAR 文件放置或 WAR 文件本身有关，并相应地解决它。