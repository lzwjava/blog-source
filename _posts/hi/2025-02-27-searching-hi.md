---
audio: false
generated: true
lang: hi
layout: post
title: जावा में खोज एल्गोरिदम
translated: true
type: note
---

खोज डेटा को कुशलतापूर्वक ढूंढने के बारे में है। आइए बाइनरी सर्च और लीनियर सर्च को समझते हैं।

## 1. बाइनरी सर्च: लॉगरिदमिक दक्षता
बाइनरी सर्च सॉर्ट किए गए ऐरे पर काम करती है, प्रत्येक चरण में खोज स्थान को आधा करते हुए, O(log n) समय के साथ।

### Java इम्प्लीमेंटेशन
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

## 2. लीनियर सर्च: सरल आधार
लीनियर सर्च प्रत्येक एलिमेंट को क्रमिक रूप से चेक करती है, O(n) समय के साथ—यह अनसॉर्टेड डेटा के लिए उपयोगी है।

### Java इम्प्लीमेंटेशन
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