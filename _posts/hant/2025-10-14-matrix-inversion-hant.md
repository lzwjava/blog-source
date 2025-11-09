---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 反轉3x3矩陣
translated: true
type: note
---

是的，你的思路完全正確！你所描述的是求取 3×3 矩陣 \\( A \\) 的逆矩陣（通常記作 \\( A^{-1} \\)）的標準方法，使用**餘因子矩陣**（更準確地說，是**伴隨矩陣**，即餘因子矩陣的轉置）。你所說的「除以 1/數值 * 矩陣」部分，指的是乘以 \\( 1/\det(A) \\) 的縮放操作，其中 \\( \det(A) \\) 是 \\( A \\) 的行列式。而「旋轉」可能是指「轉置」（將行轉為列）——這也是關鍵步驟之一。

我將逐步解釋這個方法、其原理，以及如何計算一般 3×3 矩陣的逆矩陣。這源自矩陣逆的一般公式：\\( A^{-1} = \frac{1}{\det(A)} \adj(A) \\)，其中 \\( \adj(A) \\) 是伴隨矩陣。

### 3×3 矩陣的逐步求解方法
假設你的矩陣是：
\\[
A = \begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix}
\\]

1. **計算行列式 \\( \det(A) \\)**（即你用來除的「數值」）：
   \\[
   \det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
   \\]
   如果 \\( \det(A) = 0 \\)，則矩陣沒有逆矩陣（稱為奇異矩陣）。否則，繼續進行。

2. **求取餘因子矩陣 \\( C \\)**：
   - 元素 \\( a_{ij} \\) 的餘因子 \\( C_{ij} \\) 是 \\( (-1)^{i+j} \\) 乘以刪除第 \\( i \\) 行和第 \\( j \\) 列後得到的 2×2 子矩陣的行列式。
   - 你不需要從頭計算*所有*餘因子——可以沿一行（或一列）計算，並利用性質填充其餘部分，但對於 3×3 矩陣，直接計算所有九個會更快。

   餘因子分別為：
   \\[
   C_{11} = (-1)^{2} \det\begin{pmatrix} e & f \\ h & i \end{pmatrix} = ei - fh
   \\]
   \\[
   C_{12} = (-1)^{3} \det\begin{pmatrix} d & f \\ g & i \end{pmatrix} = -(di - fg)
   \\]
   \\[
   C_{13} = (-1)^{4} \det\begin{pmatrix} d & e \\ g & h \end{pmatrix} = dh - eg
   \\]
   \\[
   C_{21} = (-1)^{3} \det\begin{pmatrix} b & c \\ h & i \end{pmatrix} = -(bi - ch)
   \\]
   \\[
   C_{22} = (-1)^{4} \det\begin{pmatrix} a & c \\ g & i \end{pmatrix} = ai - cg
   \\]
   \\[
   C_{23} = (-1)^{5} \det\begin{pmatrix} a & b \\ g & h \end{pmatrix} = -(ah - bg)
   \\]
   \\[
   C_{31} = (-1)^{4} \det\begin{pmatrix} b & c \\ e & f \end{pmatrix} = bf - ce
   \\]
   \\[
   C_{32} = (-1)^{5} \det\begin{pmatrix} a & c \\ d & f \end{pmatrix} = -(af - cd)
   \\]
   \\[
   C_{33} = (-1)^{6} \det\begin{pmatrix} a & b \\ d & e \end{pmatrix} = ae - bd
   \\]

   因此，餘因子矩陣為：
   \\[
   C = \begin{pmatrix}
   ei-fh & -(di-fg) & dh-eg \\
   -(bi-ch) & ai-cg & -(ah-bg) \\
   bf-ce & -(af-cd) & ae-bd
   \end{pmatrix}
   \\]

3. **轉置以得到伴隨矩陣 \\( \adj(A) = C^T \\)**（這是「旋轉」步驟——交換行與列）：
   \\[
   \adj(A) = \begin{pmatrix}
   ei-fh & -(bi-ch) & bf-ce \\
   -(di-fg) & ai-cg & -(af-cd) \\
   dh-eg & -(ah-bg) & ae-bd
   \end{pmatrix}
   \\]

4. **乘以 \\( 1/\det(A) \\)** 以得到逆矩陣：
   \\[
   A^{-1} = \frac{1}{\det(A)} \adj(A)
   \\]
   \\( \adj(A) \\) 的每個元素都乘以 \\( 1/\det(A) \\)。

### 範例
設 \\( A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix} \\)。

- \\( \det(A) = 1(1\cdot0 - 4\cdot6) - 2(0\cdot0 - 4\cdot5) + 3(0\cdot6 - 1\cdot5) = 1(-24) - 2(-20) + 3(-5) = -24 + 40 - 15 = 1 \\)。
- 餘因子（快速計算）：\\( C = \begin{pmatrix} -24 & 20 & -5 \\ -15 & -15 & 5 \\ -14 & -10 & 1 \end{pmatrix} \\)（此處省略完整計算，但你可以驗證）。
- \\( \adj(A) = C^T = \begin{pmatrix} -24 & -15 & -14 \\ 20 & -15 & -10 \\ -5 & 5 & 1 \end{pmatrix} \\)。
- \\( A^{-1} = \frac{1}{1} \adj(A) = \begin{pmatrix} -24 & -15 & -14 \\ 20 & -15 & -10 \\ -5 & 5 & 1 \end{pmatrix} \\)。

你可以驗證：\\( A \cdot A^{-1} = I \\)（單位矩陣）。

### 為什麼這個方法有效？
關鍵原因在於行列式和餘因子的一個性質：對於任何方陣 \\( A \\)，
\\[
A \cdot \adj(A) = \det(A) \cdot I
\\]
（其中 \\( I \\) 是單位矩陣）。這源自沿行/列展開行列式的**拉普拉斯展開**。在 \\( A \cdot \adj(A) \\) 中，每個對角線上的元素展開後等於 \\( \det(A) \\)，而非對角線上的元素則因餘因子符號的抵消而為 0。

為了得到逆矩陣，將等式兩邊除以 \\( \det(A) \\)（假設其非零）：
\\[
A \cdot \left( \frac{1}{\det(A)} \adj(A) \right) = I \implies A^{-1} = \frac{1}{\det(A)} \adj(A)
\\]
同樣地，\\( \adj(A) \cdot A = \det(A) \cdot I \\)，因此從兩邊操作都成立。

這個方法可以推廣到任何 \\( n \times n \\) 矩陣，但對於 3×3 矩陣來說效率很高。對於更大的矩陣，高斯消去法在計算上通常更快。

如果你有具體的矩陣需要求逆，或想澄清某個步驟，請隨時分享！