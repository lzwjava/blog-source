---
audio: false
generated: true
lang: hant
layout: post
title: JaCoCo Maven 插件
translated: true
type: note
---

以下是一份關於**如何使用 JaCoCo Maven 插件**在 Maven 基礎的 Java 專案中測量程式碼覆蓋率的逐步指南。JaCoCo（Java Code Coverage）是一個能與 Maven 整合的工具，用於追蹤你的程式碼有多少部分被測試（通常是單元測試）執行到。透過在專案中添加並配置 JaCoCo Maven 插件，你可以在建置過程中生成詳細的覆蓋率報告。

---

### **使用 JaCoCo Maven 插件的步驟**

#### **1. 將 JaCoCo Maven 插件添加到你的 `pom.xml`**
要使用 JaCoCo Maven 插件，你需要將它包含在專案 `pom.xml` 檔案的 `<build><plugins>` 區段中。以下是一個基本的配置設定：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version> <!-- 請使用可用的最新版本 -->
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

- **`groupId`、`artifactId` 和 `version`**：這些用於識別 JaCoCo Maven 插件。請將 `0.8.12` 替換為 [Maven Central Repository](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin) 上可用的最新版本。
- **`<executions>`**：此區段配置插件在 Maven 建置生命週期中的執行時機與方式：
  - **`<goal>prepare-agent</goal>`**：準備 JaCoCo 代理，以便在測試執行期間收集覆蓋率數據。預設情況下，它綁定到早期階段（例如 `initialize`），除非自定義，否則不需要明確指定階段。
  - **`<goal>report</goal>`**：在測試運行後生成覆蓋率報告。此處將其綁定到 `verify` 階段，該階段在 `test` 階段之後發生，確保所有測試數據可用。

#### **2. 確保測試已配置**
JaCoCo 插件透過分析測試執行（通常是由 Maven Surefire Plugin 運行的單元測試）來工作。在大多數 Maven 專案中，Surefire 預設已包含，並會運行位於 `src/test/java` 的測試。除非你的測試是非標準的，否則不需要額外配置。請確認：
- 你已編寫單元測試（例如使用 JUnit 或 TestNG）。
- Surefire 插件存在（在大多數情況下，它是從預設的 Maven 父 POM 繼承而來）。

如果你需要明確配置 Surefire，它可能看起來像這樣：

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- 請使用最新版本 -->
</plugin>
```

`prepare-agent` 目標透過修改 `argLine` 屬性來設置 JaCoCo 代理，Surefire 使用該屬性來運行啟用覆蓋率追蹤的測試。

#### **3. 運行 Maven 建置**
要生成覆蓋率報告，請在專案目錄中執行以下命令：

```bash
mvn verify
```

- **`mvn verify`**：這會運行直到 `verify` 的所有階段，包括 `compile`、`test` 和 `verify`。JaCoCo 插件將會：
  1. 在測試運行前準備代理。
  2. 在 `test` 階段（當 Surefire 執行測試時）收集覆蓋率數據。
  3. 在 `verify` 階段生成報告。

或者，如果你只想運行測試而不繼續到 `verify`，可以使用：

```bash
mvn test
```

然而，由於在此配置中 `report` 目標綁定到 `verify`，你需要運行 `mvn verify` 才能看到報告。如果你希望報告在 `mvn test` 期間生成，可以將 `report` 執行的 `<phase>` 更改為 `test`，但 `verify` 是常見的慣例。

#### **4. 查看覆蓋率報告**
運行 `mvn verify` 後，JaCoCo 預設會生成一個 HTML 報告。你可以在以下位置找到它：

```
target/site/jacoco/index.html
```

- 在網頁瀏覽器中打開此文件，以查看程式碼覆蓋率的詳細細分，包括套件、類別、方法與行的覆蓋百分比。
- 報告還包含相同目錄中的 XML 和 CSV 格式（`jacoco.xml` 和 `jacoco.csv`），對於與 CI 系統等工具的整合非常有用。

---

### **可選自定義**
對於更高級的使用案例，你可以調整插件配置：

- **排除類別或套件**：
  要從覆蓋率分析中排除某些程式碼（例如生成的程式碼），添加一個 `<configuration>` 區段：

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  將此置於 `<plugin>` 標籤內，`<executions>` 之上。

- **強制執行覆蓋率閾值**：
  如果覆蓋率低於閾值，要使建置失敗，請添加 `check` 目標：

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

- **變更報告輸出目錄**：
  要自定義報告位置，請添加：

  ```xml
  <configuration>
      <destFile>${project.build.directory}/custom-jacoco.exec</destFile>
      <dataFile>${project.build.directory}/custom-jacoco.exec</dataFile>
      <outputDirectory>${project.build.directory}/custom-reports</outputDirectory>
  </configuration>
  ```

---

### **總結**
要使用 JaCoCo Maven 插件：
1. 將插件添加到你的 `pom.xml`，並包含 `prepare-agent` 和 `report` 目標。
2. 確保你的專案已配置測試（通常透過 Surefire）。
3. 運行 `mvn verify` 以生成覆蓋率報告。
4. 在 `target/site/jacoco/index.html` 查看報告。

此設置提供了一種直接的方式，將程式碼覆蓋率整合到你的 Maven 建置過程中，幫助你評估測試的有效性。有關最新插件版本或高級配置，請參閱 [官方 JaCoCo 文檔](https://www.jacoco.org/jacoco/trunk/doc/maven.html)。