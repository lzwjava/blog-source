---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Maven Surefireプラグインユニットテストガイド
translated: true
type: note
---

**Maven Surefire Plugin** は、Maven ビルドライフサイクルの **test** フェーズでユニットテストを実行するプラグインです。ほぼすべてのプロジェクトがビルドに自動テストを統合する必要があるため、最も一般的に使用される Maven プラグインの一つです。

---

## 概要

* **名称**: `maven-surefire-plugin`
* **目的**: JUnit (3, 4, 5)、TestNG などのフレームワークで書かれたテストを実行する。
* **フェーズ**: Maven のデフォルトライフサイクルの `test` フェーズに紐づく。
* **出力**: テストレポートを生成する（デフォルトでは `target/surefire-reports` に出力）。

---

## 仕組み

1. `mvn test` または `mvn package` を実行すると、Maven は Surefire プラグインを呼び出す。
2. `src/test/java` ディレクトリをスキャンしてテストクラスを探す。
3. デフォルトでは、以下のような命名規則に一致するファイルを探す:

   * `*Test.java`
   * `Test*.java`
   * `*Tests.java`
   * `*TestCase.java`
4. これらを分離されたクラスローダーで実行する。
5. 結果を `target/surefire-reports` に書き出す（プレーンテキスト、XML、およびレポートプラグイン経由での HTML）。

---

## 基本的な使用方法

`pom.xml` で以下のように設定できます:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>3.2.5</version> <!-- 最新の安定版を使用 -->
    </plugin>
  </plugins>
</build>
```

この設定後、以下を実行するだけです:

```bash
mvn test
```

---

## 一般的な設定

* **包含/除外パターン**:

```xml
<configuration>
  <includes>
    <include>**/*MyTest.java</include>
  </includes>
  <excludes>
    <exclude>**/IntegrationTest.java</exclude>
  </excludes>
</configuration>
```

* **システムプロパティ**:

```xml
<configuration>
  <systemPropertyVariables>
    <env>dev</env>
  </systemPropertyVariables>
</configuration>
```

* **並列テスト実行**:

```xml
<configuration>
  <forkCount>2</forkCount>
  <reuseForks>true</reuseForks>
  <parallel>classes</parallel>
</configuration>
```

これにより、複数の JVM フォークまたはスレッドでテストが実行されます。

---

## 使用する場面

* **ユニットテスト**を Maven ライフサイクルに統合したい場合。
* **ユニットテスト (Surefire)** と **結合テスト (Failsafe プラグイン)** を分離したい場合:

  * Surefire → ユニットテスト (`mvn test`)
  * Failsafe → 結合テスト (`mvn verify`)

---

✅ **要約**: `maven-surefire-plugin` は、Maven プロジェクトにおけるユニットテスト実行のための主要なプラグインです。`pom.xml` で設定し、`mvn test` で実行し、レポートを `target/surefire-reports` で確認します。

---

**Surefire と Failsafe の違い**についても説明しましょうか？（混同されることが多いため）