---
audio: false
generated: true
lang: ja
layout: post
title: Apache Commons Lang を使用したランダム文字列の生成
translated: true
type: note
---

`RandomStringUtils` は Apache Commons Lang ライブラリから提供される非常に便利なクラスで、ランダムな文字列を生成するための様々な静的メソッドを提供します。これには、特定の長さの文字列、文字のみを含む文字列、数字のみ、英数字、あるいはカスタム文字セットからの文字列の生成が含まれます。

使用方法と必要な Maven 依存関係は以下の通りです：

## `org.apache.commons.lang3.RandomStringUtils;` の使用方法

まず、Java ファイルでクラスをインポートする必要があります：

```java
import org.apache.commons.lang3.RandomStringUtils;
```

その後、その静的メソッドを使用できます。以下に一般的な例を示します：

1.  **特定の長さのランダムな英数字文字列を生成：**

    ```java
    String randomAlphaNumeric = RandomStringUtils.randomAlphanumeric(10);
    System.out.println("Random alphanumeric: " + randomAlphaNumeric); // 例: "aB5cY2x9Pq"
    ```

2.  **特定の長さのランダムな英字文字列を生成：**

    ```java
    String randomAlphabetic = RandomStringUtils.randomAlphabetic(8);
    System.out.println("Random alphabetic: " + randomAlphabetic); // 例: "GhJkLmNo"
    ```

3.  **特定の長さのランダムな数字文字列を生成：**

    ```java
    String randomNumeric = RandomStringUtils.randomNumeric(6);
    System.out.println("Random numeric: " + randomNumeric); // 例: "123456"
    ```

4.  **文字と数字の混在したランダムな文字列をフラグ指定で生成：**

    ```java
    String randomLettersAndNumbers = RandomStringUtils.random(12, true, true);
    System.out.println("Random letters and numbers: " + randomLettersAndNumbers); // 例: "abC123DeF456"
    ```

5.  **カスタム文字セットからランダムな文字列を生成：**

    ```java
    String chars = "abcdefg";
    String randomFromCustomSet = RandomStringUtils.random(5, chars);
    System.out.println("Random from custom set: " + randomFromCustomSet); // 例: "gcfae"
    ```

## `pom.xml` で使用するライブラリ

Maven プロジェクトで `RandomStringUtils` を使用するには、`pom.xml` ファイルに `commons-lang3` 依存関係を追加する必要があります。

依存関係のスニペットは以下の通りです：

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.14.0</version> </dependency>
```

**重要な注意点：**

  * **バージョン:** `commons-lang3` の最新の安定版については、常に [Maven Central](https://mvnrepository.com/artifact/org.apache.commons/commons-lang3) で確認してください。最終更新時点では `3.14.0` 以降が良い選択ですが、常に利用可能な最新の安定版を使用することが最善です。
  * **スコープ:** 依存関係のデフォルトスコープは `compile` であり、通常はこのようなユーティリティライブラリに必要なものです。これは、JAR がコンパイル時、テスト時、実行時に利用可能であることを意味します。テストのみで使用する場合は `<scope>test</scope>` を使用する可能性があります。
  * **非推奨事項:** `RandomStringUtils.randomAlphabetic(int count)` のような一部の古いメソッドは、Apache Commons Lang 3 の新しいバージョンでは非推奨となっていることに注意してください。代わりに、ランダム性のソースをより細かく制御できる `secure()`、`secureStrong()`、または `insecure()` メソッドを使用することが推奨されます。例えば、`RandomStringUtils.secure().nextAlphanumeric(10)` のようになります。ただし、古いメソッドも多くのユースケースではまだ機能します。