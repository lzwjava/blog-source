---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Hamcrest Matchers 在 Java 測試中
translated: true
---

讓我帶你了解如何在 Java 中使用 Hamcrest matchers。Hamcrest 是一個提供一組 matcher 對象的框架，用於編寫更易讀的測試斷言。

1. 首先，將 Hamcrest 依賴項添加到您的項目中：

對於 Maven，將以下內容添加到您的 pom.xml：
```xml
<dependency>
    <groupId>org.hamcrest</groupId>
    <artifactId>hamcrest</artifactId>
    <version>2.2</version>
    <scope>test</scope>
</dependency>
```

對於 Gradle，將以下內容添加到您的 build.gradle：
```groovy
testImplementation 'org.hamcrest:hamcrest:2.2'
```

2. 以下是使用 Hamcrest 與 JUnit 的基本示例：

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;  // 導入常用 matcher

import org.junit.Test;

public class ExampleTest {
    @Test
    public void testExamples() {
        // 基本相等性
        assertThat(5, is(5));

        // 字符串匹配
        String text = "Hello World";
        assertThat(text, containsString("World"));
        assertThat(text, startsWith("Hello"));

        // 集合匹配
        List<String> items = Arrays.asList("apple", "banana", "orange");
        assertThat(items, hasItem("banana"));
        assertThat(items, hasSize(3));

        // 數字比較
        assertThat(10, greaterThan(5));
        assertThat(3.14, closeTo(3.0, 0.2));
    }
}
```

3. 常見的 Hamcrest Matchers：
- `is()`：測試相等性
- `equalTo()`：測試對象相等性
- `containsString()`：檢查字符串是否包含子字符串
- `startsWith()`/ `endsWith()`：字符串前綴/後綴檢查
- `greaterThan()`/ `lessThan()`：數值比較
- `hasItem()`：檢查集合是否包含元素
- `hasSize()`：檢查集合大小
- `closeTo()`：檢查數字是否在範圍內
- `not()`：否定任何 matcher
- `allOf()`：組合多個 matcher（AND）
- `anyOf()`：組合多個 matcher（OR）

4. 自定義 Matcher 示例：
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

// 使用：
@Test
public void testPalindrome() {
    assertThat("racecar", isPalindrome());
}
```

5. 組合 Matchers：
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

主要優點：
- 更易讀的測試斷言
- 更好的失敗消息
- 靈活的匹配條件
- 可擴展的自定義 matcher

提示：
- 使用 `import static` 使代碼更簡潔
- 組合 matcher 以處理複雜條件
- 查看 Hamcrest 文檔以獲取完整的 matcher 集合
- Hamcrest 可以與 JUnit、TestNG 和其他測試框架很好地配合使用

您是否希望我詳細說明任何特定的 matcher 或顯示更多示例？