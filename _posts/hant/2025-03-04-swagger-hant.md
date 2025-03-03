---
audio: false
generated: true
lang: hant
layout: post
title: Swagger 註釋
translated: true
---

要在 Java 專案中使用 `swagger-annotations` 套件，特別是為了文檔化使用 Spring Boot 建立的 REST API，請按照以下步驟進行。本指南假設您使用的是 Swagger 2.0，這通常與 `springfox` 圖書館一起整合。`swagger-annotations` 套件提供了註釋來為您的 API 端點添加元數據，從而實現自動生成 API 文檔。

---

### 第 1 步：添加所需的依賴

您需要在項目中包含 `swagger-annotations` 套件和一個 Swagger 整合圖書館（例如 `springfox`）。如果您使用的是 Maven，請將以下依賴添加到您的 `pom.xml`：

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

- **`io.swagger:swagger-annotations`**：提供 Swagger 2.0 的註釋。
- **`springfox-swagger2`**：將 Swagger 與 Spring Boot 整合並處理註釋。
- **`springfox-swagger-ui`**：添加一個網頁界面來查看生成的文檔。

> **注意**：請在 [Maven Repository](https://mvnrepository.com/) 上檢查最新版本，因為這些版本（`swagger-annotations` 的 1.6.2 和 `springfox` 的 2.9.2）可能有更新。

---

### 第 2 步：在應用程序中配置 Swagger

要啟用 Swagger 並讓它掃描您的 API 以獲取註釋，請創建一個包含 `Docket` bean 的配置類。將其添加到您的 Spring Boot 應用程序中：

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
                .apis(RequestHandlerSelectors.any()) // 檢查所有控制器
                .paths(PathSelectors.any())          // 包括所有路徑
                .build();
    }
}
```

- **`@EnableSwagger2`**：啟用 Swagger 2.0 支持。
- **`Docket`**：配置要文檔化的端點。上述設置掃描所有控制器和路徑，但您可以自定義它（例如，`RequestHandlerSelectors.basePackage("com.example.controllers")`）以限制範圍。

---

### 第 3 步：在代碼中使用 Swagger 注釋

`swagger-annotations` 套件提供了註釋來描述您的 API。將這些註釋應用到您的控制器類、方法、參數和模型。以下是一些常見的註釋及其示例：

#### 注釋控制器

使用 `@Api` 來描述控制器：

```java
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "User Controller", description = "與用戶相關的操作")
@RestController
@RequestMapping("/users")
public class UserController {
    // 方法在此處
}
```

- **`value`**：API 的簡短名稱。
- **`description`**：控制器的簡要說明。

#### 注釋 API 操作

使用 `@ApiOperation` 來描述單個端點：

```java
import io.swagger.annotations.ApiOperation;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "按 ID 获取用戶", response = User.class)
@GetMapping("/{id}")
public ResponseEntity<User> getUserById(@PathVariable Long id) {
    // 實現
    return ResponseEntity.ok(new User(id, "John Doe"));
}
```

- **`value`**：操作的摘要。
- **`response`**：預期的返回類型。

#### 描述參數

使用 `@ApiParam` 來描述方法參數：

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@ApiOperation(value = "創建新用戶")
@PostMapping
public ResponseEntity<User> createUser(
        @ApiParam(value = "要創建的用戶對象", required = true)
        @RequestBody User user) {
    // 實現
    return ResponseEntity.ok(user);
}
```

- **`value`**：描述參數。
- **`required`**：指示參數是否必需。

#### 指定響應

使用 `@ApiResponses` 和 `@ApiResponse` 來文檔化可能的 HTTP 响應：

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.ApiResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "刪除用戶")
@ApiResponses(value = {
    @ApiResponse(code = 200, message = "用戶刪除成功"),
    @ApiResponse(code = 404, message = "找不到用戶")
})
@DeleteMapping("/{id}")
public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
    // 實現
    return ResponseEntity.ok().build();
}
```

- **`code`**：HTTP 狀態碼。
- **`message`**：響應的描述。

#### 描述模型

對於數據傳輸對象（DTO），使用 `@ApiModel` 和 `@ApiModelProperty`：

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(description = "用戶數據傳輸對象")
public class User {
    @ApiModelProperty(notes = "用戶的唯一標識符", example = "1")
    private Long id;

    @ApiModelProperty(notes = "用戶的名稱", example = "John Doe")
    private String name;

    // Getters 和 setters
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
- **`@ApiModelProperty`**：詳細說明每個字段，可選擇性地提供示例。

---

### 第 4 步：運行並訪問文檔

1. 啟動您的 Spring Boot 應用程序。
2. 打開瀏覽器並導航到：
   **http://localhost:8080/swagger-ui.html**
   此 URL 顯示 Swagger UI，這是一個互動界面，顯示基於註釋生成的 API 文檔。

---

### 如何使用 `swagger-annotations` 的總結

1. **添加依賴**：在 `pom.xml` 中包含 `swagger-annotations` 和 `springfox`。
2. **配置 Swagger**：設置一個 `Docket` bean 以啟用 Swagger 掃描。
3. **註釋您的代碼**：
   - 使用 `@Api` 來註釋控制器。
   - 使用 `@ApiOperation` 來註釋方法。
   - 使用 `@ApiParam` 來註釋參數。
   - 使用 `@ApiResponses` 和 `@ApiResponse` 來註釋響應詳細信息。
   - 使用 `@ApiModel` 和 `@ApiModelProperty` 來註釋 DTO。
4. **查看文檔**：在 `/swagger-ui.html` 訪問 Swagger UI。

---

### 附加說明

- **Swagger 2.0 與 OpenAPI 3.0**：本指南使用 Swagger 2.0 及其 `io.swagger:swagger-annotations`。對於 OpenAPI 3.0，請使用 `io.swagger.core.v3:swagger-annotations` 和類似 `springdoc-openapi` 的圖書館，這些圖書館會改變一些註釋名稱（例如，`@Tag` 而不是 `@Api`）。
- **自定義**：調整 `Docket` 配置以篩選特定包或路徑，以獲取更專注的文檔。
- **質量**：在註釋中提供清晰、詳細的說明，以提高生成文檔的有用性。

通過遵循這些步驟，您可以有效地使用 `swagger-annotations` 套件來文檔化您的 REST API，使開發人員和消費者更容易理解和與您的端點進行交互。