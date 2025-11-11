---
audio: false
generated: true
lang: es
layout: post
title: Expresiones Lambda y la API Stream en Java
translated: true
type: note
---

De acuerdo, aprendamos sobre Lambda Expressions y la Stream API en Java. Estas son características poderosas introducidas en Java 8 que permiten un estilo de programación más funcional, conduciendo a un código más conciso y expresivo.

**1. Expresiones Lambda**

**¿Qué es una Expresión Lambda?**

Una expresión lambda es esencialmente una función anónima (sin nombre). Te permite definir una función en línea sin declarar explícitamente un método separado. Las expresiones lambda son particularmente útiles para pasar comportamiento como datos, haciendo tu código más flexible y legible, especialmente cuando se trabaja con interfaces funcionales.

**Sintaxis de una Expresión Lambda:**

Una expresión lambda tiene la siguiente sintaxis básica:

```java
(lista de parámetros) -> cuerpo de la expresión
```

*   **Lista de Parámetros:** Esto es similar a los parámetros de un método. Puede estar vacía, contener un parámetro o múltiples parámetros. Los tipos de los parámetros a menudo pueden ser inferidos por el compilador, por lo que no siempre necesitas declararlos explícitamente.
*   **Token de Flecha (`->`):** Esto separa la lista de parámetros del cuerpo de la expresión.
*   **Cuerpo de la Expresión:** Este es el código que la expresión lambda ejecuta. Puede ser una sola expresión o un bloque de sentencias encerrado entre llaves `{}`.

**Interfaces Funcionales:**

Las expresiones lambda en Java se utilizan para implementar métodos definidos por **interfaces funcionales**. Una interfaz funcional es una interfaz que contiene **solo un método abstracto**. Puede tener métodos predeterminados y métodos estáticos, pero solo un método abstracto.

Ejemplos de interfaces funcionales integradas en Java incluyen:

*   `Runnable` (método abstracto único: `void run()`)
*   `Callable<V>` (método abstracto único: `V call() throws Exception`)
*   `Comparator<T>` (método abstracto único: `int compare(T o1, T o2)`)
*   `Consumer<T>` (método abstracto único: `void accept(T t)`)
*   `Function<T, R>` (método abstracto único: `R apply(T t)`)
*   `Predicate<T>` (método abstracto único: `boolean test(T t)`)
*   `Supplier<T>` (método abstracto único: `T get()`)

**Ejemplos de Expresiones Lambda:**

Veamos algunos ejemplos para entender cómo funcionan las expresiones lambda:

*   **Sin parámetros:**

    ```java
    Runnable myRunnable = () -> System.out.println("¡Hola desde lambda!");
    myRunnable.run(); // Salida: ¡Hola desde lambda!
    ```

*   **Un parámetro (se pueden omitir los paréntesis):**

    ```java
    Consumer<String> printMessage = message -> System.out.println("Mensaje: " + message);
    printMessage.accept("¡Lambda es genial!"); // Salida: Mensaje: ¡Lambda es genial!
    ```

*   **Múltiples parámetros:**

    ```java
    java.util.Comparator<Integer> compareTwoNumbers = (a, b) -> a.compareTo(b);
    int result = compareTwoNumbers.compare(5, 10); // el resultado será -1
    ```

*   **Expresión lambda con un bloque de sentencias:**

    ```java
    java.util.function.Function<Integer, String> checkEvenOdd = number -> {
        if (number % 2 == 0) {
            return "Par";
        } else {
            return "Impar";
        }
    };
    String output = checkEvenOdd.apply(7); // la salida será "Impar"
    ```

**Referencias a Métodos:**

Las referencias a métodos son una sintaxis abreviada para las expresiones lambda que simplemente llaman a un método existente. Hacen tu código aún más conciso. Hay cuatro tipos de referencias a métodos:

1.  **Referencia a un método estático:** `NombreDeClase::nombreMetodoEstatico`

    ```java
    java.util.function.Function<String, Integer> stringToInt = Integer::parseInt;
    int number = stringToInt.apply("123"); // el número será 123
    ```

2.  **Referencia a un método de instancia de un objeto particular:** `instancia::nombreMetodoInstancia`

    ```java
    String message = "Hola";
    java.util.function.Supplier<Integer> getLength = message::length;
    int len = getLength.get(); // len será 5
    ```

