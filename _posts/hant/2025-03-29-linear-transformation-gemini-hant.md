---
audio: false
generated: true
lang: hant
layout: post
title: 線性變換 - Gemini
translated: true
type: note
---

好的，讓我們深入探討線性變換的詳細教程，涵蓋定義、範例、矩陣表示、核、像以及單射性和滿射性等性質。這是線性代數中的基礎主題。

## 6. 線性變換：詳細教程

一個**線性變換**是兩個向量空間之間的一個函數，它保持了向量加法和純量乘法的運算。令 \\(V\\) 和 \\(W\\) 是佈於同一體 \\(F\\)（通常是實數集 \\(\mathbb{R}\\) 或複數集 \\(\mathbb{C}\\)）的向量空間。

**定義：** 一個函數 \\(T: V \rightarrow W\\) 是一個線性變換，若它對所有向量 \\(\mathbf{u}, \mathbf{v} \in V\\) 和所有純量 \\(c \in F\\) 滿足以下兩個性質：

1.  **可加性：** \\(T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})\\)
2.  **齊次性（純量乘法）：** \\(T(c\mathbf{u}) = cT(\mathbf{u})\\)

這兩個性質可以合併為一個條件：
對所有 \\(\mathbf{u}, \mathbf{v} \in V\\) 和所有純量 \\(c, d \in F\\)，有 \\(T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})\\)。

**線性性的關鍵推論：**

* \\(T(\mathbf{0}_V) = \mathbf{0}_W\\)，其中 \\(\mathbf{0}_V\\) 是 \\(V\\) 中的零向量，\\(\mathbf{0}_W\\) 是 \\(W\\) 中的零向量。（證明：對任意 \\(\mathbf{u} \in V\\)，有 \\(T(\mathbf{0}_V) = T(0\mathbf{u}) = 0T(\mathbf{u}) = \mathbf{0}_W\\)）。
* \\(T(-\mathbf{u}) = -T(\mathbf{u})\\)。（證明：\\(T(-\mathbf{u}) = T((-1)\mathbf{u}) = (-1)T(\mathbf{u}) = -T(\mathbf{u})\\)）。

### 線性變換的範例

讓我們看一些例子來更好地理解這個概念。

**範例 1： \\(\mathbb{R}^2\\) 中的變換（旋轉）**

考慮一個變換 \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\)，它將 \\(\mathbb{R}^2\\) 中的每個向量逆時針旋轉一個角度 \\(\theta\\)。如果 \\(\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}\\)，則 \\(T(\mathbf{v}) = \begin{pmatrix} x\cos\theta - y\sin\theta \\ x\sin\theta + y\cos\theta \end{pmatrix}\\)。

讓我們檢查這是否是一個線性變換。令 \\(\mathbf{u} = \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}\\) 和 \\(\mathbf{v} = \begin{pmatrix} x_2 \\ y_2 \end{pmatrix}\\)，並令 \\(c\\) 為一個純量。

* **可加性：**
    \\(T(\mathbf{u} + \mathbf{v}) = T\left(\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}\right) = \begin{pmatrix} (x_1 + x_2)\cos\theta - (y_1 + y_2)\sin\theta \\ (x_1 + x_2)\sin\theta + (y_1 + y_2)\cos\theta \end{pmatrix}\\)
    \\(= \begin{pmatrix} (x_1\cos\theta - y_1\sin\theta) + (x_2\cos\theta - y_2\sin\theta) \\ (x_1\sin\theta + y_1\cos\theta) + (x_2\sin\theta + y_2\cos\theta) \end{pmatrix} = T(\mathbf{u}) + T(\mathbf{v})\\)

* **齊次性：**
    \\(T(c\mathbf{u}) = T\left(\begin{pmatrix} cx_1 \\ cy_1 \end{pmatrix}\right) = \begin{pmatrix} (cx_1)\cos\theta - (cy_1)\sin\theta \\ (cx_1)\sin\theta + (cy_1)\cos\theta \end{pmatrix}\\)
    \\(= \begin{pmatrix} c(x_1\cos\theta - y_1\sin\theta) \\ c(x_1\sin\theta + y_1\cos\theta) \end{pmatrix} = c \begin{pmatrix} x_1\cos\theta - y_1\sin\theta \\ x_1\sin\theta + y_1\cos\theta \end{pmatrix} = cT(\mathbf{u})\\)

