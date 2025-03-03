---
audio: false
generated: true
lang: zh
layout: post
title: JaCoCo Maven 插件
translated: true
---

这是一个关于如何使用 JaCoCo Maven 插件来测量 Maven 基于的 Java 项目代码覆盖率的分步指南。JaCoCo（Java 代码覆盖）是一个与 Maven 集成的工具，用于跟踪测试（通常是单元测试）执行了多少代码。通过在项目中添加和配置 JaCoCo Maven 插件，您可以在构建过程中生成详细的覆盖率报告。

---

### 使用 JaCoCo Maven 插件的步骤

#### 1. 将 JaCoCo Maven 插件添加到您的 `pom.xml`
要使用 JaCoCo Maven 插件，您需要在项目的 `pom.xml` 文件的 `<build><plugins>` 部分中包含它。以下是一个基本配置，用于设置插件：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version> <!-- 使用最新可用版本 -->
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

- **`groupId`、`artifactId` 和 `version`**：这些标识 JaCoCo Maven 插件。将 `0.8.12` 替换为 [Maven 中央仓库](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin) 上的最新版本。
- **`<executions>`**：此部分配置插件在 Maven 构建生命周期中何时以及如何运行：
  - **`<goal>prepare-agent</goal>`**：准备 JaCoCo 代理以在测试执行期间收集覆盖数据。默认情况下，它绑定到早期阶段（如 `initialize`），除非自定义，否则不需要显式阶段。
  - **`<goal>report</goal>`**：在测试运行后生成覆盖报告。它绑定到 `verify` 阶段，该阶段在 `test` 阶段之后，确保所有测试数据都可用。

#### 2. 确保测试已配置
JaCoCo 插件通过分析测试执行（通常是由 Maven Surefire 插件运行的单元测试）来工作。在大多数 Maven 项目中，Surefire 默认包含并运行位于 `src/test/java` 的测试。除非您的测试是非标准的，否则不需要额外配置。验证：
- 您编写了单元测试（例如，使用 JUnit 或 TestNG）。
- Surefire 插件存在（通常从大多数情况下的默认 Maven 父 POM 继承）。

如果需要显式配置 Surefire，它可能看起来像这样：

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- 使用最新版本 -->
</plugin>
```

`prepare-agent` 目标通过修改 `argLine` 属性来设置 JaCoCo 代理，Surefire 使用该属性来启用覆盖跟踪的测试运行。

#### 3. 运行 Maven 构建
要生成覆盖报告，在项目目录中执行以下命令：

```bash
mvn verify
```

- **`mvn verify`**：这将运行所有阶段，直到 `verify`，包括 `compile`、`test` 和 `verify`。JaCoCo 插件将：
  1. 在测试运行之前准备代理。
  2. 在 `test` 阶段（Surefire 执行测试时）收集覆盖数据。
  3. 在 `verify` 阶段生成报告。

或者，如果您只想运行测试而不继续到 `verify`，请使用：

```bash
mvn test
```

但是，由于 `report` 目标在此配置中绑定到 `verify`，您需要运行 `mvn verify` 才能查看报告。如果您更喜欢在 `mvn test` 期间生成报告，可以将 `report` 执行的 `<phase>` 更改为 `test`，尽管 `verify` 是常见的约定。

#### 4. 查看覆盖报告
运行 `mvn verify` 后，JaCoCo 默认生成一个 HTML 报告。您可以在以下位置找到它：

```
target/site/jacoco/index.html
```

- 打开此文件以在 Web 浏览器中查看代码覆盖率的详细分解，包括包、类、方法和行的百分比。
- 该报告还包括相同目录中的 XML 和 CSV 格式（`jacoco.xml` 和 `jacoco.csv`），这些格式对于与 CI 系统集成非常有用。

---

### 可选自定义
对于更高级的用例，您可以调整插件配置：

- **排除类或包**：
  要将某些代码排除在覆盖分析之外（例如生成的代码），请添加 `<configuration>` 部分：

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  将此放在 `<plugin>` 标签内，`<executions>` 之上。

- **强制覆盖阈值**：
  如果覆盖率低于阈值，则失败构建，添加 `check` 目标：

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
                          <minimum>0.80</minimum> <!-- 80% 行覆盖 -->
                      </limit>
                  </limits>
              </rule>
          </rules>
      </configuration>
  </execution>
  ```

- **更改报告输出目录**：
  要自定义报告位置，请添加：

  ```xml
  <configuration>
      <destFile>${project.build.directory}/custom-jacoco.exec</destFile>
      <dataFile>${project.build.directory}/custom-jacoco.exec</dataFile>
      <outputDirectory>${project.build.directory}/custom-reports</outputDirectory>
  </configuration>
  ```

---

### 摘要
要使用 JaCoCo Maven 插件：
1. 将插件添加到您的 `pom.xml` 中，并使用 `prepare-agent` 和 `report` 目标。
2. 确保您的项目配置了测试（通常通过 Surefire）。
3. 运行 `mvn verify` 以生成覆盖报告。
4. 在 `target/site/jacoco/index.html` 查看报告。

此设置提供了一种直接的方法将代码覆盖率集成到您的 Maven 构建过程中，帮助您评估测试的有效性。有关最新插件版本或高级配置，请参阅 [官方 JaCoCo 文档](https://www.jacoco.org/jacoco/trunk/doc/maven.html)。