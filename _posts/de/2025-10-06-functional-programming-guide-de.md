---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Leitfaden für funktionale Programmierung in Java
translated: true
type: note
---

Java hat seit Java 8 die Prinzipien der funktionalen Programmierung übernommen und führt Lambdas, Streams und andere Funktionen ein, die Code prägnanter, lesbarer und deklarativer machen. Dieser Leitfaden behandelt die Grundlagen bis zu fortgeschrittenen Konzepten und setzt Vertrautheit mit Core Java voraus. Wir verwenden Java 8+ Syntax, da diese Funktionen dort eingeführt wurden. Beispiele sind in Java-Codeblöcken für einfaches Kopieren.

## 1. Einführung in die funktionale Programmierung in Java

Funktionale Programmierung (FP) betont:
- **Pure functions**: Funktionen ohne Seiteneffekte (z.B. keine Veränderungen eines veränderlichen Zustands).
- **Immutability**: Daten ändern sich nicht nach ihrer Erstellung.
- **Higher-order functions**: Funktionen, die andere Funktionen als Argumente nehmen oder zurückgeben.
- **Declarative style**: Fokus auf *was* zu tun ist, nicht *wie* (z.B. via Streams statt Schleifen).

Java ist nicht rein funktional wie Haskell, aber es verbindet FP mit seinen objektorientierten Wurzeln. Wichtige Ermöglicher:
- Lambda-Ausdrücke (anonyme Funktionen).
- Funktionale Interfaces (Interfaces mit einer abstrakten Methode).
- Streams API zur funktionalen Verarbeitung von Collections.

Vorteile: Weniger Boilerplate, einfachere Parallelität, bessere Komponierbarkeit.

## 2. Lambda-Ausdrücke

Lambdas sind anonyme Funktionen, die für kurze, einmalige Implementierungen verwendet werden. Sie sind der Einstieg in FP in Java.

### Grundlegende Syntax
Ein Lambda ist: `(Parameter) -> { Körper }`
- Klammern optional für einzelnen Parameter.
- Geschweifte Klammern optional für einzelnen Ausdruck (implizites return).
- Typrückschluss funktioniert oft, aber Typen können angegeben werden.

```java
// Traditionale anonyme innere Klasse
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello, World!");
    }
};

// Lambda-Äquivalent
Runnable lambda = () -> System.out.println("Hello, World!");
lambda.run();
```

### Mit Parametern
```java
// Binärer Operator Beispiel
BinaryOperator<Integer> add = (a, b) -> a + b;
System.out.println(add.apply(2, 3)); // 5

// Mehrzeiliger Körper
Comparator<String> comparator = (s1, s2) -> {
    int lenDiff = s1.length() - s2.length();
    return lenDiff != 0 ? lenDiff : s1.compareTo(s2);
};
```

### Erfassen von Variablen (Effectively Final)
Lambdas können auf äußere Variablen zugreifen, aber diese müssen **effectively final** sein (keine Neuzuweisung).
```java
int threshold = 10;
Predicate<Integer> isHigh = x -> x > threshold; // OK
// threshold = 20; // Fehler: nicht effectively final
```

## 3. Funktionale Interfaces

Ein funktionales Interface hat genau eine abstrakte Methode (SAM - Single Abstract Method). Java bietet vordefinierte in `java.util.function`.

### Eingebaute Beispiele
- `Predicate<T>`: `boolean test(T t)`
- `Function<T, R>`: `R apply(T t)`
- `Consumer<T>`: `void accept(T t)`
- `Supplier<T>`: `T get()`
- `BiFunction<T, U, R>`, etc., für zwei Eingaben.

Benutzerdefinierte:
```java
@FunctionalInterface  // Optional, aber gute Praxis
interface Transformer {
    String transform(String input);
}

Transformer upper = s -> s.toUpperCase();
System.out.println(upper.transform("java")); // JAVA
```

Verwende `@FunctionalInterface` zur SAM-Erzwingung.

### Default und Static Methods
Funktionale Interfaces können Default-Methoden haben (Java 8+), wie `Optional.orElse()`.
```java
default int compare(String a, String b) { ... } // Erlaubt
static void utility() { ... } // Erlaubt
```

