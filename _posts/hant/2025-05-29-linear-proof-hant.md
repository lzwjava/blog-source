---
audio: false
generated: true
lang: hant
layout: post
title: 線性獨立性證明
translated: true
type: note
---

23. 已知向量 \\( \alpha_1, \alpha_2, \alpha_3 \\) 線性獨立，且向量 \\( \beta_1 = \alpha_1 + 2\alpha_2 \\)、\\( \beta_2 = -\alpha_1 + \alpha_2 - 3\alpha_3 \\)、\\( \beta_3 = 3\alpha_1 + 6\alpha_3 \\)。證明向量 \\( \beta_1, \beta_2, \beta_3 \\) 線性相關。

### 解答：
要證明向量 \\( \beta_1, \beta_2, \beta_3 \\) 線性相關，需證明存在不全為零的純量 \\( c_1, c_2, c_3 \\) 使得：

\\[ c_1 \beta_1 + c_2 \beta_2 + c_3 \beta_3 = 0 \\]

已知：
\\[ \beta_1 = \alpha_1 + 2\alpha_2 \\]
\\[ \beta_2 = -\alpha_1 + \alpha_2 - 3\alpha_3 \\]
\\[ \beta_3 = 3\alpha_1 + 6\alpha_3 \\]

需找出常數 \\( c_1, c_2, c_3 \\) 滿足：

\\[ c_1 (\alpha_1 + 2\alpha_2) + c_2 (-\alpha_1 + \alpha_2 - 3\alpha_3) + c_3 (3\alpha_1 + 6\alpha_3) = 0 \\]

改寫為：

\\[ (c_1 - c_2 + 3c_3)\alpha_1 + (2c_1 + c_2)\alpha_2 + (-3c_2 + 6c_3)\alpha_3 = 0 \\]

由於 \\( \alpha_1, \alpha_2, \alpha_3 \\) 線性獨立，\\( \alpha_1, \alpha_2, \alpha_3 \\) 的係數必須均為零：

1. \\( c_1 - c_2 + 3c_3 = 0 \\)
2. \\( 2c_1 + c_2 = 0 \\)
3. \\( -3c_2 + 6c_3 = 0 \\)

解此方程組：

由方程 2：
\\[ 2c_1 + c_2 = 0 \implies c_2 = -2c_1 \\]

由方程 3：
\\[ -3c_2 + 6c_3 = 0 \implies -3(-2c_1) + 6c_3 = 0 \implies 6c_1 + 6c_3 = 0 \implies c_3 = -c_1 \\]

將 \\( c_2 = -2c_1 \\) 與 \\( c_3 = -c_1 \\) 代入方程 1：
\\[ c_1 - (-2c_1) + 3(-c_1) = 0 \implies c_1 + 2c_1 - 3c_1 = 0 \implies 0 = 0 \\]

此式對任意 \\( c_1 \\) 均成立。取 \\( c_1 = 1 \\)：

則：
\\[ c_2 = -2 \\]
\\[ c_3 = -1 \\]

因此找到常數 \\( c_1 = 1, c_2 = -2, c_3 = -1 \\) 滿足：

\\[ 1 \cdot \beta_1 - 2 \cdot \beta_2 - 1 \cdot \beta_3 = 0 \\]

由此證明向量 \\( \beta_1, \beta_2, \beta_3 \\) 線性相關。