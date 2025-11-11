---
audio: false
generated: true
lang: hi
layout: post
title: जावा में सॉर्टिंग एल्गोरिदम
translated: true
type: note
---

सॉर्टिंग प्रोग्रामिंग में एक मौलिक ऑपरेशन है, और Java विभिन्न सॉर्टिंग एल्गोरिदम को लागू करने के लिए अपनी लचीलापन के साथ चमकती है। आइए क्विकसॉर्ट, मर्ज सॉर्ट और बबल सॉर्ट का पता लगाएं—तीन लोकप्रिय सॉर्टिंग तकनीकें जिनकी अलग-अलग विशेषताएं हैं।

## 1. क्विकसॉर्ट: डिवाइड एंड कॉन्कर
क्विकसॉर्ट एक पिवोट चुनता है, ऐरे को पार्टिशन करता है, और सबअरे को पुनरावर्ती रूप से सॉर्ट करता है। यह O(n log n) की औसत समय जटिलता के साथ कुशल है।

### Java इम्प्लीमेंटेशन
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

## 2. मर्ज सॉर्ट: स्टेबल सॉर्टिंग
मर्ज सॉर्ट ऐरे को विभाजित करता है, आधे हिस्सों को सॉर्ट करता है, और उन्हें वापस मर्ज करता है। यह स्थिर है और O(n log n) समय की गारंटी देता है।

### Java इम्प्लीमेंटेशन
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
बबल सॉर्ट लगातार आसन्न एलिमेंट्स को स्वैप करता है यदि वे क्रम से बाहर हैं। यह O(n²) है लेकिन समझने में आसान है।

### Java इम्प्लीमेंटेशन
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