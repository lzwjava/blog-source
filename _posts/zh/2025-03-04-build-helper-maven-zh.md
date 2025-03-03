---
audio: false
generated: true
lang: zh
layout: post
title: 构建助手 Maven 插件
translated: true
---

`builder-helper-maven-plugin`，现在称为**Build Helper Maven Plugin**，是一个多功能工具，旨在帮助完成Maven构建生命周期中的各种任务。最初托管在Codehaus，现在由MojoHaus维护，尽管其Maven坐标仍使用`org.codehaus.mojo`组ID。该插件提供了一组目标，帮助进行添加额外的源目录、附加额外的构件、解析版本信息等操作。下面，我将指导你如何在Maven项目中使用这个插件。

### 什么是Maven？
在深入了解插件之前，让我们先设定上下文。Maven是一个广泛使用的构建自动化工具，主要用于Java项目。它通过管理依赖、编译代码、打包应用程序等，简化和标准化构建过程，所有这些都通过一个名为`pom.xml`的中央文件进行配置。

### 第1步：在`pom.xml`中包含插件
要使用Build Helper Maven Plugin，你需要将其添加到Maven项目的`pom.xml`文件中的`<build><plugins>`部分。以下是如何做到这一点：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <!-- 将为特定目标添加执行 -->
        </plugin>
    </plugins>
</build>
```

- **组ID**：`org.codehaus.mojo`（反映其起源，尽管它现在在MojoHaus）。
- **构件ID**：`build-helper-maven-plugin`。
- **版本**：截至我最后一次更新，`3.6.0`是最新版本，但你应该检查[Maven Central](https://mvnrepository.com/artifact/org.codehaus.mojo/build-helper-maven-plugin)以获取最新发布。

这个声明使插件在你的项目中可用，但它不会做任何事情，直到你配置特定的目标。

### 第2步：配置特定目标的执行
Build Helper Maven Plugin提供了多个目标，每个目标都设计用于特定任务。你通过在插件声明中添加`<executions>`块来配置这些目标，指定它们何时运行（通过Maven生命周期阶段）以及它们如何行为。

以下是一些常用目标及其用途：

- **`add-source`**：向项目添加额外的源目录。
- **`add-test-source`**：添加额外的测试源目录。
- **`add-resource`**：添加额外的资源目录。
- **`attach-artifact`**：将额外的构件（例如文件）附加到项目以进行安装和部署。
- **`parse-version`**：解析项目的版本并设置属性（例如主要、次要、增量版本）。

每个目标都需要自己的配置，你在`<execution>`块中定义这些配置。

### 第3步：示例——添加额外的源目录
这个插件的一个常见用例是添加额外的源目录，因为Maven通常只支持一个默认目录（`src/main/java`）。以下是如何配置`add-source`目标以包含额外的源目录：

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

- **`<id>`**：此执行的唯一标识符（例如`add-source`）。
- **`<phase>`**：目标运行的Maven生命周期阶段（例如`generate-sources`确保目录在构建早期添加）。
- **`<goals>`**：指定要执行的目标（在这种情况下是`add-source`）。
- **`<configuration>`**：定义额外的源目录（用你的实际路径替换`path/to/your/extra/source/directory`，例如`src/main/generated`）。

当你运行Maven命令（例如`mvn compile`）时，Maven将包括这个额外的目录作为源文件夹。

### 附加说明
- **版本兼容性**：自3.0.0版本以来，插件需要Maven 3或更高版本。如果你使用的是较旧的Maven版本，你需要使用1.12或更早的插件版本。
- **多个目标**：你可以在同一个插件中定义多个`<execution>`块以运行不同的目标。例如，你可以通过包括`add-source`和`add-test-source`的执行来添加源和测试源目录。
- **运行插件**：配置后，运行Maven命令（例如`mvn clean install`）将在指定的阶段触发插件的目标。

### 更多资源
有关其他目标的更多详细信息和示例，请查看[官方使用页面](https://www.mojohaus.org/build-helper-maven-plugin/usage.html)。该页面提供了所有可用目标的全面文档和示例配置。

### 最后的思考
Build Helper Maven Plugin是你Maven工具包的一个强大补充，特别是对于需要非标准构建配置的项目。通过在`pom.xml`中包含它并配置适当的目标，你可以根据特定需求定制你的构建过程。尽管它起源于Codehaus，但它现在的家是MojoHaus，并且仍然是增强Maven构建的可靠选择。