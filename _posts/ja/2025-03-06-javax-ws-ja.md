---
audio: false
generated: true
lang: ja
layout: post
title: RESTful WebサービスのためのJava API
translated: true
type: note
---

`javax.ws.rs`（一般的にJAX-RSとして知られるRESTful WebサービスのためのJava API）を使用するには、プロジェクトのセットアップ、RESTfulリソースの定義、アプリケーションの設定、デプロイといった一連の手順を踏む必要があります。JAX-RSでは、アノテーションを使用してエンドポイントを定義し、HTTPリクエストを処理する、RESTアーキテクチャスタイルに準拠したWebサービスを作成できます。以下に、始めるための包括的なガイドを示します：

---

### **1. プロジェクトのセットアップ**
`javax.ws.rs`を使用するには、JAX-RS APIとその実装（`javax.ws.rs`は仕様でありランタイムではないため）を含める必要があります。人気のある実装の一つがJerseyです。Mavenを使用している場合は、必要な依存関係を`pom.xml`に追加します：

#### **依存関係**
```xml
<!-- JAX-RS API -->
<dependency>
    <groupId>javax.ws.rs</groupId>
    <artifactId>javax.ws.rs-api</artifactId>
    <version>2.1.1</version>
</dependency>

<!-- Jersey Implementation (コア依存関係を含む) -->
<dependency>
    <groupId>org.glassfish.jersey.bundles</groupId>
    <artifactId>jaxrs-ri</artifactId>
    <version>2.34</version>
</dependency>

<!-- オプション: Jacksonを使用したJSONサポート -->
<dependency>
    <groupId>org.glassfish.jersey.media</groupId>
    <artifactId>jersey-media-json-jackson</artifactId>
    <version>2.34</version>
</dependency>
```

- `javax.ws.rs-api`は、コアとなるJAX-RSのアノテーションとクラスを提供します。
- `jaxrs-ri`バンドルは、Jerseyの実装とその依存関係を含みます。
- `jersey-media-json-jackson`モジュール（オプション）は、JSONのシリアライゼーション/デシリアライゼーションのサポートを追加します。

JAX-RSアプリケーションは通常、このような環境で実行されるため、プロジェクトがサーブレットコンテナ（例：Tomcat）またはJava EEサーバーでセットアップされていることを確認してください。あるいは、後述するように、Grizzlyのような軽量サーバーを使用してスタンドアロンで実行することもできます。

---

### **2. RESTfulリソースの作成**
JAX-RSにおけるRESTfulサービスは、`@Path`および`@GET`、`@POST`などのHTTPメソッドアノテーションで注釈が付けられたリソースクラスを使用して定義されます。以下は、シンプルなリソースの例です：

#### **例: HelloResource.java**
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

- **`@Path("/hello")`**: このリソースのURIパスを指定します（例: `http://localhost:8080/api/hello`）。
- **`@GET`**: このメソッドがHTTP GETリクエストを処理することを示します。
- **`@Produces(MediaType.TEXT_PLAIN)`**: レスポンスがプレーンテキストになることを指定します。

`/hello`へのGETリクエストが行われると、このメソッドは`"Hello, World!"`を返します。

---

### **3. JAX-RSアプリケーションの設定**
どのリソースを含めるかをJAX-RSランタイムに伝える必要があります。これは、`javax.ws.rs.core.Application`を拡張するアプリケーション設定クラスを作成することで行えます。

#### **例: MyApplication.java**
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

- **`@ApplicationPath("/api")`**: すべてのリソースのベースURIパスを定義します（例: `/api/hello`）。
- **`getClasses()`**: アプリケーションに含めるリソースクラスのセットを返します。

モダンなサーブレットコンテナ（Servlet 3.0+）では、このアノテーションベースの設定で十分なことが多く、`web.xml`ファイルは必要ない場合があります。

---

### **4. 様々なHTTPメソッドとパラメータの処理**
JAX-RSは、様々なHTTPメソッド、メディアタイプ、パラメータを処理するためのアノテーションを提供します。

#### **例: POSTリクエストの処理**
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

- **`@POST`**: HTTP POSTリクエストを処理します。
- **`@Consumes(MediaType.APPLICATION_JSON)`**: JSON入力を期待し、`MyItem`オブジェクトにデシリアライズされます。
- **`Response`**: 201 Createdステータスを返します。

#### **例: パスパラメータ**
```java
import javax.ws.rs.PathParam;
import javax.ws.rs.Path;

@GET
@Path("/{id}")
@Produces(MediaType.APPLICATION_JSON)
public MyItem getItem(@PathParam("id") String id) {
    // IDでアイテムを取得するロジック
    return new MyItem(id);
}
```

- **`@Path("/{id}")`**: パスパラメータを定義します（例: `/hello/123`）。
- **`@PathParam("id")`**: URIから`id`の値を注入します。

#### **例: クエリパラメータ**
```java
import javax.ws.rs.QueryParam;

@GET
@Produces(MediaType.APPLICATION_JSON)
public List<MyItem> getItems(@QueryParam("category") String category) {
    // カテゴリでアイテムをフィルタリングするロジック
    return itemList;
}
```

- **`@QueryParam("category")`**: クエリ文字列から`category`の値を取得します（例: `/hello?category=books`）。

---

### **5. アプリケーションのデプロイ**
TomcatのようなサーブレットコンテナにJAX-RSアプリケーションをデプロイできます：

1. プロジェクトをWARファイルとしてパッケージ化します（例: `mvn package`を使用）。
2. WARファイルをコンテナにデプロイします。
3. 設定されたURI（例: `http://localhost:8080/your-app/api/hello`）でサービスにアクセスします。

あるいは、開発時やスタンドアロンでの使用のために、JerseyとGrizzlyを使用してプログラムでアプリケーションを実行できます：

#### **例: スタンドアロンメイン**
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

これにより、完全なサーブレットコンテナなしでHTTPサーバーが起動します。

---

### **6. 追加機能**
- **例外処理**: `ExceptionMapper`を使用して例外を適切に処理します。
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
- **依存性注入**: `@Context`を使用して`UriInfo`などのオブジェクトを注入するか、実装のDIフレームワーク（例：JerseyのHK2）を利用します。
- **テスト**: PostmanやJersey Test Frameworkなどのツールを使用してエンドポイントをテストします。

---

### **まとめ**
`javax.ws.rs`を使用するには、プロジェクトにJAX-RS APIとJerseyのような実装を含め、パスとHTTPメソッドのアノテーションを持つリソースクラスを定義し、（`Application`サブクラスまたは`web.xml`を介して）アプリケーションを設定し、サーブレットコンテナにデプロイするか、スタンドアロンで実行します。これにより、Javaで効率的にRESTful Webサービスを構築できます。