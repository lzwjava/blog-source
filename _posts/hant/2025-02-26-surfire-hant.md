---
audio: false
generated: true
lang: hant
layout: post
title: Maven Surefire 插件
translated: true
type: note
---

以下是對 **Maven Surefire Plugin** 的說明，這是 Maven 專案中用於在建置過程中執行單元測試的關鍵元件。此說明涵蓋其用途、配置、使用方法及自訂選項。

---

## 什麼是 Maven Surefire Plugin？

**Maven Surefire Plugin** 是 Apache Maven 中的一個插件，旨在建置生命週期中執行單元測試。它與 Maven 的 `test` 階段無縫整合，並在執行如 `mvn test`、`mvn package` 或 `mvn install` 等指令時自動觸發。該插件支援流行的測試框架，如 JUnit（版本 3、4 和 5）及 TestNG，並生成測試報告以協助開發人員評估測試結果。

### 主要功能
- 在獨立的 JVM 進程中執行測試以實現隔離。
- 支援多種測試框架（JUnit、TestNG 等）。
- 生成 XML 及純文字等格式的測試報告。
- 提供跳過測試、執行特定測試或自訂執行的靈活性。

---

## 在 `pom.xml` 中的基本設定

Surefire Plugin 預設包含在 Maven 的建置生命週期中，因此基本使用無需配置。但您可以在 `pom.xml` 檔案中明確宣告它以指定版本或自訂其行為。

### 最小配置
若未添加任何配置，Maven 將使用插件的預設設定：
- 測試位於 `src/test/java`。
- 測試檔案遵循命名模式，如 `**/*Test.java`、`**/Test*.java` 或 `**/*Tests.java`。

### 明確宣告
若要自訂插件或確保使用特定版本，請將其添加到 `pom.xml` 的 `<build><plugins>` 區段。以下為範例：

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

## 使用 Surefire 執行測試

該插件與 Maven 生命週期的 `test` 階段綁定。使用方法如下：

### 執行所有測試
要執行所有單元測試，請執行：

```
mvn test
```

### 在大型建置中執行測試
當執行包含 `test` 階段的指令時，測試會自動執行，例如：

```
mvn package
mvn install
```

### 跳過測試
您可以使用指令行標記跳過測試執行：
- **跳過執行測試**：`-DskipTests`
  ```
  mvn package -DskipTests
  ```
- **跳過測試編譯及執行**：`-Dmaven.test.skip=true`
  ```
  mvn package -Dmaven.test.skip=true
  ```

---

## 自訂 Surefire Plugin

您可以透過在 `pom.xml` 中添加 `<configuration>` 區段來調整插件的行為。以下是一些常見的自訂項目：

### 包含或排除特定測試
使用模式指定要執行或跳過的測試：
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

### 並行執行測試
透過並行執行測試來加速執行：
```xml
<configuration>
    <parallel>methods</parallel>
    <threadCount>2</threadCount>
</configuration>
```
*注意*：啟用此功能前，請確保您的測試是執行緒安全的。

### 傳遞系統屬性
為測試 JVM 設定屬性：
```xml
<configuration>
    <systemPropertyVariables>
        <propertyName>propertyValue</propertyName>
    </systemPropertyVariables>
</configuration>
```

### 生成報告
預設情況下，報告會儲存在 `target/surefire-reports`。若要生成 HTML 報告，請使用 `maven-surefire-report-plugin`：
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
執行 `mvn surefire-report:report` 以生成 HTML 報告。

---

## 處理測試失敗

### 測試失敗時使建置失敗
預設情況下，測試失敗會導致建置失敗。若要忽略失敗並繼續：
```
mvn test -Dmaven.test.failure.ignore=true
```

### 重新執行失敗的測試
透過重試失敗來處理不穩定的測試：
```xml
<configuration>
    <rerunFailingTestsCount>2</rerunFailingTestsCount>
</configuration>
```
此設定會將失敗的測試重新執行最多 2 次。

---

## 與測試框架一起使用 Surefire

該插件支援多種測試框架，且設定簡單：

### JUnit 4
無需額外配置；Surefire 會自動偵測 JUnit 4 測試。

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
使用 Surefire 版本 2.22.0 或更高版本以獲得完整支援。

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
Surefire 會自動執行 TestNG 測試。

---

## 關鍵注意事項

- **測試位置**：測試應位於 `src/test/java`，資源則位於 `src/test/resources`。
- **命名慣例**：預設模式包括 `**/*Test.java`、`**/Test*.java` 等，但這些可以自訂。
- **插件版本**：使用最新版本（例如 3.0.0-M5）以獲得最新功能及框架支援。

---

## 總結

**Maven Surefire Plugin** 是在 Maven 專案中執行單元測試的必備工具。使用方法如下：
1. 依賴其預設行為，或在 `pom.xml` 中明確宣告以進行自訂。
2. 使用 `mvn test` 或作為大型建置（如 `mvn package`）的一部分來執行測試。
3. 使用包含/排除模式、並行執行或系統屬性等選項來自訂。
4. 透過跳過測試、忽略失敗或重新執行不穩定的測試來處理失敗。
5. 透過添加正確的依賴項確保與測試框架（JUnit、TestNG）的相容性。

此插件為您的 Maven 專案提供了強大且靈活的單元測試管理方式！