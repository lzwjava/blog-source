---
lang: hant
layout: post
title: 禅与机器学习艺术
usemathjax: true
---

## 禅

一位年轻的爸爸周末正忙着学习神经网络。然而这个周末，他需要陪小女儿在公寓的游泳池里游泳。他躺在浅水区，望着高耸入云的公寓楼。突然，他想到，哇，它们真像神经网络。每个阳台就像一个神经元。一栋楼就像一层神经元。而一群楼组合在一起就成了一个神经网络。

然后他又想到了反向传播。反向传播所做的是将误差反向传播到神经元。在一次训练结束时，算法计算最后一层的输出与目标结果之间的误差。实际上，神经网络与神经元无关。它是关于可微分计算的。

写完《我终于搞懂神经网络是怎么回事了》之后，志伟发现自己还是没搞懂。懂不懂是个相对的事。就像费曼说的，没有人能100%确定任何事，我们只能相对确定某件事。所以志伟这么说，也是可以接受的。

于是，他找到了一种深入理解神经网络的方法，那就是每次复制几行示例代码，然后运行并打印变量。这些代码涉及一个简单的神经网络，用于识别手写数字。最近，他正在阅读的书名为《神经网络与深度学习》。因此，他将自己的GitHub仓库命名为“神经网络与志伟学习”。

在我们使用神经网络训练数据之前，首先需要加载数据。这部分工作花费了他一周的闲暇时间来完成。事情往往需要比预期更多的时间才能完成。但只要我们坚持不懈，就有能力完成许多看似困难的任务。

在机器学习领域中，mnist代表的是经过修改的美国国家标准与技术研究院数据库（Modified National Institute of Standards and Technology database）。因此，我们的数据加载器文件被命名为mnist_loader。我们在Python中使用print函数来打印大量的列表和ndarray数组。ndarray中的nd表示n维的（n-dimensional）。

除了打印之外，我们还必须使用matplotlib库来展示我们的数字。如下所示。

<div align="center"><img src="/assets/images/zen-neural/figure.png" width="30%" /><img/></div>

## 艺术

让我们看看更多的数字。

<div align="center">
<img src="/assets/images/zen-neural/figures.jpeg" width="100%" /><img/>
（图片来源：神经网络与深度学习）
</div>

有时能看到图片，而不是整天面对嘈杂的代码，这让人感到更加愉悦。

<div align="center">
<img src="/assets/images/zen-neural/layer.png" width="100%" /><img/>
（图片来源：《神经网络与深度学习》）
</div>

是不是看起来有点复杂？这里，我们可能在每一层都有过多的神经元。这让事情变得晦涩难懂。一旦你理解了，它其实非常简单。关于上图的第一件事是它有三层，输入层、隐藏层和输出层。一层连接到下一层。但是输入层的784个神经元如何变成第二层的15个神经元呢？隐藏层的15个神经元又如何变成输出层的10个神经元呢？

<div align="center">
<img src="/assets/images/zen-neural/simple-network.png" width="100%" /><img/>
</div>

</div>

这个网络简单得多。虽然志伟不想在这篇文章中包含任何数学公式，但这里的数学太简单太美了，无法隐藏。

$$w_1 \cdot a_1 + w_2 \cdot a_2 + \ldots + w_6 \cdot a_6 + b_1$$

假设我们将网络表示如下。

<div align="center"><img src="/assets/images/zen-neural/network-1.png" width="30%" /><img/></div>

因此，在第一层和第二层之间，我们有以下方程。

$$
\begin{eqnarray}
  w_1*a_1 +...+ w_6*a_6+b_1 = c_1 \\
  w_1*a_1 +...+ w_6*a_6+b_2 = c_2 \\
  w_1*a_1 +...+ w_6*a_6+b_3 = c_3 \\
  w_1*a_1 +...+ w_6*a_6+b_4 = c_4 
\end{eqnarray}  
$$

上述方程组表示的是四个线性方程，每个方程的形式都是权重 \( w_1 \) 到 \( w_6 \) 与对应变量 \( a_1 \) 到 \( a_6 \) 的乘积之和，再加上一个偏置项 \( b_i \)（其中 \( i = 1, 2, 3, 4 \)），等于一个常数 \( c_i \)。这种形式的方程组在机器学习中常见于线性模型的参数估计问题，其中 \( w \) 是权重，\( a \) 是特征，\( b \) 是偏置，\( c \) 是目标值。

在这里，方程1有一组权重，方程2有另一组权重。因此，方程1中的$w_1$与方程2中的$w_1$是不同的。于是，在第二层和第三层之间，我们有以下方程。

$$
\begin{eqnarray}
  w_1 \cdot c_1 + \ldots + w_4 \cdot c_4 + b_1 = d_1 \\
  w_1 \cdot c_1 + \ldots + w_4 \cdot c_4 + b_2 = d_2 \\
  w_1 \cdot c_1 + \ldots + w_4 \cdot c_4 + b_3 = d_3 
