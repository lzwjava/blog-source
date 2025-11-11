---
audio: false
generated: true
lang: ja
layout: post
title: 線形変換 — ジェミナイ
translated: true
type: note
---

では、線形変換についての詳細なチュートリアルに深く入り込み、定義、例、行列表現、核、像、単射性や全射性といった性質をカバーしていきます。これは線形代数の基礎的なトピックです。

## 6. 線形変換：詳細チュートリアル

**線形変換** とは、ベクトル空間の間の関数で、ベクトルの加法とスカラー乗法の演算を保存するものです。\\(V\\) と \\(W\\) を同じ体 \\(F\\) (これは実数 \\(\mathbb{R}\\) や複素数 \\(\mathbb{C}\\) の集合であることが多い) 上のベクトル空間とします。

**定義:** 関数 \\(T: V \rightarrow W\\) が、すべてのベクトル \\(\mathbf{u}, \mathbf{v} \in V\\) とすべてのスカラー \\(c \in F\\) に対して以下の2つの性質を満たすとき、線形変換であるといいます：

1.  **加法性:** \\(T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})\\)
2.  **斉次性 (スカラー乗法):** \\(T(c\mathbf{u}) = cT(\mathbf{u})\\)

これら2つの性質は、単一の条件にまとめることができます：
すべての \\(\mathbf{u}, \mathbf{v} \in V\\) とすべてのスカラー \\(c, d \in F\\) に対して、\\(T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})\\)。

**線形性の主な帰結:**

* \\(T(\mathbf{0}_V) = \mathbf{0}_W\\)、ここで \\(\mathbf{0}_V\\) は \\(V\\) のゼロベクトル、\\(\mathbf{0}_W\\) は \\(W\\) のゼロベクトルです。(証明: 任意の \\(\mathbf{u} \in V\\) に対して、\\(T(\mathbf{0}_V) = T(0\mathbf{u}) = 0T(\mathbf{u}) = \mathbf{0}_W\\))。
* \\(T(-\mathbf{u}) = -T(\mathbf{u})\\)。(証明: \\(T(-\mathbf{u}) = T((-1)\mathbf{u}) = (-1)T(\mathbf{u}) = -T(\mathbf{u})\\))。

### 線形変換の例

概念をよりよく理解するために、いくつかの例を見てみましょう。

**例1: \\(\mathbb{R}^2\\) における変換 (回転)**

\\(\mathbb{R}^2\\) 内のすべてのベクトルを角度 \\(\theta\\) だけ反時計回りに回転させる変換 \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) を考えます。もし \\(\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}\\) ならば、\\(T(\mathbf{v}) = \begin{pmatrix} x\cos\theta - y\sin\theta \\ x\sin\theta + y\cos\theta \end{pmatrix}\\) です。

これが線形変換かどうか確認してみましょう。\\(\mathbf{u} = \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}\\)、\\(\mathbf{v} = \begin{pmatrix} x_2 \\ y_2 \end{pmatrix}\\)、\\(c\\) をスカラーとします。

* **加法性:**
    \\(T(\mathbf{u} + \mathbf{v}) = T\left(\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}\right) = \begin{pmatrix} (x_1 + x_2)\cos\theta - (y_1 + y_2)\sin\theta \\ (x_1 + x_2)\sin\theta + (y_1 + y_2)\cos\theta \end{pmatrix}\\)
    \\(= \begin{pmatrix} (x_1\cos\theta - y_1\sin\theta) + (x_2\cos\theta - y_2\sin\theta) \\ (x_1\sin\theta + y_1\cos\theta) + (x_2\sin\theta + y_2\cos\theta) \end{pmatrix} = T(\mathbf{u}) + T(\mathbf{v})\\)

* **斉次性:**
    \\(T(c\mathbf{u}) = T\left(\begin{pmatrix} cx_1 \\ cy_1 \end{pmatrix}\right) = \begin{pmatrix} (cx_1)\cos\theta - (cy_1)\sin\theta \\ (cx_1)\sin\theta + (cy_1)\cos\theta \end{pmatrix}\\)
    \\(= \begin{pmatrix} c(x_1\cos\theta - y_1\sin\theta) \\ c(x_1\sin\theta + y_1\cos\theta) \end{pmatrix} = c \begin{pmatrix} x_1\cos\theta - y_1\sin\theta \\ x_1\sin\theta + y_1\cos\theta \end{pmatrix} = cT(\mathbf{u})\\)

