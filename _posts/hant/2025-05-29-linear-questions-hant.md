---
audio: false
generated: true
lang: hant
layout: post
title: 線性代數問題
translated: true
type: note
---

好的，我將翻譯並解答圖片中的問題。

**翻譯與解答：**

**18. 設矩陣 X 和 A 滿足關係 XA = X + A。若 $A = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix}$，求矩陣 X。**

**答案：**
已知方程式 $XA = X + A$。
我們可以將其改寫為 $XA - X = A$，所以 $X(A - I) = A$。
如果 $(A - I)$ 可逆，則 $X = A(A - I)^{-1}$。

首先，計算 $A - I$：

$A - I = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\\ 0 & 1 & 0 \\\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\\ 2 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$。

接下來，求 $(A - I)$ 的逆矩陣。令 $B = A - I$。
B 的行列式為 $\det(B) = 0(0 - 0) - (-3)(2 - 0) + 0(0 - 0) = 6$。
由於 $\det(B) \neq 0$，B 是可逆的。

B 的伴隨矩陣為：
$adj(B) = \begin{pmatrix} C_{11} & C_{21} & C_{31} \\\ C_{12} & C_{22} & C_{32} \\\ C_{13} & C_{23} & C_{33} \end{pmatrix}$
$C_{11} = \begin{vmatrix} 0 & 0 \\\ 0 & 1 \end{vmatrix} = 0$
$C_{12} = -\begin{vmatrix} 2 & 0 \\\ 0 & 1 \end{vmatrix} = -2$
$C_{13} = \begin{vmatrix} 2 & 0 \\\ 0 & 0 \end{vmatrix} = 0$
$C_{21} = -\begin{vmatrix} -3 & 0 \\\ 0 & 1 \end{vmatrix} = 3$
$C_{22} = \begin{vmatrix} 0 & 0 \\\ 0 & 1 \end{vmatrix} = 0$
$C_{23} = -\begin{vmatrix} 0 & -3 \\\ 0 & 0 \end{vmatrix} = 0$
$C_{31} = \begin{vmatrix} -3 & 0 \\\ 0 & 0 \end{vmatrix} = 0$
$C_{32} = -\begin{vmatrix} 0 & 0 \\\ 2 & 0 \end{vmatrix} = 0$
$C_{33} = \begin{vmatrix} 0 & -3 \\\ 2 & 0 \end{vmatrix} = 6$

餘因子矩陣為 $C = \begin{pmatrix} 0 & -2 & 0 \\\ 3 & 0 & 0 \\\ 0 & 0 & 6 \end{pmatrix}$。
伴隨矩陣為 $adj(B) = C^T = \begin{pmatrix} 0 & 3 & 0 \\\ -2 & 0 & 0 \\\ 0 & 0 & 6 \end{pmatrix}$。

因此，$(A - I)^{-1} = \frac{1}{\det(B)} adj(B) = \frac{1}{6} \begin{pmatrix} 0 & 3 & 0 \\\ -2 & 0 & 0 \\\ 0 & 0 & 6 \end{pmatrix} = \begin{pmatrix} 0 & 1/2 & 0 \\\ -1/3 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$。

現在計算 $X = A(A - I)^{-1}$：
$X = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} \begin{pmatrix} 0 & 1/2 & 0 \\\ -1/3 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$
$X = \begin{pmatrix} (1)(0) + (-3)(-1/3) + (0)(0) & (1)(1/2) + (-3)(0) + (0)(0) & (1)(0) + (-3)(0) + (0)(1) \\\ (2)(0) + (1)(-1/3) + (0)(0) & (2)(1/2) + (1)(0) + (0)(0) & (2)(0) + (1)(0) + (0)(1) \\\ (0)(0) + (0)(-1/3) + (2)(0) & (0)(1/2) + (0)(0) + (2)(0) & (0)(0) + (0)(0) + (2)(1) \end{pmatrix}$
$X = \begin{pmatrix} 0+1+0 & 1/2+0+0 & 0+0+0 \\\ 0-1/3+0 & 1+0+0 & 0+0+0 \\\ 0+0+0 & 0+0+0 & 0+0+2 \end{pmatrix}$
$X = \begin{pmatrix} 1 & 1/2 & 0 \\\ -1/3 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix}$。

