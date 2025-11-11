---
audio: false
generated: true
lang: de
layout: post
title: Lambda-Ausdrücke und die Stream-API in Java
translated: true
type: note
---

Okay, lernen wir etwas über Lambda-Ausdrücke und die Stream-API in Java. Dies sind leistungsstarke Funktionen, die in Java 8 eingeführt wurden und einen funktionaleren Programmierstil ermöglichen, was zu prägnanterem und ausdrucksstärkerem Code führt.

**1. Lambda-Ausdrücke**

**Was ist ein Lambda-Ausdruck?**

Ein Lambda-Ausdruck ist im Wesentlichen eine anonyme (unbenannte) Funktion. Er ermöglicht es Ihnen, eine Funktion inline zu definieren, ohne explizit eine separate Methode zu deklarieren. Lambda-Ausdrücke sind besonders nützlich, um Verhalten als Daten zu übergeben, was Ihren Code flexibler und lesbarer macht, insbesondere bei der Arbeit mit funktionalen Interfaces.

**Syntax eines Lambda-Ausdrucks:**

Ein Lambda-Ausdruck hat die folgende grundlegende Syntax:

```java
(parameter list) -> expression body
```

*   **Parameterliste:** Diese ähnelt den Parametern einer Methode. Sie kann leer sein, einen Parameter enthalten oder mehrere Parameter. Die Typen der Parameter können oft vom Compiler abgeleitet werden, sodass Sie sie nicht immer explizit deklarieren müssen.
*   **Pfeiltoken (`->`):** Dies trennt die Parameterliste vom Ausdruckskörper.
*   **Ausdruckskörper:** Dies ist der Code, den der Lambda-Ausdruck ausführt. Es kann ein einzelner Ausdruck oder ein Block von Anweisungen sein, der in geschweiften Klammern `{}` eingeschlossen ist.

**Funktionale Interfaces:**

Lambda-Ausdrücke in Java werden verwendet, um Methoden zu implementieren, die durch **funktionale Interfaces** definiert werden. Ein funktionales Interface ist ein Interface, das **nur eine abstrakte Methode** enthält. Es kann Default-Methoden und statische Methoden haben, aber nur eine abstrakte Methode.

Beispiele für integrierte funktionale Interfaces in Java sind:

*   `Runnable` (einzelne abstrakte Methode: `void run()`)
*   `Callable<V>` (einzelne abstrakte Methode: `V call() throws Exception`)
*   `Comparator<T>` (einzelne abstrakte Methode: `int compare(T o1, T o2)`)
*   `Consumer<T>` (einzelne abstrakte Methode: `void accept(T t)`)
*   `Function<T, R>` (einzelne abstrakte Methode: `R apply(T t)`)
*   `Predicate<T>` (einzelne abstrakte Methode: `boolean test(T t)`)
*   `Supplier<T>` (einzelne abstrakte Methode: `T get()`)

**Beispiele für Lambda-Ausdrücke:**

Schauen wir uns einige Beispiele an, um zu verstehen, wie Lambda-Ausdrücke funktionieren:

*   **Keine Parameter:**

    ```java
    Runnable myRunnable = () -> System.out.println("Hello from lambda!");
    myRunnable.run(); // Ausgabe: Hello from lambda!
    ```

*   **Ein Parameter (Klammern können weggelassen werden):**

    ```java
    Consumer<String> printMessage = message -> System.out.println("Message: " + message);
    printMessage.accept("Lambda is cool!"); // Ausgabe: Message: Lambda is cool!
    ```

*   **Mehrere Parameter:**

    ```java
    java.util.Comparator<Integer> compareTwoNumbers = (a, b) -> a.compareTo(b);
    int result = compareTwoNumbers.compare(5, 10); // result wird -1 sein
    ```

*   **Lambda-Ausdruck mit einem Anweisungsblock:**

    ```java
    java.util.function.Function<Integer, String> checkEvenOdd = number -> {
        if (number % 2 == 0) {
            return "Even";
        } else {
            return "Odd";
        }
    };
    String output = checkEvenOdd.apply(7); // output wird "Odd" sein
    ```

