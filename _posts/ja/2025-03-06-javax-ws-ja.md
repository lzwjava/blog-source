---
audio: false
generated: true
lang: ja
layout: post
title: 'Java API for RESTful Web Services


  Java API for RESTful Web Services'
translated: true
---

`javax.ws.rs` を使用するには、Java API for RESTful Web Services（一般的には JAX-RS と呼ばれます）を使用してプロジェクトを設定し、RESTful リソースを定義し、アプリケーションを構成し、デプロイする一連の手順を実行する必要があります。JAX-RS を使用すると、REST アーキテクチャスタイルに従う Web サービスを作成し、アノテーションを使用してエンドポイントを定義し、HTTP リクエストを処理できます。以下は、あなたが始めるための包括的なガイドです。

---

### **1. プロジェクトの設定**
`javax.ws.rs` を使用するには、JAX-RS API と実装（`javax.ws.rs` は仕様であり、ランタイムではありません）を含める必要があります。人気のある実装は Jersey です。Maven を使用している場合は、`pom.xml` に必要な依存関係を追加します。

#### **依存関係**
```xml
<!-- JAX-RS API -->
<dependency>
    <groupId>javax.ws.rs</groupId>
    <artifactId>javax.ws.rs-api</artifactId>
    <version>2.1.1</version>
</dependency>

<!-- Jersey 実装（コア依存関係を含む） -->
<dependency>
    <groupId>org.glassfish.jersey.bundles</groupId>
    <artifactId>jaxrs-ri</artifactId>
    <version>2.34</version>
</dependency>

<!-- オプション：Jackson を使用した JSON サポート -->
<dependency>
    <groupId>org.glassfish.jersey.media</groupId>
    <artifactId>jersey-media-json-jackson</artifactId>
    <version>2.34</version>
</dependency>
```

- `javax.ws.rs-api` は、JAX-RS のコア アノテーションとクラスを提供します。
- `jaxrs-ri` バンドルには、Jersey 実装とその依存関係が含まれています。
- `jersey-media-json-jackson` モジュール（オプション）は、JSON シリアライズ/デシリアライズのサポートを追加します。

プロジェクトがサーブレット コンテナ（例：Tomcat）または Java EE サーバーで設定されていることを確認してください。JAX-RS アプリケーションは、通常、このような環境で実行されます。または、軽量サーバーである Grizzly を使用してスタンドアロンで実行することもできます（後で詳しく説明します）。

---

### **2. RESTful リソースの作成**
JAX-RS での RESTful サービスは、`@Path` と HTTP メソッド アノテーション（例：`@GET`、`@POST` など）でアノテーションされたリソースクラスで定義されます。以下は、シンプルなリソースの例です。

#### **例：HelloResource.java**
```java
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/hello")
public class HelloResource {

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String sayHello() {
        return "Hello, World!";
    }
}
```

- **`@Path("/hello")`**：このリソースの URI パスを指定します（例：`http://localhost:8080/api/hello`）。
- **`@GET`**：このメソッドが HTTP GET リクエストを処理することを示します。
- **`@Produces(MediaType.TEXT_PLAIN)`**：応答がプレーンテキストであることを指定します。

GET リクエストが `/hello` に行われると、このメソッドは `"Hello, World!"` を返します。

---

### **3. JAX-RS アプリケーションの構成**
JAX-RS ランタイムにどのリソースを含めるかを教える必要があります。これは、`javax.ws.rs.core.Application` を拡張するアプリケーション構成クラスを作成することで行います。

#### **例：MyApplication.java**
```java
import javax.ws.rs.ApplicationPath;
import javax.ws.rs.core.Application;
import java.util.HashSet;
import java.util.Set;

@ApplicationPath("/api")
public class MyApplication extends Application {

    @Override
    public Set<Class<?>> getClasses() {
        Set<Class<?>> classes = new HashSet<>();
        classes.add(HelloResource.class);
        return classes;
    }
}
```

- **`@ApplicationPath("/api")`**：すべてのリソースのベース URI パスを定義します（例：`/api/hello`）。
- **`getClasses()`**：アプリケーションに含めるリソースクラスのセットを返します。

現代的なサーブレット コンテナ（Servlet 3.0+）では、このアノテーションベースの構成が十分であり、`web.xml` ファイルが必要ないことが多いです。

