---
layout: post
title: "Zen and the Art of Machine Learning - Draft"
usemathjax: true
---

<div align="center"><img src="/assets/images/zen-neural/building.jpg" width="100%" /><img/></div>

A young dad is busy learning Neural networks at the weekend. However, this weekend, he needed to accompany his baby daughter to swim in the pool of the apartment complex. He laid down in the shallow water and watched the top apartment buildings rising top to the sky. And suddenly he thought, Wow, they are a lot like neural networks. Every balcony is just like a neuron. And a building is like a layer of neurons. And a group of buildings are combined to be a neural network.

He then thought about backpropagation. What backpropagation does is to backpropagate the errors to neurons? At the end of one-time training, the algorithm calculates the error between the output of the last layer to the target result. Actually, neural networks have nothing to do with neurons. It is about differentiable computing.

After writing down the article "I Finally Understand How Neural Network Works", he found that he still didn't understand. Understanding is a relative thing. As Richard Feynman points out something like nobody can be 100% sure about anything, we can only be relatively sure about something. So it is acceptable for Zhiwei to say so.

So he figured out a way to understand the Neural Networks deeply by using the way to copy several lines of example code every time, then run it and print variables. It is about the simple neural network to recognize the handwritten digits. The book he is reading recently is titled *Neural Networks and Deep Learning*. So he gives his GitHub repository the name *Neural Networks and Zhiwei Learning*. 

Before we use Neural Network to train our data, we need to load data first. This part costs him a week of leisure time to do it. Things are always needed more time to get them done. But as long as we don't give up, we are capable to do pretty many things.

The mnist in the Machine learning area stands for Modified National Institute of Standards and Technology database. So our data loader file is called minst_loader. We use the print function in Python to print a lot of lists and arrays of ndarray. The nd in ndarray means n-dimensional. 

Besides print, we must use the matplotlib library to show our digits. Like below.

<div align="center"><img src="/assets/images/zen-neural/figure.png" width="30%" /><img/></div>

Let's see more digits.

<div align="center"><img src="/assets/images/zen-neural/figures.jpeg" width="100%" /><img/></div>

It is more joyful when you sometimes can see pictures instead of facing around the noisy codes all day long.

<div align="center"><img src="/assets/images/zen-neural/layer.png" width="100%" /><img/></div>

Does it seem complicated? Here, we may have too many neurons in each layer. And it makes things obscure. It is actually very simple once you understood it. First thing about the above picture is that it has three layers, the input layer, the hidden layer and the output layer. And one layer connects the next layer. But how can 784 neurons in the input layer change to the 15 neurons in the second layer? And how can 15 neurons in the hidden layer change to the 10 neurons in the output layer?

<div align="center"><img src="/assets/images/zen-neural/simple-network.png" width="100%" /><img/></div>

This network is much simpler. Though Zhiwei doesn't want to include any math formula in this article, here the math is too simple and beautiful to hide.

$$w_1*a_1 + w_2*a_2+...+ w_6*a_6+b_1$$

Suppose we indicate the network like below.

<div align="center"><img src="/assets/images/zen-neural/network-1.png" width="30%" /><img/></div>

So between the first layer and the second layer, we have the below equations.

$$
\begin{eqnarray}
  w_1*a_1 + w_2*a_2+...+ w_6*a_6+b_1 = c_1 \\
  w_1*a_1 + w_2*a_2+...+ w_6*a_6+b_2 = c_2 \\
  w_1*a_1 + w_2*a_2+...+ w_6*a_6+b_3 = c_3 \\
  w_1*a_1 + w_2*a_2+...+ w_6*a_6+b_4 = c_4 
\end{eqnarray}
$$

Here, Equation 1 has a group set of weights, Equation 2 has another group set of weights. So the $w_1$ in Equation 1 is different from the $w_1$ in Equation 2. And so between the second layer and the third layer, we have the below equations.

$$
\begin{eqnarray}
  w_1*c_1 + w_2*c_2+ w_3*c_3+ w_4*c_4+b_1 = d_1 \\
  w_1*c_1 + w_2*c_2+ w_3*c_3+ w_4*c_4+b_2 = d_2 \\
  w_1*c_1 + w_2*c_2+ w_3*c_3+ w_4*c_4+b_3 = d_3 
\end{eqnarray}
$$

And in the third layer to the last layer, we have the below equations.

