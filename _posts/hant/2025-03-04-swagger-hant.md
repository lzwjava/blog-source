---
audio: false
generated: true
lang: hant
layout: post
title: Swagger 註解
translated: true
type: note
---

要在你的 Java 專案中使用 `swagger-annotations` 套件（特別是用於為使用 Spring Boot 建構的 REST API 編寫文件），請按照以下步驟操作。本指南假設你使用的是 Swagger 2.0，它通常與 `springfox` 函式庫整合。`swagger-annotations` 套件提供了為你的 API 端點添加元數據的註解，從而實現 API 文件的自動生成。

---

### 步驟 1：添加必要的依賴項

你需要在專案中包含 `swagger-annotations` 套件和一個 Swagger 整合函式庫（例如 `springfox`）。如果你使用 Maven，請將以下依賴項添加到你的 `pom.xml` 中：

```xml
<!-- Swagger Annotations -->
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-annotations</artifactId>
    <version>1.6.2</version>
</dependency>

<!-- Springfox Swagger 2 for Swagger Integration -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>

<!-- Springfox Swagger UI for Interactive Documentation -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.9.2</version>
</dependency>
```

- **`io.swagger:swagger-annotations`**：提供 Swagger 2.0 的註解。
- **`springfox-swagger2`**：將 Swagger 與 Spring Boot 整合並處理註解。
- **`springfox-swagger-ui`**：添加一個網頁界面來查看生成的文件。

> **注意**：請在 [Maven Repository](https://mvnrepository.com/) 上檢查最新版本，因為這些版本（`swagger-annotations` 的 1.6.2 和 `springfox` 的 2.9.2）可能已有更新。

---

### 步驟 2：在你的應用程式中配置 Swagger

要啟用 Swagger 並允許它掃描你的 API 以尋找註解，請建立一個帶有 `Docket` bean 的配置類別。將此類別添加到你的 Spring Boot 應用程式中：

```java
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableSwagger2
public class SwaggerConfig {
    @Bean
    public Docket api() {
        return new Docket(DocumentationType.SWAGGER_2)
                .select()
                .apis(RequestHandlerSelectors.any()) // 掃描所有控制器
                .paths(PathSelectors.any())          // 包含所有路徑
                .build();
    }
}
```

- **`@EnableSwagger2`**：啟用 Swagger 2.0 支援。
- **`Docket`**：配置要記錄文件的端點。上述設定會掃描所有控制器和路徑，但你可以自定義它（例如，`RequestHandlerSelectors.basePackage("com.example.controllers")`）以限制範圍。

---

### 步驟 3：在你的程式碼中使用 Swagger 註解

`swagger-annotations` 套件提供了用於描述你的 API 的註解。將這些註解應用於你的控制器類別、方法、參數和模型。以下是一些常見的註解及其範例：

#### 為控制器添加註解

使用 `@Api` 來描述控制器：

```java
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "User Controller", description = "Operations pertaining to users")
@RestController
@RequestMapping("/users")
public class UserController {
    // 方法放在這裡
}
```

- **`value`**：API 的簡短名稱。
- **`description`**：對控制器功能的簡要說明。

#### 為 API 操作添加註解

使用 `@ApiOperation` 來描述各個端點：

```java
import io.swagger.annotations.ApiOperation;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Get a user by ID", response = User.class)
@GetMapping("/{id}")
public ResponseEntity<User> getUserById(@PathVariable Long id) {
    // 實作
    return ResponseEntity.ok(new User(id, "John Doe"));
}
```

- **`value`**：操作的摘要。
- **`response`**：預期的返回類型。

#### 描述參數

使用方法參數的 `@ApiParam`：

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@ApiOperation(value = "Create a new user")
@PostMapping
public ResponseEntity<User> createUser(
        @ApiParam(value = "User object to be created", required = true) 
        @RequestBody User user) {
    // 實作
    return ResponseEntity.ok(user);
}
```

- **`value`**：描述參數。
- **`required`**：指示參數是否為必需。

#### 指定回應

使用 `@ApiResponses` 和 `@ApiResponse` 來記錄可能的 HTTP 回應：

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.ApiResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Delete a user")
@ApiResponses(value = {
    @ApiResponse(code = 200, message = "User deleted successfully"),
    @ApiResponse(code = 404, message = "User not found")
})
@DeleteMapping("/{id}")
public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
    // 實作
    return ResponseEntity.ok().build();
}
```

- **`code`**：HTTP 狀態碼。
- **`message`**：回應的描述。

#### 描述模型

對於資料傳輸物件（DTO），使用 `@ApiModel` 和 `@ApiModelProperty`：

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(description = "User data transfer object")
public class User {
    @ApiModelProperty(notes = "The user's unique identifier", example = "1")
    private Long id;

    @ApiModelProperty(notes = "The user's name", example = "John Doe")
    private String name;

    // Getters and setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public User(Long id, String name) {
        this.id = id;
        this.name = name;
    }
}
```

- **`@ApiModel`**：描述模型。
- **`@ApiModelProperty`**：詳細說明每個欄位，可選擇性地提供範例。

---

### 步驟 4：運行並訪問文件

1.  啟動你的 Spring Boot 應用程式。
2.  打開瀏覽器並導航至：  
    **http://localhost:8080/swagger-ui.html**  
    此 URL 會顯示 Swagger UI，這是一個互動式界面，根據註解顯示你的 API 文件。

---

### 如何使用 `swagger-annotations` 的總結

1.  **添加依賴項**：在 `pom.xml` 中包含 `swagger-annotations` 和 `springfox`。
2.  **配置 Swagger**：設定一個 `Docket` bean 以啟用 Swagger 掃描。
3.  **為你的程式碼添加註解**：
    - `@Api` 用於控制器。
    - `@ApiOperation` 用於方法。
    - `@ApiParam` 用於參數。
    - `@ApiResponses` 和 `@ApiResponse` 用於回應詳細資訊。
    - `@ApiModel` 和 `@ApiModelProperty` 用於 DTOs。
4.  **查看文件**：在 `/swagger-ui.html` 訪問 Swagger UI。

---

### 補充說明

- **Swagger 2.0 vs. OpenAPI 3.0**：本指南使用 Swagger 2.0 和 `io.swagger:swagger-annotations`。對於 OpenAPI 3.0，請使用 `io.swagger.core.v3:swagger-annotations` 和像 `springdoc-openapi` 這樣的函式庫，這會改變一些註解名稱（例如，使用 `@Tag` 代替 `@Api`）。
- **自定義**：調整 `Docket` 配置以過濾特定的套件或路徑，以獲得更有針對性的文件。
- **品質**：在註解中提供清晰、詳細的描述，以提高生成文件的實用性。

通過遵循這些步驟，你可以有效地使用 `swagger-annotations` 套件來為你的 REST API 編寫文件，使開發人員和使用者更容易理解和與你的端點互動。