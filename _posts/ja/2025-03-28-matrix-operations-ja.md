---
audio: false
generated: true
lang: ja
layout: post
title: 行列と演算
translated: true
type: note
---

承知しました。以下に、**行列と演算**に関する詳細なチュートリアルを記載します。表記法、種類、および加算、減算、スカラー乗算、行列乗算、転置、逆行列などの演算について説明します。

---

## **1. 行列とその表記法**
**行列**とは、数、記号、または式を行と列に並べた長方形の配列です。行列の一般的な表記法は次のとおりです。

\\[
A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}
\\]

ここで：
- \\( A \\) は \\( m \times n \\) 行列です。
- \\( a_{ij} \\) は **i 行 j 列** の要素を表します。
- \\( m \\) は**行**の数、\\( n \\) は**列**の数です。

### **行列の種類**
#### **1.1 正方行列**
行と列の数が同じ（\\( m = n \\)）場合、その行列は**正方行列**です。

\\[
A = \begin{bmatrix} 2 & -1 \\ 4 & 3 \end{bmatrix}
\\]

#### **1.2 単位行列**
対角要素がすべて **1** で、非対角要素がすべて **0** の正方行列です。

\\[
I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\\]

任意の行列 \\( A \\) に対して、\\( I \\) を乗算しても変化しません。  
\\[
A \cdot I = I \cdot A = A
\\]

#### **1.3 ゼロ行列（零行列）**
すべての要素が**ゼロ**である行列です。

\\[
O = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}
\\]

任意の行列にゼロ行列を乗算すると、結果はゼロ行列になります。

---

## **2. 行列演算**
### **2.1 行列の加算と減算**
同じ次元（\\( m \times n \\)）を持つ2つの行列 \\( A \\) と \\( B \\) について：

\\[
A + B = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}
+
\begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix}
=
\begin{bmatrix} a_{11} + b_{11} & a_{12} + b_{12} \\ a_{21} + b_{21} & a_{22} + b_{22} \end{bmatrix}
\\]

減算の場合は、対応する要素を単純に減算します。

\\[
A - B = \begin{bmatrix} a_{11} - b_{11} & a_{12} - b_{12} \\ a_{21} - b_{21} & a_{22} - b_{22} \end{bmatrix}
\\]

**加算/減算の条件**：
- 行列は**同じ次元**でなければなりません。

---

### **2.2 スカラー乗算**
行列をスカラー（実数 \\( k \\)）で乗算するとは、各要素に \\( k \\) を乗算することを意味します。

\\[
kA = k \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}
=
\begin{bmatrix} k \cdot a_{11} & k \cdot a_{12} \\ k \cdot a_{21} & k \cdot a_{22} \end{bmatrix}
\\]

例：

\\[
3 \times \begin{bmatrix} 1 & -2 \\ 4 & 0 \end{bmatrix}
=
\begin{bmatrix} 3 & -6 \\ 12 & 0 \end{bmatrix}
\\]

---

### **2.3 行列の乗算**
行列の乗算は**要素ごと**ではなく、特別な規則に従います。

#### **2.3.1 乗算の条件**
- \\( A \\) のサイズが \\( m \times n \\) で、\\( B \\) のサイズが \\( n \times p \\) の場合、\\( A \cdot B \\) は定義され、結果は \\( m \times p \\) 行列になります。

#### **2.3.2 行列乗算の公式**
\\[
(A \cdot B)_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
\\]
各要素は、\\( A \\) の対応する行と \\( B \\) の対応する列の**内積**を取ることによって求められます。

#### **計算例**

\\[
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 2 & 0 \\ 1 & 3 \end{bmatrix}
\\]

このとき、

\\[
A \cdot B = \begin{bmatrix} (1 \times 2 + 2 \times 1) & (1 \times 0 + 2 \times 3) \\ (3 \times 2 + 4 \times 1) & (3 \times 0 + 4 \times 3) \end{bmatrix}
\\]

\\[
= \begin{bmatrix} 2 + 2 & 0 + 6 \\ 6 + 4 & 0 + 12 \end{bmatrix} = \begin{bmatrix} 4 & 6 \\ 10 & 12 \end{bmatrix}
\\]

---

## **3. 行列の転置**
行列 \\( A \\) の**転置**は、\\( A^T \\) と表記され、行と列を入れ替えることで得られます。

\\[
A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}
\\]

\\[
A^T = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}
\\]

### **転置の性質**
1. \\( (A^T)^T = A \\)  
2. \\( (A + B)^T = A^T + B^T \\)  
3. \\( (kA)^T = kA^T \\)  
4. \\( (AB)^T = B^T A^T \\)

---

## **4. 行列の逆行列**
正方行列 \\( A \\) の**逆行列**は、\\( A^{-1} \\) と表記され、以下を満たします。

\\[
A A^{-1} = A^{-1} A = I
\\]

### **4.1 逆行列が存在する条件**
- **正方**行列のみが逆行列を持ちます。
- 行列式が**非ゼロ**（\\( \det(A) \neq 0 \\)）でなければなりません。

### **4.2 逆行列の求め方（2×2行列の場合）**
2×2行列の場合：

\\[
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
\\]

逆行列は次の式で与えられます。

\\[
A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
\\]

ここで、\\( \det(A) = ad - bc \\) です。

例：

\\[
A = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix}, \quad \det(A) = (4 \times 6) - (7 \times 2) = 24 - 14 = 10
\\]

\\[
A^{-1} = \frac{1}{10} \begin{bmatrix} 6 & -7 \\ -2 & 4 \end{bmatrix} = \begin{bmatrix} 0.6 & -0.7 \\ -0.2 & 0.4 \end{bmatrix}
\\]

---

これは線形代数における**行列と演算の基礎**を網羅しています。追加の例や説明が必要でしたら、お知らせください。😊