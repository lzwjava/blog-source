---
audio: false
generated: true
lang: de
layout: post
title: Reguläre Ausdrücke in Java
translated: true
---

# Wie man `java.util.regex` in Java verwendet

Das `java.util.regex`-Paket in Java bietet Werkzeuge zur Arbeit mit regulären Ausdrücken (Regex), die Muster sind, die zum Abgleichen und Manipulieren von Text verwendet werden. Diese Anleitung führt Sie durch die Grundlagen der Verwendung dieses Pakets, wobei der Fokus auf den beiden Hauptklassen `Pattern` und `Matcher` liegt. Ich werde auch häufige Anwendungsfälle mit Beispielen behandeln, um Ihnen den Einstieg zu erleichtern.

## Übersicht über `java.util.regex`

Das `java.util.regex`-Paket enthält:

- **`Pattern`**: Repräsentiert einen kompilierten regulären Ausdruck. Sie erstellen es aus einer Regex-Zeichenfolge.
- **`Matcher`**: Wendet das Muster auf eine bestimmte Eingabezeichenfolge an und führt Abgleichsvorgänge durch.

Zusätzlich bietet die `String`-Klasse von Java regex-basierte Methoden für einfachere Aufgaben.

## Grundschritte zur Verwendung von `java.util.regex`

Um reguläre Ausdrücke in Java zu verwenden, befolgen Sie diese Schritte:

1. **Muster kompilieren**: Konvertieren Sie Ihre Regex-Zeichenfolge in ein `Pattern`-Objekt.
2. **Matcher erstellen**: Verwenden Sie das Muster, um einen `Matcher` für Ihren Eingabetext zu erstellen.
3. **Vorgänge durchführen**: Verwenden Sie den Matcher, um nach Übereinstimmungen zu suchen, Muster zu finden oder Text zu manipulieren.

Hier ist, wie es in der Praxis funktioniert.

## Beispiel 1: Validierung einer E-Mail-Adresse

Erstellen Sie einen einfachen E-Mail-Validator mit einem grundlegenden Regex-Muster: `".+@.+\\..+"`. Dieses Muster stimmt mit Zeichenfolgen überein, die mindestens ein Zeichen vor und nach einem `@`-Symbol haben, gefolgt von einem Punkt und weiteren Zeichen (z. B. `example@test.com`).

```java
import java.util.regex.*;

public class EmailValidator {
    public static boolean isValidEmail(String email) {
        // Definieren Sie das Regex-Muster
        String regex = ".+@.+\\..+";
        // Kompilieren Sie das Muster
        Pattern pattern = Pattern.compile(regex);
        // Erstellen Sie einen Matcher für die Eingabezeichenfolge
        Matcher matcher = pattern.matcher(email);
        // Überprüfen Sie, ob die gesamte Zeichenfolge mit dem Muster übereinstimmt
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
- **`Pattern.compile(regex)`**: Kompiliert die Regex-Zeichenfolge in ein `Pattern`-Objekt.
- **`pattern.matcher(email)`**: Erstellt einen `Matcher` für die Eingabezeichenfolge `email`.
- **`matcher.matches()`**: Gibt `true` zurück, wenn die gesamte Zeichenfolge mit dem Muster übereinstimmt, andernfalls `false`.

**Ausgabe**: `Gültige E-Mail`

Hinweis: Dies ist ein vereinfachtes E-Mail-Muster. Eine echte E-Mail-Validierung erfordert ein komplexeres Regex (z. B. nach RFC 5322), aber dies dient als Ausgangspunkt.

## Beispiel 2: Alle Hashtags in einer Zeichenfolge finden

Angenommen, Sie möchten alle Hashtags (z. B. `#java`) aus einem Tweet extrahieren. Verwenden Sie das Regex `"#\\w+"`, wobei `#` das Hashtag-Symbol und `\\w+` ein oder mehrere Wortzeichen (Buchstaben, Ziffern oder Unterstriche) entspricht.

```java
import java.util.regex.*;

public class HashtagExtractor {
    public static void main(String[] args) {
        String tweet = "Dies ist ein #Beispiel-Tweet mit #mehreren Hashtags wie #java";
        String regex = "#\\w+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(tweet);

        // Alle Übereinstimmungen finden
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}
```

### Erklärung
- **`matcher.find()`**: Bewegt sich zur nächsten Übereinstimmung in der Eingabezeichenfolge und gibt `true` zurück, wenn eine Übereinstimmung gefunden wird.
- **`matcher.group()`**: Gibt den übereinstimmenden Text für die aktuelle Übereinstimmung zurück.

**Ausgabe**:
```
#Beispiel
#mehreren
#java
```

## Beispiel 3: Text mit Regex ersetzen

Um alle Vorkommen eines Wortes (z. B. Zensur von "badword" mit Sternchen) zu ersetzen, können Sie die Methode `String.replaceAll()` verwenden, die intern Regex verwendet.

