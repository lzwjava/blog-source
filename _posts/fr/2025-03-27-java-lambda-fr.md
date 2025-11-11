---
audio: false
generated: true
lang: fr
layout: post
title: Expressions lambda et l'API Stream en Java
translated: true
type: note
---

D'accord, découvrons les expressions Lambda et l'API Stream en Java. Ce sont des fonctionnalités puissantes introduites dans Java 8 qui permettent un style de programmation plus fonctionnel, conduisant à un code plus concis et expressif.

**1. Expressions Lambda**

**Qu'est-ce qu'une expression Lambda ?**

Une expression lambda est essentiellement une fonction anonyme (sans nom). Elle vous permet de définir une fonction en ligne sans déclarer explicitement une méthode séparée. Les expressions lambda sont particulièrement utiles pour passer un comportement comme des données, rendant votre code plus flexible et lisible, surtout lorsqu'on travaille avec des interfaces fonctionnelles.

**Syntaxe d'une expression Lambda :**

Une expression lambda a la syntaxe de base suivante :

```java
(liste de paramètres) -> corps de l'expression
```

*   **Liste de paramètres :** C'est similaire aux paramètres d'une méthode. Elle peut être vide, contenir un paramètre ou plusieurs paramètres. Les types des paramètres peuvent souvent être inférés par le compilateur, vous n'avez donc pas toujours besoin de les déclarer explicitement.
*   **Token flèche (`->`) :** Celui-ci sépare la liste de paramètres du corps de l'expression.
*   **Corps de l'expression :** C'est le code que l'expression lambda exécute. Il peut s'agir d'une seule expression ou d'un bloc d'instructions entre accolades `{}`.

**Interfaces fonctionnelles :**

Les expressions lambda en Java sont utilisées pour implémenter les méthodes définies par des **interfaces fonctionnelles**. Une interface fonctionnelle est une interface qui contient **une seule et unique méthode abstraite**. Elle peut avoir des méthodes par défaut et des méthodes statiques, mais une seule méthode abstraite.

Des exemples d'interfaces fonctionnelles intégrées en Java incluent :

*   `Runnable` (méthode abstraite unique : `void run()`)
*   `Callable<V>` (méthode abstraite unique : `V call() throws Exception`)
*   `Comparator<T>` (méthode abstraite unique : `int compare(T o1, T o2)`)
*   `Consumer<T>` (méthode abstraite unique : `void accept(T t)`)
*   `Function<T, R>` (méthode abstraite unique : `R apply(T t)`)
*   `Predicate<T>` (méthode abstraite unique : `boolean test(T t)`)
*   `Supplier<T>` (méthode abstraite unique : `T get()`)

**Exemples d'expressions Lambda :**

Examinons quelques exemples pour comprendre comment fonctionnent les expressions lambda :

*   **Aucun paramètre :**

    ```java
    Runnable myRunnable = () -> System.out.println("Hello from lambda!");
    myRunnable.run(); // Output: Hello from lambda!
    ```

*   **Un paramètre (les parenthèses peuvent être omises) :**

    ```java
    Consumer<String> printMessage = message -> System.out.println("Message: " + message);
    printMessage.accept("Lambda is cool!"); // Output: Message: Lambda is cool!
    ```

*   **Plusieurs paramètres :**

    ```java
    java.util.Comparator<Integer> compareTwoNumbers = (a, b) -> a.compareTo(b);
    int result = compareTwoNumbers.compare(5, 10); // result will be -1
    ```

*   **Expression lambda avec un bloc d'instructions :**

    ```java
    java.util.function.Function<Integer, String> checkEvenOdd = number -> {
        if (number % 2 == 0) {
            return "Even";
        } else {
            return "Odd";
        }
    };
    String output = checkEvenOdd.apply(7); // output will be "Odd"
    ```

**Références de méthodes :**

Les références de méthodes sont une syntaxe raccourcie pour les expressions lambda qui appellent simplement une méthode existante. Elles rendent votre code encore plus concis. Il existe quatre types de références de méthodes :

1.  **Référence à une méthode statique :** `ClassName::staticMethodName`

    ```java
    java.util.function.Function<String, Integer> stringToInt = Integer::parseInt;
    int number = stringToInt.apply("123"); // number will be 123
    ```

