---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 理解Dijkstra最短路徑演算法
translated: true
type: note
---

### 理解 Dijkstra 最短路徑演算法

Dijkstra 演算法是在邊緣具有非負權重（如距離或成本）的圖中，尋找節點間最短路徑的基礎方法。它以 Edsger W. Dijkstra 命名，廣泛應用於 GPS 導航、網絡路由等領域。關鍵直覺是：它貪婪地探索圖，總是選擇最近的未訪問節點並從那裡更新路徑，就像從起點開始的漣漪效應。

#### 快速預備知識
- **圖基礎**：將圖視為由道路（邊）連接的城市（節點）地圖，道路具有長度（權重）。我們假設權重為正數——沒有負距離！
- **有向與無向**：適用於兩者，但此處示例為簡單起見使用無向圖。
- **最短路徑**：從起點到目標具有最小總權重的路徑。

如果不熟悉圖，可以想像社交網絡：人（節點）、具有「強度」分數的友誼（權重）。

#### 運作方式：逐步直覺
Dijkstra 使用**優先佇列**（像按緊急程度排序的待辦事項清單——此處按當前已知最短距離）逐步建立最短路徑。一旦節點被確定，它不會重新訪問，從而提高效率。

1. **初始化**：
   - 選擇起始節點（起點）。將其距離設為 0。
   - 將所有其他節點的距離設為無窮大（∞）。
   - 追蹤每個節點的「路徑來源」（初始為無）。

2. **當存在未訪問節點時**：
   - 選擇具有最小當前距離的未訪問節點（從優先佇列中）。
   - 「確定」它：標記為已訪問。此距離是最終的——得益於非負權重，後續不會找到更短的路徑。
   - 對於此節點的每個鄰居：
     - 計算潛在新距離：（已確定節點的距離）+（到鄰居的邊權重）。
     - 如果此值小於鄰居的當前距離，則更新它並記錄路徑來自已確定節點。
   - 重複直到所有節點被訪問或目標節點被確定。

如果只關心單一目標節點，演算法可以提前停止。

**為何有效**：它類似加權的廣度優先搜索——總是先擴展成本最低的邊界。證明依賴於一旦節點被確定，其距離無法改善的事實（貪婪選擇性質）。

#### 簡單示例
想像一個包含 4 個城市的圖：A（起點）、B、C、D。邊與權重：

- A → B: 4
- A → C: 2
- B → C: 1
- B → D: 5
- C → D: 8

ASCII 視覺化：
```
   4
A ----- B
 \     / \
  2   1   5
  \   /     |
   C ------- D
     8
```

從 A 運行 Dijkstra：

- **開始**：dist[A]=0, dist[B]=∞, dist[C]=∞, dist[D]=∞。佇列：A。
- **確定 A**（dist=0）。
  - 更新 B：0+4=4
  - 更新 C：0+2=2
  - 佇列：C(2), B(4)
- **確定 C**（dist=2）。
  - 更新 D：2+8=10
  - 佇列：B(4), D(10)
- **確定 B**（dist=4）。
  - 更新 C：4+1=5（但 2<5，無變化）
  - 更新 D：4+5=9（9<10，更新為 9）
  - 佇列：D(9)
- **確定 D**（dist=9）。

最終距離：A=0, B=4, C=2, D=9。  
到 D 的路徑：A → B → D（總計 9，短於 A → C → D=10）。

您可以使用「前節點」陣列回溯路徑。

#### 虛擬碼
以下是簡單的實現大綱（類 Python）：

```python
import heapq  # 用於優先佇列

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    pq = [(0, start)]  # (距離, 節點)
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        if current_dist > distances[current]:
            continue  # 過時條目
        
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current
                heapq.heappush(pq, (distance, neighbor))
    
    # 重構到目標（例如 'D'）的路徑
    path = []
    node = 'D'
    while node is not None:
        path.append(node)
        node = previous[node]
    return path[::-1], distances['D']  # 反轉以獲得從起點到終點
```

- `graph`：字典的字典，例如 `{'A': {'B':4, 'C':2}, ...}`
- 時間複雜度：使用二元堆積為 O((V+E) log V)（V=頂點，E=邊）。對於稀疏圖非常有效。

#### 深入理解的技巧
- **視覺化**：在紙上繪製圖，使用距離/已訪問表格模擬步驟。
- **常見陷阱**：負權重時失敗（改用 Bellman-Ford）。假設圖是連通的。
- **練習**：在小圖上嘗試，然後為地圖數據集編碼實現。
- **變體**：A* 添加啟發式以加速搜索（例如在遊戲中）。

這應該能讓您理解——從示例開始，多次在腦中運行它！

[維基百科：Dijkstra 演算法](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)  
[GeeksforGeeks：視覺解釋](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)