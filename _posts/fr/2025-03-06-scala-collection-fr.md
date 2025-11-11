---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser la bibliothèque de collections de Scala en Java
translated: true
type: note
---

Pour utiliser le package `scala.collection` en Java, vous pouvez tirer parti de l'interopérabilité entre Scala et Java, car les deux langages sont compilés en bytecode JVM. Cela permet au code Java d'appeler des classes Scala, y compris celles du package `scala.collection`, à condition que la bibliothèque Scala soit accessible à votre projet Java. Voici un guide étape par étape pour y parvenir, complet avec des explications et des exemples.

---

### **Étape 1 : Inclure la bibliothèque Scala dans votre projet Java**
Étant donné que le package `scala.collection` fait partie de la bibliothèque standard de Scala, vous devez inclure la bibliothèque Scala dans le classpath de votre projet Java. Cela peut être fait en ajoutant la dépendance de la bibliothèque Scala à votre outil de build :

- **Maven** :
  Ajoutez ce qui suit à votre `pom.xml` :
  ```xml
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-library</artifactId>
      <version>2.13.12</version> <!-- Utilisez la version qui correspond à vos besoins -->
  </dependency>
  ```

- **Gradle** :
  Ajoutez ceci à votre `build.gradle` :
  ```gradle
  implementation 'org.scala-lang:scala-library:2.13.12'
  ```

Cela garantit que les classes Scala, y compris celles de `scala.collection`, sont disponibles pour votre code Java.

---

### **Étape 2 : Importer les classes de collection Scala**
Une fois la bibliothèque Scala dans votre classpath, vous pouvez importer des classes spécifiques du package `scala.collection` dans votre code Java. Par exemple, pour utiliser la `List` immuable de Scala, vous importeriez :

```java
import scala.collection.immutable.List;
```

D'autres collections couramment utilisées incluent :
- `scala.collection.immutable.Set`
- `scala.collection.immutable.Map`
- `scala.collection.mutable.Buffer`

Notez que les collections Scala existent en variantes muables et immuables, contrairement aux collections Java, qui sont généralement mutables sauf si elles sont encapsulées (par exemple, via `Collections.unmodifiableList`).

---

### **Étape 3 : Créer des collections Scala en Java**
Les collections Scala sont généralement créées à l'aide d'objets compagnons, qui fournissent des méthodes factory comme `apply`. Cependant, comme Java ne prend pas directement en charge la syntaxe Scala (par exemple, `List(1, 2, 3)`), vous devez travailler explicitement avec ces méthodes. De plus, la méthode `apply` de Scala pour des collections comme `List` attend un `Seq` comme argument lorsqu'elle est appelée depuis Java, en raison de la façon dont les varargs de Scala sont compilés.

Pour faire le pont entre les collections Java et Scala, utilisez les utilitaires de conversion fournis par Scala, tels que `scala.collection.JavaConverters` (pour Scala 2.12 et antérieur) ou `scala.jdk.CollectionConverters` (pour Scala 2.13 et ultérieur). Voici comment créer une `List` Scala à partir d'une `List` Java :

#### **Exemple : Création d'une Liste Scala**
```java
import scala.collection.immutable.List;
import scala.collection.Seq;
import scala.jdk.CollectionConverters;
import java.util.Arrays;

public class ScalaCollectionExample {
    public static void main(String[] args) {
        // Créer une List Java
        java.util.List<Integer> javaList = Arrays.asList(1, 2, 3);

        // Convertir la List Java en Seq Scala
        Seq<Integer> scalaSeq = CollectionConverters.asScala(javaList);

        // Créer une List Scala en utilisant l'objet compagnon
        List<Integer> scalaList = List$.MODULE$.apply(scalaSeq);

        // Afficher la List Scala
        System.out.println(scalaList); // Sortie : List(1, 2, 3)
    }
}
```

