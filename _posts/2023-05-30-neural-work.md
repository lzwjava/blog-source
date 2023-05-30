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

This is copied from Michael Nelson's book *Neural Networks and Deep Learning*. Is it overwhelming? It might be at the first time you see it. But it is not after one month of studying around it. Let me explain.

There are 5 phases. The first phase is Input. Here we use handwritten digits as input. Our task is to recognize them. One handwritten digit has 784 pixels, which is 28*28. In every pixel, there is a grayscale value which is range from 0 to 255. So the activation means that we use some function to activate it, to change its original value to a new value for the convenience of processing. 

Say, we have now 1000 pictures of 784 pixels. We now train it to recognize what digit they show. We have now 100 pictures to test that learning effect. If the program can recognize 97 pictures' digits, we say its accuracy is 97%.

So we would loop over the 1000 pictures, to train out the weights and biases. We make weights and biases more correct every time we give it a new picture to learn. 

One batch training result is to be reflected in 10 neurons. Here, the 10 neurons represent from 0 to 9 and its value is range from 0 to 1 to indicate how their confidence about its accuracy. 

And the input is 784 neurons. How can we reduce 784 neurons to 10 neurons? Here is the thing. Let's suppose we have two layers. What does the layer mean? That is the first layer, we have 784 neurons. In the second layer, we have 10 neurons.

We give each neuron in the 784 neurons a weight, say, 

$$w_1, w_2, w_3, w_4, ... , w_{784}$$

And give the first layer, a bias, that is, $$b_1$$. 

And so for the first neuron in the second layer, its value is:

$$w_1*a_1 + w_2*a_2+...+ w_{784}*a_{784}+b_1$$

But these weights and a bias are for $$neuron^2_{1}$$(the first one in the second layer). To the $$neuron^2_{2}$$, we need another set of weights and a bias. 

How about the activation? 



