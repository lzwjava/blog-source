---
audio: false
generated: true
lang: ja
layout: post
title: スプリング データ REST モジュール
translated: true
---

**spring-data-rest-core** を使用するには、Spring Data REST モジュールを利用して、Spring Data リポジトリをアプリケーションの RESTful エンドポイントとして公開することができます。以下は、その手順を示した完全なガイドです。

---

### 1. Spring Data REST の依存関係を追加する
Spring Data REST を使用するには、プロジェクトにその依存関係を含める必要があります。Spring Boot を使用している場合（一般的なシナリオ）は、ビルドファイルに次の依存関係を追加します。

- **Maven**:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-data-rest</artifactId>
  </dependency>
  ```

- **Gradle**:
  ```gradle
  implementation 'org.springframework.boot:spring-boot-starter-data-rest'
  ```

このスターターは、`spring-data-rest-core` と他の必要なコンポーネントを一緒に含みます。Spring Boot 以外のプロジェクトでは、`spring-data-rest-core` を直接含めることもできますが、Spring Boot スターターを使用することをお勧めします。

---

### 2. エンティティを定義する
JPA（Java Persistence API）などの永続化技術を使用してエンティティクラスを定義し、ドメインモデルを作成します。例えば：

```java
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.GeneratedValue;

@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;
    private String name;

    // コンストラクタ
    public User() {}
    public User(String name) {
        this.name = name;
    }

    // ゲッターとセッター
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

この `User` エンティティは、データベース内の `id` と `name` を持つシンプルなテーブルを表します。

---

### 3. リポジトリインターフェースを作成する
エンティティ用のリポジトリインターフェースを定義し、Spring Data のリポジトリインターフェースの一つ（例えば、`JpaRepository`）を拡張します。例えば：

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
```

`JpaRepository` を拡張することで、基本的な CRUD（作成、読み取り、更新、削除）操作を無料で取得します。Spring Data REST は、このリポジトリを自動的に RESTful エンドポイントとして公開します。

---

### 4. アプリケーションを実行する
依存関係を追加し、エンティティとリポジトリを定義したら、Spring Boot アプリケーションを起動します。Spring Data REST は、リポジトリに基づいて REST エンドポイントを自動的に生成します。上記の `UserRepository` の場合、以下のエンドポイントにアクセスできます：

- **GET /users**: すべてのユーザーを取得します。
- **GET /users/{id}**: ID によって特定のユーザーを取得します。
- **POST /users**: 新しいユーザーを作成します（JSON ペイロード、例えば `{"name": "Alice"}`）。
- **PUT /users/{id}**: 既存のユーザーを更新します。
- **DELETE /users/{id}**: ユーザーを削除します。

例えば、アプリケーションが `localhost:8080` で実行されている場合、`curl` やブラウザを使用してテストできます：

```bash
curl http://localhost:8080/users
```

応答には HATEOAS リンクが含まれ、クライアントが関連リソースを動的にナビゲートできるようになります。

---

### 5. （オプション）REST エンドポイントをカスタマイズする
リポジトリが公開される方法をアノテーションまたは設定を使用してカスタマイズできます。

- **エンドポイントパスを変更する**:
  `@RepositoryRestResource` アノテーションを使用してカスタムパスを指定します：
  ```java
  import org.springframework.data.rest.core.annotation.RepositoryRestResource;

  @RepositoryRestResource(path = "people")
  public interface UserRepository extends JpaRepository<User, Long> {
  }
  ```
  これで、エンドポイントは `/people` ではなくなります。

- **グローバル設定を構成する**:
  `RepositoryRestConfigurer` を実装してベースパスや他の設定をカスタマイズします：
  ```java
  import org.springframework.data.rest.webmvc.config.RepositoryRestConfigurer;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.data.rest.core.config.RepositoryRestConfiguration;

  @Configuration
  public class RestConfig implements RepositoryRestConfigurer {
      @Override
      public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config) {
          config.setBasePath("/api"); // すべてのエンドポイントは /api で始まります
      }
  }
  ```
  これで、ユーザーは `/api/users` でアクセス可能になります。

---

### Spring Data REST の主要機能
- **HATEOAS サポート**: 応答には関連リソースへのハイパーメディアリンクが含まれます。
- **ページネーションとソート**: クエリパラメータ（例えば `?page=0&size=10&sort=name,asc`）を使用して結果をページ分けおよびソートします。
- **フィルタリング**: リポジトリにカスタムクエリメソッド（例えば `findByName(String name)`）を追加して追加のエンドポイントを公開します。

---

### まとめ
`spring-data-rest-core` を使用するには：
1. Spring Data REST の依存関係を含めます（例えば、Spring Boot の場合は `spring-boot-starter-data-rest`）。
2. 適切なアノテーション（例えば、JPA の場合は `@Entity`）を使用してエンティティを定義します。
3. Spring Data のインターフェース（例えば `JpaRepository`）を拡張するリポジトリインターフェースを作成します。
4. アプリケーションを実行して自動生成された REST エンドポイントにアクセスします。
5. 必要に応じてエンドポイントのパスや動作をカスタマイズします。

このアプローチにより、Spring Data REST のコア機能を活用して、最小限のコードで迅速に RESTful API を構築できます。