2.  **Référence à une méthode d'instance d'un objet particulier :** `instance::instanceMethodName`

    ```java
    String message = "Hello";
    java.util.function.Consumer<String> printContains = s -> message.contains(s);
    printContains.accept("ll"); // This will execute message.contains("ll")
    ```
    Pour un `Supplier`, c'est plutôt :

    ```java
    String message = "Hello";
    java.util.function.Supplier<Integer> getLength = message::length;
    int len = getLength.get(); // len will be 5
    ```

3.  **Référence à une méthode d'instance d'un objet arbitraire d'un type particulier :** `ClassName::instanceMethodName`

    ```java
    java.util.function.BiPredicate<String, String> checkStartsWith = String::startsWith;
    boolean starts = checkStartsWith.test("Java", "Ja"); // starts will be true
    ```

4.  **Référence à un constructeur :** `ClassName::new`

    ```java
    java.util.function.Supplier<String> createString = String::new;
    String emptyString = createString.get(); // emptyString will be ""

    java.util.function.Function<Integer, int[]> createIntArray = int[]::new;
    int[] myArray = createIntArray.apply(5); // myArray will be an int array of size 5
    ```

**2. API Stream**

**Qu'est-ce que l'API Stream ?**

L'API Stream, introduite dans Java 8, fournit un moyen puissant et élégant de traiter des collections de données. Un stream représente une séquence d'éléments qui prend en charge diverses opérations d'agrégation. Les streams sont différents des collections ; les collections concernent le stockage des données, tandis que les streams concernent le traitement des données.

**Concepts clés de l'API Stream :**

