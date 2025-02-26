---
audio: false
lang: ja
layout: post
title: 'Liquibase: データベーススキーマ管理'
translated: true
---

ここでは、Spring BootアプリケーションでLiquibaseを使用してデータベーススキーマの変更を効果的に管理するための包括的なガイドを提供します：

---

### 1. Liquibaseの依存関係を追加
まず、プロジェクトにLiquibaseの依存関係を追加する必要があります。Mavenを使用している場合、`pom.xml`に以下を追加します：

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
```

Gradleを使用している場合、`build.gradle`に以下を追加します：

```groovy
implementation 'org.liquibase:liquibase-core'
```

これにより、Liquibaseのコアライブラリがプロジェクトに含まれます。

---

### 2. Liquibaseの設定
Liquibaseは、データベーススキーマの変更を管理するために**changelogファイル**を使用します。デフォルトでは、Spring Bootはクラスパス内の`db/changelog/db.changelog-master.yaml`、`db/changelog/db.changelog-master.xml`、または`db/changelog/db.changelog-master.sql`という名前のファイルを探します。この場所をカスタマイズするには、`application.properties`（または`application.yml`）にプロパティを追加します：

```properties
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

これにより、Spring Bootにchangelogファイルの場所を教えます。

---

### 3. Changelogファイルの作成
Changelogファイルは、データベースに適用したい変更を定義します。XML、YAML、またはSQL形式で記述できます。以下は、`src/main/resources/db/changelog/db.changelog-master.xml`にある**XML changelogファイル**の例です：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.8.xsd">

    <changeSet id="1" author="your-name">
        <createTable tableName="users">
            <column name="id" type="int">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="username" type="varchar(255)"/>
            <column name="email" type="varchar(255)"/>
        </createTable>
    </changeSet>

</databaseChangeLog>
```

この例では、`id`、`username`、`email`という3つの列を持つ`users`テーブルが作成されます。各`<changeSet>`は適用する変更のセットを表します。

---

### 4. Spring Bootアプリケーションの実行
Spring Bootアプリケーションを起動すると、Liquibaseは自動的に以下を行います：
- Changelogファイルを読み込みます。
- 既に適用されたchangesetsを確認します（`DATABASECHANGELOG`という名前のテーブルで追跡）。
- データベースに新しいchangesetsを実行します。

追加のコードは必要ありません—Spring Bootの自動設定がこれを処理します。

---

### 5. Liquibaseのカスタマイズ（オプション）
`application.properties`のプロパティを使用してLiquibaseの動作を調整できます。以下は一般的なオプションです：

```properties
spring.liquibase.enabled=true          # Liquibaseを有効または無効にする
spring.liquibase.drop-first=false      # 変更を適用する前にデータベースを削除する（慎重に使用）
spring.liquibase.contexts=dev,prod     # 特定のコンテキストでのみchangesetsを実行する
```

これらの設定により、Liquibaseを環境やワークフローに適応させることができます。

---

### 6. 高度な機能を活用
Liquibaseは、スキーマ管理を強化するための強力な機能を提供します：
- **コンテキストとラベル**：特定の環境（例：`dev`対`prod`）でchangesetsを実行する制御。
- **前提条件**：changesetを適用する前に特定の条件（例：テーブルが存在する）が満たされていることを確認。
- **ロールバック**：必要に応じてchangesetを元に戻す方法を定義。
- **リファクタリング**：複雑なデータベース変更（例：列の名前変更）に対する組み込みサポート。

例えば、changesetにコンテキストを追加する：

```xml
<changeSet id="2" author="your-name" context="dev">
    <addColumn tableName="users">
        <column name="created_at" type="timestamp"/>
    </addColumn>
</changeSet>
```

このchangesetは`dev`コンテキストでのみ実行されます。

---

### 7. インメモリデータベースでテスト
テストには、LiquibaseをインメモリデータベースであるH2と組み合わせます。H2の依存関係を追加します：

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

次に、`application.properties`をテスト用に設定します：

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

Liquibaseはテスト中にインメモリデータベースに変更を適用します。

---

### 8. Changelogのバージョン管理
Changelogファイルをバージョン管理（例：Git）に保存し、アプリケーションコードと一緒に管理します。これにより、データベーススキーマがコードベースと同期して進化し、デプロイメントとロールバックが予測可能になります。

---

### まとめ
Spring BootアプリケーションでLiquibaseを使用するには：
1. Liquibaseの依存関係を追加します。
2. Changelogファイルの場所を設定します。
3. データベースの変更を含むchangelogファイルを作成します。
4. アプリケーションを実行します—Liquibaseが残りを処理します。

Liquibaseは、構造化されたバージョン管理方式でデータベーススキーマの変更を管理するための強力なツールであり、Spring Bootとシームレスに統合されています。