**19. 求 k 的值，使得向量 $\alpha_1 = (1, 1, k)^T$、$\alpha_2 = (1, k, 1)^T$、$\alpha_3 = (k, 1, 1)^T$ 線性相關。找出一個極大線性無關集，並將剩餘向量表示為該集的線性組合。**

**答案：**
向量 $\alpha_1, \alpha_2, \alpha_3$ 線性相關的條件是這些向量組成的矩陣的行列式為零。
令 $A = \begin{pmatrix} 1 & 1 & k \\\ 1 & k & 1 \\\ k & 1 & 1 \end{pmatrix}$。
$\det(A) = 1(k - 1) - 1(1 - k) + k(1 - k^2)$
$= k - 1 - 1 + k + k - k^3$
$= -k^3 + 3k - 2$。
我們需要找到 k 使得 $-k^3 + 3k - 2 = 0$，即 $k^3 - 3k + 2 = 0$。
我們可以測試 2 的因數作為整數根（即 $\pm 1, \pm 2$）。
若 $k=1$，$1^3 - 3(1) + 2 = 1 - 3 + 2 = 0$。所以 $(k-1)$ 是一個因式。
若 $k=-2$，$(-2)^3 - 3(-2) + 2 = -8 + 6 + 2 = 0$。所以 $(k+2)$ 是一個因式。
使用多項式除法或綜合除法計算 $(k^3 - 3k + 2) / (k-1)$：
$(k-1)(k^2+k-2) = 0$
$(k-1)(k+2)(k-1) = 0$
所以，根為 $k=1$（重根）和 $k=-2$。
當 $k=1$ 或 $k=-2$ 時，向量線性相關。

情況 1：$k=1$
$\alpha_1 = (1, 1, 1)^T$，$\alpha_2 = (1, 1, 1)^T$，$\alpha_3 = (1, 1, 1)^T$。
在這種情況下，三個向量完全相同。
一個極大線性無關集可以是 $\{\alpha_1\}$。
那麼 $\alpha_2 = 1 \cdot \alpha_1$ 且 $\alpha_3 = 1 \cdot \alpha_1$。

情況 2：$k=-2$
$\alpha_1 = (1, 1, -2)^T$，$\alpha_2 = (1, -2, 1)^T$，$\alpha_3 = (-2, 1, 1)^T$。
檢查 $\alpha_1$ 和 $\alpha_2$ 是否線性無關。它們不是彼此的純量倍數，因此線性無關。所以，一個極大線性無關集可以是 $\{\alpha_1, \alpha_2\}$。
我們希望將 $\alpha_3$ 表示為 $\alpha_1$ 和 $\alpha_2$ 的線性組合：
$\alpha_3 = c_1 \alpha_1 + c_2 \alpha_2$
$(-2, 1, 1)^T = c_1 (1, 1, -2)^T + c_2 (1, -2, 1)^T$
得到方程組：
1) $c_1 + c_2 = -2$
2) $c_1 - 2c_2 = 1$
3) $-2c_1 + c_2 = 1$
(1) 減去 (2)：$(c_1 + c_2) - (c_1 - 2c_2) = -2 - 1 \Rightarrow 3c_2 = -3 \Rightarrow c_2 = -1$。
將 $c_2 = -1$ 代入 (1)：$c_1 - 1 = -2 \Rightarrow c_1 = -1$。
用 (3) 檢查：$-2(-1) + (-1) = 2 - 1 = 1$。這是一致的。
所以，$\alpha_3 = -1 \cdot \alpha_1 - 1 \cdot \alpha_2$。

**20. 求解線性方程組 { $x_1 - x_2 - 3x_4 = -2$ ; $x_1 + 2x_3 - 2x_4 = -1$ ; $2x_1 - 2x_2 + x_3 - 6x_4 = -5$ ; $-x_1 + 2x_2 + 3x_3 + 4x_4 = 2$ }（求一個特解和對應齊次方程組的基礎解系）。**

