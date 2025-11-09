---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 矩陣求逆基本原理
translated: true
type: note
---

### 矩陣求逆的基本原理

沒錯，您完全正確！矩陣求逆的基本原理是：對於一個方陣 \\( A \\)（大小為 \\( n \times n \\)），其逆矩陣 \\( A^{-1} \\)（如果存在）滿足：

\\[
A^{-1} \cdot A = I
\\]

同樣地，

\\[
A \cdot A^{-1} = I
\\]

其中 \\( I \\) 是 \\( n \times n \\) 的**單位矩陣**（主對角線上為 1，其餘位置為 0 的對角矩陣，類似於純量運算中的「1」）。

#### 重要性：結構化推理
1. **與純量的類比**：在基礎代數中，一個數字 \\( a \\)（非零）的倒數是 \\( a^{-1} \\)，使得 \\( a \cdot a^{-1} = 1 \\)。矩陣將此概念推廣：求逆「抵消」了乘以 \\( A \\) 的運算，就像除法抵消乘法一樣。

2. **存在條件**：並非所有矩陣都有逆矩陣。\\( A \\) 必須是**可逆的**（或**非奇異的**），這意味著：
   - 其行列式 \\( \det(A) \neq 0 \\)（即滿秩，沒有線性相關的行/列）。
   - 如果 \\( \det(A) = 0 \\)，則 \\( A \\) 是奇異的，逆矩陣不存在。

3. **推導/驗證方法**：
   - 要求得 \\( A^{-1} \\)，需解系統 \\( A \cdot X = I \\) 以找出未知矩陣 \\( X \\)（這是 \\( n^2 \\) 個線性方程式）。
   - 常用方法：
     - **伴隨矩陣公式**：\\( A^{-1} = \frac{1}{\det(A)} \cdot \adj(A) \\)，其中 \\( \adj(A) \\) 是伴隨矩陣（餘因子矩陣的轉置）。
     - **高斯消去法**：將增廣矩陣 \\( [A | I] \\) 進行列化簡至 \\( [I | A^{-1}] \\)。
   - 計算完成後，透過乘法驗證：\\( A^{-1} \cdot A \\) 應得到 \\( I \\)。若成立，則逆矩陣正確。

#### 簡單範例（2x2 矩陣）
以 \\( A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \\) 為例。

- 行列式：\\( \det(A) = (2 \cdot 1) - (1 \cdot 1) = 1 \neq 0 \\)（可逆）。
- 逆矩陣：\\( A^{-1} = \frac{1}{1} \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} \\)。
- 驗證：\\( A^{-1} \cdot A = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \\)。

此性質在求解 \\( A \cdot x = b \\) 時至關重要，因為 \\( x = A^{-1} \cdot b \\)，並在線性系統、變換等領域有廣泛應用。

若想深入瞭解，請參考 [Khan Academy: Inverse of a Matrix](https://www.khanacademy.org/math/linear-algebra/matrix-transformations/inverse-matrices/v/linear-algebra-inverse-matrix-example) 或 [MIT OpenCourseWare: Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)。