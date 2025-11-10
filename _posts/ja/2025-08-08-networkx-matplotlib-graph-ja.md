---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: NetworkXとMatplotlibによるグラフチュートリアル
translated: true
type: note
---

### ライブラリのインストール
NetworkXとMatplotlibを図の描画に使用するには、必要に応じてインストールしてください：
- NetworkX: グラフの作成と操作を担当
- Matplotlib: プロット機能を提供

pip経由でインストール：
```bash
pip install networkx matplotlib
```

より高速なレンダリングのため、MatplotlibはNumPyのインストールを推奨しています（`pip install numpy`）。

### 基本設定と例
1. **ライブラリのインポート**:  
   ```python
   import networkx as nx
   import matplotlib.pyplot as plt
   ```

2. **グラフの作成**:  
   NetworkXを使用して単純な無向グラフを構築（有向グラフ、重み付きエッジなどでカスタマイズ可能）：
   ```python
   G = nx.Graph()  # 空のグラフを作成
   G.add_nodes_from([1, 2, 3, 4, 5])  # ノードを追加（例：5ノード）
   G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])  # エッジ（接続）を追加
   ```

3. **図の描画と表示**:  
   可視化にはMatplotlibのバックエンドを使用：
   ```python
   nx.draw(G, with_labels=True)  # ノードラベル付きでグラフを描画
   plt.show()  # プロットを表示
   ```

これにより、グラフの基本的な円形レイアウト（5ノードの循環）が生成されます。

### 高度なカスタマイズ
- **レイアウト**: ノード位置の制御（例：ランダム、スプリングレイアウト）：
  ```python
  pos = nx.spring_layout(G)  # 現実的なネットワークのための力指向レイアウト
  nx.draw(G, pos=pos, with_labels=True, node_color='lightblue', edge_color='gray')
  plt.title("ネットワーク図")
  plt.show()
  ```
- **ノードとエッジのスタイル**: 外観のカスタマイズ：
  ```python
  nx.draw(G, pos=pos, node_size=500, node_color='red', edge_width=2, font_size=10)
  ```
- **有向グラフ**: 階層関係には`nx.DiGraph`を使用：
  ```python
  DG = nx.DiGraph()
  DG.add_edges_from([('A', 'B'), ('B', 'C')])
  nx.draw(DG, with_labels=True, arrows=True)
  plt.show()
  ```
- **図の保存**: 表示ではなくファイルにエクスポート：
  ```python
  plt.savefig('diagram.png')
  ```

### ヒントとリソース
- NetworkXドキュメント（networkx.org）で木やグリッドなどのグラフタイプを参照
- Matplotlibドキュメント（matplotlib.org）でGUIやサブプロットへの埋め込みを参照
- 大規模グラフ（100ノード以上）では、`nx.draw_networkx`や外部ツール（Graphvizなど）を使用してパフォーマンスを向上
- インタラクティブなプロットにはJupyter notebookで実験。問題が発生した場合、一般的なエラーはバックエンドの不足による（インタラクティブウィンドウには`pip install pyqt5`などでインストール）。