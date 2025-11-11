---
audio: false
generated: true
lang: hant
layout: post
title: 線性變換
translated: true
type: note
---

**定義、範例、矩陣表示、核、像、性質（單射性、滿射性）**

線性變換是線性代數的基礎，在向量空間與矩陣之間建立了橋樑。本教程涵蓋：
- 線性變換的**定義**
- 常見線性變換的**範例**
- 線性變換的**矩陣表示**
- **核（零空間）**與**像（值域）**
- **性質**：單射性（一對一）與滿射性（映成）

---

## **1. 線性變換的定義**
**線性變換**（或線性映射）是指兩個定義在體 \\( \mathbb{F} \\)（通常為 \\( \mathbb{R} \\) 或 \\( \mathbb{C} \\)）上的向量空間 \\( V \\) 與 \\( W \\) 之間的函數 \\( T: V \to W \\)，且滿足：
1. **加法性**：
   \\[
   T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \quad \forall \mathbf{u}, \mathbf{v} \in V
   \\]
2. **齊次性（純量乘法）**：
   \\[
   T(c \mathbf{v}) = c T(\mathbf{v}) \quad \forall c \in \mathbb{F}, \mathbf{v} \in V
   \\]

**關鍵概念**：線性變換保持向量加法與純量乘法。

---

## **2. 線性變換範例**

### **(a) 零變換**
- 對所有 \\( \mathbf{v} \in V \\)，\\( T(\mathbf{v}) = \mathbf{0} \\)。

### **(b) 恆等變換**
- 對所有 \\( \mathbf{v} \in V \\)，\\( T(\mathbf{v}) = \mathbf{v} \\)。

### **(c) \\( \mathbb{R}^2 \\) 中的旋轉**
- 將向量旋轉角度 \\( \theta \\)：
  \\[
  T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
  \\]

### **(d) 微分（多項式空間）**
- \\( T: P_n \to P_{n-1} \\)，其中 \\( T(p(x)) = p'(x) \\)。

### **(e) 矩陣乘法**
- 對於固定的 \\( m \times n \\) 矩陣 \\( A \\)，定義 \\( T: \mathbb{R}^n \to \mathbb{R}^m \\) 為 \\( T(\mathbf{x}) = A\mathbf{x} \\)。

---

## **3. 線性變換的矩陣表示**
每個線性變換 \\( T: \mathbb{R}^n \to \mathbb{R}^m \\) 都可以用一個 \\( m \times n \\) 矩陣 \\( A \\) 表示，使得：
\\[
T(\mathbf{x}) = A\mathbf{x}
\\]

### **如何找到矩陣 \\( A \\)**
1. 將 \\( T \\) 應用於 \\( \mathbb{R}^n \\) 的標準基向量 \\( \mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\)。
2. \\( A \\) 的各行即為 \\( T(\mathbf{e}_1), T(\mathbf{e}_2), \dots, T(\mathbf{e}_n) \\)。

**範例**：
定義 \\( T: \mathbb{R}^2 \to \mathbb{R}^2 \\) 為：
\\[
T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2x + y \\ x - 3y \end{pmatrix}
\\]
- 計算 \\( T(\mathbf{e}_1) = T(1, 0) = (2, 1) \\)
- 計算 \\( T(\mathbf{e}_2) = T(0, 1) = (1, -3) \\)
- 因此，矩陣 \\( A \\) 為：
  \\[
  A = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}
  \\]

---

## **4. 核（零空間）與像（值域）**

### **(a) 核（零空間）**
\\( T \\) 的**核**是指 \\( V \\) 中所有映射到 \\( \mathbf{0} \\) 的向量集合：
\\[
\ker(T) = \{ \mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0} \}
\\]

**性質**：
- \\( \ker(T) \\) 是 \\( V \\) 的子空間。
- \\( T \\) 是**單射（一對一）**若且唯若 \\( \ker(T) = \{ \mathbf{0} \} \\)。