## 4. Methodenreferenzen

Kurzschrift für Lambdas, die bestehende Methoden aufrufen. Syntax: `Class::method` oder `instance::method`.

Typen:
- Statisch: `Class::staticMethod`
- Instanz eines bestimmten Typs: `Class::instanceMethod`
- Instanz eines beliebigen Objekts: `object::instanceMethod`
- Konstruktor: `Class::new`

Beispiele:
```java
// Lambda: x -> System.out.println(x)
Consumer<String> printer = System.out::println;

// Statische Methode
Function<String, Integer> length = String::length;

// Instanzmethode
List<String> list = Arrays.asList("a", "b");
list.forEach(System.out::println); // Gibt jedes aus

// Konstruktor
Supplier<List<String>> listSupplier = ArrayList::new;
```

## 5. Streams API

Streams verarbeiten Collections deklarativ: Erzeugen → Transformieren → Sammeln. Lazy Evaluation (intermediate Operations laufen erst bei terminal Operation).

### Streams erzeugen
```java
import java.util.*;
import java.util.stream.*;

List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

// Von Collection
Stream<String> stream = names.stream();

// Von Array
String[] arr = {"x", "y"};
Stream<String> arrStream = Arrays.stream(arr);

// Unendlich
Stream<Integer> infinite = Stream.iterate(0, n -> n + 1);
```

### Intermediate Operations (Lazy)
Kette sie; keine Berechnung bis zur terminal Operation.
- `filter(Predicate)`: Behalte passende Elemente.
- `map(Function)`: Transformiere jedes.
- `flatMap(Function<? super T, ? extends Stream<? extends R>>)`: Glätte verschachtelte Streams.
- `distinct()`, `sorted()`, `limit(n)`, `skip(n)`.

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> evensSquared = numbers.stream()
    .filter(n -> n % 2 == 0)
    .map(n -> n * n)
    .collect(Collectors.toList()); // [4, 16]
```

### Terminal Operations (Eager)
Lösen Berechnung aus und geben ein Ergebnis zurück.
- `collect(Collector)`: Zu Liste, Set, Map.
- `forEach(Consumer)`: Seiteneffekt (wenn möglich vermeiden).
- `reduce()`: Aggregiere (z.B. Summe).
- `anyMatch()`, `allMatch()`, `findFirst()`.

```java
// Reduce: Summe
int sum = numbers.stream().reduce(0, Integer::sum); // 15

// Sammeln in Map
Map<String, Integer> nameLengths = Stream.of("Alice", "Bob")
    .collect(Collectors.toMap(s -> s, String::length)); // {Alice=5, Bob=3}

// Gruppieren
Map<Integer, List<String>> byLength = names.stream()
    .collect(Collectors.groupingBy(String::length)); // {5=[Alice, Charlie], 3=[Bob]}
```

### Parallele Streams
Für Parallelität: `parallelStream()` oder `.parallel()`. Vorsichtig verwenden (Debugging schwieriger).
```java
long count = names.parallelStream().count(); // 3
```

## 6. Collectors

Aus `java.util.stream.Collectors`. Baue komplexe Reduktionen.

Häufig:
- `toList()`, `toSet()`, `toMap()`
- `joining()`: Verkette Strings.
- `summingInt()`, `averagingDouble()`
- `groupingBy()`, `partitioningBy()`
- `collectingAndThen()`: Nachbearbeiten.

```java
// Benutzerdefinierter Collector für Maximum nach Länge
String longest = names.stream()
    .collect(Collectors.maxBy(Comparator.comparingInt(String::length)))
    .orElse(""); // "Charlie"

// Partitioniere Gerade/Ungerade
Map<Boolean, List<Integer>> partitions = numbers.stream()
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
```

## 7. Optional

Vermeidet `NullPointerException` durch Einhüllen potentiell null Werte. Ermutigt explizite Null-Behandlung.

Erstellung:
- `Optional.of(value)`: Nicht-null.
- `Optional.ofNullable(value)`: Null → leer.
- `Optional.empty()`.

Operationen:
- `isPresent()`, `ifPresent(Consumer)`
- `orElse(default)`, `orElseThrow()`
- `map()`, `flatMap()` für Verkettung.

```java
Optional<String> opt = Optional.ofNullable(getName()); // Kann null zurückgeben

