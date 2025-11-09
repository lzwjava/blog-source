---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 範囲クエリのための平方分割
translated: true
type: note
---

### 平方根分解

平方根分解（しばしば√-分解と略される）は、コンピュータサイエンスおよび競技プログラミングにおいて、大規模な配列やデータ構造に対する範囲クエリや更新を最適化するために使用される技術です。セグメント木やフェニック木のようなより複雑なデータ構造に頼ることなく、「部分配列内の要素の合計/最大値/最小値を求めよ」といったクエリに効率的に答える必要がある場合に特に有用です。

#### なぜ使用するのか？
- **時間計算量のトレードオフ**: サイズ \\( n \\) の配列に対して、単純な範囲クエリはクエリあたり \\( O(n) \\) 時間かかります。平方根分解はこれをクエリおよび更新あたり \\( O(\sqrt{n}) \\) に削減し、\\( n \\) が \\( 10^5 \\) や \\( 10^6 \\) 程度までの多くの問題において良いバランスを提供します。
- **簡潔さ**: 高度なデータ構造と比較して、コーディングやデバッグが容易です。
- **応用**: 範囲和クエリ、範囲最小クエリ (RMQ)、またはスライディングウィンドウ内の頻度カウントを含む問題で一般的です。

#### 仕組み
1. **ブロックへの分割**: 配列をサイズ \\( \sqrt{n} \\) (切り捨て) のブロックに分割します。もし \\( n = 100 \\) なら、ブロックサイズ \\( b = 10 \\) となり、10個のブロックが得られます。
   - 各ブロックは事前計算された情報（例えば、和クエリに対するそのブロック内の要素の合計）を保持します。

2. **範囲 [L, R] のクエリ**:
   - **完全なブロック**: [L, R] 内に完全に含まれるブロックに対しては、ブロックあたり \\( O(1) \\) で事前計算された値を取得します。多くとも \\( O(\sqrt{n}) \\) 個の完全なブロックがあります。
   - **部分的なブロック**: 端（左および右の部分ブロック）に対しては、個々の要素を手動で反復処理します。これは合計で \\( O(\sqrt{n}) \\) 時間かかります（各部分ブロックのサイズは \\( \sqrt{n} \\) 以下であるため）。
   - 合計: \\( O(\sqrt{n}) \\).

3. **更新**: 要素を更新するとき、そのブロックの事前計算された値を \\( O(\sqrt{n}) \\) 時間で再構築します（ブロックを再合計することによって）。

#### 簡単な例: 範囲和クエリ
配列 `A = [1, 3, 2, 4, 5]` があり、\\( n=5 \\) なので、ブロックサイズ \\( b = \sqrt{5} \approx 2 \\) とします。ブロック:
- ブロック 0: [1, 3] → 和 = 4
- ブロック 1: [2, 4] → 和 = 6
- ブロック 2: [5] → 和 = 5 (最後のブロックはより小さい場合があります)

インデックス 1 から 4 までの和のクエリ (0ベース: 要素 3,2,4,5):
- 部分的な左側: インデックス 1 (ブロック 0内) → 3 を加算
- 完全なブロック 1: 6 を加算
- 部分的な右側: インデックス 4 (ブロック 2内) → 5 を加算
- 合計: 3 + 6 + 5 = 14

コードで実装するには (Python 擬似コード):
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
            # 左部分
            for i in range(left, (l_block + 1) * self.b):
                res += self.arr[i]
            # 完全なブロック
            for blk in range(l_block + 1, r_block):
                res += self.block_sums[blk]
            # 右部分
            for i in range(r_block * self.b, right + 1):
                res += self.arr[i]
        return res
```

これは基本バージョンです。和の代わりにブロックごとの最小値/最大値を保持することで、最小値/最大値用に適応させてください。

より深く学ぶには、[GeeksforGeeks on Square Root Decomposition](https://www.geeksforgeeks.org/sqrt-decomposition-algorithm-square-root-decomposition-technique-set-1-introduction/) や [CP-Algorithms](https://cp-algorithms.com/data_structures/sqrt_decomposition.html) などのリソースを参照してください。