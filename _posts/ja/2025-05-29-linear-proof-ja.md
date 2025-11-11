---
audio: false
generated: true
lang: ja
layout: post
title: 線型独立性の証明
translated: true
type: note
---

### 翻訳:

23. ベクトル \\( \alpha_1, \alpha_2, \alpha_3 \\) が線形独立であるとき、ベクトル \\( \beta_1 = \alpha_1 + 2\alpha_2 \\), \\( \beta_2 = -\alpha_1 + \alpha_2 - 3\alpha_3 \\), \\( \beta_3 = 3\alpha_1 + 6\alpha_3 \\) が線形従属であることを証明せよ。

### 解答:
ベクトル \\( \beta_1, \beta_2, \beta_3 \\) が線形従属であることを証明するには、すべてがゼロではないスカラー \\( c_1, c_2, c_3 \\) が存在して、次式が成り立つことを示せばよい：

\\[ c_1 \beta_1 + c_2 \beta_2 + c_3 \beta_3 = 0 \\]

与えられた式：
\\[ \beta_1 = \alpha_1 + 2\alpha_2 \\]
\\[ \beta_2 = -\alpha_1 + \alpha_2 - 3\alpha_3 \\]
\\[ \beta_3 = 3\alpha_1 + 6\alpha_3 \\]

次式を満たす定数 \\( c_1, c_2, c_3 \\) を見つける必要がある：

\\[ c_1 (\alpha_1 + 2\alpha_2) + c_2 (-\alpha_1 + \alpha_2 - 3\alpha_3) + c_3 (3\alpha_1 + 6\alpha_3) = 0 \\]

これは次のように書き直せる：

\\[ (c_1 - c_2 + 3c_3)\alpha_1 + (2c_1 + c_2)\alpha_2 + (-3c_2 + 6c_3)\alpha_3 = 0 \\]

\\( \alpha_1, \alpha_2, \alpha_3 \\) は線形独立であるため、\\( \alpha_1, \alpha_2, \alpha_3 \\) の係数はそれぞれゼロでなければならない：

1. \\( c_1 - c_2 + 3c_3 = 0 \\)
2. \\( 2c_1 + c_2 = 0 \\)
3. \\( -3c_2 + 6c_3 = 0 \\)

この連立方程式を解く：

式2より：
\\[ 2c_1 + c_2 = 0 \implies c_2 = -2c_1 \\]

式3より：
\\[ -3c_2 + 6c_3 = 0 \implies -3(-2c_1) + 6c_3 = 0 \implies 6c_1 + 6c_3 = 0 \implies c_3 = -c_1 \\]

\\( c_2 = -2c_1 \\) と \\( c_3 = -c_1 \\) を式1に代入する：
\\[ c_1 - (-2c_1) + 3(-c_1) = 0 \implies c_1 + 2c_1 - 3c_1 = 0 \implies 0 = 0 \\]

これは任意の \\( c_1 \\) に対して成り立つ。\\( c_1 = 1 \\) と選ぶ：

すると：
\\[ c_2 = -2 \\]
\\[ c_3 = -1 \\]

したがって、定数 \\( c_1 = 1, c_2 = -2, c_3 = -1 \\) が見つかり、次式が成り立つ：

\\[ 1 \cdot \beta_1 - 2 \cdot \beta_2 - 1 \cdot \beta_3 = 0 \\]

これにより、ベクトル \\( \beta_1, \beta_2, \beta_3 \\) が線形従属であることが証明された。