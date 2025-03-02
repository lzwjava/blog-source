---
audio: false
generated: false
lang: zh
layout: post
title: 使用 WebSphere Liberty 服务器在 VSCode 中
translated: true
---

要在 Visual Studio Code (VSCode) 中使用 WebSphere Liberty 服务器，可以利用 **Liberty Tools** 扩展，该扩展支持 Open Liberty 和 WebSphere Liberty。该扩展允许您在 VSCode 中管理 Liberty 服务器、部署应用程序并进行调试，从而简化开发工作流程。

### 在 VSCode 中使用 WebSphere Liberty 的步骤

#### 1. **安装 Liberty Tools 扩展**
   - 打开 VSCode，导航到扩展视图，点击活动栏中的扩展图标或按 `Ctrl+Shift+X`。
   - 在扩展商店中搜索 "Liberty Tools"。
   - 点击 "安装" 将扩展添加到 VSCode。
   - 如果提示，重新加载 VSCode 以启用扩展。

#### 2. **设置先决条件**
   - **Java**：确保安装了兼容版本的 Java（推荐 Java 8 或更高版本）。Liberty 是基于 Java 的服务器，因此 Java 是运行它的必要条件。
   - **WebSphere Liberty**：如果尚未安装，下载并安装 WebSphere Liberty 运行时。可以从 [IBM 官方网站](https://www.ibm.com/docs/en/was-liberty) 获取。请注意安装目录，因为您需要它来配置扩展。

#### 3. **配置 Liberty Tools 扩展**
   - 安装扩展后，配置它指向您的 Liberty 安装。
   - 打开 VSCode 的命令面板，按 `Ctrl+Shift+P`。
   - 输入 "Liberty: Add Liberty Runtime" 并选择该命令。
   - 提供 Liberty 安装目录的路径（例如，`/opt/ibm/wlp`）。
   - 扩展将检测到 Liberty 运行时并使其在 VSCode 中可用。

#### 4. **管理您的 Liberty 服务器**
   - 配置完成后，可以直接在 VSCode 中管理您的 Liberty 服务器。
   - **Liberty 仪表板**：在资源管理器窗格或通过命令面板访问 Liberty 仪表板视图。该仪表板列出了您的 Liberty 项目和服务器。
   - **启动/停止服务器**：在仪表板中右键单击服务器以启动、停止或重新启动它。
   - **部署应用程序**：对于 Liberty 项目（例如，带有 Liberty 插件的 Maven 或 Gradle 项目），右键单击项目并选择 "Deploy to Liberty" 以部署应用程序。
   - **开发模式（Dev Mode）**：对于 Maven 或 Gradle 项目，以开发模式启动服务器，该模式会自动检测代码更改、重新编译并重新部署应用程序而无需重新启动服务器。这对于迭代开发非常理想。

#### 5. **调试和测试**
   - **调试**：直接从 VSCode 将调试器附加到运行中的 Liberty 服务器。使用 Liberty 仪表板中的 "Debug" 选项或在 VSCode 的运行和调试视图中设置调试配置。
   - **运行测试**：如果项目包含测试，可以从仪表板运行它们并在 VSCode 中查看结果。

#### 6. **其他功能**
   - **配置协助**：扩展为 Liberty 配置文件（例如 `server.xml`）提供代码补全、验证和悬停描述，简化服务器配置。
   - **语言支持**：支持 Java、MicroProfile 和 Jakarta EE API，增强开发体验。

### 主要优势
- **无缝集成**：在不离开 VSCode 的情况下管理您的 Liberty 服务器，提高效率。
- **自动部署**：在开发模式下，代码更改会自动检测并部署，节省开发时间。
- **调试支持**：轻松将调试器附加到服务器以进行故障排除。
- **轻量级和高效**：Liberty Tools 设计轻量级，与 Liberty 专注于速度和效率的理念一致。

### 其他资源
- 详细指南，请参考 [Open Liberty 文档](https://openliberty.io/docs/) 和 [Liberty Tools VSCode 文档](https://openliberty.io/docs/latest/develop/liberty-tools.html)。
- 如果遇到问题，请查看扩展的故障排除部分或在 Stack Overflow 等平台上寻求社区帮助。

通过遵循这些步骤，您可以在 VSCode 中有效使用 WebSphere Liberty，利用其功能增强开发过程。