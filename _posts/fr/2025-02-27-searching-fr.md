---
audio: false
generated: true
lang: fr
layout: post
title: Algorithmes de recherche en Java
translated: true
type: note
---

La recherche consiste à trouver des données efficacement. Explorons la recherche binaire et la recherche linéaire.

## 1. Recherche Binaire : Efficacité Logarithmique
La recherche binaire fonctionne sur des tableaux triés, réduisant l'espace de recherche de moitié à chaque étape, avec un temps O(log n).

### Implémentation Java
```java
public class BinarySearch {
    public static int binarySearch(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) return mid;
            if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {2, 3, 4, 10, 40, 50};
        int target = 10;
        System.out.println("Found at: " + binarySearch(arr, target));
    }
}
```
**Sortie :** `Found at: 3`

## 2. Recherche Linéaire : Base de Référence Simple
La recherche linéaire vérifie chaque élément séquentiellement, avec un temps O(n) — utile pour les données non triées.

### Implémentation Java
```java
public class LinearSearch {
    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {10, 20, 80, 30, 60, 50, 110};
        int target = 30;
        System.out.println("Found at: " + linearSearch(arr, target));
    }
}
```
**Sortie :** `Found at: 3`