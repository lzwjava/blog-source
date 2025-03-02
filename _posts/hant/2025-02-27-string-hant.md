---
audio: true
generated: false
lang: hant
layout: post
title: 字串演算法
translated: true
---

字串無處不在，而高效的字串操作是一項關鍵技能。讓我們來看看 KMP 演算法、字典樹資料結構和 Rabin-Karp 進行模式匹配。

## 1. KMP 演算法：高效字串匹配
Knuth-Morris-Pratt (KMP) 演算法預處理模式以避免不必要的比較，達到 O(n + m) 時間。

### Java 實現
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
**輸出:** `Found at 10`

## 2. 字典樹：前綴查找
字典樹以樹狀結構儲存字串，進行快速前綴查找，空間複雜度與總字符數成正比。

### Java 實現
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
**輸出:**
```
Apple: true
App: false
```

## 3. Rabin-Karp：基於哈希的匹配
Rabin-Karp 使用哈希來查找模式，平均時間為 O(n + m)，但最壞情況為 O(nm)。

### Java 實現
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
        int q = 101; // 素數
        search(pat, txt, q);
    }
}
```
**輸出:**
```
Found at 0
Found at 8
```