*   **Stream :** Une séquence d'éléments prenant en charge des opérations d'agrégation séquentielles et parallèles.
*   **Source :** L'origine du stream (par exemple, une collection, un tableau, un canal d'E/S).
*   **Opérations intermédiaires :** Des opérations qui transforment ou filtrent le stream et renvoient un nouveau stream. Ces opérations sont *lazy*, ce qui signifie qu'elles ne sont pas exécutées tant qu'une opération terminale n'est pas invoquée.
*   **Opérations terminales :** Des opérations qui produisent un résultat ou un effet secondaire et consomment le stream (le stream n'est plus utilisable après une opération terminale).

**Création de Streams :**

Vous pouvez créer des streams de diverses manières :

*   **À partir d'une Collection :**

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<String> sequentialStream = names.stream();
    java.util.stream.Stream<String> parallelStream = names.parallelStream();
    ```

*   **À partir d'un Tableau :**

    ```java
    int[] numbers = {1, 2, 3, 4, 5};
    java.util.stream.IntStream intStream = java.util.Arrays.stream(numbers);
    ```

*   **En utilisant `Stream.of()` :**

    ```java
    java.util.stream.Stream<String> stringStream = java.util.stream.Stream.of("apple", "banana", "cherry");
    ```

*   **En utilisant `Stream.iterate()` :** (Crée un stream ordonné séquentiel infini)

    ```java
    java.util.stream.Stream<Integer> evenNumbers = java.util.stream.Stream.iterate(0, n -> n + 2).limit(5); // 0, 2, 4, 6, 8
    ```

*   **En utilisant `Stream.generate()` :** (Crée un stream non ordonné séquentiel infini)

    ```java
    java.util.stream.Stream<Double> randomNumbers = java.util.stream.Stream.generate(Math::random).limit(3);
    ```

**Opérations intermédiaires :**

Ces opérations transforment ou filtrent le stream et renvoient un nouveau stream. Les opérations intermédiaires courantes incluent :

*   **`filter(Predicate<T> predicate)` :** Renvoie un stream constitué des éléments qui correspondent au prédicat donné.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4, 5, 6);
    java.util.stream.Stream<Integer> evenNumbersStream = numbers.stream().filter(n -> n % 2 == 0); // 2, 4, 6
    ```

*   **`map(Function<T, R> mapper)` :** Renvoie un stream constitué des résultats de l'application de la fonction donnée aux éléments de ce stream.

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<Integer> nameLengths = names.stream().map(String::length); // 5, 3, 7
    ```

*   **`flatMap(Function<T, Stream<R>> mapper)` :** Renvoie un stream constitué des résultats du remplacement de chaque élément de ce stream par le contenu d'un stream mappé produit en appliquant la fonction de mapping fournie à chaque élément. Utile pour aplatir des collections imbriquées.

    ```java
    java.util.List<java.util.List<Integer>> listOfLists = java.util.Arrays.asList(
            java.util.Arrays.asList(1, 2),
            java.util.Arrays.asList(3, 4, 5)
    );
    java.util.stream.Stream<Integer> singleStream = listOfLists.stream().flatMap(java.util.List::stream); // 1, 2, 3, 4, 5
    ```

*   **`sorted()` :** Renvoie un stream constitué des éléments de ce stream, triés selon l'ordre naturel.

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("banana", "apple", "cherry");
    java.util.stream.Stream<String> sortedFruits = fruits.stream().sorted(); // apple, banana, cherry
    ```

*   **`distinct()` :** Renvoie un stream constitué des éléments distincts (selon `equals()`) de ce stream.

    ```java
    java.util.List<Integer> numbersWithDuplicates = java.util.Arrays.asList(1, 2, 2, 3, 3, 3);
    java.util.stream.Stream<Integer> distinctNumbers = numbersWithDuplicates.stream().distinct(); // 1, 2, 3
    ```

*   **`peek(Consumer<T> action)` :** Renvoie un stream constitué des éléments de ce stream, en effectuant en plus l'action fournie sur chaque élément lors de leur consommation à partir du stream résultant. Principalement pour le débogage ou les effets secondaires.

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob");
    java.util.stream.Stream<String> peekedNames = names.stream().peek(name -> System.out.println("Processing: " + name));
    peekedNames.forEach(System.out::println);
    // Output:
    // Processing: Alice
    // Alice
    // Processing: Bob
    // Bob
    ```

*   **`limit(long maxSize)` :** Renvoie un stream constitué des éléments de ce stream, tronqué pour ne pas dépasser `maxSize` en longueur.

    ```java
    java.util.stream.Stream<Integer> firstThree = java.util.stream.Stream.iterate(1, n -> n + 1).limit(3); // 1, 2, 3
    ```

*   **`skip(long n)` :** Renvoie un stream constitué des éléments restants de ce stream après avoir ignoré les `n` premiers éléments.

    ```java
    java.util.stream.Stream<Integer> afterSkipping = java.util.stream.Stream.iterate(1, n -> n + 1).skip(2).limit(3); // 3, 4, 5
    ```

**Opérations terminales :**

Ces opérations produisent un résultat ou un effet secondaire et consomment le stream. Les opérations terminales courantes incluent :

*   **`forEach(Consumer<T> action)` :** Effectue une action pour chaque élément de ce stream.

    ```java
    java.util.List<String> colors = java.util.Arrays.asList("red", "green", "blue");
    colors.stream().forEach(System.out::println);
    ```

*   **`count()` :** Renvoie le nombre d'éléments dans ce stream.

    ```java
    long numberOfFruits = java.util.Arrays.asList("apple", "banana", "cherry").stream().count(); // 3
    ```

*   **`collect(Collector<T, A, R> collector)` :** Effectue une opération de réduction mutable sur les éléments de ce stream en utilisant un `Collector`. Les collecteurs courants incluent `toList()`, `toSet()`, `toMap()`, `joining()`, `groupingBy()`, `summarizingInt()`, etc.

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("apple", "banana", "cherry");
    java.util.List<String> fruitList = fruits.stream().collect(java.util.stream.Collectors.toList());
    java.util.Set<String> fruitSet = fruits.stream().collect(java.util.stream.Collectors.toSet());
    String joinedFruits = fruits.stream().collect(java.util.stream.Collectors.joining(", ")); // "apple, banana, cherry"
    ```

*   **`reduce(T identity, BinaryOperator<T> accumulator)` :** Effectue une réduction sur les éléments de ce stream, en utilisant la valeur d'identité fournie et une fonction d'accumulation associative.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4);
    int sum = numbers.stream().reduce(0, (a, b) -> a + b); // sum will be 10
    ```

*   **`min(Comparator<T> comparator)` :** Renvoie un `Optional` décrivant l'élément minimum de ce stream selon le comparateur fourni.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> minNumber = numbers.stream().min(Integer::compareTo); // Optional[1]
    ```

