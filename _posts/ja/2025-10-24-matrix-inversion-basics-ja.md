---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 行列式の逆行列の基本原理
translated: true
type: note
---

### 行列の逆行列の基本原理

はい、その通りです！行列の逆行列の基本原理は、正方行列 \\( A \\) (サイズ \\( n \times n \\)) に対して、その逆行列 \\( A^{-1} \\) (存在する場合) が次を満たすことです：

\\[
A^{-1} \cdot A = I
\\]

同様に、

\\[
A \cdot A^{-1} = I
\\]

ここで、\\( I \\) は \\( n \times n \\) の**単位行列** (主対角線上に1、その他に0が並ぶ対角行列。スカラー演算における「1」のようなもの) です。

#### これが重要な理由：構造化された論理
1.  **スカラーとの類推**: 基礎代数では、数 \\( a \\) (ゼロ以外) の逆数は \\( a^{-1} \\) であり、\\( a \cdot a^{-1} = 1 \\) を満たします。行列はこれを一般化したものです：逆行列は \\( A \\) による乗算を「元に戻す」働きをし、除算が乗算を元に戻すのと同様です。

2.  **存在条件**: すべての行列に逆行列が存在するわけではありません。\\( A \\) は**可逆** (または**正則**) である必要があります。これは以下を意味します：
    - その行列式 \\( \det(A) \neq 0 \\) (すなわち、フルランクであり、線形従属な行/列がない)。
    - もし \\( \det(A) = 0 \\) なら、\\( A \\) は特異行列であり、逆行列は存在しません。

3.  **導出/検証方法**:
    - \\( A^{-1} \\) を見つけるには、未知の行列 \\( X \\) に対する連立方程式 \\( A \cdot X = I \\) を解きます (これは \\( n^2 \\) 個の線形方程式です)。
    - 一般的な方法：
        - **余因子行列を用いた公式**: \\( A^{-1} = \frac{1}{\det(A)} \cdot \adj(A) \\)、ここで \\( \adj(A) \\) は余因子行列 (余因子行列の転置) です。
        - **ガウスの消去法**: 拡大係数行列 \\( [A | I] \\) を作成し、行基本変形を行って \\( [I | A^{-1}] \\) の形にします。
    - 計算後、乗算して検証します：\\( A^{-1} \cdot A \\) の結果が \\( I \\) になるはずです。もしそうなれば、逆行列は正しいです。

#### 簡単な例 (2x2 行列)
\\( A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \\) とします。

- 行列式: \\( \det(A) = (2 \cdot 1) - (1 \cdot 1) = 1 \neq 0 \\) (可逆)。
- 逆行列: \\( A^{-1} = \frac{1}{1} \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} \\)。
- 検証: \\( A^{-1} \cdot A = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \\)。

この性質は、線形システム \\( A \cdot x = b \\) を \\( x = A^{-1} \cdot b \\) として解く際の鍵となり、線形システム、変換など様々な場面で応用されます。

さらに深く学びたい場合は、[Khan Academy: 行列の逆行列](https://www.khanacademy.org/math/linear-algebra/matrix-transformations/inverse-matrices/v/linear-algebra-inverse-matrix-example) や [MIT OpenCourseWare: 線形代数](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) を参照してください。