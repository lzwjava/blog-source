---
audio: false
generated: true
lang: hant
layout: post
title: LinkedHashMap 與 TreeMap 之比較
translated: true
type: note
---

很好的問題！`LinkedHashMap` 和 `TreeMap` 都是 Java 中 `Map` 介面的實現，但它們具有**不同的排序策略**且使用**不同的底層資料結構**。

### 🌳 `TreeMap`
- **排序方式**：按照鍵的**自然順序**排序（或透過自訂的 `Comparator` 來指定）。
- **資料結構**：基於**紅黑樹**（一種自平衡二元搜尋樹）。
- **效能表現**：
  - 讀取/寫入/刪除操作的時間複雜度為 `O(log n)`
  - 隨時保持排序狀態
- **使用情境**：當你需要**按鍵排序**時使用。

### 🔗 `LinkedHashMap`
- **排序方式**：保持**插入順序**（或可設定為存取順序）。
- **資料結構**：基於**雜湊表 + 鏈結串列**。
- **效能表現**：
  - 讀取/寫入/刪除操作的時間複雜度為 `O(1)`（與 `HashMap` 相同）
  - 因鏈結串列而略有記憶體開銷
- **使用情境**：當你關心**條目加入的順序**時使用。

---

### ✅ 迭代器順序
是的，它們的**迭代器順序會不同**：

| Map 類型       | 迭代器順序                     |
|----------------|------------------------------------|
| `TreeMap`      | 按鍵排序                     |
| `LinkedHashMap`| 插入順序（或存取順序）  |

---

### 🔍 範例

```java
Map<String, Integer> treeMap = new TreeMap<>();
Map<String, Integer> linkedMap = new LinkedHashMap<>();

treeMap.put("banana", 2);
treeMap.put("apple", 3);
treeMap.put("cherry", 1);

linkedMap.put("banana", 2);
linkedMap.put("apple", 3);
linkedMap.put("cherry", 1);

System.out.println("TreeMap:");
for (String key : treeMap.keySet()) {
    System.out.println(key);
}

System.out.println("LinkedHashMap:");
for (String key : linkedMap.keySet()) {
    System.out.println(key);
}
```

**輸出結果：**
```
TreeMap:
apple
banana
cherry

LinkedHashMap:
banana
apple
cherry
```

如果你想更詳細了解效能或記憶體使用情況，歡迎隨時告訴我。