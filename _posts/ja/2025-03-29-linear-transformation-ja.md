---
audio: false
generated: true
lang: ja
layout: post
title: 線形変換
translated: true
type: note
---

**定義、例、行列表現、核、像、性質（単射性、全射性）**

線形変換は線形代数の基礎であり、ベクトル空間と行列の間の架け橋を提供します。このチュートリアルでは以下を扱います：
- 線形変換の**定義**
- 一般的な線形変換の**例**
- 線形変換の**行列表現**
- **核（零空間）**と**像（値域）**
- **性質**: 単射性（1対1）と全射性（上への写像）

---

## **1. 線形変換の定義**
体 \\( \mathbb{F} \\)（通常 \\( \mathbb{R} \\) または \\( \mathbb{C} \\)）上の2つのベクトル空間 \\( V \\) と \\( W \\) の間の**線形変換**（または線形写像）は、以下を満たす関数 \\( T: V \to W \\) です：
1. **加法性**:
   \\[
   T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \quad \forall \mathbf{u}, \mathbf{v} \in V
   \\]
2. **斉次性（スカラー倍）**:
   \\[
   T(c \mathbf{v}) = c T(\mathbf{v}) \quad \forall c \in \mathbb{F}, \mathbf{v} \in V
   \\]

**重要な考え方**: 線形変換はベクトルの加法とスカラー倍を保存します。

---

## **2. 線形変換の例**

### **(a) 零変換**
- 全ての \\( \mathbf{v} \in V \\) に対して \\( T(\mathbf{v}) = \mathbf{0} \\)。

### **(b) 恒等変換**
- 全ての \\( \mathbf{v} \in V \\) に対して \\( T(\mathbf{v}) = \mathbf{v} \\)。

### **(c) \\( \mathbb{R}^2 \\) における回転**
- ベクトルを角度 \\( \theta \\) だけ回転:
  \\[
  T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
  \\]

### **(d) 微分（多項式空間）**
- \\( T: P_n \to P_{n-1} \\) で、\\( T(p(x)) = p'(x) \\) と定義。

### **(e) 行列の乗算**
- 固定された \\( m \times n \\) 行列 \\( A \\) に対して、\\( T: \mathbb{R}^n \to \mathbb{R}^m \\) を \\( T(\mathbf{x}) = A\mathbf{x} \\) で定義。

---

## **3. 線形変換の行列表現**
すべての線形変換 \\( T: \mathbb{R}^n \to \mathbb{R}^m \\) は、次を満たす \\( m \times n \\) 行列 \\( A \\) で表現できます：
\\[
T(\mathbf{x}) = A\mathbf{x}
\\]

### **行列 \\( A \\) を見つける方法**
1. \\( T \\) を \\( \mathbb{R}^n \\) の標準基底ベクトル \\( \mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\) に適用する。
2. \\( A \\) の列は \\( T(\mathbf{e}_1), T(\mathbf{e}_2), \dots, T(\mathbf{e}_n) \\) である。

**例**:
\\( T: \mathbb{R}^2 \to \mathbb{R}^2 \\) を次で定義する：
\\[
T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2x + y \\ x - 3y \end{pmatrix}
\\]
- \\( T(\mathbf{e}_1) = T(1, 0) = (2, 1) \\) を計算
- \\( T(\mathbf{e}_2) = T(0, 1) = (1, -3) \\) を計算
- したがって、行列 \\( A \\) は：
  \\[
  A = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}
  \\]

---

## **4. 核（零空間）と像（値域）**

### **(a) 核（零空間）**
\\( T \\) の**核**は、\\( \mathbf{0} \\) に写像される \\( V \\) 内のすべてのベクトルの集合です：
\\[
\ker(T) = \{ \mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0} \}
\\]

**性質**:
- \\( \ker(T) \\) は \\( V \\) の部分空間です。
- \\( T \\) が**単射（1対1）**であるための必要十分条件は \\( \ker(T) = \{ \mathbf{0} \} \\) です。

