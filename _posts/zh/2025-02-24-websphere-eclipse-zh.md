---
audio: false
generated: false
lang: zh
layout: post
title: 使用 WebSphere Liberty 与 Eclipse
translated: true
---

要在 Eclipse 中使用 WebSphere 插件工具并将其与 WebSphere Liberty 集成以进行工作，可以选择两个主要选项：**IBM Liberty 开发者工具**和 **Liberty 工具**。两者都可以通过 Eclipse Marketplace 获取，并提供构建、部署和管理 WebSphere Liberty 上的应用程序的功能，WebSphere Liberty 是一个轻量级、生产就绪的 Java EE 和云原生应用程序服务器。以下是如何使用和集成这些工具的详细指南。

---

### **工具概述**
- **IBM Liberty 开发者工具**：IBM 提供的传统插件，用于在 Eclipse 中管理 Liberty 服务器。它允许您创建和管理 Liberty 服务器、部署应用程序并直接从 IDE 调试。此工具适用于服务器中心工作流或不使用 Maven 或 Gradle 的项目。
- **Liberty 工具**：专注于 Maven 和 Gradle 项目的下一代开源替代方案。它提供了与构建工具更紧密的集成体验、自动检测 Liberty 项目以及支持 Liberty 的开发模式（开发模式）。此工具更适合现代、构建工具中心的工作流。

两种工具都简化了 WebSphere Liberty 的开发，但它们在方法上有所不同。选择最适合您项目类型和开发偏好的工具。

---

### **安装**
1. **安装 Eclipse**：
   - 使用兼容版本，例如 **Eclipse for Enterprise Java and Web Developers**。
   - 确保您的 Eclipse 版本支持您选择的插件（在市场列表中检查兼容性）。

2. **安装插件**：
   - 打开 Eclipse，转到 **Help > Eclipse Marketplace**。
   - 搜索：
     - "IBM Liberty Developer Tools" 以获取传统的 IBM 工具集，或
     - "Liberty Tools" 以获取开源替代方案。
   - 按照提示安装所需的插件。

---

