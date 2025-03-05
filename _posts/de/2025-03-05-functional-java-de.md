---
audio: false
generated: true
lang: de
layout: post
title: Funktionale Schnittstellen in Java
translated: true
---

Das `java.util.function`-Paket in Java bietet eine Sammlung von funktionalen Schnittstellen, die entwickelt wurden, um funktionales Programmieren zu unterstützen, das in Java 8 eingeführt wurde. Diese Schnittstellen haben jeweils eine einzige abstrakte Methode, wodurch sie mit Lambda-Ausdrücken und Methodenverweisen kompatibel sind. Diese Antwort erklärt, wie man einige der gebräuchlichsten funktionalen Schnittstellen in diesem Paket – `Function<T, R>`, `Predicate<T>`, `Consumer<T>` und `Supplier<T>` – mit praktischen Beispielen verwendet.

---

### Was sind funktionale Schnittstellen?
Eine funktionale Schnittstelle ist eine Schnittstelle mit genau einer abstrakten Methode. Das `java.util.function`-Paket bietet vordefinierte funktionale Schnittstellen für häufige Aufgaben, sodass Sie keine eigenen erstellen müssen. Diese Schnittstellen werden weit verbreitet mit Lambda-Ausdrücken, Methodenverweisen und der Stream-API verwendet, um prägnanten und ausdrucksstarken Code zu schreiben.

Hier ist, wie man die wichtigsten Schnittstellen verwendet:

---

### 1. `Function<T, R>`: Eingabe in Ausgabe umwandeln
Die `Function<T, R>`-Schnittstelle stellt eine Funktion dar, die eine Eingabe vom Typ `T` nimmt und eine Ausgabe vom Typ `R` produziert. Ihre abstrakte Methode ist `apply`.

#### Beispiel: Länge einer Zeichenkette erhalten
```java
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        Function<String, Integer> stringLength = s -> s.length();
        System.out.println(stringLength.apply("Hello")); // Ausgabe: 5
    }
}
```
- **Erklärung**: Der Lambda-Ausdruck `s -> s.length()` definiert eine `Function`, die eine `String` (`T`) nimmt und eine `Integer` (`R`) zurückgibt. Die `apply`-Methode führt diese Logik aus.

---

### 2. `Predicate<T>`: Bedingung testen
Die `Predicate<T>`-Schnittstelle stellt eine boolesche Funktion dar, die eine Eingabe vom Typ `T` nimmt. Ihre abstrakte Methode ist `test`.

#### Beispiel: Überprüfen, ob eine Zahl gerade ist
```java
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        Predicate<Integer> isEven = n -> n % 2 == 0;
        System.out.println(isEven.test(4)); // Ausgabe: true
        System.out.println(isEven.test(5)); // Ausgabe: false
    }
}
```
- **Erklärung**: Der Lambda-Ausdruck `n -> n % 2 == 0` definiert eine `Predicate`, die `true` zurückgibt, wenn die Eingabe gerade ist. Die `test`-Methode bewertet diese Bedingung.

---

### 3. `Consumer<T>`: Aktion ausführen
Die `Consumer<T>`-Schnittstelle stellt eine Operation dar, die eine Eingabe vom Typ `T` nimmt und kein Ergebnis zurückgibt. Ihre abstrakte Methode ist `accept`.

#### Beispiel: Zeichenkette drucken
```java
import java.util.function.Consumer;

public class Main {
    public static void main(String[] args) {
        Consumer<String> printer = s -> System.out.println(s);
        printer.accept("Hello, World!"); // Ausgabe: Hello, World!
    }
}
```
- **Erklärung**: Der Lambda-Ausdruck `s -> System.out.println(s)` definiert einen `Consumer`, der seine Eingabe druckt. Die `accept`-Methode führt die Aktion aus.

---

### 4. `Supplier<T>`: Ergebnis generieren
Die `Supplier<T>`-Schnittstelle stellt einen Lieferanten von Ergebnissen dar, der keine Eingabe nimmt und einen Wert vom Typ `T` zurückgibt. Ihre abstrakte Methode ist `get`.

