---
audio: false
generated: true
lang: ja
layout: post
title: Liquibaseによるデータベーススキーマ管理
translated: true
type: note
---

以下は、Spring Bootアプリケーションでデータベーススキーマ変更を効果的に管理するための **Liquibaseの使用方法** に関する包括的なガイドです：

---

### 1. Liquibase依存関係の追加
始めるには、プロジェクトにLiquibaseの依存関係を含める必要があります。**Maven**を使用している場合は、`pom.xml`に以下を追加します：

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
```

**Gradle**の場合は、`build.gradle`に以下を追加します：

```groovy
implementation 'org.liquibase:liquibase-core'
```

これにより、Liquibaseコアライブラリがプロジェクトに導入されます。

---

### 2. Liquibaseの設定
Liquibaseはデータベーススキーマ変更を管理するために**changelogファイル**を使用します。デフォルトでは、Spring Bootはクラスパス上で`db/changelog/db.changelog-master.yaml`、`db/changelog/db.changelog-master.xml`、または`db/changelog/db.changelog-master.sql`という名前のファイルを探します。この場所は、`application.properties`（または`application.yml`）にプロパティを追加することでカスタマイズできます：

```properties
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

これにより、Spring Bootはchangelogファイルの場所を認識します。

---

### 3. Changelogファイルの作成
changelogファイルは、データベースに適用したい変更を定義します。XML、YAML、SQLなどの形式で記述できます。以下は、`src/main/resources/db/changelog/db.changelog-master.xml`に配置された**XML changelog**ファイルの例です：

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

この例では、`id`、`username`、`email`の3つのカラムを持つ`users`テーブルを作成します。各`<changeSet>`は適用する変更のセットを表します。

---

### 4. Spring Bootアプリケーションの実行
Spring Bootアプリケーションを起動すると、Liquibaseは自動的に以下を実行します：
- changelogファイルを読み取ります。
- どのchangesetが既に適用されているかをチェックします（`DATABASECHANGELOG`というテーブルで追跡されます）。
- 新しいchangesetをデータベースに対して実行します。

追加のコードは必要ありません。Spring Bootの自動設定がこれを処理します。

---

### 5. Liquibaseのカスタマイズ（オプション）
`application.properties`のプロパティを使用してLiquibaseの動作を調整できます。以下は一般的なオプションです：

```properties
spring.liquibase.enabled=true          # Liquibaseを有効または無効にする
spring.liquibase.drop-first=false      # 変更を適用する前にデータベースを削除する（注意して使用）
spring.liquibase.contexts=dev,prod     # 特定のコンテキストでのみchangesetを実行する
```

これらの設定により、Liquibaseを環境やワークフローに適応させることができます。

---

### 6. 高度な機能の活用
Liquibaseは、スキーマ管理を強化する強力な機能を提供します：
- **コンテキストとラベル**: 特定の環境（例：`dev`対`prod`）でどのchangesetを実行するかを制御します。
- **前提条件**: changesetを適用する前に特定の条件（例：テーブルが存在する）が満たされていることを確認します。
- **ロールバック**: 必要に応じてchangesetを元に戻す方法を定義します。
- **リファクタリング**: 複雑なデータベース変更（例：カラムの名前変更）に対する組み込みサポートを使用します。

例：changesetにコンテキストを追加する：

```xml
<changeSet id="2" author="your-name" context="dev">
    <addColumn tableName="users">
        <column name="created_at" type="timestamp"/>
    </addColumn>
</changeSet>
```

このchangesetは`dev`コンテキストでのみ実行されます。

---

### 7. インメモリデータベースでのテスト
テストでは、LiquibaseをH2のようなインメモリデータベースと組み合わせます。H2依存関係を追加します：

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

次に、テスト用に`application.properties`を設定します：

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

Liquibaseはテスト中にインメモリデータベースに変更を適用します。

---

### 8. Changelogのバージョン管理
changelogファイルは、アプリケーションコードと一緒にバージョン管理システム（例：Git）に保存してください。これにより、データベーススキーマがコードベースと同期して進化し、デプロイメントとロールバックがより予測可能になります。

---

### まとめ
Spring BootアプリケーションでLiquibaseを使用するには：
1. Liquibase依存関係を追加します。
2. changelogファイルの場所を設定します。
3. データベース変更を含むchangelogファイルを作成します。
4. アプリケーションを実行します。Liquibaseが残りを処理します。

Liquibaseは、構造化されバージョン管理された方法でデータベーススキーマ変更を管理する堅牢なツールであり、Spring Bootとシームレスに統合されています。