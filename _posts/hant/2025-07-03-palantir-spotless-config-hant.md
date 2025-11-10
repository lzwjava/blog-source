---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Spotless 配置 Palantir Java 格式
translated: true
type: note
---

要在 `pom.xml` 檔案中配置 **Palantir Java Format** 與 **Spotless Maven Plugin**，您需要設定插件使用 `palantirJavaFormat` 並指定格式化選項，例如 tabspace、縮排、匯入順序和其他設定。以下是關於如何配置這些設定及可用選項的詳細指南，基於 Spotless 插件和 Palantir Java Format。

### 新增 Spotless Maven Plugin 與 Palantir Java Format

在您的 `pom.xml` 中包含 Spotless Maven Plugin 並配置其使用 `palantirJavaFormat`。以下是一個基本設定，包含 tabspace、縮排、匯入順序和其他選項的常見配置：

```xml
<plugin>
    <groupId>com.diffplug.spotless</groupId>
    <artifactId>spotless-maven-plugin</artifactId>
    <version>2.43.0</version> <!-- 使用最新版本 -->
    <configuration>
        <java>
            <!-- 指定要格式化的檔案（可選，預設為所有 .java 檔案） -->
            <includes>
                <include>src/main/java/**/*.java</include>
                <include>src/test/java/**/*.java</include>
            </includes>
            <!-- Palantir Java Format -->
            <palantirJavaFormat>
                <version>2.53.0</version> <!-- 指定所需版本 -->
                <style>GOOGLE</style> <!-- 選項：GOOGLE、AOSP 或 PALANTIR -->
                <formatJavadoc>true</formatJavadoc> <!-- 可選：格式化 Javadoc -->
            </palantirJavaFormat>
            <!-- 縮排設定 -->
            <indent>
                <tabs>true</tabs> <!-- 使用 tab 而非空格 -->
                <spacesPerTab>4</spacesPerTab> <!-- 每個 tab 的空格數 -->
            </indent>
            <!-- 匯入順序配置 -->
            <importOrder>
                <order>java,javax,org,com,\\#</order> <!-- 自訂匯入順序 -->
            </importOrder>
            <!-- 移除未使用的匯入 -->
            <removeUnusedImports/>
            <!-- 其他可選設定 -->
            <trimTrailingWhitespace/>
            <endWithNewline/>
            <toggleOffOn/> <!-- 啟用 spotless:off 和 spotless:on 標籤 -->
        </java>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>apply</goal> <!-- 自動格式化程式碼 -->
            </goals>
            <phase>validate</phase> <!-- 在 validate 階段執行 -->
        </execution>
    </executions>
</plugin>
```

### 配置選項說明

以下是 Spotless 中 `java` 區段與 `palantirJavaFormat` 的關鍵配置選項細目，重點關注 tabspace、縮排、匯入順序和其他相關設定：

#### 1. **Palantir Java Format (`<palantirJavaFormat>`)**