$$
\begin{eqnarray}
  w_1*d_1 + w_2*d_2+ w_3*d_3+ b_1 = e_1 \\
\end{eqnarray}
$$

The one problem with the above equations is that the value is not simple or formal enough. The range of the value of multiplication and addition is quite large. We want it constrained in a small range, say, 0 to 1. So here, we have the Sigmoid function. 

$$
\begin{eqnarray} 
  \sigma(z) \equiv \frac{1}{1+e^{-z}}
\end{eqnarray}
$$

We don't need to be intimidated by the sigma symbol $\sigma$. It is just a symbol just like the symbol a. If we give it the input as 0.5, its value is 

$$
 \frac{1}{1+e^{-0.5}} \approx 0.622459 
$$

And,

$$
\frac{1}{1+e^{-(-100)}} \approx 3.72*e^{-44}  \\
\frac{1}{1+e^{-(-10)}} \approx 0.000045  \\
\frac{1}{1+e^{-(-1)}} \approx 0.26894  \\
\frac{1}{1+e^{-{0}}} = 0.5  \\
\frac{1}{1+e^{-10}} \approx 0.99995  \\
\frac{1}{1+e^{-100}} = 1
$$

It is intriguing here. I don't know the above before I write this article. Now, I got a feeling about how its approximate result value for the normal input. And we observe that for the input that ranges from 0 to $\infty$, its value is from 0.5 to 1, and for the input that ranges from $-\infty$ to 0, its value is from 0 to 0.5.

<div align="center"><img src="/assets/images/zen-neural/curve.png" width="100%" /><img/></div>

So regarding the above equations, they are not accurate. The most proper ones should be like below.

$$
\begin{eqnarray}
  \sigma(w_1*a_1 + w_2*a_2+...+ w_6*a_6+b_1) = c_1 \\
  \sigma(w_1*a_1 + w_2*a_2+...+ w_6*a_6+b_2) = c_2 \\
  \sigma(w_1*a_1 + w_2*a_2+...+ w_6*a_6+b_3) = c_3 \\
  \sigma(w_1*a_1 + w_2*a_2+...+ w_6*a_6+b_4) = c_4 
\end{eqnarray}
$$

So for the first equation, it is that, 

$$
\begin{eqnarray}
   \frac{1}{1+e^{-(w_1*a_1 + w_2*a_2+...+ w_6*a_6+b_1)}}
\end{eqnarray}
$$

How can we update the new weight for $w_1$? That is, 

$$
\begin{eqnarray}
    w_1 & \rightarrow & w_1' = w_1- \Delta w \\
\end{eqnarray}
$$

To the equation, 

$$w_1*a_1 + w_2*a_2+...+ w_6*a_6+b_1$$

Its derivative to the $w_1$ is $a_1$. Let's give the sum the symbol $S_1$.

So, 

$$
\frac{\partial S_1}{\partial w_1} = a_1 , \frac{\partial S_1}{\partial w_2} = a_2, ...
$$

The derivate means the rate of change. It means that for the change $\Delta w$ in $w_1$, its change in the result $S_1$ is $a_1 * \Delta w$. And how can we reverse such a calculation? Let's calculate it.

$$
S_1' - S_1 = \Delta S_1  \\
\frac{\Delta S_1}{a_1} = \Delta w \\
w_1- \Delta w = w_1'
$$

And the chain rule explains that the derivative of $f(g(x))$ is $f'(g(x))⋅g'(x)$.

So here, 

$$
f(z) = \sigma(z) = \frac{1}{1+e^{-z}} \\
g(x) = w_1*a_1 + w_2*a_2+...+ w_6*a_6+b_1
$$

And the derivative of the sigmoid function is, 

$$
\sigma'(z) = \frac{\sigma(z)}{1-\sigma(z)}
$$

So the derivative of $f(g(w_1))$ is $\frac{\sigma(z)}{1-\sigma(z)} * a_1$.

So, 

$$
\frac{\sigma(z)}{1-\sigma(z)} * a_1 * \Delta w = \Delta C \\
\Delta w = \frac{\Delta C}{\frac{\sigma(z)}{1-\sigma(z)} * a_1} 
$$

And for the bias $b_1$, 

$$
g'(b_1) = 1 \\
\frac{\sigma(z)}{1-\sigma(z)} * \Delta b = \Delta C \\
\Delta b = \frac{\Delta C}{\frac{\sigma(z)}{1-\sigma(z)}}
$$
