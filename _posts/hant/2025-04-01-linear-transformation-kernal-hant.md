---
audio: false
generated: true
lang: hant
layout: post
title: 線性轉換的核心
translated: true
type: note
---

**線性轉換的核**是指所有被轉換映射至零向量的輸入向量所構成的集合。

### 定義：
若 \\( T: V \to W \\) 是兩個向量空間 \\( V \\) 與 \\( W \\) 之間的線性轉換，則 \\( T \\) 的**核**（或**零空間**）為：

\\[
\ker(T) = \{ v \in V \mid T(v) = 0 \}
\\]

### 關鍵性質：
1. **子空間**：線性轉換的核始終是定義域 \\( V \\) 的一個子空間。
2. **維度**：核的維度稱為轉換的**零維度**。
3. **與單射性的關係**：
   - 若 \\( \ker(T) = \{0\} \\)，則 \\( T \\) 是**單射**（一對一）。
   - 若 \\( \ker(T) \\) 的維度大於零，則 \\( T \\) 不是單射。

### 範例：
考慮矩陣轉換 \\( T: \mathbb{R}^3 \to \mathbb{R}^2 \\)，定義為：

\\[
T(x, y, z) = (x + y, y + z)
\\]

以矩陣形式表示：

<div>
$$
T \begin{bmatrix} x \\ y \\ z \end{bmatrix} =
\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
$$
</div>

為求核，解方程：

\\[
\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
\\]

得到方程組：

\\[
x + y = 0
\\]
\\[
y + z = 0
\\]

解 \\( x, y, z \\)：

\\[
x = -y, \quad z = -y
\\]

因此，核由所有形式如下的向量組成：

<div>
$$
\ker(T) = \text{span} \left\{ \begin{bmatrix} -1 \\ 1 \\ -1 \end{bmatrix} \right\}
$$
</div>

此為 \\( \mathbb{R}^3 \\) 中的一個一維子空間。

如有需要進一步說明，請告知！