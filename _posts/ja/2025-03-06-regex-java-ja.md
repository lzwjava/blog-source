---
audio: false
generated: true
lang: ja
layout: post
title: Javaにおける正規表現
translated: true
type: note
---

# Javaでの`java.util.regex`の使用方法

Javaの`java.util.regex`パッケージは、テキストのマッチングや操作に使用されるパターンである正規表現（regex）を扱うためのツールを提供します。このガイドでは、このパッケージの基本的な使用方法を、2つの主要なクラスである`Pattern`と`Matcher`に焦点を当てて説明します。また、実際の使用例も紹介しますので、初心者の方でも理解しやすい内容になっています。

## `java.util.regex`の概要

`java.util.regex`パッケージには以下が含まれます：

- **`Pattern`**: コンパイルされた正規表現を表します。正規表現の文字列から作成します。
- **`Matcher`**: パターンを特定の入力文字列に適用し、マッチング操作を実行します。

さらに、Javaの`String`クラスには、より単純なタスクのための正規表現ベースのメソッドも用意されています。

## `java.util.regex`の基本的な使用手順

Javaで正規表現を使用するには、以下の手順に従います：

1. **パターンのコンパイル**: 正規表現の文字列を`Pattern`オブジェクトに変換します。
2. **マッチャーの作成**: パターンを使用して、入力テキストに対する`Matcher`を作成します。
3. **操作の実行**: マッチャーを使用して、マッチの確認、パターンの検索、テキストの操作などを行います。

実際の動作を以下で確認しましょう。

## 例1: メールアドレスの検証

基本的な正規表現パターン`".+@.+\\..+"`を使用して、シンプルなメールアドレス検証ツールを作成してみましょう。このパターンは、`@`記号の前後に少なくとも1文字以上あり、その後にドットとさらに文字が続く文字列（例: `example@test.com`）にマッチします。

```java
import java.util.regex.*;

public class EmailValidator {
    public static boolean isValidEmail(String email) {
        // 正規表現パターンを定義
        String regex = ".+@.+\\..+";
        // パターンをコンパイル
        Pattern pattern = Pattern.compile(regex);
        // 入力文字列に対するマッチャーを作成
        Matcher matcher = pattern.matcher(email);
        // 文字列全体がパターンにマッチするか確認
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
- **`Pattern.compile(regex)`**: 正規表現文字列を`Pattern`オブジェクトにコンパイルします。
- **`pattern.matcher(email)`**: 入力文字列`email`に対する`Matcher`を作成します。
- **`matcher.matches()`**: 文字列全体がパターンにマッチする場合は`true`、それ以外は`false`を返します。

**出力**: `有効なメールアドレス`

注: これは簡略化されたメールパターンです。実際のメールアドレス検証にはより複雑な正規表現（RFC 5322準拠など）が必要ですが、ここでは入門用として紹介しています。

## 例2: 文字列内のすべてのハッシュタグを検索

ツイートからすべてのハッシュタグ（例: `#java`）を抽出したい場合を考えます。正規表現`"#\\w+"`を使用します。ここで、`#`はハッシュタグ記号そのものにマッチし、`\\w+`は1つ以上の単語文字（英字、数字、アンダースコア）にマッチします。

```java
import java.util.regex.*;

public class HashtagExtractor {
    public static void main(String[] args) {
        String tweet = "これは#sampleツイートで、#multipleや#javaのような#複数のハッシュタグがあります";
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
- **`matcher.find()`**: 入力文字列内で次のマッチに移動し、マッチが見つかった場合は`true`を返します。
- **`matcher.group()`**: 現在のマッチに該当するテキストを返します。

**出力**:
```
#sample
#multiple
#java
```

## 例3: 正規表現を使用したテキストの置換

特定の単語（例: "badword"をアスタリスクで置き換えて検閲する）のすべての出現を置換するには、内部的に正規表現を使用する`String.replaceAll()`メソッドを使用できます。

```java
public class TextCensor {
    public static void main(String[] args) {
        String text = "これはbadwordの例で、badwordが繰り返されています。";
        String censored = text.replaceAll("badword", "*******");
        System.out.println(censored);
    }
}
```

**出力**: `これは*******の例で、*******が繰り返されています。`

より複雑な置換には、`Matcher`を使用します：

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

## 例4: グループを使用した構造化データの解析

正規表現のグループ（括弧`()`で定義）を使用すると、マッチの一部をキャプチャできます。例えば、`123-45-6789`のような社会保障番号（SSN）を解析する場合：

```java
import java.util.regex.*;