**Methodenreferenzen:**

Methodenreferenzen sind eine Kurzschreibweise für Lambda-Ausdrücke, die einfach eine vorhandene Methode aufrufen. Sie machen Ihren Code noch prägnanter. Es gibt vier Arten von Methodenreferenzen:

1.  **Referenz auf eine statische Methode:** `ClassName::staticMethodName`

    ```java
    java.util.function.Function<String, Integer> stringToInt = Integer::parseInt;
    int number = stringToInt.apply("123"); // number wird 123 sein
    ```

2.  **Referenz auf eine Instanzmethode eines bestimmten Objekts:** `instance::instanceMethodName`

    ```java
    String message = "Hello";
    java.util.function.Consumer<String> printContains = s -> message.contains(s);
    printContains.accept("ll"); // Dies wird message.contains("ll") ausführen
    ```
    Für einen `Supplier` ist es eher so:

    ```java
    String message = "Hello";
    java.util.function.Supplier<Integer> getLength = message::length;
    int len = getLength.get(); // len wird 5 sein
    ```

3.  **Referenz auf eine Instanzmethode eines beliebigen Objekts eines bestimmten Typs:** `ClassName::instanceMethodName`

    ```java
    java.util.function.BiPredicate<String, String> checkStartsWith = String::startsWith;
    boolean starts = checkStartsWith.test("Java", "Ja"); // starts wird true sein
    ```

4.  **Referenz auf einen Konstruktor:** `ClassName::new`

    ```java
    java.util.function.Supplier<String> createString = String::new;
    String emptyString = createString.get(); // emptyString wird "" sein

    java.util.function.Function<Integer, int[]> createIntArray = int[]::new;
    int[] myArray = createIntArray.apply(5); // myArray wird ein int-Array der Größe 5 sein
    ```

**2. Stream-API**

**Was ist die Stream-API?**

Die Stream-API, eingeführt in Java 8, bietet eine leistungsstarke und elegante Möglichkeit, Sammlungen von Daten zu verarbeiten. Ein Stream repräsentiert eine Sequenz von Elementen, die verschiedene Aggregatoperationen unterstützt. Streams unterscheiden sich von Collections; Collections dienen der Speicherung von Daten, während Streams der Verarbeitung von Daten dienen.

**Schlüsselkonzepte der Stream-API:**

*   **Stream:** Eine Sequenz von Elementen, die sequentielle und parallele Aggregatoperationen unterstützt.
*   **Quelle:** Der Ursprung des Streams (z.B. eine Collection, ein Array, ein I/O-Kanal).
*   **Intermediate Operations (Zwischenoperationen):** Operationen, die den Stream transformieren oder filtern und einen neuen Stream zurückgeben. Diese Operationen sind lazy, was bedeutet, dass sie erst ausgeführt werden, wenn eine Terminaloperation aufgerufen wird.
*   **Terminal Operations (Terminaloperationen):** Operationen, die ein Ergebnis oder einen Seiteneffekt erzeugen und den Stream verbrauchen (der Stream ist nach einer Terminaloperation nicht mehr verwendbar).

**Erzeugen von Streams:**

Sie können Streams auf verschiedene Arten erstellen:

*   **Aus einer Collection:**

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<String> sequentialStream = names.stream();
    java.util.stream.Stream<String> parallelStream = names.parallelStream();
    ```

*   **Aus einem Array:**

    ```java
    int[] numbers = {1, 2, 3, 4, 5};
    java.util.stream.IntStream intStream = java.util.Arrays.stream(numbers);
    ```

*   **Verwenden von `Stream.of()`:**

    ```java
    java.util.stream.Stream<String> stringStream = java.util.stream.Stream.of("apple", "banana", "cherry");
    ```

*   **Verwenden von `Stream.iterate()`:** (Erzeugt einen unendlichen sequentiell geordneten Stream)

    ```java
    java.util.stream.Stream<Integer> evenNumbers = java.util.stream.Stream.iterate(0, n -> n + 2).limit(5); // 0, 2, 4, 6, 8
    ```

*   **Verwenden von `Stream.generate()`:** (Erzeugt einen unendlichen sequentiell ungeordneten Stream)

    ```java
    java.util.stream.Stream<Double> randomNumbers = java.util.stream.Stream.generate(Math::random).limit(3);
    ```

**Intermediate Operations (Zwischenoperationen):**

Diese Operationen transformieren oder filtern den Stream und geben einen neuen Stream zurück. Häufige Zwischenoperationen sind:

*   **`filter(Predicate<T> predicate)`:** Gibt einen Stream zurück, der aus den Elementen besteht, die dem gegebenen Prädikat entsprechen.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4, 5, 6);
    java.util.stream.Stream<Integer> evenNumbersStream = numbers.stream().filter(n -> n % 2 == 0); // 2, 4, 6
    ```

*   **`map(Function<T, R> mapper)`:** Gibt einen Stream zurück, der aus den Ergebnissen der Anwendung der gegebenen Funktion auf die Elemente dieses Streams besteht.

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<Integer> nameLengths = names.stream().map(String::length); // 5, 3, 7
    ```

*   **`flatMap(Function<T, Stream<R>> mapper)`:** Gibt einen Stream zurück, der aus den Ergebnissen des Ersetzens jedes Elements dieses Streams durch den Inhalt eines gemappten Streams besteht, der durch Anwenden der bereitgestellten Mapping-Funktion auf jedes Element erzeugt wird. Nützlich zum "Abflachen" verschachtelter Sammlungen.

    ```java
    java.util.List<java.util.List<Integer>> listOfLists = java.util.Arrays.asList(
            java.util.Arrays.asList(1, 2),
            java.util.Arrays.asList(3, 4, 5)
    );
    java.util.stream.Stream<Integer> singleStream = listOfLists.stream().flatMap(java.util.List::stream); // 1, 2, 3, 4, 5
    ```

*   **`sorted()`:** Gibt einen Stream zurück, der aus den Elementen dieses Streams besteht, sortiert nach der natürlichen Ordnung.

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("banana", "apple", "cherry");
    java.util.stream.Stream<String> sortedFruits = fruits.stream().sorted(); // apple, banana, cherry
    ```

*   **`distinct()`:** Gibt einen Stream zurück, der aus den unterschiedlichen Elementen (gemäß `equals()`) dieses Streams besteht.

    ```java
    java.util.List<Integer> numbersWithDuplicates = java.util.Arrays.asList(1, 2, 2, 3, 3, 3);
    java.util.stream.Stream<Integer> distinctNumbers = numbersWithDuplicates.stream().distinct(); // 1, 2, 3
    ```