3.  **Referencia a un método de instancia de un objeto arbitrario de un tipo particular:** `NombreDeClase::nombreMetodoInstancia`

    ```java
    java.util.function.BiPredicate<String, String> checkStartsWith = String::startsWith;
    boolean starts = checkStartsWith.test("Java", "Ja"); // starts será true
    ```

4.  **Referencia a un constructor:** `NombreDeClase::new`

    ```java
    java.util.function.Supplier<String> createString = String::new;
    String emptyString = createString.get(); // emptyString será ""

    java.util.function.Function<Integer, int[]> createIntArray = int[]::new;
    int[] myArray = createIntArray.apply(5); // myArray será un array de int de tamaño 5
    ```

**2. Stream API**

**¿Qué es la Stream API?**

La Stream API, introducida en Java 8, proporciona una forma poderosa y elegante de procesar colecciones de datos. Un stream representa una secuencia de elementos que admite varias operaciones agregadas. Los streams son diferentes de las colecciones; las colecciones se tratan de almacenar datos, mientras que los streams se tratan de procesar datos.

**Conceptos Clave de la Stream API:**

*   **Stream:** Una secuencia de elementos que admite operaciones agregadas secuenciales y paralelas.
*   **Fuente:** El origen del stream (por ejemplo, una colección, un array, un canal de E/S).
*   **Operaciones Intermedias:** Operaciones que transforman o filtran el stream y devuelven un nuevo stream. Estas operaciones son perezosas, lo que significa que no se ejecutan hasta que se invoca una operación terminal.
*   **Operaciones Terminales:** Operaciones que producen un resultado o un efecto secundario y consumen el stream (el stream ya no es utilizable después de una operación terminal).

**Creando Streams:**

Puedes crear streams de varias maneras:

*   **Desde una Colección:**

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<String> sequentialStream = names.stream();
    java.util.stream.Stream<String> parallelStream = names.parallelStream();
    ```

*   **Desde un Array:**

    ```java
    int[] numbers = {1, 2, 3, 4, 5};
    java.util.stream.IntStream intStream = java.util.Arrays.stream(numbers);
    ```

*   **Usando `Stream.of()`:**

    ```java
    java.util.stream.Stream<String> stringStream = java.util.stream.Stream.of("manzana", "plátano", "cereza");
    ```

*   **Usando `Stream.iterate()`:** (Crea un stream ordenado secuencial infinito)

    ```java
    java.util.stream.Stream<Integer> evenNumbers = java.util.stream.Stream.iterate(0, n -> n + 2).limit(5); // 0, 2, 4, 6, 8
    ```

*   **Usando `Stream.generate()`:** (Crea un stream no ordenado secuencial infinito)

    ```java
    java.util.stream.Stream<Double> randomNumbers = java.util.stream.Stream.generate(Math::random).limit(3);
    ```

**Operaciones Intermedias:**

Estas operaciones transforman o filtran el stream y devuelven un nuevo stream. Las operaciones intermedias comunes incluyen:

*   **`filter(Predicate<T> predicate)`:** Devuelve un stream que consiste en los elementos que coinciden con el predicado dado.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4, 5, 6);
    java.util.stream.Stream<Integer> evenNumbersStream = numbers.stream().filter(n -> n % 2 == 0); // 2, 4, 6
    ```

*   **`map(Function<T, R> mapper)`:** Devuelve un stream que consiste en los resultados de aplicar la función dada a los elementos de este stream.

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<Integer> nameLengths = names.stream().map(String::length); // 5, 3, 7
    ```

*   **`flatMap(Function<T, Stream<R>> mapper)`:** Devuelve un stream que consiste en los resultados de reemplazar cada elemento de este stream con el contenido de un stream mapeado producido al aplicar la función de mapeo proporcionada a cada elemento. Útil para aplanar colecciones anidadas.

    ```java
    java.util.List<java.util.List<Integer>> listOfLists = java.util.Arrays.asList(
            java.util.Arrays.asList(1, 2),
            java.util.Arrays.asList(3, 4, 5)
    );
    java.util.stream.Stream<Integer> singleStream = listOfLists.stream().flatMap(java.util.List::stream); // 1, 2, 3, 4, 5
    ```

*   **`sorted()`:** Devuelve un stream que consiste en los elementos de este stream, ordenados según el orden natural.

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("plátano", "manzana", "cereza");
    java.util.stream.Stream<String> sortedFruits = fruits.stream().sorted(); // manzana, plátano, cereza
    ```