因此，旋轉是一個線性變換。

**範例 2： \\(\mathbb{R}^2\\) 中的變換（投影到 x 軸）**

考慮 \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) 定義為 \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x \\ 0 \end{pmatrix}\\)。這個變換將每個向量投影到 x 軸上。你可以使用定義驗證這也是一個線性變換。

**範例 3： \\(\mathbb{R}^2\\) 中的變換（平移）**

考慮 \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) 定義為 \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + a \\ y + b \end{pmatrix}\\)，其中 \\(a\\) 和 \\(b\\) 是常數（不同時為零）。

讓我們檢查第一個性質：
\\(T(\mathbf{u} + \mathbf{v}) = T\left(\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}\right) = \begin{pmatrix} (x_1 + x_2) + a \\ (y_1 + y_2) + b \end{pmatrix} = \begin{pmatrix} x_1 + a + x_2 + a \\ y_1 + b + y_2 + b \end{pmatrix}\\)
\\(T(\mathbf{u}) + T(\mathbf{v}) = \begin{pmatrix} x_1 + a \\ y_1 + b \end{pmatrix} + \begin{pmatrix} x_2 + a \\ y_2 + b \end{pmatrix} = \begin{pmatrix} x_1 + a + x_2 + a \\ y_1 + b + y_2 + b \end{pmatrix}\\)

這看起來正確，讓我們重新檢查。
\\(T(\mathbf{u} + \mathbf{v}) = \begin{pmatrix} x_1 + x_2 + a \\ y_1 + y_2 + b \end{pmatrix}\\)
\\(T(\mathbf{u}) + T(\mathbf{v}) = \begin{pmatrix} x_1 + a \\ y_1 + b \end{pmatrix} + \begin{pmatrix} x_2 + a \\ y_2 + b \end{pmatrix} = \begin{pmatrix} x_1 + x_2 + 2a \\ y_1 + y_2 + 2b \end{pmatrix}\\)

如果 \\(a \neq 0\\) 或 \\(b \neq 0\\)，則 \\(T(\mathbf{u} + \mathbf{v}) \neq T(\mathbf{u}) + T(\mathbf{v})\\)。此外，\\(T(\mathbf{0}) = T\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} a \\ b \end{pmatrix} \neq \begin{pmatrix} 0 \\ 0 \end{pmatrix}\\) 如果 \\(a\\) 或 \\(b\\) 非零。因此，平移通常**不是**線性變換。

**範例 4：由矩陣定義的從 \\(\mathbb{R}^n\\) 到 \\(\mathbb{R}^m\\) 的變換**

令 \\(A\\) 是一個 \\(m \times n\\) 矩陣。由 \\(T(\mathbf{x}) = A\mathbf{x}\\) 定義的變換 \\(T: \mathbb{R}^n \rightarrow \mathbb{R}^m\\)（其中 \\(\mathbf{x}\\) 是一個 \\(n \times 1\\) 行向量）是一個線性變換。這是因為矩陣乘法滿足可加性和齊次性：
\\(A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v}\\)
\\(A(c\mathbf{u}) = c(A\mathbf{u})\\)

**範例 5：多項式的微分**

