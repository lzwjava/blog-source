---
audio: false
generated: true
lang: hant
layout: post
title: JaCoCo Maven 插件
translated: true
---

這裡有一個逐步指南，教你如何使用 **JaCoCo Maven 插件** 來測量 Maven 為基礎的 Java 專案的程式碼覆蓋率。JaCoCo（Java 程式碼覆蓋率）是一個與 Maven 集成的工具，用來追蹤測試（通常是單元測試）執行了多少程式碼。通過在專案中添加和配置 JaCoCo Maven 插件，你可以在構建過程中生成詳細的覆蓋率報告。

---

### **使用 JaCoCo Maven 插件的步驟**

#### **1. 在 `pom.xml` 中添加 JaCoCo Maven 插件**
要使用 JaCoCo Maven 插件，你需要在專案的 `pom.xml` 文件的 `<build><plugins>` 部分中包含它。以下是一個基本配置，設置插件：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version> <!-- 使用可用的最新版本 -->
            <executions>
                <execution>
                    <goals>
                        <goal>prepare-agent</goal>
                    </goals>
                </execution>
                <execution>
                    <id>report</id>
                    <phase>verify</phase>
                    <goals>
                        <goal>report</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`groupId`、`artifactId` 和 `version`**：這些標識 JaCoCo Maven 插件。將 `0.8.12` 替換為 [Maven Central Repository](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin) 上可用的最新版本。
- **`<executions>`**：這部分配置插件在 Maven 构建生命週期中何時以及如何運行：
  - **`<goal>prepare-agent</goal>`**：準備 JaCoCo 代理以在測試執行期間收集覆蓋數據。默認情況下，它綁定到一個早期階段（例如 `initialize`），除非自定義，否則不需要顯式階段。
  - **`<goal>report</goal>`**：在測試運行後生成覆蓋報告。它在此處綁定到 `verify` 阶段，該階段在 `test` 阶段之後發生，確保所有測試數據都可用。

#### **2. 確保測試已配置**
JaCoCo 插件通過分析測試執行來工作，通常是由 Maven Surefire 插件運行的單元測試。在大多數 Maven 專案中，Surefire 默認包含並在 `src/test/java` 中運行測試。除非測試非標準，否則不需要額外配置。驗證：
- 您已編寫單元測試（例如使用 JUnit 或 TestNG）。
- Surefire 插件存在（它通常從大多數情況下的默認 Maven 父 POM 繼承）。

如果需要顯式配置 Surefire，它可能看起來像這樣：

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- 使用最新版本 -->
</plugin>
```

`prepare-agent` 目標通過修改 `argLine` 屬性來設置 JaCoCo 代理，Surefire 使用該屬性來啟用覆蓋追蹤的測試運行。

#### **3. 運行 Maven 构建**
要生成覆蓋報告，在專案目錄中執行以下命令：

```bash
mvn verify
```

- **`mvn verify`**：這運行所有階段，包括 `compile`、`test` 和 `verify`。JaCoCo 插件將：
  1. 在測試運行之前準備代理。
  2. 在 `test` 阶段（當 Surefire 執行測試時）收集覆蓋數據。
  3. 在 `verify` 阶段生成報告。

或者，如果你只想運行測試而不繼續進行 `verify`，使用：

```bash
mvn test
```

然而，由於在這種配置中 `report` 目標綁定到 `verify`，你需要運行 `mvn verify` 才能看到報告。如果你更喜歡在 `mvn test` 期間生成報告，可以將 `report` 執行的 `<phase>` 更改為 `test`，儘管 `verify` 是一個常見的約定。

#### **4. 查看覆蓋報告**
運行 `mvn verify` 後，JaCoCo 默認生成一個 HTML 報告。你可以在以下位置找到它：

```
target/site/jacoco/index.html
```

- 打開這個文件以在網頁瀏覽器中查看程式碼覆蓋率的詳細分解，包括套件、類、方法和行的百分比。
- 報告還包括相同目錄中的 XML 和 CSV 格式（`jacoco.xml` 和 `jacoco.csv`），這對於與 CI 系統等工具集成非常有用。

---

### **可選自定義**
對於更高級的用例，你可以調整插件配置：

- **排除類或套件**：
  要將某些程式碼排除在覆蓋分析之外（例如生成的程式碼），添加一個 `<configuration>` 部分：

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  將此放在 `<plugin>` 標籤內，`<executions>` 之上。

- **強制覆蓋閾值**：
  如果覆蓋率低於閾值，則失敗構建，添加 `check` 目標：

  ```xml
  <execution>
      <id>check</id>
      <phase>verify</phase>
      <goals>
          <goal>check</goal>
      </goals>
      <configuration>
          <rules>
              <rule>
                  <element>BUNDLE</element>
                  <limits>
                      <limit>
                          <counter>LINE</counter>
                          <value>COVEREDRATIO</value>
                          <minimum>0.80</minimum> <!-- 80% 行覆蓋率 -->
                      </limit>
                  </limits>
              </rule>
          </rules>
      </configuration>
  </execution>
  ```

- **更改報告輸出目錄**：
  要自定義報告位置，添加：

  ```xml
  <configuration>
      <destFile>${project.build.directory}/custom-jacoco.exec</destFile>
      <dataFile>${project.build.directory}/custom-jacoco.exec</dataFile>
      <outputDirectory>${project.build.directory}/custom-reports</outputDirectory>
  </configuration>
  ```

---

### **摘要**
要使用 JaCoCo Maven 插件：
1. 將插件添加到 `pom.xml` 中，並配置 `prepare-agent` 和 `report` 目標。
2. 確保專案已配置測試（通常通過 Surefire）。
3. 運行 `mvn verify` 以生成覆蓋報告。
4. 在 `target/site/jacoco/index.html` 查看報告。

這種設置提供了一種簡單的方法來將程式碼覆蓋率集成到 Maven 构建過程中，幫助你評估測試的有效性。有關最新插件版本或高級配置，請參閱 [官方 JaCoCo 文檔](https://www.jacoco.org/jacoco/trunk/doc/maven.html)。