\end{eqnarray}  
$$

在第三层到最后一层中，我们有以下方程。

$$
  w_1 \cdot d_1 + w_2 \cdot d_2 + w_3 \cdot d_3 + b_1 = e_1
$$

上述方程存在一个问题，即其值不够简洁或规范。乘法和加法运算的结果范围相当广泛。我们希望将其限制在一个较小的范围内，比如0到1之间。因此，这里我们引入了Sigmoid函数。

$$
  \sigma(z) \equiv \frac{1}{1+e^{-z}}
$$

上式定义了Sigmoid函数，其中$\sigma(z)$表示Sigmoid函数的输出，$z$是输入变量。Sigmoid函数是一种常用的激活函数，它将输入值映射到0和1之间的范围内。具体来说，当$z$趋近于正无穷时，$\sigma(z)$趋近于1；当$z$趋近于负无穷时，$\sigma(z)$趋近于0；当$z=0$时，$\sigma(z)=0.5$。Sigmoid函数在机器学习和神经网络中广泛应用，特别是在二分类问题中，它可以用来表示概率或进行非线性变换。

我们不必被符号$\sigma$吓倒。它就像字母a一样，只是一个符号。如果我们输入0.5，它的值就是...

$$
 \frac{1}{1+e^{-0.5}} \approx 0.622459 
$$

翻译为：

$$
 \frac{1}{1+e^{-0.5}} \approx 0.622459 
$$

并且，

$$
\begin{eqnarray}
\frac{1}{1+e^{-(-100)}} \approx 3.72 \times e^{-44}  \\
\frac{1}{1+e^{-(-10)}} \approx 0.000045  \\
\frac{1}{1+e^{-(-1)}} \approx 0.26894  \\
\frac{1}{1+e^{-{0}}} = 0.5  \\
\frac{1}{1+e^{-10}} \approx 0.99995  \\
\frac{1}{1+e^{-100}} = 1
\end{eqnarray}
$$

这里的情况颇为有趣。在撰写本文之前，我并未知晓上述内容。现在，我对它在正常输入下的近似结果值有了一定的感觉。我们观察到，对于输入范围从0到$\infty$的情况，其值介于0.5到1之间；而对于输入范围从$-\infty$到0的情况，其值则落在0到0.5之间。

<div align="center"><img src="/assets/images/zen-neural/curve.png" width="100%" /><img/></div>

因此，关于上述方程，它们并不准确。最合适的表达应如下所示。

$$
\begin{eqnarray}
  \sigma(w_1*a_1 + ... + w_6*a_6+b_1) = c_1 \\
  \sigma(w_1*a_1 + ... + w_6*a_6+b_2) = c_2 \\
  \sigma(w_1*a_1 + ... + w_6*a_6+b_3) = c_3 \\
  \sigma(w_1*a_1 + ... + w_6*a_6+b_4) = c_4 
\end{eqnarray}
$$

所以对于第一个方程，它是这样的，

$$
   \frac{1}{1+e^{-(w_1*a_1 +...+ w_6*a_6+b_1)}}
$$

上式表示一个逻辑函数（Sigmoid函数），它将输入的特征加权和加上偏置项后，通过指数函数和倒数运算，映射到0到1之间的概率值。其中，\(w_1\)到\(w_6\)是权重系数，\(a_1\)到\(a_6\)是输入特征，\(b_1\)是偏置项。这个公式常用于二分类问题中，作为激活函数来预测某个事件发生的概率。

我们如何更新$w_1$的新权重呢？也就是说，

$$
    w_1 \rightarrow w_1' = w_1 - \Delta w
$$

对于这个方程，

$$w_1 \cdot a_1 + w_2 \cdot a_2 + \ldots + w_6 \cdot a_6 + b_1$$

其对 $w_1$ 的导数为 $a_1$。让我们给这个和赋予一个符号 $S_1$。

因此，

$$
\frac{\partial S_1}{\partial w_1} = a_1 , \frac{\partial S_1}{\partial w_2} = a_2, ...
$$

上述公式表示的是函数 \( S_1 \) 对权重 \( w_1 \) 和 \( w_2 \) 的偏导数分别等于 \( a_1 \) 和 \( a_2 \)。在机器学习和深度学习中，这种偏导数通常用于梯度下降算法中，以更新模型的权重，从而最小化损失函数。

导数表示变化率。这意味着对于$w_1$中的变化$\Delta w$，其结果$S_1$中的变化是$a_1 * \Delta w$。那么，我们如何逆转这样的计算呢？让我们来计算一下。

$$
\begin{eqnarray}
S_1' - S_1 = \Delta S_1  \\
\frac{\Delta S_1}{a_1} = \Delta w \\
w_1- \Delta w = w_1'
\end{eqnarray}
$$