**答案：**
增廣矩陣為：
$\begin{pmatrix} 1 & -1 & 0 & -3 & | & -2 \\\ 1 & 0 & 2 & -2 & | & -1 \\\ 2 & -2 & 1 & -6 & | & -5 \\\ -1 & 2 & 3 & 4 & | & 2 \end{pmatrix}$

$R_2 \leftarrow R_2 - R_1$
$R_3 \leftarrow R_3 - 2R_1$
$R_4 \leftarrow R_4 + R_1$
$\begin{pmatrix} 1 & -1 & 0 & -3 & | & -2 \\\ 0 & 1 & 2 & 1 & | & 1 \\\ 0 & 0 & 1 & 0 & | & -1 \\\ 0 & 1 & 3 & 1 & | & 0 \end{pmatrix}$

$R_1 \leftarrow R_1 + R_2$
$R_4 \leftarrow R_4 - R_2$
$\begin{pmatrix} 1 & 0 & 2 & -2 & | & -1 \\\ 0 & 1 & 2 & 1 & | & 1 \\\ 0 & 0 & 1 & 0 & | & -1 \\\ 0 & 0 & 1 & 0 & | & -1 \end{pmatrix}$

$R_1 \leftarrow R_1 - 2R_3$
$R_2 \leftarrow R_2 - 2R_3$
$R_4 \leftarrow R_4 - R_3$
$\begin{pmatrix} 1 & 0 & 0 & -2 & | & 1 \\\ 0 & 1 & 0 & 1 & | & 3 \\\ 0 & 0 & 1 & 0 & | & -1 \\\ 0 & 0 & 0 & 0 & | & 0 \end{pmatrix}$

方程組等價於：
$x_1 - 2x_4 = 1 \Rightarrow x_1 = 1 + 2x_4$
$x_2 + x_4 = 3 \Rightarrow x_2 = 3 - x_4$
$x_3 = -1$
令 $x_4 = t$（自由變量）。
通解為：
$x_1 = 1 + 2t$
$x_2 = 3 - t$
$x_3 = -1$
$x_4 = t$
向量形式：$X = \begin{pmatrix} 1 \\\ 3 \\\ -1 \\\ 0 \end{pmatrix} + t \begin{pmatrix} 2 \\\ -1 \\\ 0 \\\ 1 \end{pmatrix}$。

令 $t=0$ 得到一個特解：$X_p = \begin{pmatrix} 1 \\\ 3 \\\ -1 \\\ 0 \end{pmatrix}$。

對應的齊次方程組的解為 $X_h = t \begin{pmatrix} 2 \\\ -1 \\\ 0 \\\ 1 \end{pmatrix}$。
齊次方程組的基礎解系為 $\{\begin{pmatrix} 2 \\\ -1 \\\ 0 \\\ 1 \end{pmatrix}\}$。

**21. 設矩陣 A = \begin{pmatrix} x & 0 & y \\\ 0 & 2 & 0 \\\ y & 0 & -2 \end{pmatrix} 有一個特徵值為 -3，且 |A| = -12。求 x 和 y 的值。**

**答案：**
特徵方程為 $\det(A - \lambda I) = 0$。
$A - \lambda I = \begin{pmatrix} x-\lambda & 0 & y \\\ 0 & 2-\lambda & 0 \\\ y & 0 & -2-\lambda \end{pmatrix}$。
$\det(A - \lambda I) = (x-\lambda)[(2-\lambda)(-2-\lambda) - 0] - 0 + y[0 - y(2-\lambda)]$
$= (x-\lambda)(2-\lambda)(-2-\lambda) - y^2(2-\lambda)$
$= (2-\lambda)[(x-\lambda)(-2-\lambda) - y^2]$
$= (2-\lambda)[-2x - x\lambda + 2\lambda + \lambda^2 - y^2] = 0$。
特徵值為 $\lambda_1 = 2$，以及方程 $\lambda^2 + (2-x)\lambda - (2x+y^2) = 0$ 的根。
已知一個特徵值為 -3。
如果 $2 = -3$，這不成立。所以，-3 必須是方程 $\lambda^2 + (2-x)\lambda - (2x+y^2) = 0$ 的根。
代入 $\lambda = -3$：
$(-3)^2 + (2-x)(-3) - (2x+y^2) = 0$
$9 - 6 + 3x - 2x - y^2 = 0$
$3 + x - y^2 = 0 \Rightarrow x - y^2 = -3$（方程 1）

