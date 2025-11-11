---
audio: false
generated: true
lang: hant
layout: post
title: Exec Maven 插件
translated: true
type: note
---

要在你的 Maven 專案中使用 `org.codehaus.mojo` Exec Maven Plugin，你需要在 `pom.xml` 檔案中進行配置，並決定在建置過程中要如何執行程式——無論是外部指令還是 Java 程式。該插件提供了兩個主要目標：用於執行外部程式的 `exec:exec` 和用於執行 Java 類別的 `exec:java`。下面我將引導你完成設定並有效使用它的步驟。

### 步驟 1：將插件添加到你的 `pom.xml`
首先，在你的 `pom.xml` 的 `<build><plugins>` 部分加入 Exec Maven Plugin。指定 `groupId`、`artifactId` 和版本（目前最新版本是 `3.1.0`）：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
        </plugin>
    </plugins>
</build>
```

這會將插件添加到你的專案中，但在你配置它或手動執行其目標之前，它還不會做任何事情。

### 步驟 2：選擇你的目標
該插件提供了兩個主要目標：
- **`exec:exec`**：執行任何外部程式（例如，Shell 腳本、二進制檔案，甚至是 `java` 指令）。
- **`exec:java`**：在你的專案中，於與 Maven 相同的 JVM 中執行具有 `main` 方法的 Java 類別。

你可以透過從命令列手動執行這些目標（例如，`mvn exec:exec`）或將它們綁定到 Maven 建置生命週期的特定階段來使用它們。

### 選項 1：使用 `exec:java` 執行 Java 程式
如果你想從你的專案中執行一個 Java 類別，請使用 `exec:java` 目標。這非常適合執行專案中某個類別的 `main` 方法，它會自動利用專案的執行時 classpath（包括依賴項）。

#### 手動執行
添加配置以指定主類別：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <mainClass>com.example.Main</mainClass>
            </configuration>
        </plugin>
    </plugins>
</build>
```

然後，從命令列執行：

```bash
mvn exec:java
```

這會在與 Maven 相同的 JVM 中執行 `com.example.Main`，並繼承 Maven 的 JVM 設定。

#### 在建置期間自動執行
要在建置階段（例如 `test`）自動執行它，請使用 `<executions>` 部分：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>run-my-java</id>
                    <phase>test</phase>
                    <goals>
                        <goal>java</goal>
                    </goals>
                    <configuration>
                        <mainClass>com.example.Main</mainClass>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

現在，當你執行 `mvn test` 時，`com.example.Main` 類別將在 `test` 階段執行。

#### 傳遞參數或系統屬性
你可以傳遞參數給 `main` 方法或設定系統屬性：

```xml
<configuration>
    <mainClass>com.example.Main</mainClass>
    <arguments>
        <argument>arg1</argument>
        <argument>arg2</argument>
    </arguments>
    <systemProperties>
        <systemProperty>
            <key>propertyName</key>
            <value>propertyValue</value>
        </systemProperty>
    </systemProperties>
</configuration>
```

請注意，`exec:java` 在與 Maven 相同的 JVM 中執行，因此 JVM 選項（例如 `-Xmx`）是從呼叫 Maven 的方式繼承而來的（例如 `mvn -Xmx512m exec:java`）。

### 選項 2：使用 `exec:exec` 執行外部程式
要執行像 Shell 腳本或指令這樣的外部程式，請使用 `exec:exec` 目標。

#### 手動執行
配置插件以執行腳本：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <executable>myScript.sh</executable>
                <workingDirectory>/path/to/dir</workingDirectory>
                <arguments>
                    <argument>param1</argument>
                    <argument>param2</argument>
                </arguments>
            </configuration>
        </plugin>
    </plugins>
</build>
```

使用以下指令執行：

```bash
mvn exec:exec
```

這會在指定的工作目錄中，使用給定的參數執行 `myScript.sh`。

#### 在建置期間自動執行
將它綁定到一個階段，例如為整合測試啟動和停止伺服器：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>start-server</id>
                    <phase>pre-integration-test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>startServer.sh</executable>
                    </configuration>
                </execution>
                <execution>
                    <id>stop-server</id>
                    <phase>post-integration-test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>stopServer.sh</executable>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

執行 `mvn integration-test` 將在測試前啟動伺服器並在測試後停止它。

#### 使用自訂 JVM 選項執行 Java
如果你需要一個具有特定選項的獨立 JVM（與 `exec:java` 不同），請使用帶有 `java` 可執行檔的 `exec:exec`。你需要手動管理 classpath。以下是一個範例：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <executable>java</executable>
                <arguments>
                    <argument>-Xmx512m</argument>
                    <argument>-classpath</argument>
                    <argument>${project.build.outputDirectory}</argument>
                    <argument>com.example.Main</argument>
                </arguments>
            </configuration>
        </plugin>
    </plugins>
</build>
```

要將依賴項包含在 classpath 中，你可以使用 `maven-dependency-plugin` 來生成它：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.2.0</version>
            <executions>
                <execution>
                    <id>build-classpath</id>
                    <phase>generate-resources</phase>
                    <goals>
                        <goal>build-classpath</goal>
                    </goals>
                    <configuration>
                        <outputProperty>project.classpath</outputProperty>
                    </configuration>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>run-java</id>
                    <phase>test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>java</executable>
                        <arguments>
                            <argument>-Xmx512m</argument>
                            <argument>-classpath</argument>
                            <argument>${project.classpath}:${project.build.outputDirectory}</argument>
                            <argument>com.example.Main</argument>
                        </arguments>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

請根據需要調整 classpath 分隔符號（Unix 用 `:`，Windows 用 `;`）。

### 其他配置選項
- **環境變數**（適用於 `exec:exec`）：
  ```xml
  <configuration>
      <executable>myScript.sh</executable>
      <environmentVariables>
          <MY_VAR>value</MY_VAR>
      </environmentVariables>
  </configuration>
  ```
- **工作目錄**：使用 `<workingDirectory>` 來設定指令執行的位置。

### 總結
Exec Maven Plugin 功能多樣：
- 使用 `exec:java` 輕鬆執行專案中的 Java 類別，利用專案的 classpath，但它會在 Maven 的 JVM 中執行。
- 使用 `exec:exec` 來執行外部程式或具有自訂 JVM 選項的 Java，如果需要，需手動管理 classpath。
- 在 `pom.xml` 中配置它，並可以手動執行（`mvn exec:java` 或 `mvn exec:exec`）或使用 `<executions>` 將其綁定到建置階段。

這種設定讓你可以將自訂執行無縫整合到你的 Maven 建置過程中！