したがって、回転は線形変換です。

**例2: \\(\mathbb{R}^2\\) における変換 (x軸への射影)**

\\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) を \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x \\ 0 \end{pmatrix}\\) で定義される変換とします。この変換はすべてのベクトルをx軸上に射影します。定義を用いてこれも線形変換であることを確認できます。

**例3: \\(\mathbb{R}^2\\) における変換 (平行移動)**

\\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) を \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + a \\ y + b \end{pmatrix}\\) で定義される変換とします。ここで、\\(a\\) と \\(b\\) は定数 (両方がゼロではない) です。

最初の性質を確認してみましょう：
\\(T(\mathbf{u} + \mathbf{v}) = T\left(\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}\right) = \begin{pmatrix} (x_1 + x_2) + a \\ (y_1 + y_2) + b \end{pmatrix} = \begin{pmatrix} x_1 + a + x_2 + a \\ y_1 + b + y_2 + b \end{pmatrix}\\)
\\(T(\mathbf{u}) + T(\mathbf{v}) = \begin{pmatrix} x_1 + a \\ y_1 + b \end{pmatrix} + \begin{pmatrix} x_2 + a \\ y_2 + b \end{pmatrix} = \begin{pmatrix} x_1 + a + x_2 + a \\ y_1 + b + y_2 + b \end{pmatrix}\\)

これは正しいように見えますが、再確認してみましょう。
\\(T(\mathbf{u} + \mathbf{v}) = \begin{pmatrix} x_1 + x_2 + a \\ y_1 + y_2 + b \end{pmatrix}\\)
\\(T(\mathbf{u}) + T(\mathbf{v}) = \begin{pmatrix} x_1 + a \\ y_1 + b \end{pmatrix} + \begin{pmatrix} x_2 + a \\ y_2 + b \end{pmatrix} = \begin{pmatrix} x_1 + x_2 + 2a \\ y_1 + y_2 + 2b \end{pmatrix}\\)

もし \\(a \neq 0\\) または \\(b \neq 0\\) ならば、\\(T(\mathbf{u} + \mathbf{v}) \neq T(\mathbf{u}) + T(\mathbf{v})\\) です。また、\\(T(\mathbf{0}) = T\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} a \\ b \end{pmatrix} \neq \begin{pmatrix} 0 \\ 0 \end{pmatrix}\\) (もし \\(a\\) または \\(b\\) が非ゼロなら)。したがって、平行移動は一般に線形変換では**ありません**。

**例4: 行列によって定義される \\(\mathbb{R}^n\\) から \\(\mathbb{R}^m\\) への変換**

\\(A\\) を \\(m \times n\\) 行列とします。\\(T: \mathbb{R}^n \rightarrow \mathbb{R}^m\\) を \\(T(\mathbf{x}) = A\mathbf{x}\\) (ここで \\(\mathbf{x}\\) は \\(n \times 1\\) 列ベクトル) で定義される変換は、線形変換です。なぜなら行列の乗算は加法性と斉次性の性質を満たすからです：
\\(A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v}\\)
\\(A(c\mathbf{u}) = c(A\mathbf{u})\\)

**例5: 多項式の微分**

