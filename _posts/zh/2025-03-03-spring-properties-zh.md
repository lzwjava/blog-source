---
audio: false
generated: true
lang: zh
layout: post
title: 属性文件选择在Spring Boot
translated: true
---

在一个Spring Boot Maven项目中，你有两个属性文件，`appProperties.properties` 和 `appProperties-hk.properties`，位于 `src/main/resources` 下。要控制使用哪个属性文件，特别是指定使用 `-hk` 属性，可以利用 Spring Boot 的配置机制。以下是如何做到的：

### 解决方案

1. **创建一个 `application.properties` 文件**
   - 默认情况下，Spring Boot 会在 `src/main/resources` 中查找 `application.properties` 或 `application.yml` 来加载配置设置。
   - 要使用你的自定义属性文件（`appProperties.properties` 和 `appProperties-hk.properties`），你需要通知 Spring Boot 查找基名为 `appProperties` 的文件，而不是默认的 `application`。
   - 在 `src/main/resources` 中的新 `application.properties` 文件中添加以下行：

     ```properties
     spring.config.name=appProperties
     ```

   - 此设置告诉 Spring Boot 将 `appProperties.properties` 作为基础配置文件加载，并且在激活配置文件时，它还会自动查找类似 `appProperties-{profile}.properties` 的配置文件变体。

2. **使用 Spring 配置文件指定 `-hk` 属性**
   - Spring Boot 支持配置文件，允许你根据活动配置文件加载额外的或覆盖的属性文件。
   - 由于你的文件命名为 `appProperties-hk.properties`，它遵循 `appProperties-{profile}.properties` 的模式。这里，“hk” 可以被视为配置文件名。
   - 要使用 `appProperties-hk.properties`，在运行应用程序时激活 “hk” 配置文件。Spring Boot 将加载 `appProperties.properties` 和 `appProperties-hk.properties`，其中 `appProperties-hk.properties` 中的属性将覆盖 `appProperties.properties` 中的任何匹配属性。

3. **如何激活 “hk” 配置文件**
   - **通过命令行**：在运行 Spring Boot 应用程序时，使用 `--spring.profiles.active` 参数指定活动配置文件。例如：
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     将 `myapp.jar` 替换为 Maven 生成的应用程序的 JAR 文件名称。

   - **通过 Maven**：如果你使用 `spring-boot:run` 目标运行应用程序，请在 `pom.xml` 中配置配置文件：
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <profiles>
                 <profile>hk</profile>
             </profiles>
         </configuration>
     </plugin>
     ```
     然后运行：
     ```bash
     mvn spring-boot:run
     ```

   - **通过系统属性**：将配置文件设置为 JVM 参数：
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **通过环境变量**：在环境中导出配置文件（例如，在类 Unix 系统中）：
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### 它是如何工作的
- 设置 `spring.config.name=appProperties` 后，Spring Boot 使用 `appProperties` 作为配置文件的基名。
- 当没有活动配置文件时，只加载 `appProperties.properties`。
- 当激活 “hk” 配置文件（例如，通过 `--spring.profiles.active=hk`），Spring Boot 将加载 `appProperties.properties` 和 `appProperties-hk.properties`。如果有重复的属性，`appProperties-hk.properties` 中的属性将优先。

### 最后步骤
- 确保 `appProperties.properties` 和 `appProperties-hk.properties` 位于 `src/main/resources`。
- 将 `application.properties` 文件（其中包含 `spring.config.name=appProperties`）添加到 `src/main/resources`。
- 使用激活 “hk” 配置文件运行你的应用程序，以使用 `-hk` 属性。

这种方法符合 Spring Boot 约定，使其成为控制项目中使用哪个属性文件的典型和简便方法。要特别使用 `-hk` 属性，只需按照上述方法激活 “hk” 配置文件。