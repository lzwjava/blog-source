---
audio: true
lang: ja
layout: post
title: Maven Surefire プラグイン
translated: true
---

以下は、Mavenベースのプロジェクトでビルドプロセス中にユニットテストを実行するための重要なコンポーネントである **Maven Surefire Plugin** の説明です。この説明では、その目的、設定、使用方法、カスタマイズオプションについて説明します。

---

## Maven Surefire Plugin とは？

**Maven Surefire Plugin** は、Apache Mavenのビルドライフサイクル中にユニットテストを実行するために設計されたプラグインです。このプラグインは、Mavenの `test` フェーズとシームレスに統合され、`mvn test`、`mvn package`、`mvn install` などのコマンドを実行すると自動的にトリガーされます。このプラグインは、JUnit（バージョン3、4、5）やTestNGなどの人気のあるテストフレームワークをサポートし、テスト結果を評価するためのテストレポートを生成します。

### 主要機能
- テストを別のJVMプロセスで実行して隔離します。
- 多くのテストフレームワーク（JUnit、TestNGなど）をサポートします。
- XMLやプレーンテキストなどの形式でテストレポートを生成します。
- テストをスキップする、特定のテストを実行する、実行をカスタマイズするなどの柔軟性を提供します。

---

## `pom.xml` の基本設定

Surefireプラグインは、Mavenのビルドライフサイクルにデフォルトで含まれているため、基本的な使用には設定する必要はありません。しかし、`pom.xml` ファイルに明示的に宣言してバージョンを指定したり、動作をカスタマイズしたりすることもできます。

### 最小限の設定
設定を追加しない場合、Mavenはデフォルト設定でプラグインを使用します：
- テストは `src/test/java` にあります。
- テストファイルは `**/*Test.java`、`**/Test*.java`、`**/*Tests.java` などの名前付けパターンに従います。

### 明示的な宣言
プラグインをカスタマイズするか、特定のバージョンを確保するには、`pom.xml` の `<build><plugins>` セクションに追加します。以下は例です：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M5</version> <!-- 最新バージョンを使用 -->
        </plugin>
    </plugins>
</build>
```

---

## Surefire でテストを実行する

このプラグインは、Mavenライフサイクルの `test` フェーズに結びついています。以下にその使用方法を示します：

### すべてのテストを実行する
すべてのユニットテストを実行するには、以下を実行します：

```
mvn test
```

### 大規模なビルドでテストを実行する
`test` フェーズを含むコマンドを実行すると、テストが自動的に実行されます。例えば：

```
mvn package
mvn install
```

### テストをスキップする
コマンドラインフラグを使用してテストの実行をスキップできます：
- **テストの実行をスキップする**：`-DskipTests`
  ```
  mvn package -DskipTests
  ```
- **テストのコンパイルと実行をスキップする**：`-Dmaven.test.skip=true`
  ```
  mvn package -Dmaven.test.skip=true
  ```

---

## Surefire プラグインのカスタマイズ

`pom.xml` に `<configuration>` セクションを追加してプラグインの動作をカスタマイズできます。以下に一般的なカスタマイズ方法を示します：

### 特定のテストを含めるまたは除外する
パターンを指定して実行するテストやスキップするテストを指定します：
```xml
<configuration>
    <includes>
        <include>**/My*Test.java</include>
    </includes>
    <excludes>
        <exclude>**/SlowTest.java</exclude>
    </excludes>
</configuration>
```

### テストを並行して実行する
テストを並行して実行して実行を高速化します：
```xml
<configuration>
    <parallel>methods</parallel>
    <threadCount>2</threadCount>
</configuration>
```
*注*：この機能を有効にする前に、テストがスレッドセーフであることを確認してください。

### システムプロパティを渡す
テストJVMに対してプロパティを設定します：
```xml
<configuration>
    <systemPropertyVariables>
        <propertyName>propertyValue</propertyName>
    </systemPropertyVariables>
</configuration>
```

### レポートを生成する
デフォルトでは、レポートは `target/surefire-reports` に保存されます。HTMLレポートを生成するには、`maven-surefire-report-plugin` を使用します：
```xml
<reporting>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-report-plugin</artifactId>
            <version>3.0.0-M5</version>
        </plugin>
    </plugins>
</reporting>
```
HTMLレポートを生成するには、`mvn surefire-report:report` を実行します。

---

## テストの失敗を処理する

### テストの失敗でビルドを失敗させる
デフォルトでは、失敗したテストはビルドを失敗させます。失敗を無視して続行するには：
```
mvn test -Dmaven.test.failure.ignore=true
```

### 失敗したテストを再実行する
フレーキーテストを処理するために失敗を再試行します：
```xml
<configuration>
    <rerunFailingTestsCount>2</rerunFailingTestsCount>
</configuration>
```
これにより、失敗したテストが最大2回再実行されます。

---

## テストフレームワークとSurefireを使用する

このプラグインは、最小限の設定でさまざまなテストフレームワークをサポートします：

### JUnit 4
追加の設定は不要です。SurefireはJUnit 4のテストを自動的に検出します。

### JUnit 5
JUnit 5の依存関係を追加します：
```xml
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.8.1</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
完全なサポートを得るには、Surefireバージョン2.22.0以降を使用してください。

### TestNG
TestNGの依存関係を追加します：
```xml
<dependencies>
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <version>7.4.0</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
Surefireは自動的にTestNGテストを実行します。

---

## 主要なポイント

- **テストの場所**：テストは `src/test/java` にあり、リソースは `src/test/resources` にあります。
- **命名規則**：デフォルトのパターンには `**/*Test.java`、`**/Test*.java` などがありますが、これらをカスタマイズすることもできます。
- **プラグインのバージョン**：最新の機能とフレームワークサポートを得るために、最新のバージョン（例：3.0.0-M5）を使用してください。

---

## まとめ

**Maven Surefire Plugin** は、Mavenプロジェクトでユニットテストを実行するための重要なプラグインです。これを使用するには：
1. デフォルトの動作に頼るか、`pom.xml` に明示的に宣言してカスタマイズします。
2. `mvn test` または `mvn package` などの大規模なビルドでテストを実行します。
3. 含める/除外するパターン、並行実行、システムプロパティなどのオプションでカスタマイズします。
4. テストをスキップする、無視する、フレーキーテストを再実行するなどして失敗を処理します。
5. JUnitやTestNGなどのテストフレームワークとの互換性を確保するために、適切な依存関係を追加します。

このプラグインは、Mavenプロジェクトでのユニットテスト管理に強力で柔軟な方法を提供します！