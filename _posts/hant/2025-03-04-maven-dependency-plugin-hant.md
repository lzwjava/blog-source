---
audio: false
generated: true
lang: hant
layout: post
title: Maven 依賴插件
translated: true
type: note
---

**Maven Dependency Plugin** 是 Maven（一個廣泛用於 Java 專案的建構自動化工具）中的一個強大工具，可協助您管理和操作專案依賴項。Maven 專案中的依賴項是在 `pom.xml` 檔案中宣告的外部函式庫或模組，Maven 會從儲存庫下載這些依賴項，並在編譯、執行階段或測試期間提供使用。Dependency Plugin 透過提供各種目標（任務）來分析、複製、列出或以其他方式處理這些依賴項，從而擴展了此功能。以下是如何有效使用它：

---

#### **1. 使用方式概覽**
您可以使用兩種主要方式使用 Maven Dependency Plugin：
- **在 `pom.xml` 檔案中進行配置**：這允許您將特定的插件目標綁定到 Maven 建構生命週期的階段（例如 `package`、`install`），以便在建構過程中自動執行。
- **直接從命令列執行目標**：這適用於一次性任務或當您不想修改 `pom.xml` 時。

該插件由其座標識別：`groupId: org.apache.maven.plugins`、`artifactId: maven-dependency-plugin`。在配置時，您需要指定版本（例如 `3.2.0`），儘管在命令列使用中若省略版本，Maven 通常可以解析最新版本。

---

#### **2. 將插件新增至 `pom.xml`**
若要將插件作為建構過程的一部分使用，請將其新增至 `pom.xml` 的 `<build><plugins>` 區段。以下是一個基本範例：

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

透過此設定，您可以透過新增 `<executions>` 區塊來配置在建構生命週期期間執行的特定目標。

---

#### **3. 常見目標及使用方式**
該插件提供了多個用於管理依賴項的目標。以下是一些最常用的目標，以及如何使用它們的範例：

##### **a. `copy-dependencies`**
- **用途**：將專案依賴項複製到指定目錄（例如，打包到 `lib` 資料夾中）。
- **在 `pom.xml` 中配置**：
  將此目標綁定到 `package` 階段，以便在 `mvn package` 期間複製依賴項：

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

  - `${project.build.directory}/lib` 會解析為您專案中的 `target/lib`。
  - `<includeScope>runtime</includeScope>` 將複製限制為具有 `compile` 和 `runtime` 範圍的依賴項，排除 `test` 和 `provided`。

- **命令列**：
  直接執行而無需修改 `pom.xml`：

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib
  ```

##### **b. `tree`**
- **用途**：顯示依賴項樹，展示所有直接和傳遞依賴項及其版本。這對於識別版本衝突非常有用。
- **命令列**：
  直接執行：

  ```bash
  mvn dependency:tree
  ```

  這會將依賴項的階層結構視圖輸出到控制台。
- **在 `pom.xml` 中配置**（可選）：
  如果您希望在建構階段（例如 `verify`）執行此目標，可以類似於 `copy-dependencies` 進行配置。

##### **c. `analyze`**
- **用途**：分析依賴項以識別問題，例如：
  - 已使用但未宣告的依賴項。
  - 已宣告但未使用的依賴項。
- **命令列**：
  執行：

  ```bash
  mvn dependency:analyze
  ```

  這會在控制台中產生報告。
- **注意**：對於複雜的專案，此目標可能需要額外配置以改進其分析。

##### **d. `list`**
- **用途**：列出專案的所有已解析依賴項。
- **命令列**：
  執行：

  ```bash
  mvn dependency:list
  ```

  這提供了一個依賴項的扁平列表，便於快速參考。

##### **e. `unpack`**
- **用途**：將特定依賴項（例如 JAR 檔案）的內容解壓縮到目錄。
- **命令列**：
  解壓縮特定產品的範例：

  ```bash
  mvn dependency:unpack -Dartifact=groupId:artifactId:version -DoutputDirectory=target/unpacked
  ```

  將 `groupId:artifactId:version` 替換為依賴項的座標（例如 `org.apache.commons:commons-lang3:3.12.0`）。

##### **f. `purge-local-repository`**
- **用途**：從您的本地 Maven 儲存庫（`~/.m2/repository`）中移除指定的依賴項，強制從遠端儲存庫重新下載。
- **命令列**：
  執行：

  ```bash
  mvn dependency:purge-local-repository
  ```

  這有助於解決損壞的依賴項檔案問題。

---

#### **4. 自訂選項**
許多目標支援配置參數以自訂其行為：
- **`outputDirectory`**：指定複製或解壓縮檔案的位置（例如 `target/lib`）。
- **`includeScope` 或 `excludeScope`**：依範圍篩選依賴項（例如 `runtime`、`test`）。
- **`artifact`**：針對特定依賴項，用於 `unpack` 等目標。

這些可以在 `pom.xml` 的 `<configuration>` 區段中設定，或透過 `-D` 作為命令列參數傳遞（例如 `-DincludeScope=runtime`）。

---

#### **5. 實用範例**
- **情境 1：打包獨立應用程式**
  使用 `copy-dependencies` 將所有執行階段依賴項收集到 `lib` 資料夾：

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
  ```

- **情境 2：除錯依賴項衝突**
  執行 `dependency:tree` 以檢查傳遞依賴項：

  ```bash
  mvn dependency:tree
  ```

  如果您發現某個函式庫有多個版本（例如 `commons-logging`），請透過在 `pom.xml` 中新增 `<dependencyManagement>` 區段來解決衝突。

- **情境 3：提取資源**
  解壓縮依賴項以存取其內容：

  ```bash
  mvn dependency:unpack -Dartifact=org.example:my-lib:1.0.0 -DoutputDirectory=target/resources
  ```

---

#### **6. 總結**
要使用 Maven Dependency Plugin：
- 如果您希望將其整合到建構過程中，請將其新增至 `pom.xml` 並指定特定目標和配置。
- 對於臨時任務，直接從命令列執行目標，例如 `copy-dependencies`、`tree`、`analyze`、`list` 或 `unpack`。
- 使用配置選項自訂行為以滿足專案需求。

此插件是一個多功能工具，用於管理依賴項，不僅僅是簡單的宣告，使其對於建構、除錯和分發 Maven 專案非常寶貴。