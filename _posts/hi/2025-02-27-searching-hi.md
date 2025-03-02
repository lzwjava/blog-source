---
audio: false
generated: true
lang: hi
layout: post
title: खोज एल्गोरिथम्स इन जावा
translated: true
---

खोजने का मतलब है कि डेटा को दक्षता से ढूंढना। हम बाइनरी सर्च और लिनियर सर्च की खोज करें।

## 1. बाइनरी सर्च: लॉगारिथ्मिक दक्षता
बाइनरी सर्च सॉर्टेड एरेज पर काम करता है, हर कदम में खोज क्षेत्र को आधा कर देता है, O(log n) समय के साथ।

### जावा इम्प्लिमेंटेशन
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
**आउटपुट:** `Found at: 3`

## 2. लिनियर सर्च: सरल बेसलाइन
लिनियर सर्च हर तत्व को क्रमिक रूप से चेक करता है, O(n) समय के साथ—असॉर्टेड डेटा के लिए उपयोगी।

### जावा इम्प्लिमेंटेशन
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
**आउटपुट:** `Found at: 3`