String name = opt.orElse("Unknown");
opt.ifPresent(System.out::println);

String upper = opt.map(String::toUpperCase).orElse("DEFAULT");
```

Streams geben oft `Optional` zurück (z.B. `findFirst()`).

## 8. Fortgeschrittene Themen

### Komponierbare Funktionen
`Function.andThen()`, `Function.compose()` für Verkettung.
```java
Function<String, Integer> len = String::length;
Function<Integer, String> toStr = i -> "Len: " + i;

Function<String, String> chain = len.andThen(toStr);
System.out.println(chain.apply("Java")); // Len: 4
```

### Rekursion und Tail Calls
Java hat keine Optimierung, aber verwende `Stream.iterate()` für iterative Rekursion.

### Immutability Helfer
Verwende `Collections.unmodifiableList()` oder Bibliotheken wie Guava/Immutable Collections (eingebaut seit Java 10+ mit `List.of()`).

`List.of("a", "b")` erzeugt unveränderliche Listen (Java 9+).

### Pattern Matching (Java 21+ Preview/Stable)
Erweitert FP mit Destrukturierung in Switches.
```java
// Preview-Feature; aktivieren mit --enable-preview
String desc = switch (obj) {
    case Integer i -> "int: " + i;
    case String s -> "str: " + s.length();
    default -> "unknown";
};
```

### Virtuelle Threads (Java 21+)
FP glänzt mit leichtgewichtigen Threads für nebenläufige Streams.

## 9. Best Practices

- **Bevorzuge Immutability**: Verwende final Felder, vermeide veränderbare Collections.
- **Vermeide Seiteneffekte**: Halte Lambdas pure; Seiteneffekte nur in `forEach` oder expliziten Consumern.
- **Streams vs. Schleifen**: Verwende Streams für Lesbarkeit; Schleifen für performance-kritischen Code.
- **Nulls**: Bevorzuge `Optional` gegenüber Null-Checks.
- **Testing**: Mocke funktionale Interfaces einfach mit Lambdas.
- **Performance**: Streams haben Overhead; profiliere vor paralleler Verwendung.
- **Lesbarkeit**: Kurze Lambdas sind in Ordnung; extrahiere Methoden für komplexe Logik.

Häufige Fallstricke:
- Ändern externen Zustands in Lambdas.
- Vergessen der terminal Operation (Streams tun nichts!).
- Übermäßiger Einsatz paralleler Streams (nicht immer schneller).

## 10. Beispiel: Funktionale Pipeline

Verarbeite eine Liste von Mitarbeitern funktional.

```java
import java.util.*;
import java.util.stream.Collectors;

class Employee {
    String name;
    int salary;
    Department dept;

    Employee(String name, int salary, Department dept) {
        this.name = name;
        this.salary = salary;
        this.dept = dept;
    }
}

enum Department { ENG, HR }

public class FunctionalExample {
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
            new Employee("Alice", 50000, Department.ENG),
            new Employee("Bob", 60000, Department.HR),
            new Employee("Charlie", 55000, Department.ENG)
        );

        // Namen hochbezahlter Ingenieure, sortiert
        List<String> result = employees.stream()
            .filter(e -> e.dept == Department.ENG)
            .filter(e -> e.salary > 52000)
            .map(Employee::getName)  // Nimm Getter an
            .sorted()
            .collect(Collectors.toList());

        System.out.println(result); // [Charlie]
    }
}
```

## Fazit

Lambdas und FP verwandeln Java von imperativ zu expressiv. Beginne mit einfachen Ersetzungen (z.B. `forEach` statt Schleifen), dann baue Pipelines. Übe an echten Projekten für Meisterschaft. Für tiefere Einblicke, experimentiere in einer IDE.

### Referenzen
- [Oracle Java Tutorials: Lambda Expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)
- [Baeldung: Java 8 Functional Interfaces](https://www.baeldung.com/java-functional-interfaces)
- [Java Streams Guide](https://www.baeldung.com/java-8-streams)
- [Effective Java (3rd Ed.) - Item 42-45 on Lambdas](https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/)