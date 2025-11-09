---
audio: false
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: NetworkX 圖形建立與分析範例
translated: true
type: note
---

NetworkX 是一個功能強大的 Python 函式庫，用於創建、分析和可視化複雜網絡。以下是幾個展示其功能的範例：

## 1. 基礎圖形創建與可視化

```python
import networkx as nx
import matplotlib.pyplot as plt

# 創建空圖形
G = nx.Graph()

# 添加節點
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from(range(4, 7))

# 添加邊緣
G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 4), (4, 5), (5, 6), (6, 1)])

# 可視化圖形
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
```

## 2. 有向圖範例

```python
# 創建有向圖
D = nx.DiGraph()

# 添加邊緣（自動添加節點）
D.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# 以不同節點顏色繪製
pos = nx.spring_layout(D)
nx.draw(D, pos, with_labels=True, node_color='lightgreen',
        edge_color='red', node_size=1000, arrowsize=20)
plt.show()
```

## 3. 圖形分析範例

```python
# 創建圖形
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# 基礎圖形屬性
print("節點數量:", G.number_of_nodes())
print("邊緣數量:", G.number_of_edges())
print("節點:", G.nodes())
print("邊緣:", G.edges())
print("節點 2 的度數:", G.degree(2))
print("節點 2 的鄰居:", list(G.neighbors(2)))
print("圖形是否連通?", nx.is_connected(G))
print("從 1 到 5 的最短路徑:", nx.shortest_path(G, 1, 5))
```

## 4. 加權圖範例

```python
# 創建加權圖
G = nx.Graph()

# 添加加權邊緣
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=1)
G.add_edge('C', 'D', weight=5)

# 繪製顯示權重的邊緣標籤
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightcoral')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
```

## 5. 社交網絡分析範例

```python
# 創建社交網絡圖
social = nx.Graph()

# 添加人員及其連接
people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
social.add_nodes_from(people)

connections = [('Alice', 'Bob'), ('Alice', 'Charlie'),
               ('Bob', 'Charlie'), ('Bob', 'David'),
               ('Charlie', 'Eve'), ('David', 'Eve')]
social.add_edges_from(connections)

# 計算中心性指標
degree_centrality = nx.degree_centrality(social)
betweenness_centrality = nx.betweenness_centrality(social)
closeness_centrality = nx.closeness_centrality(social)

print("度數中心性:", degree_centrality)
print("中介中心性:", betweenness_centrality)
print("接近中心性:", closeness_centrality)

# 可視化
nx.draw(social, with_labels=True, node_color='lightgreen', node_size=2000)
plt.show()
```

## 6. 隨機圖生成

```python
# 創建 Erdős–Rényi 隨機圖
random_graph = nx.erdos_renyi_graph(10, 0.3)  # 10 個節點，30% 邊緣概率

# 可視化
nx.draw(random_graph, with_labels=True, node_color='skyblue')
plt.show()
```

## 7. 圖形演算法範例

```python
# 創建圖形
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

# 尋找兩節點間所有簡單路徑
print("從 1 到 6 的所有路徑:", list(nx.all_simple_paths(G, 1, 6)))

# 最小生成樹
T = nx.minimum_spanning_tree(G)
print("MST 中的邊緣:", T.edges())

# 社群檢測（需要 python-louvain 套件）
# pip install python-louvain
try:
    import community as community_louvain
    partition = community_louvain.best_partition(G)
    print("社群分區:", partition)
except ImportError:
    print("請安裝 python-louvain 以進行社群檢測")
```

這些範例涵蓋了基礎圖形創建、可視化、分析和一些常見演算法。NetworkX 提供了更多處理複雜網絡的功能。