\\(P_n\\) を次数が高々 \\(n\\) の多項式からなるベクトル空間とします。\\(D: P_n \rightarrow P_{n-1}\\) を \\(D(p(x)) = p'(x)\\) (\\(p(x)\\) の導関数) で定義される変換は、線形変換です。
もし \\(p(x)\\) と \\(q(x)\\) が多項式で、\\(c\\) がスカラーならば：
\\(D(p(x) + q(x)) = (p(x) + q(x))' = p'(x) + q'(x) = D(p(x)) + D(q(x))\\)
\\(D(cp(x)) = (cp(x))' = cp'(x) = cD(p(x))\\)

**例6: 関数の積分**

\\(C[a, b]\\) を区間 \\([a, b]\\) 上の連続関数からなるベクトル空間とします。\\(I: C[a, b] \rightarrow \mathbb{R}\\) を \\(I(f) = \int_a^b f(x) dx\\) で定義される変換は、線形変換です。
\\(I(f + g) = \int_a^b (f(x) + g(x)) dx = \int_a^b f(x) dx + \int_a^b g(x) dx = I(f) + I(g)\\)
\\(I(cf) = \int_a^b cf(x) dx = c \int_a^b f(x) dx = cI(f)\\)

### 線形変換の行列表現

線形代数における基本的な結果として、有限次元ベクトル空間の間の任意の線形変換は、行列によって表現できるというものがあります。

\\(V\\) を基底 \\(\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2, ..., \mathbf{b}_n\}\\) を持つ \\(n\\) 次元ベクトル空間、\\(W\\) を基底 \\(\mathcal{C} = \{\mathbf{c}_1, \mathbf{c}_2, ..., \mathbf{c}_m\}\\) を持つ \\(m\\) 次元ベクトル空間とします。\\(T: V \rightarrow W\\) を線形変換とします。

基底 \\(\mathcal{B}\\) と \\(\mathcal{C}\\) に関する \\(T\\) の行列表現 (記号で \\([T]_{\mathcal{B}}^{\mathcal{C}}\\)、または基底が明らかな場合は単に \\([T]\\)) を見つけるには、\\(V\\) の基底ベクトルたちの \\(T\\) による像を求め、これらの像を \\(W\\) の基底ベクトルたちの線形結合として表現する必要があります。

各 \\(\mathbf{b}_j \in \mathcal{B}\\) に対して、\\(T(\mathbf{b}_j)\\) は \\(W\\) のベクトルなので、\\(\mathcal{C}\\) の基底ベクトルたちの線形結合として一意に書くことができます：
\\(T(\mathbf{b}_j) = a_{1j}\mathbf{c}_1 + a_{2j}\mathbf{c}_2 + ... + a_{mj}\mathbf{c}_m = \sum_{i=1}^{m} a_{ij}\mathbf{c}_i\\)

この線形結合の係数が、行列表現 \\([T]_{\mathcal{B}}^{\mathcal{C}}\\) の \\(j\\) 列を形成します：
$[T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}$

もし \\(\mathbf{v} \in V\\) が基底 \\(\mathcal{B}\\) に関する座標ベクトル \\([\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}\\) を持つならば、\\(T(\mathbf{v})\\) の基底 \\(\mathcal{C}\\) に関する座標ベクトル (記号で \\([T(\mathbf{v})]_{\mathcal{C}}\\)) は、行列積によって与えられます：
\\([T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\mathbf{v}]_{\mathcal{B}}\\)

**例: 行列表現**

\\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) を \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\) で定義される線形変換とします。\\(\mathbb{R}^2\\) と \\(\mathbb{R}^3\\) の標準基底を、それぞれ \\(\mathcal{B} = \{\mathbf{e}_1, \mathbf{e}_2\} = \left\{ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix} \right\}\\) および \\(\mathcal{C} = \{\mathbf{f}_1, \mathbf{f}_2, \mathbf{f}_3\} = \left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \right\}\\) とします。

\\(\mathbb{R}^2\\) の基底ベクトルたちの \\(T\\) による像を求めます：
\\(T(\mathbf{e}_1) = T\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1 + 0 \\ 2(1) - 0 \\ 3(0) \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} = 1\mathbf{f}_1 + 2\mathbf{f}_2 + 0\mathbf{f}_3\\)
\\(T(\mathbf{e}_2) = T\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 0 + 1 \\ 2(0) - 1 \\ 3(1) \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} = 1\mathbf{f}_1 - 1\mathbf{f}_2 + 3\mathbf{f}_3\\)

標準基底に関する \\(T\\) の行列表現は：
\\([T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ 0 & 3 \end{pmatrix}\\)

ここで、任意のベクトル \\(\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}\\) in \\(\mathbb{R}^2\\) を考えます。その基底 \\(\mathcal{B}\\) に関する座標ベクトルは \\([\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} x \\ y \end{pmatrix}\\) です。
\\([T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)
基底 \\(\mathcal{C}\\) に関する座標ベクトルは確かに \\(\begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\) であり、これは先に定義したベクトル \\(T(\mathbf{v})\\) に対応します。

### 線形変換の核 (零空間)

線形変換 \\(T: V \rightarrow W\\) の**核** (または零空間) は、記号 \\(\text{ker}(T)\\) または \\(N(T)\\) で表され、\\(V\\) 内のベクトルで \\(W\\) のゼロベクトルに写されるものすべての集合です：
\\(\text{ker}(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}_W\}\\)

**核の性質:**

