---
audio: false
generated: true
lang: de
layout: post
title: Suchalgorithmen in Java
translated: true
type: note
---

Die Suche dreht sich darum, Daten effizient zu finden. Lassen Sie uns die binäre Suche und die lineare Suche untersuchen.

## 1. Binäre Suche: Logarithmische Effizienz
Die binäre Suche funktioniert auf sortierten Arrays, halbiert den Suchraum in jedem Schritt und hat eine O(log n) Zeitkomplexität.

### Java-Implementierung
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
**Ausgabe:** `Found at: 3`

## 2. Lineare Suche: Einfache Basis
Die lineare Suche überprüft jedes Element sequenziell, mit einer O(n) Zeitkomplexität – nützlich für unsortierte Daten.

### Java-Implementierung
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
**Ausgabe:** `Found at: 3`