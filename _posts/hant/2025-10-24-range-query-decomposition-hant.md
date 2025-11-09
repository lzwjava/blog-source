---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 平方根分解處理範圍查詢
translated: true
type: note
---

### 平方根分解

平方根分解（常簡稱為 √-decomposition）是電腦科學和競技程式設計中的一種技巧，用於優化對大型陣列或資料結構的範圍查詢和更新操作。當你需要高效地回答「找出子陣列中元素的總和/最大值/最小值」這類查詢，而又不想依賴像線段樹或芬威克樹這類實現較複雜的進階資料結構時，這種方法尤其有用。

#### 為何使用它？
- **時間複雜度權衡**：對於大小為 \\( n \\) 的陣列，樸素的範圍查詢每次查詢需要 \\( O(n) \\) 時間。平方根分解將此降低到每次查詢和更新只需 \\( O(\sqrt{n}) \\)，這在許多 \\( n \\) 高達 \\( 10^5 \\) 或 \\( 10^6 \\) 的問題中是一個良好的平衡點。
- **簡單性**：與進階資料結構相比，它更容易編碼和除錯。
- **應用場景**：常見於涉及範圍總和查詢、範圍最小值查詢（RMQ）或滑動視窗中的頻率計數等問題。

#### 運作原理
1. **分割成區塊**：將陣列分割成大小為 \\( \sqrt{n} \\)（向下取整）的區塊。如果 \\( n = 100 \\)，區塊大小 \\( b = 10 \\)，因此你會得到 10 個區塊。
   - 每個區塊儲存預先計算的資訊（例如，針對總和查詢，儲存該區塊中元素的總和）。
   
2. **查詢範圍 [L, R]**：
   - **完整區塊**：對於完全位於 [L, R] 內的完整區塊，只需在 \\( O(1) \\) 時間內取得預先計算的值。最多有 \\( O(\sqrt{n}) \\) 個完整區塊。
   - **部分區塊**：對於邊緣（左側和右側的部分區塊），手動遍歷個別元素，總共需要 \\( O(\sqrt{n}) \\) 時間（因為每個部分區塊的大小為 \\( \sqrt{n} \\)）。
   - 總計：\\( O(\sqrt{n}) \\)。

3. **更新操作**：當更新一個元素時，在 \\( O(\sqrt{n}) \\) 時間內重新計算其所屬區塊的預先計算值（通過重新計算該區塊的總和）。

#### 簡單範例：範圍總和查詢
假設我們有一個陣列 `A = [1, 3, 2, 4, 5]` 且 \\( n=5 \\)，因此區塊大小 \\( b = \sqrt{5} \approx 2 \\)。區塊如下：
- 區塊 0: [1, 3] → 總和 = 4
- 區塊 1: [2, 4] → 總和 = 6
- 區塊 2: [5] → 總和 = 5（最後一個區塊可能較小）

查詢從索引 1 到 4 的總和（0-based：元素 3,2,4,5）：
- 左側部分：索引 1（在區塊 0 中）→ 加上 3
- 完整區塊 1：加上 6
- 右側部分：索引 4（在區塊 2 中）→ 加上 5
- 總計：3 + 6 + 5 = 14

以程式碼實現（Python 虛擬碼）：
```python
import math

class SqrtDecomp:
    def __init__(self, arr):
        self.n = len(arr)
        self.b = int(math.sqrt(self.n))
        self.arr = arr[:]
        self.block_sums = [0] * ((self.n + self.b - 1) // self.b)
        self._build()
    
    def _build(self):
        for i in range(self.n):
            block_id = i // self.b
            self.block_sums[block_id] += self.arr[i]
    
    def update(self, idx, val):
        diff = val - self.arr[idx]
        self.arr[idx] = val
        block_id = idx // self.b
        self.block_sums[block_id] += diff
    
    def query(self, left, right):
        res = 0
        l_block, r_block = left // self.b, right // self.b
        
        if l_block == r_block:
            for i in range(left, right + 1):
                res += self.arr[i]
        else:
            # Left partial
            for i in range(left, (l_block + 1) * self.b):
                res += self.arr[i]
            # Full blocks
            for blk in range(l_block + 1, r_block):
                res += self.block_sums[blk]
            # Right partial
            for i in range(r_block * self.b, right + 1):
                res += self.arr[i]
        return res
```

這是一個基礎版本 — 若要應用於最小值/最大值查詢，只需將每個區塊儲存的總和改為最小值/最大值即可。

若想深入瞭解，可參考資源如 [GeeksforGeeks 上的平方根分解](https://www.geeksforgeeks.org/sqrt-decomposition-algorithm-square-root-decomposition-technique-set-1-introduction/) 或 [CP-Algorithms](https://cp-algorithms.com/data_structures/sqrt_decomposition.html)。