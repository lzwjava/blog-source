---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 聯合查找算法簡介
translated: true
type: note
---

### 聯合查找（並查集）演算法簡介

**聯合查找**演算法（亦稱為**並查集**或**DSU**）是一種資料結構及操作集合，用於管理互不相交的集合（元素群組之間沒有重疊）。它在處理涉及分組、合併或連通性檢查的問題時非常高效，例如圖論演算法或聚類分析。

核心操作：
- **查找**：確定元素所屬的集合（通常透過尋找該集合的「根節點」或代表元素）。
- **合併**：將兩個集合合併為一個。

此演算法的優勢在於其優化技巧，例如**路徑壓縮**（在查找過程中扁平化樹狀結構）和**按秩合併**（將較小的樹合併到較大的樹中以保持結構平衡）。這使得每次操作的分攤時間複雜度接近 O(1)——對於大型資料集來說極為迅速。

#### 核心資料結構
- 一個陣列 `p[]`（父節點陣列）：`p[i]` 指向元素 `i` 的父節點。初始時，每個元素都是自身的父節點（`p[i] = i`）。
- 可選：一個 `rank[]` 陣列，用於按秩合併以平衡合併操作。

#### 查找操作（含路徑壓縮）
`find` 函數從一個元素回溯至其根節點。您提到的程式碼行—`if (p[i] != -1) i = p[i]`—是此過程中的遞迴或迭代步驟。它跟隨父節點指標直到抵達根節點（其中 `p[root] == root` 或對於哨兵值而言 `p[root] == -1`）。

以下是一個簡單的迭代虛擬碼實現：

```
function find(i):
    if p[i] != -1:  # 非根節點（或非哨兵值）
        i = p[i]     # 移至父節點（這是您的程式碼行！）
        return find(i)  # 遞迴：持續直至根節點
    else:
        return i     # 找到根節點
```

**使用完整路徑壓縮**（以優化未來的查找操作），我們透過將所有節點直接指向根節點來扁平化路徑：

```
function find(i):
    if p[i] != i:  # 非根節點
        p[i] = find(p[i])  # 壓縮：將父節點設為找到的根節點
    return p[i]
```

- `-1` 常被用作根節點的哨兵值（而非使用 `i` 表示自身為父節點），特別是在某些實現中用於區分未初始化或無效的節點。
- 若無壓縮，重複的查找操作可能使結構變成長鏈（最壞情況 O(n)）。壓縮則使其幾乎扁平化。

#### 合併操作
要合併 `x` 和 `y` 的集合：
1. 查找根節點：`rootX = find(x)`，`rootY = find(y)`。
2. 若 `rootX != rootY`，將其中之一連結至另一個（例如，按秩合併：將秩較小的樹附加至秩較大的樹）。

虛擬碼：
```
function union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            p[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            p[rootX] = rootY
        else:
            p[rootY] = rootX
            rank[rootX] += 1  # 增加新父節點的秩
```

#### 如何使用此演算法
聯合查找非常適合動態連通性問題。以下為逐步指南及範例：

1. **初始化**：
   - 建立大小為 `n`（元素數量）的 `p[]` 陣列：`for i in 0 to n-1: p[i] = -1`（或使用 `i` 表示自身為父節點）。
   - 可選：將 `rank[]` 全部設為 0 或 1。

2. **基本使用流程**：
   - 檢查兩個元素是否屬於同一集合：`if find(a) == find(b)`。
   - 合併集合：`union(a, b)`。
   - 以任意順序處理查詢/合併——它是動態的！

3. **範例：檢測圖中的連通分量**
   假設一個圖有 5 個節點 (0-4) 及邊如 (0-1)、(1-2)、(3-4)。
   ```
   // 初始化
   p = [-1, -1, -1, -1, -1]
   rank = [0, 0, 0, 0, 0]

   // 合併邊
   union(0, 1)  // 合併 0 和 1，假設 p[0]=-1, p[1]=0
   union(1, 2)  // 將 2 合併至 {0,1}，p[2]=0
   union(3, 4)  // 合併 {3,4}，假設 p[3]=-1, p[4]=3

   // 查詢：0 和 2 是否連通？find(0)=0, find(2)=0 → 是
   // 2 和 3 是否連通？find(2)=0, find(3)=-1 → 否
   ```

4. **實際應用場景**：
   - **Kruskal 最小生成樹**：按權重排序邊，合併不會形成環的邊（若 `find(u) == find(v)` 則跳過）。
   - **社交網絡好友關係**：合併好友，查找共同聯繫。
   - **影像分割**：合併顏色相近的相鄰像素。
   - **無向圖中的環檢測**：合併端點；若已在同一集合，則存在環。

#### 簡易 Python 實現
```python
class UnionFind:
    def __init__(self, n):
        self.p = [-1] * n
        self.rank = [0] * n
    
    def find(self, i):
        if self.p[i] != -1 and self.p[i] != i:  # 處理哨兵值 + 自身為父節點
            self.p[i] = self.find(self.p[i])  # 路徑壓縮
        return self.p[i] if self.p[i] != -1 else i
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.p[py] = px
            elif self.rank[px] < self.rank[py]:
                self.p[px] = py
            else:
                self.p[py] = px
                self.rank[px] += 1

# 使用範例
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print(uf.find(0) == uf.find(2))  # True
```

這保持了高效性——嘗試使用更大的 `n` 來體驗其速度！

若需深入瞭解，請參閱 [GeeksforGeeks: Union-Find Algorithm](https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank-and-path-compression/) 或 [CP-Algorithms: DSU](https://cp-algorithms.com/data_structures/disjoint_set_union.html)。