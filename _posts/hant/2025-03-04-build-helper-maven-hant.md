---
audio: false
generated: true
lang: hant
layout: post
title: 建構助手 Maven 插件
translated: true
type: note
---

`builder-helper-maven-plugin`，現稱為 **Build Helper Maven Plugin**，是一款多功能工具，旨在協助處理 Maven 建置生命週期中的各種任務。該插件最初由 Codehaus 託管，現由 MojoHaus 維護，但其 Maven 座標仍使用 `org.codehaus.mojo` 群組 ID。此插件提供一系列目標（goals），可協助執行添加額外原始碼目錄、附加額外成品、解析版本資訊等操作。以下將引導您如何在 Maven 專案中使用此插件。

### 什麼是 Maven？
在深入探討插件之前，先建立背景知識。Maven 是廣泛使用的建置自動化工具，主要針對 Java 專案。它透過中央設定檔 `pom.xml` 來管理依賴項、編譯程式碼、打包應用程式等，從而簡化並標準化建置流程。

### 步驟 1：在 `pom.xml` 中包含插件
要使用 Build Helper Maven Plugin，您需要將其添加到 Maven 專案的 `pom.xml` 檔案中的 `<build><plugins>` 區塊。具體操作如下：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <!-- 特定目標的執行配置將在此處添加 -->
        </plugin>
    </plugins>
</build>
```

- **Group ID**：`org.codehaus.mojo`（反映其起源，即使現由 MojoHaus 維護）。
- **Artifact ID**：`build-helper-maven-plugin`。
- **Version**：根據最新更新，`3.6.0` 是最新版本，但您應檢查 [Maven Central](https://mvnrepository.com/artifact/org.codehaus.mojo/build-helper-maven-plugin) 以獲取最新發布版本。

此聲明使插件在您的專案中可用，但在配置特定目標之前，它不會執行任何操作。

### 步驟 2：配置特定目標的執行
Build Helper Maven Plugin 提供多個目標，每個目標針對特定任務設計。您需在插件聲明中添加 `<executions>` 區塊來配置這些目標，指定它們應在何時運行（透過 Maven 生命週期階段）以及其行為方式。

以下是一些常用目標及其用途：

- **`add-source`**：為專案添加額外原始碼目錄。
- **`add-test-source`**：添加額外測試原始碼目錄。
- **`add-resource`**：添加額外資源目錄。
- **`attach-artifact`**：附加額外成品（例如檔案）到專案，以便安裝和部署。
- **`parse-version`**：解析專案版本並設定屬性（例如主版本、次版本、增量版本）。

每個目標都需要在 `<execution>` 區塊內定義其專屬配置。

### 步驟 3：範例 – 添加額外原始碼目錄
此插件的常見用途是添加額外原始碼目錄，因為 Maven 預設僅支援一個目錄（`src/main/java`）。以下是配置 `add-source` 目標以包含額外原始碼目錄的方法：

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

- **`<id>`**：此執行的唯一識別碼（例如 `add-source`）。
- **`<phase>`**：目標運行的 Maven 生命週期階段（例如 `generate-sources` 確保目錄在建置早期被添加）。
- **`<goals>`**：指定要執行的目標（此處為 `add-source`）。
- **`<configuration>`**：定義額外原始碼目錄（將 `path/to/your/extra/source/directory` 替換為實際路徑，例如 `src/main/generated`）。

當您執行如 `mvn compile` 的 Maven 指令時，Maven 會將此額外目錄視為原始碼資料夾。

### 補充說明
- **版本相容性**：自 3.0.0 版起，此插件需要 Maven 3 或更高版本。若您使用舊版 Maven，則需使用 1.12 或更早的插件版本。
- **多目標配置**：您可以在同一插件中定義多個 `<execution>` 區塊以執行不同目標。例如，透過為 `add-source` 和 `add-test-source` 添加執行配置，可同時添加原始碼和測試原始碼目錄。
- **執行插件**：配置完成後，執行 Maven 指令（例如 `mvn clean install`）將在指定階段觸發插件的目標。

### 進一步資源
如需更多詳細資訊和其他目標的範例，請查閱 [官方使用頁面](https://www.mojohaus.org/build-helper-maven-plugin/usage.html)。該頁面提供完整文件及所有可用目標的範例配置。

### 結語
Build Helper Maven Plugin 是 Maven 工具組中的強大補充，尤其適用於需要非標準建置配置的專案。透過將其包含在 `pom.xml` 中並配置適當目標，您可以根據特定需求調整建置流程。儘管它起源於 Codehaus，但現由 MojoHaus 維護，並持續是增強 Maven 建置的可靠選擇。