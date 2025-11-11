---
audio: false
generated: true
lang: hant
layout: post
title: 在 Java 測試中使用 Hamcrest 匹配器
translated: true
type: note
---

讓我引導你使用 Java 中的 Hamcrest 匹配器。Hamcrest 是一個框架，提供了一組匹配器物件，用於編寫更易讀的測試斷言。

1. 首先，將 Hamcrest 依賴項添加到你的專案中：

若使用 Maven，請在 pom.xml 中添加：
```xml
<dependency>
    <groupId>org.hamcrest</groupId>
    <artifactId>hamcrest</artifactId>
    <version>2.2</version>
    <scope>test</scope>
</dependency>
```

若使用 Gradle，請在 build.gradle 中添加：
```groovy
testImplementation 'org.hamcrest:hamcrest:2.2'
```

2. 以下是使用 Hamcrest 與 JUnit 的基本範例：

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;  // 導入常用匹配器

import org.junit.Test;

public class ExampleTest {
    @Test
    public void testExamples() {
        // 基本相等性
        assertThat(5, is(5));
        
        // 字串匹配
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

3. 常用 Hamcrest 匹配器：
- `is()`：測試相等性
- `equalTo()`：測試物件相等性
- `containsString()`：檢查字串是否包含子字串
- `startsWith()`/ `endsWith()`：字串前綴/後綴檢查
- `greaterThan()`/ `lessThan()`：數值比較
- `hasItem()`：檢查集合是否包含元素
- `hasSize()`：檢查集合大小
- `closeTo()`：檢查數字是否在範圍內
- `not()`：否定任何匹配器
- `allOf()`：組合多個匹配器（AND）
- `anyOf()`：組合多個匹配器（OR）

4. 自定義匹配器範例：
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

// 用法：
@Test
public void testPalindrome() {
    assertThat("racecar", isPalindrome());
}
```

5. 組合匹配器：
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
- 更好的失敗訊息
- 靈活的匹配條件
- 可擴展自定義匹配器

提示：
- 使用 `import static` 使程式碼更簡潔
- 組合匹配器處理複雜條件
- 查閱 Hamcrest 文檔以獲取完整的匹配器集合
- Hamcrest 與 JUnit、TestNG 和其他測試框架配合良好

你想了解任何特定匹配器的詳細資訊或需要更多範例嗎？