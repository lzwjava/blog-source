---
audio: false
generated: true
lang: fr
layout: post
title: API de flux en Java
translated: true
type: note
---

Pour utiliser `java.util.stream` en Java, vous pouvez exploiter l'API Stream introduite dans Java 8 pour traiter des collections de données de manière fonctionnelle et déclarative. Les streams permettent d'effectuer des opérations telles que le filtrage, le mapping et la réduction sur des séquences d'éléments (comme des listes ou des tableaux) de manière efficace et concise. Ci-dessous, je vais expliquer comment utiliser `java.util.stream` en parcourant un exemple spécifique : trouver la moyenne des nombres pairs supérieurs à 10 à partir d'une liste d'entiers. Cela démontrera les opérations et concepts clés des streams.

---

### **Aperçu de `java.util.stream`**
Le package `java.util.stream` fournit l'interface `Stream` et les classes associées (comme `IntStream`, `DoubleStream`, etc.) pour traiter les données. Un stream est une séquence d'éléments qui prend en charge des opérations exécutées dans un pipeline. Ces opérations sont :
- **Opérations intermédiaires** : Transforment ou filtrent le stream (par exemple, `filter`, `map`), renvoyant un nouveau stream. Elles sont paresseuses et ne sont exécutées que lorsqu'une opération terminale est invoquée.
- **Opérations terminales** : Produisent un résultat ou un effet secondaire (par exemple, `average`, `collect`), déclenchant le traitement des données par le pipeline.

Pour utiliser les streams, vous devez généralement :
1. Créer un stream à partir d'une source de données (par exemple, une liste).
2. Appliquer des opérations intermédiaires pour transformer ou filtrer les données.
3. Utiliser une opération terminale pour produire un résultat.

---

### **Exemple de problème**
Résolvons ce problème : Étant donné une `List<Integer>`, calculez la moyenne de tous les nombres pairs supérieurs à 10. Si aucun tel nombre n'existe, retournez 0.0. Voici comment le faire en utilisant `java.util.stream`.

#### **Solution étape par étape**
1. **Créer un Stream**
   - Commencez avec une `List<Integer>` (par exemple, `List.of(1, 2, 12, 15, 20, 25, 30)`).
   - Utilisez la méthode `stream()` pour créer un `Stream<Integer>` :
     ```java
     list.stream()
     ```

2. **Filtrer le Stream**
   - Utilisez la méthode `filter` pour ne conserver que les nombres pairs et supérieurs à 10.
   - La méthode `filter` prend un `Predicate` (une fonction renvoyant un booléen) comme expression lambda :
     ```java
     .filter(number -> number % 2 == 0 && number > 10)
     ```
     - `number % 2 == 0` vérifie si un nombre est pair.
     - `number > 10` garantit que le nombre est supérieur à 10.
     - Pour la liste exemple `[1, 2, 12, 15, 20, 25, 30]`, cela conserve `[12, 20, 30]`.

3. **Convertir en `IntStream`**
   - Puisque `average()` est disponible sur les streams primitifs comme `IntStream` (et non sur `Stream<Integer>`), convertissez le `Stream<Integer>` en `IntStream` en utilisant `mapToInt` :
     ```java
     .mapToInt(i -> i)
     ```
     - `i -> i` déboxe chaque `Integer` en `int`. Alternativement, vous pourriez utiliser `Integer::intValue`.
     - Cela donne un `IntStream` de `[12, 20, 30]`.

4. **Calculer la moyenne**
   - Utilisez la méthode `average()` sur `IntStream`, qui renvoie un `OptionalDouble` (car le stream pourrait être vide) :
     ```java
     .average()
     ```
     - Pour `[12, 20, 30]`, cela calcule `(12 + 20 + 30) / 3 = 20.666...`.
     - Si le stream est vide, il renvoie un `OptionalDouble` vide.

5. **Gérer le cas vide**
   - Utilisez `orElse(0.0)` sur le `OptionalDouble` pour renvoyer 0.0 si aucun nombre ne satisfait le filtre :
     ```java
     .orElse(0.0)
     ```
     - Pour `[12, 20, 30]`, cela renvoie `20.666...`.
     - Pour une liste comme `[1, 3, 5]` (aucun nombre pair > 10), cela renvoie `0.0`.

#### **Code complet**
Voici la solution complète sous forme de méthode :
```java
import java.util.List;

public class Main {
    public static double averageOfEvenGreaterThanTen(List<Integer> list) {
        return list.stream()
                   .filter(number -> number % 2 == 0 && number > 10)
                   .mapToInt(i -> i)
                   .average()
                   .orElse(0.0);
    }

    public static void main(String[] args) {
        // Cas de test
        System.out.println(averageOfEvenGreaterThanTen(List.of(1, 2, 12, 15, 20, 25, 30)));  // ~20.666
        System.out.println(averageOfEvenGreaterThanTen(List.of(1, 3, 5)));                    // 0.0
        System.out.println(averageOfEvenGreaterThanTen(List.of(12)));                         // 12.0
        System.out.println(averageOfEvenGreaterThanTen(List.of()));                           // 0.0
        System.out.println(averageOfEvenGreaterThanTen(List.of(10, 8, 6)));                   // 0.0
        System.out.println(averageOfEvenGreaterThanTen(List.of(11, 13, 14, 16)));             // 15.0
    }
}
```

---

### **Fonctionnalités clés de `java.util.stream` démontrées**
- **Chaînage** : Les opérations sont chaînées dans un style fluide (par exemple, `.filter().mapToInt().average()`).
- **Paresse** : Les opérations intermédiaires (comme `filter` et `mapToInt`) ne sont exécutées que lorsque l'opération terminale (`average`) est appelée.
- **Streams primitifs** : `IntStream` fournit des méthodes comme `average()` adaptées aux opérations numériques, évitant les surcoûts de boxing.
- **Gestion des Optional** : `OptionalDouble` gère les cas où aucun résultat n'existe, avec `orElse` fournissant une valeur par défaut.

---

### **Approche alternative**
Vous pourriez également utiliser la classe `Collectors` :
```java
import java.util.stream.Collectors;

double average = list.stream()
                     .filter(number -> number % 2 == 0 && number > 10)
                     .collect(Collectors.averagingInt(i -> i));
```
- Cela renvoie un `Double` directement et renvoie `0.0` pour un stream vide. Cependant, `mapToInt().average()` est plus direct pour ce cas simple et correspond à l'utilisation des streams primitifs.

---

### **Quand utiliser les Streams**
- Utilisez `java.util.stream` pour un code concis et lisible lors du traitement de collections.
- Pour de grands ensembles de données, envisagez `parallelStream()` au lieu de `stream()` pour tirer parti du parallélisme, bien que ce soit excessif pour les petites listes en raison de la surcharge.

---

Cet exemple montre comment utiliser `java.util.stream` pour résoudre un problème pratique. Vous pouvez adapter ces étapes — création d'un stream, filtrage, mapping et réduction — à d'autres scénarios selon les besoins !