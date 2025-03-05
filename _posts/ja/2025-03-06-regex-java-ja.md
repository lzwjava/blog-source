---
audio: false
generated: true
lang: ja
layout: post
title: 正規表現のJava
translated: true
---

# `java.util.regex` の Java 使用方法

Java の `java.util.regex` パッケージは、正規表現（regex）を使用してテキストをマッチングおよび操作するためのツールを提供します。このガイドでは、このパッケージの基本的な使用方法について説明し、主に `Pattern` および `Matcher` という2つの主要なクラスに焦点を当てます。また、一般的な使用例と例を提供して、あなたが始めるのを助けます。

## `java.util.regex` の概要

`java.util.regex` パッケージには以下が含まれます：

- **`Pattern`**: 正規表現をコンパイルしたものを表します。正規表現文字列から作成します。
- **`Matcher`**: パターンを特定の入力文字列に適用し、マッチング操作を実行します。

さらに、Java の `String` クラスは、より簡単なタスクのために正規表現ベースのメソッドを提供します。

## `java.util.regex` を使用する基本的な手順

Java で正規表現を使用するには、以下の手順に従います：

1. **パターンをコンパイルする**: 正規表現文字列を `Pattern` オブジェクトに変換します。
2. **マッチャーを作成する**: パターンを使用して、入力テキストのマッチャーを作成します。
3. **操作を実行する**: マッチャーを使用して、マッチングを確認し、パターンを検索し、テキストを操作します。

実際にどのように動作するかを以下に示します。

## 例 1: メールアドレスの検証

基本的な正規表現パターン `".+@.+\\..+"` を使用して、簡単なメール検証器を作成します。このパターンは、 `@` 記号の前後に少なくとも1文字が含まれ、その後にドットとさらに文字が続く文字列にマッチします（例： `example@test.com`）。

```java
import java.util.regex.*;

public class EmailValidator {
    public static boolean isValidEmail(String email) {
        // 正規表現パターンを定義
        String regex = ".+@.+\\..+";
        // パターンをコンパイル
        Pattern pattern = Pattern.compile(regex);
        // 入力文字列のマッチャーを作成
        Matcher matcher = pattern.matcher(email);
        // 文字列全体がパターンに一致するかどうかを確認
        return matcher.matches();
    }

    public static void main(String[] args) {
        String email = "example@test.com";
        if (isValidEmail(email)) {
            System.out.println("有効なメールアドレス");
        } else {
            System.out.println("無効なメールアドレス");
        }
    }
}
```

### 説明
- **`Pattern.compile(regex)`**: 正規表現文字列を `Pattern` オブジェクトにコンパイルします。
- **`pattern.matcher(email)`**: 入力文字列 `email` のマッチャーを作成します。
- **`matcher.matches()`**: 文字列全体がパターンに一致する場合は `true` を返し、そうでない場合は `false` を返します。

**出力**: `有効なメールアドレス`

注意: これは簡略化されたメールパターンです。実際のメール検証には、より複雑な正規表現（例：RFC 5322 に従ったもの）が必要ですが、これは始めるための出発点です。

## 例 2: 文字列からすべてのハッシュタグを検索する

ツイートからすべてのハッシュタグ（例：`#java`）を抽出する場合、正規表現 `"#\\w+"` を使用します。ここで、`#` は文字通りのハッシュタグ記号にマッチし、`\\w+` は1つ以上の単語文字（文字、数字、またはアンダースコア）にマッチします。

```java
import java.util.regex.*;

public class HashtagExtractor {
    public static void main(String[] args) {
        String tweet = "これは #サンプルのツイートで #複数のハッシュタグが含まれています #java";
        String regex = "#\\w+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(tweet);

        // すべてのマッチを検索
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}
```

### 説明
- **`matcher.find()`**: 入力文字列内の次のマッチに移動し、マッチが見つかった場合は `true` を返します。
- **`matcher.group()`**: 現在のマッチのマッチしたテキストを返します。

**出力**:
```
#サンプル
#複数の
#java
```

## 例 3: 正規表現を使用してテキストを置換する

単語（例：`badword` をアスタリスクで検閲する）のすべての出現を置換するには、`String.replaceAll()` メソッドを使用し、内部で正規表現を使用します。

```java
public class TextCensor {
    public static void main(String[] args) {
        String text = "これは badword の例で badword が繰り返されています。";
        String censored = text.replaceAll("badword", "*******");
        System.out.println(censored);
    }
}
```

**出力**: `これは ******* の例で ******* が繰り返されています。`

より複雑な置換には `Matcher` を使用します：

```java
import java.util.regex.*;

public class ComplexReplacement {
    public static void main(String[] args) {
        String text = "連絡先: 123-456-7890";
        String regex = "\\d{3}-\\d{3}-\\d{4}"; // 電話番号にマッチ
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);
        String result = matcher.replaceAll("XXX-XXX-XXXX");
        System.out.println(result);
    }
}
```

