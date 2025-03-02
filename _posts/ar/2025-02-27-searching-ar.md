---
audio: false
generated: false
lang: ar
layout: post
title: خوارزميات البحث في جافا
translated: true
---

البحث عن البيانات هو عن العثور عليها بشكل فعال. دعونا نستكشف البحث الثنائي والبحث الخطي.

## 1. البحث الثنائي: كفاءة لوغاريتمية
يعمل البحث الثنائي على المصفوفات المصفوفة، ويقلل من مساحة البحث إلى النصف في كل خطوة، مع وقت O(log n).

### تنفيذ Java
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
**Output:** `Found at: 3`

## 2. البحث الخطي: قاعدة بسيطة
يبحث البحث الخطي عن كل عنصر تسلسليا، مع وقت O(n)— مفيد للبيانات غير المصفوفة.

### تنفيذ Java
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
**Output:** `Found at: 3`