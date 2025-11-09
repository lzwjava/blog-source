---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Union-Findアルゴリズム入門
translated: true
type: note
---

### Union-Find（Disjoint Set Union）アルゴリズム入門

**Union-Find**アルゴリズム（**Disjoint Set Union**または**DSU**とも呼ばれる）は、互いに素な集合（重複しない要素のグループ）を管理するためのデータ構造と操作のセットです。グラフアルゴリズムやクラスタリングなど、グループ化、結合、接続性の確認を伴う問題に効率的です。

主な操作:
- **Find**: 要素がどの集合に属するかを決定します（多くの場合、集合の「ルート」または代表を見つけることで行います）。
- **Union**: 2つの集合を1つに結合します。

このアルゴリズムが優れている理由は、**経路圧縮**（Find操作中に木構造を平坦化する）や**Union by rank/size**（構造をバランスさせるために小さな木を大きな木に結合する）などの最適化によるものです。これにより、操作あたり償却時間でほぼO(1)という非常に高速な処理が可能になり、大規模なデータセットにも適しています。

#### コアデータ構造
- 配列 `p[]`（親配列）: `p[i]` は要素 `i` の親を指します。初期状態では、各要素は自身の親です（`p[i] = i`）。
- オプション: 結合をバランスさせるための `rank[]` 配列（Union by rank用）。

#### Find操作（経路圧縮付き）
`find` 関数は、要素からそのルートまで遡ります。あなたが言及した行 `if (p[i] != -1) i = p[i]` は、このプロセスにおける再帰的または反復的なステップです。これは、ルート（`p[root] == root` または番兵として `p[root] == -1` の場所）に到達するまで親ポインタをたどります。

以下に、擬似コードによる単純な反復的実装を示します:

```
function find(i):
    if p[i] != -1:  # ルートではない（または番兵ではない）
        i = p[i]     # 親に移動（これがあなたの言及した行です！）
        return find(i)  # 再帰的: ルートに到達するまで続行
    else:
        return i     # ルートが見つかった
```

**完全な経路圧縮**（将来のFind操作を最適化するため）では、すべてのノードを直接ルートに設定してパスを平坦化します:

```
function find(i):
    if p[i] != i:  # ルートではない
        p[i] = find(p[i])  # 圧縮: 親が見つかったルートに設定
    return p[i]
```

- `-1` は、多くの場合、ルートの番兵として使用されます（自己親指定の `i` の代わりに）。特に、未初期化または無効なノードを区別するための実装で使用されます。
- 圧縮がない場合、繰り返しのFind操作により構造が長い鎖状になり（最悪の場合O(n)）、性能が劣化します。圧縮により、構造はほぼ平坦になります。

#### Union操作
`x` と `y` の集合を結合するには:
1. ルートを見つける: `rootX = find(x)`, `rootY = find(y)`。
2. `rootX != rootY` の場合、一方をもう一方にリンクします（例: ランクによる - 小さいランクの木を大きいランクの木に接続）。

擬似コード:
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
            rank[rootX] += 1  # 新しい親のランクを増加
```

#### アルゴリズムの使用方法
Union-Findは動的接続性問題に理想的です。以下に例を用いたステップバイステップのガイドを示します:

1. **初期化**:
   - サイズ `n`（要素数）の `p[]` を作成: `for i in 0 to n-1: p[i] = -1`（または自己親指定の場合は `i`）。
   - オプション: `rank[]` をすべて0または1に設定。

2. **基本的な使用フロー**:
   - 2つの要素が同じ集合にあるか確認: `if find(a) == find(b)`。
   - 結合: `union(a, b)`。
   - クエリ/結合を任意の順序で処理できます - 動的です！

3. **例: グラフにおける連結成分の検出**
   5つのノード(0-4)と(0-1), (1-2), (3-4)のようなエッジを持つグラフを想像してください。
   ```
   // 初期化
   p = [-1, -1, -1, -1, -1]
   rank = [0, 0, 0, 0, 0]

   // エッジを結合
   union(0, 1)  // 0と1を結合, 例えば p[0]=-1, p[1]=0
   union(1, 2)  // 2を {0,1} に結合, p[2]=0
   union(3, 4)  // {3,4} を結合, 例えば p[3]=-1, p[4]=3

   // クエリ: 0と2は接続されているか? find(0)=0, find(2)=0 → はい
   // 2と3は接続されているか? find(2)=0, find(3)=-1 → いいえ
   ```

4. **実世界での応用例**:
   - **Kruskalの最小全域木**: エッジを重みでソートし、サイクルを形成しないエッジを結合（`find(u) == find(v)` の場合はスキップ）。
   - **ソーシャルネットワークの友達**: 友達を結合し、共通の接続を検索。
   - **画像セグメンテーション**: 類似色の隣接ピクセルを結合。
   - **無向グラフのサイクル検出**: 端点を結合；既に同じ集合にある場合、サイクルが存在。

#### シンプルなPython実装
```python
class UnionFind:
    def __init__(self, n):
        self.p = [-1] * n
        self.rank = [0] * n
    
    def find(self, i):
        if self.p[i] != -1 and self.p[i] != i:  # 番兵 + 自己親の処理
            self.p[i] = self.find(self.p[i])  # 経路圧縮
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

# 使用例
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print(uf.find(0) == uf.find(2))  # True
```

これにより効率性が保たれます - より大きな `n` で試して速度を確認してください！

さらに深く学びたい場合は、[GeeksforGeeks: Union-Find Algorithm](https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank-and-path-compression/) や [CP-Algorithms: DSU](https://cp-algorithms.com/data_structures/disjoint_set_union.html) をチェックしてください。