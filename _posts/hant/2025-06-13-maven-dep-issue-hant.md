---
audio: false
generated: true
lang: hant
layout: post
title: Maven 依賴問題
translated: true
type: note
---

### 問題概述

使用者在執行一個基於 Maven 的 Spring Boot 應用程式時遇到建置失敗。錯誤訊息顯示出現 `IllegalArgumentException`，原因為 `NoClassDefFoundError: org/springframework/beans/factory/aot/BeanRegistrationExcludeFilter`。這表明專案的依賴項存在版本不相容問題，導致應用程式無法正確啟動。提供的 `pom.xml` 檔案及 Maven 輸出內容為我們提供了診斷並解決此問題所需的背景資訊。

### 根本原因

此錯誤的發生，是因為 Spring Boot 應用程式無法實例化 `SharedMetadataReaderFactoryContextInitializer`——一個參與 Spring Boot 自動配置流程的類別。其根本原因在於缺少了 `BeanRegistrationExcludeFilter` 類別，該類別是 Spring Framework 6.0 及後續版本的一部分。此專案使用了 Spring Boot 3.4.2，其依賴於 Spring Framework 6.1.14。然而，`pom.xml` 中指定了較舊且不相容的 Spring Framework 依賴項版本，導致了類別路徑衝突。

在 `pom.xml` 中發現的關鍵問題如下：

1. **不相容的 Spring Boot Maven Plugin 版本：**
   - `spring-boot-maven-plugin` 設定為版本 `2.7.0`，該版本是為 Spring Boot 2.x 設計的，而非 Spring Boot 3.4.2（一個 3.x 版本）。此版本不符可能在建置及執行階段導致問題。

2. **明確宣告了不相容的 Spring Framework 依賴項：**
   - `pom.xml` 明確宣告了 `spring-aop` 和 `spring-aspects` 的版本為 `5.3.23`（Spring Framework 5.x），而 Spring Boot 3.4.2 需要 Spring Framework 6.1.14。Maven 會優先採用這些明確宣告的版本，而非 Spring Boot 所管理的版本，導致類別路徑上混合了 Spring Framework 5.x 和 6.x 的元件。這種混合情況造成了 `NoClassDefFoundError`，因為當載入了舊版的 5.x jar 檔時，`BeanRegistrationExcludeFilter`（來自 Spring Framework 6.x）便無法使用。

### 解決方案

為解決此問題，我們需要確保專案的所有元件均與 Spring Boot 3.4.2 相容，並且讓 Spring Boot 管理其依賴項的版本以避免衝突。應對 `pom.xml` 進行以下修改：

1. **更新 Spring Boot Maven Plugin 版本：**
   - 將 `spring-boot-maven-plugin` 的版本從 `2.7.0` 更改為 `3.4.2`，以與專案中使用的 Spring Boot 版本保持一致。

2. **移除明確宣告的 Spring Framework 依賴項：**
   - 移除明確宣告的 `spring-aop` 和 `spring-aspects`（版本 `5.3.23`）。Spring Boot 3.4.2 透過其 starter（例如 `spring-boot-starter-web` 包含了正確版本 6.1.14 的 `spring-aop`）來管理這些依賴項。移除這些宣告可防止 Maven 覆寫 Spring Boot 的依賴項管理。

### 更新後的 `pom.xml`

以下是修正後的 `pom.xml` 檔案，其中應用了必要的更改：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.lzwjava</groupId>
    <artifactId>blog-server</artifactId>
    <version>1.0</version>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <version>3.4.2</version>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-engine</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <version>5.3.1</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <version>3.4.2</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjrt</artifactId>
            <version>1.9.22</version>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjweaver</artifactId>
            <version>1.9.22</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>3.4.2</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0-M8</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-checkstyle-plugin</artifactId>
                <version>3.1.1</version>
                <configuration>
                    <configLocation>google_checks.xml</configLocation>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>check</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### 更改說明

- **Spring Boot Maven Plugin 更新：**
  - 在 `spring-boot-maven-plugin` 配置中，將 `<version>2.7.0</version>` 更改為 `<version>3.4.2</version>`。這確保了該外掛與 Spring Boot 3.4.2 相容，並支援 3.x 系列特有的功能與配置。

- **移除 `spring-aop` 和 `spring-aspects`：**
  - 移除了以下依賴項：
    ```xml
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-aop</artifactId>
        <version>5.3.23</version>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-aspects</artifactId>
        <version>5.3.23</version>
    </dependency>
    ```
  - `spring-aop` 已包含在 `spring-boot-starter-web` 中（透過 `spring-web`），且 Spring Boot 將其版本管理為 6.1.14，該版本與 3.4.2 相容。
  - `spring-aspects` 並非 Spring Boot starter 中的標準依賴項。如果專案明確需要它（例如用於自訂切面），可以重新加入但不指定版本（讓 Spring Boot 的依賴項管理來處理），或將其版本設定為 `6.1.14`。然而，由於錯誤發生在啟動階段且與自動配置相關，而非缺少切面功能，因此很可能在此處並非必要，可以安全地移除。

### 補充說明

- **AspectJ 依賴項：**
  - `aspectjrt` 和 `aspectjweaver` 依賴項（版本 1.9.22）保留在 `pom.xml` 中，因為它們與 Spring Framework 6.1.14 相容，並且如果專案使用 AspectJ 功能則可能需要。這些依賴項不會與 Spring Boot 3.4.2 衝突。

- **最佳實踐：**
  - 對於 Spring Boot 專案，建議使用 `spring-boot-starter-parent` 作為父 POM，或匯入 `spring-boot-dependencies` BOM 以自動管理依賴項版本。當前的 `pom.xml` 並未採用這兩種方式，但由於在移除明確的覆寫後，`spring-boot-starter-web` 及其他 starter 仍能強制執行版本一致性，因此此解決方案無需進行此變更也能運作。

- **驗證：**
  - 套用這些更改後，執行 `mvn clean spring-boot:run` 以驗證應用程式能否在無錯誤的情況下啟動。如果專案依賴 `spring-aspects`（例如用於特定的 AOP 功能），且移除它導致問題，請將其重新加入並指定 `<version>6.1.14</version>`，或省略版本並確保依賴項管理正確。

### 結論

透過將 `spring-boot-maven-plugin` 更新至版本 3.4.2，並移除明確宣告的 `spring-aop` 和 `spring-aspects` 依賴項，專案將使用一致的 Spring Boot (3.4.2) 和 Spring Framework (6.1.14) 版本。這解決了導致 `NoClassDefFoundError` 的類別路徑衝突問題，使應用程式能夠成功啟動。