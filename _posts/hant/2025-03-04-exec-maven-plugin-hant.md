---
audio: false
generated: true
lang: hant
layout: post
title: Maven 插件
translated: true
---

在你的 Maven 專案中使用 `org.codehaus.mojo` Exec Maven 插件，你需要在 `pom.xml` 文件中配置它，並決定在構建過程中如何執行程序——無論是外部命令還是 Java 程序。插件提供兩個主要目標：`exec:exec` 用於運行外部程序，`exec:java` 用於執行 Java 類。以下，我將指導你如何設置並有效使用它。

### 第 1 步：在 `pom.xml` 中添加插件
首先，在 `pom.xml` 的 `<build><plugins>` 部分中包含 Exec Maven 插件。指定 `groupId`、`artifactId` 和一個版本（目前最新版本是 `3.1.0`）：

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

這將插件添加到你的專案中，但直到你配置它或手動運行其目標，它什麼也做不了。

### 第 2 步：選擇你的目標
插件提供兩個主要目標：
- **`exec:exec`**：執行任何外部程序（例如 shell 腳本、二進制文件，甚至是 `java` 命令）。
- **`exec:java`**：在與 Maven 相同的 JVM 中運行具有 `main` 方法的 Java 類。

你可以通過從命令行手動運行它們（例如 `mvn exec:exec`）或將它們綁定到 Maven 构建生命周期的特定階段來使用這些目標。

### 選項 1：使用 `exec:java` 運行 Java 程序
如果你想從專案中執行 Java 類，請使用 `exec:java` 目標。這對於運行專案中具有 `main` 方法的類來說是理想的，自動利用專案的運行時類路徑（包括依賴）。

#### 手動執行
添加配置以指定主類：

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

然後，從命令行運行它：

```bash
mvn exec:java
```

這將在與 Maven 相同的 JVM 中執行 `com.example.Main`，繼承 Maven 的 JVM 設置。

#### 在構建過程中自動執行
要在構建階段（例如 `test`）自動運行它，請使用 `<executions>` 部分：

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

現在，當你運行 `mvn test` 時，`com.example.Main` 類將在 `test` 阶段執行。

#### 傳遞參數或系統屬性
你可以將參數傳遞給 `main` 方法或設置系統屬性：

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

請注意，`exec:java` 在與 Maven 相同的 JVM 中運行，因此 JVM 選項（例如 `-Xmx`）將從如何調用 Maven（例如 `mvn -Xmx512m exec:java`）繼承。

### 選項 2：使用 `exec:exec` 運行外部程序
對於執行外部程序（例如 shell 腳本或命令），請使用 `exec:exec` 目標。

#### 手動執行
配置插件以運行腳本：

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

使用以下命令運行它：

```bash
mvn exec:exec
```

這將在指定的工作目錄中使用指定的參數運行 `myScript.sh`。

#### 在構建過程中自動執行
將其綁定到一個階段，例如在集成測試之前啟動和停止伺服器：

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

運行 `mvn integration-test` 將在測試之前啟動伺服器，並在測試之後停止它。

#### 使用自定義 JVM 選項運行 Java
如果你需要一個具有特定選項的單獨 JVM（與 `exec:java` 不同），請使用 `exec:exec` 並使用 `java` 可執行文件。你需要手動管理類路徑。以下是一個示例：

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

要在類路徑中包含依賴，你可以使用 `maven-dependency-plugin` 來生成它：

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

根據需要調整類路徑分隔符（Unix 使用 `:`，Windows 使用 `;`）。

### 額外的配置選項
- **環境變量**（適用於 `exec:exec`）：

  ```xml
  <configuration>
      <executable>myScript.sh</executable>
      <environmentVariables>
          <MY_VAR>value</MY_VAR>
      </environmentVariables>
  </configuration>
  ```
- **工作目錄**：使用 `<workingDirectory>` 設置命令運行的位置。

### 摘要
Exec Maven 插件非常靈活：
- 使用 `exec:java` 可以輕鬆運行專案中的 Java 類，利用專案的類路徑，但它在 Maven 的 JVM 中運行。
- 使用 `exec:exec` 運行外部程序或具有自定義 JVM 選項的 Java，如果需要則手動管理類路徑。
- 在 `pom.xml` 中配置它，並通過 `<executions>` 將其綁定到構建階段，或者手動運行它（`mvn exec:java` 或 `mvn exec:exec`）。

這樣的設置允許你將自定義執行無縫地集成到 Maven 构建過程中！