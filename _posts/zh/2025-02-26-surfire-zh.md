---
audio: true
generated: false
lang: zh
layout: post
title: Maven Surefire 插件
translated: true
---

以下是关于 **Maven Surefire 插件** 的解释，它是 Maven 项目中用于在构建过程中运行单元测试的关键组件。本解释涵盖了其目的、配置、使用和自定义选项。

---

## 什么是 Maven Surefire 插件？

**Maven Surefire 插件** 是 Apache Maven 中设计用于在构建生命周期中执行单元测试的插件。它与 Maven 的 `test` 阶段无缝集成，并在运行命令如 `mvn test`、`mvn package` 或 `mvn install` 时自动触发。该插件支持流行的测试框架，如 JUnit（版本 3、4 和 5）和 TestNG，并生成测试报告以帮助开发人员评估测试结果。

### 主要特性
- 在单独的 JVM 进程中运行测试以实现隔离。
- 支持多种测试框架（JUnit、TestNG 等）。
- 生成 XML 和纯文本格式的测试报告。
- 提供灵活性以跳过测试、运行特定测试或自定义执行。

---

## 在 `pom.xml` 中的基本设置

Surefire 插件默认包含在 Maven 的构建生命周期中，因此不需要为基本使用进行配置。但是，您可以在 `pom.xml` 文件中显式声明它以指定版本或自定义其行为。

### 最小配置
如果不添加任何配置，Maven 将使用插件的默认设置：
- 测试位于 `src/test/java`。
- 测试文件遵循命名模式，如 `**/*Test.java`、`**/Test*.java` 或 `**/*Tests.java`。

### 显式声明
要自定义插件或确保特定版本，请将其添加到 `pom.xml` 的 `<build><plugins>` 部分。以下是一个示例：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M5</version> <!-- 使用最新版本 -->
        </plugin>
    </plugins>
</build>
```

---

## 使用 Surefire 运行测试

该插件与 Maven 生命周期的 `test` 阶段绑定。以下是如何使用它的方法：

### 运行所有测试
要执行所有单元测试，运行：

```
mvn test
```

### 在较大的构建中运行测试
在运行包括 `test` 阶段的命令时，测试会自动执行，例如：

```
mvn package
mvn install
```

### 跳过测试
可以使用命令行标志跳过测试执行：
- **跳过运行测试**：`-DskipTests`
  ```
  mvn package -DskipTests
  ```
- **跳过测试编译和执行**：`-Dmaven.test.skip=true`
  ```
  mvn package -Dmaven.test.skip=true
  ```

---

## 自定义 Surefire 插件

可以通过在 `pom.xml` 中添加 `<configuration>` 部分来定制插件的行为。以下是一些常见的自定义：

### 包含或排除特定测试
使用模式指定要运行或跳过的测试：
```xml
<configuration>
    <includes>
        <include>**/My*Test.java</include>
    </includes>
    <excludes>
        <exclude>**/SlowTest.java</exclude>
    </excludes>
</configuration>
```

### 并行运行测试
通过并发运行测试来加快执行速度：
```xml
<configuration>
    <parallel>methods</parallel>
    <threadCount>2</threadCount>
</configuration>
```
*注意*：在启用此功能之前，请确保您的测试是线程安全的。

### 传递系统属性
为测试 JVM 设置属性：
```xml
<configuration>
    <systemPropertyVariables>
        <propertyName>propertyValue</propertyName>
    </systemPropertyVariables>
</configuration>
```

### 生成报告
默认情况下，报告保存在 `target/surefire-reports`。要生成 HTML 报告，请使用 `maven-surefire-report-plugin`：
```xml
<reporting>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-report-plugin</artifactId>
            <version>3.0.0-M5</version>
        </plugin>
    </plugins>
</reporting>
```
运行 `mvn surefire-report:report` 以生成 HTML 报告。

---

## 处理测试失败

### 测试失败时失败构建
默认情况下，失败的测试会导致构建失败。要忽略失败并继续：
```
mvn test -Dmaven.test.failure.ignore=true
```

### 重新运行失败的测试
通过重试失败来处理不稳定的测试：
```xml
<configuration>
    <rerunFailingTestsCount>2</rerunFailingTestsCount>
</configuration>
```
这将重新运行失败的测试，最多 2 次。

---

## 使用 Surefire 与测试框架

该插件支持各种测试框架，几乎不需要额外的设置：

### JUnit 4
不需要额外配置；Surefire 会自动检测 JUnit 4 测试。

### JUnit 5
添加 JUnit 5 依赖：
```xml
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.8.1</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
使用 Surefire 版本 2.22.0 或更高版本以获得完整支持。

### TestNG
添加 TestNG 依赖：
```xml
<dependencies>
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <version>7.4.0</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
Surefire 将自动运行 TestNG 测试。

---

## 关键说明

- **测试位置**：测试应位于 `src/test/java`，资源应位于 `src/test/resources`。
- **命名约定**：默认模式包括 `**/*Test.java`、`**/Test*.java` 等，但可以自定义。
- **插件版本**：使用较新版本（例如 3.0.0-M5）以获得最新功能和框架支持。

---

## 总结

**Maven Surefire 插件** 是在 Maven 项目中运行单元测试的重要工具。要使用它：
1. 依赖其默认行为，或者在 `pom.xml` 中显式声明以进行自定义。
2. 使用 `mvn test` 或作为较大构建的一部分运行测试，如 `mvn package`。
3. 使用选项（如包含/排除模式、并行执行或系统属性）进行自定义。
4. 通过跳过测试、忽略它们或重新运行不稳定的测试来处理失败。
5. 确保与您的测试框架（JUnit、TestNG）兼容，方法是添加正确的依赖项。

该插件为管理 Maven 项目中的单元测试提供了强大且灵活的方法！