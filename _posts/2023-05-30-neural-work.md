---
layout: post
title: "What I Know About Neural Work"
usemathjax: true
---

Let's directly discuss the core of neural work. That said, the backpropagation algorithm:

1. Input x: Set the corresponding activation $$a^{1}$$ for the input layer.
2. Feedforward: For each l=2,3,…,L compute $$z^{l} = w^l a^{l-1}+b^l$$ and $$a^{l} = \sigma(z^{l})$$
3. Output error $$\delta^{L}$$: Compute the vector $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$
4. Backpropagate the error: For each l=L−1,L−2,…,2, compute $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$
5. Output: The gradient of the cost function is given by $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$
and $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$

Is it overwhelming? It might be at the first time you see it. But it is not after one month of studying around it. Let me explain.

There are 5 phases. The first phase is Input...