*   **`distinct()`:** Devuelve un stream que consiste en los elementos distintos (según `equals()`) de este stream.

    ```java
    java.util.List<Integer> numbersWithDuplicates = java.util.Arrays.asList(1, 2, 2, 3, 3, 3);
    java.util.stream.Stream<Integer> distinctNumbers = numbersWithDuplicates.stream().distinct(); // 1, 2, 3
    ```

*   **`peek(Consumer<T> action)`:** Devuelve un stream que consiste en los elementos de este stream, realizando adicionalmente la acción proporcionada en cada elemento a medida que los elementos son consumidos del stream resultante. Principalmente para depuración o efectos secundarios.

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob");
    java.util.stream.Stream<String> peekedNames = names.stream().peek(name -> System.out.println("Procesando: " + name));
    peekedNames.forEach(System.out::println);
    // Salida:
    // Procesando: Alice
    // Alice
    // Procesando: Bob
    // Bob
    ```

*   **`limit(long maxSize)`:** Devuelve un stream que consiste en los elementos de este stream, truncado a no más de `maxSize` en longitud.

    ```java
    java.util.stream.Stream<Integer> firstThree = java.util.stream.Stream.iterate(1, n -> n + 1).limit(3); // 1, 2, 3
    ```

*   **`skip(long n)`:** Devuelve un stream que consiste en los elementos restantes de este stream después de descartar los primeros `n` elementos.

    ```java
    java.util.stream.Stream<Integer> afterSkipping = java.util.stream.Stream.iterate(1, n -> n + 1).skip(2).limit(3); // 3, 4, 5
    ```

**Operaciones Terminales:**

Estas operaciones producen un resultado o un efecto secundario y consumen el stream. Las operaciones terminales comunes incluyen:

*   **`forEach(Consumer<T> action)`:** Realiza una acción para cada elemento de este stream.

    ```java
    java.util.List<String> colors = java.util.Arrays.asList("rojo", "verde", "azul");
    colors.stream().forEach(System.out::println);
    ```

*   **`count()`:** Devuelve el conteo de elementos en este stream.

    ```java
    long numberOfFruits = java.util.Arrays.asList("manzana", "plátano", "cereza").stream().count(); // 3
    ```

*   **`collect(Collector<T, A, R> collector)`:** Realiza una operación de reducción mutable en los elementos de este stream usando un `Collector`. Los colectores comunes incluyen `toList()`, `toSet()`, `toMap()`, `joining()`, `groupingBy()`, `summarizingInt()`, etc.

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("manzana", "plátano", "cereza");
    java.util.List<String> fruitList = fruits.stream().collect(java.util.stream.Collectors.toList());
    java.util.Set<String> fruitSet = fruits.stream().collect(java.util.stream.Collectors.toSet());
    String joinedFruits = fruits.stream().collect(java.util.stream.Collectors.joining(", ")); // "manzana, plátano, cereza"
    ```

*   **`reduce(T identity, BinaryOperator<T> accumulator)`:** Realiza una reducción en los elementos de este stream, usando el valor de identidad proporcionado y una función de acumulación asociativa.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4);
    int sum = numbers.stream().reduce(0, (a, b) -> a + b); // la suma será 10
    ```

*   **`min(Comparator<T> comparator)`:** Devuelve un `Optional` que describe el elemento mínimo de este stream según el comparador proporcionado.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> minNumber = numbers.stream().min(Integer::compareTo); // Optional[1]
    ```