令 \\(P_n\\) 為次數最多為 \\(n\\) 的多項式向量空間。由 \\(D(p(x)) = p'(x)\\)（\\(p(x)\\) 的導數）定義的變換 \\(D: P_n \rightarrow P_{n-1}\\) 是一個線性變換。
如果 \\(p(x)\\) 和 \\(q(x)\\) 是多項式且 \\(c\\) 是一個純量：
\\(D(p(x) + q(x)) = (p(x) + q(x))' = p'(x) + q'(x) = D(p(x)) + D(q(x))\\)
\\(D(cp(x)) = (cp(x))' = cp'(x) = cD(p(x))\\)

**範例 6：函數的積分**

令 \\(C[a, b]\\) 為區間 \\([a, b]\\) 上連續函數的向量空間。由 \\(I(f) = \int_a^b f(x) dx\\) 定義的變換 \\(I: C[a, b] \rightarrow \mathbb{R}\\) 是一個線性變換。
\\(I(f + g) = \int_a^b (f(x) + g(x)) dx = \int_a^b f(x) dx + \int_a^b g(x) dx = I(f) + I(g)\\)
\\(I(cf) = \int_a^b cf(x) dx = c \int_a^b f(x) dx = cI(f)\\)

### 線性變換的矩陣表示

線性代數的一個基本結果是，任何有限維向量空間之間的線性變換都可以用矩陣來表示。

令 \\(V\\) 是一個 \\(n\\) 維向量空間，其基底為 \\(\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2, ..., \mathbf{b}_n\}\\)，\\(W\\) 是一個 \\(m\\) 維向量空間，其基底為 \\(\mathcal{C} = \{\mathbf{c}_1, \mathbf{c}_2, ..., \mathbf{c}_m\}\\)。令 \\(T: V \rightarrow W\\) 是一個線性變換。

為了找到 \\(T\\) 關於基底 \\(\mathcal{B}\\) 和 \\(\mathcal{C}\\) 的矩陣表示（記為 \\([T]_{\mathcal{B}}^{\mathcal{C}}\\) 或簡記為 \\([T]\\)，當基底明確時），我們需要確定 \\(V\\) 的基底向量在 \\(T\\) 下的像，並將這些像表示為 \\(W\\) 的基底向量的線性組合。

對於每個 \\(\mathbf{b}_j \in \mathcal{B}\\)，\\(T(\mathbf{b}_j)\\) 是 \\(W\\) 中的一個向量，因此它可以唯一地寫成 \\(\mathcal{C}\\) 中基底向量的線性組合：
\\(T(\mathbf{b}_j) = a_{1j}\mathbf{c}_1 + a_{2j}\mathbf{c}_2 + ... + a_{mj}\mathbf{c}_m = \sum_{i=1}^{m} a_{ij}\mathbf{c}_i\\)

這個線性組合的係數構成了矩陣表示 \\([T]_{\mathcal{B}}^{\mathcal{C}}\\) 的第 \\(j\\) 列：
$[T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}$

如果 \\(\mathbf{v} \in V\\) 關於基底 \\(\mathcal{B}\\) 的座標向量為 \\([\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}\\)，則 \\(T(\mathbf{v})\\) 關於基底 \\(\mathcal{C}\\) 的座標向量，記為 \\([T(\mathbf{v})]_{\mathcal{C}}\\)，由矩陣乘積給出：
\\([T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\mathbf{v}]_{\mathcal{B}}\\)

**範例：矩陣表示**

令 \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) 是一個線性變換，定義為 \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)。令 \\(\mathbb{R}^2\\) 和 \\(\mathbb{R}^3\\) 的標準基底分別為 \\(\mathcal{B} = \{\mathbf{e}_1, \mathbf{e}_2\} = \left\{ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix} \right\}\\) 和 \\(\mathcal{C} = \{\mathbf{f}_1, \mathbf{f}_2, \mathbf{f}_3\} = \left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \right\}\\)。

我們找出 \\(\mathbb{R}^2\\) 的基底向量在 \\(T\\) 下的像：
\\(T(\mathbf{e}_1) = T\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1 + 0 \\ 2(1) - 0 \\ 3(0) \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} = 1\mathbf{f}_1 + 2\mathbf{f}_2 + 0\mathbf{f}_3\\)
\\(T(\mathbf{e}_2) = T\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 0 + 1 \\ 2(0) - 1 \\ 3(1) \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} = 1\mathbf{f}_1 - 1\mathbf{f}_2 + 3\mathbf{f}_3\\)

\\(T\\) 關於標準基底的矩陣表示為：
\\([T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ 0 & 3 \end{pmatrix}\\)

現在，取一個任意向量 \\(\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}\\) 在 \\(\mathbb{R}^2\\) 中。它關於 \\(\mathcal{B}\\) 的座標向量是 \\([\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} x \\ y \end{pmatrix}\\)。
\\([T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)
關於 \\(\mathcal{C}\\) 的座標向量確實是 \\(\begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)，對應於我們之前定義的向量 \\(T(\mathbf{v})\\)。

### 線性變換的核（零空間）

線性變換 \\(T: V \rightarrow W\\) 的**核**（或零空間），記為 \\(\text{ker}(T)\\) 或 \\(N(T)\\)，是 \\(V\\) 中所有被映射到 \\(W\\) 中零向量的向量集合：
\\(\text{ker}(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}_W\}\\)

