---
audio: false
generated: true
lang: fr
layout: post
title: LinkedHashMap contre TreeMap
translated: true
type: note
---

Excellente question ! `LinkedHashMap` et `TreeMap` sont toutes deux des implémentations de l'interface `Map` en Java, mais elles ont **des stratégies d'ordonnancement différentes** et utilisent **des structures de données sous-jacentes différentes**.

### 🌳 `TreeMap`
- **Ordonnancement** : Trié selon **l'ordre naturel** des clés (ou par un `Comparator` personnalisé si fourni).
- **Structure de données** : Repose sur un **Arbre Rouge-Noir** (un type d'arbre binaire de recherche auto-équilibré).
- **Performances** :
  - `O(log n)` pour get/put/remove
  - L'ordre trié est maintenu en permanence
- **Cas d'utilisation** : Lorsque vous avez besoin que **les clés soient triées**.

### 🔗 `LinkedHashMap`
- **Ordonnancement** : Maintient **l'ordre d'insertion** (ou l'ordre d'accès si configuré ainsi).
- **Structure de données** : Repose sur une **table de hachage + une liste chaînée**.
- **Performances** :
  - `O(1)` pour get/put/remove (comme `HashMap`)
  - Légèrement plus gourmande en mémoire à cause de la liste chaînée
- **Cas d'utilisation** : Lorsque l'**ordre dans lequel les entrées ont été ajoutées** est important.

---

### ✅ Ordre de l'Itérateur
Oui, **l'ordre de leur itérateur sera différent** :

| Type de Map    | Ordre de l'Itérateur               |
|----------------|------------------------------------|
| `TreeMap`      | Trié par les clés                  |
| `LinkedHashMap`| Ordre d'insertion (ou ordre d'accès) |

---

### 🔍 Exemple

```java
Map<String, Integer> treeMap = new TreeMap<>();
Map<String, Integer> linkedMap = new LinkedHashMap<>();

treeMap.put("banana", 2);
treeMap.put("apple", 3);
treeMap.put("cherry", 1);

linkedMap.put("banana", 2);
linkedMap.put("apple", 3);
linkedMap.put("cherry", 1);

System.out.println("TreeMap:");
for (String key : treeMap.keySet()) {
    System.out.println(key);
}

System.out.println("LinkedHashMap:");
for (String key : linkedMap.keySet()) {
    System.out.println(key);
}
```

**Sortie :**
```
TreeMap:
apple
banana
cherry

LinkedHashMap:
banana
apple
cherry
```

N'hésitez pas si vous souhaitez une analyse plus détaillée des performances ou de l'utilisation de la mémoire.