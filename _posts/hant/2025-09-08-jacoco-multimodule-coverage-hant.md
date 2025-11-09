---
audio: false
date: 2025-09-08
generated: true
image: false
lang: hant
layout: post
title: JaCoCo 多模組覆蓋率報告策略
translated: true
type: note
---

當然。您的分析非常準確，特別是關於 JaCoCo 與外部整合測試的複雜性。執行兩次建構確實不是理想的作法。

您正在尋找的策略是將測試執行集中化，然後匯總結果。您已經非常接近了，`aggregate` 目標確實是正確的工具，但需要針對此情境以特定方式應用。

以下是推薦的策略：**在您的 Web 應用程式模組中產生一個覆蓋率檔案 (`.exec`)，然後使用一個獨立的、專用的報告模組來為所有相關模組建立單一的匯總報告。**

這種方法簡潔、可擴展，並且避免了重複建構。

-----

## 核心概念

當您的 `PlaygroundWeb` 應用程式在 Jetty 上運行並啟用 JaCoCo 代理時，該代理會檢測**應用程式類別載入器載入的所有類別**。這包括 `PlaygroundWeb` 本身的類別*以及*其所有依賴項，例如 `PlaygroundUtils.jar`。

因此，在 `PlaygroundWeb` 建構期間產生的單一 `jacoco-it.exec` 檔案已經包含了**兩個模組**的覆蓋率數據。挑戰在於如何讓 JaCoCo 報告工具指向它所需的所有模組的原始碼，以建立最終的 HTML 報告。

-----

## 一個可擴展的四步驟策略

以下是逐步指南，用於重構您的專案以實現簡潔的匯總覆蓋率報告。

### 步驟 1：建立一個專用的報告模組

首先，建立一個專門用於匯總的新模組。這是 Maven 的最佳實踐，可以保持職責分離。

1.  在您的根 `pom.xml` (`PlaygroundLib`) 中，新增模組：
    ```xml
    <modules>
        <module>PlaygroundUtils</module>
        <module>PlaygroundWeb</module>
        <module>PlaygroundReports</module> </modules>
    ```
2.  在根目錄建立一個新目錄 `PlaygroundReports`，並包含其自己的 `pom.xml`。

您的新專案結構將如下所示：

```
.
├── PlaygroundReports
│   └── pom.xml
├── PlaygroundUtils
│   └── pom.xml
├── PlaygroundWeb
│   └── pom.xml
└── pom.xml
```

### 步驟 2：配置報告模組的 `pom.xml`

這個新的 `pom.xml` 是實現功能的關鍵。它將依賴於您想要包含在報告中的所有模組，並執行 `report-aggregate` 目標。

**`PlaygroundReports/pom.xml`:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.lzw</groupId>
        <artifactId>PlaygroundLib</artifactId>
        <version>1.0</version>
    </parent>
    <artifactId>PlaygroundReports</artifactId>
    <packaging>pom</packaging>
    <name>PlaygroundReports</name>

    <dependencies>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundWeb</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundUtils</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <executions>
                    <execution>
                        <id>aggregate-report</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>report-aggregate</goal>
                        </goals>
                        <configuration>
                            <dataFiles>
                                <dataFile>${project.basedir}/../PlaygroundWeb/target/jacoco-it.exec</dataFile>
                            </dataFiles>
                            <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### 步驟 3：簡化 `PlaygroundWeb` 模組

您的 `PlaygroundWeb` 模組現在只負責**產生覆蓋率數據**，而不是為其生成報告。您可以從其 `pom.xml` 中移除 `jacoco:report` 的執行。

**`PlaygroundWeb/pom.xml` (僅顯示變更部分):**

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>prepare-agent</id>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
            <configuration>
                <propertyName>jacoco.it.agent</propertyName>
                <destFile>${project.build.directory}/jacoco-it.exec</destFile>
            </configuration>
        </execution>
        </executions>
</plugin>

<plugin>
    <groupId>org.eclipse.jetty</groupId>
    <artifactId>jetty-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>start-jetty</id>
            <phase>pre-integration-test</phase>
            <goals>
                <goal>start</goal>
            </goals>
            <configuration>
                <daemon>true</daemon>
                <jvmArgs>
                    ${jacoco.it.agent}
                </jvmArgs>
                </configuration>
        </execution>
        </executions>
</plugin>
```

*注意*：我稍微修改了 `prepare-agent` 的配置，使用一個屬性 (`jacoco.it.agent`)，然後在 `jetty-maven-plugin` 中引用該屬性。這是傳遞代理字串的一種穩健方法。您之前在 `pom.xml` 中的配置也是可以的，但這樣寫意圖更清晰。

### 步驟 4：清理 `PlaygroundUtils`

`PlaygroundUtils` 模組不需要為整合測試配置任何 JaCoCo 外掛。它的程式碼是透過 `PlaygroundWeb` 被覆蓋的，而報告則由 `PlaygroundReports` 處理。您可以從其 `pom.xml` 中移除任何與 JaCoCo 相關的屬性或外掛。

-----

## 這個方法如何解決問題

1.  **單次建構：** 您只需從根目錄執行一次 `mvn clean verify`。
2.  **正確的生命週期：**
      * Maven 建構 `PlaygroundUtils`。
      * Maven 建構 `PlaygroundWeb`，啟動帶有 JaCoCo 代理的 Jetty，執行您的 Python 測試（這些測試會觸及兩個模組中的程式碼），停止 Jetty，並產生 `PlaygroundWeb/target/jacoco-it.exec`。
      * Maven 建構 `PlaygroundReports`。在 `verify` 階段，`report-aggregate` 目標會執行。它從 `PlaygroundWeb` 找到 `.exec` 檔案，並且由於依賴關係，它知道去哪裡尋找 `PlaygroundWeb` 和 `PlaygroundUtils` 的原始碼。
      * 它會產生一個**單一的、統一的 HTML 報告**，其中包含兩個模組的覆蓋率。
3.  **可擴展性：** 如果您新增了十個以上的函式庫模組，只需將它們作為依賴項新增到 `PlaygroundReports/pom.xml` 中。核心邏輯保持不變。這正是您正在尋找的簡潔、可擴展的解決方案。