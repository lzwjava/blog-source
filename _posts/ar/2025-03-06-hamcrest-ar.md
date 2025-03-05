---
audio: false
generated: true
lang: ar
layout: post
title: استخدام Hamcrest Matchers في اختبارات Java
translated: true
---

أرشدك في استخدام Hamcrest matchers في Java. Hamcrest هو إطار يعمل على توفير مجموعة من كائنات المقارنة لتكتب تصريحات أكثر قابلية للقراءة في الاختبارات.

1. أولاً، أضف التبعية Hamcrest إلى مشروعك:

للمباني، أضف هذا إلى ملفك pom.xml:
```xml
<dependency>
    <groupId>org.hamcrest</groupId>
    <artifactId>hamcrest</artifactId>
    <version>2.2</version>
    <scope>test</scope>
</dependency>
```

لغرادل، أضف هذا إلى ملفك build.gradle:
```groovy
testImplementation 'org.hamcrest:hamcrest:2.2'
```

2. إليك مثال أساسي لاستخدام Hamcrest مع JUnit:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;  // استيراد المقارنات الشائعة

import org.junit.Test;

public class ExampleTest {
    @Test
    public void testExamples() {
        // المساواة الأساسية
        assertThat(5, is(5));

        // تطابق النص
        String text = "Hello World";
        assertThat(text, containsString("World"));
        assertThat(text, startsWith("Hello"));

        // تطابق المجموعات
        List<String> items = Arrays.asList("apple", "banana", "orange");
        assertThat(items, hasItem("banana"));
        assertThat(items, hasSize(3));

        // المقارنات العددية
        assertThat(10, greaterThan(5));
        assertThat(3.14, closeTo(3.0, 0.2));
    }
}
```

3. المقارنات الشائعة في Hamcrest:
- `is()`: يجرى اختبار المساواة
- `equalTo()`: يجرى اختبار المساواة بين الكائنات
- `containsString()`: يجرى فحص ما إذا كان النص يحتوي على نص فرعي
- `startsWith()`/ `endsWith()`: فحص البادئة/اللاحقة للنص
- `greaterThan()`/ `lessThan()`: المقارنات العددية
- `hasItem()`: يجرى فحص ما إذا كانت المجموعة تحتوي على عنصر
- `hasSize()`: يجرى فحص حجم المجموعة
- `closeTo()`: يجرى فحص ما إذا كان العدد ضمن نطاق
- `not()`: ينفي أي مقارنات
- `allOf()`: يجمع بين عدة مقارنات (و)
- `anyOf()`: يجمع بين عدة مقارنات (أو)

4. مثال على المقارنات المخصصة:
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

// الاستخدام:
@Test
public void testPalindrome() {
    assertThat("racecar", isPalindrome());
}
```

5. الجمع بين المقارنات:
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

المزايا الرئيسية:
- تصريحات اختبار أكثر قابلية للقراءة
- رسائل فشل أفضل
- شروط المقارنة مرنة
- قابل للتوسيع مع المقارنات المخصصة

نصائح:
- استخدم `import static` لجعل الكود أكثر إحكامًا
- قم بجمع المقارنات لشروط معقدة
- تحقق من وثائق Hamcrest للحصول على مجموعة كاملة من المقارنات
- يعمل Hamcrest بشكل جيد مع JUnit، TestNG، وأطر الاختبار الأخرى

هل ترغب في أن أشرح أي مقارنات محددة أو أن أظهر أمثلة أخرى؟