- **`<version>`**：指定要使用的 `palantir-java-format` 版本。請在 [Maven Repository](https://mvnrepository.com/artifact/com.palantir.java-format/palantir-java-format) 或 [GitHub](https://github.com/palantir/palantir-java-format/releases) 上檢查最新版本。範例：`<version>2.53.0</version>`。
- **`<style>`**：定義格式化樣式。選項為：
  - `GOOGLE`：使用 Google Java 樣式（2 空格縮排，100 字元行限制）。
  - `AOSP`：使用 Android Open Source Project 樣式（4 空格縮排，100 字元行限制）。
  - `PALANTIR`：使用 Palantir 樣式（4 空格縮排，120 字元行限制，lambda-friendly 格式化）。[](https://github.com/palantir/palantir-java-format)
- **`<formatJavadoc>`**：布林值，用於啟用/停用 Javadoc 格式化（需要 Palantir Java Format 版本 ≥ 2.39.0）。範例：`<formatJavadoc>true</formatJavadoc>`。[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)
- **自訂 Group Artifact**：很少需要，但您可以為格式化工具指定自訂的 group 和 artifact。範例：`<groupArtifact>com.palantir.java-format:palantir-java-format</groupArtifact>`。

#### 2. **縮排 (`<indent>`)**

- **`<tabs>`**：布林值，使用 tab (`true`) 或空格 (`false`) 進行縮排。範例：`<tabs>true</tabs>`。[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<spacesPerTab>`**：每個 tab 的空格數（當 `<tabs>` 為 `false` 時使用，或用於混合縮排）。常見值為 `2` 或 `4`。範例：`<spacesPerTab>4</spacesPerTab>`。[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
  - **注意**：Palantir Java Format 的樣式（例如 `GOOGLE`、`AOSP`、`PALANTIR`）可能會影響縮排行為。例如，`GOOGLE` 預設為 2 空格，而 `AOSP` 和 `PALANTIR` 使用 4 空格。Spotless 中的 `<indent>` 設定可以覆寫或補充這些預設值，但請確保一致性以避免衝突。[](https://stackoverflow.com/questions/50027892/override-google-java-format-with-spotless-maven-plugin)

#### 3. **匯入順序 (`<importOrder>`)**

- **`<order>`**：指定匯入群組的順序，以逗號分隔。使用 `\\#` 表示靜態匯入，使用空字串 (`""`) 表示未指定的匯入。範例：`<order>java,javax,org,com,\\#</order>` 會先排序以 `java` 開頭的匯入，然後是 `javax` 等，最後是靜態匯入。[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)
- **`<file>`**：或者，指定一個包含匯入順序的檔案。範例：`<file>${project.basedir}/eclipse.importorder</file>`。檔案格式符合 Eclipse 的匯入順序配置（例如 `java|javax|org|com|\\#`）。[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)
  - 範例檔案內容：
    ```
    #sort
    java
    javax
    org
    com
    \#
    ```

#### 4. **其他實用設定**

- **`<removeUnusedImports>`**：移除未使用的匯入。可選擇指定引擎：
  - 預設：使用 `google-java-format` 進行移除。
  - 替代方案：`<engine>cleanthat-javaparser-unnecessaryimport</engine>` 用於 JDK8+ 相容性與較新的 Java 功能（例如 Java 17）。[](https://stackoverflow.com/questions/77126927/spotless-eclipse-formatter-java-17-error-on-string-literals-removing-unu)
- **`<trimTrailingWhitespace>`**：移除行尾的空白字元。範例：`<trimTrailingWhitespace/>`。[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<endWithNewline>`**：確保檔案以換行結尾。範例：`<endWithNewline/>`。[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<toggleOffOn>`**：啟用 `// spotless:off` 和 `// spotless:on` 註解，以排除程式碼區段不進行格式化。範例：`<toggleOffOn/>`。[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<licenseHeader>`**：在檔案中加入授權標頭。範例：
  ```xml
  <licenseHeader>
      <content>/* (C) $YEAR */</content>
  </licenseHeader>
  ```
  您也可以使用檔案：`<file>${project.basedir}/license.txt</file>`。[](https://www.baeldung.com/java-maven-spotless-plugin)
- **`<formatAnnotations>`**：確保型別註解與其描述的欄位位於同一行。範例：`<formatAnnotations/>`。[](https://www.baeldung.com/java-maven-spotless-plugin)
- **`<ratchetFrom>`**：將格式化限制在相對於 Git 分支（例如 `origin/main`）已變更的檔案。範例：`<ratchetFrom>origin/main</ratchetFrom>`。[](https://github.com/diffplug/spotless/blob/main/plugin-maven/README.md)

#### 5. **POM 特定格式化 (`<pom>`)**

要格式化 `pom.xml` 檔案本身，請使用 `<pom>` 區段與 `sortPom`：
```xml
<pom>
    <sortPom>
        <nrOfIndentSpace>2</nrOfIndentSpace> <!-- POM 的縮排 -->
        <predefinedSortOrder>recommended_2008_06</predefinedSortOrder> <!-- 標準 POM 順序 -->
        <sortDependencies>groupId,artifactId</sortDependencies> <!-- 排序 dependencies -->
        <sortPlugins>groupId,artifactId</sortPlugins> <!-- 排序 plugins -->
        <endWithNewline>true</endWithNewline>
    </sortPom>
</pom>
```
- **`sortPom` 的選項**：
  - `<nrOfIndentSpace>`：縮排的空格數（例如 `2` 或 `4`）。
  - `<predefinedSortOrder>`：用於元素順序的選項，例如 `recommended_2008_06` 或 `custom_1`。[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)
  - `<sortDependencies>`：按 `groupId`、`artifactId` 或其他條件排序。
  - `<sortPlugins>`：類似地排序 plugins。
  - `<endWithNewline>`：確保 POM 以換行結尾。
  - `<expandEmptyElements>`：展開空的 XML 標籤（例如 `<tag></tag>` 與 `<tag/>`）。[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)

### 執行 Spotless

- **檢查格式化**：`mvn spotless:check` – 根據配置的規則驗證程式碼，如果發現違規則使建置失敗。
- **套用格式化**：`mvn spotless:apply` – 自動格式化程式碼以符合規則。

### 注意事項與最佳實踐

- **與 IDE 的一致性**：要讓 IntelliJ 或 Eclipse 與 Spotless 對齊，請安裝 `palantir-java-format` IntelliJ 插件或使用 Eclipse formatter XML 檔案。對於 IntelliJ，匯入相容的樣式檔案（例如，Google 樣式的 `intellij-java-google-style.xml`）或手動配置以符合 Palantir 設定。[](https://plugins.jetbrains.com/plugin/13180-palantir-java-format)
- **版本相容性**：確保 `palantir-java-format` 版本支援您的 Java 版本。對於 Java 17+，請使用較新的版本（例如 2.53.0）。某些功能（如模式匹配）可能支援有限。[](https://www.reddit.com/r/java/comments/1g8zu8c/codestyle_and_formatters/)
- **自訂格式化**：對於進階自訂，請使用 Eclipse formatter XML 檔案搭配 `<eclipse>` 而非 `<palantirJavaFormat>`：
  ```xml
  <eclipse>
      <file>${project.basedir}/custom-style.xml</file>
  </eclipse>
  ```
  範例 `custom-style.xml`：
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <profiles version="21">
      <profile kind="CodeFormatterProfile" name="custom" version="21">
          <setting id="org.eclipse.jdt.core.formatter.tabulation.char" value="space"/>
          <setting id="org.eclipse.jdt.core.formatter.indentation.size" value="4"/>
          <setting id="org.eclipse.jdt.core.formatter.tabulation.size" value="4"/>
      </profile>
  </profiles>
  ```
  [](https://www.baeldung.com/java-maven-spotless-plugin)
- **限制**：Palantir Java Format 的可配置性不如 Eclipse 的格式化工具，但旨在實現一致性和現代 Java 功能（例如 lambda）。它可能無法處理所有邊緣情況（例如深度巢狀的 lambda）。[](https://www.reddit.com/r/java/comments/18z151f/strict_code_formatter/)

### 可用選項摘要

| **選項**                  | **說明**                                                                 | **範例值**                              |
|-----------------------------|---------------------------------------------------------------------------------|------------------------------------------------|
| `<palantirJavaFormat>`      | 配置 Palantir Java Format。                                                | `<version>2.53.0</version>`, `<style>PALANTIR</style>` |
| `<indent>`                  | 設定縮排樣式（tab 或空格）和大小。                               | `<tabs>true</tabs>`, `<spacesPerTab>4</spacesPerTab>` |
| `<importOrder>`             | 定義匯入群組順序或使用檔案。                                      | `<order>java,javax,org,com,\\#</order>`        |
| `<removeUnusedImports>`     | 移除未使用的匯入，可選引擎。                                   | `<engine>cleanthat-javaparser-unnecessaryimport</engine>` |
| `<trimTrailingWhitespace>`  | 移除行尾空白字元。                                                   | `<trimTrailingWhitespace/>`                    |
| `<endWithNewline>`         | 確保檔案以換行結尾。                                              | `<endWithNewline/>`                           |
| `<toggleOffOn>`            | 啟用 `spotless:off`/`spotless:on` 標籤。                                     | `<toggleOffOn/>`                              |
| `<licenseHeader>`          | 加入授權標頭。                                                         | `<content>/* (C) $YEAR */</content>`           |
| `<formatAnnotations>`       | 將註解格式化為與欄位位於同一行。                          | `<formatAnnotations/>`                         |
| `<sortPom>`                | 使用排序和縮排格式化 `pom.xml`。                                | `<nrOfIndentSpace>2</nrOfIndentSpace>`        |

### 來源

- Spotless Maven Plugin 文件：[GitHub](https://github.com/diffplug/spotless/tree/main/plugin-maven)[](https://github.com/diffplug/spotless/blob/main/plugin-maven/README.md)
- Palantir Java Format：[GitHub](https://github.com/palantir/palantir-java-format)[](https://github.com/palantir/palantir-java-format)
- Stack Overflow 與社群範例，關於 Spotless 配置[](https://stackoverflow.com/questions/50027892/override-google-java-format-with-spotless-maven-plugin)[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)[](https://stackoverflow.com/questions/77126927/spotless-eclipse-formatter-java-17-error-on-string-literals-removing-unu)

此配置確保使用 Palantir Java Format 進行一致的程式碼格式化，並根據您對 tabspace、縮排和匯入順序的偏好進行調整。如果您需要進一步說明或其他選項，請告訴我！