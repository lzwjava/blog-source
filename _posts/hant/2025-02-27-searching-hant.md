---
audio: false
generated: true
lang: hant
layout: post
title: Java 搜尋演算法
translated: true
type: note
---

搜尋是關於高效地尋找數據。讓我們來探索二分搜尋和線性搜尋。

## 1. 二分搜尋：對數效率
二分搜尋適用於已排序的陣列，每一步將搜尋空間減半，時間複雜度為 O(log n)。

### Java 實作
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
**輸出：** `Found at: 3`

## 2. 線性搜尋：簡單基準
線性搜尋按順序檢查每個元素，時間複雜度為 O(n)——適用於未排序的數據。

### Java 實作
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
**輸出：** `Found at: 3`