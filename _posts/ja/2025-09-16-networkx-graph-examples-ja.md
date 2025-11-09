---
audio: false
generated: true
image: false
lang: ja
layout: post
model: mistralai/mistral-medium-3.1
title: NetworkXグラフ作成と分析の例
translated: true
type: note
---

NetworkXは、複雑なネットワークを作成、分析、視覚化するための強力なPythonライブラリです。以下に、その機能を示すいくつかの例を紹介します。

## 1. 基本的なグラフ作成と視覚化

```python
import networkx as nx
import matplotlib.pyplot as plt

# 空のグラフを作成
G = nx.Graph()

# ノードを追加
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from(range(4, 7))

# エッジを追加
G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 4), (4, 5), (5, 6), (6, 1)])

# グラフを視覚化
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
```

## 2. 有向グラフの例

```python
# 有向グラフを作成
D = nx.DiGraph()

# エッジを追加（ノードも自動的に追加）
D.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# 異なるノード色で描画
pos = nx.spring_layout(D)
nx.draw(D, pos, with_labels=True, node_color='lightgreen',
        edge_color='red', node_size=1000, arrowsize=20)
plt.show()
```

## 3. グラフ分析の例

```python
# グラフを作成
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# 基本的なグラフプロパティ
print("ノード数:", G.number_of_nodes())
print("エッジ数:", G.number_of_edges())
print("ノード:", G.nodes())
print("エッジ:", G.edges())
print("ノード2の次数:", G.degree(2))
print("ノード2の隣接ノード:", list(G.neighbors(2)))
print("グラフは連結か？", nx.is_connected(G))
print("ノード1から5への最短経路:", nx.shortest_path(G, 1, 5))
```

## 4. 重み付きグラフの例

```python
# 重み付きグラフを作成
G = nx.Graph()

# 重み付きエッジを追加
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=1)
G.add_edge('C', 'D', weight=5)

# 重みを表示するエッジラベルで描画
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightcoral')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
```

## 5. ソーシャルネットワーク分析の例

```python
# ソーシャルネットワークグラフを作成
social = nx.Graph()

# 人物とその接続を追加
people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
social.add_nodes_from(people)

connections = [('Alice', 'Bob'), ('Alice', 'Charlie'),
               ('Bob', 'Charlie'), ('Bob', 'David'),
               ('Charlie', 'Eve'), ('David', 'Eve')]
social.add_edges_from(connections)

# 中心性指標を計算
degree_centrality = nx.degree_centrality(social)
betweenness_centrality = nx.betweenness_centrality(social)
closeness_centrality = nx.closeness_centrality(social)

print("次数中心性:", degree_centrality)
print("媒介中心性:", betweenness_centrality)
print("近接中心性:", closeness_centrality)

# 視覚化
nx.draw(social, with_labels=True, node_color='lightgreen', node_size=2000)
plt.show()
```

## 6. ランダムグラフ生成

```python
# エルデシュ・レーニィランダムグラフを作成
random_graph = nx.erdos_renyi_graph(10, 0.3)  # 10ノード、30%のエッジ確率

# 視覚化
nx.draw(random_graph, with_labels=True, node_color='skyblue')
plt.show()
```

## 7. グラフアルゴリズムの例

```python
# グラフを作成
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

# 2つのノード間の全ての単純経路を検索
print("ノード1から6への全ての経路:", list(nx.all_simple_paths(G, 1, 6)))

# 最小全域木
T = nx.minimum_spanning_tree(G)
print("MSTのエッジ:", T.edges())

# コミュニティ検出（python-louvainパッケージが必要）
# pip install python-louvain
try:
    import community as community_louvain
    partition = community_louvain.best_partition(G)
    print("コミュニティ分割:", partition)
except ImportError:
    print("コミュニティ検出にはpython-louvainをインストールしてください")
```

これらの例は、基本的なグラフ作成、視覚化、分析、および一般的なアルゴリズムをカバーしています。NetworkXは、複雑なネットワークを扱うための多くの機能を提供しています。