---
audio: false
generated: true
lang: de
layout: post
title: Funktionale Schnittstellen in Java
translated: true
type: note
---

Das `java.util.function`-Paket in Java bietet eine Sammlung von funktionalen Interfaces, die entwickelt wurden, um funktionale Programmierung zu unterstützen, eingeführt in Java 8. Diese Interfaces haben jeweils eine einzige abstrakte Methode, was sie mit Lambda-Ausdrücken und Methodenreferenzen kompatibel macht. Diese Antwort erklärt, wie man einige der gebräuchlichsten funktionalen Interfaces in diesem Paket verwendet – `Function<T, R>`, `Predicate<T>`, `Consumer<T>` und `Supplier<T>` – mit praktischen Beispielen.

---

### Was sind funktionale Interfaces?
Ein funktionales Interface ist ein Interface mit genau einer abstrakten Methode. Das `java.util.function`-Paket bietet vordefinierte funktionale Interfaces für häufige Aufgaben, sodass Sie keine eigenen erstellen müssen. Diese Interfaces werden häufig mit Lambda-Ausdrücken, Methodenreferenzen und der Stream-API verwendet, um prägnanten und ausdrucksstarken Code zu schreiben.

Hier ist, wie man die wichtigsten Interfaces verwendet:

---

### 1. `Function<T, R>`: Eingabe in Ausgabe umwandeln
Das `Function<T, R>`-Interface repräsentiert eine Funktion, die eine Eingabe vom Typ `T` entgegennimmt und eine Ausgabe vom Typ `R` erzeugt. Seine abstrakte Methode ist `apply`.

#### Beispiel: Länge eines Strings ermitteln
```java
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        Function<String, Integer> stringLength = s -> s.length();
        System.out.println(stringLength.apply("Hello")); // Gibt aus: 5
    }
}
```
- **Erklärung**: Der Lambda-Ausdruck `s -> s.length()` definiert eine `Function`, die einen `String` (`T`) entgegennimmt und einen `Integer` (`R`) zurückgibt. Die `apply`-Methode führt diese Logik aus.

---

### 2. `Predicate<T>`: Eine Bedingung testen
Das `Predicate<T>`-Interface repräsentiert eine boolesche Funktion, die eine Eingabe vom Typ `T` entgegennimmt. Seine abstrakte Methode ist `test`.

#### Beispiel: Prüfen, ob eine Zahl gerade ist
```java
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        Predicate<Integer> isEven = n -> n % 2 == 0;
        System.out.println(isEven.test(4)); // Gibt aus: true
        System.out.println(isEven.test(5)); // Gibt aus: false
    }
}
```
- **Erklärung**: Der Lambda-Ausdruck `n -> n % 2 == 0` definiert ein `Predicate`, das `true` zurückgibt, wenn die Eingabe gerade ist. Die `test`-Methode wertet diese Bedingung aus.

---

### 3. `Consumer<T>`: Eine Aktion ausführen
Das `Consumer<T>`-Interface repräsentiert eine Operation, die eine Eingabe vom Typ `T` entgegennimmt und kein Ergebnis zurückgibt. Seine abstrakte Methode ist `accept`.

#### Beispiel: Einen String ausgeben
```java
import java.util.function.Consumer;

public class Main {
    public static void main(String[] args) {
        Consumer<String> printer = s -> System.out.println(s);
        printer.accept("Hello, World!"); // Gibt aus: Hello, World!
    }
}
```
- **Erklärung**: Der Lambda-Ausdruck `s -> System.out.println(s)` definiert einen `Consumer`, der seine Eingabe ausgibt. Die `accept`-Methode führt die Aktion aus.

---

### 4. `Supplier<T>`: Ein Ergebnis erzeugen
Das `Supplier<T>`-Interface repräsentiert einen Lieferanten von Ergebnissen, der keine Eingabe entgegennimmt und einen Wert vom Typ `T` zurückgibt. Seine abstrakte Methode ist `get`.