**核的性質：**

* 線性變換的核始終是定義域 \\(V\\) 的一個子空間。
    * **包含零向量：** \\(T(\mathbf{0}_V) = \mathbf{0}_W\\)，所以 \\(\mathbf{0}_V \in \text{ker}(T)\\)。
    * **對加法封閉：** 如果 \\(\mathbf{u}, \mathbf{v} \in \text{ker}(T)\\)，則 \\(T(\mathbf{u}) = \mathbf{0}_W\\) 且 \\(T(\mathbf{v}) = \mathbf{0}_W\\)。因此，\\(T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) = \mathbf{0}_W + \mathbf{0}_W = \mathbf{0}_W\\)，所以 \\(\mathbf{u} + \mathbf{v} \in \text{ker}(T)\\)。
    * **對純量乘法封閉：** 如果 \\(\mathbf{u} \in \text{ker}(T)\\) 且 \\(c\\) 是一個純量，則 \\(T(c\mathbf{u}) = cT(\mathbf{u}) = c\mathbf{0}_W = \mathbf{0}_W\\)，所以 \\(c\mathbf{u} \in \text{ker}(T)\\)。

**範例：求核**

考慮線性變換 \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) 定義為 \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)。
為了求核，我們需要解 \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}\\)：
\\(\begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}\\)

這給出線性方程組：
\\(x + y = 0\\)
\\(2x - y = 0\\)
\\(3y = 0\\)

從第三個方程，\\(y = 0\\)。將其代入第一個方程，\\(x + 0 = 0\\)，所以 \\(x = 0\\)。第二個方程也滿足：\\(2(0) - 0 = 0\\)。
唯一解是 \\(x = 0\\) 和 \\(y = 0\\)。因此，\\(\text{ker}(T) = \left\{ \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\}\\)，即 \\(\mathbb{R}^2\\) 的零子空間。

### 線性變換的像（值域）

線性變換 \\(T: V \rightarrow W\\) 的**像**（或值域），記為 \\(\text{im}(T)\\) 或 \\(R(T)\\)，是 \\(W\\) 中所有是某個 \\(V\\) 中向量的像的向量集合：
\\(\text{im}(T) = \{\mathbf{w} \in W \mid \mathbf{w} = T(\mathbf{v}) \text{ for some } \mathbf{v} \in V\}\\)

**像的性質：**

* 線性變換的像始終是對應域 \\(W\\) 的一個子空間。
    * **包含零向量：** \\(T(\mathbf{0}_V) = \mathbf{0}_W\\)，所以 \\(\mathbf{0}_W \in \text{im}(T)\\)。
    * **對加法封閉：** 如果 \\(\mathbf{w}_1, \mathbf{w}_2 \in \text{im}(T)\\)，則存在 \\(\mathbf{v}_1, \mathbf{v}_2 \in V\\) 使得 \\(T(\mathbf{v}_1) = \mathbf{w}_1\\) 且 \\(T(\mathbf{v}_2) = \mathbf{w}_2\\)。那麼 \\(\mathbf{w}_1 + \mathbf{w}_2 = T(\mathbf{v}_1) + T(\mathbf{v}_2) = T(\mathbf{v}_1 + \mathbf{v}_2)\\)。由於 \\(\mathbf{v}_1 + \mathbf{v}_2 \in V\\)，所以 \\(\mathbf{w}_1 + \mathbf{w}_2 \in \text{im}(T)\\)。
    * **對純量乘法封閉：** 如果 \\(\mathbf{w} \in \text{im}(T)\\) 且 \\(c\\) 是一個純量，則存在 \\(\mathbf{v} \in V\\) 使得 \\(T(\mathbf{v}) = \mathbf{w}\\)。那麼 \\(c\mathbf{w} = cT(\mathbf{v}) = T(c\mathbf{v})\\)。由於 \\(c\mathbf{v} \in V\\)，所以 \\(c\mathbf{w} \in \text{im}(T)\\)。

* 如果 \\(V\\) 是有限維的，且有一個基底 \\(\{\mathbf{b}_1, \mathbf{b}_2, ..., \mathbf{b}_n\}\\)，則 \\(T\\) 的像是基底向量像的生成空間：
    \\(\text{im}(T) = \text{span}\{T(\mathbf{b}_1), T(\mathbf{b}_2), ..., T(\mathbf{b}_n)\}\\)

