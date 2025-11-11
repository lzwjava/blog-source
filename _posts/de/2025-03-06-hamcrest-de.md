---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von Hamcrest Matchern in Java-Tests
translated: true
type: note
---

Ich führe Sie durch die Verwendung von Hamcrest-Matchern in Java. Hamcrest ist ein Framework, das eine Reihe von Matcher-Objekten bereitstellt, um lesbarere Assertions in Tests zu schreiben.

1. Fügen Sie zunächst die Hamcrest-Abhängigkeit zu Ihrem Projekt hinzu:

Für Maven, fügen Sie dies zur pom.xml hinzu:
```xml
<dependency>
    <groupId>org.hamcrest</groupId>
    <artifactId>hamcrest</artifactId>
    <version>2.2</version>
    <scope>test</scope>
</dependency>
```

Für Gradle, fügen Sie dies zur build.gradle hinzu:
```groovy
testImplementation 'org.hamcrest:hamcrest:2.2'
```

2. Hier ist ein grundlegendes Beispiel für die Verwendung von Hamcrest mit JUnit:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;  // Importiere gängige Matcher

import org.junit.Test;

public class ExampleTest {
    @Test
    public void testExamples() {
        // Grundlegende Gleichheit
        assertThat(5, is(5));
        
        // String-Matching
        String text = "Hello World";
        assertThat(text, containsString("World"));
        assertThat(text, startsWith("Hello"));
        
        // Collection-Matching
        List<String> items = Arrays.asList("apple", "banana", "orange");
        assertThat(items, hasItem("banana"));
        assertThat(items, hasSize(3));
        
        // Zahlenvergleiche
        assertThat(10, greaterThan(5));
        assertThat(3.14, closeTo(3.0, 0.2));
    }
}
```

3. Gängige Hamcrest-Matcher:
- `is()`: Testet Gleichheit
- `equalTo()`: Testet Objektgleichheit
- `containsString()`: Prüft, ob String Teilstring enthält
- `startsWith()`/ `endsWith()`: String-Präfix/Suffix-Prüfung
- `greaterThan()`/ `lessThan()`: Numerische Vergleiche
- `hasItem()`: Prüft, ob Collection ein Element enthält
- `hasSize()`: Prüft die Collection-Größe
- `closeTo()`: Prüft, ob Zahl innerhalb eines Bereichs liegt
- `not()`: Negiert jeden Matcher
- `allOf()`: Kombiniert mehrere Matcher (UND)
- `anyOf()`: Kombiniert mehrere Matcher (ODER)

4. Beispiel für benutzerdefinierten Matcher:
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
                description.appendText("ein Palindrom");
            }
        };
    }
}

// Verwendung:
@Test
public void testPalindrome() {
    assertThat("racecar", isPalindrome());
}
```

5. Matcher kombinieren:
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

Wichtige Vorteile:
- Lesbarere Test-Assertions
- Bessere Fehlermeldungen
- Flexible Matching-Bedingungen
- Erweiterbar mit benutzerdefinierten Matchern

Tipps:
- Verwenden Sie `import static`, um Code prägnanter zu machen
- Kombinieren Sie Matcher für komplexe Bedingungen
- Überprüfen Sie die Hamcrest-Dokumentation für den vollständigen Satz an Matchern
- Hamcrest funktioniert gut mit JUnit, TestNG und anderen Test-Frameworks

Möchten Sie, dass ich einen bestimmten Matcher näher erläutere oder weitere Beispiele zeige?