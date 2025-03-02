---
audio: true
generated: true
lang: hant
layout: post
title: Maven Surefire 插件
translated: true
---

以下是關於 **Maven Surefire Plugin** 的說明，這是 Maven 專案中用於在構建過程中運行單元測試的關鍵組件。這個說明涵蓋了其目的、配置、使用和自定義選項。

---

## 什麼是 Maven Surefire Plugin？

**Maven Surefire Plugin** 是 Apache Maven 中設計用來在構建生命週期中執行單元測試的插件。它與 Maven 的 `test` 阶段無縫集成，並在運行命令如 `mvn test`、`mvn package` 或 `mvn install` 時自動觸發。該插件支持流行的測試框架，如 JUnit（版本 3、4 和 5）和 TestNG，並生成測試報告，幫助開發人員評估測試結果。

### 主要功能
- 在單獨的 JVM 進程中運行測試以實現隔離。
- 支持多種測試框架（如 JUnit、TestNG 等）。
- 生成 XML 和純文本格式的測試報告。
- 提供靈活性以跳過測試、運行特定測試或自定義執行。

---

## 在 `pom.xml` 中的基本設置

Surefire 插件默認包含在 Maven 的構建生命週期中，因此您不需要為基本使用進行配置。然而，您可以在 `pom.xml` 文件中明確聲明它，以指定版本或自定義其行為。

### 最小配置
如果不添加任何配置，Maven 將使用插件的默認設置：
- 測試位於 `src/test/java`。
- 測試文件遵循命名模式，如 `**/*Test.java`、`**/Test*.java` 或 `**/*Tests.java`。

### 明確聲明
要自定義插件或確保特定版本，請將其添加到 `pom.xml` 的 `<build><plugins>` 部分。以下是一個示例：

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

## 使用 Surefire 運行測試

該插件與 Maven 生命週期的 `test` 阶段相關聯。以下是如何使用它：

### 運行所有測試
要執行所有單元測試，運行：

```
mvn test
```

### 在較大的構建中運行測試
在運行包含 `test` 阶段的命令時，測試會自動執行，例如：

```
mvn package
mvn install
```

### 跳過測試
您可以使用命令行標誌跳過測試執行：
- **跳過運行測試**：`-DskipTests`
  ```
  mvn package -DskipTests
  ```
- **跳過測試編譯和執行**：`-Dmaven.test.skip=true`
  ```
  mvn package -Dmaven.test.skip=true
  ```

---

## 自定義 Surefire 插件

您可以通過在 `pom.xml` 中添加 `<configuration>` 部分來自定義插件的行為。以下是一些常見的自定義：

### 包含或排除特定測試
使用模式指定要運行或跳過的測試：
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

### 並行運行測試
通過並行運行測試來加快執行速度：
```xml
<configuration>
    <parallel>methods</parallel>
    <threadCount>2</threadCount>
</configuration>
```
*注意*：在啟用此功能之前，請確保您的測試是線程安全的。

### 通過系統屬性
為測試 JVM 設置屬性：
```xml
<configuration>
    <systemPropertyVariables>
        <propertyName>propertyValue</propertyName>
    </systemPropertyVariables>
</configuration>
```

### 生成報告
默認情況下，報告保存在 `target/surefire-reports`。要生成 HTML 報告，請使用 `maven-surefire-report-plugin`：
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
運行 `mvn surefire-report:report` 以生成 HTML 報告。

---

## 處理測試失敗

### 測試失敗時失敗構建
默認情況下，失敗的測試會導致構建失敗。要忽略失敗並繼續：
```
mvn test -Dmaven.test.failure.ignore=true
```

### 重新運行失敗的測試
通過重試失敗來處理不穩定的測試：
```xml
<configuration>
    <rerunFailingTestsCount>2</rerunFailingTestsCount>
</configuration>
```
這將重新運行失敗的測試，最多 2 次。

---

## 使用 Surefire 與測試框架

該插件支持各種測試框架，並且需要最少的設置：

### JUnit 4
不需要額外配置；Surefire 會自動檢測 JUnit 4 測試。

### JUnit 5
添加 JUnit 5 依賴：
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
使用 Surefire 版本 2.22.0 或更高版本以獲得完整支持。

### TestNG
添加 TestNG 依賴：
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
Surefire 將自動運行 TestNG 測試。

---

## 關鍵說明

- **測試位置**：測試應位於 `src/test/java`，資源應位於 `src/test/resources`。
- **命名約定**：默認模式包括 `**/*Test.java`、`**/Test*.java` 等，但可以自定義。
- **插件版本**：使用較新的版本（例如 3.0.0-M5）以獲得最新的功能和框架支持。

---

## 摘要

**Maven Surefire Plugin** 是在 Maven 專案中運行單元測試的必不可少的插件。要使用它：
1. 依賴其默認行為，或者在 `pom.xml` 中明確聲明以進行自定義。
2. 使用 `mvn test` 或作為較大構建的一部分運行測試，例如 `mvn package`。
3. 使用選項（如包含/排除模式、並行執行或系統屬性）自定義它。
4. 通過跳過測試、忽略它們或重新運行不穩定的測試來處理失敗。
5. 確保與您的測試框架（JUnit、TestNG）兼容，方法是添加正確的依賴。

該插件提供了一種強大且靈活的方式來管理 Maven 專案中的單元測試！