```java
public class TextCensor {
    public static void main(String[] args) {
        String text = "Dies ist ein badword Beispiel mit badword wiederholt.";
        String censored = text.replaceAll("badword", "*******");
        System.out.println(censored);
    }
}
```

**Ausgabe**: `Dies ist ein ******* Beispiel mit ******* wiederholt.`

Für komplexere Ersetzungen verwenden Sie `Matcher`:

```java
import java.util.regex.*;

public class ComplexReplacement {
    public static void main(String[] args) {
        String text = "Kontakt: 123-456-7890";
        String regex = "\\d{3}-\\d{3}-\\d{4}"; // Übereinstimmungen mit Telefonnummern
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);
        String result = matcher.replaceAll("XXX-XXX-XXXX");
        System.out.println(result);
    }
}
```

**Ausgabe**: `Kontakt: XXX-XXX-XXXX`

## Beispiel 4: Gruppen zum Parsen strukturierter Daten verwenden

Regex-Gruppen, die mit Klammern `()` definiert sind, ermöglichen es Ihnen, Teile einer Übereinstimmung zu erfassen. Zum Beispiel, um eine Sozialversicherungsnummer (SSN) wie `123-45-6789` zu parsen:

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
- **`matcher.group(n)`**: Ruft den Text ab, der von Gruppe `n` (1-basierter Index) übereinstimmt.

**Ausgabe**:
```
Bereichsnummer: 123
Gruppennummer: 45
Seriennummer: 6789
```

Sie können auch **benannte Gruppen** für Klarheit verwenden:

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
Passen Sie das Musterverhalten mit Flags in `Pattern.compile()` an:
- **`Pattern.CASE_INSENSITIVE`**: Ignoriert die Groß-/Kleinschreibung beim Abgleichen.
  ```java
  Pattern pattern = Pattern.compile("hello", Pattern.CASE_INSENSITIVE);
  Matcher matcher = pattern.matcher("HELLO");
  System.out.println(matcher.matches()); // true
  ```

### String-Methoden
Für einfache Aufgaben verwenden Sie `String`-Methoden:
- **`matches()`**: Überprüft, ob die gesamte Zeichenfolge mit einem Regex übereinstimmt.
  ```java
  String text = "cat";
  System.out.println(text.matches("\\w{3}")); // true
  ```
- **`split()`**: Teilt eine Zeichenfolge durch ein Regex-Muster.
  ```java
  String data = "apple, banana, cherry";
  String[] fruits = data.split("\\s*,\\s*");
  // Ausgabe: apple, banana, cherry
  ```

### Sonderzeichen escapen
Regex verwendet Sonderzeichen wie `.`, `*` und `?`. Um sie wörtlich zu treffen, escapen Sie sie mit `\\`:
- Punkt abgleichen: `"\\."`
- In Java-Zeichenfolgen Backslashes escapen: `"\\d"` für Ziffern, `"\\\\"` für einen wörtlichen Backslash.

### Leistung
Das Kompilieren eines Musters ist kostspielig. Wiederverwenden Sie `Pattern`-Objekte, wenn möglich:
```java
Pattern pattern = Pattern.compile("\\d+"); // Einmal kompilieren
for (String input : new String[]{"123", "456"}) {
    Matcher matcher = pattern.matcher(input);
    if (matcher.matches()) {
        System.out.println("Zahl: " + input);
    }
}
```

### Fehlerbehandlung
Ungültige Regex-Muster werfen `PatternSyntaxException`. Behandeln Sie dies im Produktionscode:
```java
try {
    Pattern pattern = Pattern.compile("["); // Ungültiges Regex
} catch (PatternSyntaxException e) {
    System.err.println("Ungültiges Regex: " + e.getMessage());
}
```

## Zusammenfassung

- **Muster kompilieren**: `Pattern.compile(regex)`
- **Matcher erstellen**: `pattern.matcher(input)`
- **Wichtige Operationen**:
  - `matches()`: Vollständige Zeichenfolgenübereinstimmung
  - `find()`: Nächste Übereinstimmung finden
  - `group()`: Übereinstimmenden Text extrahieren
  - `replaceAll()`: Übereinstimmungen ersetzen
- **Bequemlichkeit**: Verwenden Sie `String`-Methoden für einfache Aufgaben.
- **Best Practices**: Escapen Sie Sonderzeichen, verwenden Sie Muster wieder und behandeln Sie Ausnahmen.

Dies deckt die Grundlagen von `java.util.regex` ab. Für fortgeschrittene Themen wie Lookaheads oder Zeichenklassen konsultieren Sie die [Java-Dokumentation](https://docs.oracle.com/en/java/javase/17/docs/api/java.util.regex/package-summary.html) oder experimentieren Sie mit spezifischen Anwendungsfällen!