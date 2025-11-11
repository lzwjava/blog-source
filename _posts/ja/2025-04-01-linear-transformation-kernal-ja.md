---
audio: false
generated: true
lang: ja
layout: post
title: 線形変換の核
translated: true
type: note
---

線形変換の**カーネル**（核）とは、その変換によってゼロベクトルに写されるすべての入力ベクトルの集合です。

### 定義：
\\( T: V \to W \\) が2つのベクトル空間 \\( V \\) と \\( W \\) の間の線形変換であるとき、\\( T \\) の**カーネル**（または**零空間**）は以下で定義されます：

\\[
\ker(T) = \{ v \in V \mid T(v) = 0 \}
\\]

### 主な性質：
1. **部分空間**: 線形変換のカーネルは、常に定義域 \\( V \\) の部分空間です。
2. **次元**: カーネルの次元は、変換の**退化次数** (nullity) と呼ばれます。
3. **単射性との関係**:
   - \\( \ker(T) = \{0\} \\) ならば、\\( T \\) は**単射**（一対一）です。
   - \\( \ker(T) \\) の次元が0より大きいならば、\\( T \\) は単射ではありません。

### 例：
行列変換 \\( T: \mathbb{R}^3 \to \mathbb{R}^2 \\) を考えます。この変換は以下で与えられます：

\\[
T(x, y, z) = (x + y, y + z)
\\]

これを行列で表すと、

<div>
$$
T \begin{bmatrix} x \\ y \\ z \end{bmatrix} =
\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
$$
</div>

カーネルを求めるには、次の方程式を解きます：

\\[
\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
\\]

これにより、次の連立方程式が得られます：

\\[
x + y = 0
\\]
\\[
y + z = 0
\\]

\\( x, y, z \\) について解くと：

\\[
x = -y, \quad z = -y
\\]

したがって、カーネルは次の形式のすべてのベクトルからなります：

<div>
$$
\ker(T) = \text{span} \left\{ \begin{bmatrix} -1 \\ 1 \\ -1 \end{bmatrix} \right\}
$$
</div>

これは \\( \mathbb{R}^3 \\) の一次元部分空間です。

さらに説明が必要な場合はお知らせください！