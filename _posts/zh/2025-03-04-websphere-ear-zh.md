---
audio: true
generated: true
lang: zh
layout: post
title: WebSphere Liberty Profile 中的 EAR 部署
translated: true
---

听起来你已经成功使用 `mvn package` 通过 Maven 构建了一个 EAR（企业档案）文件，并且构建过程没有任何错误。然而，当你将这个 EAR 部署到 WebSphere Liberty Profile（WLP）并启动服务器时，遇到了“未找到模块”错误。这令人困惑，因为平滑的构建通常暗示一切正常，但服务器没有按预期识别你的应用程序。让我们分解并找出可能发生的情况，以及解决问题的步骤。

### 理解问题
EAR 文件是一个标准的 Java EE 归档文件，通常包含一个或多个模块，如 WAR 文件（用于 Web 应用程序）、JAR 文件（用于 EJBs 或库）和部署描述符（`application.xml`）。当你将 EAR 部署到 WLP 时，服务器应该检测到这些模块并启动应用程序。消息“未找到模块”表明 WLP 可能无法找到 EAR 中的任何模块，或者不识别它们，从而阻止应用程序启动。

由于你的 Maven 构建是成功的（“一切顺利”），问题可能出在以下三个方面之一：
1. **EAR 文件内容**：EAR 可能不包含预期的模块，或者部署描述符可能缺失或不正确。
2. **部署过程**：你将 EAR 部署到 WLP 的方式可能不符合服务器期望的方式来找到和处理它。
3. **服务器配置**：WLP 可能没有设置为识别 EAR 中的模块，因为缺少功能或配置错误。

让我们探讨这些可能性，并提供可操作的步骤来诊断和解决问题。

---

### 可能的原因和解决方案

#### 1. EAR 文件可能为空或打包不正确
尽管构建成功，但你的 EAR 可能不包含任何模块（例如 WAR 或 JAR 文件），或者 `application.xml` 文件（告诉服务器包含哪些模块）可能缺失或配置不正确。

