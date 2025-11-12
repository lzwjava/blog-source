---
audio: false
generated: true
lang: ja
layout: post
title: Maven Surefire プラグイン
translated: true
type: note
---

以下は、**Maven Surefire Plugin** の説明です。これは Maven ベースのプロジェクトにおいて、ビルドプロセス中にユニットテストを実行するための主要なコンポーネントです。この説明では、その目的、設定、使用方法、およびカスタマイズオプションについて説明します。

---

## Maven Surefire Plugin とは？

**Maven Surefire Plugin** は、Apache Maven におけるプラグインで、ビルドライフサイクル中にユニットテストを実行するために設計されています。これは Maven の `test` フェーズとシームレスに統合され、`mvn test`、`mvn package`、または `mvn install` などのコマンドを実行したときに自動的に起動します。このプラグインは JUnit (バージョン 3, 4, 5) や TestNG などの人気のあるテストフレームワークをサポートし、開発者がテスト結果を評価するのに役立つテストレポートを生成します。

### 主な機能
- 分離のために別の JVM プロセスでテストを実行します。
- 複数のテストフレームワーク (JUnit, TestNG など) をサポートします。
- XML やプレーンテキストなどの形式でテストレポートを生成します。
- テストをスキップしたり、特定のテストを実行したり、実行をカスタマイズする柔軟性を提供します。

---

## `pom.xml` での基本的な設定

Surefire Plugin は Maven のビルドライフサイクルにデフォルトで含まれているため、基本的な使用には設定は不要です。ただし、バージョンを指定したり、動作をカスタマイズしたりするために、`pom.xml` ファイルで明示的に宣言することができます。

### 最小限の設定
設定を何も追加しない場合、Maven はデフォルト設定でプラグインを使用します：
- テストは `src/test/java` に配置されます。
- テストファイルは `**/*Test.java`、`**/Test*.java`、`**/*Tests.java` などの命名パターンに従います。

### 明示的な宣言
プラグインをカスタマイズするか、特定のバージョンを保証するために、`pom.xml` の `<build><plugins>` セクションに追加します。以下は例です：

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

## Surefire でのテスト実行

このプラグインは Maven ライフサイクルの `test` フェーズに関連付けられています。使用方法は以下の通りです：

### すべてのテストを実行
すべてのユニットテストを実行するには、以下を実行します：

```
mvn test
```

### より大きなビルド内でテストを実行
`test` フェーズを含むコマンドを実行すると、テストは自動的に実行されます。例えば：

```
mvn package
mvn install
```

### テストをスキップ
コマンドラインフラグを使用してテスト実行をスキップできます：
- **テスト実行をスキップ**: `-DskipTests`
  ```
  mvn package -DskipTests
  ```
- **テストのコンパイルと実行をスキップ**: `-Dmaven.test.skip=true`
  ```
  mvn package -Dmaven.test.skip=true
  ```

---

## Surefire Plugin のカスタマイズ

`pom.xml` に `<configuration>` セクションを追加することで、プラグインの動作を調整できます。以下は一般的なカスタマイズの例です：

### 特定のテストを含めるまたは除外する
パターンを使用して、実行するテストやスキップするテストを指定します：
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

### テストを並列実行
テストを同時実行して実行速度を向上させます：
```xml
<configuration>
    <parallel>methods</parallel>
    <threadCount>2</threadCount>
</configuration>
```
*注意*: これを有効にする前に、テストがスレッドセーフであることを確認してください。

### システムプロパティを渡す
テスト JVM 用のプロパティを設定します：
```xml
<configuration>
    <systemPropertyVariables>
        <propertyName>propertyValue</propertyName>
    </systemPropertyVariables>
</configuration>
```

### レポートを生成
デフォルトでは、レポートは `target/surefire-reports` に保存されます。HTML レポートの場合は、`maven-surefire-report-plugin` を使用します：
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
HTML レポートを生成するには、`mvn surefire-report:report` を実行します。

---

## テスト失敗の処理

### テスト失敗時にビルドを失敗させる
デフォルトでは、テストが失敗するとビルドが失敗します。失敗を無視して続行するには：
```
mvn test -Dmaven.test.failure.ignore=true
```

### 失敗したテストを再実行
不安定なテストに対処するために、失敗をリトライします：
```xml
<configuration>
    <rerunFailingTestsCount>2</rerunFailingTestsCount>
</configuration>
```
これにより、失敗したテストは最大 2 回再実行されます。

---

## テストフレームワークでの Surefire の使用

このプラグインは、最小限の設定で様々なテストフレームワークをサポートします：

### JUnit 4
追加の設定は不要です。Surefire は JUnit 4 テストを自動的に検出します。

### JUnit 5
JUnit 5 の依存関係を追加します：
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
完全なサポートのためには、Surefire バージョン 2.22.0 以降を使用してください。

### TestNG
TestNG の依存関係を追加します：
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
Surefire は自動的に TestNG テストを実行します。

---

## 重要な注意点

- **テストの場所**: テストは `src/test/java` に、リソースは `src/test/resources` に配置する必要があります。
- **命名規則**: デフォルトのパターンは `**/*Test.java`、`**/Test*.java` などですが、これらはカスタマイズ可能です。
- **プラグインバージョン**: 最新の機能とフレームワークサポートのために、最近のバージョン (例: 3.0.0-M5) を使用してください。

---

## まとめ

**Maven Surefire Plugin** は、Maven プロジェクトでユニットテストを実行するために不可欠です。使用方法は以下の通りです：
1. デフォルトの動作に依存するか、カスタマイズのために `pom.xml` で明示的に宣言します。
2. `mvn test` または `mvn package` のようなより大きなビルドの一部としてテストを実行します。
3. インクルード/エクスクルードパターン、並列実行、システムプロパティなどのオプションでカスタマイズします。
4. テストをスキップしたり、無視したり、不安定なテストを再実行したりして、失敗を処理します。
5. 適切な依存関係を追加することで、使用するテストフレームワーク (JUnit, TestNG) との互換性を確保します。

このプラグインは、Maven プロジェクトにおけるユニットテスト管理のための堅牢で柔軟な方法を提供します！