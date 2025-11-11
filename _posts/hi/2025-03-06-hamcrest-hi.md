---
audio: false
generated: true
lang: hi
layout: post
title: जावा परीक्षणों में हैमक्रेस्ट मैचर्स का उपयोग
translated: true
type: note
---

मैं आपको Java में Hamcrest matchers का उपयोग करने के बारे में मार्गदर्शन करता हूँ। Hamcret एक ऐसा फ्रेमवर्क है जो परीक्षणों में अधिक पठनीय दावे (assertions) लिखने के लिए matcher objects का एक सेट प्रदान करता है।

1. सबसे पहले, अपने प्रोजेक्ट में Hamcrest निर्भरता (dependency) जोड़ें:

Maven के लिए, इसे अपनी pom.xml फाइल में जोड़ें:
```xml
<dependency>
    <groupId>org.hamcrest</groupId>
    <artifactId>hamcrest</artifactId>
    <version>2.2</version>
    <scope>test</scope>
</dependency>
```

Gradle के लिए, इसे अपनी build.gradle फाइल में जोड़ें:
```groovy
testImplementation 'org.hamcrest:hamcrest:2.2'
```

2. JUnit के साथ Hamcrest का उपयोग करने का एक बुनियादी उदाहरण यहां दिया गया है:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;  // सामान्य matchers को import करें

import org.junit.Test;

public class ExampleTest {
    @Test
    public void testExamples() {
        // बुनियादी समानता
        assertThat(5, is(5));
        
        // स्ट्रिंग मिलान
        String text = "Hello World";
        assertThat(text, containsString("World"));
        assertThat(text, startsWith("Hello"));
        
        // संग्रह (collection) मिलान
        List<String> items = Arrays.asList("apple", "banana", "orange");
        assertThat(items, hasItem("banana"));
        assertThat(items, hasSize(3));
        
        // संख्या तुलना
        assertThat(10, greaterThan(5));
        assertThat(3.14, closeTo(3.0, 0.2));
    }
}
```

3. सामान्य Hamcrest Matchers:
- `is()`: समानता का परीक्षण करता है
- `equalTo()`: वस्तु समानता का परीक्षण करता है
- `containsString()`: जांचता है कि क्या स्ट्रिंग में उपस्ट्रिंग है
- `startsWith()`/ `endsWith()`: स्ट्रिंग उपसर्ग/प्रत्यय जांच
- `greaterThan()`/ `lessThan()`: संख्यात्मक तुलना
- `hasItem()`: जांचता है कि क्या संग्रह में कोई तत्व है
- `hasSize()`: संग्रह का आकार जांचता है
- `closeTo()`: जांचता है कि क्या संख्या एक सीमा के भीतर है
- `not()`: किसी भी matcher को नकारता है
- `allOf()`: कई matchers को जोड़ता है (AND)
- `anyOf()`: कई matchers को जोड़ता है (OR)

4. कस्टम Matcher उदाहरण:
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

// उपयोग:
@Test
public void testPalindrome() {
    assertThat("racecar", isPalindrome());
}
```

5. Matchers को जोड़ना:
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
- अधिक पठनीय परीक्षण दावे (assertions)
- बेहतर विफलता संदेश
- लचीली मिलान शर्तें
- कस्टम matchers के साथ विस्तार योग्य

सुझाव:
- कोड को अधिक संक्षिप्त बनाने के लिए `import static` का उपयोग करें
- जटिल शर्तों के लिए matchers को जोड़ें
- matchers के पूर्ण सेट के लिए Hamcrest दस्तावेज़ देखें
- Hamcrest JUnit, TestNG और अन्य परीक्षण फ्रेमवर्क के साथ अच्छी तरह काम करता है

क्या आप किसी विशेष matcher पर अधिक विस्तार से चर्चा करना चाहेंगे या और उदाहरण देखना चाहेंगे?