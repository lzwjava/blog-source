---
audio: false
generated: true
lang: hant
layout: post
title: 屬性檔案選擇於 Spring Boot
translated: true
---

在一個 Spring Boot Maven 專案中，你有兩個屬性文件，`appProperties.properties` 和 `appProperties-hk.properties`，位於 `src/main/resources`。要控制使用哪個屬性文件，特別是指定使用 `-hk` 屬性，可以利用 Spring Boot 的配置機制。以下是如何做到的：

### 解決方案

1. **創建一個 `application.properties` 文件**
   - 默認情況下，Spring Boot 會在 `src/main/resources` 中查找 `application.properties` 或 `application.yml` 來加載配置設置。
   - 要使用自定義屬性文件（`appProperties.properties` 和 `appProperties-hk.properties`），需要告訴 Spring Boot 查找基名為 `appProperties` 的文件，而不是默認的 `application`。
   - 在 `src/main/resources` 中新建一個 `application.properties` 文件，並添加以下行：

     ```properties
     spring.config.name=appProperties
     ```

   - 這個設置告訴 Spring Boot 將 `appProperties.properties` 作為基礎配置文件，並且在活動的配置文件中自動查找像 `appProperties-{profile}.properties` 這樣的配置文件。

2. **使用 Spring 配置文件指定 `-hk` 屬性**
   - Spring Boot 支持配置文件，允許根據活動的配置文件加載額外的或覆蓋的屬性文件。
   - 由於你的文件名為 `appProperties-hk.properties`，它遵循 `appProperties-{profile}.properties` 的模式。這裡的 "hk" 可以被視為配置文件名。
   - 要使用 `appProperties-hk.properties`，在運行應用程序時激活 "hk" 配置文件。Spring Boot 將加載 `appProperties.properties` 和 `appProperties-hk.properties`，並且 `appProperties-hk.properties` 中的屬性將覆蓋 `appProperties.properties` 中的任何匹配屬性。

3. **如何激活 "hk" 配置文件**
   - **通過命令行**：在運行 Spring Boot 應用程序時，使用 `--spring.profiles.active` 參數指定活動配置文件。例如：
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     將 `myapp.jar` 替換為 Maven 生成的應用程序的 JAR 文件名。

   - **通過 Maven**：如果你使用 `spring-boot:run` 目標運行應用程序，在 `pom.xml` 中配置配置文件：
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
     然後運行：
     ```bash
     mvn spring-boot:run
     ```

   - **通過系統屬性**：將配置文件設置為 JVM 參數：
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **通過環境變量**：在環境中導出配置文件（例如在類 Unix 系統中）：
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### 運作方式
- 設置 `spring.config.name=appProperties` 後，Spring Boot 使用 `appProperties` 作為配置文件的基名。
- 當沒有活動配置文件時，只加載 `appProperties.properties`。
- 當激活 "hk" 配置文件（例如通過 `--spring.profiles.active=hk`）時，Spring Boot 將加載 `appProperties.properties` 和 `appProperties-hk.properties`。`appProperties-hk.properties` 中定義的屬性將優先於 `appProperties.properties` 中的屬性。

### 最後步驟
- 確保 `appProperties.properties` 和 `appProperties-hk.properties` 位於 `src/main/resources`。
- 在 `src/main/resources` 中添加 `application.properties`，內容為 `spring.config.name=appProperties`。
- 使用激活 "hk" 配置文件運行應用程序，以使用 `-hk` 屬性。

這種方法符合 Spring Boot 慣例，是一種典型且簡單的方法來控制專案中使用哪個屬性文件。要特定使用 `-hk` 屬性，只需按照上述方法激活 "hk" 配置文件。