**出力**: `連絡先: XXX-XXX-XXXX`

## 例 4: グループを使用して構造化されたデータを解析する

正規表現のグループは、括弧 `()` で定義され、マッチの一部をキャプチャします。例えば、SSN（社会保障番号）のような `123-45-6789` を解析するには：

```java
import java.util.regex.*;

public class SSNParser {
    public static void main(String[] args) {
        String ssn = "123-45-6789";
        String regex = "(\\d{3})-(\\d{2})-(\\d{4})"; // エリア、グループ、シリアル番号のグループ
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(ssn);

        if (matcher.matches()) {
            System.out.println("エリア番号: " + matcher.group(1));
            System.out.println("グループ番号: " + matcher.group(2));
            System.out.println("シリアル番号: " + matcher.group(3));
        }
    }
}
```

### 説明
- **`"(\\d{3})-(\\d{2})-(\\d{4})"`**: 3つのグループを定義します：
  - グループ 1: `\\d{3}`（3桁）
  - グループ 2: `\\d{2}`（2桁）
  - グループ 3: `\\d{4}`（4桁）
- **`matcher.group(n)`**: グループ `n`（1から始まるインデックス）にマッチしたテキストを取得します。

**出力**:
```
エリア番号: 123
グループ番号: 45
シリアル番号: 6789
```

名前付きグループを使用して明確にすることもできます：

```java
String regex = "(?<area>\\d{3})-(?<group>\\d{2})-(?<serial>\\d{4})";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher("123-45-6789");
if (matcher.matches()) {
    System.out.println("エリア: " + matcher.group("area"));
    System.out.println("グループ: " + matcher.group("group"));
    System.out.println("シリアル: " + matcher.group("serial"));
}
```

## 追加の機能とヒント

### フラグ

`Pattern.compile()` でパターンの動作を変更するフラグを使用します：
- **`Pattern.CASE_INSENSITIVE`**: マッチング時に大文字と小文字を無視します。
  ```java
  Pattern pattern = Pattern.compile("hello", Pattern.CASE_INSENSITIVE);
  Matcher matcher = pattern.matcher("HELLO");
  System.out.println(matcher.matches()); // true
  ```

### 文字列メソッド

簡単なタスクには `String` メソッドを使用します：
- **`matches()`**: 文字列全体が正規表現に一致するかどうかを確認します。
  ```java
  String text = "cat";
  System.out.println(text.matches("\\w{3}")); // true
  ```
- **`split()`**: 正規表現パターンで文字列を分割します。
  ```java
  String data = "apple, banana, cherry";
  String[] fruits = data.split("\\s*,\\s*");
  // 出力: apple, banana, cherry
  ```

### 特殊文字のエスケープ

正規表現は `.`、`*`、`?` などの特殊文字を使用します。これらを文字通りにマッチさせるには、`\\` でエスケープします：
- 期限をマッチさせる: `"\\."`
- Java 文字列でバックスラッシュをエスケープ: `"\\d"` は数字、`"\\\\"` は文字通りのバックスラッシュです。

### パフォーマンス

パターンのコンパイルはコストがかかります。可能な限り `Pattern` オブジェクトを再利用します：
```java
Pattern pattern = Pattern.compile("\\d+"); // 1回コンパイル
for (String input : new String[]{"123", "456"}) {
    Matcher matcher = pattern.matcher(input);
    if (matcher.matches()) {
        System.out.println("数字: " + input);
    }
}
```

### エラーハンドリング

無効な正規表現パターンは `PatternSyntaxException` をスローします。生産コードでこれを処理します：
```java
try {
    Pattern pattern = Pattern.compile("["); // 無効な正規表現
} catch (PatternSyntaxException e) {
    System.err.println("無効な正規表現: " + e.getMessage());
}
```

## 要約

- **パターンをコンパイルする**: `Pattern.compile(regex)`
- **マッチャーを作成する**: `pattern.matcher(input)`
- **主要な操作**:
  - `matches()`: 文字列全体のマッチ
  - `find()`: 次のマッチを検索
  - `group()`: マッチしたテキストを抽出
  - `replaceAll()`: マッチを置換
- **便利な機能**: 簡単なタスクには `String` メソッドを使用します。
- **ベストプラクティス**: 特殊文字をエスケープし、パターンを再利用し、例外を処理します。

これでは `java.util.regex` の基本的な使用方法について説明しました。ルックアヘッドや文字クラスなどの高度なトピックについては、[Java ドキュメント](https://docs.oracle.com/en/java/javase/17/docs/api/java.util.regex/package-summary.html)を参照するか、特定の使用例で実験してください！