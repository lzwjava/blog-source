---
audio: false
generated: false
lang: zh
layout: post
title: WebSphere Liberty - 你好，世界应用程序
translated: true
---

这是一个在您的 WebSphere Liberty 服务器上运行 "Hello World" 应用程序的简单示例，假设您已经按照之前的说明启用了 `javaee-8.0` 功能。这个示例使用一个基本的 JSP（JavaServer Pages）文件，并通过 `dropins` 目录进行部署，以简化操作。

### 分步指南

#### 1. 创建应用程序目录和文件
您将通过在 Liberty 服务器的 `dropins` 目录中放置一个 JSP 文件来创建一个小型 Web 应用程序。`dropins` 目录允许 Liberty 自动检测和部署应用程序。

- **定位 `dropins` 目录**：
  导航到服务器文件夹中的 `dropins` 目录。如果您的 Liberty 安装位于 `/opt/ibm/wlp`，并且服务器名为 `myServer`，路径如下：
  ```
  /opt/ibm/wlp/usr/servers/myServer/dropins
  ```
  将 `/opt/ibm/wlp` 替换为您的实际 Liberty 安装目录，将 `myServer` 替换为您的服务器名称。

- **创建一个爆破 WAR 目录**：
  在 `dropins` 目录中，创建一个名为 `myApp.war` 的目录。`.war` 扩展名告诉 Liberty 将其视为一个 Web 应用程序。使用以下命令：
  ```bash
  mkdir -p /opt/ibm/wlp/usr/servers/myServer/dropins/myApp.war
  ```

- **创建 `index.jsp` 文件**：
  在 `myApp.war` 中，创建一个名为 `index.jsp` 的文件，内容如下，以显示 "Hello World!"：
  ```jsp
  <html>
  <body>
  <h2>Hello World!</h2>
  </body>
  </html>
  ```
  您可以直接使用以下命令创建它：
  ```bash
  echo '<html><body><h2>Hello World!</h2></body></html>' > /opt/ibm/wlp/usr/servers/myServer/dropins/myApp.war/index.jsp
  ```
  或者，使用文本编辑器创建 `index.jsp` 并将其保存到该位置。

#### 2. 启动服务器（如果尚未运行）
如果您的服务器没有运行，您需要启动它，以便它可以部署和提供应用程序。

- **导航到 `bin` 目录**：
  进入 Liberty 安装的 `bin` 目录：
  ```bash
  cd /opt/ibm/wlp/bin
  ```

- **启动服务器**：
  以前台模式运行服务器，以直接查看输出：
  ```bash
  ./server run myServer
  ```
  或者，在后台启动它：
  ```bash
  ./server start myServer
  ```
  如果服务器已经在运行，请跳过此步骤——Liberty 将自动检测新应用程序。

#### 3. 验证应用程序部署
Liberty 将在 `dropins` 目录中检测到 `myApp.war` 应用程序时自动部署它。

- **检查控制台输出**：
  如果您以前台模式启动了服务器，请查找类似以下的消息：
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myApp/
  ```
  这确认了应用程序已部署并可用。

- **检查日志（如果在后台运行）**：
  如果服务器在后台运行，请在以下位置查找相同的部署消息：
  ```
  /opt/ibm/wlp/usr/servers/myServer/logs/console.log
  ```

#### 4. 访问应用程序
现在应用程序已部署，您可以在 Web 浏览器中查看它。

- **打开浏览器**：
  导航到：
  ```
  http://localhost:9080/myApp/
  ```
  上下文根 `/myApp` 来自 `myApp.war` 目录名称，`index.jsp` 默认作为欢迎文件提供。

- **预期结果**：
  您应该看到一个显示以下内容的页面：
  ```
  Hello World!
  ```
  以大字体显示。

### 注意事项
- **端口号**：此示例使用端口 `9080`，这是 Liberty 的默认 HTTP 端口。如果您配置了不同的端口，请相应调整 URL（例如，`http://localhost:YOUR_PORT/myApp/`）。
- **权限**：确保您对 `dropins` 目录具有写权限。
- **JSP 支持**：`javaee-8.0` 功能包括 JSP 支持，因此无需额外配置。
- **故障排除**：如果页面未加载，请检查服务器日志 `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` 中的错误，或者确保服务器正在运行，文件位于正确位置。

