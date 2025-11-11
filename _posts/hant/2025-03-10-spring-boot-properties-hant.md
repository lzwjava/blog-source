---
audio: false
generated: true
lang: hant
layout: post
title: Spring Boot 屬性運作原理
translated: true
type: note
---

讓我們來探索 Spring Boot 中屬性的運作方式，包括如何使用 YAML 或 `.properties` 檔案、如何透過命令列參數（如 `-D`）覆寫屬性、各種初始化屬性的方法，以及如何有效測試它們。

---

### **Spring Boot 中屬性的運作方式**
Spring Boot 透過屬性（鍵值對）提供靈活的應用程式配置管理系統。這些屬性可以從多個來源定義，Spring Boot 會根據特定的優先順序來解析它們。這讓您可以針對不同環境或部署情境自訂應用程式。屬性會被載入到 **Spring Environment** 中，使其在整個應用程式中都可存取。

屬性的主要來源包括：
- 配置檔案（例如 `application.properties` 或 `application.yml`）
- 命令列參數（例如 `--server.port=8081`）
- 系統屬性（例如 `-Dserver.port=8081`）
- 環境變數
- Java 程式碼（例如透過 `@Value` 或 `@ConfigurationProperties`）

---

### **使用 YAML 或 Properties 檔案**
Spring Boot 支援兩種主要的配置檔案格式，通常都放在 `src/main/resources` 目錄下：

#### **1. `.properties` 檔案**
這是一種簡單的扁平鍵值對格式：
```properties
server.port=8080
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
```

#### **2. `.yml` 或 `.yaml` 檔案**
這是一種使用縮排的結構化階層格式：
```yaml
server:
  port: 8080
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
```

**重點：**
- 簡單配置使用 `.properties`，巢狀或複雜設定使用 `.yml`。
- 可以使用環境特定的設定檔檔案（例如 `application-dev.yml`）。
- 範例：設定 `server.port=8080` 會變更 Spring Boot 應用程式運行的埠號。

---

### **使用命令列參數覆寫屬性**
您可以透過兩種方式使用命令列參數來覆寫配置檔案中定義的屬性：

#### **1. 使用 `--` 設定 Spring Boot 屬性**
在運行應用程式時直接傳遞屬性：
```bash
java -jar myapp.jar --server.port=8081 --spring.datasource.url=jdbc:mysql://localhost:3306/testdb
```
這些參數的優先順序高於配置檔案。

#### **2. 使用 `-D` 設定系統屬性**
使用 `-D` 設定系統屬性，Spring Boot 也會識別：
```bash
java -Dserver.port=8081 -Dspring.datasource.url=jdbc:mysql://localhost:3306/testdb -jar myapp.jar
```
系統屬性也會覆寫配置檔案中的值。

---

### **初始化屬性的不同方式**
除了檔案和命令列參數，Spring Boot 還提供多種定義或初始化屬性的方法：

#### **1. 環境變數**
可以透過環境變數設定屬性。例如：
- 在環境中設定 `SERVER_PORT=8081`，Spring Boot 會將其映射到 `server.port`。
- **命名慣例：** 將屬性名稱轉換為大寫，並將點（`.`）替換為底線（`_`），例如 `spring.datasource.url` 變成 `SPRING_DATASOURCE_URL`。

#### **2. Java 程式碼**
您可以透過程式設計方式初始化屬性：
- **使用 `@Value`**：將特定屬性注入到欄位中。
  ```java
  @Value("${server.port}")
  private int port;
  ```
- **使用 `@ConfigurationProperties`**：將一組屬性綁定到 Java 物件。
  ```java
  @Component
  @ConfigurationProperties(prefix = "app")
  public class AppProperties {
      private String name;
      // getters and setters
  }
  ```
  這會將像 `app.name` 這樣的屬性綁定到 `name` 欄位。

#### **3. 預設值**
如果屬性未定義，可以提供後備值：
- 在 `@Value` 中：`@Value("${server.port:8080}")` 如果 `server.port` 未設定，則使用 `8080`。
- 在配置檔案中：在 `application.properties` 或 YAML 中設定預設值。

---

### **屬性優先順序**
Spring Boot 會按以下順序從多個來源解析屬性（優先順序高的覆寫低的）：
1. 命令列參數（`--property=value`）
2. 系統屬性（`-Dproperty=value`）
3. 環境變數
4. 配置檔案（`application.properties` 或 `application.yml`）
5. 程式碼中的預設值

**範例：** 如果 `application.properties` 中有 `server.port=8080`，但您運行 `java -jar myapp.jar --server.port=8081`，則埠號將會是 `8081`。

---

### **如何測試屬性**
測試屬性能確保您的應用程式行為符合預期。以下是常見的方法：

#### **1. 使用 `@TestPropertySource`**
在單元測試中覆寫屬性：
```java
@SpringBootTest
@TestPropertySource(properties = {"server.port=9090"})
public class MyTest {
    // 測試程式碼
}
```

#### **2. 使用 `application-test.properties`**
將測試專用的檔案放在 `src/test/resources` 目錄下：
```properties
server.port=9090
```
Spring Boot 在測試期間會自動載入此檔案。

#### **3. 程式設計覆寫**
在測試設定中設定屬性：
```java
@SpringBootTest
public class MyTest {
    @BeforeEach
    public void setup() {
        System.setProperty("server.port", "9090");
    }
}
```

#### **4. 使用 `@ActiveProfiles`**
啟用設定檔專用的屬性：
- 定義帶有測試設定的 `application-test.yml`。
- 使用：
  ```java
  @SpringBootTest
  @ActiveProfiles("test")
  public class MyTest {
      // 測試程式碼
  }
  ```

---

### **總結**
- **配置檔案**：使用 `application.properties` 或 `application.yml` 進行預設設定。
- **命令列參數**：使用 `--property=value` 或 `-Dproperty=value` 進行覆寫。
- **初始化方法**：利用環境變數、Java 程式碼（`@Value`、`@ConfigurationProperties`）或預設值。
- **測試**：使用 `@TestPropertySource`、測試專用檔案、程式設計覆寫或設定檔。

這涵蓋了在 Spring Boot 中使用屬性的基本知識。如果您需要更多詳細資訊，請告訴我！