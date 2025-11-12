---
audio: false
generated: true
lang: ja
layout: post
title: Javaにおける検索アルゴリズム
translated: true
type: note
---

検索はデータを効率的に見つけることです。バイナリサーチとリニアサーチについて見ていきましょう。

## 1. バイナリサーチ：対数的効率
バイナリサーチはソート済み配列で動作し、各ステップで探索空間を半分に削減し、O(log n)の時間計算量です。

### Java実装
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
**出力:** `Found at: 3`

## 2. リニアサーチ：シンプルな基本
リニアサーチはすべての要素を順番にチェックし、O(n)の時間計算量です。ソートされていないデータに有効です。

### Java実装
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
**出力:** `Found at: 3`