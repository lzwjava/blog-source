---
audio: false
generated: true
lang: ja
layout: post
title: Spring Data RESTモジュール
translated: true
type: note
---

**spring-data-rest-core**を使用するには、Spring Data RESTモジュールを活用して、Spring Dataリポジトリをアプリケーション内でRESTfulエンドポイントとして公開できます。以下に、始めるための完全なステップバイステップガイドを示します：

---

### 1. Spring Data RESTの依存関係を追加する
Spring Data RESTを使用するには、プロジェクトにその依存関係を含める必要があります。**Spring Boot**を使用している場合（一般的なシナリオ）、ビルドファイルに次の依存関係を追加してください：

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

このスターターは、`spring-data-rest-core`と他の必要なコンポーネントを一緒に取り込みます。Spring Bootを使用しないプロジェクトでは、`spring-data-rest-core`を直接含めることもできますが、シンプルさのためにSpring Bootスターターを使用することを推奨します。

---

### 2. エンティティを定義する
JPA（Java Persistence API）のような永続化技術を使用してエンティティクラスを定義し、ドメインモデルを作成します。例：

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

この`User`エンティティは、`id`と`name`を持つデータベース内の単純なテーブルを表します。

---

### 3. リポジトリインターフェースを作成する
Spring Dataのリポジトリインターフェース（例：`JpaRepository`）を拡張して、エンティティのリポジトリインターフェースを定義します。例：

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
```

`JpaRepository`を拡張することで、基本的なCRUD（作成、読み取り、更新、削除）操作を無償で取得できます。Spring Data RESTはこのリポジトリを自動的にRESTfulエンドポイントとして公開します。

---

### 4. アプリケーションを実行する
依存関係を追加し、エンティティとリポジトリを定義したら、Spring Bootアプリケーションを起動します。Spring Data RESTはリポジトリに基づいてRESTエンドポイントを自動生成します。上記の`UserRepository`の場合、以下にアクセスできます：

- **GET /users**: すべてのユーザーのリストを取得します。
- **GET /users/{id}**: IDで特定のユーザーを取得します。
- **POST /users**: 新しいユーザーを作成します（JSONペイロード例：`{"name": "Alice"}`）。
- **PUT /users/{id}**: 既存のユーザーを更新します。
- **DELETE /users/{id}**: ユーザーを削除します。

例えば、アプリケーションが`localhost:8080`で実行されている場合、`curl`やブラウザなどのツールを使用してテストできます：

```bash
curl http://localhost:8080/users
```

レスポンスにはHATEOASリンクが含まれており、クライアントが関連リソースを動的にナビゲートできるようになります。

---

### 5. （オプション）RESTエンドポイントをカスタマイズする
アノテーションや設定を使用して、リポジトリの公開方法をカスタマイズできます：

- **エンドポイントパスの変更**:
  `@RepositoryRestResource`アノテーションを使用してカスタムパスを指定します：
  ```java
  import org.springframework.data.rest.core.annotation.RepositoryRestResource;

  @RepositoryRestResource(path = "people")
  public interface UserRepository extends JpaRepository<User, Long> {
  }
  ```
  これで、エンドポイントは`/users`ではなく`/people`になります。

- **グローバル設定の構成**:
  `RepositoryRestConfigurer`を実装してベースパスやその他の設定をカスタマイズします：
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
  これにより、ユーザーは`/api/users`でアクセス可能になります。

---

### Spring Data RESTの主な機能
- **HATEOASサポート**: レスポンスには関連リソースへのハイパーメディアリンクが含まれます。
- **ページネーションとソート**: `?page=0&size=10&sort=name,asc`のようなクエリパラメータを使用して結果のページネーションとソートを行います。
- **フィルタリング**: リポジトリにカスタムクエリメソッド（例：`findByName(String name)`）を追加して、追加のエンドポイントを公開します。

---

### まとめ
`spring-data-rest-core`を使用するには：
1. Spring Data RESTの依存関係（例：Spring Bootの場合は`spring-boot-starter-data-rest`）を含めます。
2. 適切なアノテーション（例：JPAの場合は`@Entity`）でエンティティを定義します。
3. Spring Dataインターフェース（例：`JpaRepository`）を拡張するリポジトリインターフェースを作成します。
4. アプリケーションを実行して、自動生成されたRESTエンドポイントにアクセスします。
5. 必要に応じて、エンドポイントのパスや動作をカスタマイズします。

このアプローチにより、最小限のコードでRESTful APIを迅速に構築でき、Spring Data RESTのコア機能を活用できます。