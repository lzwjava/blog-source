---
audio: false
generated: true
lang: zh
layout: post
title: Swagger 注解
translated: true
---

要在 Java 项目中使用 `swagger-annotations` 包，特别是用于文档化使用 Spring Boot 构建的 REST API，请按照以下步骤进行操作。本指南假设您使用的是 Swagger 2.0，它通常与 `springfox` 库集成。`swagger-annotations` 包提供了注解，用于为 API 端点添加元数据，从而实现自动生成 API 文档。

---

### 第 1 步：添加所需的依赖

您需要在项目中包含 `swagger-annotations` 包和一个 Swagger 集成库（例如 `springfox`）。如果您使用的是 Maven，请将以下依赖项添加到您的 `pom.xml`：

```xml
<!-- Swagger 注解 -->
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-annotations</artifactId>
    <version>1.6.2</version>
</dependency>

<!-- Springfox Swagger 2 用于 Swagger 集成 -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>

<!-- Springfox Swagger UI 用于交互式文档 -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.9.2</version>
</dependency>
```

- **`io.swagger:swagger-annotations`**：提供 Swagger 2.0 的注解。
- **`springfox-swagger2`**：将 Swagger 与 Spring Boot 集成并处理注解。
- **`springfox-swagger-ui`**：添加一个 Web 界面以查看生成的文档。

> **注意**：请在 [Maven 仓库](https://mvnrepository.com/) 上检查最新版本，因为这些版本（`swagger-annotations` 的 1.6.2 和 `springfox` 的 2.9.2）可能有更新。

---

### 第 2 步：在应用程序中配置 Swagger

要启用 Swagger 并允许它扫描 API 以查找注解，请创建一个包含 `Docket` bean 的配置类。将其添加到您的 Spring Boot 应用程序中：

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
                .apis(RequestHandlerSelectors.any()) // 扫描所有控制器
                .paths(PathSelectors.any())          // 包括所有路径
                .build();
    }
}
```

- **`@EnableSwagger2`**：激活 Swagger 2.0 支持。
- **`Docket`**：配置要文档化的端点。上述设置扫描所有控制器和路径，但您可以自定义它（例如，`RequestHandlerSelectors.basePackage("com.example.controllers")`）以限制范围。

---

### 第 3 步：在代码中使用 Swagger 注解

`swagger-annotations` 包提供了注解来描述您的 API。将这些注解应用到控制器类、方法、参数和模型中。以下是常见注解及其示例：

#### 注解控制器

使用 `@Api` 来描述控制器：

```java
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "用户控制器", description = "与用户相关的操作")
@RestController
@RequestMapping("/users")
public class UserController {
    // 方法在此处
}
```

- **`value`**：API 的简短名称。
- **`description`**：控制器的简要说明。

#### 注解 API 操作

使用 `@ApiOperation` 来描述单个端点：

```java
import io.swagger.annotations.ApiOperation;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "通过 ID 获取用户", response = User.class)
@GetMapping("/{id}")
public ResponseEntity<User> getUserById(@PathVariable Long id) {
    // 实现
    return ResponseEntity.ok(new User(id, "John Doe"));
}
```

- **`value`**：操作的摘要。
- **`response`**：预期的返回类型。

#### 描述参数

使用 `@ApiParam` 为方法参数：

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@ApiOperation(value = "创建新用户")
@PostMapping
public ResponseEntity<User> createUser(
        @ApiParam(value = "要创建的用户对象", required = true)
        @RequestBody User user) {
    // 实现
    return ResponseEntity.ok(user);
}
```

- **`value`**：描述参数。
- **`required`**：指示参数是否必需。

#### 指定响应

使用 `@ApiResponses` 和 `@ApiResponse` 来文档化可能的 HTTP 响应：

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.ApiResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "删除用户")
@ApiResponses(value = {
    @ApiResponse(code = 200, message = "用户删除成功"),
    @ApiResponse(code = 404, message = "用户未找到")
})
@DeleteMapping("/{id}")
public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
    // 实现
    return ResponseEntity.ok().build();
}
```

- **`code`**：HTTP 状态代码。
- **`message`**：响应的描述。

#### 描述模型

对于数据传输对象（DTO），使用 `@ApiModel` 和 `@ApiModelProperty`：

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(description = "用户数据传输对象")
public class User {
    @ApiModelProperty(notes = "用户的唯一标识符", example = "1")
    private Long id;

    @ApiModelProperty(notes = "用户的名称", example = "John Doe")
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
- **`@ApiModelProperty`**：详细说明每个字段，可选示例。

---

### 第 4 步：运行并访问文档

1. 启动您的 Spring Boot 应用程序。
2. 打开浏览器并导航到：
   **http://localhost:8080/swagger-ui.html**
   此 URL 显示 Swagger UI，这是一个交互式界面，显示基于注解的 API 文档。

---

### 如何使用 `swagger-annotations` 的总结

1. **添加依赖**：在 `pom.xml` 中包含 `swagger-annotations` 和 `springfox`。
2. **配置 Swagger**：设置一个 `Docket` bean 以启用 Swagger 扫描。
3. **注解您的代码**：
   - 使用 `@Api` 为控制器。
   - 使用 `@ApiOperation` 为方法。
   - 使用 `@ApiParam` 为参数。
   - 使用 `@ApiResponses` 和 `@ApiResponse` 为响应详细信息。
   - 使用 `@ApiModel` 和 `@ApiModelProperty` 为 DTO。
4. **查看文档**：在 `/swagger-ui.html` 访问 Swagger UI。

---

### 附加说明

- **Swagger 2.0 与 OpenAPI 3.0**：本指南使用 Swagger 2.0 与 `io.swagger:swagger-annotations`。对于 OpenAPI 3.0，使用 `io.swagger.core.v3:swagger-annotations` 和类似 `springdoc-openapi` 的库，这会更改一些注解名称（例如，`@Tag` 而不是 `@Api`）。
- **自定义**：调整 `Docket` 配置以过滤特定包或路径，以获得更专注的文档。
- **质量**：在注解中提供清晰、详细的描述，以提高生成文档的有用性。

通过遵循这些步骤，您可以有效地使用 `swagger-annotations` 包来文档化您的 REST API，使开发人员和消费者更容易理解和与您的端点进行交互。