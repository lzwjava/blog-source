---
audio: false
generated: true
lang: ja
layout: post
title: スプリングHTTPクライアント
translated: true
---

クエリ「FeignClient、またはSpring RestClient、またはSpring WebClientの使い方」に答えるために、これらのSpringツールを使用してHTTPリクエストを作成する方法を説明します。これらのツールは、すべてSpringエコシステムの一部であり、RESTfulサービスとの相互作用に使用されますが、アプリケーションのニーズに応じて異なる目的を果たします。以下に、それぞれのツールの明確なステップバイステップガイドと簡単な例を提供します。

---

### **1. FeignClientの使用**
FeignClientは、Spring Cloudによって提供される宣言的なRESTクライアントです。インターフェースにアノテーションを付けることでHTTPクライアントを定義でき、特にマイクロサービスアーキテクチャで他のサービスを呼び出す際に便利です。

#### **FeignClientの使用手順**
1. **依存関係の追加**: プロジェクトにSpring Cloudの依存関係を追加します。Mavenを使用している場合は、`pom.xml`にSpring CloudのStarter for Feignを追加します:
   ```xml
   <dependency>
       <groupId>org.springframework.cloud</groupId>
       <artifactId>spring-cloud-starter-openfeign</artifactId>
   </dependency>
   ```
   Spring Cloudの互換バージョンを指定するための依存関係管理ブロックも確認してください。

2. **Feignクライアントの有効化**: メインアプリケーションクラスまたは設定クラスに`@EnableFeignClients`アノテーションを付けてFeignサポートを有効にします:
   ```java
   import org.springframework.boot.SpringApplication;
   import org.springframework.boot.autoconfigure.SpringBootApplication;
   import org.springframework.cloud.openfeign.EnableFeignClients;

   @SpringBootApplication
   @EnableFeignClients
   public class MyApplication {
       public static void main(String[] args) {
           SpringApplication.run(MyApplication.class, args);
       }
   }
   ```

3. **FeignClientインターフェースの定義**: `@FeignClient`アノテーションを付けたインターフェースを作成し、サービス名またはURLを指定し、RESTエンドポイントに対応するメソッドを定義します:
   ```java
   import org.springframework.cloud.openfeign.FeignClient;
   import org.springframework.web.bind.annotation.GetMapping;
   import java.util.List;

   @FeignClient(name = "user-service", url = "http://localhost:8080")
   public interface UserClient {
       @GetMapping("/users")
       List<User> getUsers();
   }
   ```
   ここで、`name`はクライアントの論理名であり、`url`はターゲットサービスのベースURLです。`@GetMapping`アノテーションは`/users`エンドポイントにマッピングされます。

4. **クライアントのインジェクトと使用**: サービスまたはコントローラーでインターフェースを自動ワイヤリングし、ローカルメソッドのように呼び出します:
   ```java
   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.stereotype.Service;
   import java.util.List;

   @Service
   public class UserService {
       @Autowired
       private UserClient userClient;

       public List<User> fetchUsers() {
           return userClient.getUsers();
       }
   }
   ```

#### **重要ポイント**
- FeignClientはデフォルトで同期です。
- サービスディスカバリー（例：Eureka）を使用するマイクロサービスで、`url`を省略し、Spring Cloudが解決するようにするのが理想的です。
- フォールバックやサーキットブレイカー（例：HystrixまたはResilience4j）を使用してエラーハンドリングを追加できます。

---

### **2. Spring RestClientの使用**
Spring RestClientは、Springフレームワーク6.1で導入された同期HTTPクライアントで、非推奨の`RestTemplate`の現代的な代替手段です。フルエントAPIを提供してリクエストの構築と実行を簡素化します。

#### **RestClientの使用手順**
1. **依存関係**: RestClientは`spring-web`に含まれており、Spring Bootの`spring-boot-starter-web`の一部です。通常、追加の依存関係は必要ありません:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-web</artifactId>
   </dependency>
   ```

2. **RestClientインスタンスの作成**: `RestClient`の静的`create()`メソッドを使用してインスタンスを作成するか、ビルダーを使用してカスタマイズします:
   ```java
   import org.springframework.web.client.RestClient;

   RestClient restClient = RestClient.create();
   ```
   カスタム設定（例：タイムアウト）には`RestClient.builder()`を使用します。

3. **リクエストの構築と実行**: フルエントAPIを使用してHTTPメソッド、URI、ヘッダー、ボディを指定し、応答を取得します:
   ```java
   import org.springframework.http.MediaType;
   import org.springframework.web.client.RestClient;
   import java.util.List;

   public class UserService {
       private final RestClient restClient;

       public UserService() {
           this.restClient = RestClient.create();
       }

       public List<User> fetchUsers() {
           return restClient.get()
               .uri("http://localhost:8080/users")
               .accept(MediaType.APPLICATION_JSON)
               .retrieve()
               .body(new ParameterizedTypeReference<List<User>>() {});
       }
   }
   ```
   - `get()`はHTTPメソッドを指定します。
   - `uri()`はエンドポイントを設定します。
   - `accept()`は期待されるコンテンツタイプを設定します。
   - `retrieve()`はリクエストを実行し、`body()`は応答を抽出し、ジェネリックタイプ（例：リスト）に対して`ParameterizedTypeReference`を使用します。

4. **応答の処理**: RestClientは同期なので、応答は直接返されます。より多くの制御（例：ステータスコード）が必要な場合は、`toEntity()`を使用します:
   ```java
   import org.springframework.http.ResponseEntity;

   ResponseEntity<List<User>> response = restClient.get()
       .uri("http://localhost:8080/users")
       .accept(MediaType.APPLICATION_JSON)
       .retrieve()
       .toEntity(new ParameterizedTypeReference<List<User>>() {});
   List<User> users = response.getBody();
   ```

#### **重要ポイント**
- RestClientは同期なので、伝統的なブロッキングアプリケーションに適しています。
- HTTPエラーが発生した場合に例外（例：`RestClientException`）をスローし、キャッチして処理できます。
- `RestTemplate`の代替手段で、より直感的なAPIを提供します。

---

### **3. Spring WebClientの使用**
Spring WebClientは、Spring WebFluxで導入された非同期、非ブロッキングHTTPクライアントです。非同期操作に設計されており、リアクティブストリーム（MonoとFlux）と統合されています。

#### **WebClientの使用手順**
1. **依存関係の追加**: プロジェクトにWebFluxの依存関係を追加します:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-webflux</artifactId>
   </dependency>
   ```