* 線形変換の核は、常に定義域 \\(V\\) の部分空間です。
    * **ゼロベクトルを含む:** \\(T(\mathbf{0}_V) = \mathbf{0}_W\\) なので、\\(\mathbf{0}_V \in \text{ker}(T)\\)。
    * **加法について閉じている:** もし \\(\mathbf{u}, \mathbf{v} \in \text{ker}(T)\\) ならば、\\(T(\mathbf{u}) = \mathbf{0}_W\\) かつ \\(T(\mathbf{v}) = \mathbf{0}_W\\) です。したがって、\\(T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) = \mathbf{0}_W + \mathbf{0}_W = \mathbf{0}_W\\) なので、\\(\mathbf{u} + \mathbf{v} \in \text{ker}(T)\\)。
    * **スカラー乗法について閉じている:** もし \\(\mathbf{u} \in \text{ker}(T)\\) で \\(c\\) がスカラーならば、\\(T(c\mathbf{u}) = cT(\mathbf{u}) = c\mathbf{0}_W = \mathbf{0}_W\\) なので、\\(c\mathbf{u} \in \text{ker}(T)\\)。

**例: 核を求める**

\\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) を \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\) で定義される線形変換とします。
核を求めるには、\\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}\\) を解く必要があります：
\\(\begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}\\)

これは次の連立一次方程式を与えます：
\\(x + y = 0\\)
\\(2x - y = 0\\)
\\(3y = 0\\)

第3式から、\\(y = 0\\)。これを第1式に代入すると、\\(x + 0 = 0\\) なので、\\(x = 0\\)。第2式も満たされます：\\(2(0) - 0 = 0\\)。
唯一の解は \\(x = 0\\) かつ \\(y = 0\\) です。したがって、\\(\text{ker}(T) = \left\{ \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\}\\)、これは \\(\mathbb{R}^2\\) のゼロ部分空間です。

### 線形変換の像 (値域)

線形変換 \\(T: V \rightarrow W\\) の**像** (または値域) は、記号 \\(\text{im}(T)\\) または \\(R(T)\\) で表され、\\(W\\) 内のベクトルで、ある \\(V\\) のベクトルの像であるものすべての集合です：
\\(\text{im}(T) = \{\mathbf{w} \in W \mid \mathbf{w} = T(\mathbf{v}) \text{ for some } \mathbf{v} \in V\}\\)

**像の性質:**

* 線形変換の像は、常に終域 \\(W\\) の部分空間です。
    * **ゼロベクトルを含む:** \\(T(\mathbf{0}_V) = \mathbf{0}_W\\) なので、\\(\mathbf{0}_W \in \text{im}(T)\\)。
    * **加法について閉じている:** もし \\(\mathbf{w}_1, \mathbf{w}_2 \in \text{im}(T)\\) ならば、\\(T(\mathbf{v}_1) = \mathbf{w}_1\\) かつ \\(T(\mathbf{v}_2) = \mathbf{w}_2\\) となるような \\(\mathbf{v}_1, \mathbf{v}_2 \in V\\) が存在します。すると、\\(\mathbf{w}_1 + \mathbf{w}_2 = T(\mathbf{v}_1) + T(\mathbf{v}_2) = T(\mathbf{v}_1 + \mathbf{v}_2)\\)。\\(\mathbf{v}_1 + \mathbf{v}_2 \in V\\) なので、\\(\mathbf{w}_1 + \mathbf{w}_2 \in \text{im}(T)\\)。
    * **スカラー乗法について閉じている:** もし \\(\mathbf{w} \in \text{im}(T)\\) で \\(c\\) がスカラーならば、\\(T(\mathbf{v}) = \mathbf{w}\\) となるような \\(\mathbf{v} \in V\\) が存在します。すると、\\(c\mathbf{w} = cT(\mathbf{v}) = T(c\mathbf{v})\\)。\\(c\mathbf{v} \in V\\) なので、\\(c\mathbf{w} \in \text{im}(T)\\)。

* もし \\(V\\) が基底 \\(\{\mathbf{b}_1, \mathbf{b}_2, ..., \mathbf{b}_n\}\\) を持つ有限次元ならば、\\(T\\) の像は基底ベクトルたちの像の張る空間です：
    \\(\text{im}(T) = \text{span}\{T(\mathbf{b}_1), T(\mathbf{b}_2), ..., T(\mathbf{b}_n)\}\\)

**例: 像を求める**

