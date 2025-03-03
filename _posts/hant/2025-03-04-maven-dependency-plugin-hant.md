---
audio: false
generated: true
lang: hant
layout: post
title: Maven 相依性插件
translated: true
---

**Maven 相依性插件** 是 Maven 中一個強大的工具，Maven 是一個廣泛使用的 Java 專案自動化構建工具，它幫助你管理和操作專案的相依性。Maven 專案中的相依性是外部庫或模組，聲明在 `pom.xml` 文件中，Maven 從存儲庫下載並在編譯、運行或測試時提供。相依性插件通過提供各種目標（任務）來擴展這一功能，以分析、複製、列出或以其他方式處理這些相依性。以下是如何有效使用它的方法：

---

#### **1. 使用概述**
你可以以兩種主要方式使用 Maven 相依性插件：
- **在 `pom.xml` 文件中配置它**：這允許你將特定插件目標綁定到 Maven 构建生命周期的階段（例如 `package`、`install`），以便在構建過程中自動執行。
- **直接從命令行運行目標**：這對於一次性任務或不想修改 `pom.xml` 的情況非常理想。

插件由其坐標識別：`groupId: org.apache.maven.plugins`，`artifactId: maven-dependency-plugin`。在配置時需要指定一個版本（例如 `3.2.0`），儘管在命令行使用時 Maven 通常可以解析最新版本。

---

#### **2. 將插件添加到 `pom.xml`**
要將插件作為構建過程的一部分使用，將其添加到 `pom.xml` 的 `<build><plugins>` 部分。以下是一個基本示例：

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

使用這種設置，可以通過添加 `<executions>` 块來配置在構建生命周期期間執行的特定目標。

---

#### **3. 常見目標及其使用方法**
插件提供了多個目標來管理相依性。以下是一些最常用的目標及其使用示例：

##### **a. `copy-dependencies`**
- **用途**：將專案相依性複製到指定目錄（例如，打包到 `lib` 資料夾）。
- **在 `pom.xml` 中配置**：
  將此目標綁定到 `package` 阶段，以在 `mvn package` 期間複製相依性：

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

  - `${project.build.directory}/lib` 解析為專案中的 `target/lib`。
  - `<includeScope>runtime</includeScope>` 將複製限制為 `compile` 和 `runtime` 範圍的相依性，排除 `test` 和 `provided`。

- **命令行**：
  直接運行而不修改 `pom.xml`：

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib
  ```

##### **b. `tree`**
- **用途**：顯示相依性樹，顯示所有直接和傳遞相依性及其版本。這對於識別版本衝突很有用。
- **命令行**：
  簡單運行：

  ```bash
  mvn dependency:tree
  ```

  這將輸出相依性的層次結構視圖到控制台。
- **在 `pom.xml` 中配置**（可選）：
  如果要在構建階段（例如 `verify`）運行，請類似於 `copy-dependencies` 配置。

##### **c. `analyze`**
- **用途**：分析相依性以識別問題，例如：
  - 使用但未聲明的相依性。
  - 聲明但未使用的相依性。
- **命令行**：
  運行：

  ```bash
  mvn dependency:analyze
  ```

  這在控制台生成一份報告。
- **注意**：此目標可能需要對複雜專案進行額外配置以精細化其分析。

##### **d. `list`**
- **用途**：列出專案的所有解析相依性。
- **命令行**：
  運行：

  ```bash
  mvn dependency:list
  ```

  這提供了一個相依性的平面列表，適合快速參考。

##### **e. `unpack`**
- **用途**：將特定相依性（例如 JAR 文件）的內容提取到目錄。
- **命令行**：
  示例以提取特定工件：

  ```bash
  mvn dependency:unpack -Dartifact=groupId:artifactId:version -DoutputDirectory=target/unpacked
  ```

  將 `groupId:artifactId:version` 替換為相依性的坐標（例如 `org.apache.commons:commons-lang3:3.12.0`）。

##### **f. `purge-local-repository`**
- **用途**：從本地 Maven 存儲庫（`~/.m2/repository`）中刪除指定的相依性，強制從遠程存儲庫重新下載。
- **命令行**：
  運行：

  ```bash
  mvn dependency:purge-local-repository
  ```

  這對於排除腐敗的相依性文件很有幫助。

---

#### **4. 自定義選項**
許多目標支持配置參數以定制其行為：
- **`outputDirectory`**：指定複製或解壓文件的位置（例如 `target/lib`）。
- **`includeScope` 或 `excludeScope`**：按範圍篩選相依性（例如 `runtime`、`test`）。
- **`artifact`**：針對特定相依性的目標（例如 `unpack`）。

這些可以在 `pom.xml` 的 `<configuration>` 部分設置，或作為命令行參數與 `-D` 一起傳遞（例如 `-DincludeScope=runtime`）。

---

#### **5. 實際示例**
- **情景 1：打包獨立應用程序**
  使用 `copy-dependencies` 將所有運行時相依性收集到 `lib` 資料夾：

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
  ```

- **情景 2：調試相依性衝突**
  運行 `dependency:tree` 以檢查傳遞相依性：

  ```bash
  mvn dependency:tree
  ```

  如果發現多個庫的版本（例如 `commons-logging`），通過在 `pom.xml` 中添加 `<dependencyManagement>` 部分來解決衝突。

- **情景 3：提取資源**
  提取相依性以訪問其內容：

  ```bash
  mvn dependency:unpack -Dartifact=org.example:my-lib:1.0.0 -DoutputDirectory=target/resources
  ```

---

#### **6. 摘要**
要使用 Maven 相依性插件：
- 將其添加到 `pom.xml` 中，並配置特定目標和配置，如果希望將其集成到構建過程中。
- 直接從命令行運行目標（例如 `copy-dependencies`、`tree`、`analyze`、`list` 或 `unpack`）以進行臨時任務。
- 使用配置選項自定義行為以適應專案的需求。

這個插件是一個靈活的工具，用於管理相依性超越簡單聲明，使其對於構建、調試和分發 Maven 專案至關重要。