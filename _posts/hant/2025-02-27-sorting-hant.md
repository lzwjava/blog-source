---
audio: false
generated: true
lang: hant
layout: post
title: Java 排序算法
translated: true
type: note
---

排序是程式設計中的基礎操作，而 Java 在實現各種排序演算法方面展現出其靈活性。讓我們探討快速排序、合併排序和氣泡排序——這三種具有不同特性的常用排序技術。

## 1. 快速排序：分治法
快速排序選擇一個基準點，分割陣列，並遞迴排序子陣列。其效率高，平均時間複雜度為 O(n log n)。

### Java 實現
```java
public class QuickSort {
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        return i + 1;
    }

    public static void main(String[] args) {
        int[] arr = {10, 7, 8, 9, 1, 5};
        quickSort(arr, 0, arr.length - 1);
        System.out.println("Sorted: " + java.util.Arrays.toString(arr));
    }
}
```
**輸出：** `Sorted: [1, 5, 7, 8, 9, 10]`

## 2. 合併排序：穩定排序
合併排序將陣列分割，排序兩半，然後合併回去。它是穩定的，並保證 O(n log n) 的時間複雜度。

### Java 實現
```java
public class MergeSort {
    public static void mergeSort(int[] arr, int l, int r) {
        if (l < r) {
            int m = (l + r) / 2;
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    private static void merge(int[] arr, int l, int m, int r) {
        int n1 = m - l + 1, n2 = r - m;
        int[] L = new int[n1], R = new int[n2];
        for (int i = 0; i < n1; i++) L[i] = arr[l + i];
        for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2) arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6, 7};
        mergeSort(arr, 0, arr.length - 1);
        System.out.println("Sorted: " + java.util.Arrays.toString(arr));
    }
}
```
**輸出：** `Sorted: [5, 6, 7, 11, 12, 13]`

## 3. 氣泡排序：簡單但緩慢
氣泡排序重複交換相鄰元素（如果它們順序錯誤）。其時間複雜度為 O(n²)，但易於理解。

### Java 實現
```java
public class BubbleSort {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        bubbleSort(arr);
        System.out.println("Sorted: " + java.util.Arrays.toString(arr));
    }
}
```
**輸出：** `Sorted: [11, 12, 22, 25, 34, 64, 90]`