同時已知 $\det(A) = -12$。
$\det(A) = x(2(-2) - 0) - 0 + y(0 - 2y)$
$= -4x - 2y^2 = -12$
除以 -2：$2x + y^2 = 6$（方程 2）

現在我們得到關於 x 和 y 的方程組：
1) $x - y^2 = -3$
2) $2x + y^2 = 6$
將方程 1 和方程 2 相加：
$(x - y^2) + (2x + y^2) = -3 + 6$
$3x = 3 \Rightarrow x = 1$。
將 $x=1$ 代入方程 1：
$1 - y^2 = -3$
$-y^2 = -4$
$y^2 = 4 \Rightarrow y = \pm 2$。

所以值為 $x=1$ 和 $y=2$，或 $x=1$ 和 $y=-2$。

檢查兩種情況下的特徵值。
特徵多項式因式分解為 $(2-\lambda)[\lambda^2 + (2-x)\lambda - (2x+y^2)] = 0$。
若 $x=1, y=2$：
$(2-\lambda)[\lambda^2 + (2-1)\lambda - (2(1)+2^2)] = 0$
$(2-\lambda)[\lambda^2 + \lambda - (2+4)] = 0$
$(2-\lambda)(\lambda^2 + \lambda - 6) = 0$
$(2-\lambda)(\lambda+3)(\lambda-2) = 0$。
特徵值為 $\lambda = 2, -3, 2$。這與有一個特徵值為 -3 一致。

若 $x=1, y=-2$：
$(2-\lambda)[\lambda^2 + (2-1)\lambda - (2(1)+(-2)^2)] = 0$
$(2-\lambda)[\lambda^2 + \lambda - (2+4)] = 0$
$(2-\lambda)(\lambda^2 + \lambda - 6) = 0$
$(2-\lambda)(\lambda+3)(\lambda-2) = 0$。
特徵值為 $\lambda = 2, -3, 2$。這也一致。

兩組 $(x,y) = (1,2)$ 和 $(x,y) = (1,-2)$ 都滿足條件。

**22. 設三元二次型 $f(x_1, x_2, x_3) = t(x_1^2 + x_2^2 + x_3^2) + 2x_1x_2 + 2x_1x_3 - 2x_2x_3$。確定 t 為何值時，該二次型是正定的。**

**答案：**
該二次型的矩陣 A 為：
$A = \begin{pmatrix} t & 1 & 1 \\\ 1 & t & -1 \\\ 1 & -1 & t \end{pmatrix}$。
要使二次型正定，A 的所有順序主子式必須為正。

1. 第一順序主子式為 $M_1 = t$。
要正定，$t > 0$。

2. 第二順序主子式為 $M_2 = \det \begin{pmatrix} t & 1 \\\ 1 & t \end{pmatrix} = t^2 - 1$。
要正定，$t^2 - 1 > 0 \Rightarrow t^2 > 1$。
由於已有 $t > 0$，這意味著 $t > 1$。

3. 第三順序主子式為 $M_3 = \det(A)$。
$M_3 = t(t^2 - 1) - 1(t - (-1)) + 1(-1 - t)$
$= t(t^2 - 1) - (t + 1) - (1 + t)$
$= t^3 - t - t - 1 - 1 - t$
$= t^3 - 3t - 2$。
要正定，$t^3 - 3t - 2 > 0$。

從第 19 題可知 $k^3 - 3k - 2 = (k+1)^2(k-2)$。（這裡 k 是 t）
所以，$t^3 - 3t - 2 = (t+1)^2(t-2)$。
需要 $(t+1)^2(t-2) > 0$。
由於 $(t+1)^2 \ge 0$，且為了不為零，$t \neq -1$。
所以需要 $t-2 > 0$，即 $t > 2$。

合併條件：
1) $t > 0$
2) $t > 1$
3) $t > 2$

這些條件的交集是 $t > 2$。
因此，當 $t > 2$ 時，該二次型是正定的。