#### Beispiel: Zufallszahl generieren
```java
import java.util.function.Supplier;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Supplier<Integer> randomInt = () -> new Random().nextInt(100);
        System.out.println(randomInt.get()); // Ausgabe einer Zufallszahl zwischen 0 und 99
    }
}
```
- **Erklärung**: Der Lambda-Ausdruck `() -> new Random().nextInt(100)` definiert einen `Supplier`, der eine Zufallszahl generiert. Die `get`-Methode holt den Wert ab.

---

### Funktionale Schnittstellen mit Streams verwenden
Diese Schnittstellen glänzen in der Java Stream-API, wo sie prägnante Datenverarbeitung ermöglichen. Hier ist ein Beispiel, das eine Liste von Zeichenketten filtert, transformiert und druckt:

#### Beispiel: Verarbeiten einer Liste von Zeichenketten
```java
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        List<String> strings = Arrays.asList("a", "bb", "ccc", "dddd");

        Predicate<String> longerThanTwo = s -> s.length() > 2;       // Filtert Zeichenketten länger als 2
        Function<String, String> toUpperCase = s -> s.toUpperCase(); // Konvertiert in Großbuchstaben
        Consumer<String> printer = s -> System.out.println(s);       // Druckt jedes Ergebnis

        strings.stream()
               .filter(longerThanTwo)   // Behält "ccc" und "dddd"
               .map(toUpperCase)        // Konvertiert zu "CCC" und "DDDD"
               .forEach(printer);       // Ausgabe: CCC, DDDD (in separaten Zeilen)
    }
}
```
- **Erklärung**:
  - `filter` verwendet eine `Predicate`, um Zeichenketten mit einer Länge > 2 zu behalten.
  - `map` verwendet eine `Function`, um Zeichenketten in Großbuchstaben zu transformieren.
  - `forEach` verwendet einen `Consumer`, um jedes Ergebnis zu drucken.

#### Methodenverweise verwenden
Man kann dies mit Methodenverweisen noch kürzer machen:
```java
strings.stream()
       .filter(s -> s.length() > 2)
       .map(String::toUpperCase)      // Methodenverweis für Function
       .forEach(System.out::println); // Methodenverweis für Consumer
```

---

### Zusammensetzen funktionaler Schnittstellen
Einige Schnittstellen ermöglichen die Komposition für komplexere Operationen:
- **Funktionszusammensetzung**: Verwenden Sie `andThen` oder `compose`.
  ```java
  Function<String, Integer> toLength = s -> s.length();
  Function<Integer, String> toString = i -> "Length is " + i;
  Function<String, String> combined = toLength.andThen(toString);
  System.out.println(combined.apply("Hello")); // Ausgabe: Length is 5
  ```
- **Prädikatkombination**: Verwenden Sie `and`, `or` oder `negate`.
  ```java
  Predicate<String> isLong = s -> s.length() > 5;
  Predicate<String> startsWithA = s -> s.startsWith("A");
  Predicate<String> isLongAndStartsWithA = isLong.and(startsWithA);
  System.out.println(isLongAndStartsWithA.test("Avocado")); // Ausgabe: true
  ```

---

### Zusammenfassung
Hier ist, wann und wie man diese Schnittstellen verwendet:
- **`Function<T, R>`**: Wandelt eine Eingabe in eine Ausgabe um (z. B. `apply`).
- **`Predicate<T>`**: Testet eine Bedingung (z. B. `test`).
- **`Consumer<T>`**: Führt eine Aktion auf einer Eingabe aus (z. B. `accept`).
- **`Supplier<T>`**: Generiert einen Wert ohne Eingabe (z. B. `get`).
- **Mit Streams**: Kombinieren Sie sie für eine leistungsstarke Datenverarbeitung.
- **Zusammensetzung**: Ketten oder kombinieren Sie sie für komplexe Logik.

Sie können diese Schnittstellen mit Lambda-Ausdrücken (z. B. `s -> s.length()`) oder Methodenverweisen (z. B. `String::toUpperCase`) implementieren. Sie ermöglichen einen funktionalen Programmierstil in Java, der Ihren Code prägnanter, lesbarer und wiederverwendbarer macht, insbesondere mit der Stream-API.