*   **`peek(Consumer<T> action)`:** Gibt einen Stream zurück, der aus den Elementen dieses Streams besteht und zusätzlich die bereitgestellte Aktion für jedes Element ausführt, wenn die Elemente aus dem resultierenden Stream verbraucht werden. Primär für Debugging oder Seiteneffekte.

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob");
    java.util.stream.Stream<String> peekedNames = names.stream().peek(name -> System.out.println("Processing: " + name));
    peekedNames.forEach(System.out::println);
    // Ausgabe:
    // Processing: Alice
    // Alice
    // Processing: Bob
    // Bob
    ```

*   **`limit(long maxSize)`:** Gibt einen Stream zurück, der aus den Elementen dieses Streams besteht, auf eine Länge von maximal `maxSize` gekürzt.

    ```java
    java.util.stream.Stream<Integer> firstThree = java.util.stream.Stream.iterate(1, n -> n + 1).limit(3); // 1, 2, 3
    ```

*   **`skip(long n)`:** Gibt einen Stream zurück, der aus den verbleibenden Elementen dieses Streams besteht, nachdem die ersten `n` Elemente verworfen wurden.

    ```java
    java.util.stream.Stream<Integer> afterSkipping = java.util.stream.Stream.iterate(1, n -> n + 1).skip(2).limit(3); // 3, 4, 5
    ```

**Terminal Operations (Terminaloperationen):**

Diese Operationen erzeugen ein Ergebnis oder einen Seiteneffekt und verbrauchen den Stream. Häufige Terminaloperationen sind:

*   **`forEach(Consumer<T> action)`:** Führt eine Aktion für jedes Element dieses Streams aus.

    ```java
    java.util.List<String> colors = java.util.Arrays.asList("red", "green", "blue");
    colors.stream().forEach(System.out::println);
    ```

*   **`count()`:** Gibt die Anzahl der Elemente in diesem Stream zurück.

    ```java
    long numberOfFruits = java.util.Arrays.asList("apple", "banana", "cherry").stream().count(); // 3
    ```

*   **`collect(Collector<T, A, R> collector)`:** Führt eine mutable Reduktionsoperation auf den Elementen dieses Streams unter Verwendung eines `Collector` durch. Häufige Collector sind `toList()`, `toSet()`, `toMap()`, `joining()`, `groupingBy()`, `summarizingInt()`, etc.

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("apple", "banana", "cherry");
    java.util.List<String> fruitList = fruits.stream().collect(java.util.stream.Collectors.toList());
    java.util.Set<String> fruitSet = fruits.stream().collect(java.util.stream.Collectors.toSet());
    String joinedFruits = fruits.stream().collect(java.util.stream.Collectors.joining(", ")); // "apple, banana, cherry"
    ```

*   **`reduce(T identity, BinaryOperator<T> accumulator)`:** Führt eine Reduktion der Elemente dieses Streams durch, unter Verwendung des bereitgestellten Identitätswerts und einer assoziativen Akkumulationsfunktion.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4);
    int sum = numbers.stream().reduce(0, (a, b) -> a + b); // sum wird 10 sein
    ```

*   **`min(Comparator<T> comparator)`:** Gibt ein `Optional` zurück, das das minimale Element dieses Streams gemäß dem bereitgestellten Comparator beschreibt.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> minNumber = numbers.stream().min(Integer::compareTo); // Optional[1]
    ```

