---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Spring BootでのH2データベーステスト
translated: true
type: note
---

### Spring BootのJUnitテストでH2データベースを使用する

H2は軽量なインメモリデータベースで、特にSpring Bootを使用したJavaアプリケーションの単体テストや統合テストに最適です。外部データベースの設定が不要なため、テストを迅速に実行できます。以下は、Spring BootプロジェクトでJPA/Hibernateを使用する場合のステップバイステップガイドです。Springを使用していない場合は、プレーンなJDBCでH2を利用できます（末尾の注記を参照）。

#### ステップ1: H2依存関係の追加
`pom.xml`（Maven）または`build.gradle`（Gradle）にH2の依存関係を追加します。本番環境での組み込みを避けるため、スコープを`test`に設定します。

**Maven (`pom.xml`):**
```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>test</scope>
</dependency>
```

**Gradle (`build.gradle`):**
```gradle
testImplementation 'com.h2database:h2'
```

これにより、テスト実行時のみH2のJARが取得されます。

#### ステップ2: テストプロパティでのH2設定
`src/test/resources/application.properties`（または`application-test.yml`）を作成または更新し、H2を指すように設定します。これにより、本番環境のデータベース設定が上書きされます。

**application.properties:**
```
# H2データベース設定
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# H2コンソール（オプション、デバッグ用）
spring.h2.console.enabled=true

# JPA/Hibernate設定
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true
```

- `mem:testdb`: 「testdb」という名前のインメモリデータベース
- `create-drop`: 起動時にテーブルを自動作成し、シャットダウン時に削除
- テスト中に`http://localhost:8080/h2-console`でH2コンソールを有効化（JDBC URL: `jdbc:h2:mem:testdb`を使用）

プロファイルを使用する場合は、テストクラスで`@ActiveProfiles("test")`を指定して有効化します。

#### ステップ3: JUnitテストの作成
完全なコンテキストが必要な場合は`@SpringBootTest`を、リポジトリに焦点を当てたテストの場合は`@DataJpaTest`を使用します。`@Test`で注釈し、JUnit 5（`@ExtendWith(SpringExtension.class)`）を使用します。

**例: JPAリポジトリのテスト**
`User`のような`Entity`と、`JpaRepository`を継承した`UserRepository`があると仮定します。

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.ActiveProfiles;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest  // JPA関連のBeanのみを読み込み、高速なテストを実現
@ActiveProfiles("test")  // テストプロファイルを有効化
public class UserRepositoryTest {

    @Autowired
    private UserRepository userRepository;

    @Test
    public void shouldSaveAndFindUser() {
        // 前提条件
        User user = new User("John Doe", "john@example.com");
        userRepository.save(user);

        // 実行
        User foundUser = userRepository.findByEmail("john@example.com").orElse(null);

        // 検証
        assertThat(foundUser).isNotNull();
        assertThat(foundUser.getName()).isEqualTo("John Doe");
    }
}
```

- `@DataJpaTest`: H2を自動設定し、各テスト後にトランザクションをロールバック
- 検証には`AssertJ`または`JUnit`のアサーションを使用
- サービス層のテストには`@SpringBootTest`を使用し、サービス/リポジトリを注入

`mvn test`またはIDEのテストランナーで実行します。各テストは新しいデータベースで開始されます。

#### ステップ4: 高度なヒント
- **Flyway/Liquibaseマイグレーション**: スキーママイグレーションを使用する場合は、`src/test/resources`に追加するとH2が適用します
- **現実的なテスト**: H2はほとんどのSQL方言を模倣しますが、本番環境（例: PostgreSQL）との差異がある場合があります。より正確なテストには、Testcontainersと実際のデータベースコンテナの使用を検討してください
- **本番設定の除外**: `pom.xml`でプロファイルを使用し、テストでの実際のデータベースドライバーを除外します:
  ```xml
  <profile>
      <id>test</id>
      <dependencies>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-data-jpa</artifactId>
              <exclusions>
                  <exclusion>
                      <groupId>mysql</groupId>  <!-- または本番DB -->
                      <artifactId>mysql-connector-java</artifactId>
                  </exclusion>
              </exclusions>
          </dependency>
      </dependencies>
  </profile>
  ```
- **トラブルシューティング**: テストが本番データベースを使用する場合は、`spring.profiles.active=test`を確認するか、`@TestPropertySource`を使用してください

#### スタンドアロンJUnit（Springなし）
Springを使用しないプレーンなJDBCの場合:
1. 上記のようにH2依存関係を追加
2. テストで以下のように実装:
```java
import org.h2.jdbcx.JdbcDataSource;
import org.junit.jupiter.api.Test;

public class StandaloneH2Test {
    @Test
    public void testH2Connection() throws Exception {
        JdbcDataSource ds = new JdbcDataSource();
        ds.setURL("jdbc:h2:mem:test;DB_CLOSE_DELAY=-1");
        ds.setUser("sa");
        ds.setPassword("");

        try (Connection conn = ds.getConnection();
             Statement stmt = conn.createStatement()) {
            stmt.execute("CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255))");
            stmt.execute("INSERT INTO users VALUES (1, 'Test User')");
            ResultSet rs = stmt.executeQuery("SELECT * FROM users");
            assertTrue(rs.next());
        }
    }
}
```
これにより、テストごとにインメモリデータベースが作成されます。

詳細は以下の参考文献を参照してください。

[Setting Up H2 for Testing in Spring Boot](https://medium.com/@paulkunda/setting-up-h2-for-testing-in-spring-boot-245d3a98e405)  
[Self-Contained Testing Using an In-Memory Database | Baeldung](https://www.baeldung.com/spring-jpa-test-in-memory-database)  
[Setting Up H2 for Testing in Spring Boot application](https://medium.com/@akshatakanaje08/setting-up-h2-for-testing-in-spring-boot-application-7f016220a475)  
[Test Spring Data Repositories with H2 in-memory database](https://www.geekyhacker.com/test-spring-data-repositories-with-h2-in-memory-database/)