*   **`max(Comparator<T> comparator)`:** Devuelve un `Optional` que describe el elemento máximo de este stream según el comparador proporcionado.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> maxNumber = numbers.stream().max(Integer::compareTo); // Optional[9]
    ```

*   **`findFirst()`:** Devuelve un `Optional` que describe el primer elemento de este stream.

    ```java
    java.util.Optional<String> firstFruit = java.util.Arrays.asList("manzana", "plátano", "cereza").stream().findFirst(); // Optional[manzana]
    ```

*   **`findAny()`:** Devuelve un `Optional` que describe algún elemento del stream. Esta operación podría no siempre devolver el mismo resultado cuando el stream es paralelo.

    ```java
    java.util.Optional<String> anyFruit = java.util.Arrays.asList("manzana", "plátano", "cereza").stream().findAny(); // Podría devolver Optional[manzana], Optional[plátano], o Optional[cereza]
    ```

*   **`anyMatch(Predicate<T> predicate)`:** Devuelve si algún elemento de este stream coincide con el predicado proporcionado.

    ```java
    boolean hasEven = java.util.Arrays.asList(1, 3, 5, 2, 7).stream().anyMatch(n -> n % 2 == 0); // true
    ```

*   **`allMatch(Predicate<T> predicate)`:** Devuelve si todos los elementos de este stream coinciden con el predicado proporcionado.

    ```java
    boolean allPositive = java.util.Arrays.asList(2, 4, 6, 8).stream().allMatch(n -> n > 0); // true
    ```

*   **`noneMatch(Predicate<T> predicate)`:** Devuelve si ningún elemento de este stream coincide con el predicado proporcionado.

    ```java
    boolean noNegatives = java.util.Arrays.asList(1, 2, 3, 4).stream().noneMatch(n -> n < 0); // true
    ```

**3. Relación Entre Lambdas y Streams**

Las expresiones lambda se utilizan mucho con la Stream API. Proporcionan una forma concisa de definir el comportamiento para muchas de las operaciones intermedias y terminales. Por ejemplo, el `Predicate` en `filter()`, la `Function` en `map()` y el `Consumer` en `forEach()` a menudo se implementan usando expresiones lambda.

**Ejemplos Combinando Lambdas y Streams:**

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class LambdaStreamExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve");

        // Filtrar nombres que empiezan con 'A' y convertirlos a mayúsculas
        List<String> aNamesUppercase = names.stream()
                .filter(name -> name.startsWith("A")) // Lambda para filtrar
                .map(String::toUpperCase)             // Referencia a método para mapear
                .collect(Collectors.toList());

        System.out.println("Nombres que empiezan con 'A' en mayúsculas: " + aNamesUppercase);
        // Salida: Nombres que empiezan con 'A' en mayúsculas: [ALICE]

        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // Encontrar la suma de los cuadrados de los números pares
        int sumOfSquaresOfEvens = numbers.stream()
                .filter(n -> n % 2 == 0)       // Lambda para filtrar números pares
                .map(n -> n * n)              // Lambda para elevar al cuadrado
                .reduce(0, Integer::sum);     // Referencia a método para sumar

        System.out.println("Suma de los cuadrados de los números pares: " + sumOfSquaresOfEvens);
        // Salida: Suma de los cuadrados de los números pares: 220

        List<Person> people = Arrays.asList(
                new Person("Alice", 30),
                new Person("Bob", 25),
                new Person("Charlie", 35)
        );

        // Obtener una lista de nombres de personas mayores de 28 años
        List<String> olderPeopleNames = people.stream()
                .filter(person -> person.getAge() > 28) // Lambda para filtrar
                .map(Person::getName)                 // Referencia a método para obtener el nombre
                .collect(Collectors.toList());

        System.out.println("Nombres de personas mayores de 28: " + olderPeopleNames);
        // Salida: Nombres de personas mayores de 28: [Alice, Charlie]
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

**4. Streams Paralelos**

La Stream API también admite procesamiento paralelo. Puedes procesar fácilmente elementos de un stream en paralelo usando el método `parallelStream()` en una colección o llamando al método `parallel()` en un stream secuencial. Esto puede mejorar significativamente el rendimiento para ciertas operaciones en grandes conjuntos de datos.

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// Calcular la suma de cuadrados en paralelo
int sumOfSquaresParallel = numbers.parallelStream()
        .map(n -> n * n)
        .reduce(0, Integer::sum);

System.out.println("Suma de cuadrados (paralelo): " + sumOfSquaresParallel);
```

**Conclusión**

Las expresiones lambda y la Stream API son adiciones poderosas a Java que permiten una forma más funcional y concisa de escribir código, especialmente cuando se trata con colecciones de datos. Al usar lambdas con streams, puedes realizar operaciones complejas de procesamiento de datos de una manera declarativa y legible. Comprender estas características es esencial para el desarrollo moderno en Java. Recuerda practicar usándolas para volverte más cómodo y competente.