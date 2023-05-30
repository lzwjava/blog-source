---
layout: post
title: "我终于明白了神经网络是如何工作的"
usemathjax: true
---

让我们直接讨论神经系统工作的核心。也就是说，反向传播算法：

1. 输入x： 为输入层设置相应的激活值$a^{1}$。
2. 前馈式： 对于每个l=2,3,...,L计算$$z^{l} = w^l a^{l-1}+b^l$$和$$a^{l} = \sigma(z^{l})$$
3. 输出误差$$delta^{L}$$： 计算矢量 $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$
4. 反向传播误差： 对于每个l=L-1,L-2,...,2，计算$$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$
5. 输出： 成本函数的梯度由 $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$ 和 $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$ 给出。


这是从迈克尔-尼尔森的《神经网络与深度学习》一书中抄来的。这是不是让人不知所措？在你第一次看到它时可能是这样。但在围绕它研究了一个月后，就不会了。让我解释一下。

## 输入

一共有5个阶段。第一阶段是输入。这里我们用手写的数字作为输入。我们的任务是识别它们。一个手写的数字有784个像素，即28*28。在每个像素中，都有一个灰度值，范围是0到255。因此，激活意味着我们使用一些函数来激活它，把它的原始值变成一个新的值，以便于处理。

例如，我们现在有1000张784像素的图片。我们现在训练它来识别它们所显示的数字。我们现在有100张图片来测试这个学习效果。如果程序能够识别97张图片的数字，我们就说它的准确率是97%。

因此，我们将在这1000张图片中进行循环，以训练出权重和偏差。每当我们给它一张新的图片来学习时，我们就会使权重和偏置更加正确。

一个批次的训练结果将反映在10个神经元中。这里，10个神经元代表从0到9，其数值范围是0到1，以表示他们对其准确性的信心。

而输入是784个神经元。我们怎样才能将784个神经元减少到10个神经元？事情是这样的。让我们假设我们有两个层。这个层是什么意思？那就是第一层，我们有784个神经元。在第二层，我们有10个神经元。

我们给784个神经元中的每个神经元一个权重，比如、 

$$w_1, w_2, w_3, w_4, ... , w_{784}$$

并给第一层一个偏置，即$$b_1$$。

于是对于第二层的第一个神经元，它的值是：

$$w_1*a_1 + w_2*a_2+...+ w_{784}*a_{784}+b_1$$

但这些权重和偏置是针对$$neuron^2_{1}$$(第二层的第一个)的。对于$$neuron^2_{2}$$来说，我们需要另一组权重和一个偏置。

那么，sigmoid函数呢？我们用sigmoid函数把上面的值从0映射到1。

$$
\begin{eqnarray} 
  \sigma(z) \equiv \frac{1}{1+e^{-z}}.
\end{eqnarray}
$$

$$
\begin{eqnarray} 
  \frac{1}{1+\exp(-\sum_j w_j x_j-b)}.
\end{eqnarray}
$$

我们也使用sigmoid函数来激活第一层。也就是说，我们把这个灰度值改为从0到1的范围。所以现在，每一层的每个神经元都有一个从0到1的值。

所以现在对于我们的两层网络，第一层有784个神经元，第二层有10个神经元。我们训练它以获得权重和偏置。

我们有784*10个权重和10个偏置。在第二层，对于每个神经元，我们将使用784个权重和1个偏置来计算其值。这里的代码像、 

```python
    def __init__(self, sizes)：
        self.num_layers = len( sizes)
        self.size = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]] 。
        self.weights = [np.random.randn(y, x)
                        for x, y in zip( sizes[:-1], sizes[1:])]
```

## 前馈

> 前馈： 对于每个l=2,3,...,L计算$$z^{l} = w^l a^{l-1}+b^l$$和$$a^{l} = \sigma(z^{l})$$

注意这里，我们使用最后一层的值，即$a^{l-1}$和当前层的权重$w^l$及其偏置$b^l$来做sigmoid，得到当前层的值，$a^{l}$。

代码：

```python
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights].
        # 前馈式
        激活 = x
        激活 = [x］ 
        zs = [] 
        for b, w in zip(self.biases, self.weights)：
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
```


## 输出错误

> 输出误差$$delta^{L}$$： 计算矢量 $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$

让我们看看$$nabla$意味着什么。

> Del，或称nabla，是数学中（特别是在矢量微积分中）使用的一种矢量微分算子，通常用nabla符号∇表示。

$$
\begin{eqnarray}
  w_k & \rightarrow & w_k' = w_k-\eta \frac{\partial C}{\partial w_k} \\
  b_l & \rightarrow & b_l' = b_l-\eta \frac{\partial C}{\partial b_l}
\end{eqnarray}
$$

这里$$\eta$$是学习率。我们使用的导数是C与权重和偏差各自的导数，也就是它们之间的速率变化。这就是下面的`sigmoid_prime`。

代码：

```python
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
```

```python
    def cost_derivative(self, output_activations, y):
        return (output_activations-y)
```

## 反向传播误差

> 反向传播误差： 对于每个l=L-1,L-2,...,2，计算$$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$

```python
     for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)
```

## 输出

> 输出： 成本函数的梯度由 $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$ 和 $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$ 给出。

```python
    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
```

## 最后

这是一篇短文。而且在大多数段落里，它只是显示了代码和数学公式。但对我来说，这足够了。在写这篇文章之前，我不太明白。在写完或只是复制了代码和书中的片段后，我明白了大部分内容。在从王垠老师那里获得信心，阅读了*神经网络和深度学习*这本书的大约30%，听了Andrej Karpathy的斯坦福讲座和Andrew Ng的部分课程，与我的朋友Qi讨论，捣鼓Anaconda、numpy和Theano库使书上多年前的代码能够工作，现在我明白了。

其中的一个关键点是维度。我们应该知道每个符号和变量的维度。而整个代码只是做可微分的计算。让我们以王垠的引言结束吧：

> 机器学习真的很有用，甚至可以说是优美的理论，因为它根本就是改头换面之后的微积分！它是牛顿，莱布尼兹古老而伟大的理论，以更加简单，优雅而强大的形式出现。机器学习基本就是利用微积分求导，拟合一些函数，深度学习就是拟合更加复杂的函数。

> 人工智能里面没有什么“智能”，神经网络里面也没有什么“神经”，机器学习里面也没有什么“学习”，深度学习里面也没有什么“深度”。这里面真正有效的东西，叫做“微积分”。所以我宁愿把这个领域叫做“可求导计算”（differentiable computing），构建模型的过程叫做“可求导编程”（differentiable programming）。
