---
audio: false
generated: true
lang: zh
layout: post
title: Maven 发布插件
translated: true
---

这是一个关于如何使用 **Maven 发布插件** 来管理和自动化 Maven 项目发布过程的全面指南。

---

### 什么是 Maven 发布插件？

**Maven 发布插件** 是一个自动化 Maven 项目发布过程的工具。它处理以下任务：

- 更新项目 POM 文件中的版本号。
- 提交更改到版本控制系统（VCS），例如 Git。
- 在 VCS 中为发布创建标签。
- 构建和部署发布构件。
- 通过更新版本号为下一个开发周期做准备。

插件的两个主要目标是：

- **`release:prepare`**：通过更新版本、提交更改和在 VCS 中标记发布来为项目发布做准备。
- **`release:perform`**：使用 VCS 中的标记代码构建和部署已发布的版本。

---

### 使用 Maven 发布插件的分步指南

#### 1. 将 Maven 发布插件添加到 POM 文件

要使用插件，需要在项目的 `pom.xml` 中包含它。在 `<build><plugins>` 部分添加如下内容：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-release-plugin</artifactId>
            <version>2.5.3</version> <!-- 使用最新的稳定版本 -->
        </plugin>
    </plugins>
</build>
```

**注意**：查看 [官方 Maven 发布插件页面](https://maven.apache.org/maven-release/maven-release-plugin/) 以获取最新版本，并相应地替换 `2.5.3`。

#### 2. 配置 SCM（源代码管理）部分

插件与 VCS（例如 Git）交互以提交更改和创建标签。必须在 `pom.xml` 的 `<scm>` 部分指定 VCS 详细信息。对于托管在 GitHub 上的 Git 仓库，可能如下所示：

```xml
<scm>
    <connection>scm:git:git://github.com/username/project.git</connection>
    <developerConnection>scm:git:git@github.com:username/project.git</developerConnection>
    <url>https://github.com/username/project</url>
</scm>
```

- 将 `username` 和 `project` 替换为实际的 GitHub 用户名和仓库名称。
- 如果使用不同的 Git 托管服务（例如 GitLab、Bitbucket），请调整 URL。
- 确保配置了必要的凭证（例如 SSH 密钥或个人访问令牌）以推送更改到仓库。

#### 3. 为发布准备项目

在运行发布命令之前，确保项目已准备好：

- 所有测试通过（`mvn test`）。
- 工作目录中没有未提交的更改（运行 `git status` 进行检查）。
- 处于正确的分支（例如 `master` 或 `main`）进行发布。

#### 4. 运行 `release:prepare`

`release:prepare` 目标为项目发布做准备。在终端中执行以下命令：

```bash
mvn release:prepare
```

**`release:prepare` 期间发生的情况**：

- **检查未提交的更改**：确保工作目录干净。
- **提示版本**：询问发布版本和下一个开发版本。
  - 例如：如果当前版本是 `1.0-SNAPSHOT`，它可能建议 `1.0` 作为发布版本和 `1.1-SNAPSHOT` 作为下一个开发版本。可以接受默认值或输入自定义版本（例如 `1.0.1` 用于补丁发布）。
- **更新 POM 文件**：将版本更改为发布版本（例如 `1.0`），提交更改并在 VCS 中标记它（例如 `project-1.0`）。
- **为下一个周期做准备**：将 POM 更新为下一个开发版本（例如 `1.1-SNAPSHOT`）并提交它。

**可选的干运行**：要测试过程而不进行更改，使用：

```bash
mvn release:prepare -DdryRun=true
```

这将模拟准备步骤而不提交或标记。

#### 5. 运行 `release:perform`

准备好发布后，使用以下命令构建和部署它：

```bash
mvn release:perform
```

**`release:perform` 期间发生的情况**：

- 从 VCS 检出标记的版本。
- 构建项目。
- 将构件部署到 POM 中 `<distributionManagement>` 部分指定的仓库。

**配置 `<distributionManagement>`**（如果部署到远程仓库）：

```xml
<distributionManagement>
    <repository>
        <id>releases</id>
        <url>http://my-repository-manager/releases</url>
    </repository>
    <snapshotRepository>
        <id>snapshots</id>
        <url>http://my-repository-manager/snapshots</url>
    </snapshotRepository>
</distributionManagement>
```

- 将 URL 替换为仓库管理器的地址（例如 Nexus、Artifactory）。
- 确保在 `~/.m2/settings.xml` 文件的 `<servers>` 下配置了匹配 `id` 的凭证。

#### 6. 验证发布

在 `release:perform` 之后，验证发布：

- 检查仓库管理器以确保构件（例如 JAR、源代码）已部署。
- 通过在其 POM 中将其添加为依赖项在另一个项目中测试已发布的版本。

---

### 附加配置和技巧

#### 处理失败

- **清理**：如果发布过程失败，使用：
  ```bash
  mvn release:clean
  ```
  删除插件创建的临时文件。
- **回滚**：要撤消 `release:prepare` 所做的更改：
  ```bash
  mvn release:rollback
  ```
  谨慎操作并验证哪些更改被撤消。

#### 多模块项目

对于多模块项目，插件默认情况下会一致地更新所有模块的版本。确保父 POM 包含插件和 SCM 配置。

#### 批处理模式用于自动化

要非交互式运行发布（例如在 CI/CD 管道中），使用 `-B` 标志并指定版本：

```bash
mvn release:prepare -B -DreleaseVersion=1.0 -DdevelopmentVersion=1.1-SNAPSHOT
mvn release:perform -B
```

#### 常见问题及解决方案

- **VCS 错误**：确保 Git 命令（例如 `git commit`、`git push`）手动工作。检查身份验证（SSH 密钥、令牌）。
- **构建失败**：验证构建在本地成功（`mvn clean install`）并且依赖项正确解析。
- **版本策略**：在提示期间或通过属性自定义版本，如果默认值不适合您的需求。

---

### 命令摘要

1. **准备发布**：
   ```bash
   mvn release:prepare
   ```
2. **执行发布**：
   ```bash
   mvn release:perform
   ```
3. **可选的干运行**：
   ```bash
   mvn release:prepare -DdryRun=true
   ```
4. **清理或回滚（如果需要）**：
   ```bash
   mvn release:clean
   mvn release:rollback
   ```

---

### 结论

Maven 发布插件通过自动化版本管理、VCS 交互和部署简化了发布过程。通过将插件添加到 POM、配置 SCM 并按照 `release:prepare` 和 `release:perform` 步骤操作，可以高效地发布 Maven 项目。始终使用干运行测试配置并验证结果，以确保流畅的发布过程。