\\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) を \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\) で定義される線形変換とします。
\\(\mathbb{R}^2\\) の標準基底 \\(\{\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}\}\\) を用いると、次のようになります：
\\(T\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}\\)
\\(T\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}\\)

\\(T\\) の像はこれら2つのベクトルが張る空間です：
\\(\text{im}(T) = \text{span}\left\{ \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} \right\}\\)
これは \\(\mathbb{R}^3\\) の部分空間です。これら2つのベクトルは線形独立 (一方が他方のスカラー倍ではない) なので、像は \\(\mathbb{R}^3\\) 内の原点を通る平面です。

**行列表現と像の関係:**

もし \\(T: \mathbb{R}^n \rightarrow \mathbb{R}^m\\) が \\(T(\mathbf{x}) = A\mathbf{x}\\) で与えられ、\\(A\\) が \\(m \times n\\) 行列ならば、\\(T\\) の像は行列 \\(A\\) の列空間、すなわち \\(A\\) の列ベクトルたちが張る空間です。

### 線形変換の性質：単射性と全射性

**単射性 (一対一)**

線形変換 \\(T: V \rightarrow W\\) が**単射** (または一対一) であるとは、すべての \\(\mathbf{w} \in W\\) に対して、\\(T(\mathbf{v}) = \mathbf{w}\\) となる \\(\mathbf{v} \in V\\) が高々1つしか存在しないことです。同値的に、もし \\(T(\mathbf{u}) = T(\mathbf{v})\\) ならば、\\(\mathbf{u} = \mathbf{v}\\) が成り立つことです。

**定理:** 線形変換 \\(T: V \rightarrow W\\) が単射であるための必要十分条件は、その核がゼロ部分空間であること、すなわち \\(\text{ker}(T) = \{\mathbf{0}_V\}\\) であることです。

**証明:**
* **(\\(\Rightarrow\\)) \\(T\\) が単射であると仮定する。** もし \\(\mathbf{v} \in \text{ker}(T)\\) ならば、\\(T(\mathbf{v}) = \mathbf{0}_W\\) です。また、\\(T(\mathbf{0}_V) = \mathbf{0}_W\\) も知っています。\\(T\\) が単射で \\(T(\mathbf{v}) = T(\mathbf{0}_V)\\) なので、\\(\mathbf{v} = \mathbf{0}_V\\) でなければなりません。したがって、\\(\text{ker}(T) = \{\mathbf{0}_V\}\\)。
* **(\\(\Leftarrow\\)) \\(\text{ker}(T) = \{\mathbf{0}_V\}\\) であると仮定する。** ある \\(\mathbf{u}, \mathbf{v} \in V\\) に対して \\(T(\mathbf{u}) = T(\mathbf{v})\\) であるとします。すると、\\(T(\mathbf{u}) - T(\mathbf{v}) = \mathbf{0}_W\\) です。線形性により、\\(T(\mathbf{u} - \mathbf{v}) = \mathbf{0}_W\\) です。これは \\(\mathbf{u} - \mathbf{v} \in \text{ker}(T)\\) を意味します。\\(\text{ker}(T) = \{\mathbf{0}_V\}\\) なので、\\(\mathbf{u} - \mathbf{v} = \mathbf{0}_V\\) であり、これは \\(\mathbf{u} = \mathbf{v}\\) を意味します。したがって、\\(T\\) は単射です。

**例: 単射性の確認**

\\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) を \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\) で定義される変換に対して、\\(\text{ker}(T) = \left\{ \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\}\\) であることを見つけました。したがって、この変換は単射です。

**全射性 (上への写像)**

線形変換 \\(T: V \rightarrow W\\) が**全射** (または上への写像) であるとは、すべての \\(\mathbf{w} \in W\\) に対して、\\(T(\mathbf{v}) = \mathbf{w}\\) となるような少なくとも1つの \\(\mathbf{v} \in V\\) が存在することです。言い換えると、\\(T\\) の像が終域 \\(W\\) と等しいこと、すなわち \\(\text{im}(T) = W\\) です。

**定理 (階数・退化次数の定理):** 線形変換 \\(T: V \rightarrow W\\) に対して、\\(V\\) が有限次元ベクトル空間ならば、
\\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = \text{dim}(V)\\)
ここで、\\(\text{dim}(\text{ker}(T))\\) は \\(T\\) の**退化次数**、\\(\text{dim}(\text{im}(T))\\) は \\(T\\) の**階数**と呼ばれます。

