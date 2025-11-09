---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Spring Boot と Liquibase の統合
translated: true
type: note
---

## Spring BootでのLiquibase統合

Liquibaseは、データベーススキーマ変更（マイグレーション）をバージョン管理するための人気のあるオープンソースツールです。Spring BootはLiquibaseに対する優れた自動設定サポートを提供しており、簡単に統合できます。このガイドではSpring Boot 3.x（2025年現在最新）とMavenを使用することを想定していますが、概念はGradleにも適用されます。基本的な手順を段階的に説明します。

### 前提条件
- Spring Bootプロジェクトのセットアップ（例：Spring Initializr経由）
- データベース（例：テスト用H2、本番用PostgreSQL/MySQL）が`application.properties`で設定済み

### ステップ1: Liquibase依存関係の追加
`pom.xml`にLiquibase Spring Bootスターターを含めます。これによりLiquibaseが導入され、シームレスに統合されます。

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId> <!-- データベース接続用 -->
</dependency>
```

Gradleの場合、`build.gradle`に追加：
```groovy
implementation 'org.liquibase:liquibase-core'
implementation 'org.springframework.boot:spring-boot-starter-jdbc'
```

依存関係を取得するために`mvn clean install`（または`./gradlew build`）を実行します。

### ステップ2: Liquibaseの設定
変更ログファイルをデフォルトの場所に配置すると、Spring BootはLiquibaseを自動検出します。`application.properties`（または同等の`.yml`）でカスタマイズします。

`application.properties`の例：
```properties
# データベース設定（使用するDBに合わせて調整）
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driver-class-name=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# Liquibase設定
spring.liquibase.change-log=classpath:db/changelog/db.changelog-master.xml
spring.liquibase.enabled=true  # デフォルトはtrue
spring.liquibase.drop-first=false  # 開発時にスキーマを起動時に削除する場合はtrueに設定
```

- `change-log`：マスターチェンジログファイルへのパス（デフォルト：`db/changelog/db.changelog-master.xml`）
- `spring.liquibase.enabled`で有効/無効を切り替え
- コンテキスト/プロファイルには`spring.liquibase.contexts=dev`を使用して特定の変更を実行

### ステップ3: チェンジログファイルの作成
Liquibaseは「チェンジログ」を使用してスキーマ変更を定義します。`src/main/resources`の下にディレクトリ構造を作成します：
```
src/main/resources/
└── db/
    └── changelog/
        ├── db.changelog-master.xml  # 他のファイルを含むマスターファイル
        └── changes/
            ├── 001-create-users-table.xml  # 個々の変更
            └── 002-add-email-column.xml
```

#### マスターチェンジログ（`db.changelog-master.xml`）
他のチェンジログを含みます：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.24.xsd">

    <include file="changes/001-create-users-table.xml"/>
    <include file="changes/002-add-email-column.xml"/>
</databaseChangeLog>
```

#### サンプル変更（`001-create-users-table.xml`）
テーブル作成を定義：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                                       http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.24.xsd">

    <changeSet id="001" author="yourname">
        <createTable tableName="users">
            <column name="id" type="bigint">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="name" type="varchar(255)">
                <constraints nullable="false"/>
            </column>
        </createTable>
    </changeSet>
</databaseChangeLog>
```

- チェンジログにはXML、YAML、JSON、またはSQL形式を使用
- 各`<changeSet>`はIDを持つマイグレーション（追跡用）
- `java -jar target/your-app.jar`を実行してアプリを起動 - Liquibaseはブートストラップ時に自動的に変更を適用

### ステップ4: 実行とテスト
- **起動時**: Spring Bootはアプリが完全に起動する前にLiquibaseを実行
- **ロールバック**: テストには`spring.liquibase.rollback-file`またはCLIを使用
- **CLI統合**: 手動実行にはLiquibase Mavenプラグインを追加：
  ```xml
  <plugin>
      <groupId>org.liquibase</groupId>
      <artifactId>liquibase-maven-plugin</artifactId>
      <version>4.24.0</version>
      <configuration>
          <changeLogFile>src/main/resources/db/changelog/db.changelog-master.xml</changeLogFile>
          <url>jdbc:h2:mem:testdb</url>
          <username>sa</username>
          <password></password>
      </configuration>
  </plugin>
  ```
  その後`mvn liquibase:update`を実行

- **検証**: チェンジログをチェックするために`spring.liquibase.validate-on-migrate=true`を有効化

### 一般的なヒント
- **プロファイル**: 必要に応じてBeanに`@Profile("dev")`を使用するが、Liquibaseはフィルタリングされない限りグローバルに実行
- **前提条件**: 変更セットに`<preConditions>`を追加してDB状態をチェック
- **SQL形式**: 生のSQLには`.sql`ファイルを作成し、`<sqlFile path="changes/create-users.sql" relativeToChangelogFile="true"/>`で含める
- **トラブルシューティング**: エラーについてはログを確認（例：`liquibase`接頭辞付き）。DB URLが正しいことを確認
- **本番環境**: 好みに応じてFlywayを使用可能だが、Liquibaseは複雑な変更とマルチDBサポートに優れる

タグ付きロールバックやカスタム拡張などの高度な機能については、ドキュメントを参照してください。

### 参考文献
- [Spring Boot Liquibase自動設定](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#io.liquibase)
- [Liquibase公式ドキュメント](https://docs.liquibase.com/start/home.html)
- [Baeldung Spring Boot + Liquibaseチュートリアル](https://www.baeldung.com/liquibase-refactor-schema-of-jpa-entity-in-spring-boot)