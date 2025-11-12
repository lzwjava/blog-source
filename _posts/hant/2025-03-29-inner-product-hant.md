---
audio: false
generated: true
lang: hant
layout: post
title: 內積空間
translated: true
type: note
---

當然！讓我們深入探討線性代數中「內積空間」的關鍵概念與主題。這些概念是理解向量空間及其幾何性質的基礎。

### 1. 點積
在 n 維空間中，兩個向量 \\( \mathbf{u} \\) 和 \\( \mathbf{v} \\) 的點積（或純量積）定義為：

\\[ \mathbf{u} \cdot \mathbf{v} = u_1v_1 + u_2v_2 + \cdots + u_nv_n \\]

點積衡量兩個向量指向相同方向的程度，並用於定義其他幾何性質，例如向量之間的角度。

### 2. 範數
向量 \\( \mathbf{v} \\) 的範數記為 \\( \|\mathbf{v}\| \\)，是衡量其長度或大小的指標。最常見的範數是歐幾里得範數，定義為：

\\[ \|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}} = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2} \\]

範數用於量化向量的大小，並在定義向量空間中的距離時至關重要。

### 3. 正交性
如果兩個向量 \\( \mathbf{u} \\) 和 \\( \mathbf{v} \\) 的點積為零，則它們是正交的：

\\[ \mathbf{u} \cdot \mathbf{v} = 0 \\]

正交向量彼此垂直。正交性是許多應用中的關鍵概念，例如投影和分解。

### 4. 正交規範基
向量空間的正交規範基是指每個向量具有單位範數（長度為 1）且與基中其他每個向量都正交的基。如果 \\( \{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\} \\) 是正交規範基，則：

\\[ \mathbf{v}_i \cdot \mathbf{v}_j = \begin{cases}
1 & \text{若 } i = j \\
0 & \text{若 } i \neq j
\end{cases} \\]

正交規範基簡化了許多計算，並用於各種應用中，包括傅立葉分析和訊號處理。

### 5. 格拉姆-施密特過程
格拉姆-施密特過程是一種將一組線性獨立向量轉換為正交規範集的演算法。給定一組向量 \\( \{\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n\} \\)，該過程按以下方式構造正交規範集 \\( \{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\} \\)：

1. 從 \\( \mathbf{v}_1 = \mathbf{u}_1 \\) 開始。
2. 對於每個後續向量 \\( \mathbf{u}_k \\)，計算：

\\[ \mathbf{v}_k = \mathbf{u}_k - \sum_{j=1}^{k-1} \text{proj}_{\mathbf{v}_j}(\mathbf{u}_k) \\]

其中 \\( \text{proj}_{\mathbf{v}_j}(\mathbf{u}_k) \\) 是 \\( \mathbf{u}_k \\) 在 \\( \mathbf{v}_j \\) 上的投影。

3. 將每個 \\( \mathbf{v}_k \\) 標準化為單位長度。

### 範例
讓我們考慮一個簡單的範例來說明這些概念。

假設我們在 \\( \mathbb{R}^2 \\) 中有兩個向量 \\( \mathbf{u} \\) 和 \\( \mathbf{v} \\)：

\\[ \mathbf{u} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}, \quad \mathbf{v} = \begin{pmatrix} -1 \\ 2 \end{pmatrix} \\]

#### 步驟 1：計算點積
\\[ \mathbf{u} \cdot \mathbf{v} = (3)(-1) + (4)(2) = -3 + 8 = 5 \\]

#### 步驟 2：計算範數
\\[ \|\mathbf{u}\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5 \\]
\\[ \|\mathbf{v}\| = \sqrt{(-1)^2 + 2^2} = \sqrt{1 + 4} = \sqrt{5} \\]

#### 步驟 3：檢查正交性
為了檢查 \\( \mathbf{u} \\) 和 \\( \mathbf{v} \\) 是否正交，我們已經計算了點積：

\\[ \mathbf{u} \cdot \mathbf{v} = 5 \neq 0 \\]

因此，\\( \mathbf{u} \\) 和 \\( \mathbf{v} \\) 並非正交。

### 結論
內積空間以及點積、範數、正交性和正交規範基等概念，對於理解向量空間的幾何性質至關重要。這些概念在物理學、工程學和數據科學中具有廣泛的應用，使其成為任何學習線性代數的人的關鍵知識。