这个简单的示例演示了如何在 WebSphere Liberty 服务器上使用 `dropins` 目录进行自动部署来部署和运行 "Hello World" 应用程序。享受您的第一个 Liberty 应用程序！

---

以下是在 WebSphere Liberty 上部署 "Hello World" 应用程序时的工作原理解释：

### 1. **Dropins 目录**
WebSphere Liberty 提供了一种通过 `dropins` 目录部署应用程序的便捷功能。这是一个特殊的文件夹，您可以将应用程序（作为 WAR（Web Application Archive）文件或爆破 WAR 目录）放置其中，Liberty 将自动检测并部署它。与传统部署方法不同，您不需要在 `server.xml` 文件中手动配置应用程序。当 Liberty 启动或在 `dropins` 文件夹中检测到更改（例如添加新应用程序）时，它会自动启动部署过程。

### 2. **使用爆破 WAR 目录**
在这个示例中，应用程序作为一个名为 `myApp.war` 的爆破 WAR 目录进行部署，而不是单个打包的 WAR 文件。爆破 WAR 只是包含 Web 应用程序的所有内容（例如 HTML、JSP 文件和其他资源）的文件夹，以未压缩的形式。Liberty 将此目录视为 WAR 文件，将其部署为一个完全功能的 Web 应用程序。这种方法在开发过程中特别有用，因为您可以直接编辑文件（例如调整 HTML 或 JSP），而无需重新打包所有内容到 WAR 文件中。

### 3. **JSP 文件**
这个 "Hello World" 应用程序的核心是一个名为 `index.jsp` 的文件，这是一个 JavaServer Page（JSP）。该文件包含基本的 HTML 以在屏幕上显示 "Hello World!"，并且可以包含 Java 代码（尽管在这种情况下，它保持简单）。当您访问应用程序时，Liberty 会动态编译 JSP 为 servlet（一个小型 Java 程序，用于生成网页），并将其提供给您的浏览器。

### 4. **启用 Java EE 功能**
为了使所有这些工作，Liberty 依赖于在其配置文件 `server.xml` 中启用特定功能。在这里，启用了 `javaee-8.0` 功能，它为 JSP、servlet 和 Java Enterprise Edition（EE）8 平台的其他组件提供支持。此功能确保 Liberty 加载了运行应用程序所需的必要库和设置。

### 5. **自动部署过程**
一旦将 `myApp.war` 目录放置在 `dropins` 文件夹中并启动 Liberty（或者如果它已经在运行），服务器会自动检测并部署应用程序。您将在 Liberty 的输出中看到日志消息，指示应用程序已启动并可在特定 URL 访问。这种无需手动操作的部署过程使得快速启动和运行应用程序变得非常简单。

### 6. **访问应用程序：上下文根**
您可以访问应用程序的 URL 由其 **上下文根** 确定，这只是 WAR 文件或目录的名称。在这种情况下，由于目录名为 `myApp.war`，上下文根变为 `/myApp`。默认情况下，Liberty 在端口 `9080` 上运行，因此访问应用程序的完整 URL 为 `http://localhost:9080/myApp/`。

### 7. **提供欢迎文件**
当您在浏览器中访问 `http://localhost:9080/myApp/` 时，Liberty 需要确定要显示的内容。它会查找 **欢迎文件**——当未请求特定文件时要提供的默认页面。在这种情况下，`index.jsp` 位于 `myApp.war` 目录的根目录中，并默认被识别为欢迎文件。Liberty 编译并提供 `index.jsp`，然后在您的屏幕上显示 "Hello World!"。

### 总结
这个 "Hello World" 应用程序展示了 WebSphere Liberty 如何简化 Web 应用程序部署。通过利用 `dropins` 目录进行自动部署、支持爆破 WAR 以便于编辑，以及使用 `javaee-8.0` 功能以实现 Java EE 兼容性，Liberty 让您能够快速部署和测试一个简单的 Web 应用程序，而无需复杂的设置。结果是一个轻量级、开发者友好的方法，可以在 `http://localhost:9080/myApp/` 看到 "Hello World!"，非常适合学习或原型设计。