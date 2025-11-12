---
audio: false
generated: true
lang: hant
layout: post
title: 格拉姆－施密特過程
translated: true
type: note
---

**Gram-Schmidt 過程**是一種在內積空間（通常為 \\(\mathbb{R}^n\\) 或 \\(\mathbb{C}^n\\)）中將一組線性獨立向量正交歸一化的方法。它將給定的基底轉換為**正交歸一基底**，其中向量彼此正交且具有單位長度。

---

### **演算法：Gram-Schmidt 過程**
給定內積空間中一組**線性獨立**向量 \\( \{v_1, v_2, \dots, v_n\} \\)，我們按以下步驟構建**正交歸一基底** \\( \{u_1, u_2, \dots, u_n\} \\)：

1. **步驟 1：計算第一個正交歸一向量**  
   \\[
   u_1 = \frac{v_1}{\|v_1\|}
   \\]
   
2. **步驟 2：使第二個向量與第一個正交並將其歸一化**  
   \\[
   v_2' = v_2 - \text{proj}_{u_1}(v_2) = v_2 - \frac{\langle v_2, u_1 \rangle}{\langle u_1, u_1 \rangle} u_1
   \\]
   \\[
   u_2 = \frac{v_2'}{\|v_2'\|}
   \\]

3. **步驟 3：對其餘向量重複此過程**  
   對於 \\( k = 3, \dots, n \\)：
   \\[
   v_k' = v_k - \sum_{j=1}^{k-1} \frac{\langle v_k, u_j \rangle}{\langle u_j, u_j \rangle} u_j
   \\]
   \\[
   u_k = \frac{v_k'}{\|v_k'\|}
   \\]

此處，\\( \text{proj}_{u_j}(v_k) = \frac{\langle v_k, u_j \rangle}{\langle u_j, u_j \rangle} u_j \\) 表示 \\( v_k \\) 在 \\( u_j \\) 上的投影。

---

### **範例：將 Gram-Sch