*   **`max(Comparator<T> comparator)`:** Gibt ein `Optional` zurück, das das maximale Element dieses Streams gemäß dem bereitgestellten Comparator beschreibt.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> maxNumber = numbers.stream().max(Integer::compareTo); // Optional[9]
    ```

*   **`findFirst()`:** Gibt ein `Optional` zurück, das das erste Element dieses Streams beschreibt.

    ```java
    java.util.Optional<String> firstFruit = java.util.Arrays.asList("apple", "banana", "cherry").stream().findFirst(); // Optional[apple]
    ```

*   **`findAny()`:** Gibt ein `Optional` zurück, das ein beliebiges Element des Streams beschreibt. Diese Operation gibt möglicherweise nicht immer das gleiche Ergebnis zurück, wenn der Stream parallel ist.

    ```java
    java.util.Optional<String> anyFruit = java.util.Arrays.asList("apple", "banana", "cherry").stream().findAny(); // Könnte Optional[apple], Optional[banana] oder Optional[cherry] zurückgeben
    ```

*   **`anyMatch(Predicate<T> predicate)`:** Gibt zurück, ob irgendein Element dieses Streams dem bereitgestellten Prädikat entspricht.

    ```java
    boolean hasEven = java.util.Arrays.asList(1, 3, 5, 2, 7).stream().anyMatch(n -> n % 2 == 0); // true
    ```

*   **`allMatch(Predicate<T> predicate)`:** Gibt zurück, ob alle Elemente dieses Streams dem bereitgestellten Prädikat entsprechen.

    ```java
    boolean allPositive = java.util.Arrays.asList(2, 4, 6, 8).stream().allMatch(n -> n > 0); // true
    ```

*   **`noneMatch(Predicate<T> predicate)`:** Gibt zurück, ob keine Elemente dieses Streams dem bereitgestellten Prädikat entsprechen.

    ```java
    boolean noNegatives = java.util.Arrays.asList(1, 2, 3, 4).stream().noneMatch(n -> n < 0); // true
    ```

**3. Beziehung zwischen Lambdas und Streams**

Lambda-Ausdrücke werden intensiv mit der Stream-API verwendet. Sie bieten eine prägnante Möglichkeit, das Verhalten für viele der Zwischen- und Terminaloperationen zu definieren. Zum Beispiel werden das `Predicate` in `filter()`, die `Function` in `map()` und der `Consumer` in `forEach()` oft mit Lambda-Ausdrücken implementiert.

**Beispiele, die Lambdas und Streams kombinieren:**

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class LambdaStreamExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve");

        // Filtere Namen, die mit 'A' beginnen, und wandle sie in Großbuchstaben um
        List<String> aNamesUppercase = names.stream()
                .filter(name -> name.startsWith("A")) // Lambda für Filterung
                .map(String::toUpperCase)             // Methodenreferenz für Mapping
                .collect(Collectors.toList());

        System.out.println("Namen, die mit 'A' beginnen, in Großbuchstaben: " + aNamesUppercase);
        // Ausgabe: Namen, die mit 'A' beginnen, in Großbuchstaben: [ALICE]

        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // Finde die Summe der Quadrate der geraden Zahlen
        int sumOfSquaresOfEvens = numbers.stream()
                .filter(n -> n % 2 == 0)       // Lambda für Filterung gerader Zahlen
                .map(n -> n * n)              // Lambda für Quadrieren
                .reduce(0, Integer::sum);     // Methodenreferenz für Summierung

        System.out.println("Summe der Quadrate der geraden Zahlen: " + sumOfSquaresOfEvens);
        // Ausgabe: Summe der Quadrate der geraden Zahlen: 220

        List<Person> people = Arrays.asList(
                new Person("Alice", 30),
                new Person("Bob", 25),
                new Person("Charlie", 35)
        );

        // Erhalte eine Liste der Namen von Personen, die älter als 28 sind
        List<String> olderPeopleNames = people.stream()
                .filter(person -> person.getAge() > 28) // Lambda für Filterung
                .map(Person::getName)                 // Methodenreferenz für Namensabruf
                .collect(Collectors.toList());

        System.out.println("Namen von Personen älter als 28: " + olderPeopleNames);
        // Ausgabe: Namen von Personen älter als 28: [Alice, Charlie]
    }
}

class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}
```

**4. Parallele Streams**

Die Stream-API unterstützt auch parallele Verarbeitung. Sie können Elemente eines Streams leicht parallel verarbeiten, indem Sie die Methode `parallelStream()` auf einer Collection verwenden oder indem Sie die Methode `parallel()` auf einem sequentiellen Stream aufrufen. Dies kann die Leistung für bestimmte Operationen auf großen Datensätzen erheblich verbessern.

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// Berechne die Summe der Quadrate parallel
int sumOfSquaresParallel = numbers.parallelStream()
        .map(n -> n * n)
        .reduce(0, Integer::sum);

System.out.println("Summe der Quadrate (parallel): " + sumOfSquaresParallel);
```

**Schlussfolgerung**

Lambda-Ausdrücke und die Stream-API sind leistungsstarke Ergänzungen für Java, die eine funktionalere und prägnantere Art der Code-Erstellung ermöglichen, insbesondere bei der Arbeit mit Datensammlungen. Durch die Verwendung von Lambdas mit Streams können Sie komplexe Datenverarbeitungsoperationen auf deklarative und lesbare Weise durchführen. Das Verständnis dieser Funktionen ist für die moderne Java-Entwicklung unerlässlich. Denken Sie daran, sie zu üben, um sich damit vertraut und sicher zu fühlen.