2. **WebClientインスタンスの作成**: ベースURLまたはデフォルト設定を使用して`WebClient`のインスタンスを作成します:
   ```java
   import org.springframework.web.reactive.function.client.WebClient;

   WebClient webClient = WebClient.create("http://localhost:8080");
   ```
   カスタム設定（例：コーデック、フィルター）には`WebClient.builder()`を使用します。

3. **リクエストの構築と実行**: フルエントAPIを使用してリクエストを構築し、リアクティブ応答を取得します:
   ```java
   import org.springframework.http.MediaType;
   import org.springframework.web.reactive.function.client.WebClient;
   import reactor.core.publisher.Mono;
   import java.util.List;

   public class UserService {
       private final WebClient webClient;

       public UserService(WebClient webClient) {
           this.webClient = webClient;
       }

       public Mono<List<User>> fetchUsers() {
           return webClient.get()
               .uri("/users")
               .accept(MediaType.APPLICATION_JSON)
               .retrieve()
               .bodyToFlux(User.class)
               .collectList();
       }
   }
   ```
   - `bodyToFlux(User.class)`は`User`オブジェクトのストリームを処理します。
   - `collectList()`は`Flux<User>`を`Mono<List<User>>`に変換します。

4. **応答のサブスクライブ**: WebClientはリアクティブなので、`Mono`または`Flux`にサブスクライブしてリクエストをトリガーする必要があります:
   ```java
   Mono<List<User>> usersMono = fetchUsers();
   usersMono.subscribe(users -> System.out.println(users));
   ```
   または、リアクティブパイプラインにチェーンするか、ブロック（リアクティブコンテキストでは推奨されません）します:
   ```java
   List<User> users = fetchUsers().block();
   ```

#### **重要ポイント**
- WebClientは非ブロッキングで、Spring WebFluxベースのリアクティブアプリケーションや高い並行性を扱う際に適しています。
- 単一値応答には`Mono`を、複数値応答には`Flux`を使用します。
- エラーハンドリングには`onErrorResume()`や`retry()`などの演算子を使用します。

---

### **比較と使用時のポイント**
- **FeignClient**: マイクロサービス設定でインターフェースベースの宣言的クライアントを使用します。同期で、サービス間の呼び出しを簡素化します。
- **RestClient**: 伝統的なブロッキングSpringアプリケーションでの同期HTTPリクエストに使用します。`RestTemplate`の現代的な代替手段です。
- **WebClient**: WebFluxベースのアプリケーションや高い並行性を扱う際の非同期、非ブロッキングHTTPリクエストに使用します。

---

### **例: POSTエンドポイントの呼び出し**
`POST /users`に`User`オブジェクトを送信してユーザーを作成する必要があるとします。

#### **FeignClient**
```java
@FeignClient(name = "user-service", url = "http://localhost:8080")
public interface UserClient {
    @PostMapping("/users")
    User createUser(@RequestBody User user);
}

@Service
public class UserService {
    @Autowired
    private UserClient userClient;

    public User createUser(User user) {
        return userClient.createUser(user);
    }
}
```

#### **RestClient**
```java
@Service
public class UserService {
    private final RestClient restClient = RestClient.create();

    public User createUser(User user) {
        return restClient.post()
            .uri("http://localhost:8080/users")
            .contentType(MediaType.APPLICATION_JSON)
            .body(user)
            .retrieve()
            .body(User.class);
    }
}
```

#### **WebClient**
```java
@Service
public class UserService {
    private final WebClient webClient;

    public UserService(WebClient webClient) {
        this.webClient = WebClient.create("http://localhost:8080");
    }

    public Mono<User> createUser(User user) {
        return webClient.post()
            .uri("/users")
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(user)
            .retrieve()
            .bodyToMono(User.class);
    }
}
```

---

### **まとめ**
- **FeignClient**: インターフェースを定義し、有効にし、ローカルビーンのように使用します。
- **RestClient**: フルエントAPIを使用してリクエストを構築し、応答を同期的に取得します。
- **WebClient**: フルエントAPIを使用してリクエストを構築し、リアクティブストリームを取得し、非同期で処理します。

アプリケーションのアーキテクチャに応じて選択してください: マイクロサービスにはFeignClient、ブロッキングアプリにはRestClient、リアクティブアプリにはWebClientを使用します。それぞれの設定と使用パターンは上記のように簡単です。