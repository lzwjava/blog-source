---
audio: false
generated: true
lang: zh
layout: post
title: Maven 依赖插件
translated: true
---

**Maven 依赖插件** 是 Maven 中一个强大的工具，Maven 是一个广泛使用的 Java 项目构建自动化工具，它帮助你管理和操作项目依赖。Maven 项目中的依赖是外部库或模块，声明在 `pom.xml` 文件中，Maven 从仓库下载并在编译、运行或测试时使用。依赖插件通过提供各种目标（任务）来分析、复制、列出或处理这些依赖，从而扩展了这一功能。以下是如何有效使用它的方法：

---

#### **1. 使用概述**
你可以通过两种主要方式使用 Maven 依赖插件：
- **在 `pom.xml` 文件中配置它**：这允许你将特定的插件目标绑定到 Maven 构建生命周期的阶段（例如 `package`、`install`），以便在构建过程中自动执行。
- **直接从命令行运行目标**：这对于一次性任务或不想修改 `pom.xml` 的情况非常理想。

插件由其坐标标识：`groupId: org.apache.maven.plugins`，`artifactId: maven-dependency-plugin`。在配置时需要指定一个版本（例如 `3.2.0`），尽管在命令行使用时 Maven 通常可以解析最新版本。

---

#### **2. 将插件添加到 `pom.xml`**
要将插件作为构建过程的一部分使用，将其添加到 `pom.xml` 的 `<build><plugins>` 部分。以下是一个基本示例：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.2.0</version>
        </plugin>
    </plugins>
</build>
```

使用此设置，可以通过添加 `<executions>` 块来配置在构建生命周期中执行的特定目标。

---

#### **3. 常见目标及其使用方法**
插件为管理依赖提供了几个目标。以下是一些最常用的目标，以及如何使用它们的示例：

##### **a. `copy-dependencies`**
- **目的**：将项目依赖复制到指定目录（例如，打包到 `lib` 文件夹）。
- **在 `pom.xml` 中配置**：将此目标绑定到 `package` 阶段，以便在 `mvn package` 时复制依赖：

  ```xml
  <build>
      <plugins>
          <plugin>
              <groupId>org.apache.maven.plugins</groupId>
              <artifactId>maven-dependency-plugin</artifactId>
              <version>3.2.0</version>
              <executions>
                  <execution>
                      <id>copy-dependencies</id>
                      <phase>package</phase>
                      <goals>
                          <goal>copy-dependencies</goal>
                      </goals>
                      <configuration>
                          <outputDirectory>${project.build.directory}/lib</outputDirectory>
                          <includeScope>runtime</includeScope>
                      </configuration>
                  </execution>
              </executions>
          </plugin>
      </plugins>
  </build>
  ```

  - `${project.build.directory}/lib` 解析为项目中的 `target/lib`。
  - `<includeScope>runtime</includeScope>` 将复制限制为 `compile` 和 `runtime` 作用域的依赖，排除 `test` 和 `provided`。

- **命令行**：直接运行而不修改 `pom.xml`：

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib
  ```

##### **b. `tree`**
- **目的**：显示依赖树，显示所有直接和传递依赖及其版本。这对于识别版本冲突很有用。
- **命令行**：只需运行：

  ```bash
  mvn dependency:tree
  ```

  这将输出依赖的层次结构视图到控制台。
- **在 `pom.xml` 中配置**（可选）：如果要在构建阶段（例如 `verify`）运行它，可以类似于 `copy-dependencies` 进行配置。

##### **c. `analyze`**
- **目的**：分析依赖以识别问题，例如：
  - 使用但未声明的依赖。
  - 声明但未使用的依赖。
- **命令行**：运行：

  ```bash
  mvn dependency:analyze
  ```

  这将在控制台生成报告。
- **注意**：此目标可能需要对复杂项目进行额外配置以细化其分析。

##### **d. `list`**
- **目的**：列出项目的所有解析依赖。
- **命令行**：运行：

  ```bash
  mvn dependency:list
  ```

  这提供了一个依赖的扁平列表，适合快速参考。

##### **e. `unpack`**
- **目的**：将特定依赖（例如 JAR 文件）的内容提取到目录中。
- **命令行**：示例以解包特定的工件：

  ```bash
  mvn dependency:unpack -Dartifact=groupId:artifactId:version -DoutputDirectory=target/unpacked
  ```

  将 `groupId:artifactId:version` 替换为依赖的坐标（例如 `org.apache.commons:commons-lang3:3.12.0`）。

##### **f. `purge-local-repository`**
- **目的**：从本地 Maven 仓库（`~/.m2/repository`）中删除指定的依赖，强制从远程仓库重新下载。
- **命令行**：运行：

  ```bash
  mvn dependency:purge-local-repository
  ```

  这对于排除损坏的依赖文件很有帮助。

---

#### **4. 自定义选项**
许多目标支持配置参数以定制其行为：
- **`outputDirectory`**：指定复制或解包文件的位置（例如 `target/lib`）。
- **`includeScope` 或 `excludeScope`**：按作用域过滤依赖（例如 `runtime`、`test`）。
- **`artifact`**：针对特定依赖的目标（例如 `unpack`）。

这些可以在 `pom.xml` 的 `<configuration>` 部分设置，或者通过命令行参数 `-D` 传递（例如 `-DincludeScope=runtime`）。

---

#### **5. 实际示例**
- **场景 1：打包独立应用程序**
  使用 `copy-dependencies` 将所有运行时依赖收集到 `lib` 文件夹中：

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
  ```

- **场景 2：调试依赖冲突**
  运行 `dependency:tree` 检查传递依赖：

  ```bash
  mvn dependency:tree
  ```

  如果发现多个版本的库（例如 `commons-logging`），通过在 `pom.xml` 中添加 `<dependencyManagement>` 部分来解决冲突。

- **场景 3：提取资源**
  解包依赖以访问其内容：

  ```bash
  mvn dependency:unpack -Dartifact=org.example:my-lib:1.0.0 -DoutputDirectory=target/resources
  ```

---

#### **6. 总结**
要使用 Maven 依赖插件：
- 如果要将其集成到构建过程中，将其添加到 `pom.xml` 中，并配置特定目标和配置。
- 直接从命令行运行目标（例如 `copy-dependencies`、`tree`、`analyze`、`list` 或 `unpack`）以进行临时任务。
- 使用配置选项自定义行为以满足项目的需求。

此插件是一个管理依赖的多功能工具，超越了简单声明，使其在构建、调试和分发 Maven 项目方面非常有价值。