**範例：求像**

考慮線性變換 \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) 定義為 \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)。
使用 \\(\mathbb{R}^2\\) 的標準基底 \\(\{\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}\}\\)，我們有：
\\(T\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}\\)
\\(T\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}\\)

\\(T\\) 的像是這兩個向量的生成空間：
\\(\text{im}(T) = \text{span}\left\{ \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} \right\}\\)
這是 \\(\mathbb{R}^3\\) 的一個子空間。由於這兩個向量線性獨立（一個不是另一個的純量倍數），該像是 \\(\mathbb{R}^3\\) 中通過原點的一個平面。

**矩陣表示與像之間的關係：**

如果 \\(T: \mathbb{R}^n \rightarrow \mathbb{R}^m\\) 由 \\(T(\mathbf{x}) = A\mathbf{x}\\) 給出，其中 \\(A\\) 是一個 \\(m \times n\\) 矩陣，則 \\(T\\) 的像是矩陣 \\(A\\) 的列空間，即 \\(A\\) 的行的生成空間。

### 線性變換的性質：單射性與滿射性

**單射性（一對一）**

一個線性變換 \\(T: V \rightarrow W\\) 是**單射**（或一對一）的，如果對於每個 \\(\mathbf{w} \in W\\)，至多存在一個 \\(\mathbf{v} \in V\\) 使得 \\(T(\mathbf{v}) = \mathbf{w}\\)。等價地說，如果 \\(T(\mathbf{u}) = T(\mathbf{v})\\)，則 \\(\mathbf{u} = \mathbf{v}\\)。

**定理：** 一個線性變換 \\(T: V \rightarrow W\\) 是單射的，若且唯若其核是零子空間，即 \\(\text{ker}(T) = \{\mathbf{0}_V\}\\)。

**證明：**
* **(\\(\Rightarrow\\)) 假設 \\(T\\) 是單射。** 如果 \\(\mathbf{v} \in \text{ker}(T)\\)，則 \\(T(\mathbf{v}) = \mathbf{0}_W\\)。我們也知道 \\(T(\mathbf{0}_V) = \mathbf{0}_W\\)。由於 \\(T\\) 是單射且 \\(T(\mathbf{v}) = T(\mathbf{0}_V)\\)，則必須有 \\(\mathbf{v} = \mathbf{0}_V\\)。因此，\\(\text{ker}(T) = \{\mathbf{0}_V\}\\)。
* **(\\(\Leftarrow\\)) 假設 \\(\text{ker}(T) = \{\mathbf{0}_V\}\\)。** 假設對於某些 \\(\mathbf{u}, \mathbf{v} \in V\\) 有 \\(T(\mathbf{u}) = T(\mathbf{v})\\)。那麼 \\(T(\mathbf{u}) - T(\mathbf{v}) = \mathbf{0}_W\\)。由線性性，\\(T(\mathbf{u} - \mathbf{v}) = \mathbf{0}_W\\)。這意味著 \\(\mathbf{u} - \mathbf{v} \in \text{ker}(T)\\)。由於 \\(\text{ker}(T) = \{\mathbf{0}_V\}\\)，我們有 \\(\mathbf{u} - \mathbf{v} = \mathbf{0}_V\\)，這意味著 \\(\mathbf{u} = \mathbf{v}\\)。因此，\\(T\\) 是單射。

**範例：檢查單射性**

對於變換 \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) 定義為 \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)，我們發現 \\(\text{ker}(T) = \left\{ \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\}\\)。因此，這個變換是單射的。

**滿射性（映成）**

一個線性變換 \\(T: V \rightarrow W\\) 是**滿射**（或映成）的，如果對於每個 \\(\mathbf{w} \in W\\)，至少存在一個 \\(\mathbf{v} \in V\\) 使得 \\(T(\mathbf{v}) = \mathbf{w}\\)。換句話說，\\(T\\) 的像等於對應域 \\(W\\)，即 \\(\text{im}(T) = W\\)。

**定理（秩-零化度定理）：** 對於線性變換 \\(T: V \rightarrow W\\)，其中 \\(V\\) 是有限維向量空間，
\\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = \text{dim}(V)\\)
這裡，\\(\text{dim}(\text{ker}(T))\\) 稱為 \\(T\\) 的**零化度**，\\(\text{dim}(\text{im}(T))\\) 稱為 \\(T\\) 的**秩**。

