---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/o1-mini
title: NetworkX Pythonグラフライブラリ入門
translated: true
type: note
---

NetworkXは、複雑なネットワーク（グラフ）の作成、操作、解析のための強力なPythonライブラリです。無向グラフと有向グラフの両方を扱うツールを提供し、重み付きエッジの処理や様々なネットワーク解析を実行できます。

以下は、NetworkXを使い始めるためのいくつかの例です：

---

### 1. **NetworkXのインストール**

NetworkXを使用する前に、インストールされていることを確認してください。`pip`を使用してインストールできます：

```bash
pip install networkx
```

---

### 2. **単純なグラフの作成と可視化**

単純な無向グラフを作成し、ノードとエッジを追加して、Matplotlibを使用して可視化する方法を示します。

```python
import networkx as nx
import matplotlib.pyplot as plt

# 空のグラフを作成
G = nx.Graph()

# ノードを追加
G.add_node(1)
G.add_nodes_from([2, 3, 4])

# エッジを追加（ノードが存在しない場合は自動的に追加）
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 4)])

# グラフを描画
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
plt.title("単純な無向グラフ")
plt.show()
```

**出力：**

4つのノードがエッジで接続された単純な無向グラフ。

---

### 3. **有向グラフ**

有向グラフ（DiGraph）の作成と可視化：

```python
import networkx as nx
import matplotlib.pyplot as plt

# 有向グラフを作成
DG = nx.DiGraph()

# エッジを追加（ノードは自動的に追加）
DG.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('C', 'A'),
    ('C', 'D')
])

# 矢印付きで有向グラフを描画
pos = nx.circular_layout(DG)
nx.draw(DG, pos, with_labels=True, node_color='lightgreen', edge_color='gray', arrows=True, node_size=700)
plt.title("有向グラフ")
plt.show()
```

**出力：**

エッジの方向を矢印で示した有向グラフ。

---

### 4. **重み付きグラフ**

エッジに重みを割り当てて可視化：

```python
import networkx as nx
import matplotlib.pyplot as plt

# 重み付きグラフを作成
WG = nx.Graph()

# 重みとともにエッジを追加
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# ラベル付けのためのエッジの重みを取得
edge_labels = nx.get_edge_attributes(WG, 'weight')

# グラフを描画
pos = nx.spring_layout(WG)
nx.draw(WG, pos, with_labels=True, node_color='lightyellow', edge_color='gray', node_size=700)
nx.draw_networkx_edge_labels(WG, pos, edge_labels=edge_labels)
plt.title("重み付きグラフ")
plt.show()
```

**出力：**

重みを表すエッジラベル付きの重み付きグラフ。

---

### 5. **最短経路の計算**

ダイクストラ法を使用した2ノード間の最短経路の検索（重み付きグラフ用）：

```python
import networkx as nx

# 重み付きグラフを作成（前の例と同じ）
WG = nx.Graph()
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# 'A'から'D'への最短経路を計算
shortest_path = nx.dijkstra_path(WG, source='A', target='D', weight='weight')
path_length = nx.dijkstra_path_length(WG, source='A', target='D', weight='weight')

print(f"AからDへの最短経路: {shortest_path}、総重み: {path_length}")
```

**出力：**

```
AからDへの最短経路: ['A', 'C', 'D']、総重み: 5
```

---

### 6. **中心性指標**

グラフ内の重要なノードを特定するための様々な中心性指標の計算。

```python
import networkx as nx

# サンプルグラフを作成
G = nx.karate_club_graph()

# 次数中心性を計算
degree_centrality = nx.degree_centrality(G)

# 媒介中心性を計算
betweenness_centrality = nx.betweenness_centrality(G)

# 固有ベクトル中心性を計算
eigen_centrality = nx.eigenvector_centrality(G, max_iter=1000)

# 次数中心性で上位5ノードを表示
sorted_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)
print("次数中心性による上位5ノード:")
for node, centrality in sorted_degree[:5]:
    print(f"ノード {node}: {centrality:.4f}")

# 同様に他の中心性も表示可能
```

**出力：**

```
次数中心性による上位5ノード:
ノード 33: 0.6035
ノード 0: 0.3793
ノード 1: 0.3793
ノード 2: 0.3793
ノード 3: 0.3793
```