*   **`max(Comparator<T> comparator)` :** Renvoie un `Optional` décrivant l'élément maximum de ce stream selon le comparateur fourni.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> maxNumber = numbers.stream().max(Integer::compareTo); // Optional[9]
    ```

*   **`findFirst()` :** Renvoie un `Optional` décrivant le premier élément de ce stream.

    ```java
    java.util.Optional<String> firstFruit = java.util.Arrays.asList("apple", "banana", "cherry").stream().findFirst(); // Optional[apple]
    ```

*   **`findAny()` :** Renvoie un `Optional` décrivant un élément quelconque du stream. Cette opération peut ne pas toujours renvoyer le même résultat lorsque le stream est parallèle.

    ```java
    java.util.Optional<String> anyFruit = java.util.Arrays.asList("apple", "banana", "cherry").stream().findAny(); // Might return Optional[apple], Optional[banana], or Optional[cherry]
    ```

*   **`anyMatch(Predicate<T> predicate)` :** Renvoie si un élément de ce stream correspond au prédicat fourni.

    ```java
    boolean hasEven = java.util.Arrays.asList(1, 3, 5, 2, 7).stream().anyMatch(n -> n % 2 == 0); // true
    ```

*   **`allMatch(Predicate<T> predicate)` :** Renvoie si tous les éléments de ce stream correspondent au prédicat fourni.

    ```java
    boolean allPositive = java.util.Arrays.asList(2, 4, 6, 8).stream().allMatch(n -> n > 0); // true
    ```

*   **`noneMatch(Predicate<T> predicate)` :** Renvoie si aucun élément de ce stream ne correspond au prédicat fourni.

    ```java
    boolean noNegatives = java.util.Arrays.asList(1, 2, 3, 4).stream().noneMatch(n -> n < 0); // true
    ```

**3. Relation entre les Lambdas et les Streams**

Les expressions lambda sont largement utilisées avec l'API Stream. Elles fournissent un moyen concis de définir le comportement pour de nombreuses opérations intermédiaires et terminales. Par exemple, le `Predicate` dans `filter()`, la `Function` dans `map()` et le `Consumer` dans `forEach()` sont souvent implémentés à l'aide d'expressions lambda.

**Exemples combinant Lambdas et Streams :**

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class LambdaStreamExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve");

        // Filtrer les noms commençant par 'A' et les convertir en majuscules
        List<String> aNamesUppercase = names.stream()
                .filter(name -> name.startsWith("A")) // Lambda pour le filtrage
                .map(String::toUpperCase)             // Référence de méthode pour le mapping
                .collect(Collectors.toList());

        System.out.println("Names starting with 'A' in uppercase: " + aNamesUppercase);
        // Output: Names starting with 'A' in uppercase: [ALICE]

        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // Trouver la somme des carrés des nombres pairs
        int sumOfSquaresOfEvens = numbers.stream()
                .filter(n -> n % 2 == 0)       // Lambda pour filtrer les nombres pairs
                .map(n -> n * n)              // Lambda pour la mise au carré
                .reduce(0, Integer::sum);     // Référence de méthode pour la somme

        System.out.println("Sum of squares of even numbers: " + sumOfSquaresOfEvens);
        // Output: Sum of squares of even numbers: 220

        List<Person> people = Arrays.asList(
                new Person("Alice", 30),
                new Person("Bob", 25),
                new Person("Charlie", 35)
        );

        // Obtenir une liste des noms des personnes de plus de 28 ans
        List<String> olderPeopleNames = people.stream()
                .filter(person -> person.getAge() > 28) // Lambda pour le filtrage
                .map(Person::getName)                 // Référence de méthode pour obtenir le nom
                .collect(Collectors.toList());

        System.out.println("Names of people older than 28: " + olderPeopleNames);
        // Output: Names of people older than 28: [Alice, Charlie]
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

**4. Streams parallèles**

L'API Stream prend également en charge le traitement parallèle. Vous pouvez facilement traiter les éléments d'un stream en parallèle en utilisant la méthode `parallelStream()` sur une collection ou en appelant la méthode `parallel()` sur un stream séquentiel. Cela peut améliorer considérablement les performances pour certaines opérations sur de grands ensembles de données.

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// Calculer la somme des carrés en parallèle
int sumOfSquaresParallel = numbers.parallelStream()
        .map(n -> n * n)
        .reduce(0, Integer::sum);

System.out.println("Sum of squares (parallel): " + sumOfSquaresParallel);
```

**Conclusion**

Les expressions lambda et l'API Stream sont des ajouts puissants à Java qui permettent une manière plus fonctionnelle et concise d'écrire du code, en particulier lorsqu'il s'agit de traiter des collections de données. En utilisant les lambdas avec les streams, vous pouvez effectuer des opérations complexes de traitement de données de manière déclarative et lisible. Comprendre ces fonctionnalités est essentiel pour le développement Java moderne. N'oubliez pas de vous entraîner à les utiliser pour devenir plus à l'aise et compétent.