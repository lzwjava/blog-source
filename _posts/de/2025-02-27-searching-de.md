---
audio: false
generated: false
lang: de
layout: post
title: Suchalgorithmen in Java
translated: true
---

Suchen bedeutet, Daten effizient zu finden. Lassen Sie uns die binäre Suche und die lineare Suche erkunden.

## 1. Binäre Suche: Logarithmische Effizienz
Die binäre Suche funktioniert mit sortierten Arrays und reduziert den Suchraum bei jedem Schritt um die Hälfte, mit einer Zeitkomplexität von O(log n).

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
        System.out.println("Gefunden bei: " + binarySearch(arr, target));
    }
}
```
**Ausgabe:** `Gefunden bei: 3`

## 2. Lineare Suche: Einfacher Standard
Die lineare Suche überprüft jedes Element der Reihe nach, mit einer Zeitkomplexität von O(n)—nützlich für unsortierte Daten.

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
        System.out.println("Gefunden bei: " + linearSearch(arr, target));
    }
}
```
**Ausgabe:** `Gefunden bei: 3`