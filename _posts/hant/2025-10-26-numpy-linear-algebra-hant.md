---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: NumPy 線性代數便攜指南
translated: true
type: note
---

作為你的工程導向導師，本指南在先前明確索引公式的基礎上，整合了實用的 NumPy 示範，透過 `import numpy as np` 和 `np.linalg` 實現。所有數學運算仍可使用索引驗證（例如 \\( A = [a_{ij}]_{i=1}^2, j=1^2 \\)）；程式碼使用明確陣列以確保清晰度。輸出皆來自驗證過的執行結果（例如對於 \\( A = \begin{pmatrix} a_{11}=1 & a_{12}=2 \\ a_{21}=3 & a_{22}=4 \end{pmatrix} \\)，\\( B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} \\)）。在考試準備中，可利用這些進行快速計算——重點在於將輸出結果與公式對照解讀。

## 1. 矩陣運算
數學公式如前：\\( (AB)_{ij} = \sum_{k=1}^2 a_{ik} b_{kj} \\)，等等。

**NumPy 示範**：
```python
import numpy as np
A = np.array([[1, 2], [3, 4]], dtype=float)
B = np.array([[5, 6], [7, 8]], dtype=float)
```
- 加法：`A + B` 得到 \\( \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix} \\)（逐項 \\( a_{ij} + b_{ij} \\)）。
- 純量乘法：`2 * A` 得到 \\( \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix} \\)（\\( c a_{ij} \\)）。
- 矩陣乘法：`A @ B`（或 `np.dot(A, B)`）得到 \\( \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix} \\)（驗證：第1列第1行總和 \\( 1\cdot5 + 2\cdot7 = 19 \\)）。注意不可交換性：`np.allclose(A @ B, B @ A)` 為 `False`。
- 轉置：`A.T` 得到 \\( \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} \\)（\\( (A^T)_{ij} = a_{ji} \\)）。
- 逆矩陣：`np.linalg.inv(A)` 得到 \\( \begin{pmatrix} -2 & 1 \\ 1.5 & -0.5 \end{pmatrix} \\)（驗證：`A @ inv_A` ≈ \\( I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \\)，有微小浮點誤差 ~1e-16）。

## 2. 行列式
數學：\\( \det A = \sum_{j=1}^2 a_{1j} C_{1j} \\)，\\( C_{1j} = (-1)^{1+j} \det(M_{1j}) \\)（例如，\\( M_{11} = [4] \\)，所以 \\( C_{11} = 4 \\)；完整 \\( \det A = 1\cdot4 - 2\cdot3 = -2 \\)）。

**NumPy 示範**（續上）：
- `np.linalg.det(A)`：-2.0（符合公式；浮點精度 -2.0000000000000004）。
- 乘積：`np.linalg.det(A @ B)` = 4.0；`det_A * np.linalg.det(B)` ≈ 4.0（驗證 \\( \det(AB) = \det A \cdot \det B \\)）。
- 轉置：`np.linalg.det(A.T)` = -2.0（驗證 \\( \det(A^T) = \det A \\)）。

關於伴隨矩陣/逆矩陣連結：逆矩陣在分母中使用行列式，如公式 \\( A^{-1} = \frac{1}{\det A} \adj A \\)。

## 3. 線性系統與高斯消去法
數學：增廣矩陣 \\( [A | b] \\)，其中 \\( b = [b_i]_{i=1}^2 = [5, 11]^T \\)；在化為階梯形式後透過回代求解。

**NumPy 示範**：
- `np.linalg.solve(A, b)` 得到 [1. 2.]（精確解：\\( x_1 = \frac{\det A_1}{\det A} \\)，其中 \\( A_1 \\) 是將第1行與 b 交換，行列式 = -2 相同；驗證克拉瑪公式）。
- 檢查：`A @ x` = [5. 11.]（殘差為 0）。
- 秩：`np.linalg.matrix_rank(A)` = 2（滿秩；對於奇異矩陣，秩 < 2 表示無限解或無解）。

NumPy 的 `solve` 在內部執行類似 LU 分解的運算（無需編寫顯式高斯消去法程式碼；如需自訂，可使用 `scipy.linalg.lu`，但此處建議使用 np.linalg）。

## 4. 向量空間
數學：rank A = 主元數量 = dim Col(A)；nullity = 2 - rank A。

**NumPy 示範**：
- 秩如上所述：2。
- 透過 SVD 估計零維度：`U, S, Vt = np.linalg.svd(A)`；計算奇異值 > 1e-10 的數量：2，所以 nullity = 2 - 2 = 0（Nul(A) = {0}）。對於基底，零空間向量來自具有小奇異值的 Vt 列。

## 5. 線性變換
數學：T(x)_i = \\( \sum_j a_{ij} x_j \\)；矩陣表示為 A。

**NumPy 關聯**：與矩陣運算相同；例如，`T_x = A @ x` 應用變換（向量化）。

## 6. 特徵值
數學：求解 det(A - λ I) = 0，(A - λ I)_{ij} = a_{ij} - λ δ_{ij}；然後求解 (A - λ I) v = 0 得到 v_j。

**NumPy 示範**：
- `eigvals, eigvecs = np.linalg.eig(A)`：eigvals ≈ [-0.372, 5.372]（λ² - tr(A)λ + det A = λ² - 5λ -2 =0 的根）。
- 特徵向量列：例如，col0 ≈ [-0.825, 0.566]^T 對應 λ≈-0.372。
- 檢查：`A @ eigvecs[:,0]` ≈ λ eigvecs[:,0]（縮放驗證：`A @ eigvecs[:,0] / eigvals[0]` 符合 eigvecs[:,0]）。

對於可對角化：滿秩特徵向量（det ≠0）。

## 7. 內積與正交化
數學：<u,v> = \\( \sum_i u_i v_i \\)；投影 = (<v,w>/<w,w>) w（對 w_i 的純量乘法）。

**NumPy 示範**（u=[1,2], v=[3,4]）：
- `np.dot(u, v)` = 11（或 `u @ v`）。
- `np.linalg.norm(u)` ≈ 2.236（√<u,u>）。

Gram-Schmidt：對矩陣 V（列作為基底向量）使用 `np.linalg.qr(V)`；Q = 正交歸一。
- 範例 V = \\( \begin{pmatrix} 3 & 0 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix} \\)（列 v^{(1)}=[3,1,0]^T，等等）。
- `ortho = np.linalg.qr(V)[0]` 得到 ≈ \\( \begin{pmatrix} -0.949 & -0.316 & 0 \\ -0.316 & 0.949 & 0 \\ 0 & 0 & 1 \end{pmatrix} \\)（符號翻轉無妨）。
- 檢查：`np.allclose(ortho.T @ ortho, np.eye(3))` = True（δ_{ij}）。

二次形式：`u @ A @ u` = 27.0（x^T A x，其中 x_i = u_i；對於正定，所有特徵值 >0——此處符號混合）。

**快速驗證提示**：對於浮點數，一律使用 `np.allclose`；對於小規模 n，手動進行列簡化，然後與 `solve` 或 `eig` 比對。練習：替換為你自己的 3×3 矩陣。

[NumPy linalg 文件](https://numpy.org/doc/stable/reference/routines.linalg.html)  
[NumPy 中的線性代數 - SciPy 講義](https://scipy-lectures.org/intro/numpy/auto_examples/plot_linear_algebra.html)