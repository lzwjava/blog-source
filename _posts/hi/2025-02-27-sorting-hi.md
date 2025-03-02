---
audio: false
generated: false
lang: hi
layout: post
title: Java में Sorting Algorithms
translated: true
---

सॉर्टिंग प्रोग्रामिंग में एक मूलभूत ऑपरेशन है, और जावा अपने विभिन्न सॉर्टिंग एल्गोरिथम्स को लागू करने के लिए अपने लचीलापन के लिए चमकता है। चलीए क्विकसॉर्ट, मर्ज सॉर्ट और बबल सॉर्ट—तीन लोकप्रिय सॉर्टिंग तकनीकों को खोजें, जिनके अलग-अलग विशेषताएं हैं।

## 1. क्विकसॉर्ट: विभाजन और विजय
क्विकसॉर्ट एक पिवॉट चुनता है, एर्रे को विभाजित करता है, और पुनरावर्ती रूप से सबएर्रे को सॉर्ट करता है। यह औसत समय जटिलता के साथ O(n log n) में दक्ष है।

### जावा इम्प्लीमेंटेशन
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
**आउटपुट:** `Sorted: [1, 5, 7, 8, 9, 10]`

## 2. मर्ज सॉर्ट: स्थिर सॉर्टिंग
मर्ज सॉर्ट एर्रे को विभाजित करता है, आधे को सॉर्ट करता है, और उन्हें वापस मिलाता है। यह स्थिर है और O(n log n) समय की गारंटी देता है।

### जावा इम्प्लीमेंटेशन
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
**आउटपुट:** `Sorted: [5, 6, 7, 11, 12, 13]`

## 3. बबल सॉर्ट: सरल लेकिन धीमा
बबल सॉर्ट बार-बार पिछले तत्वों को बदल देता है अगर वे अनुक्रम में नहीं हैं। यह O(n²) है लेकिन समझने में आसान है।

### जावा इम्प्लीमेंटेशन
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
**आउटपुट:** `Sorted: [11, 12, 22, 25, 34, 64, 90]`