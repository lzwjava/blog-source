---
audio: false
generated: true
lang: ja
layout: post
title: Spring HTTPクライアント
translated: true
type: note
---

「FeignClient、Spring RestClient、Spring WebClientの使用方法」という質問に答えるために、これらのSpringツールを使用してHTTPリクエストを行う方法を、セットアップと基本的な使用法に焦点を当てて説明します。これらはすべてRESTfulサービスと対話するためのSpringエコシステムの一部ですが、アプリケーションのニーズに応じて異なる目的に使用されます。以下に、それぞれについて明確なステップバイステップガイドと簡単な例を示します。

---

### **1. FeignClientの使用**
FeignClientは、Spring Cloudが提供する宣言型のRESTクライアントです。アノテーションを使用してHTTPクライアントをインターフェースとして定義できるため、他のサービスを呼び出す必要があるマイクロサービスアーキテクチャで特に役立ちます。

#### **FeignClientを使用する手順**
1. **依存関係の追加**: プロジェクトにSpring Cloudの依存関係を含めます。Mavenを使用している場合は、`pom.xml`にFeign用のSpring Cloudスターターを追加します：
   ```xml
   <dependency>
       <groupId>org.springframework.cloud</groupId>
       <artifactId>spring-cloud-starter-openfeign</artifactId>
   </dependency>
   ```
   互換性のあるバージョンを指定したSpring Cloud用の依存関係管理ブロックも確実に含めてください。

2. **Feign Clientsの有効化**: メインアプリケーションクラスまたは設定クラスに`@EnableFeignClients`アノテーションを付けて、Feignサポートをアクティブにします：
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

3. **FeignClientインターフェースの定義**: `@FeignClient`アノテーションを付けたインターフェースを作成し、サービス名またはURLを指定し、RESTエンドポイントに対応するメソッドを定義します：
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
   ここで、`name`はクライアントの論理名、`url`はターゲットサービスのベースURLです。`@GetMapping`アノテーションは`/users`エンドポイントにマッピングされます。

4. **クライアントの注入と使用**: インターフェースをサービスまたはコントローラーにオートワイヤリングし、あたかもローカルであるかのようにそのメソッドを呼び出します：
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

#### **主なポイント**
- FeignClientはデフォルトで同期的です。
- サービスディスカバリー（例：Eureka）を使用するマイクロサービスに理想的です（`url`を省略し、Spring Cloudに解決させることができます）。
- フォールバックやサーキットブレーカー（例：HystrixやResilience4j）を使用してエラーハンドリングを追加できます。

---

### **2. Spring RestClientの使用**
Spring RestClientは、Spring Framework 6.1で導入された同期的なHTTPクライアントで、非推奨となった`RestTemplate`の現代的な代替手段です。リクエストの構築と実行のための流暢なAPIを提供します。

#### **RestClientを使用する手順**
1. **依存関係**: RestClientは`spring-web`に含まれており、これはSpring Bootの`spring-boot-starter-web`の一部です。通常、追加の依存関係は必要ありません：
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-web</artifactId>
   </dependency>
   ```

2. **RestClientインスタンスの作成**: 静的メソッド`create()`を使用して`RestClient`をインスタンス化するか、ビルダーでカスタマイズします：
   ```java
   import org.springframework.web.client.RestClient;

   RestClient restClient = RestClient.create();
   ```
   カスタム設定（例：タイムアウト）には、`RestClient.builder()`を使用します。

3. **リクエストの構築と実行**: 流暢なAPIを使用してHTTPメソッド、URI、ヘッダー、ボディを指定し、レスポンスを取得します：
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
   - `accept()`は期待するコンテンツタイプを設定します。
   - `retrieve()`はリクエストを実行し、`body()`はレスポンスを抽出します（リストのようなジェネリック型には`ParameterizedTypeReference`を使用します）。

4. **レスポンスの処理**: RestClientは同期的であるため、レスポンスは直接返されます。より制御が必要な場合（例：ステータスコード）、`toEntity()`を使用します：
   ```java
   import org.springframework.http.ResponseEntity;

   ResponseEntity<List<User>> response = restClient.get()
       .uri("http://localhost:8080/users")
       .accept(MediaType.APPLICATION_JSON)
       .retrieve()
       .toEntity(new ParameterizedTypeReference<List<User>>() {});
   List<User> users = response.getBody();
   ```

#### **主なポイント**
- RestClientは同期的であり、従来のブロッキングアプリケーションに適しています。
- HTTPエラー時に例外（例：`RestClientException`）をスローするため、キャッチして処理できます。
- `RestTemplate`のより直感的なAPIを備えた代替品です。

---

### **3. Spring WebClientの使用**
Spring WebClientは、Spring WebFluxで導入されたリアクティブでノンブロッキングなHTTPクライアントです。非同期操作向けに設計されており、リアクティブストリーム（MonoおよびFlux）と統合されます。

#### **WebClientを使用する手順**
1. **依存関係の追加**: プロジェクトにWebFluxの依存関係を含めます：
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-webflux</artifactId>
   </dependency>
   ```

2. **WebClientインスタンスの作成**: ベースURLまたはデフォルト設定で`WebClient`をインスタンス化します：
   ```java
   import org.springframework.web.reactive.function.client.WebClient;

   WebClient webClient = WebClient.create("http://localhost:8080");
   ```
   カスタム設定（例：コーデック、フィルター）には`WebClient.builder()`を使用します。

3. **リクエストの構築と実行**: 流暢なAPIを使用してリクエストを構築し、リアクティブなレスポンスを取得します：
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

4. **レスポンスのサブスクライブ**: WebClientはリアクティブであるため、リクエストをトリガーするには`Mono`または`Flux`をサブスクライブする必要があります：
   ```java
   Mono<List<User>> usersMono = fetchUsers();
   usersMono.subscribe(users -> System.out.println(users));
   ```
   あるいは、リアクティブパイプラインでチェーンするか、（リアクティブコンテキストでは推奨されませんが）ブロックします：
   ```java
   List<User> users = fetchUsers().block();
   ```

#### **主なポイント**
- WebClientはノンブロッキングであり、Spring WebFluxで構築されたリアクティブアプリケーションに理想的です。
- 単一値のレスポンスには`Mono`を、複数値のレスポンスには`Flux`を使用します。
- エラーハンドリングは、`onErrorResume()`や`retry()`のような演算子を使用して行うことができます。

---

### **比較とそれぞれを使用する場面**
- **FeignClient**: マイクロサービス設定における宣言的でインターフェースベースのクライアントに使用します。同期的であり、サービス間呼び出しを簡素化します。
- **RestClient**: 従来のブロッキングSpringアプリケーションにおける同期的なHTTPリクエストに使用します。`RestTemplate`の現代的な代替品です。
- **WebClient**: WebFluxベースのアプリケーション、または高同時実行性を扱う場合のリアクティブでノンブロッキングなHTTPリクエストに使用します。

---

### **例: POSTエンドポイントの呼び出し**
`User`オブジェクトを使用して`POST /users`を呼び出してユーザーを作成する必要があるとします。

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

### **結論**
- **FeignClient**: インターフェースを定義し、有効にして、ローカルビーンのように使用します。
- **RestClient**: リクエストを流暢に構築し、同期的にレスポンスを取得します。
- **WebClient**: リクエストを流暢に構築し、リアクティブストリームを取得し、非同期に処理します。

アプリケーションのアーキテクチャに基づいて選択してください：マイクロサービスにはFeignClient、ブロッキングアプリにはRestClient、リアクティブアプリにはWebClientを使用します。それぞれは、上記に示したように、 straightforward なセットアップと使用パターンに従います。