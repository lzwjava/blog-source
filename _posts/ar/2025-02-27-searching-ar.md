---
audio: false
generated: true
lang: ar
layout: post
title: خوارزميات البحث في جافا
translated: true
type: note
---

البحث يتعلق بإيجاد البيانات بكفاءة. دعنا نستكشف البحث الثنائي والبحث الخطي.

## 1. البحث الثنائي: كفاءة لوغاريتمية
يعمل البحث الثنائي على المصفوفات المرتبة، مما يقلل مساحة البحث إلى النصف في كل خطوة، مع تعقيد زمني O(log n).

### التنفيذ بلغة Java
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
**الناتج:** `Found at: 3`

## 2. البحث الخطي: الأساس البسيط
يفحص البحث الخطي كل عنصر بالتسلسل، مع تعقيد زمني O(n) — مفيد للبيانات غير المرتبة.

### التنفيذ بلغة Java
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
**الناتج:** `Found at: 3`