- **`CollectionConverters.asScala`** : Convertit une `List` Java en `Seq` Scala (spécifiquement un `mutable.Buffer` dans Scala 2.13, qui est un sous-type de `Seq`).
- **`List$.MODULE$`** : Accède à l'instance singleton de l'objet compagnon `List` en Scala, vous permettant d'appeler sa méthode `apply`.
- **`apply(scalaSeq)`** : Crée une nouvelle `List` Scala immuable à partir du `Seq`.

---

### **Étape 4 : Utiliser les collections Scala**
Une fois que vous avez une collection Scala en Java, vous pouvez utiliser ses méthodes. Cependant, soyez conscient des différences entre Scala et Java :
- **Immuabilité** : De nombreuses collections Scala (par exemple, `scala.collection.immutable.List`) sont immuables, ce qui signifie que les méthodes renvoient de nouvelles collections plutôt que de modifier l'originale.
- **Effacement de type** : Scala et Java utilisent tous deux l'effacement de type, vous devrez donc peut-être caster les résultats lors de la récupération d'éléments.
- **Méthodes fonctionnelles** : Les collections Scala prennent en charge les opérations fonctionnelles comme `map`, `filter`, etc., que vous pouvez utiliser avec les lambdas Java 8+.

#### **Exemple : Accéder aux éléments**
```java
// Obtenir le premier élément
Integer head = (Integer) scalaList.head();
System.out.println("Head: " + head); // Sortie : Head: 1

// Obtenir la queue (tout sauf la tête)
List<Integer> tail = scalaList.tail();
System.out.println("Tail: " + tail); // Sortie : Tail: List(2, 3)
```

#### **Exemple : Appliquer une fonction map sur une Liste Scala**
Utilisation d'une lambda pour doubler chaque élément :
```java
import scala.Function1;

Function1<Integer, Integer> doubler = x -> x * 2;
List<Integer> doubledList = scalaList.map(doubler);
System.out.println("Doubled: " + doubledList); // Sortie : Doubled: List(2, 4, 6)
```

Ici, `Function1` est une interface Scala représentant une fonction avec un argument, qui correspond à la syntaxe lambda de Java.

---

### **Considérations clés**
- **Sécurité de type** : Les collections Scala sont paramétrées, mais les types de retour des méthodes peuvent apparaître comme `Object` en Java en raison de l'effacement de type. Castez si nécessaire (par exemple, `(Integer) scalaList.head()`).
- **Performance** : Franchir la frontière Java-Scala introduit une certaine surcharge, bien qu'elle soit généralement mineure.
- **Changement de paradigme** : Les collections Scala mettent l'accent sur l'immuabilité et la programmation fonctionnelle, ce qui peut différer du style impératif de Java. Par exemple, vous ne pouvez pas "ajouter" à une `List` immuable — vous en créez une nouvelle à la place (par exemple, en utilisant `:+` pour ajouter en fin, ce qui renvoie une nouvelle `List`).
- **Compatibilité des versions** : Assurez-vous que la version de la bibliothèque Scala correspond à vos besoins. Pour Scala 2.13+, utilisez `scala.jdk.CollectionConverters` ; pour 2.12 ou antérieur, utilisez `scala.collection.JavaConverters`.

---

### **Résumé**
Vous pouvez utiliser le package `scala.collection` en Java en :
1. Ajoutant la bibliothèque Scala au classpath de votre projet (par exemple, via Maven ou Gradle).
2. Important les classes de collection Scala souhaitées (par exemple, `scala.collection.immutable.List`).
3. Créant des collections Scala à l'aide d'objets compagnons (par exemple, `List$.MODULE$.apply`) et en convertissant les collections Java en `Seq` Scala avec `CollectionConverters`.
4. Manipulant les collections avec les méthodes Scala, en utilisant des casts et des lambdas si nécessaire.

Cette approche vous permet de tirer parti de la puissante bibliothèque de collections de Scala en Java, telle que ses structures de données immuables ou ses opérations fonctionnelles, tout en travaillant dans l'écosystème Java.