### **设置 Liberty 运行时**
- **下载 Liberty**：
  - 如果尚未下载，请从 [官方 IBM 网站](https://www.ibm.com/docs/en/was-liberty) 下载 WebSphere Liberty 运行时。
  - 确保 Liberty 版本与您安装的插件兼容。

- **在 Eclipse 中配置运行时**：
  - 对于 **IBM Liberty Developer Tools**：
    - 转到 **Window > Preferences > Server > Runtime Environments**。
    - 点击“Add”，选择“Liberty Server”，并指定到您的 Liberty 安装目录的路径。
  - 对于 **Liberty 工具**：
    - 不需要显式运行时配置。Liberty 工具通过 Maven 或 Gradle 配置检测 Liberty 项目，因此请确保您的项目配置正确（见下文）。

---

### **与项目集成**
两种工具的集成过程略有不同。根据您安装的工具，请按照以下步骤操作。

#### **对于 IBM Liberty Developer Tools**
1. **创建 Liberty 服务器**：
   - 打开 **Servers** 视图 (**Window > Show View > Servers**)。
   - 在 Servers 视图中右键单击并选择 **New > Server**。
   - 从列表中选择“Liberty Server”，并按照向导配置服务器，包括指定到您的 Liberty 安装的路径。

2. **添加您的项目**：
   - 在 Servers 视图中右键单击服务器并选择 **Add and Remove...**。
   - 选择您的项目并将其移动到“Configured” 侧。

3. **启动服务器**：
   - 右键单击服务器并选择 **Start** 或 **Debug** 以运行您的应用程序。
   - 在指定的 URL（默认：`http://localhost:9080/<context-root>`）访问您的应用程序。

#### **对于 Liberty 工具 (Maven/Gradle 项目)**
1. **确保项目配置**：
   - 您的项目必须包含必要的 Liberty 插件：
     - 对于 Maven：在 `pom.xml` 中添加 `liberty-maven-plugin`。
     - 对于 Gradle：在 `build.gradle` 中添加 `liberty-gradle-plugin`。
   - `server.xml` 配置文件应位于标准位置：
     - 对于 Maven：`src/main/liberty/config`。
     - 对于 Gradle：根据项目结构进行调整。

2. **使用 Liberty 仪表板**：
   - 点击 Eclipse 工具栏中的 Liberty 图标以打开 **Liberty 仪表板**。
   - Liberty 工具会自动检测并在仪表板中列出您的 Liberty 项目。
   - 在仪表板中右键单击您的项目以访问命令，例如：
     - “在开发模式下启动”（自动重新部署更改而无需重新启动服务器）。
     - “运行测试”。
     - “查看测试报告”。

3. **访问您的应用程序**：
   - 服务器运行后，在指定的 URL（默认：`http://localhost:9080/<context-root>`）访问您的应用程序。
   - 在开发模式下，对代码进行更改，Liberty 会自动重新部署它们。

---

### **关键功能**
两种工具都提供强大的功能来提高生产力：

- **服务器管理**：
  - 直接从 Eclipse 启动、停止和调试 Liberty 服务器。
- **应用程序部署**：
  - 轻松部署和重新部署应用程序。
- **配置协助**：
  - 两种工具都提供代码补全、验证和悬停描述，用于 Liberty 配置文件（例如 `server.xml`）。
- **开发模式**：
  - 自动检测并重新部署代码更改而无需重新启动服务器（特别是在 Liberty 工具的开发模式下）。
- **调试**：
  - 将 Eclipse 调试器附加到 Liberty 服务器以进行故障排除。

---

### **考虑事项和潜在问题**
- **版本兼容性**：
  - 确保您的 Eclipse、插件和 Liberty 运行时版本兼容。检查文档以获取特定要求。
- **项目配置**：
  - 对于 Liberty 工具，您的项目必须是配置正确的 Maven 或 Gradle 项目，并包含 Liberty 插件。
  - 确保 `server.xml` 位于工具预期的位置，以便工具识别您的项目。
- **网络设置**：
  - 确保默认的 Liberty 端口（例如 9080 用于 HTTP，9443 用于 HTTPS）开放且未被防火墙阻止。
- **Java 兼容性**：
  - Liberty 是基于 Java 的服务器，因此请确保为您的 Liberty 运行时安装了兼容的 Java 版本。

---

### **使用 Liberty 工具的快速入门 (Maven/Gradle)**
如果您使用 Maven 或 Gradle，Liberty 工具提供了简化的体验。以下是分步指南：

1. 安装 **Eclipse for Enterprise Java and Web Developers**。
2. 转到 **Help > Eclipse Marketplace**，搜索“Liberty Tools”，并安装插件。
3. 创建或导入配置为 Liberty 的 Maven/Gradle 项目：
   - 您可以使用 [Open Liberty Starter](https://openliberty.io/start/) 生成示例项目。
4. 确保您的项目配置了 `liberty-maven-plugin`（用于 Maven）或 `liberty-gradle-plugin`（用于 Gradle）。
5. 通过点击工具栏中的 Liberty 图标打开 **Liberty 仪表板**。
6. 您的项目应出现在仪表板中。右键单击它并选择“在开发模式下启动”。
7. 在指定的 URL（默认：`http://localhost:9080/<context-root>`）访问您的应用程序。
8. 对代码进行更改；Liberty 开发模式会自动重新部署它们。
9. 使用仪表板运行测试或查看测试报告。

---

### **选择工具**
- **IBM Liberty Developer Tools**：
  - 适用于传统服务器管理方法或不使用 Maven 或 Gradle 的项目。
  - 提供 Servers 视图以显式管理 Liberty 服务器。
- **Liberty 工具**：
  - 更适合 Maven 或 Gradle 项目，与这些构建系统集成更紧密。
  - 提供 Liberty 仪表板以进行项目中心管理和开发模式支持。
  - 开源，允许社区贡献和更新。

两种工具都可以从 Eclipse Marketplace 获取，因此您可以尝试两者并选择最适合您工作流的工具。

---

总之，在 Eclipse 中使用 WebSphere 插件工具涉及安装适当的插件、设置 Liberty 运行时并配置项目以与 Liberty 协同工作。无论您选择 IBM Liberty Developer Tools 还是 Liberty 工具，两者都提供了强大的功能，以简化 Eclipse IDE 中的 WebSphere Liberty 开发。