- **为什么会发生**：在 Maven EAR 项目中，`maven-ear-plugin` 负责组装 EAR。它根据你的 `pom.xml` 配置或依赖项包含模块。如果没有指定模块，或者依赖项（如 WAR）没有正确定义或解析，EAR 可能为空或缺少合适的 `application.xml`。
- **如何检查**：
  - 使用工具（如 `unzip`）打开你的 EAR 文件，或者在终端中运行 `jar tf myApp.ear` 列出其内容。
  - 查找：
    - 模块文件（例如 `my-web.war`、`my-ejb.jar`）在 EAR 的根目录。
    - `META-INF/application.xml` 文件。
  - 在 `application.xml` 内部，你应该看到定义模块的条目，例如：
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <application>
        <module>
            <web>
                <web-uri>my-web.war</web-uri>
                <context-root>/myapp</context-root>
            </web>
        </module>
    </application>
    ```
- **如何修复**：
  - 验证 EAR 模块的 `pom.xml`。确保你已经指定了要包含的模块的依赖项，例如：
    ```xml
    <dependencies>
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>my-web</artifactId>
            <type>war</type>
        </dependency>
    </dependencies>
    ```
  - 如果需要，配置 `maven-ear-plugin`：
    ```xml
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-ear-plugin</artifactId>
        <version>3.3.0</version>
        <configuration>
            <modules>
                <webModule>
                    <groupId>com.example</groupId>
                    <artifactId>my-web</artifactId>
                    <contextRoot>/myapp</contextRoot>
                </webModule>
            </modules>
        </configuration>
    </plugin>
    ```
  - 使用 `mvn clean package` 重新构建并重新检查 EAR 内容。

如果 EAR 为空或 `application.xml` 缺失/不正确，这可能是根本原因。修复 Maven 配置应该解决问题。

---

#### 2. 部署方法问题
你将 EAR 部署到 WLP 的方式也可能是问题所在。WLP 支持两种主要的部署方法：`dropins` 目录和 `server.xml` 中的显式配置。

- **使用 `dropins` 目录**：
  - 如果你将 EAR 放在 `wlp/usr/servers/<serverName>/dropins/` 目录中，WLP 应该自动检测并部署它。
  - 然而，对于 EAR 文件，自动部署可能不会总是按预期工作，特别是如果需要额外配置（如上下文根）。
- **使用 `server.xml`**：
  - 对于 EAR 文件，通常最好在 `wlp/usr/servers/<serverName>/server.xml` 中显式配置应用程序：
    ```xml
    <server>
        <featureManager>
            <feature>servlet-3.1</feature> <!-- 确保启用所需功能 -->
        </featureManager>
        <application id="myApp" name="myApp" type="ear" location="${server.config.dir}/apps/myApp.ear"/>
    </server>
    ```
  - 将 EAR 放在 `wlp/usr/servers/<serverName>/apps/`（或相应调整 `location` 路径）。
- **如何检查**：
  - 确认你放置 EAR 的位置以及你启动服务器的方式（例如 `./bin/server run <serverName>`）。
  - 检查服务器日志（例如 `wlp/usr/servers/<serverName>/logs/console.log` 或 `messages.log`）以获取部署消息。
- **如何修复**：
  - 尝试在 `server.xml` 中配置 EAR，如上所示，而不是依赖 `dropins`。
  - 更改后重新启动服务器：`./bin/server stop <serverName>` 后跟 `./bin/server start <serverName>`。

如果 EAR 没有正确注册到服务器，这可能解释了错误。

---

#### 3. 缺少服务器功能
WLP 是一个轻量级服务器，只加载你在 `server.xml` 中启用的功能。如果你的 EAR 包含需要特定功能（例如 servlet、EJBs）的模块，并且这些功能没有启用，WLP 可能无法识别或加载模块。

- **为什么会发生**：例如，WAR 文件需要 `servlet-3.1` 功能（或更高版本），而 EJB 模块需要 `ejbLite-3.2`。没有这些功能，服务器可能无法处理模块。
- **如何检查**：
  - 查看你的 `server.xml` 并检查 `<featureManager>` 部分。
  - 常见功能包括：
    - `<feature>servlet-3.1</feature>` 用于 Web 模块。
    - `<feature>ejbLite-3.2</feature>` 用于 EJB 模块。
  - 审查服务器日志以获取有关缺少功能的消息（例如“所需功能未安装”）。
- **如何修复**：
  - 根据应用程序的需求，将必要的功能添加到 `server.xml`：
    ```xml
    <featureManager>
        <feature>servlet-3.1</feature>
        <!-- 根据需要添加其他功能 -->
    </featureManager>
    ```
  - 重新启动服务器以应用更改。

如果缺少功能，启用它们应该允许 WLP 识别模块。

---

### 诊断步骤
为了找出问题，请按照以下步骤进行：

1. **检查 EAR 文件**：
   - 运行 `jar tf myApp.ear` 或解压缩它。
   - 确保它包含你的模块（例如 `my-web.war`）和有效的 `META-INF/application.xml`。

2. **检查 Maven 构建**：
   - 审查 EAR 模块的 `pom.xml` 以确认依赖项和 `maven-ear-plugin` 配置。
   - 再次运行 `mvn clean package` 并检查构建输出，查找有关包含模块的消息（例如“添加模块 my-web.war”）。

3. **验证部署**：
   - 确认 EAR 的位置（例如 `dropins` 或 `apps`）。
   - 如果使用 `dropins`，尝试将其移动到 `apps` 并将其添加到 `server.xml`。

4. **检查服务器日志**：
   - 启动服务器并检查 `console.log` 或 `messages.log`，以获取超出“未找到模块”的详细错误消息。
   - 查找线索，例如“应用程序不包含任何模块”或与功能相关的错误。

5. **使用简单的 EAR 进行测试**：
   - 使用已知工作的 `pom.xml` 创建一个包含单个 WAR 文件的基本 EAR，并将其部署到 WLP。如果它工作，问题可能特定于你的原始 EAR 的打包。

---

### 最有可能的原因
鉴于你的构建顺利但 WLP 报告“未找到模块”，最有可能的原因是 **EAR 文件不包含任何模块** 或 **`application.xml` 缺失/不正确**。这可能发生在你的 `pom.xml` 没有正确指定要包含的模块，即使 Maven 没有标记错误。或者，如果 EAR 正确，问题可能与部署（例如未在 `server.xml` 中配置）或缺少服务器功能有关。

### 最终建议
- 从检查 EAR 的内容（`jar tf myApp.ear`）和你的 `pom.xml` 配置开始。
- 如果 EAR 为空或缺少 `application.xml`，修复 Maven 设置并重新构建。
- 如果 EAR 看起来正确，在 `server.xml` 中配置它，确保启用所需功能，并重新部署。
- 检查服务器日志以获取更多上下文。

通过这些步骤，你应该能够确定问题是构建、部署还是服务器配置，并成功在 WLP 上运行你的应用程序。如果你需要帮助进行特定配置，请告诉我！