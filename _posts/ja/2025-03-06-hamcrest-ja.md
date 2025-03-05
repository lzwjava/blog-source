---
audio: false
generated: true
lang: ja
layout: post
title: Hamcrest MatchersをJavaテストで使用する
translated: true
---

HamcrestマッチャーをJavaで使う方法を案内します。Hamcrestは、テストでより読みやすいアサーションを書くためのマッチャーオブジェクトのセットを提供するフレームワークです。

1. まず、プロジェクトにHamcrestの依存関係を追加します：

Mavenの場合、pom.xmlに以下を追加します：
```xml
<dependency>
    <groupId>org.hamcrest</groupId>
    <artifactId>hamcrest</artifactId>
    <version>2.2</version>
    <scope>test</scope>
</dependency>
```

Gradleの場合、build.gradleに以下を追加します：
```groovy
testImplementation 'org.hamcrest:hamcrest:2.2'
```

2. JUnitとHamcrestを使った基本的な例：

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;  // 一般的なマッチャーをインポート

import org.junit.Test;

public class ExampleTest {
    @Test
    public void testExamples() {
        // 基本的な等価性
        assertThat(5, is(5));

        // 文字列のマッチング
        String text = "Hello World";
        assertThat(text, containsString("World"));
        assertThat(text, startsWith("Hello"));

        // コレクションのマッチング
        List<String> items = Arrays.asList("apple", "banana", "orange");
        assertThat(items, hasItem("banana"));
        assertThat(items, hasSize(3));

        // 数値の比較
        assertThat(10, greaterThan(5));
        assertThat(3.14, closeTo(3.0, 0.2));
    }
}
```

3. 一般的なHamcrestマッチャー：
- `is()`: 等価性をテスト
- `equalTo()`: オブジェクトの等価性をテスト
- `containsString()`: 文字列が部分文字列を含むかどうかをチェック
- `startsWith()`/ `endsWith()`: 文字列の接頭辞/接尾辞をチェック
- `greaterThan()`/ `lessThan()`: 数値の比較
- `hasItem()`: コレクションに要素が含まれているかどうかをチェック
- `hasSize()`: コレクションのサイズをチェック
- `closeTo()`: 数値が範囲内にあるかどうかをチェック
- `not()`: 任意のマッチャーを否定
- `allOf()`: 複数のマッチャーを組み合わせる（AND）
- `anyOf()`: 複数のマッチャーを組み合わせる（OR）

4. カスタムマッチャーの例：
```java
import org.hamcrest.BaseMatcher;
import org.hamcrest.Description;
import org.hamcrest.Matcher;

public class CustomMatchers {
    public static Matcher<String> isPalindrome() {
        return new BaseMatcher<String>() {
            @Override
            public boolean matches(Object item) {
                String str = (String) item;
                String reversed = new StringBuilder(str).reverse().toString();
                return str.equals(reversed);
            }

            @Override
            public void describeTo(Description description) {
                description.appendText("a palindrome");
            }
        };
    }
}

// 使用例：
@Test
public void testPalindrome() {
    assertThat("racecar", isPalindrome());
}
```

5. マッチャーの組み合わせ：
```java
@Test
public void testCombined() {
    List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
    assertThat(numbers, allOf(
        hasSize(5),
        hasItem(greaterThan(4)),
        everyItem(lessThan(10))
    ));
}
```

主要な利点：
- より読みやすいテストアサーション
- より良い失敗メッセージ
- 柔軟なマッチング条件
- カスタムマッチャーで拡張可能

ヒント：
- `import static`を使ってコードを簡潔にする
- 複雑な条件のためにマッチャーを組み合わせる
- Hamcrestのドキュメントを確認してマッチャーの全セットを確認する
- HamcrestはJUnit、TestNG、その他のテストフレームワークとよく組み合わせられる

特定のマッチャーについて詳しく説明したり、さらに例を示したりしたいですか？