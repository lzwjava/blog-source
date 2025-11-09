---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 特性多項式の定義と性質
translated: true
type: note
---

線形代数において、**特性多項式**は正方行列 \\( A \\)（サイズ \\( n \times n \\)）の固有値に関する情報を符号化する多項式です。以下のように定義されます：

\\[
p(\lambda) = \det(A - \lambda I)
\\]

ここで：
- \\( A \\) は \\( n \times n \\) 行列です。
- \\( \lambda \\) はスカラー（多項式の変数）です。
- \\( I \\) は \\( n \times n \\) 単位行列です。
- \\( \det \\) は行列式を表します。

### 主な特性
1. **形式**: 特性多項式は次数 \\( n \\) のモニック多項式であり、すなわち \\( \lambda^n \\) の項の係数が 1 です。
   - \\( 2 \times 2 \\) 行列 \\( A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \\) の場合、特性多項式は：
     \\[
     p(\lambda) = \det \begin{bmatrix} a - \lambda & b \\ c & d - \lambda \end{bmatrix} = \lambda^2 - (a + d)\lambda + (ad - bc)
     \\]
     ここで、\\( a + d \\) はトレース、\\( ad - bc \\) は行列式です。

2. **固有値**: 特性多項式 \\( p(\lambda) = 0 \\) の根が行列 \\( A \\) の固有値です。これらは実数または複素数となります。

3. **係数**: 多項式の係数は行列の性質と関連しています：
   - \\( \lambda^{n-1} \\) の係数は \\( -\text{trace}(A) \\) です。
   - 定数項は \\( (-1)^n \det(A) \\) です。
   - その他の係数は \\( A \\) の主小行列式の和によって決まります。

4. **不変性**: 特性多項式は相似変換に対して不変です。もし \\( B = P^{-1}AP \\) ならば、\\( A \\) と \\( B \\) は同じ特性多項式を持ちます。

5. **Cayley-Hamilton の定理**: 行列 \\( A \\) は自身の特性多項式を満たします。すなわち、\\( p(\lambda) \\) が特性多項式ならば、\\( p(A) = 0 \\)（零行列）が成り立ちます。

### 例
行列 \\( A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \\) の場合：
- \\( A - \lambda I = \begin{bmatrix} 1 - \lambda & 2 \\ 3 & 4 - \lambda \end{bmatrix} \\) を計算します。
- 特性多項式は：
  \\[
  p(\lambda) = \det \begin{bmatrix} 1 - \lambda & 2 \\ 3 & 4 - \lambda \end{bmatrix} = (1 - \lambda)(4 - \lambda) - (2)(3) = \lambda^2 - 5\lambda + 4 - 6 = \lambda^2 - 5\lambda - 2
  \\]
- 固有値は \\( \lambda^2 - 5\lambda - 2 = 0 \\) を解くことで求められます。

### 応用
- **固有値計算**: \\( p(\lambda) = 0 \\) を解くことで固有値が得られます。
- **行列の性質**: 対角化可能性、正則性などの性質の判定に役立ちます。
- **微分方程式**: 線形微分方程式系の解を求めるために使用されます。

特定の例や詳細な情報が必要な場合は、お知らせください！