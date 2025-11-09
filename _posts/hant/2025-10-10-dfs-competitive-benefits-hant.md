---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 競賽程式設計中深度優先搜尋的優勢
translated: true
type: note
---

### 為何在競程中使用 DFS？

深度優先搜尋（DFS）是一種基礎的圖形遍歷演算法，在競技程式設計中廣泛使用，因為它能有效率地探索涉及連通性、路徑和遞迴結構的問題。以下是它特別有價值的原因：

- **深度探索的效率**：DFS 在回溯前會深入探索一條路徑，這使其非常適合需要尋找單一路徑、偵測循環或徹底探索所有可能性的問題（例如回溯情境）。其時間複雜度對於圖形為 O(V + E)（V = 頂點，E = 邊），在大多數競賽限制下是線性且快速的。
  
- **自然處理遞迴問題**：許多問題可以建模為具有遞迴子問題的樹或圖（例如迷宮、謎題或樹遍歷）。DFS 使用呼叫堆疊進行遞迴，與迭代方法相比，保持程式碼簡潔且記憶體效率高。

- **適用於多種圖形問題**：它非常適合偵測連通元件、尋找橋接點/關節點、拓撲排序或解決二分圖問題。在競賽中，圖形常常隱藏在其他形式中（例如字串或網格），而 DFS 在這些情況下表現出色。

- **回溯能力**：對於組合問題，如 N 皇后問題、數獨或生成子集/排列，帶有回溯的 DFS 能及早修剪無效路徑，避免暴力解法的計算爆炸。

- **空間權衡**：對於深度圖形，它比 BFS 使用更少的記憶體（僅遞迴堆疊），這在記憶體受限的競賽中很重要。

總的來說，當問題明顯需要「深入探索並在卡住時回溯」時，DFS 是首選，尤其是在像 Codeforces 或 LeetCode 這樣的平台上。

### DFS 範例

以下是三個常見範例，附帶虛擬碼（以 Python 風格撰寫以求清晰）。這些範例經過簡化以用於說明—請根據完整問題進行調整。

#### 1. **偵測無向圖中的循環**
   - **問題**：給定一個圖形，檢查是否存在循環。
   - **為何使用 DFS？**：深入遍歷；如果在目前路徑中重新訪問一個節點，則存在循環。
   - **虛擬碼**：
     ```python:disable-run
     def has_cycle(graph, start, visited, parent):
         visited[start] = True
         for neighbor in graph[start]:
             if not visited[neighbor]:
                 if has_cycle(graph, neighbor, visited, start):
                     return True
             elif neighbor != parent:
                 return True  # 回邊到祖先節點
         return False

     # 使用方式
     visited = {node: False for node in graph}
     cycle_exists = any(has_cycle(graph, node, visited, -1) for node in graph if not visited[node])
     ```

#### 2. **尋找圖中的連通元件**
   - **問題**：識別無向圖中所有獨立的連通群組。
   - **為何使用 DFS？**：從一個節點開始，將所有可到達的節點標記為一個元件，然後移動到下一個未訪問的節點。
   - **虛擬碼**：
     ```python
     def dfs(graph, start, visited, component):
         visited[start] = True
         component.append(start)
         for neighbor in graph[start]:
             if not visited[neighbor]:
                 dfs(graph, neighbor, visited, component)

     # 使用方式
     visited = {node: False for node in graph}
     components = []
     for node in graph:
         if not visited[node]:
             component = []
             dfs(graph, node, visited, component)
             components.append(component)
     ```

#### 3. **迷宮/路徑尋找（回溯）**
   - **問題**：在網格迷宮中尋找從起點到終點的路徑（0 = 開放，1 = 牆壁）。
   - **為何使用 DFS？**：遞迴嘗試路徑；在死路時回溯。
   - **虛擬碼**（網格為二維列表）：
     ```python
     def solve_maze(grid, x, y, end_x, end_y, path):
         if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 1:
             return False
         if x == end_x and y == end_y:
             path.append((x, y))
             return True
         path.append((x, y))
         grid[x][y] = 1  # 標記為已訪問
         # 嘗試方向：下、右、上、左
         if (solve_maze(grid, x+1, y, end_x, end_y, path) or
             solve_maze(grid, x, y+1, end_x, end_y, path) or
             solve_maze(grid, x-1, y, end_x, end_y, path) or
             solve_maze(grid, x, y-1, end_x, end_y, path)):
             return True
         path.pop()  # 回溯
         grid[x][y] = 0  # 取消標記
         return False

     # 使用方式：path = []; solve_maze(grid, 0, 0, rows-1, cols-1, path)
     ```

這些範例展示了 DFS 的遞迴優雅性—在像「Number of Islands」（LeetCode）或「Cycle Detection」（HackerRank）這樣的問題上練習，以親眼見證其運作！