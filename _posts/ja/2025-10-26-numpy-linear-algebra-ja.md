---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: NumPy線形代数ポケットガイド
translated: true
type: note
---

あなたのエンジニアリングに特化したチューターとして、このガイドは前回の明示的なインデックス表記を基に、実践的なNumPyデモンストレーションを `import numpy as np` と `np.linalg` を用いて統合します。すべての数学はインデックスで検証可能です（例: \\( A = [a_{ij}]_{i=1}^2, j=1^2 \\)）。コードでは明確さのために明示的な配列を使用します。出力は検証済みの実行結果です（例: \\( A = \begin{pmatrix} a_{11}=1 & a_{12}=2 \\ a_{21}=3 & a_{22}=4 \end{pmatrix} \\), \\( B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} \\)）。試験準備での迅速な計算にこれらを使用してください—公式に対する出力の解釈に集中しましょう。

## 1. 行列演算
数学は前回同様: \\( (AB)_{ij} = \sum_{k=1}^2 a_{ik} b_{kj} \\) など。

**NumPy デモ**:
```python
import numpy as np
A = np.array([[1, 2], [3, 4]], dtype=float)
B = np.array([[5, 6], [7, 8]], dtype=float)
```
- 加算: `A + B` は \\( \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix} \\) を生成 (要素ごとの \\( a_{ij} + b_{ij} \\))。
- スカラー倍: `2 * A` は \\( \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix} \\) を生成 (\\( c a_{ij} \\))。
- 乗算: `A @ B` (または `np.dot(A, B)`) は \\( \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix} \\) を生成 (検証: 行1-列1の和 \\( 1\cdot5 + 2\cdot7 = 19 \\))。非可換性に注意: `np.allclose(A @ B, B @ A)` は `False`。
- 転置: `A.T` は \\( \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} \\) を生成 (\\( (A^T)_{ij} = a_{ji} \\))。
- 逆行列: `np.linalg.inv(A)` は \\( \begin{pmatrix} -2 & 1 \\ 1.5 & -0.5 \end{pmatrix} \\) を生成 (検証: `A @ inv_A` ≈ \\( I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \\), 微小な浮動小数点誤差 ~1e-16 あり)。

## 2. 行列式
数学: \\( \det A = \sum_{j=1}^2 a_{1j} C_{1j} \\), \\( C_{1j} = (-1)^{1+j} \det(M_{1j}) \\) (例: \\( M_{11} = [4] \\), よって \\( C_{11} = 4 \\); 全体で \\( \det A = 1\cdot4 - 2\cdot3 = -2 \\))。

**NumPy デモ** (上記の続き):
- `np.linalg.det(A)`: -2.0 (公式と一致; 浮動小数点精度 -2.0000000000000004)。
- 積: `np.linalg.det(A @ B)` = 4.0; `det_A * np.linalg.det(B)` ≈ 4.0 (\\( \det(AB) = \det A \cdot \det B \\) を検証)。
- 転置: `np.linalg.det(A.T)` = -2.0 (\\( \det(A^T) = \det A \\) を検証)。

余因子行列/逆行列の関連: 逆行列は分母に det を使用。公式 \\( A^{-1} = \frac{1}{\det A} \adj A \\) 通り。

## 3. 線形システムとガウスの消去法
数学: 拡大係数行列 \\( [A | b] \\)、ただし \\( b = [b_i]_{i=1}^2 = [5, 11]^T \\); 階段行列化後の後退代入で解く。

**NumPy デモ**:
- `np.linalg.solve(A, b)` は [1. 2.] を生成 (厳密解: \\( x_1 = \frac{\det A_1}{\det A} \\)、ここで \\( A_1 \\) は1列目を b と交換、det= -2 で同じ; クラメルの公式を検証)。
- チェック: `A @ x` = [5. 11.] (残差 0)。
- 階数: `np.linalg.matrix_rank(A)` = 2 (フルランク; 特異行列の場合、階数 < 2 は解が無限または存在しないことを意味)。

NumPyの`solve`は内部でLU分解のような因数分解を実行 (明示的なガウスの消去法コードは不要; カスタムには `scipy.linalg.lu` を使用するが、ここでは np.linalg に従う)。

## 4. ベクトル空間
数学: rank A = ピボットの数 = dim Col(A); 退化次数 = 2 - rank A。

**NumPy デモ**:
- 階数は上記: 2。
- SVDによる退化次数の推定: `U, S, Vt = np.linalg.svd(A)`; 1e-10より大きい特異値の数を数える: 2, よって退化次数 = 2 - 2 = 0 (Nul(A) = {0})。基底については、小さな S 値に対応する Vt の行から零空間ベクトルを得る。

## 5. 線形変換
数学: T(x)_i = \\( \sum_j a_{ij} x_j \\); 行列表現は A。

**NumPy との関連**: 行列演算と同じ; 例: `T_x = A @ x` は変換を適用 (ベクトル化済み)。

## 6. 固有値
数学: det(A - λ I) = 0 を解く, (A - λ I)_{ij} = a_{ij} - λ δ_{ij}; 次に (A - λ I) v = 0 を v_j について解く。

**NumPy デモ**:
- `eigvals, eigvecs = np.linalg.eig(A)`: eigvals ≈ [-0.372, 5.372] (λ² - tr(A)λ + det A = λ² - 5λ -2 =0 の根)。
- 固有ベクトルの列: 例: λ≈-0.372 に対する col0 ≈ [-0.825, 0.566]^T。
- チェック: `A @ eigvecs[:,0]` ≈ λ eigvecs[:,0] (スケーリング検証: `A @ eigvecs[:,0] / eigvals[0]` が eigvecs[:,0] と一致)。

対角化可能について: フルランクの固有ベクトル (det ≠0)。

## 7. 内積と直交化
数学: <u,v> = \\( \sum_i u_i v_i \\); 射影 = (<v,w>/<w,w>) w (w_i へのスカラー倍)。

**NumPy デモ** (u=[1,2], v=[3,4]):
- `np.dot(u, v)` = 11 (または `u @ v`)。
- `np.linalg.norm(u)` ≈ 2.236 (√<u,u>)。

グラム・シュミット: 行列 V (列を基底ベクトルとする) に対して `np.linalg.qr(V)` を使用; Q = 正規直交。
- 例 V = \\( \begin{pmatrix} 3 & 0 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix} \\) (列 v^{(1)}=[3,1,0]^T, など)。
- `ortho = np.linalg.qr(V)[0]` は ≈ \\( \begin{pmatrix} -0.949 & -0.316 & 0 \\ -0.316 & 0.949 & 0 \\ 0 & 0 & 1 \end{pmatrix} \\) を生成 (符号反転は問題なし)。
- チェック: `np.allclose(ortho.T @ ortho, np.eye(3))` = True (δ_{ij})。

二次形式: `u @ A @ u` = 27.0 (x^T A x、x_i = u_i; 正定値については、すべての固有値 >0—ここでは符号が混在)。

**迅速な検証のヒント**: 浮動小数点数の比較には常に `np.allclose` を使用; 小さな n では手動で行簡約し、その後 `solve` または `eig` と一致するか確認。練習: 自身の 3×3 行列を代入してみてください。

[NumPy linalg ドキュメント](https://numpy.org/doc/stable/reference/routines.linalg.html)  
[NumPy での線形代数 - SciPy 講義ノート](https://scipy-lectures.org/intro/numpy/auto_examples/plot_linear_algebra.html)