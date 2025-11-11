---
audio: false
generated: true
lang: de
layout: post
title: Reguläre Ausdrücke in Java
translated: true
type: note
---

# Verwendung von `java.util.regex` in Java

Das Paket `java.util.regex` in Java bietet Werkzeuge für die Arbeit mit regulären Ausdrücken (Regex), die Muster zur Textsuche und -manipulation darstellen. Diese Anleitung führt Sie durch die Grundlagen der Verwendung dieses Pakets und konzentriert sich auf die beiden Hauptklassen: `Pattern` und `Matcher`. Ich werde auch gängige Anwendungsfälle mit Beispielen behandeln, um Ihnen den Einstieg zu erleichtern.

## Überblick über `java.util.regex`

Das Paket `java.util.regex` umfasst:

- **`Pattern`**: Stellt einen kompilierten regulären Ausdruck dar. Sie erstellen ihn aus einem Regex-String.
- **`Matcher`**: Wendet das Muster auf einen bestimmten Eingabestring an und führt Übereinstimmungsoperationen durch.

Zusätzlich bieten Methoden der `String`-Klasse in Java vereinfachte Operationen auf Regex-Basis für einfachere Aufgaben.

## Grundlegende Schritte zur Verwendung von `java.util.regex`

Um reguläre Ausdrücke in Java zu verwenden, befolgen Sie diese Schritte:

1.  **Kompilieren eines Patterns**: Wandeln Sie Ihren Regex-String in ein `Pattern`-Objekt um.
2.  **Erstellen eines Matchers**: Verwenden Sie das Pattern, um einen `Matcher` für Ihren Eingabetext zu erstellen.
3.  **Durchführen von Operationen**: Verwenden Sie den Matcher, um auf Übereinstimmungen zu prüfen, Muster zu finden oder Text zu manipulieren.

So funktioniert es in der Praxis.

## Beispiel 1: Validierung einer E-Mail-Adresse

Lassen Sie uns einen einfachen E-Mail-Validator mit einem grundlegenden Regex-Muster erstellen: `".+@.+\\..+"`. Dieses Muster findet Zeichenketten, die mindestens ein Zeichen vor und nach einem `@`-Symbol haben, gefolgt von einem Punkt und weiteren Zeichen (z.B. `example@test.com`).

```java
import java.util.regex.*;

public class EmailValidator {
    public static boolean isValidEmail(String email) {
        // Definiere das Regex-Muster
        String regex = ".+@.+\\..+";
        // Kompiliere das Muster
        Pattern pattern = Pattern.compile(regex);
        // Erstelle einen Matcher für den Eingabestring
        Matcher matcher = pattern.matcher(email);
        // Prüfe, ob der gesamte String dem Muster entspricht
        return matcher.matches();
    }

    public static void main(String[] args) {
        String email = "example@test.com";
        if (isValidEmail(email)) {
            System.out.println("Gültige E-Mail");
        } else {
            System.out.println("Ungültige E-Mail");
        }
    }
}
```

### Erklärung
- **`Pattern.compile(regex)`**: Kompiliert den Regex-String in ein `Pattern`-Objekt.
- **`pattern.matcher(email)`**: Erstellt einen `Matcher` für den Eingabestring `email`.
- **`matcher.matches()`**: Gibt `true` zurück, wenn der gesamte String dem Muster entspricht, andernfalls `false`.

**Ausgabe**: `Gültige E-Mail`

Hinweis: Dies ist ein vereinfachtes E-Mail-Muster. Echte E-Mail-Validierung erfordert einen komplexeren Regex (z.B. gemäß RFC 5322), aber dies dient als Ausgangspunkt.

## Beispiel 2: Finden aller Hashtags in einem String

Angenommen, Sie möchten alle Hashtags (z.B. `#java`) aus einem Tweet extrahieren. Verwenden Sie den Regex `"#\\w+"`, wobei `#` das eigentliche Hashtag-Symbol findet und `\\w+` auf ein oder mehrere Wortzeichen (Buchstaben, Ziffern oder Unterstriche) passt.

```java
import java.util.regex.*;

public class HashtagExtractor {
    public static void main(String[] args) {
        String tweet = "This is a #sample tweet with #multiple hashtags like #java";
        String regex = "#\\w+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(tweet);

        // Finde alle Übereinstimmungen
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}
```

### Erklärung
- **`matcher.find()`**: Geht zur nächsten Übereinstimmung im Eingabestring und gibt `true` zurück, wenn eine Übereinstimmung gefunden wurde.
- **`matcher.group()`**: Gibt den gefundenen Text für die aktuelle Übereinstimmung zurück.

**Ausgabe**:
```
#sample
#multiple
#java
```

## Beispiel 3: Ersetzen von Text mit Regex

Um alle Vorkommen eines Wortes zu ersetzen (z.B. Zensieren von "badword" mit Sternchen), können Sie die Methode `String.replaceAll()` verwenden, die intern Regex nutzt.

```java
public class TextCensor {
    public static void main(String[] args) {
        String text = "This is a badword example with badword repeated.";
        String censored = text.replaceAll("badword", "*******");
        System.out.println(censored);
    }
}
```

**Ausgabe**: `This is a ******* example with ******* repeated.`

Für komplexere Ersetzungen verwenden Sie `Matcher`:

```java
import java.util.regex.*;

public class ComplexReplacement {
    public static void main(String[] args) {
        String text = "Contact: 123-456-7890";
        String regex = "\\d{3}-\\d{3}-\\d{4}"; // Findet Telefonnummern
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);
        String result = matcher.replaceAll("XXX-XXX-XXXX");
        System.out.println(result);
    }
}
```

**Ausgabe**: `Contact: XXX-XXX-XXXX`

## Beispiel 4: Verwenden von Gruppen zum Parsen strukturierter Daten

Regex-Gruppen, definiert mit runden Klammern `()`, ermöglichen es Ihnen, Teile einer Übereinstimmung zu erfassen. Um beispielsweise eine Sozialversicherungsnummer (SSN) wie `123-45-6789` zu parsen:

```java
import java.util.regex.*;

public class SSNParser {
    public static void main(String[] args) {
        String ssn = "123-45-6789";
        String regex = "(\\d{3})-(\\d{2})-(\\d{4})"; // Gruppen für Bereich, Gruppe, Seriennummer
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(ssn);

        if (matcher.matches()) {
            System.out.println("Bereichsnummer: " + matcher.group(1));
            System.out.println("Gruppennummer: " + matcher.group(2));
            System.out.println("Seriennummer: " + matcher.group(3));
        }
    }
}
```

### Erklärung
- **`"(\\d{3})-(\\d{2})-(\\d{4})"`**: Definiert drei Gruppen:
  - Gruppe 1: `\\d{3}` (drei Ziffern)
  - Gruppe 2: `\\d{2}` (zwei Ziffern)
  - Gruppe 3: `\\d{4}` (vier Ziffern)
- **`matcher.group(n)`**: Ruft den Text ab, der von Gruppe `n` gefunden wurde (1-basierter Index).

**Ausgabe**:
```
Bereichsnummer: 123
Gruppennummer: 45
Seriennummer: 6789
```

Sie können auch **benannte Gruppen** für mehr Klarheit verwenden:

```java
String regex = "(?<area>\\d{3})-(?<group>\\d{2})-(?<serial>\\d{4})";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher("123-45-6789");
if (matcher.matches()) {
    System.out.println("Bereich: " + matcher.group("area"));
    System.out.println("Gruppe: " + matcher.group("group"));
    System.out.println("Seriennummer: " + matcher.group("serial"));
}
```

## Zusätzliche Funktionen und Tipps

### Flags
Modifizieren Sie das Musterverhalten mit Flags in `Pattern.compile()`:
- **`Pattern.CASE_INSENSITIVE`**: Ignoriert Groß-/Kleinschreibung beim Abgleich.
  ```java
  Pattern pattern = Pattern.compile("hello", Pattern.CASE_INSENSITIVE);
  Matcher matcher = pattern.matcher("HELLO");
  System.out.println(matcher.matches()); // true
  ```

### String-Methoden
Für einfache Aufgaben verwenden Sie `String`-Methoden:
- **`matches()`**: Prüft, ob der gesamte String einem Regex entspricht.
  ```java
  String text = "cat";
  System.out.println(text.matches("\\w{3}")); // true
  ```
- **`split()`**: Teilt einen String anhand eines Regex-Musters.
  ```java
  String data = "apple, banana, cherry";
  String[] fruits = data.split("\\s*,\\s*");
  // Gibt aus: apple, banana, cherry
  ```

### Maskieren spezieller Zeichen
Regex verwendet spezielle Zeichen wie `.`, `*` und `?`. Um sie wörtlich zu finden, maskieren Sie sie mit `\\`:
- Einen Punkt finden: `"\\."`
- In Java-Strings müssen Backslashes maskiert werden: `"\\d"` für Ziffern, `"\\\\"` für einen wörtlichen Backslash.

### Leistung
Das Kompilieren eines Patterns ist aufwändig. Wiederverwenden Sie `Pattern`-Objekte, wenn möglich:
```java
Pattern pattern = Pattern.compile("\\d+"); // Einmal kompilieren
for (String input : new String[]{"123", "456"}) {
    Matcher matcher = pattern.matcher(input);
    if (matcher.matches()) {
        System.out.println("Nummer: " + input);
    }
}
```

### Fehlerbehandlung
Ungültige Regex-Muster werfen eine `PatternSyntaxException`. Behandeln Sie diese in Produktionscode:
```java
try {
    Pattern pattern = Pattern.compile("["); // Ungültiger Regex
} catch (PatternSyntaxException e) {
    System.err.println("Ungültiger Regex: " + e.getMessage());
}
```

## Zusammenfassung

- **Kompilieren eines Patterns**: `Pattern.compile(regex)`
- **Erstellen eines Matchers**: `pattern.matcher(input)`
- **Wichtige Operationen**:
  - `matches()`: Vollständige String-Übereinstimmung
  - `find()`: Nächste Übereinstimmung finden
  - `group()`: Gefundenen Text extrahieren
  - `replaceAll()`: Übereinstimmungen ersetzen
- **Bequemlichkeit**: Verwenden Sie `String`-Methoden für einfache Aufgaben.
- **Beste Praktiken**: Maskieren Sie Sonderzeichen, verwenden Sie Patterns wieder und behandeln Sie Ausnahmen.

Dies behandelt die Grundlagen von `java.util.regex`. Für fortgeschrittene Themen wie Lookaheads oder Zeichenklassen konsultieren Sie die [Java-Dokumentation](https://docs.oracle.com/en/java/javase/17/docs/api/java.util.regex/package-summary.html) oder experimentieren Sie mit spezifischen Anwendungsfällen!