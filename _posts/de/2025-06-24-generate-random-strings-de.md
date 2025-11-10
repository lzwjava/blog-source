---
audio: false
generated: true
lang: de
layout: post
title: Erstellen von Zufallszeichenketten mit Apache Commons Lang
translated: true
type: note
---

`RandomStringUtils` ist eine äußerst nützliche Klasse aus der Apache Commons Lang-Bibliothek, die verschiedene statische Methoden zur Erzeugung zufälliger Zeichenketten bereitstellt. Dazu gehört das Generieren von Zeichenketten mit bestimmten Längen, die nur Buchstaben, nur Zahlen, alphanumerische Zeichen oder sogar Zeichen aus einem benutzerdefinierten Zeichensatz enthalten.

So verwenden Sie sie und die notwendige Maven-Abhängigkeit:

## Wie man `org.apache.commons.lang3.RandomStringUtils;` verwendet

Zuerst müssen Sie die Klasse in Ihrer Java-Datei importieren:

```java
import org.apache.commons.lang3.RandomStringUtils;
```

Dann können Sie ihre statischen Methoden verwenden. Hier sind einige gängige Beispiele:

1.  **Generiere eine zufällige alphanumerische Zeichenkette einer bestimmten Länge:**

    ```java
    String randomAlphaNumeric = RandomStringUtils.randomAlphanumeric(10);
    System.out.println("Zufällige alphanumerische Zeichenkette: " + randomAlphaNumeric); // z.B. "aB5cY2x9Pq"
    ```

2.  **Generiere eine zufällige alphabetische Zeichenkette einer bestimmten Länge:**

    ```java
    String randomAlphabetic = RandomStringUtils.randomAlphabetic(8);
    System.out.println("Zufällige alphabetische Zeichenkette: " + randomAlphabetic); // z.B. "GhJkLmNo"
    ```

3.  **Generiere eine zufällige numerische Zeichenkette einer bestimmten Länge:**

    ```java
    String randomNumeric = RandomStringUtils.randomNumeric(6);
    System.out.println("Zufällige numerische Zeichenkette: " + randomNumeric); // z.B. "123456"
    ```

4.  **Generiere eine zufällige Zeichenkette mit einer Mischung aus Buchstaben und Zahlen, unter Angabe von Flags:**

    ```java
    String randomLettersAndNumbers = RandomStringUtils.random(12, true, true);
    System.out.println("Zufällige Zeichenkette mit Buchstaben und Zahlen: " + randomLettersAndNumbers); // z.B. "abC123DeF456"
    ```

5.  **Generiere eine zufällige Zeichenkette aus einem benutzerdefinierten Zeichensatz:**

    ```java
    String chars = "abcdefg";
    String randomFromCustomSet = RandomStringUtils.random(5, chars);
    System.out.println("Zufällige Zeichenkette aus benutzerdefiniertem Set: " + randomFromCustomSet); // z.B. "gcfae"
    ```

## Welche Bibliothek in `pom.xml` zu verwenden ist

Um `RandomStringUtils` in einem Maven-Projekt zu verwenden, müssen Sie die `commons-lang3`-Abhängigkeit zu Ihrer `pom.xml`-Datei hinzufügen.

Hier ist der Abhängigkeits-Snippet:

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.14.0</version> </dependency>
```

**Wichtige Hinweise:**

  * **Version:** Überprüfen Sie immer [Maven Central](https://mvnrepository.com/artifact/org.apache.commons/commons-lang3) auf die neueste stabile Version von `commons-lang3`. Zum Zeitpunkt meiner letzten Aktualisierung ist `3.14.0` oder höher eine gute Wahl, aber es ist immer am besten, die absolut neueste verfügbare stabile Version zu verwenden.
  * **Scope:** Der Standard-Scope für Abhängigkeiten ist `compile`, was normalerweise für Utility-Bibliotheken wie diese gewünscht ist. Es bedeutet, dass das JAR während der Kompilierung, Tests und Laufzeit verfügbar ist. Wenn Sie es nur für Tests verwenden würden, könnten Sie `<scope>test</scope>` verwenden.
  * **Veraltung:** Beachten Sie, dass einige ältere Methoden wie `RandomStringUtils.randomAlphabetic(int count)` in neueren Versionen von Apache Commons Lang 3 als veraltet markiert sind. Stattdessen wird die Verwendung der Methoden `secure()`, `secureStrong()` oder `insecure()` empfohlen, die mehr Kontrolle über die Zufallsquelle bieten. Zum Beispiel: `RandomStringUtils.secure().nextAlphanumeric(10)`. Die älteren Methoden funktionieren jedoch weiterhin für viele Anwendungsfälle.