**例**:
\\( T(\mathbf{x}) = A\mathbf{x} \\)、ただし \\( A = \begin{pmatrix} 1 & 2 \\ 3 & 6 \end{pmatrix} \\) の場合、
\\[
\ker(T) = \text{Span} \left\{ \begin{pmatrix} -2 \\ 1 \end{pmatrix} \right\}
\\]

### **(b) 像（値域）**
\\( T \\) の**像**は、\\( W \\) 内のすべての出力の集合です：
\\[
\text{Im}(T) = \{ T(\mathbf{v}) \mid \mathbf{v} \in V \}
\\]

**性質**:
- \\( \text{Im}(T) \\) は \\( W \\) の部分空間です。
- \\( T \\) が**全射（上への写像）**であるための必要十分条件は \\( \text{Im}(T) = W \\) です。

**例**:
\\( T(\mathbf{x}) = A\mathbf{x} \\)、ただし \\( A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix} \\) の場合、
\\[
\text{Im}(T) = \text{Span} \left\{ \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \right\}
\\]

---

## **5. 性質: 単射性と全射性**

### **(a) 単射性（1対1）**
線形変換 \\( T \\) が**単射**であるとは：
\\[
T(\mathbf{u}) = T(\mathbf{v}) \implies \mathbf{u} = \mathbf{v}
\\]
**判定法**:
- \\( T \\) が単射 \\( \iff \ker(T) = \{ \mathbf{0} \} \\)。
- \\( \dim(V) < \dim(W) \\) の場合、\\( T \\) は単射でない可能性がある。

### **(b) 全射性（上への写像）**
線形変換 \\( T \\) が**全射**であるとは：
\\[
\forall \mathbf{w} \in W, \exists \mathbf{v} \in V \text{ such that } T(\mathbf{v}) = \mathbf{w}
\\]
**判定法**:
- \\( T \\) が全射 \\( \iff \text{Im}(T) = W \\)。
- \\( \dim(V) > \dim(W) \\) の場合、\\( T \\) は全射でない可能性がある。

### **(c) 階数・退化次数の定理**
\\( T: V \to W \\) に対して、
\\[
\dim(V) = \dim(\ker(T)) + \dim(\text{Im}(T))
\\]
- **階数** \\( = \dim(\text{Im}(T)) \\)
- **退化次数** \\( = \dim(\ker(T)) \\)

**例**:
\\( T: \mathbb{R}^3 \to \mathbb{R}^2 \\) で \\( \dim(\ker(T)) = 1 \\) の場合、\\( \dim(\text{Im}(T)) = 2 \\)。

---

## **まとめ**

| 概念 | 定義 | 主な性質 |
|---------|------------|--------------|
| **線形変換** | \\( T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \\) かつ \\( T(c\mathbf{v}) = cT(\mathbf{v}) \\) | 線形構造を保存する |
| **行列表現** | \\( T(\mathbf{x}) = A\mathbf{x} \\)、ただし \\( A \\) の列は \\( T(\mathbf{e}_i) \\) | 変換を符号化する |
| **核** | \\( \ker(T) = \{ \mathbf{v} \mid T(\mathbf{v}) = \mathbf{0} \} \\) | 単射性を測る |
| **像** | \\( \text{Im}(T) = \{ T(\mathbf{v}) \mid \mathbf{v} \in V \} \\) | 全射性を測る |
| **単射性** | \\( \ker(T) = \{ \mathbf{0} \} \\) | 1対1 |
| **全射性** | \\( \text{Im}(T) = W \\) | 上への写像 |

---

## **練習問題**
1. \\( T(x, y, z) = (2x - y, y + 3z) \\) の行列表現を求めよ。
2. \\( T(\mathbf{x}) = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \mathbf{x} \\) が単射/全射かどうかを判定せよ。
3. \\( T(x, y) = (x + y, 2x - y, x) \\) に対する \\( \ker(T) \\) と \\( \text{Im}(T) \\) を計算せよ。

---

このチュートリアルは、大学の線形代数の授業で通常教えられる線形変換の核心的な概念をカバーしています。さらなる説明や追加の例が必要な場合はお知らせください！