**全射性と次元の関係:**

もし \\(T: V \rightarrow W\\) が有限次元ベクトル空間の間の線形変換ならば：
* もし \\(\text{dim}(V) < \text{dim}(W)\\) ならば、\\(T\\) は全射にはなりえません。(階数・退化次数の定理により、\\(\text{dim}(\text{im}(T)) \leq \text{dim}(V) < \text{dim}(W)\\))。
* もし \\(\text{dim}(V) > \text{dim}(W)\\) ならば、\\(T\\) は単射にはなりえません (なぜなら \\(\text{dim}(\text{ker}(T)) = \text{dim}(V) - \text{dim}(\text{im}(T)) \geq \text{dim}(V) - \text{dim}(W) > 0\\) なので、核がゼロベクトルだけではないからです)。
* もし \\(\text{dim}(V) = \text{dim}(W)\\) ならば、\\(T\\) が単射であることと全射であることは同値です。(\\(T\\) が単射ならば、\\(\text{dim}(\text{ker}(T)) = 0\\) なので、\\(\text{dim}(\text{im}(T)) = \text{dim}(V) = \text{dim}(W)\\)、すなわち \\(\text{im}(T) = W\\) を意味し、\\(T\\) は全射です。逆に、\\(T\\) が全射ならば、\\(\text{dim}(\text{im}(T)) = \text{dim}(W) = \text{dim}(V)\\) なので、\\(\text{dim}(\text{ker}(T)) = 0\\) を意味し、\\(T\\) は単射です)。

**例: 全射性の確認**

\\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) を \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\) で定義される変換に対して、\\(\text{im}(T) = \text{span}\left\{ \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} \right\}\\) であることを見つけました。像の次元 (\\(T\\) の階数) は2です。なぜなら、これら2つの張るベクトルは線形独立だからです。定義域の次元は \\(\text{dim}(\mathbb{R}^2) = 2\\) です。階数・退化次数の定理により、\\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = 2\\) なので、\\(\text{dim}(\text{ker}(T)) + 2 = 2\\)、これは \\(\text{dim}(\text{ker}(T)) = 0\\) を与え、以前の結果と一致します。

像の次元 (2) が終域の次元 (3) より小さいので、像は終域の真部分空間であり、したがってこの変換は全射ではありません。\\(\mathbb{R}^3\\) 内には \\(T\\) の像に含まれないベクトルが存在します。例えば、\\(\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}\\) は \\(\begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}\\) と \\(\begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}\\) の線形結合として表すことはできません。

**同型写像**

線形変換 \\(T: V \rightarrow W\\) が、単射かつ全射であるとき、**同型写像** と呼ばれます。もし2つのベクトル空間 \\(V\\) と \\(W\\) の間に同型写像が存在するならば、\\(V\\) と \\(W\\) は**同型** であるといい、\\(V \cong W\\) と表します。同型なベクトル空間は本質的に同じ代数構造を持ちます。

有限次元ベクトル空間の場合、2つのベクトル空間が同型であるための必要十分条件は、それらが同じ次元を持つことです。もし \\(\text{dim}(V) = \text{dim}(W) = n\\) ならば、線形変換 \\(T: V \rightarrow W\\) が同型写像であるための必要十分条件は、それが単射であるか、または全射であることです。

**主要概念のまとめ:**

* **線形変換:** ベクトルの加法とスカラー乗法を保存する、ベクトル空間の間の関数。
* **行列表現:** 有限次元ベクトル空間の間の線形変換を行列として表現する方法。
* **核 (零空間):** 定義域内のベクトルで、終域のゼロベクトルに写されるものの集合。定義域の部分空間。
* **像 (値域):** 終域内のベクトルで、ある定義域のベクトルの像であるものの集合。終域の部分空間。
* **単射性 (一対一):** 線形変換が単射であるための必要十分条件は、その核がゼロ部分空間であること。
* **全射性 (上への写像):** 線形変換が全射であるための必要十分条件は、その像が終域と等しいこと。
* **階数・退化次数の定理:** 有限次元の定義域 \\(V\\) を持つ線形変換 \\(T: V \rightarrow W\\) に対して、\\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = \text{dim}(V)\\)。
* **同型写像:** 単射かつ全射である線形変換。

この詳細なチュートリアルが、線形変換を理解するための確かな基礎を提供するはずです。これらの概念の理解を確固たるものにする