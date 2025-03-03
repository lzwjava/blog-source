---
audio: false
generated: true
lang: hant
layout: post
title: 建構助手 Maven 插件
translated: true
---

`builder-helper-maven-plugin`，現稱為 **Build Helper Maven Plugin**，是一個多功能的工具，旨在協助各種 Maven 建置生命週期中的任務。最初在 Codehaus 托管，現由 MojoHaus 維護，儘管其 Maven 坐標仍使用 `org.codehaus.mojo` 群組 ID。此插件提供一組目標，以幫助執行添加額外的源目錄、附加額外的工件、解析版本信息等操作。以下，我將指導您如何在 Maven 專案中使用此插件。

### 什麼是 Maven？
在深入探討插件之前，讓我們先設定上下文。Maven 是一個廣泛使用的建置自動化工具，主要用於 Java 專案。它通過管理依賴、編譯代碼、打包應用程序等，簡化和標準化建置過程，所有這些都通過一個名為 `pom.xml` 的中央文件進行配置。

### 第 1 步：在 `pom.xml` 中包含插件
要使用 Build Helper Maven Plugin，您需要在 Maven 專案的 `pom.xml` 文件中的 `<build><plugins>` 部分添加它。以下是如何做到的：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <!-- 將為特定目標添加執行 -->
        </plugin>
    </plugins>
</build>
```

- **群組 ID**：`org.codehaus.mojo`（反映其起源，儘管它現在屬於 MojoHaus）。
- **工件 ID**：`build-helper-maven-plugin`。
- **版本**：截至我最後一次更新，`3.6.0` 是最新版本，但您應該檢查 [Maven Central](https://mvnrepository.com/artifact/org.codehaus.mojo/build-helper-maven-plugin) 以獲取最新版本。

此聲明使插件在您的專案中可用，但直到您配置特定目標之前，它什麼也做不了。

### 第 2 步：配置特定目標的執行
Build Helper Maven Plugin 提供多個目標，每個目標都針對特定任務設計。您可以通過在插件聲明內添加 `<executions>` 塊來配置這些目標，指定它們應該在哪個 Maven 生命週期階段運行以及它們應該如何運行。

以下是一些常用目標及其用途：

- **`add-source`**：向專案添加額外的源目錄。
- **`add-test-source`**：添加額外的測試源目錄。
- **`add-resource`**：添加額外的資源目錄。
- **`attach-artifact`**：將額外的工件（例如文件）附加到專案以進行安裝和部署。
- **`parse-version`**：解析專案的版本並設置屬性（例如主要、次要、增量版本）。

每個目標都需要自己的配置，您可以在 `<execution>` 塊內定義它。

### 第 3 步：範例 – 添加額外的源目錄
此插件的常見用例之一是添加額外的源目錄，因為 Maven 通常只支持一個（`src/main/java`）。以下是如何配置 `add-source` 目標以包含額外的源目錄：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <executions>
                <execution>
                    <id>add-source</id>
                    <phase>generate-sources</phase>
                    <goals>
                        <goal>add-source</goal>
                    </goals>
                    <configuration>
                        <sources>
                            <source>path/to/your/extra/source/directory</source>
                        </sources>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`<id>`**：此執行的唯一標識符（例如 `add-source`）。
- **`<phase>`**：目標運行的 Maven 生命週期階段（例如 `generate-sources` 確保目錄在建置過程中早期添加）。
- **`<goals>`**：指定要執行的目標（在此情況下為 `add-source`）。
- **`<configuration>`**：定義額外的源目錄（用您的實際路徑替換 `path/to/your/extra/source/directory`，例如 `src/main/generated`）。

當您運行類似 `mvn compile` 的 Maven 命令時，Maven 將包括此額外目錄作為源文件夾。

### 額外說明
- **版本兼容性**：自 3.0.0 版本起，插件需要 Maven 3 或更高版本。如果您使用的是較舊的 Maven 版本，則需要使用 1.12 或更早的插件版本。
- **多個目標**：您可以在同一插件中定義多個 `<execution>` 塊以運行不同的目標。例如，您可以通過包含 `add-source` 和 `add-test-source` 的執行來添加源和測試源目錄。
- **運行插件**：配置好後，運行 Maven 命令（例如 `mvn clean install`）將在指定的階段觸發插件的目標。

### 更多資源
有關其他目標的更多詳細信息和範例，請參閱 [官方使用頁面](https://www.mojohaus.org/build-helper-maven-plugin/usage.html)。該頁面提供了所有可用目標的全面文檔和範例配置。

### 最後的想法
Build Helper Maven Plugin 是您 Maven 工具包的強大補充，特別是對於需要非標準建置配置的專案。通過在 `pom.xml` 中包含它並配置適當的目標，您可以根據具體需求定制建置過程。儘管它起源於 Codehaus，但其當前的家園是 MojoHaus，並且它仍然是增強 Maven 建置的可靠選擇。