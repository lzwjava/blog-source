---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de programmation fonctionnelle en Java
translated: true
type: note
---

Java a adopté les principes de la programmation fonctionnelle depuis Java 8, introduisant les lambdas, les streams et d'autres fonctionnalités qui rendent le code plus concis, lisible et déclaratif. Ce guide couvre les fondamentaux jusqu'aux concepts avancés, en supposant une familiarité avec le Java de base. Nous utiliserons la syntaxe Java 8+, car c'est à ce moment que ces fonctionnalités ont fait leur apparition. Les exemples sont dans des blocs de code Java pour une copie facile.

## 1. Introduction à la programmation fonctionnelle en Java

La programmation fonctionnelle (FP) met l'accent sur :
- **Les fonctions pures** : Fonctions sans effets de bord (par exemple, pas de changements d'état mutable).
- **L'immuabilité** : Les données ne changent pas une fois créées.
- **Les fonctions d'ordre supérieur** : Fonctions qui prennent ou renvoient d'autres fonctions.
- **Le style déclaratif** : Se concentrer sur *ce qu'il faut* faire, pas *comment* le faire (par exemple, via des streams au lieu de boucles).

Java n'est pas purement fonctionnel comme Haskell, mais il mélange la PF avec ses racines orientées objet. Principaux facilitateurs :
- Les expressions lambda (fonctions anonymes).
- Les interfaces fonctionnelles (interfaces avec une seule méthode abstraite).
- L'API Streams pour traiter les collections de manière fonctionnelle.

Avantages : Réduction du code boilerplate, parallélisation plus facile, meilleure composabilité.

## 2. Expressions Lambda

Les lambdas sont des fonctions anonymes utilisées pour des implémentations courtes et ponctuelles. Elles sont la porte d'entrée vers la PF en Java.

### Syntaxe de base
Un lambda est : `(paramètres) -> { corps }`
- Les parenthèses sont optionnelles pour un seul paramètre.
- Les accolades sont optionnelles pour une seule expression (retour implicite).
- L'inférence de type fonctionne souvent, mais vous pouvez spécifier les types.

```java
// Classe interne anonyme traditionnelle
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello, World!");
    }
};

// Équivalent lambda
Runnable lambda = () -> System.out.println("Hello, World!");
lambda.run();
```

### Avec paramètres
```java
// Exemple d'opérateur binaire
BinaryOperator<Integer> add = (a, b) -> a + b;
System.out.println(add.apply(2, 3)); // 5

// Corps multi-lignes
Comparator<String> comparator = (s1, s2) -> {
    int lenDiff = s1.length() - s2.length();
    return lenDiff != 0 ? lenDiff : s1.compareTo(s2);
};
```

### Capture de variables (effectivement final)
Les lambdas peuvent accéder aux variables externes, mais elles doivent être **effectivement final** (non réaffectées).
```java
int threshold = 10;
Predicate<Integer> isHigh = x -> x > threshold; // OK
// threshold = 20; // Erreur : pas effectivement final
```

## 3. Interfaces fonctionnelles

Une interface fonctionnelle a exactement une méthode abstraite (SAM - Single Abstract Method). Java fournit des interfaces intégrées dans `java.util.function`.

### Exemples intégrés
- `Predicate<T>` : `boolean test(T t)`
- `Function<T, R>` : `R apply(T t)`
- `Consumer<T>` : `void accept(T t)`
- `Supplier<T>` : `T get()`
- `BiFunction<T, U, R>`, etc., pour deux entrées.

Personnalisées :
```java
@FunctionalInterface  // Optionnel, mais bonne pratique
interface Transformer {
    String transform(String input);
}

Transformer upper = s -> s.toUpperCase();
System.out.println(upper.transform("java")); // JAVA
```

Utilisez `@FunctionalInterface` pour imposer le SAM.

### Méthodes par défaut et statiques
Les interfaces fonctionnelles peuvent avoir des méthodes par défaut (Java 8+), comme `Optional.orElse()`.
```java
default int compare(String a, String b) { ... } // Autorisé
static void utility() { ... } // Autorisé
```

## 4. Références de méthodes

Raccourci pour les lambdas invoquant des méthodes existantes. Syntaxe : `Class::method` ou `instance::method`.

Types :
- Statique : `Class::staticMethod`
- Instance d'un type spécifique : `Class::instanceMethod`
- Instance d'un objet arbitraire : `object::instanceMethod`
- Constructeur : `Class::new`

Exemples :
```java
// Lambda : x -> System.out.println(x)
Consumer<String> printer = System.out::println;

// Méthode statique
Function<String, Integer> length = String::length;

// Méthode d'instance
List<String> list = Arrays.asList("a", "b");
list.forEach(System.out::println); // Imprime chaque élément

// Constructeur
Supplier<List<String>> listSupplier = ArrayList::new;
```

## 5. API Streams

Les Streams traitent les collections de manière déclarative : créer → transformer → collecter. Évaluation paresseuse (les opérations intermédiaires ne s'exécutent pas jusqu'à l'opération terminale).

### Création de Streams
```java
import java.util.*;
import java.util.stream.*;

List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

// À partir d'une collection
Stream<String> stream = names.stream();

// À partir d'un tableau
String[] arr = {"x", "y"};
Stream<String> arrStream = Arrays.stream(arr);

// Infini
Stream<Integer> infinite = Stream.iterate(0, n -> n + 1);
```

### Opérations intermédiaires (paresseuses)
Enchaînez-les ; aucun calcul jusqu'à l'opération terminale.
- `filter(Predicate)` : Garder les éléments correspondants.
- `map(Function)` : Transformer chaque élément.
- `flatMap(Function<? super T, ? extends Stream<? extends R>>)` : Aplatir les streams imbriqués.
- `distinct()`, `sorted()`, `limit(n)`, `skip(n)`.

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> evensSquared = numbers.stream()
    .filter(n -> n % 2 == 0)
    .map(n -> n * n)
    .collect(Collectors.toList()); // [4, 16]
```

### Opérations terminales (eager)
Déclenchent le calcul et renvoient un résultat.
- `collect(Collector)` : Vers une liste, un ensemble, une map.
- `forEach(Consumer)` : Effet de bord (à éviter si possible).
- `reduce()` : Agréger (par exemple, somme).
- `anyMatch()`, `allMatch()`, `findFirst()`.

```java
// Reduce : somme
int sum = numbers.stream().reduce(0, Integer::sum); // 15

// Collecter vers une map
Map<String, Integer> nameLengths = Stream.of("Alice", "Bob")
    .collect(Collectors.toMap(s -> s, String::length)); // {Alice=5, Bob=3}

// Regroupement
Map<Integer, List<String>> byLength = names.stream()
    .collect(Collectors.groupingBy(String::length)); // {5=[Alice, Charlie], 3=[Bob]}
```

### Streams parallèles
Pour le parallélisme : `parallelStream()` ou `.parallel()`. À utiliser avec prudence (débogage plus difficile).
```java
long count = names.parallelStream().count(); // 3
```

## 6. Collecteurs

De `java.util.stream.Collectors`. Construisent des réductions complexes.

Courants :
- `toList()`, `toSet()`, `toMap()`
- `joining()` : Concaténer des chaînes.
- `summingInt()`, `averagingDouble()`
- `groupingBy()`, `partitioningBy()`
- `collectingAndThen()` : Post-traiter.

```java
// Collecteur personnalisé pour le max par longueur
String longest = names.stream()
    .collect(Collectors.maxBy(Comparator.comparingInt(String::length)))
    .orElse(""); // "Charlie"

// Partition pairs/impairs
Map<Boolean, List<Integer>> partitions = numbers.stream()
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
```

## 7. Optional

Évite `NullPointerException` en encapsulant les valeurs potentiellement nulles. Encourage la gestion explicite des null.

Création :
- `Optional.of(value)` : Non null.
- `Optional.ofNullable(value)` : Null → vide.
- `Optional.empty()`.

Opérations :
- `isPresent()`, `ifPresent(Consumer)`
- `orElse(default)`, `orElseThrow()`
- `map()`, `flatMap()` pour l'enchaînement.

```java
Optional<String> opt = Optional.ofNullable(getName()); // Suppose peut retourner null

String name = opt.orElse("Unknown");
opt.ifPresent(System.out::println);

String upper = opt.map(String::toUpperCase).orElse("DEFAULT");
```

Les Streams renvoient souvent `Optional` (par exemple, `findFirst()`).

## 8. Sujets avancés

### Fonctions composables
`Function.andThen()`, `Function.compose()` pour l'enchaînement.
```java
Function<String, Integer> len = String::length;
Function<Integer, String> toStr = i -> "Len: " + i;

Function<String, String> chain = len.andThen(toStr);
System.out.println(chain.apply("Java")); // Len: 4
```

### Récursion et appels terminaux
Java manque d'optimisation, mais utilisez `Stream.iterate()` pour la récursion itérative.

### Aides à l'immuabilité
Utilisez `Collections.unmodifiableList()` ou des bibliothèques comme Guava/Immutable Collections (bien qu'intégrées depuis Java 10+ avec `List.of()`).

`List.of("a", "b")` crée des listes immuables (Java 9+).

### Pattern Matching (Java 21+ Preview/Stable)
Améliore la PF avec le destructuring dans les switches.
```java
// Fonctionnalité d'aperçu ; activez avec --enable-preview
String desc = switch (obj) {
    case Integer i -> "int: " + i;
    case String s -> "str: " + s.length();
    default -> "unknown";
};
```

### Virtual Threads (Java 21+)
La PF brille avec les threads légers pour les streams concurrents.

## 9. Bonnes pratiques

- **Préférez l'immuabilité** : Utilisez des champs finaux, évitez de muter les collections.
- **Évitez les effets de bord** : Gardez les lambdas pures ; effets de bord uniquement dans `forEach` ou des consumers explicites.
- **Streams vs. Boucles** : Utilisez les streams pour la lisibilité ; les boucles pour le code critique en performance.
- **Nulls** : Préférez `Optional` aux vérifications de null.
- **Tests** : Mockez facilement les interfaces fonctionnelles avec des lambdas.
- **Performance** : Les Streams ont une surcharge ; profilez avant d'utiliser le parallélisme.
- **Lisibilité** : Les lambdas courts sont bien ; extrayez des méthodes pour une logique complexe.

Pièges courants :
- Modifier l'état externe dans les lambdas.
- Oublier l'opération terminale (les streams ne font rien !).
- Abuser des streams parallèles (pas toujours plus rapides).

## 10. Exemple : Pipeline fonctionnel

Traiter une liste d'employés de manière fonctionnelle.

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

        // Noms des ingénieurs bien payés, triés
        List<String> result = employees.stream()
            .filter(e -> e.dept == Department.ENG)
            .filter(e -> e.salary > 52000)
            .map(Employee::getName)  // Suppose un getter
            .sorted()
            .collect(Collectors.toList());

        System.out.println(result); // [Charlie]
    }
}
```

## Conclusion

Les lambdas et la PF transforment Java d'impératif à expressif. Commencez par des remplacements simples (par exemple, `forEach` au lieu des boucles), puis construisez des pipelines. Pratiquez sur des projets réels pour la maîtrise. Pour des plongées plus profondes, expérimentez dans un IDE.

### Références
- [Oracle Java Tutorials: Lambda Expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)
- [Baeldung: Java 8 Functional Interfaces](https://www.baeldung.com/java-functional-interfaces)
- [Java Streams Guide](https://www.baeldung.com/java-8-streams)
- [Effective Java (3rd Ed.) - Item 42-45 on Lambdas](https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/)