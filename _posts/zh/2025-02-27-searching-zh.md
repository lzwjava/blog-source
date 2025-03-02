---
audio: false
generated: true
lang: zh
layout: post
title: 搜索算法在Java中
translated: true
---

搜索是关于高效地找到数据。让我们探索二分搜索和线性搜索。

## 1. 二分搜索：对数时间复杂度
二分搜索适用于排序数组，每一步将搜索空间减半，时间复杂度为 O(log n)。

### Java 实现
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
**输出:** `Found at: 3`

## 2. 线性搜索：简单基准
线性搜索顺序检查每个元素，时间复杂度为 O(n)—适用于未排序数据。

### Java 实现
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
**输出:** `Found at: 3`