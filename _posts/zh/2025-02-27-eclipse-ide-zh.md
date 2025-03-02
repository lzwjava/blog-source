---
audio: false
generated: true
lang: zh
layout: post
title: 使用Eclipse
translated: true
---

### 关键要点
- 似乎可以有效地使用 Eclipse 与 IBM Websphere Liberty、Spring、Spring Boot 和 Maven，但需要特定的配置。
- 研究表明，在 Eclipse 中安装 Spring Tool Suite（STS）和 IBM Liberty Developer Tools 作为插件，以获得增强的功能。
- 证据表明，使用 STS 或 Spring Initializr 创建 Spring Boot 项目，然后为 Websphere Liberty 部署进行配置。

### 配置 Eclipse
首先，从 [Eclipse 下载](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) 下载并安装“Eclipse IDE for Enterprise Java and Web Developers”。确保已安装 JDK 17 或更高版本，可以通过在终端中运行 `java -version` 进行验证。

### 配置 Spring 和 Spring Boot
通过在 Eclipse 中转到 Help -> Eclipse Marketplace，搜索“Spring Tools”，并安装适当的版本来安装 Spring Tool Suite（STS）插件。这增强了 Spring 和 Spring Boot 开发。可以通过 File -> New -> Spring Starter Project 在 Eclipse 中直接创建新的 Spring Boot 项目，选择 Maven 作为构建工具，并添加必要的依赖项，如 Spring Web。

### 集成 IBM Websphere Liberty
通过搜索“IBM Liberty Developer Tools”并按照安装提示进行操作，从 Eclipse Marketplace 安装 IBM Liberty Developer Tools。通过 Window -> Preferences -> Servers -> Runtime Environments，添加新的 Websphere Liberty 运行时，并通过 File -> New -> Other -> Server 创建服务器实例。确保服务器的 server.xml 包含 `<feature>springBoot-2.0</feature>`，以支持 Spring Boot，如 [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html) 中所述。

### 部署您的应用程序
修改 Spring Boot 应用程序以扩展 `SpringBootServletInitializer` 而不是使用启动嵌入式服务器的主方法，通过在 pom.xml 中设置 `<packaging>war</packaging>` 将其打包为 WAR 文件。通过右键点击项目，选择“Run As -> Run on Server”，并选择您的 Liberty 服务器进行部署。这确保应用程序在 Liberty 的 Web 容器上运行。

---

### 调查说明：使用 Eclipse 与 IBM Websphere Liberty、Spring、Spring Boot 和 Maven 的全面指南

本指南提供了详细的操作步骤，介绍如何在 Eclipse 中有效地使用 IBM Websphere Liberty、Spring、Spring Boot 和 Maven，适用于在这些生态系统中工作的开发人员。该过程涉及设置 Eclipse、安装必要的插件、创建和配置项目以及部署应用程序，重点介绍集成和最佳实践，截至 2025 年 2 月 27 日。

#### Eclipse 设置和先决条件
Eclipse 是用于 Java 开发的强大 IDE，特别是用于企业应用程序。对于此设置，下载“Eclipse IDE for Enterprise Java and Web Developers” 2024-06 版本，可在 [Eclipse 下载](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) 找到。确保系统安装了 JDK 17 或更高版本，可以通过在终端中运行 `java -version` 进行检查。此版本确保与现代 Spring 和 Liberty 功能兼容。

