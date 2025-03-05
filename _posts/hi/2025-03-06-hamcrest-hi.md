---
audio: false
generated: true
lang: hi
layout: post
title: Hamcrest Matchers को Java Tests में उपयोग करना
translated: true
---

मुझे आपको Java में Hamcrest matchers का उपयोग करने में मार्गदर्शन करने दो। Hamcrest एक फ्रेमवर्क है जो टेस्ट में अधिक पढ़ने योग्य दावों लिखने के लिए एक सेट ऑफ मेचर ऑब्जेक्ट प्रदान करता है।

1. पहले, अपने प्रोजेक्ट में Hamcrest निर्भरता जोड़ें:

Maven के लिए, अपने pom.xml में यह जोड़ें:
```xml
<dependency>
    <groupId>org.hamcrest</groupId>
    <artifactId>hamcrest</artifactId>
    <version>2.2</version>
    <scope>test</scope>
</dependency>
```

Gradle के लिए, अपने build.gradle में यह जोड़ें:
```groovy
testImplementation 'org.hamcrest:hamcrest:2.2'
```

2. यहाँ Hamcrest का JUnit के साथ उपयोग करने का एक बुनियादी उदाहरण है:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;  // सामान्य मेचर इम्पोर्ट करें

import org.junit.Test;

public class ExampleTest {
    @Test
    public void testExamples() {
        // बुनियादी समानता
        assertThat(5, is(5));

        // स्ट्रिंग मैचिंग
        String text = "Hello World";
        assertThat(text, containsString("World"));
        assertThat(text, startsWith("Hello"));

        // संग्रह मैचिंग
        List<String> items = Arrays.asList("apple", "banana", "orange");
        assertThat(items, hasItem("banana"));
        assertThat(items, hasSize(3));

        // संख्या तुलनाएँ
        assertThat(10, greaterThan(5));
        assertThat(3.14, closeTo(3.0, 0.2));
    }
}
```

3. आम Hamcrest Matchers:
- `is()`: समानता परीक्षण करता है
- `equalTo()`: ऑब्जेक्ट समानता परीक्षण करता है
- `containsString()`: स्ट्रिंग में उप-स्ट्रिंग है कि नहीं
- `startsWith()`/ `endsWith()`: स्ट्रिंग प्रीफिक्स/सफिक्स जांच
- `greaterThan()`/ `lessThan()`: संख्यात्मक तुलनाएँ
- `hasItem()`: संग्रह में एक तत्व है कि नहीं
- `hasSize()`: संग्रह आकार जांच
- `closeTo()`: संख्या एक रेंज में है कि नहीं
- `not()`: किसी भी मेचर को नकार देता है
- `allOf()`: कई मेचर को संयोजित करता है (एंड)
- `anyOf()`: कई मेचर को संयोजित करता है (ओर)

4. कस्टम मेचर उदाहरण:
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
                description.appendText("एक पलिंड्रोम");
            }
        };
    }
}

// उपयोग:
@Test
public void testPalindrome() {
    assertThat("racecar", isPalindrome());
}
```

5. मेचर संयोजित करना:
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

मुख्य लाभ:
- अधिक पढ़ने योग्य टेस्ट दावे
- बेहतर विफलता संदेश
- लचीले मैचिंग शर्तें
- कस्टम मेचर के साथ विस्तार

टिप्स:
- `import static` का उपयोग करें ताकि कोड को संक्षिप्त बनाया जा सके
- जटिल शर्तों के लिए मेचर संयोजित करें
- Hamcrest दस्तावेज़ देखें पूरी मेचर सेट के लिए
- Hamcrest JUnit, TestNG और अन्य टेस्टिंग फ्रेमवर्क के साथ अच्छी तरह काम करता है

क्या आप किसी विशेष मेचर पर विस्तार करना चाहते हैं या और उदाहरण दिखाना चाहते हैं?