---

### **4. 異なる HTTP メソッドとパラメータの処理**
JAX-RS は、さまざまな HTTP メソッド、メディアタイプ、パラメータを処理するためのアノテーションを提供します。

#### **例：POST リクエストの処理**
```java
import javax.ws.rs.POST;
import javax.ws.rs.Consumes;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@POST
@Consumes(MediaType.APPLICATION_JSON)
public Response createItem(MyItem item) {
    // アイテムを処理するロジック
    return Response.status(Response.Status.CREATED).build();
}
```

- **`@POST`**：HTTP POST リクエストを処理します。
- **`@Consumes(MediaType.APPLICATION_JSON)`**：JSON 入力を期待し、それを `MyItem` オブジェクトにデシリアライズします。
- **`Response`**：201 Created ステータスを返します。

#### **例：パスパラメータ**
```java
import javax.ws.rs.PathParam;
import javax.ws.rs.Path;

@GET
@Path("/{id}")
@Produces(MediaType.APPLICATION_JSON)
public MyItem getItem(@PathParam("id") String id) {
    // ID でアイテムを取得するロジック
    return new MyItem(id);
}
```

- **`@Path("/{id}")`**：パスパラメータを定義します（例：`/hello/123`）。
- **`@PathParam("id")`**：URI から `id` 値を注入します。

#### **例：クエリパラメータ**
```java
import javax.ws.rs.QueryParam;

@GET
@Produces(MediaType.APPLICATION_JSON)
public List<MyItem> getItems(@QueryParam("category") String category) {
    // カテゴリーでアイテムをフィルタリングするロジック
    return itemList;
}
```

- **`@QueryParam("category")`**：クエリ文字列から `category` 値を取得します（例：`/hello?category=books`）。

---

### **5. アプリケーションのデプロイ**
JAX-RS アプリケーションをサーブレット コンテナ（例：Tomcat）にデプロイできます。

1. プロジェクトを WAR ファイルにパッケージ化します（例：`mvn package`）。
2. WAR ファイルをコンテナにデプロイします。
3. 設定された URI（例：`http://localhost:8080/your-app/api/hello`）でサービスにアクセスします。

開発またはスタンドアロン使用のために、Jersey を使用してプログラムでアプリケーションを実行することもできます。

#### **例：スタンドアロン メイン**
```java
import org.glassfish.jersey.grizzly2.httpserver.GrizzlyHttpServerFactory;
import org.glassfish.jersey.server.ResourceConfig;
import java.net.URI;

public class Main {
    public static void main(String[] args) {
        URI baseUri = URI.create("http://localhost:8080/api/");
        ResourceConfig config = new ResourceConfig(HelloResource.class);
        GrizzlyHttpServerFactory.createHttpServer(baseUri, config);
        System.out.println("Server running at " + baseUri);
    }
}
```

これにより、完全なサーブレット コンテナなしで HTTP サーバーが起動します。

---

### **6. 追加機能**
- **例外処理**：`ExceptionMapper` を使用して例外を優雅に処理します。
  ```java
  import javax.ws.rs.NotFoundException;
  import javax.ws.rs.core.Response;
  import javax.ws.rs.ext.ExceptionMapper;
  import javax.ws.rs.ext.Provider;

  @Provider
  public class NotFoundExceptionMapper implements ExceptionMapper<NotFoundException> {
      @Override
      public Response toResponse(NotFoundException exception) {
          return Response.status(Response.Status.NOT_FOUND).build();
      }
  }
  ```
- **依存関係注入**：`@Context` を使用して `UriInfo` などのオブジェクトを注入するか、実装の DI フレームワーク（例：Jersey の HK2）に依存します。
- **テスト**：Postman や Jersey Test Framework などのツールを使用してエンドポイントをテストします。

---

### **まとめ**
`javax.ws.rs` を使用するには、プロジェクトに JAX-RS API と Jersey などの実装を含め、パスと HTTP メソッドのアノテーションを使用してリソースクラスを定義し、アプリケーションを構成（`Application` サブクラスまたは `web.xml` を使用）し、サーブレット コンテナにデプロイするかスタンドアロンで実行します。これにより、Java を使用して効率的に RESTful Web サービスを構築できます。