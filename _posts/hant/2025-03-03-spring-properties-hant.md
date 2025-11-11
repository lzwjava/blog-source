---
audio: false
generated: true
lang: hant
layout: post
title: Spring Boot 中的屬性檔案選擇
translated: true
type: note
---

在 Spring Boot Maven 專案中，您有兩個屬性檔案 `appProperties.properties` 和 `appProperties-hk.properties`，位於 `src/main/resources` 目錄下。要控制使用哪個屬性檔案，特別是指定使用 `-hk` 屬性檔案，您可以利用 Spring Boot 的配置機制。以下是具體做法：

### 解決方案

1. **建立 `application.properties` 檔案**
   - 預設情況下，Spring Boot 會在 `src/main/resources` 中尋找 `application.properties` 或 `application.yml` 來載入配置設定。
   - 要使用您的自訂屬性檔案（`appProperties.properties` 和 `appProperties-hk.properties`），您需要告知 Spring Boot 尋找基礎名稱為 `appProperties` 的檔案，而非預設的 `application`。
   - 在 `src/main/resources` 中建立新的 `application.properties` 檔案，並加入以下行：

     ```properties
     spring.config.name=appProperties
     ```

   - 此設定會告訴 Spring Boot 將 `appProperties.properties` 作為基礎配置檔案載入，並且在啟動設定檔時，會自動尋找設定檔專用的變體檔案，例如 `appProperties-{profile}.properties`。

2. **使用 Spring 設定檔指定 `-hk` 屬性**
   - Spring Boot 支援設定檔，允許您根據啟動的設定檔載入額外或覆寫的屬性檔案。
   - 由於您的檔案命名為 `appProperties-hk.properties`，符合 `appProperties-{profile}.properties` 的模式。此處的 "hk" 可視為設定檔名稱。
   - 要使用 `appProperties-hk.properties`，請在執行應用程式時啟動 "hk" 設定檔。Spring Boot 將會同時載入 `appProperties.properties` 和 `appProperties-hk.properties`，且 `appProperties-hk.properties` 中的屬性會覆寫 `appProperties.properties` 中任何重複的屬性。

3. **如何啟動 "hk" 設定檔**
   - **透過命令列**：執行 Spring Boot 應用程式時，使用 `--spring.profiles.active` 參數指定啟動的設定檔。例如：
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     請將 `myapp.jar` 替換為您的 Maven 生成的應用程式 JAR 檔案名稱。

   - **透過 Maven**：如果您使用 `spring-boot:run` 目標執行應用程式，請在 `pom.xml` 中配置設定檔：
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
     然後執行：
     ```bash
     mvn spring-boot:run
     ```

   - **透過系統屬性**：將設定檔設定為 JVM 參數：
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **透過環境變數**：在您的環境中匯出設定檔（例如，在類 Unix 系統中）：
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### 運作原理
- 在 `application.properties` 中設定 `spring.config.name=appProperties` 後，Spring Boot 會使用 `appProperties` 作為配置檔案的基礎名稱。
- 當沒有啟動任何設定檔時，僅會載入 `appProperties.properties`。
- 當啟動 "hk" 設定檔時（例如透過 `--spring.profiles.active=hk`），Spring Boot 會同時載入 `appProperties.properties` 和 `appProperties-hk.properties`。如果存在重複的屬性，`appProperties-hk.properties` 中定義的屬性將優先於 `appProperties.properties` 中的屬性。

### 最終步驟
- 確保 `appProperties.properties` 和 `appProperties-hk.properties` 都位於 `src/main/resources` 目錄中。
- 將包含 `spring.config.name=appProperties` 的 `application.properties` 新增至 `src/main/resources`。
- 使用啟動的 "hk" 設定檔執行您的應用程式，以使用 `-hk` 屬性。

此方法符合 Spring Boot 的慣例，是在專案中控制使用哪個屬性檔案的典型且直接的方式。要特別使用 `-hk` 屬性，只需按照上述方式啟動 "hk" 設定檔即可。