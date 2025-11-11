---
audio: false
generated: true
lang: hant
layout: post
title: 格拉姆－施密特過程
translated: true
type: note
---

**Gram-Schmidt 過程**是線性代數中的一種方法，用於將一組線性獨立向量轉換為跨越相同子空間的正交歸一向量集合。這在各種應用中特別有用，例如 QR 分解、解決最小平方問題，以及簡化向量空間中的計算。

### **關鍵概念**

- **線性獨立向量**：無法表示為彼此線性組合的向量。
- **正交向量**：彼此垂直的向量，意味著它們的點積為零。
- **正交歸一集合**：一組既正交且長度為單位長度（範數等於 1）的向量。

### **Gram-Schmidt 過程的目的**

- **正交化**：將一組向量轉換為每個向量都彼此正交的集合。
- **歸一化**：調整每個向量的長度，使其成為單位向量。
- **簡化**：在向量空間中的投影、分解和轉換計算中，使運算更為簡便。

### **過程詳解**

給定內積空間（如 \\( \mathbb{R}^n \\)）中的一組線性獨立向量 \\( \{ \mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \} \\)，Gram-Schmidt 過程按照以下步驟構建一個正交歸一集合 \\( \{ \mathbf{q}_1, \mathbf{q}_2, \ldots, \mathbf{q}_n \} \\)：

1. **初始化第一個向量**：
   \\[
   \mathbf{u}_1 = \mathbf{v}_1
   \\]
   歸一化得到：
   \\[
   \mathbf{q}_1 = \frac{\mathbf{u}_1}{\| \mathbf{u}_1 \|}
   \\]

2. **迭代正交化與歸一化**（針對 \\( k = 2 \\) 到 \\( n \\)）：
   - **正交化**：
     \\[
     \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \text{proj}_{\mathbf{q}_j} \mathbf{v}_k
     \\]
     其中投影 \\( \text{proj}_{\mathbf{q}_j} \mathbf{v}_k \\) 計算為：
     \\[
     \text{proj}_{\mathbf{q}_j} \mathbf{v}_k = (\mathbf{v}_k \cdot \mathbf{q}_j) \mathbf{q}_j
     \\]
   - **歸一化**：
     \\[
     \mathbf{q}_k = \frac{\mathbf{u}_k}{\| \mathbf{u}_k \|}
     \\]

### **詳細步驟**

1. **計算 \\( \mathbf{u}_1 \\) 和 \\( \mathbf{q}_1 \\)**：
   - \\( \mathbf{u}_1 = \mathbf{v}_1 \\)
   - \\( \mathbf{q}_1 = \frac{\mathbf{u}_1}{\| \mathbf{u}_1 \|} \\)

2. **對每個後續向量 \\( \mathbf{v}_k \\)**：
   - **減去所有先前 \\( \mathbf{q}_j \\) 上的投影**：
     \\[
     \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} (\mathbf{v}_k \cdot \mathbf{q}_j) \mathbf{q}_j
     \\]
   - **將 \\( \mathbf{u}_k \\) 歸一化得到 \\( \mathbf{q}_k \\)**：
     \\[
     \mathbf{q}_k = \frac{\mathbf{u}_k}{\| \mathbf{u}_k \|}
     \\]

### **範例**

讓我們將 Gram-Schmidt 過程應用於 \\( \mathbb{R}^2 \\) 中的向量 \\( \mathbf{v}_1 = [1, 1] \\) 和 \\( \mathbf{v}_2 = [1, 0] \\)。

1. **第一個向量**：
   - \\( \mathbf{u}_1 = \mathbf{v}_1 = [1, 1] \\)
   - 歸一化：
     \\[
     \| \mathbf{u}_1 \