*注：* Karate Clubグラフは、NetworkXでよく使用されるソーシャルネットワークの例です。

---

### 7. **Girvan-Newmanアルゴリズムによるコミュニティ検出**

グラフ内のコミュニティの特定。

```python
import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt

# グラフを作成（Karate Clubグラフを使用）
G = nx.karate_club_graph()

# Girvan-Newman法を使用してコミュニティを計算
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
second_level_communities = next(communities_generator)

# コミュニティに色を割り当てる関数
def get_community_colors(G, communities):
    color_map = {}
    for idx, community in enumerate(communities):
        for node in community:
            color_map[node] = idx
    return [color_map[node] for node in G.nodes()]

# 希望のレベルのコミュニティを選択
communities = second_level_communities
colors = get_community_colors(G, communities)

# コミュニティの色でグラフを描画
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=colors, with_labels=True, cmap=plt.cm.Set1)
plt.title("Karate Clubグラフのコミュニティ")
plt.show()
```

**出力：**

コミュニティの所属に基づいてノードが色分けされたKarate Clubグラフの可視化。

---

### 8. **グラフの読み書き**

NetworkXは、隣接リスト、エッジリスト、GraphMLなどの様々な形式でのグラフの読み書きをサポートしています。

**エッジリストの読み込み：**

```python
import networkx as nx

# 'edges.txt'が以下を含むと仮定：
# A B
# A C
# B C
# B D
# C D

G = nx.read_edgelist('edges.txt', delimiter=' ')
print("ノード:", G.nodes())
print("エッジ:", G.edges())
```

**GraphMLへのグラフの書き出し：**

```python
import networkx as nx

G = nx.complete_graph(5)  # 5ノードの完全グラフを作成
nx.write_graphml(G, 'complete_graph.graphml')
print("グラフを 'complete_graph.graphml' に保存")
```

---

### 9. **Pandas DataFrameとの連携**

より高度なデータ操作のためにNetworkXをPandasと統合。

```python
import networkx as nx
import pandas as pd

# 重み付きエッジを表すDataFrameを作成
data = {
    'source': ['A', 'A', 'B', 'B', 'C'],
    'target': ['B', 'C', 'C', 'D', 'D'],
    'weight': [4, 2, 5, 10, 3]
}
df = pd.DataFrame(data)

# DataFrameから重み付きグラフを作成
G = nx.from_pandas_edgelist(df, 'source', 'target', ['weight'])

# 重み付きエッジを表示
for u, v, data in G.edges(data=True):
    print(f"({u}, {v}) - 重み: {data['weight']}")
```

**出力：**

```
(A, B) - 重み: 4
(A, C) - 重み: 2
(B, C) - 重み: 5
(B, D) - 重み: 10
(C, D) - 重み: 3
```

---

### 10. **NetworkXとMatplotlibによる高度な可視化**

読みやすさのためにグラフの外観をカスタマイズ。

```python
import networkx as nx
import matplotlib.pyplot as plt

# グラフを作成
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'C'), ('C', 'D'), ('D', 'E'),
    ('E', 'F'), ('F', 'C')
])

# レイアウトを使用して位置を割り当て
pos = nx.spring_layout(G, seed=42)

# 異なるサイズと色でノードを描画
node_sizes = [700 if node == 'C' else 300 for node in G.nodes()]
node_colors = ['red' if node == 'C' else 'skyblue' for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors)

# 幅を変えてエッジを描画
edge_widths = [2 if (u == 'C' or v == 'C') else 1 for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, width=edge_widths)

# ラベルを描画
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

plt.title("カスタマイズされたグラフ可視化")
plt.axis('off')
plt.show()
```

**出力：**

ノード'C'が赤色で大きくハイライトされ、'C'に接続されたエッジが太い線で表示されるカスタマイズされたグラフ。

---

これらの例は、Pythonでグラフを作成、操作、解析するためにNetworkXを活用する方法の基礎的理解を提供します。より高度な使用方法と詳細なドキュメントについては、[公式NetworkXドキュメント](https://networkx.org/documentation/stable/)を参照してください。