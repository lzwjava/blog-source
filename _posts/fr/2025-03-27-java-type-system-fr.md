---
audio: false
generated: true
lang: fr
layout: post
title: Système de types de Java
translated: true
type: note
---

Parfait, plongeons dans le système de types de Java ! Ce tutoriel couvrira les concepts fondamentaux pour bien démarrer.

**Qu'est-ce qu'un système de types ?**

En programmation, un système de types définit les types de valeurs qui peuvent être utilisées et la manière dont elles peuvent être manipulées. Il aide à garantir que les programmes sont type-safe, ce qui signifie que les opérations sont effectuées sur les types de données corrects, évitant ainsi des erreurs inattendues et améliorant la fiabilité du code.

Java possède **un système de types fort et statique**.

* **Typage Fort :** Java est fortement typé, ce qui signifie que le type d'une variable est strictement appliqué au moment de la compilation et de l'exécution. Vous ne pouvez généralement pas effectuer d'opérations sur des types incompatibles sans conversion explicite (cast). Cela aide à détecter les erreurs tôt dans le processus de développement.
* **Typage Statique :** Java est statiquement typé, ce qui signifie que les types des variables sont déclarés (ou inférés dans certains cas avec `var`) avant que le programme ne soit exécuté. Le compilateur vérifie la compatibilité de ces types avant l'exécution.

**Composants clés du système de types de Java :**

Le système de types de Java est largement divisé en deux catégories principales :

1.  **Types Primitifs :** Ce sont les types de données les plus basiques en Java. Ils représentent des valeurs uniques directement en mémoire.
2.  **Types Références :** Ces types représentent des objets, qui sont des instances de classes ou d'interfaces. Les variables de type référence stockent l'adresse mémoire (la référence) de l'objet.

Explorons chacun d'eux en détail.

**1. Types Primitifs :**

Java a huit types de données primitifs :

| Type     | Taille (bits) | Description                                      | Plage                                                                 | Exemple           |
| -------- | ------------- | ------------------------------------------------ | --------------------------------------------------------------------- | ----------------- |
| `byte`   | 8             | Entier signé                                     | -128 à 127                                                            | `byte age = 30;`  |
| `short`  | 16            | Entier signé                                     | -32 768 à 32 767                                                      | `short count = 1000;` |
| `int`    | 32            | Entier signé                                     | -2 147 483 648 à 2 147 483 647                                        | `int score = 95;` |
| `long`   | 64            | Entier signé                                     | -9 223 372 036 854 775 808 à 9 223 372 036 854 775 807               | `long population = 1000000000L;` (Notez le suffixe 'L') |
| `float`  | 32            | Nombre à virgule flottante simple précision (IEEE 754) | Environ ±3,40282347E+38F                                              | `float price = 19.99F;` (Notez le suffixe 'F') |
| `double` | 64            | Nombre à virgule flottante double précision (IEEE 754) | Environ ±1,79769313486231570E+308                                     | `double pi = 3.14159;` |
| `char`   | 16            | Caractère Unicode unique                         | '\u0000' (0) à '\uffff' (65 535)                                      | `char initial = 'J';` |
| `boolean`| Variable      | Représente une valeur logique                    | `true` ou `false`                                                     | `boolean isVisible = true;` |

**Points clés sur les types primitifs :**

* Ils sont stockés directement en mémoire.
* Ils ont des tailles et des plages prédéfinies.
* Ils ne sont pas des objets et n'ont pas de méthodes associées (bien que les classes wrapper comme `Integer`, `Double`, etc., fournissent des représentations objet).
* Des valeurs par défaut sont attribuées aux champs de type primitif s'ils ne sont pas explicitement initialisés (par exemple, `int` vaut par défaut 0, `boolean` vaut par défaut `false`).

**2. Types Références :**

Les types références représentent des objets, qui sont des instances de classes ou d'interfaces. Les variables de types références contiennent l'adresse mémoire (la référence) de l'objet dans le tas (heap).

**Types Références Courants :**

* **Classes :** Les classes sont des plans pour créer des objets. Elles définissent les données (champs/attributs) et le comportement (méthodes) des objets de ce type.
    ```java
    class Dog {
        String name;
        int age;

        public void bark() {
            System.out.println("Woof !");
        }
    }

    public class Main {
        public static void main(String[] args) {
            Dog myDog = new Dog(); // 'Dog' est le type référence
            myDog.name = "Buddy";
            myDog.age = 3;
            myDog.bark();
        }
    }
    ```
* **Interfaces :** Les interfaces définissent un contrat de méthodes qu'une classe peut implémenter. Elles représentent un ensemble de comportements.
    ```java
    interface Animal {
        void makeSound();
    }

    class Cat implements Animal {
        public void makeSound() {
            System.out.println("Meow !");
        }
    }

    public class Main {
        public static void main(String[] args) {
            Animal myCat = new Cat(); // 'Animal' est le type référence
            myCat.makeSound();
        }
    }
    ```
* **Tableaux :** Les tableaux sont des collections d'éléments du même type. Le type du tableau est déterminé par le type de ses éléments.
    ```java
    int[] numbers = new int[5]; // 'int[]' est le type référence
    numbers[0] = 10;

    String[] names = {"Alice", "Bob", "Charlie"}; // 'String[]' est le type référence
    ```
* **Enums (Énumérations) :** Les enums représentent un ensemble fixe de constantes nommées.
    ```java
    enum Day {
        MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
    }

    public class Main {
        public static void main(String[] args) {
            Day today = Day.MONDAY; // 'Day' est le type référence
            System.out.println("Aujourd'hui est " + today);
        }
    }
    ```
