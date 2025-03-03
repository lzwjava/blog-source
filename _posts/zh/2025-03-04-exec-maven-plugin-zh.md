---
audio: false
generated: true
lang: zh
layout: post
title: Maven Exec 插件
translated: true
---

要在 Maven 项目中使用 `org.codehaus.mojo` Exec Maven 插件，您需要在 `pom.xml` 文件中配置它，并决定在构建过程中如何执行程序——无论是外部命令还是 Java 程序。插件提供了两个主要目标：`exec:exec` 用于运行外部程序，`exec:java` 用于执行 Java 类。下面，我将指导您完成设置和有效使用它的步骤。

### 步骤 1：在 `pom.xml` 中添加插件
首先，在 `pom.xml` 的 `<build><plugins>` 部分包含 Exec Maven 插件。指定 `groupId`、`artifactId` 和版本（目前最新版本是 `3.1.0`）：

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

这将插件添加到您的项目中，但直到您配置它或手动运行其目标时，它什么也不会做。

### 步骤 2：选择您的目标
插件提供了两个主要目标：
- **`exec:exec`**：执行任何外部程序（例如，shell 脚本、二进制文件，甚至是 `java` 命令）。
- **`exec:java`**：在与 Maven 相同的 JVM 中运行项目中的具有 `main` 方法的 Java 类。

您可以通过从命令行手动运行它们（例如，`mvn exec:exec`）或将它们绑定到 Maven 构建生命周期的特定阶段来使用这些目标。

### 选项 1：使用 `exec:java` 运行 Java 程序
如果要从项目中执行 Java 类，请使用 `exec:java` 目标。这对于运行项目中具有 `main` 方法的类非常理想，自动利用项目的运行时类路径（包括依赖项）。

#### 手动执行
添加配置以指定主类：

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

然后，从命令行运行它：

```bash
mvn exec:java
```

这将在与 Maven 相同的 JVM 中执行 `com.example.Main`，继承 Maven 的 JVM 设置。

#### 构建期间的自动执行
要在构建阶段（例如，`test`）自动运行它，请使用 `<executions>` 部分：

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

现在，当您运行 `mvn test` 时，`com.example.Main` 类将在 `test` 阶段执行。

#### 传递参数或系统属性
您可以将参数传递给 `main` 方法或设置系统属性：

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

请注意，`exec:java` 在与 Maven 相同的 JVM 中运行，因此 JVM 选项（例如，`-Xmx`）将从如何调用 Maven（例如，`mvn -Xmx512m exec:java`）继承。

### 选项 2：使用 `exec:exec` 运行外部程序
对于执行外部程序（例如，shell 脚本或命令），请使用 `exec:exec` 目标。

#### 手动执行
配置插件以运行脚本：

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

使用以下命令运行它：

```bash
mvn exec:exec
```

这将在指定的工作目录中使用指定的参数执行 `myScript.sh`。

#### 构建期间的自动执行
将其绑定到某个阶段，例如在集成测试之前启动和停止服务器：

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

运行 `mvn integration-test` 将在测试之前启动服务器并在之后停止。

#### 使用自定义 JVM 选项运行 Java
如果需要具有特定选项的单独 JVM（与 `exec:java` 不同），请使用 `exec:exec` 并使用 `java` 可执行文件。您需要手动管理类路径。以下是一个示例：

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

要在类路径中包含依赖项，可以使用 `maven-dependency-plugin` 来生成它：

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

根据需要调整类路径分隔符（Unix 使用 `:`，Windows 使用 `;`）。

### 附加配置选项
- **环境变量**（用于 `exec:exec`）：

  ```xml
  <configuration>
      <executable>myScript.sh</executable>
      <environmentVariables>
          <MY_VAR>value</MY_VAR>
      </environmentVariables>
  </configuration>
  ```

- **工作目录**：使用 `<workingDirectory>` 设置命令运行的位置。

### 总结
Exec Maven 插件非常多功能：
- 使用 `exec:java` 可以轻松运行项目中的 Java 类，利用项目的类路径，但它在 Maven 的 JVM 中运行。
- 使用 `exec:exec` 运行外部程序或具有自定义 JVM 选项的 Java，如果需要，则需要手动管理类路径。
- 在 `pom.xml` 中配置它，并通过 `<executions>` 将其绑定到构建阶段，或者手动运行它（`mvn exec:java` 或 `mvn exec:exec`）。

这种设置允许您将自定义执行无缝集成到 Maven 构建过程中！