#### 安装必要的插件
要增强 Eclipse 以进行 Spring 和 Spring Boot 开发，安装 Spring Tool Suite（STS），即下一代 Spring 工具。通过 Help -> Eclipse Marketplace 访问，搜索“Spring Tools”，并安装标有“Spring Tools（即 Spring IDE 和 Spring Tool Suite）”的条目。此插件，详见 [Spring Tools](https://spring.io/tools/)，为基于 Spring 的应用程序提供了世界级的支持，与 Eclipse 无缝集成，提供项目创建和调试等功能。

对于 IBM Websphere Liberty 集成，通过搜索“IBM Liberty Developer Tools”安装 IBM Liberty Developer Tools，也可通过 Eclipse Marketplace 找到。此插件，适用于 Eclipse 2024-06，详见 [IBM Liberty Developer Tools](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)，便于将 Java EE 应用程序构建和部署到 Liberty，支持自 2019-12 以来的版本。

#### 创建 Spring Boot 项目
在安装了 STS 的 Eclipse 中有两种主要方法创建 Spring Boot 项目：

1. **使用 Spring Initializr**：访问 [Spring Initializr](https://start.spring.io/)，选择 Maven 作为构建工具，选择项目元数据（组、工件等），并添加依赖项，如 Spring Web。将项目生成为 ZIP 文件，解压缩，并通过 File -> Import -> Existing Maven Project 将其导入 Eclipse，选择解压缩后的文件夹。

2. **直接使用 STS**：打开 Eclipse，转到 File -> New -> Other，展开 Spring Boot，选择“Spring Starter Project”。按照向导操作，确保选择 Maven 作为类型，并选择依赖项。此方法，详见 [Creating Spring Boot Project with Eclipse and Maven](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)，优先选择与 Eclipse 工作区集成。

两种方法都确保了 Maven 为基础的项目，这对于 Spring Boot 的依赖管理至关重要。

#### 配置 Websphere Liberty 部署
要部署到 Websphere Liberty，请修改 Spring Boot 应用程序以在 Liberty 的 Web 容器上运行，而不是启动嵌入式服务器。这包括：

- 确保主应用程序类扩展 `SpringBootServletInitializer`。例如：

  ```java
  @SpringBootApplication
  public class MyApplication extends SpringBootServletInitializer {
      // 没有主方法；Liberty 处理启动
  }
  ```

- 更新 pom.xml 以将其打包为 WAR 文件，添加：

  ```xml
  <packaging>war</packaging>
  ```

  这对于传统的 servlet 容器部署是必要的，详见 [Deploying Spring Boot Applications](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet)。

Websphere Liberty，特别是其开源变体 Open Liberty，支持具有特定功能的 Spring Boot 应用程序。确保 Liberty 服务器的 server.xml 包含 `<feature>springBoot-2.0</feature>`，以支持 Spring Boot 2.x，详见 [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html)。此配置禁用嵌入式 Web 容器，利用 Liberty 的容器。

#### 在 Eclipse 中设置和配置 Websphere Liberty 服务器
安装 IBM Liberty Developer Tools 后，设置 Liberty 服务器：

- 转到 Window -> Preferences -> Servers -> Runtime Environments，点击“Add”，选择“WebSphere Application Server Liberty”。按照向导操作，找到 Liberty 安装，通常在类似 `<Liberty_Root>/wlp` 的目录中，详见 [Liberty and Eclipse](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9)。

- 通过 File -> New -> Other -> Server，选择“WebSphere Application Server Liberty”和配置的运行时，创建新的服务器实例。命名服务器并根据需要调整设置。

- 通过 Servers 视图编辑服务器的 server.xml，添加必要的功能。对于 Spring Boot，添加：

  ```xml
  <featureManager>
      <feature>springBoot-2.0</feature>
      <!-- 其他功能，如 servlet-3.1 以支持 Web -->
  </featureManager>
  ```

此设置，支持 [IBM WebSphere Liberty](https://www.ibm.com/docs/en/was-liberty/base?topic=liberty-overview)，确保与 Spring Boot 应用程序兼容。

#### 部署和运行应用程序
要部署，右键点击项目资源管理器中的项目，选择“Run As -> Run on Server”，选择您的 Liberty 服务器，然后点击“Finish”。Eclipse 将 WAR 文件部署到 Liberty 服务器，可以在控制台视图中监控日志。确保在 server.xml 中正确设置应用程序上下文根，通常在 `<webApplication>` 标签下，以通过适当的 URL 访问您的应用程序，例如 `http://localhost:9080/yourapp`。

对于调试，使用调试视图，根据需要设置断点，利用 Liberty 对远程调试的支持，详见 [Debugging with Eclipse and Liberty](https://stackoverflow.com/questions/41428156/how-to-debug-web-service-with-eclipse-websphere-liberty)。

#### 附加考虑
- **打包选项**：虽然 WAR 是 servlet 容器的标准，Open Liberty 也支持 JAR 部署，详见 [Configure and Deploy Spring Boot to Open Liberty](https://openliberty.io/docs/latest/deploy-spring-boot.html)。对于 JAR，确保应用程序配置为不启动嵌入式服务器，这可能需要额外的 Liberty 功能或配置。
- **Maven 集成**：使用 Maven 进行依赖管理，确保包含 `liberty-maven-plugin` 以进行自动化部署，详见 [IBM Liberty Maven Plugin](https://github.com/WASdev/ci.maven#liberty-maven-plugin)。
- **故障排除**：如果出现问题，检查 Liberty 服务器实例下的 `logs` 目录中的服务器日志，并确保 Liberty 版本与 Spring Boot 兼容，例如 Liberty 8.5.5.9 或更高版本支持可运行的 JAR，详见 [Stack Overflow Discussion](https://stackoverflow.com/questions/36132791/how-to-use-websphere-liberty-in-spring-boot-application)。

此全面的设置确保了在 IBM Websphere Liberty 上使用 Eclipse 开发和部署 Spring Boot 应用程序，利用 Maven 进行构建管理。

#### 表：部署选项比较

| 部署类型 | 优点                                      | 缺点                                      | 配置说明                          |
|---------|-------------------------------------------|-------------------------------------------|----------------------------------|
| WAR 文件 | 适用于 servlet 容器，广泛支持             | 需要扩展 `SpringBootServletInitializer` | 在 pom.xml 中设置 `<packaging>war</packaging>` |
| JAR 文件 | 开发简单，支持 Open Liberty               | 可能需要额外的 Liberty 功能               | 确保没有嵌入式服务器启动，使用 springBoot 功能 |

此表，源自 [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html)，有助于根据项目需求选择适当的部署策略。

### 关键引用
- [Creating Spring Boot Project with Eclipse and Maven, step-by-step guide](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)
- [IBM Liberty Developer Tools, Eclipse plugin for Java EE applications](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)
- [Open Liberty Docs, deploying Spring Boot applications](https://openliberty.io/docs/latest/deploy-spring-boot.html)
- [Spring Tools, next generation tooling for Spring development](https://spring.io/tools/)
- [Eclipse Downloads, packages for enterprise Java development](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers)
- [Liberty and Eclipse, installing development environment](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9)
- [Deploying Spring Boot Applications, Spring Boot reference](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet)