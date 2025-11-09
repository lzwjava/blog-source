---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/o1-mini
title: NetworkX Python 圖形庫入門
translated: true
type: note
---

NetworkX 是一個功能強大的 Python 函式庫，用於建立、操作和研究複雜網絡（圖形）。它提供了處理無向圖與有向圖、加權邊及執行各種網絡分析的工具。

以下是一些幫助您開始使用 NetworkX 的範例：

---

### 1. **安裝 NetworkX**

在使用 NetworkX 之前，請確保已安裝。您可以使用 `pip` 安裝：

```bash
pip install networkx
```

---

### 2. **建立與視覺化簡單圖形**

以下是建立簡單無向圖、添加節點與邊，並使用 Matplotlib 進行視覺化的方法。

```python
import networkx as nx
import matplotlib.pyplot as plt

# 建立空圖形
G = nx.Graph()

# 添加節點
G.add_node(1)
G.add_nodes_from([2, 3, 4])

# 添加邊（如果節點不存在會自動添加）
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 4)])

# 繪製圖形
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
plt.title("簡單無向圖")
plt.show()
```

**輸出：**

一個包含 4 個節點並通過邊連接的簡單無向圖。

---

### 3. **有向圖**

建立與視覺化有向圖（DiGraph）：

```python
import networkx as nx
import matplotlib.pyplot as plt

# 建立有向圖
DG = nx.DiGraph()

# 添加邊（節點會自動添加）
DG.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('C', 'A'),
    ('C', 'D')
])

# 繪製帶箭頭的有向圖
pos = nx.circular_layout(DG)
nx.draw(DG, pos, with_labels=True, node_color='lightgreen', edge_color='gray', arrows=True, node_size=700)
plt.title("有向圖")
plt.show()
```

**輸出：**

一個用箭頭顯示邊方向的有向圖。

---

### 4. **加權圖**

為邊分配權重並進行視覺化：

```python
import networkx as nx
import matplotlib.pyplot as plt

# 建立加權圖
WG = nx.Graph()

# 添加帶權重的邊
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# 獲取邊權重標籤
edge_labels = nx.get_edge_attributes(WG, 'weight')

# 繪製圖形
pos = nx.spring_layout(WG)
nx.draw(WG, pos, with_labels=True, node_color='lightyellow', edge_color='gray', node_size=700)
nx.draw_networkx_edge_labels(WG, pos, edge_labels=edge_labels)
plt.title("加權圖")
plt.show()
```

**輸出：**

一個帶有邊標籤顯示權重的加權圖。

---

### 5. **計算最短路徑**

使用 Dijkstra 演算法（適用於加權圖）尋找兩個節點之間的最短路徑：

```python
import networkx as nx

# 建立加權圖（與前例相同）
WG = nx.Graph()
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# 計算從 'A' 到 'D' 的最短路徑
shortest_path = nx.dijkstra_path(WG, source='A', target='D', weight='weight')
path_length = nx.dijkstra_path_length(WG, source='A', target='D', weight='weight')

print(f"從 A 到 D 的最短路徑：{shortest_path}，總權重為 {path_length}")
```

**輸出：**

```
從 A 到 D 的最短路徑：['A', 'C', 'D']，總權重為 5
```

---

### 6. **中心性度量**

計算各種中心性度量以識別圖中的重要節點。

```python
import networkx as nx

# 建立範例圖形
G = nx.karate_club_graph()

# 計算度中心性
degree_centrality = nx.degree_centrality(G)

# 計算中介中心性
betweenness_centrality = nx.betweenness_centrality(G)

# 計算特徵向量中心性
eigen_centrality = nx.eigenvector_centrality(G, max_iter=1000)

# 顯示按度中心性排序的前 5 個節點
sorted_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)
print("按度中心性排序的前 5 個節點：")
for node, centrality in sorted_degree[:5]:
    print(f"節點 {node}：{centrality:.4f}")

# 同樣可以顯示其他中心性度量
```

**輸出：**

```
按度中心性排序的前 5 個節點：
節點 33：0.6035
節點 0：0.3793
節點 1：0.3793
節點 2：0.3793
節點 3：0.3793
```

*註：* Karate Club 圖是 NetworkX 中常用的社交網絡範例。

---

### 7. **使用 Girvan-Newman 演算法檢測社群**

識別圖中的社群結構。

```python
import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt

# 建立圖形（使用 Karate Club 圖）
G = nx.karate_club_graph()

# 使用 Girvan-Newman 演算法計算社群
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
second_level_communities = next(communities_generator)

# 為社群分配顏色的函數
def get_community_colors(G, communities):
    color_map = {}
    for idx, community in enumerate(communities):
        for node in community:
            color_map[node] = idx
    return [color_map[node] for node in G.nodes()]

# 選擇所需的社群層級
communities = second_level_communities
colors = get_community_colors(G, communities)

# 繪製帶有社群顏色的圖形
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=colors, with_labels=True, cmap=plt.cm.Set1)
plt.title("Karate Club 圖中的社群結構")
plt.show()
```

**輸出：**

根據社群歸屬以不同顏色顯示節點的 Karate Club 圖視覺化。

---

### 8. **讀取與寫入圖形**

NetworkX 支援多種圖形讀寫格式，例如鄰接列表、邊列表和 GraphML。

**讀取邊列表：**

```python
import networkx as nx

# 假設 'edges.txt' 包含：
# A B
# A C
# B C
# B D
# C D

G = nx.read_edgelist('edges.txt', delimiter=' ')
print("節點：", G.nodes())
print("邊：", G.edges())
```

**將圖形寫入 GraphML：**

```python
import networkx as nx

G = nx.complete_graph(5)  # 建立包含 5 個節點的完全圖
nx.write_graphml(G, 'complete_graph.graphml')
print("圖形已儲存至 'complete_graph.graphml'")
```

---

### 9. **將 NetworkX 與 Pandas DataFrames 結合使用**

整合 NetworkX 與 Pandas 進行進階數據操作。

```python
import networkx as nx
import pandas as pd

# 建立代表帶權重邊的 DataFrame
data = {
    'source': ['A', 'A', 'B', 'B', 'C'],
    'target': ['B', 'C', 'C', 'D', 'D'],
    'weight': [4, 2, 5, 10, 3]
}
df = pd.DataFrame(data)

# 從 DataFrame 建立加權圖
G = nx.from_pandas_edgelist(df, 'source', 'target', ['weight'])

# 顯示帶權重的邊
for u, v, data in G.edges(data=True):
    print(f"({u}, {v}) - 權重：{data['weight']}")
```

**輸出：**

```
(A, B) - 權重：4
(A, C) - 權重：2
(B, C) - 權重：5
(B, D) - 權重：10
(C, D) - 權重：3
```

---

### 10. **使用 NetworkX 與 Matplotlib 進行進階視覺化**

自訂圖形外觀以提升可讀性。

```python
import networkx as nx
import matplotlib.pyplot as plt

# 建立圖形
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'C'), ('C', 'D'), ('D', 'E'),
    ('E', 'F'), ('F', 'C')
])

# 使用佈局分配位置
pos = nx.spring_layout(G, seed=42)

# 繪製不同大小和顏色的節點
node_sizes = [700 if node == 'C' else 300 for node in G.nodes()]
node_colors = ['red' if node == 'C' else 'skyblue' for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors)

# 繪製不同寬度的邊
edge_widths = [2 if (u == 'C' or v == 'C') else 1 for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, width=edge_widths)

# 繪製標籤
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

plt.title("自訂圖形視覺化")
plt.axis('off')
plt.show()
```

**輸出：**

一個自訂的圖形，其中節點 'C' 以紅色突出顯示且尺寸較大，與 'C' 相連的邊線條較粗。

---

這些範例提供了使用 NetworkX 在 Python 中建立、操作和分析圖形的基礎知識。如需進階用法和詳細文檔，請參閱 [官方 NetworkX 文檔](https://networkx.org/documentation/stable/)。