---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 3x3行列の逆行列
translated: true
type: note
---

はい、あなたは正しい道を進んでいます！あなたが説明しているのは、**余因子行列**（より正確には、余因子行列の転置である**随伴行列**）を使用して3×3行列 \\( A \\)（しばしば \\( A^{-1} \\) と表記される）の逆行列を求める標準的な方法です。「1/値 * 行列で割る」という部分は、\\( 1/\det(A) \\) によるスケーリングを指しており、ここで \\( \det(A) \\) は \\( A \\) の行列式です。そして「回転(rorate)」はおそらく「転置(transpose)」（行と列を入れ替えること）を意味しているのでしょう。これも重要なステップです。

この方法を一般的な3×3行列に対して、段階的に説明し、なぜそれが機能するのか、そしてどのように計算するのかを説明します。これは、逆行列の一般公式 \\( A^{-1} = \frac{1}{\det(A)} \adj(A) \\) から来ています。ここで、\\( \adj(A) \\) は随伴行列です。

### 3×3行列に対する段階的な方法
行列が以下のように与えられるとします：
\\[
A = \begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix}
\\]

1.  **行列式 \\( \det(A) \\) を計算する**（割り算に使う「値」）：
    \\[
    \det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
    \\]
    \\( \det(A) = 0 \\) の場合、行列は逆行列を持ちません（特異行列です）。それ以外の場合は続行します。

2.  **余因子行列 \\( C \\) を求める**：
    - 要素 \\( a_{ij} \\) に対する余因子 \\( C_{ij} \\) は、\\( i \\) 行と \\( j \\) 列を削除して得られる2×2小行列の行列式に \\( (-1)^{i+j} \\) を乗じたものです。
    - *すべての*余因子を最初から計算する必要はありません。1つの行（または列）に沿って計算し、性質を利用して残りを埋めることもできますが、3×3の場合は9つすべてを計算するのが早いです。

    余因子は以下の通りです：
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

    したがって、余因子行列は：
    \\[
    C = \begin{pmatrix}
    ei-fh & -(di-fg) & dh-eg \\
    -(bi-ch) & ai-cg & -(ah-bg) \\
    bf-ce & -(af-cd) & ae-bd
    \end{pmatrix}
    \\]

3.  **転置して随伴行列 \\( \adj(A) = C^T \\) を得る**（これが「回転(rorate)」のステップ、つまり行と列を入れ替えること）：
    \\[
    \adj(A) = \begin{pmatrix}
    ei-fh & -(bi-ch) & bf-ce \\
    -(di-fg) & ai-cg & -(af-cd) \\
    dh-eg & -(ah-bg) & ae-bd
    \end{pmatrix}
    \\]

4.  **\\( 1/\det(A) \\) でスケーリングして逆行列を得る**：
    \\[
    A^{-1} = \frac{1}{\det(A)} \adj(A)
    \\]
    \\( \adj(A) \\) の各要素に \\( 1/\det(A) \\) が乗算されます。

### 例
\\( A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix} \\) とします。

- \\( \det(A) = 1(1\cdot0 - 4\cdot6) - 2(0\cdot0 - 4\cdot5) + 3(0\cdot6 - 1\cdot5) = 1(-24) - 2(-20) + 3(-5) = -24 + 40 - 15 = 1 \\)。
- 余因子（簡潔に）： \\( C = \begin{pmatrix} -24 & 20 & -5 \\ -15 & -15 & 5 \\ -14 & -10 & 1 \end{pmatrix} \\)（ここでは完全な計算は省略しますが、検証できます）。
- \\( \adj(A) = C^T = \begin{pmatrix} -24 & -15 & -14 \\ 20 & -15 & -10 \\ -5 & 5 & 1 \end{pmatrix} \\)。
- \\( A^{-1} = \frac{1}{1} \adj(A) = \begin{pmatrix} -24 & -15 & -14 \\ 20 & -15 & -10 \\ -5 & 5 & 1 \end{pmatrix} \\)。

確認できます： \\( A \cdot A^{-1} = I \\)（単位行列）。

### なぜこれが機能するのか？
その主な理由は、行列式と余因子の性質にあります：任意の正方行列 \\( A \\) に対して、
\\[
A \cdot \adj(A) = \det(A) \cdot I
\\]
（ここで \\( I \\) は単位行列です）。これは、行/列に沿った**ラプラス展開**から来ています。\\( A \cdot \adj(A) \\) の各要素は、対角線上では \\( \det(A) \\) に等しく、それ以外の場所では0になる和に展開されます（非対角項は余因子の符号によって打ち消されるため）。

逆行列を得るには、両辺を \\( \det(A) \\) で割ります（それが非ゼロであると仮定して）：
\\[
A \cdot \left( \frac{1}{\det(A)} \adj(A) \right) = I \implies A^{-1} = \frac{1}{\det(A)} \adj(A)
\\]
同様に、\\( \adj(A) \cdot A = \det(A) \cdot I \\) も成り立つので、両側から機能します。

この方法は任意の \\( n \times n \\) 行列に一般化できますが、3×3の場合は効率的です。より大きな行列の場合、計算上はガウスの消去法の方が高速なことが多いです。

逆行列を求めたい特定の行列がある場合、またはステップを明確にしたい場合は、それを共有してください！