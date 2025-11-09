---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Flywayデータベース移行ガイド
translated: true
type: note
---

### Flywayの紹介
Flywayは、データベーススキーママイグレーションをバージョン管理された方法で管理する人気のあるオープンソースツールです。データベースへの増分的な変更（テーブルの作成、カラムの変更、データの挿入など）を繰り返し可能で安全な方法で適用できます。Javaアプリケーションでは、FlywayはAPI経由で統合でき、多くの場合アプリケーション起動時に実行され、コードがデータベースと対話する前にスキーマが最新であることを保証します。JDBC経由でほとんどのデータベース（PostgreSQL、MySQL、Oracleなど）で動作します。

### ステップ1: Flyway依存関係の追加
ビルドファイルにFlywayを追加します。エンタープライズ機能が必要でない限り、オープンソースエディションを使用してください。

**Maven (`pom.xml`)**:
```xml
<dependencies>
    <dependency>
        <groupId>org.flywaydb</groupId>
        <artifactId>flyway-core</artifactId>
        <version>11.14.1</version> <!-- 最新バージョンを確認してください -->
    </dependency>
    <!-- データベースJDBCドライバを追加（例：PostgreSQLの場合） -->
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
        <version>42.7.3</version>
    </dependency>
</dependencies>
```

**Gradle (`build.gradle`)**:
```groovy
dependencies {
    implementation 'org.flywaydb:flyway-core:11.14.1'
    // データベースJDBCドライバを追加
    implementation 'org.postgresql:postgresql:42.7.3'
}
```

対象データベースのJDBCドライバも必要です。

### ステップ2: Flywayの設定
Flywayは設定に流れるようなAPIを使用します。主な設定には、データベース接続の詳細、マイグレーションスクリプトの場所、オプションのコールバックなどがあります。

Javaコードで`Flyway`インスタンスを作成します：
```java
import org.flywaydb.core.Flyway;

public class DatabaseMigration {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "username";
        String password = "password";

        Flyway flyway = Flyway.configure()
                .dataSource(url, user, password)
                .locations("classpath:db/migration")  // SQLスクリプトのフォルダ（デフォルト: db/migration）
                .load();
    }
}
```
- `locations`: マイグレーションファイルが格納されている場所を指します（クラスパスの場合は`src/main/resources/db/migration`など）。
- その他の一般的な設定: 既存スキーマをベースライン化する`.baselineOnMigrate(true)`、履歴テーブルをカスタマイズする`.table("flyway_schema_history")`など。

### ステップ3: マイグレーションスクリプトの作成
マイグレーションスクリプトは、設定された場所（例: `src/main/resources/db/migration`）に配置されるSQLファイルです。Flywayはこれらを順番に適用します。

#### 命名規則
- **バージョン管理マイグレーション**（一度限りのスキーマ変更用）: `V<バージョン>__<説明>.sql`（例: `V1__Create_person_table.sql`, `V2__Add_age_column.sql`）。
  - バージョン形式: セグメントにはアンダースコアを使用（例: `V1_1__Initial.sql`）。
- **繰り返し可能マイグレーション**（ビューなどの継続的なタスク用）: `R__<説明>.sql`（例: `R__Update_view.sql`）。これらは変更されるたびに毎回実行されます。
- ファイルは辞書順に適用されます。

#### スクリプトの例
`src/main/resources/db/migration`に以下のファイルを作成します。

**V1__Create_person_table.sql**:
```sql
CREATE TABLE person (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO person (id, name) VALUES (1, 'John Doe');
```

**V2__Add_age_column.sql**:
```sql
ALTER TABLE person ADD COLUMN age INT;
```

**R__Populate_names.sql**（繰り返し可能）:
```sql
UPDATE person SET name = CONCAT(name, ' (Updated)') WHERE id = 1;
```

Flywayは適用されたマイグレーションを`flyway_schema_history`テーブルで追跡します。

SQLに適さない複雑なロジックには、Javaベースのマイグレーション（`org.flywaydb.core.api.migration.java.JavaMigration`を実装）を使用します。

### ステップ4: プログラムによるマイグレーションの実行
保留中のマイグレーションを適用するには`migrate()`を呼び出します。これをアプリの起動時（例: `main()`やSpringの`@PostConstruct`）に統合します。

```java
import org.flywaydb.core.Flyway;
import org.flywaydb.core.api.FlywayException;

public class DatabaseMigration {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "username";
        String password = "password";

        Flyway flyway = Flyway.configure()
                .dataSource(url, user, password)
                .locations("classpath:db/migration")
                .load();

        try {
            flyway.migrate();  // 保留中のすべてのマイグレーションを適用
            System.out.println("Database migrated successfully!");
        } catch (FlywayException e) {
            System.err.println("Migration failed: " + e.getMessage());
            // エラー処理（例: 終了またはロールバック）
        }

        // ここでアプリケーションの残りの部分を開始
    }
}
```

- `migrate()`: バージョン管理マイグレーションを順番に適用し、その後繰り返し可能マイグレーションを適用。
- その他のコマンド: ステータス確認の`flyway.info()`、問題修正の`flyway.repair()`、一貫性チェックの`flyway.validate()`。
- スキーマ互換性を保証するために、データベース操作の前にこれを実行します。

### ベストプラクティス
- マイグレーションは冪等性を保つ（再実行可能に）。
- 本番データのコピーでマイグレーションをテスト。
- マイグレーションファイルはバージョン管理する。
- Spring Bootの場合、`spring-boot-starter-jdbc`を追加し、`application.properties`で`spring.flyway.enabled=true`を設定して自動設定を有効化。

### 参考文献
- [Flyway API (Java) ドキュメント](https://documentation.red-gate.com/fd/api-java-277579358.html)
- [Flyway Migrations ドキュメント](https://documentation.red-gate.com/fd/migrations-271585107.html)
- [Flyway 入門ガイド](https://documentation.red-gate.com/fd/getting-started-with-flyway-184127223.html)