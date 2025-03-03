---
audio: false
generated: true
lang: ja
layout: post
title: スワガーアノテーション
translated: true
---

`swagger-annotations` パッケージをJavaプロジェクトで使用し、特にSpring Bootで構築されたREST APIのドキュメント化を行うには、以下の手順に従ってください。このガイドでは、Swagger 2.0を使用していることを前提としています。Swagger 2.0は、`springfox`ライブラリと共に一般的に統合されます。`swagger-annotations`パッケージは、APIエンドポイントにメタデータを追加するためのアノテーションを提供し、APIドキュメントの自動生成を可能にします。

---

### ステップ1: 必要な依存関係を追加する

プロジェクトに`swagger-annotations`パッケージとSwagger統合ライブラリ（例：`springfox`）を含める必要があります。Mavenを使用している場合、`pom.xml`に以下の依存関係を追加します：

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

- **`io.swagger:swagger-annotations`**: Swagger 2.0用のアノテーションを提供します。
- **`springfox-swagger2`**: SwaggerをSpring Bootと統合し、アノテーションを処理します。
- **`springfox-swagger-ui`**: 生成されたドキュメントを表示するためのWebインターフェースを追加します。

> **注意**: [Mavenリポジトリ](https://mvnrepository.com/)で最新バージョンを確認してください。これらのバージョン（`swagger-annotations`の1.6.2および`springfox`の2.9.2）には更新が含まれている可能性があります。

---

### ステップ2: アプリケーションでSwaggerを設定する

Swaggerを有効にし、APIのアノテーションをスキャンするために、`Docket`ビーンを含む設定クラスを作成します。これをSpring Bootアプリケーションに追加します：

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
                .apis(RequestHandlerSelectors.any()) // すべてのコントローラをスキャン
                .paths(PathSelectors.any())          // すべてのパスを含める
                .build();
    }
}
```

- **`@EnableSwagger2`**: Swagger 2.0のサポートを有効にします。
- **`Docket`**: ドキュメント化するエンドポイントを設定します。上記の設定では、すべてのコントローラとパスをスキャンしますが、範囲を制限するためにカスタマイズできます（例：`RequestHandlerSelectors.basePackage("com.example.controllers")`）。

---

### ステップ3: コードでSwaggerアノテーションを使用する

`swagger-annotations`パッケージは、APIを説明するためのアノテーションを提供します。これらをコントローラークラス、メソッド、パラメータ、モデルに適用します。以下に一般的なアノテーションと例を示します：

#### コントローラのアノテーション

`@Api`を使用してコントローラを説明します：

```java
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "User Controller", description = "ユーザーに関連する操作")
@RestController
@RequestMapping("/users")
public class UserController {
    // メソッドはここに
}
```

- **`value`**: APIの短い名前。
- **`description`**: コントローラが何をするかの簡単な説明。

#### API操作のアノテーション

`@ApiOperation`を使用して個々のエンドポイントを説明します：

```java
import io.swagger.annotations.ApiOperation;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "IDでユーザーを取得", response = User.class)
@GetMapping("/{id}")
public ResponseEntity<User> getUserById(@PathVariable Long id) {
    // 実装
    return ResponseEntity.ok(new User(id, "John Doe"));
}
```

- **`value`**: 操作の概要。
- **`response`**: 期待される返却型。

#### パラメータの説明

メソッドパラメータには`@ApiParam`を使用します：

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@ApiOperation(value = "新しいユーザーを作成")
@PostMapping
public ResponseEntity<User> createUser(
        @ApiParam(value = "作成するユーザーオブジェクト", required = true)
        @RequestBody User user) {
    // 実装
    return ResponseEntity.ok(user);
}
```

- **`value`**: パラメータを説明します。
- **`required`**: パラメータが必須かどうかを示します。

#### レスポンスの指定

`@ApiResponses`および`@ApiResponse`を使用して、可能なHTTPレスポンスをドキュメント化します：

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.ApiResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "ユーザーを削除")
@ApiResponses(value = {
    @ApiResponse(code = 200, message = "ユーザーが正常に削除されました"),
    @ApiResponse(code = 404, message = "ユーザーが見つかりません")
})
@DeleteMapping("/{id}")
public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
    // 実装
    return ResponseEntity.ok().build();
}
```

- **`code`**: HTTPステータスコード。
- **`message`**: レスポンスの説明。

#### モデルの説明

データ転送オブジェクト（DTO）には、`@ApiModel`および`@ApiModelProperty`を使用します：

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(description = "ユーザーデータ転送オブジェクト")
public class User {
    @ApiModelProperty(notes = "ユーザーの一意の識別子", example = "1")
    private Long id;

    @ApiModelProperty(notes = "ユーザーの名前", example = "John Doe")
    private String name;

    // ゲッターとセッター
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

- **`@ApiModel`**: モデルを説明します。
- **`@ApiModelProperty`**: 各フィールドの詳細を示し、オプションで例を提供します。

---

### ステップ4: ドキュメントを実行してアクセスする

1. Spring Bootアプリケーションを起動します。
2. ブラウザを開き、以下のURLにアクセスします：
   **http://localhost:8080/swagger-ui.html**
   このURLには、アノテーションに基づいて生成されたAPIドキュメントを表示するSwagger UIが表示されます。

---

### `swagger-annotations`の使用方法のまとめ

1. **依存関係を追加**: `swagger-annotations`および`springfox`を`pom.xml`に含めます。
2. **Swaggerを設定**: Swaggerスキャンを有効にするために`Docket`ビーンを設定します。
3. **コードにアノテーションを適用**:
   - コントローラには`@Api`を使用。
   - メソッドには`@ApiOperation`を使用。
   - パラメータには`@ApiParam`を使用。
   - レスポンスの詳細には`@ApiResponses`および`@ApiResponse`を使用。
   - DTOには`@ApiModel`および`@ApiModelProperty`を使用。
4. **ドキュメントを表示**: `/swagger-ui.html`でSwagger UIにアクセスします。

---

### 追加の注意

- **Swagger 2.0対OpenAPI 3.0**: このガイドでは、Swagger 2.0と`io.swagger:swagger-annotations`を使用しています。OpenAPI 3.0の場合は、`io.swagger.core.v3:swagger-annotations`および`springdoc-openapi`のようなライブラリを使用し、アノテーション名が変更される場合があります（例：`@Tag`の代わりに`@Api`）。
- **カスタマイズ**: `Docket`設定を調整して、特定のパッケージやパスをフィルタリングし、より集中したドキュメントを作成します。
- **品質**: アノテーションに明確で詳細な説明を提供して、生成されたドキュメントの有用性を向上させます。

これらの手順に従うことで、`swagger-annotations`パッケージを使用してREST APIのドキュメント化を行い、開発者や消費者がエンドポイントを理解しやすくすることができます。