**滿射性與維度之間的關係：**

如果 \\(T: V \rightarrow W\\) 是有限維向量空間之間的線性變換，則：
* 如果 \\(\text{dim}(V) < \text{dim}(W)\\)，則 \\(T\\) 不可能是滿射。（根據秩-零化度定理，\\(\text{dim}(\text{im}(T)) \leq \text{dim}(V) < \text{dim}(W)\\)）。
* 如果 \\(\text{dim}(V) > \text{dim}(W)\\)，則 \\(T\\) 不可能是單射（因為 \\(\text{dim}(\text{ker}(T)) = \text{dim}(V) - \text{dim}(\text{im}(T)) \geq \text{dim}(V) - \text{dim}(W) > 0\\)，所以核不僅僅是零向量）。
* 如果 \\(\text{dim}(V) = \text{dim}(W)\\)，則 \\(T\\) 是單射若且唯若它是滿射。（如果 \\(T\\) 是單射，則 \\(\text{dim}(\text{ker}(T)) = 0\\)，所以 \\(\text{dim}(\text{im}(T)) = \text{dim}(V) = \text{dim}(W)\\)，意味著 \\(\text{im}(T) = W\\)，所以 \\(T\\) 是滿射。反之，如果 \\(T\\) 是滿射，則 \\(\text{dim}(\text{im}(T)) = \text{dim}(W) = \text{dim}(V)\\)，所以 \\(\text{dim}(\text{ker}(T)) = 0\\)，意味著 \\(T\\) 是單射）。

**範例：檢查滿射性**

對於變換 \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) 定義為 \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)，我們發現 \\(\text{im}(T) = \text{span}\left\{ \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} \right\}\\)。像的維度（\\(T\\) 的秩）是 2，因為這兩個生成向量線性獨立。定義域的維度是 \\(\text{dim}(\mathbb{R}^2) = 2\\)。根據秩-零化度定理，\\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = 2\\)，所以 \\(\text{dim}(\text{ker}(T)) + 2 = 2\\)，這給出 \\(\text{dim}(\text{ker}(T)) = 0\\)，與我們之前的發現一致。

由於像的維度 (2) 小於對應域的維度 (3)，該像是對應域的一個真子空間，因此該變換不是滿射。在 \\(\mathbb{R}^3\\) 中存在不在 \\(T\\) 的像中的向量。例如，\\(\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}\\) 不能表示為 \\(\begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}\\) 和 \\(\begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}\\) 的線性組合。

**同構**

一個線性變換 \\(T: V \rightarrow W\\) 被稱為**同構**，如果它既是單射又是滿射。如果兩個向量空間 \\(V\\) 和 \\(W\\) 之間存在一個同構，則稱 \\(V\\) 和 \\(W\\) 是**同構的**，記為 \\(V \cong W\\)。同構的向量空間具有本質上相同的代數結構。

對於有限維向量空間，兩個向量空間同構若且唯若它們具有相同的維度。如果 \\(\text{dim}(V) = \text{dim}(W) = n\\)，則線性變換 \\(T: V \rightarrow W\\) 是一個同構若且唯若它是單射或滿射。

**關鍵概念總結：**

* **線性變換：** 向量空間之間的一個函數，它保持向量加法和純量乘法。
* **矩陣表示：** 一種將有限維向量空間之間的線性變換表示為矩陣的方法。
* **核（零空間）：** 定義域中被映射到對應域中零向量的向量集合。它是定義域的一個子空間。
* **像（值域）：** 對應域中是某個定義域向量的像的向量集合。它是對應域的一個子空間。
* **單射性（一對一）：** 一個線性變換是單射的若且唯若其核是零子空間。
* **滿射性（映成）：** 一個線性變換是滿射的若且唯若其像等於對應域。
* **秩-零化度定理：** 對於線性變換 \\(T: V \rightarrow W\\) 且 \\(V\\) 是有限維的，有 \\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = \text{dim}(V)\\)。
* **同構：** 一個既是單射又是滿射的線性變換。

這個詳細的教程應該能為理解線性變換提供堅實的基礎。記得練習各種例子來鞏固你對這些概念的理解。祝你學習順利！