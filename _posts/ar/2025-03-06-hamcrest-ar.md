---
audio: false
generated: true
lang: ar
layout: post
title: استخدام مقارنات هامكريست في اختبارات جافا
translated: true
type: note
---

دعني أرشدك خلال استخدام مطابقات Hamcrest في Java. Hamcret هو إطار عمل يوفر مجموعة من كائنات المطابقة لكتابة تأكيدات أكثر قابلية للقراءة في الاختبارات.

1. أولاً، أضف تبعية Hamcrest إلى مشروعك:

بالنسبة لـ Maven، أضف هذا إلى ملف pom.xml:
```xml
<dependency>
    <groupId>org.hamcrest</groupId>
    <artifactId>hamcrest</artifactId>
    <version>2.2</version>
    <scope>test</scope>
</dependency>
```

بالنسبة لـ Gradle، أضف هذا إلى ملف build.gradle:
```groovy
testImplementation 'org.hamcrest:hamcrest:2.2'
```

2. إليك مثالاً أساسياً لاستخدام Hamcrest مع JUnit:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;  // استيراد المطابقات الشائعة

import org.junit.Test;

public class ExampleTest {
    @Test
    public void testExamples() {
        // المساواة الأساسية
        assertThat(5, is(5));
        
        // مطابقة النصوص
        String text = "Hello World";
        assertThat(text, containsString("World"));
        assertThat(text, startsWith("Hello"));
        
        // مطابقة المجموعات
        List<String> items = Arrays.asList("apple", "banana", "orange");
        assertThat(items, hasItem("banana"));
        assertThat(items, hasSize(3));
        
        // مقارنات الأرقام
        assertThat(10, greaterThan(5));
        assertThat(3.14, closeTo(3.0, 0.2));
    }
}
```

3. مطابقات Hamcrest الشائعة:
- `is()`: يختبر المساواة
- `equalTo()`: يختبر مساواة الكائنات
- `containsString()`: يتحقق مما إذا كان النص يحتوي على جزء نصي فرعي
- `startsWith()`/ `endsWith()`: التحقق من البادئة/اللاحقة للنص
- `greaterThan()`/ `lessThan()`: مقارنات رقمية
- `hasItem()`: يتحقق مما إذا كانت المجموعة تحتوي على عنصر
- `hasSize()`: يتحقق من حجم المجموعة
- `closeTo()`: يتحقق مما إذا كان الرقم ضمن نطاق محدد
- `not()`: ينفي أي مطابقة
- `allOf()`: يجمع عدة مطابقات (AND)
- `anyOf()`: يجمع عدة مطابقات (OR)

4. مثال على مطابقة مخصصة:
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
                description.appendText("نص متماثل");
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

5. دمج المطابقات:
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

الفوائد الرئيسية:
- تأكيدات اختبار أكثر قابلية للقراءة
- رسائل فشل أفضل
- شروط مطابقة مرنة
- قابلة للتوسيع بمطابقات مخصصة

نصائح:
- استخدم `import static` لجعل الكود أكثر إيجازاً
- ادمج المطابقات للشروط المعقدة
- راجع وثائق Hamcrest للحصول على المجموعة الكاملة من المطابقات
- يعمل Hamcrest بشكل جيد مع JUnit و TestNG وأطر عمل الاختبار الأخرى

هل تريد مني شرح أي مطابقة محددة أو عرض المزيد من الأمثلة؟