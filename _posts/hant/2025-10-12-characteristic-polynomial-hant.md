---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 特徵多項式定義與性質
translated: true
type: note
---

在線性代數中，**特徵多項式**是一個方陣 \\( A \\)（大小為 \\( n \times n \\)）的多項式，它編碼了該矩陣特徵值的資訊。其定義為：

\\[
p(\lambda) = \det(A - \lambda I)
\\]

其中：
- \\( A \\) 是 \\( n \times n \\) 矩陣。
- \\( \lambda \\) 是一個純量（多項式的變數）。
- \\( I \\) 是 \\( n \times n \\) 單位矩陣。
- \\( \det \\) 表示行列式。

### 主要特性
1. **形式**：特徵多項式是一個首一多項式，其次數為 \\( n \\)，這意味著其首項係數（對應 \\( \lambda^n \\) 項）為 1。
   - 對於一個 \\( 2 \times 2 \\) 矩陣 \\( A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \\)，其特徵多項式為：
     \\[
     p(\lambda) = \det \begin{bmatrix} a - \lambda & b \\ c & d - \lambda \end{bmatrix} = \lambda^2 - (a + d)\lambda + (ad - bc)
     \\]
     其中 \\( a + d \\) 是跡數，而 \\( ad - bc \\) 是行列式。

2. **特徵值**：特徵多項式 \\( p(\lambda) = 0 \\) 的根即為矩陣 \\( A \\) 的特徵值。這些特徵值可以是實數或複數。

3. **係數**：多項式的係數與矩陣的性質相關：
   - \\( \lambda^{n-1} \\) 的係數為 \\( -\text{trace}(A) \\)。
   - 常數項為 \\( (-1)^n \det(A) \\)。
   - 其他係數由 \\( A \\) 的主子式之和決定。

4. **不變性**：特徵多項式在相似變換下保持不變。如果 \\( B = P^{-1}AP \\)，則 \\( A \\) 和 \\( B \\) 具有相同的特徵多項式。

5. **Cayley-Hamilton 定理**：矩陣 \\( A \\) 滿足其自身的特徵多項式，即如果 \\( p(\lambda) \\) 是特徵多項式，則 \\( p(A) = 0 \\)（零矩陣）。

### 範例
對於矩陣 \\( A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \\)：
- 計算 \\( A - \lambda I = \begin{bmatrix} 1 - \lambda & 2 \\ 3 & 4 - \lambda \end{bmatrix} \\)。
- 特徵多項式為：
  \\[
  p(\lambda) = \det \begin{bmatrix} 1 - \lambda & 2 \\ 3 & 4 - \lambda \end{bmatrix} = (1 - \lambda)(4 - \lambda) - (2)(3) = \lambda^2 - 5\lambda + 4 - 6 = \lambda^2 - 5\lambda - 2
  \\]
- 通過解 \\( \lambda^2 - 5\lambda - 2 = 0 \\) 即可求得特徵值。

### 應用
- **特徵值計算**：解 \\( p(\lambda) = 0 \\) 可得特徵值。
- **矩陣性質**：有助於判斷矩陣是否可對角化、可逆性及其他性質。
- **微分方程**：用於線性微分方程組中求解。

如果你需要具體範例或進一步細節，請告訴我！