public class SSNParser {
    public static void main(String[] args) {
        String ssn = "123-45-6789";
        String regex = "(\\d{3})-(\\d{2})-(\\d{4})"; // 地域番号、グループ番号、シリアル番号のグループ
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(ssn);

        if (matcher.matches()) {
            System.out.println("地域番号: " + matcher.group(1));
            System.out.println("グループ番号: " + matcher.group(2));
            System.out.println("シリアル番号: " + matcher.group(3));
        }
    }
}
```

### 説明
- **`"(\\d{3})-(\\d{2})-(\\d{4})"`**: 3つのグループを定義：
  - グループ1: `\\d{3}`（3桁の数字）
  - グループ2: `\\d{2}`（2桁の数字）
  - グループ3: `\\d{4}`（4桁の数字）
- **`matcher.group(n)`**: グループ`n`（1から始まるインデックス）でマッチしたテキストを取得します。

**出力**:
```
地域番号: 123
グループ番号: 45
シリアル番号: 6789
```

明確さのために**名前付きグループ**も使用できます：

```java
String regex = "(?<area>\\d{3})-(?<group>\\d{2})-(?<serial>\\d{4})";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher("123-45-6789");
if (matcher.matches()) {
    System.out.println("地域: " + matcher.group("area"));
    System.out.println("グループ: " + matcher.group("group"));
    System.out.println("シリアル: " + matcher.group("serial"));
}
```

## 追加機能とヒント

### フラグ
`Pattern.compile()`でフラグを使用してパターンの動作を変更できます：
- **`Pattern.CASE_INSENSITIVE`**: マッチング時に大文字小文字を区別しません。
  ```java
  Pattern pattern = Pattern.compile("hello", Pattern.CASE_INSENSITIVE);
  Matcher matcher = pattern.matcher("HELLO");
  System.out.println(matcher.matches()); // true
  ```

### Stringメソッド
単純なタスクには、`String`メソッドを使用します：
- **`matches()`**: 文字列全体が正規表現にマッチするか確認します。
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
正規表現では、`.`、`*`、`?`などの特殊文字を使用します。これらを文字通りにマッチさせるには、`\\`でエスケープします：
- ピリオドにマッチ: `"\\."`
- Javaの文字列では、バックスラッシュをエスケープ: 数字には`"\\d"`、バックスラッシュそのものには`"\\\\"`。

### パフォーマンス
パターンのコンパイルはコストがかかります。可能な場合は`Pattern`オブジェクトを再利用します：
```java
Pattern pattern = Pattern.compile("\\d+"); // 一度コンパイル
for (String input : new String[]{"123", "456"}) {
    Matcher matcher = pattern.matcher(input);
    if (matcher.matches()) {
        System.out.println("数値: " + input);
    }
}
```

### エラーハンドリング
無効な正規表現パターンは`PatternSyntaxException`をスローします。本番コードではこれを処理します：
```java
try {
    Pattern pattern = Pattern.compile("["); // 無効な正規表現
} catch (PatternSyntaxException e) {
    System.err.println("無効な正規表現: " + e.getMessage());
}
```

## まとめ

- **パターンのコンパイル**: `Pattern.compile(regex)`
- **マッチャーの作成**: `pattern.matcher(input)`
- **主要な操作**:
  - `matches()`: 文字列全体のマッチ
  - `find()`: 次のマッチを検索
  - `group()`: マッチしたテキストを抽出
  - `replaceAll()`: マッチを置換
- **便利な機能**: 単純なタスクには`String`メソッドを使用。
- **ベストプラクティス**: 特殊文字をエスケープ、パターンを再利用、例外を処理。

これで`java.util.regex`の基本を網羅しました。先読みや文字クラスなどの高度なトピックについては、[Javaドキュメント](https://docs.oracle.com/en/java/javase/17/docs/api/java.util.regex/package-summary.html)を参照するか、具体的なユースケースで実験してみてください！