* **Classes Wrapper :** Pour chaque type primitif, Java fournit une classe wrapper correspondante (par exemple, `Integer` pour `int`, `Double` pour `double`). Elles permettent de traiter les valeurs primitives comme des objets.
    ```java
    Integer num = 10; // 'Integer' est le type référence
    Double piValue = 3.14; // 'Double' est le type référence
    ```

**Points clés sur les types références :**

* Ils stockent des références (adresses mémoire) vers des objets dans le tas.
* Ils peuvent être `null`, ce qui signifie que la référence ne pointe vers aucun objet.
* Ils ont des méthodes et des champs associés (définis par leur classe ou interface).
* La valeur par défaut pour les champs de type référence non initialisés est `null`.

**3. Inférence de type avec `var` (Java 10 et versions ultérieures) :**

Java 10 a introduit le mot-clé `var`, qui permet l'inférence de type des variables locales. Au lieu de déclarer explicitement le type, le compilateur peut inférer le type en fonction de l'expression d'initialisation.

```java
var message = "Hello"; // Le compilateur infère que 'message' est de type String
var count = 100;      // Le compilateur infère que 'count' est de type int
var prices = new double[]{10.5, 20.3}; // Le compilateur infère que 'prices' est de type double[]
```

**Notes importantes sur `var` :**

* `var` ne peut être utilisé que pour les variables locales dans les méthodes, constructeurs ou initialiseurs.
* Vous devez fournir un initialiseur lors de l'utilisation de `var` car le compilateur en a besoin pour inférer le type.
* `var` ne change pas le typage statique de Java. Le type est toujours déterminé au moment de la compilation.

**4. Génériques :**

Les génériques permettent de paramétrer les types. Cela signifie que vous pouvez définir des classes, des interfaces et des méthodes qui peuvent fonctionner avec différents types tout en offrant une sécurité de type au moment de la compilation.

```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> names = new ArrayList<>(); // Liste de Strings
        names.add("Alice");
        names.add("Bob");

        // names.add(123); // Cela provoquerait une erreur de compilation

        List<Integer> numbers = new ArrayList<>(); // Liste d'Integers
        numbers.add(10);
        numbers.add(20);
    }
}
```

Ici, `<String>` et `<Integer>` sont des paramètres de type. Les génériques aident à prévenir les `ClassCastException` à l'exécution en appliquant les contraintes de type au moment de la compilation.

**5. Vérification de type :**

Java effectue la vérification de type à deux étapes principales :

* **Vérification de type à la compilation :** Le compilateur Java vérifie le code à la recherche d'erreurs de type avant son exécution. S'il y a des incompatibilités de type (par exemple, essayer d'assigner une `String` à une variable `int` sans cast explicite), le compilateur signalera une erreur et empêchera la compilation du programme.
* **Vérification de type à l'exécution :** Certaines vérifications de type sont effectuées pendant l'exécution du programme. Par exemple, lorsque vous castez un type référence vers un autre type, la JVM vérifie si l'objet est bien une instance du type cible. Si ce n'est pas le cas, une `ClassCastException` est levée.

**6. Conversion de type (Casting) :**

Parfois, vous devez convertir une valeur d'un type à un autre. Java prend en charge deux types de casting :

* **Casting Implicite (Conversion Élargissante) :** Cela se produit automatiquement lorsque vous assignez une valeur d'un type primitif plus petit à une variable d'un type primitif plus grand. Aucune perte de données ne se produit.
    ```java
    int myInt = 10;
    long myLong = myInt; // Casting implicite de int vers long
    double myDouble = myLong; // Casting implicite de long vers double
    ```
* **Casting Explicite (Conversion Rétrécissante) :** Cela doit être fait manuellement en utilisant un opérateur de cast `(targetType)` lorsque vous assignez une valeur d'un type primitif plus grand à une variable d'un type primitif plus petit. Une perte de données peut se produire.
    ```java
    double myDouble = 10.99;
    int myInt = (int) myDouble; // Casting explicite de double vers int (myInt vaudra 10)
    ```
* **Casting de Type Référence :** Vous pouvez également caster entre des types références, mais c'est plus complexe et implique l'héritage et les interfaces.
    * **Upcasting :** Caster un objet d'une sous-classe vers le type de sa superclasse. Ceci est toujours autorisé implicitement.
    * **Downcasting :** Caster un objet du type d'une superclasse vers le type de sa sous-classe. Cela nécessite un cast explicite et peut entraîner une `ClassCastException` à l'exécution si l'objet n'est pas réellement une instance de la sous-classe.

**Exemple de Casting de Type Référence :**

```java
class Animal {}
class Dog extends Animal {
    public void bark() {
        System.out.println("Woof !");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myAnimal = new Dog(); // Upcasting (implicite)

        // Dog myDog = myAnimal; // Erreur de compilation : Conversion implicite de Animal vers Dog impossible
        Dog myDog = (Dog) myAnimal; // Downcasting (explicite)
        myDog.bark(); // Cela fonctionnera

        Animal anotherAnimal = new Animal();
        // Dog anotherDog = (Dog) anotherAnimal; // Cela lèvera une ClassCastException à l'exécution
    }
}
```

**Conclusion :**

Comprendre le système de types de Java est crucial pour écrire un code correct et robuste. En connaissant la différence entre les types primitifs et les types références, le fonctionnement des génériques, et les règles de vérification et de conversion de type, vous pouvez éviter les erreurs de programmation courantes et créer des applications plus fiables.

Ce tutoriel fournit une compréhension fondamentale. En continuant à apprendre Java, vous rencontrerez des concepts plus avancés liés aux types, tels que l'héritage, le polymorphisme et des scénarios génériques plus complexes. Continuez à pratiquer et à expérimenter avec différents types pour solidifier votre compréhension !