#### Beispiel: Eine Zufallszahl erzeugen
```java
import java.util.function.Supplier;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Supplier<Integer> randomInt = () -> new Random().nextInt(100);
        System.out.println(randomInt.get()); // Gibt eine zufällige Ganzzahl zwischen 0 und 99 aus
    }
}
```
- **Erklärung**: Der Lambda-Ausdruck `() -> new Random().nextInt(100)` definiert einen `Supplier`, der eine zufällige Ganzzahl erzeugt. Die `get`-Methode ruft den Wert ab.

---

### Funktionale Interfaces mit Streams verwenden
Diese Interfaces glänzen in der Java Stream-API, wo sie prägnante Datenverarbeitung ermöglichen. Hier ist ein Beispiel, das eine Liste von Strings filtert, transformiert und ausgibt:

#### Beispiel: Eine Liste von Strings verarbeiten
```java
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        List<String> strings = Arrays.asList("a", "bb", "ccc", "dddd");

        Predicate<String> longerThanTwo = s -> s.length() > 2;       // Filtert Strings länger als 2
        Function<String, String> toUpperCase = s -> s.toUpperCase(); // In Großbuchstaben umwandeln
        Consumer<String> printer = s -> System.out.println(s);       // Gibt jedes Ergebnis aus

        strings.stream()
               .filter(longerThanTwo)   // Behält "ccc" und "dddd"
               .map(toUpperCase)        // Wandelt um in "CCC" und "DDDD"
               .forEach(printer);       // Gibt aus: CCC, DDDD (auf separaten Zeilen)
    }
}
```
- **Erklärung**:
  - `filter` verwendet ein `Predicate`, um Strings mit einer Länge > 2 zu behalten.
  - `map` verwendet eine `Function`, um Strings in Großbuchstaben umzuwandeln.
  - `forEach` verwendet einen `Consumer`, um jedes Ergebnis auszugeben.

#### Methodenreferenzen verwenden
Sie können dies noch kürzer mit Methodenreferenzen machen:
```java
strings.stream()
       .filter(s -> s.length() > 2)
       .map(String::toUpperCase)      // Methodenreferenz für Function
       .forEach(System.out::println); // Methodenreferenz für Consumer
```

---

### Funktionale Interfaces komponieren
Einige Interfaces erlauben Komposition für komplexere Operationen:
- **Funktionskomposition**: Verwenden Sie `andThen` oder `compose`.
  ```java
  Function<String, Integer> toLength = s -> s.length();
  Function<Integer, String> toString = i -> "Length is " + i;
  Function<String, String> combined = toLength.andThen(toString);
  System.out.println(combined.apply("Hello")); // Gibt aus: Length is 5
  ```
- **Prädikat-Kombination**: Verwenden Sie `and`, `or` oder `negate`.
  ```java
  Predicate<String> isLong = s -> s.length() > 5;
  Predicate<String> startsWithA = s -> s.startsWith("A");
  Predicate<String> isLongAndStartsWithA = isLong.and(startsWithA);
  System.out.println(isLongAndStartsWithA.test("Avocado")); // Gibt aus: true
  ```

---

### Zusammenfassung
Hier ist, wann und wie man diese Interfaces verwendet:
- **`Function<T, R>`**: Eine Eingabe in eine Ausgabe umwandeln (z.B. `apply`).
- **`Predicate<T>`**: Eine Bedingung testen (z.B. `test`).
- **`Consumer<T>`**: Eine Aktion auf einer Eingabe ausführen (z.B. `accept`).
- **`Supplier<T>`**: Einen Wert ohne Eingabe erzeugen (z.B. `get`).
- **Mit Streams**: Kombinieren Sie sie für leistungsstarke Datenverarbeitung.
- **Komposition**: Verketten oder kombinieren Sie sie für komplexe Logik.

Sie können diese Interfaces mit Lambda-Ausdrücken (z.B. `s -> s.length()`) oder Methodenreferenzen (z.B. `String::toUpperCase`) implementieren. Sie ermöglichen einen funktionalen Programmierstil in Java, was Ihren Code prägnanter, lesbarer und wiederverwendbarer macht, besonders mit der Stream-API.