---
audio: false
generated: true
lang: hant
layout: post
title: Java 字串演算法
translated: true
type: note
---

字串無處不在，高效的字符串處理是關鍵技能。讓我們來看看 KMP 演算法、字典樹資料結構以及用於模式匹配的 Rabin-Karp 演算法。

## 1. KMP 演算法：高效字串匹配
Knuth-Morris-Pratt (KMP) 演算法通過預處理模式來避免不必要的比較，實現 O(n + m) 的時間複雜度。

### Java 實作
```java
public class KMP {
    static void KMPSearch(String pat, String txt) {
        int M = pat.length(), N = txt.length();
        int[] lps = new int[M];
        computeLPSArray(pat, M, lps);
        int i = 0, j = 0;
        while (i < N) {
            if (pat.charAt(j) == txt.charAt(i)) { i++; j++; }
            if (j == M) {
                System.out.println("Found at " + (i - j));
                j = lps[j - 1];
            } else if (i < N && pat.charAt(j) != txt.charAt(i)) {
                if (j != 0) j = lps[j - 1];
                else i++;
            }
        }
    }

    static void computeLPSArray(String pat, int M, int[] lps) {
        int len = 0, i = 1;
        lps[0] = 0;
        while (i < M) {
            if (pat.charAt(i) == pat.charAt(len)) lps[i++] = ++len;
            else if (len != 0) len = lps[len - 1];
            else lps[i++] = 0;
        }
    }

    public static void main(String[] args) {
        String txt = "ABABDABACDABABCABAB";
        String pat = "ABABCABAB";
        KMPSearch(pat, txt);
    }
}
```
**輸出：** `Found at 10`

## 2. 字典樹：基於前綴的搜尋
字典樹將字串儲存在樹結構中，實現快速前綴查找，空間複雜度與總字符數成正比。

### Java 實作
```java
public class Trie {
    static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEndOfWord;
    }

    TrieNode root = new TrieNode();

    void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) node.children[index] = new TrieNode();
            node = node.children[index];
        }
        node.isEndOfWord = true;
    }

    boolean search(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) return false;
            node = node.children[index];
        }
        return node.isEndOfWord;
    }

    public static void main(String[] args) {
        Trie trie = new Trie();
        trie.insert("apple");
        System.out.println("Apple: " + trie.search("apple"));
        System.out.println("App: " + trie.search("app"));
    }
}
```
**輸出：**
```
Apple: true
App: false
```

## 3. Rabin-Karp：基於雜湊的匹配
Rabin-Karp 使用雜湊技術來尋找模式，平均時間複雜度為 O(n + m)，最壞情況下為 O(nm)。

### Java 實作
```java
public class RabinKarp {
    public static void search(String pat, String txt, int q) {
        int d = 256, M = pat.length(), N = txt.length(), p = 0, t = 0, h = 1;
        for (int i = 0; i < M - 1; i++) h = (h * d) % q;
        for (int i = 0; i < M; i++) {
            p = (d * p + pat.charAt(i)) % q;
            t = (d * t + txt.charAt(i)) % q;
        }
        for (int i = 0; i <= N - M; i++) {
            if (p == t) {
                boolean match = true;
                for (int j = 0; j < M; j++) {
                    if (pat.charAt(j) != txt.charAt(i + j)) { match = false; break; }
                }
                if (match) System.out.println("Found at " + i);
            }
            if (i < N - M) {
                t = (d * (t - txt.charAt(i) * h) + txt.charAt(i + M)) % q;
                if (t < 0) t += q;
            }
        }
    }

    public static void main(String[] args) {
        String txt = "GEEKSFORGEEKS";
        String pat = "GEEKS";
        int q = 101; // 質數
        search(pat, txt, q);
    }
}
```
**輸出：**
```
Found at 0
Found at 8
```