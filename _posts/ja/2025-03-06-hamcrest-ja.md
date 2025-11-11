---
audio: false
generated: true
lang: ja
layout: post
title: JavaテストでのHamcrestマッチャーの使い方
translated: true
type: note
---

JavaでHamcrestマッチャーを使用する方法をご案内します。Hamcrestは、テスト内でより読みやすいアサーションを書くためのマッチャーオブジェクトのセットを提供するフレームワークです。

1. まず、プロジェクトにHamcrestの依存関係を追加します：

Mavenの場合、pom.xmlに以下を追加：
```xml
<dependency>
    <groupId>org.hamcrest</groupId>
    <artifactId>hamcrest</artifactId>
    <version>2.2</version>
    <scope>test</scope>
</dependency>
```

Gradleの場合、build.gradleに以下を追加：
```groovy
testImplementation 'org.hamcrest:hamcrest:2.2'
```

2. JUnitでHamcrestを使用する基本的な例：

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;  // 一般的なマッチャーをインポート

import org.junit.Test;

public class ExampleTest {
    @Test
    public void testExamples() {
        // 基本的な等価性
        assertThat(5, is(5));
        
        // 文字列マッチング
        String text = "Hello World";
        assertThat(text, containsString("World"));
        assertThat(text, startsWith("Hello"));
        
        // コレクションマッチング
        List<String> items = Arrays.asList("apple", "banana", "orange");
        assertThat(items, hasItem("banana"));
        assertThat(items, hasSize(3));
        
        // 数値比較
        assertThat(10, greaterThan(5));
        assertThat(3.14, closeTo(3.0, 0.2));
    }
}
```

3. 一般的なHamcrestマッチャー：
- `is()`: 等価性テスト
- `equalTo()`: オブジェクトの等価性テスト
- `containsString()`: 文字列が部分文字列を含むかチェック
- `startsWith()`/ `endsWith()`: 文字列の接頭辞/接尾辞チェック
- `greaterThan()`/ `lessThan()`: 数値比較
- `hasItem()`: コレクションが要素を含むかチェック
- `hasSize()`: コレクションサイズチェック
- `closeTo()`: 数値が範囲内かチェック
- `not()`: 任意のマッチャーを否定
- `allOf()`: 複数のマッチャーを結合（AND）
- `anyOf()`: 複数のマッチャーを結合（OR）

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

主な利点：
- より読みやすいテストアサーション
- より良い失敗メッセージ
- 柔軟なマッチング条件
- カスタムマッチャーで拡張可能

ヒント：
- `import static`を使用してコードを簡潔に
- 複雑な条件にはマッチャーを組み合わせる
- 完全なマッチャーセットはHamcrestドキュメントを確認
- HamcrestはJUnit、TestNG、その他のテストフレームワークと連携良好

特定のマッチャーについて詳しく説明が必要ですか？または他の例を見たいですか？