链式法则解释了$f(g(x))$的导数是$f'(g(x))⋅g'(x)$。

因此，在这里，

$$
\begin{eqnarray}
f(z) = \sigma(z) = \frac{1}{1+e^{-z}} \\
g(x) = w_1 \cdot a_1 + \ldots + w_6 \cdot a_6 + b_1
\end{eqnarray}
$$

而sigmoid函数的导数是，

$$
\sigma'(z) = \frac{\sigma(z)}{1-\sigma(z)}
$$

因此，$f(g(w_1))$ 的导数是 $\frac{\sigma(z)}{1-\sigma(z)} * a_1$。

所以，

$$
\begin{eqnarray}
\frac{\sigma(z)}{1-\sigma(z)} * a_1 * \Delta w = \Delta C \\
\Delta w = \frac{\Delta C}{\frac{\sigma(z)}{1-\sigma(z)} * a_1} 
\end{eqnarray}
$$

而对于偏置$b_1$，

$$
\begin{eqnarray}
g'(b_1) = 1 \\
\frac{\sigma(z)}{1-\sigma(z)} * \Delta b = \Delta C \\
\Delta b = \frac{\Delta C}{\frac{\sigma(z)}{1-\sigma(z)}}
\end{eqnarray}
$$

## 代码

打印变量的方法非常实用且简单，尽管如今人们发明了Jupyter Notebook来完成此类任务。正如志伟之前提到的，理解神经网络的关键之一在于我们必须关注维度。

```python
def print_shape(array):
    arr = np.array(array)
    print(arr.shape)
    
print(len(test_data[0][0])) # 10
print_shape(training_results[0]) # (784, 1)
print(list(training_data)[0:1]) # <class 'list'>
```

翻譯如下：

```python
def 打印形狀(陣列):
    arr = np.array(陣列)
    print(arr.shape)
    
print(len(test_data[0][0])) # 10
打印形狀(training_results[0]) # (784, 1)
print(list(training_data)[0:1]) # <class 'list'>
```

由于志伟刚刚完成了数据加载部分，他将继续采用复制几行代码并打印变量的方式，来学习神经网络的实际操作部分。你可以在这里跟进学习进度：https://github.com/lzwjava/neural-networks-and-zhiwei-learning。

在编程过程中，我多次陷入了困境。尽管那段代码看起来非常简单，但经过一次又一次地尝试理解，我仍然失败了。于是，我决定跳出当前代码的细节，从更高的层次去审视它，思考作者为何要那样编写那部分代码。突然间，我恍然大悟。以下是那段代码：
```python
def load_data_wrapper():
    tr_d, va_d, te_d = load_data()
```

    training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)

    訓練輸入 = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    訓練結果 = [vectorized_result(y) for y in tr_d[1]]
    訓練數據 = zip(訓練輸入, 訓練結果)

    validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
    validation_data = zip(validation_inputs, va_d[1])

翻譯：

    驗證輸入 = [np.reshape(x, (784, 1)) for x in va_d[0]]
    驗證數據 = zip(驗證輸入, va_d[1])

    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])
    return (training_data, validation_data, test_data)

翻譯：

    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])
    return (training_data, validation_data, test_data)

```python
def vectorized_result(j):
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e
```

這段程式碼的功能是將一個數字 `j` 轉換為一個 10 維的向量，其中只有第 `j` 個位置的值為 1.0，其餘位置的值為 0.0。這種表示方式通常用於將類別標籤轉換為 one-hot 編碼的形式，以便在機器學習模型中使用。

此处，变量的维度颇为复杂。然而，当我们考虑到作者的初衷时，便有了些许线索。瞧，这段代码由三个相似的部分组成，尽管变量名各异，但每一部分几乎如出一辙。现在，对我来说，这一切显得格外顺眼——zip函数、对列表进行的“for”操作，以及reshape函数。理解就在这数百次打印变量、试图弄清变量值为何如此的过程中逐渐累积起来。

而志伟总是发现错误非常有价值。比如下面的代码，他遇到了很多错误，例如，

* TypeError: 图像数据的形状无效 (784,)
* ValueError: 尝试用序列设置数组元素时出错。请求的数组在二维之后具有不均匀的形状。检测到的形状为 (1, 2) 加上不均匀部分。

错误堆栈跟踪，宛如一首优美的诗篇。

此外，当我们在Visual Studio Code中格式化值输出时，其可读性大大提高。

```python
[陣列([[0.92733598],
       [0.01054299],
       [1.0195613],
       ...
       [0.67045368],
       [-0.29942482],
       [-0.35010666]]),
 陣列([[-1.87093344],
        [-0.18758503],
        [1.35792778],
        ...
        [0.36830578],
        [0.61671649],
        [0.67084213]])]
```

謝謝你的閱讀。

---

注：部分图片摘自《神经网络与深度学习》一书。