**範例**：
對於 \\( T(\mathbf{x}) = A\mathbf{x} \\)，其中 \\( A = \begin{pmatrix} 1 & 2 \\ 3 & 6 \end{pmatrix} \\)，
\\[
\ker(T) = \text{Span} \left\{ \begin{pmatrix} -2 \\ 1 \end{pmatrix} \right\}
\\]

### **(b) 像（值域）**
\\( T \\) 的**像**是指 \\( W \\) 中所有輸出的集合：
\\[
\text{Im}(T) = \{ T(\mathbf{v}) \mid \mathbf{v} \in V \}
\\]

**性質**：
- \\( \text{Im}(T) \\) 是 \\( W \\) 的子空間。
- \\( T \\) 是**滿射（映成）**若且唯若 \\( \text{Im}(T) = W \\)。

**範例**：
對於 \\( T(\mathbf{x}) = A\mathbf{x} \\)，其中 \\( A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix} \\)，
\\[
\text{Im}(T) = \text{Span} \left\{ \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \right\}
\\]

---

## **5. 性質：單射性與滿射性**

### **(a) 單射性（一對一）**
線性變換 \\( T \\) 是**單射**若：
\\[
T(\mathbf{u}) = T(\mathbf{v}) \implies \mathbf{u} = \mathbf{v}
\\]
**檢驗方法**：
- \\( T \\) 是單射 \\( \iff \ker(T) = \{ \mathbf{0} \} \\)。
- 若 \\( \dim(V) < \dim(W) \\)，則 \\( T \\) 可能不是單射。

### **(b) 滿射性（映成）**
線性變換 \\( T \\) 是**滿射**若：
\\[
\forall \mathbf{w} \in W, \exists \mathbf{v} \in V \text{ 使得 } T(\mathbf{v}) = \mathbf{w}
\\]
**檢驗方法**：
- \\( T \\) 是滿射 \\( \iff \text{Im}(T) = W \\)。
- 若 \\( \dim(V) > \dim(W) \\)，則 \\( T \\) 可能不是滿射。

### **(c) 秩-零化度定理**
對於 \\( T: V \to W \\)，
\\[
\dim(V) = \dim(\ker(T)) + \dim(\text{Im}(T))
\\]
- **秩** \\( = \dim(\text{Im}(T)) \\)
- **零化度** \\( = \dim(\ker(T)) \\)

**範例**：
若 \\( T: \mathbb{R}^3 \to \mathbb{R}^2 \\) 滿足 \\( \dim(\ker(T)) = 1 \\)，則 \\( \dim(\text{Im}(T)) = 2 \\)。

---

## **總結**

| 概念 | 定義 | 關鍵性質 |
|---------|------------|--------------|
| **線性變換** | \\( T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \\) 且 \\( T(c\mathbf{v}) = cT(\mathbf{v}) \\) | 保持線性結構 |
| **矩陣表示** | \\( T(\mathbf{x}) = A\mathbf{x} \\)，其中 \\( A \\) 的各行是 \\( T(\mathbf{e}_i) \\) | 編碼變換 |
| **核** | \\( \ker(T) = \{ \mathbf{v} \mid T(\mathbf{v}) = \mathbf{0} \} \\) | 衡量單射性 |
| **像** | \\( \text{Im}(T) = \{ T(\mathbf{v}) \mid \mathbf{v} \in V \} \\) | 衡量滿射性 |
| **單射性** | \\( \ker(T) = \{ \mathbf{0} \} \\) | 一對一 |
| **滿射性** | \\( \text{Im}(T) = W \\) | 映成 |

---

## **練習問題**
1. 求 \\( T(x, y, z) = (2x - y, y + 3z) \\) 的矩陣表示。
2. 判斷 \\( T(\mathbf{x}) = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \mathbf{x} \\) 是否為單射/滿射。
3. 計算 \\( T(x, y) = (x + y, 2x - y, x) \\) 的 \\( \ker(T) \\) 與 \\( \text{Im}(T) \\)。

---

本教程涵蓋了大學線性代數課程中通常教授的線性變換核心概念。如果你需要進一步說明或更多範例，請告訴我！