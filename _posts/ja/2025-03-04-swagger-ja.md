---
audio: false
generated: true
lang: ja
layout: post
title: Swaggerアノテーション
translated: true
type: note
---

Javaプロジェクトで`swagger-annotations`パッケージを使用するには、特にSpring Bootで構築されたREST APIを文書化する場合、以下の手順に従ってください。このガイドは、`springfox`ライブラリと統合されることが一般的なSwagger 2.0を使用していることを前提としています。`swagger-annotations`パッケージは、APIエンドポイントにメタデータを追加するアノテーションを提供し、APIドキュメントの自動生成を可能にします。

---

### ステップ1: 必要な依存関係を追加する

プロジェクトに`swagger-annotations`パッケージとSwagger統合ライブラリ（例: `springfox`）を含める必要があります。Mavenを使用している場合は、`pom.xml`に以下の依存関係を追加してください：

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

- **`io.swagger:swagger-annotations`**: Swagger 2.0のアノテーションを提供します。
- **`springfox-swagger2`**: SwaggerをSpring Bootと統合し、アノテーションを処理します。
- **`springfox-swagger-ui`**: 生成されたドキュメントを表示するWebインターフェースを追加します。

> **注意**: これらのバージョン（`swagger-annotations`の1.6.2と`springfox`の2.9.2）は更新されている可能性があるため、[Maven Repository](https://mvnrepository.com/)で最新バージョンを確認してください。

---

### ステップ2: アプリケーションでSwaggerを設定する

Swaggerを有効にしてAPIのアノテーションをスキャンできるようにするには、`Docket` Beanを含む設定クラスを作成します。これをSpring Bootアプリケーションに追加してください：

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
                .apis(RequestHandlerSelectors.any()) // すべてのコントローラーをスキャン
                .paths(PathSelectors.any())          // すべてのパスを含める
                .build();
    }
}
```

- **`@EnableSwagger2`**: Swagger 2.0サポートを有効にします。
- **`Docket`**: ドキュメント化するエンドポイントを設定します。上記の設定はすべてのコントローラーとパスをスキャンしますが、スコープを制限するようにカスタマイズできます（例: `RequestHandlerSelectors.basePackage("com.example.controllers")`）。

---

### ステップ3: コードでSwaggerアノテーションを使用する

`swagger-annotations`パッケージは、APIを記述するアノテーションを提供します。これらをコントローラークラス、メソッド、パラメータ、モデルに適用してください。以下は一般的なアノテーションと例です：

#### コントローラーのアノテーション

`@Api`を使用してコントローラーを記述します：

```java
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "User Controller", description = "ユーザーに関連する操作")
@RestController
@RequestMapping("/users")
public class UserController {
    // メソッドをここに記述
}
```

- **`value`**: APIの短い名前。
- **`description`**: コントローラーの機能の簡単な説明。

#### API操作のアノテーション

`@ApiOperation`を使用して個々のエンドポイントを記述します：

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
- **`response`**: 期待される戻り値の型。

#### パラメータの記述

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

- **`value`**: パラメータの説明。
- **`required`**: パラメータが必須かどうかを示します。

#### レスポンスの指定

`@ApiResponses`と`@ApiResponse`を使用して可能なHTTPレスポンスを文書化します：

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

#### モデルの記述

データ転送オブジェクト（DTO）には、`@ApiModel`と`@ApiModelProperty`を使用します：

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(description = "ユーザーデータ転送オブジェクト")
public class User {
    @ApiModelProperty(notes = "ユーザーの一意な識別子", example = "1")
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

- **`@ApiModel`**: モデルを記述します。
- **`@ApiModelProperty`**: 各フィールドの詳細を、オプションの例とともに記述します。

---

### ステップ4: ドキュメントを実行してアクセスする

1. Spring Bootアプリケーションを起動します。
2. ブラウザを開き、以下に移動します：  
   **http://localhost:8080/swagger-ui.html**  
   このURLは、アノテーションに基づいてAPIドキュメントを表示する対話型インターフェースであるSwagger UIを表示します。

---

### `swagger-annotations`の使用方法のまとめ

1. **依存関係の追加**: `pom.xml`に`swagger-annotations`と`springfox`を含めます。
2. **Swaggerの設定**: Swaggerスキャンを有効にする`Docket` Beanを設定します。
3. **コードへのアノテーション適用**:
   - コントローラーには`@Api`
   - メソッドには`@ApiOperation`
   - パラメータには`@ApiParam`
   - レスポンスの詳細には`@ApiResponses`と`@ApiResponse`
   - DTOには`@ApiModel`と`@ApiModelProperty`
4. **ドキュメントの表示**: `/swagger-ui.html`でSwagger UIにアクセスします。

---

### 追加の注意点

- **Swagger 2.0 vs. OpenAPI 3.0**: このガイドは`io.swagger:swagger-annotations`を使用したSwagger 2.0を使用しています。OpenAPI 3.0の場合は、`io.swagger.core.v3:swagger-annotations`と`springdoc-openapi`のようなライブラリを使用し、いくつかのアノテーション名が変更されます（例: `@Api`の代わりに`@Tag`）。
- **カスタマイズ**: 特定のパッケージやパスをフィルタリングして、より焦点を絞ったドキュメントにするために`Docket`設定を調整します。
- **品質**: 生成されたドキュメントの有用性を高めるために、アノテーションに明確で詳細な説明を提供してください。

これらの手順に従うことで、`swagger-annotations`パッケージを効果的に使用してREST APIを文書化し、開発者や利用者がエンドポイントを理解し対話することを容易にすることができます。