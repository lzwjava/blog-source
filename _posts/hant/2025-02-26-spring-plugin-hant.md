---
audio: false
generated: true
lang: hant
layout: post
title: Spring Boot Maven 插件
translated: true
type: note
---

要在 Maven 基礎的 Spring Boot 專案中使用 `spring-boot-maven-plugin`，請按照以下步驟配置和使用該插件來建置、執行和管理您的應用程式。以下是完整指南：

---

### **1. 確認您的專案是 Spring Boot 專案**
在使用 `spring-boot-maven-plugin` 之前，請確認您的專案已設定為 Spring Boot 專案。這通常涉及：

- **繼承 `spring-boot-starter-parent`（推薦）**：
  - 在您的 `pom.xml` 中，將 `spring-boot-starter-parent` 設為父專案，以管理 Spring Boot 依賴項和插件版本。
  - 範例：
    ```xml
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.4</version> <!-- 請替換為您的 Spring Boot 版本 -->
        <relativePath/> <!-- 從儲存庫查找父專案 -->
    </parent>
    ```

- **或者，使用 `spring-boot-dependencies` BOM（物料清單）**：
  - 如果無法使用 `spring-boot-starter-parent`，請在 `dependencyManagement` 部分導入 `spring-boot-dependencies` BOM。
  - 範例：
    ```xml
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.5.4</version> <!-- 請替換為您的 Spring Boot 版本 -->
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    ```

推薦使用 `spring-boot-starter-parent`，因為它會自動管理插件版本，操作更簡單。

---

### **2. 將 `spring-boot-maven-plugin` 添加到您的 `pom.xml`**
要使用該插件，您需要在 `pom.xml` 的 `<build><plugins>` 部分聲明它。

- **如果使用 `spring-boot-starter-parent`**：
  - 添加插件時無需指定版本，因為父專案會管理版本。
  - 範例：
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
    ```

- **如果未使用 `spring-boot-starter-parent`**：
  - 請明確指定版本，並與使用的 Spring Boot 版本匹配。
  - 範例：
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.5.4</version> <!-- 請替換為您的 Spring Boot 版本 -->
            </plugin>
        </plugins>
    </build>
    ```

---

### **3. 使用插件目標**
`spring-boot-maven-plugin` 提供了多個目標來幫助建置、執行和管理您的 Spring Boot 應用程式。以下是最常用的目標：

- **`spring-boot:run`**
  - 使用嵌入式 Web 伺服器（例如 Tomcat）直接從 Maven 運行您的 Spring Boot 應用程式。
  - 適用於開發和測試。
  - 指令：
    ```
    mvn spring-boot:run
    ```

- **`spring-boot:repackage`**
  - 將 `mvn package` 生成的 JAR 或 WAR 檔案重新打包為包含所有依賴項的可執行「fat JAR」或 WAR。
  - 如果配置了該插件，此目標會在 `package` 階段自動執行。
  - 指令：
    ```
    mvn package
    ```
  - 運行後，您可以使用以下指令啟動應用程式：
    ```
    java -jar target/myapp.jar
    ```

- **`spring-boot:start` 和 `spring-boot:stop`**
  - 用於整合測試，分別在 `pre-integration-test` 和 `post-integration-test` 階段啟動和停止應用程式。
  - 範例：
    ```
    mvn spring-boot:start
    mvn spring-boot:stop
    ```

- **`spring-boot:build-info`**
  - 生成包含建置資訊（例如建置時間、版本）的 `build-info.properties` 檔案。
  - 此資訊可以在您的應用程式中使用 Spring Boot 的 `BuildProperties` bean 或 `@Value` 註解來訪問。
  - 指令：
    ```
    mvn spring-boot:build-info
    ```

---

### **4. 自訂插件配置（可選）**
您可以通過在 `pom.xml` 中添加配置選項來自訂 `spring-boot-maven-plugin` 的行為。以下是一些常見的自訂配置：

- **指定主類別**：
  - 如果插件無法自動檢測到主類別，請手動指定。
  - 範例：
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <mainClass>com.example.MyApplication</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```

- **從 Fat JAR 中排除依賴項**：
  - 排除由運行時環境（例如外部 servlet 容器）提供的依賴項。
  - 範例：
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>com.example</groupId>
                            <artifactId>some-dependency</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```

- **設定應用程式參數**：
  - 配置在運行 `spring-boot:run` 時傳遞給應用程式的參數。
  - 在 `pom.xml` 中的範例：
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <arguments>
                        <argument>--server.port=8081</argument>
                    </arguments>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```
  - 或者，通過指令行傳遞參數：
    ```
    mvn spring-boot:run -Dspring-boot.run.arguments=--server.port=8081
    ```

- **建置 WAR 檔案**：
  - 如果要建置 WAR 檔案以部署到外部 servlet 容器，請確保在 `pom.xml` 中將專案打包方式設定為 `war`：
    ```xml
    <packaging>war</packaging>
    ```
  - 您可能還需要排除嵌入式 servlet 容器（例如 Tomcat），如果它們由環境提供。請添加以下依賴項並將其範圍設為 `provided`：
    ```xml
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-tomcat</artifactId>
            <scope>provided</scope>
        </dependency>
    </dependencies>
    ```

---

### **5. 關鍵注意事項**
- **預設行為**：
  - 當您運行 `mvn package` 時，插件會在 `package` 階段自動重新打包 JAR/WAR，使其可執行。
  - 重新打包的成品是主要成品，原始的 JAR/WAR 會附加分類器（例如 `original`）。

- **開發工作流程**：
  - 使用 `mvn spring-boot:run` 進行快速開發和測試。
  - 使用 `mvn package` 來建置可部署的可執行 JAR 或 WAR。

- **整合測試**：
  - 使用 `spring-boot:start` 和 `spring-boot:stop` 在整合測試期間管理應用程式的生命週期。

---

### **總結**
要使用 `spring-boot-maven-plugin`：
1. 確保您的專案是 Spring Boot 專案，通常是通過繼承 `spring-boot-starter-parent` 或使用 `spring-boot-dependencies` BOM。
2. 將插件添加到您的 `pom.xml` 的 `<build><plugins>` 部分。
3. 使用 Maven 指令，例如：
   - `mvn spring-boot:run` 來運行應用程式。
   - `mvn package` 來建置可執行的 JAR/WAR。
   - 其他目標，如 `spring-boot:start`、`spring-boot:stop` 和 `spring-boot:build-info`，根據需要進行使用。
4. 可選地，在 `pom.xml` 中自訂插件的配置以滿足進階使用案例。

此設定使您能夠使用 Maven 高效地建置、執行和管理 Spring Boot 應用程式。