---
audio: false
generated: true
lang: fr
layout: post
title: API de flux en Java
translated: true
---

Pour utiliser `java.util.stream` en Java, vous pouvez tirer parti de l'API Stream introduite dans Java 8 pour traiter des collections de données de manière fonctionnelle et déclarative. Les flux permettent d'effectuer des opérations telles que le filtrage, le mappage et la réduction sur des séquences d'éléments (comme des listes ou des tableaux) de manière efficace et concise. Ci-dessous, je vais expliquer comment utiliser `java.util.stream` en passant par un exemple spécifique : trouver la moyenne des nombres pairs supérieurs à 10 à partir d'une liste d'entiers. Cela démontrera les opérations et concepts clés des flux.

---

### **Aperçu de `java.util.stream`**
Le package `java.util.stream` fournit l'interface `Stream` et les classes associées (comme `IntStream`, `DoubleStream`, etc.) pour traiter les données. Un flux est une séquence d'éléments qui prend en charge les opérations exécutées dans un pipeline. Ces opérations sont :
- **Opérations intermédiaires** : Transforment ou filtrent le flux (par exemple, `filter`, `map`), en retournant un nouveau flux. Elles sont paresseuses et ne sont exécutées que lorsqu'une opération terminale est invoquée.
- **Opérations terminales** : Produisent un résultat ou un effet secondaire (par exemple, `average`, `collect`), déclenchant le pipeline pour traiter les données.

Pour utiliser les flux, vous faites généralement :
1. Créez un flux à partir d'une source de données (par exemple, une liste).
2. Appliquez des opérations intermédiaires pour transformer ou filtrer les données.
3. Utilisez une opération terminale pour produire un résultat.

---

### **Exemple de Problème**
Résolvons ce problème : étant donné une `List<Integer>`, calculez la moyenne de tous les nombres pairs supérieurs à 10. Si aucun nombre ne répond à ces critères, retournez 0.0. Voici comment le faire avec `java.util.stream`.

#### **Solution Étape par Étape**
1. **Créer un Flux**
   - Commencez avec une `List<Integer>` (par exemple, `List.of(1, 2, 12, 15, 20, 25, 30)`).
   - Utilisez la méthode `stream()` pour créer un `Stream<Integer>` :
     ```java
     list.stream()
     ```

2. **Filtrer le Flux**
   - Utilisez la méthode `filter` pour ne conserver que les nombres qui sont pairs et supérieurs à 10.
   - La méthode `filter` prend un `Predicate` (une fonction retournant un booléen) sous forme d'expression lambda :
     ```java
     .filter(number -> number % 2 == 0 && number > 10)
     ```
     - `number % 2 == 0` vérifie si un nombre est pair.
     - `number > 10` assure que le nombre est supérieur à 10.
     - Pour la liste d'exemple `[1, 2, 12, 15, 20, 25, 30]`, cela conserve `[12, 20, 30]`.

3. **Convertir en `IntStream`**
   - Puisque `average()` est disponible sur les flux primitifs comme `IntStream` (et non `Stream<Integer>`), convertissez le `Stream<Integer>` en `IntStream` en utilisant `mapToInt` :
     ```java
     .mapToInt(i -> i)
     ```
     - `i -> i` déballote chaque `Integer` en un `int`. Vous pourriez également utiliser `Integer::intValue`.
     - Cela donne un `IntStream` de `[12, 20, 30]`.

4. **Calculer la Moyenne**
   - Utilisez la méthode `average()` sur `IntStream`, qui retourne un `OptionalDouble` (puisque le flux pourrait être vide) :
     ```java
     .average()
     ```
     - Pour `[12, 20, 30]`, cela calcule `(12 + 20 + 30) / 3 = 20.666...`.
     - Si le flux est vide, il retourne un `OptionalDouble` vide.

5. **Gérer le Cas Vide**
   - Utilisez `orElse(0.0)` sur le `OptionalDouble` pour retourner 0.0 si aucun nombre ne satisfait le filtre :
     ```java
     .orElse(0.0)
     ```
     - Pour `[12, 20, 30]`, cela retourne `20.666...`.
     - Pour une liste comme `[1, 3, 5]` (aucun nombre pair > 10), cela retourne `0.0`.

#### **Code Complet**
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

### **Fonctionnalités Clés de `java.util.stream` Démontrées**
- **Chaînage** : Les opérations sont chaînées dans un style fluide (par exemple, `.filter().mapToInt().average()`).
- **Paresse** : Les opérations intermédiaires (comme `filter` et `mapToInt`) ne sont exécutées que lorsque l'opération terminale (`average`) est appelée.
- **Flux Primitifs** : `IntStream` fournit des méthodes comme `average()` adaptées aux opérations numériques, évitant les surcoûts de boîte.
- **Gestion des Optionnels** : `OptionalDouble` gère les cas où aucun résultat n'existe, avec `orElse` fournissant une valeur par défaut.

---

### **Approche Alternative**
Vous pouvez également utiliser la classe `Collectors` :
```java
import java.util.stream.Collectors;

double average = list.stream()
                     .filter(number -> number % 2 == 0 && number > 10)
                     .collect(Collectors.averagingInt(i -> i));
```
- Cela retourne un `Double` directement et retourne `0.0` pour un flux vide. Cependant, `mapToInt().average()` est plus direct pour ce cas simple et s'aligne avec l'utilisation des flux primitifs.

---

### **Quand Utiliser les Flux**
- Utilisez `java.util.stream` pour un code concis et lisible lors du traitement des collections.
- Pour de grands ensembles de données, envisagez d'utiliser `parallelStream()` au lieu de `stream()` pour tirer parti du parallélisme, bien que cela soit superflu pour les petites listes en raison des surcoûts.

---

Cet exemple montre comment utiliser `java.util.stream` pour résoudre un problème pratique. Vous pouvez adapter ces étapes—créer un flux, filtrer, mapper et réduire—to d'autres scénarios selon les besoins !