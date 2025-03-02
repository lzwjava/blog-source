---
audio: false
generated: false
lang: ja
layout: post
title: neural network
translated: true
usemathjax: true
---

ニューラルネットワークの核心に直接触れていきましょう。つまり、バックプロパゲーション（逆伝播）アルゴリズムについてです。

1. 入力 x: 入力層に対応する活性化 $$a^{1}$$ を設定します。
2. 順伝播: 各 l=2,3,…,L に対して、$$z^{l} = w^l a^{l-1}+b^l$$ と $$a^{l} = \sigma(z^{l})$$ を計算します。
3. 出力誤差 $$\delta^{L}$$: ベクトル $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$ を計算します。
4. 誤差の逆伝播: 各 l=L−1,L−2,…,2 に対して、$$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$ を計算します。
5. 出力: コスト関数の勾配は、$$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$ と $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$ で与えられます。

これはMichael Nelsonの著書『Neural Networks and Deep Learning』から引用したものです。圧倒されるでしょうか？初めて見たときはそうかもしれません。しかし、1か月ほど勉強すればそうではなくなります。説明させてください。

## 入力

5つのフェーズがあります。最初のフェーズは入力です。ここでは手書きの数字を入力として使用します。私たちのタスクはそれらを認識することです。1つの手書き数字は784ピクセル、つまり28*28で構成されています。各ピクセルには、0から255の範囲のグレースケール値があります。活性化とは、処理を容易にするために、何らかの関数を使用して元の値を新しい値に変更することを意味します。

例えば、784ピクセルの画像が1000枚あるとします。これを使って、画像が示す数字を認識するように訓練します。そして、学習効果をテストするために100枚の画像を使います。もしプログラムが97枚の画像の数字を正しく認識できた場合、その精度は97%であると言います。

したがって、1000枚の画像をループして、重みとバイアスを訓練します。新しい画像を学習させるたびに、重みとバイアスをより正確に調整していきます。

1回のバッチトレーニングの結果は、10個のニューロンに反映されます。ここで、10個のニューロンは0から9を表し、その値は0から1の範囲で、その精度に対する自信度を示します。

そして入力は784個のニューロンです。784個のニューロンを10個のニューロンに減らすにはどうすればいいでしょうか？ここで重要なのは、2つの層があると仮定することです。層とは何を意味するのでしょうか？最初の層には784個のニューロンがあり、2番目の層には10個のニューロンがあります。

784個のニューロンそれぞれに重みを与えます。例えば、

$$w_1, w_2, w_3, w_4, ... , w_{784}$$

そして、最初の層にバイアス、つまり $$b_1$$ を与えます。

そして、2層目の最初のニューロンの値は次のようになります：

$$w_1*a_1 + w_2*a_2+...+ w_{784}*a_{784}+b_1$$

しかし、これらの重みとバイアスは $$neuron^2_{1}$$（第2層の最初のニューロン）のためのものです。$$neuron^2_{2}$$ には、別の重みとバイアスのセットが必要です。

シグモイド関数はどうでしょうか？シグモイド関数を使用して、上記の値を0から1にマッピングします。

$$
\begin{eqnarray} 
  \sigma(z) \equiv \frac{1}{1+e^{-z}}
\end{eqnarray}
$$

$$
\begin{eqnarray} 
  \frac{1}{1+\exp(-\sum_j w_j x_j-b)}
\end{eqnarray}
$$

また、最初の層を活性化するためにシグモイド関数を使用します。これにより、グレースケールの値を0から1の範囲に変換します。これで、すべての層のすべてのニューロンが0から1の範囲の値を持つようになります。

さて、私たちの2層ネットワークでは、最初の層に784個のニューロンがあり、2番目の層には10個のニューロンがあります。重みとバイアスを取得するためにそれを訓練します。

784 * 10個の重みと10個のバイアスがあります。第2層では、各ニューロンに対して784個の重みと1個のバイアスを使用してその値を計算します。ここでのコードは次のようになります。

```python
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
```

このコードは、ニューラルネットワークの初期化を行うためのPythonのメソッドです。以下にその内容を日本語で説明します。

- `__init__(self, sizes)`: これはクラスのコンストラクタで、ニューラルネットワークの初期化を行います。`sizes`はネットワークの各層のニューロン数を表すリストです。
- `self.num_layers = len(sizes)`: ネットワークの層の数を`sizes`リストの長さから取得し、`num_layers`属性に保存します。
- `self.sizes = sizes`: ネットワークの各層のニューロン数を`sizes`属性に保存します。
- `self.biases = [np.random.randn(y, 1) for y in sizes[1:]]`: 各層のバイアスをランダムに初期化します。`sizes[1:]`は入力層を除いた層のニューロン数で、それぞれの層のバイアスは正規分布に従うランダムな値で初期化されます。
- `self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]`: 各層の重みをランダムに初期化します。`sizes[:-1]`と`sizes[1:]`はそれぞれ前の層と次の層のニューロン数で、それぞれの層の重みは正規分布に従うランダムな値で初期化されます。

このコードは、ニューラルネットワークの初期化を行うための基本的な部分であり、バイアスと重みをランダムに設定することで、ネットワークの学習が進むための基盤を提供します。

## フィードフォワード

> フィードフォワード: 各層 \( l = 2, 3, \ldots, L \) に対して、次のように計算します。
> $$z^{l} = w^l a^{l-1} + b^l$$
> そして
> $$a^{l} = \sigma(z^{l})$$

ここで注目すべきは、前の層の値、つまり $$a^{l-1}$$ と、現在の層の重み $$w^l$$ およびバイアス $$b^l$$ を使用して、シグモイド関数を適用し、現在の層の値 $$a^{l}$$ を取得している点です。

コード:

```python
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # 順伝播
        activation = x
        activations = [x] 
        zs = [] 
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
```
## 出力エラー

> 出力誤差 $$\delta^{L}$$: ベクトル $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$ を計算する

$$\nabla$$ の意味を見てみましょう。

> Del（デル）、またはナブラは、数学（特にベクトル解析）で使用される演算子で、ベクトル微分演算子として機能します。通常、ナブラ記号∇で表されます。

$$
\begin{eqnarray}
  w_k & \rightarrow & w_k' = w_k-\eta \frac{\partial C}{\partial w_k} \\
  b_l & \rightarrow & b_l' = b_l-\eta \frac{\partial C}{\partial b_l}
\end{eqnarray}
$$

上記の数式は、ニューラルネットワークにおける重み \( w_k \) とバイアス \( b_l \) の更新規則を示しています。ここで、\( \eta \) は学習率、\( C \) はコスト関数です。この更新規則は、勾配降下法を用いてネットワークのパラメータを最適化するためのものです。

ここで、$$\eta$$ は学習率です。C に対する重みとバイアスの微分、つまりそれらの間の変化率を使用します。これは以下の `sigmoid_prime` です。

コード:

```python
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
```

このコードは、ニューラルネットワークのバックプロパゲーション（逆伝播）アルゴリズムの一部です。以下に日本語で説明します。

- `delta` は、出力層の誤差を表します。これは、コスト関数の導関数 `self.cost_derivative(activations[-1], y)` と、シグモイド関数の導関数 `sigmoid_prime(zs[-1])` の積として計算されます。
- `nabla_b[-1]` は、出力層のバイアスに対する勾配を表し、`delta` をそのまま代入します。
- `nabla_w[-1]` は、出力層の重みに対する勾配を表し、`delta` と前の層の活性化値 `activations[-2]` の転置行列とのドット積として計算されます。

このコードは、ニューラルネットワークの学習において、誤差を逆伝播させて各パラメータ（重みとバイアス）の勾配を計算するために使用されます。

```python
    def cost_derivative(self, output_activations, y):
        return (output_activations-y)
```

このコードブロックは、Pythonで定義された関数 `cost_derivative` を示しています。この関数は、ニューラルネットワークの出力活性化値 `output_activations` と目標値 `y` の差を計算し、その結果を返します。この差は、コスト関数の導関数として使用されることが一般的です。

## 誤差を逆伝播させる

> 誤差を逆伝播する: 各層 \( l = L-1, L-2, \ldots, 2 \) に対して、次式を計算する:
> 
> \[
> \delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})
> \]

```python
     for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)
```

このコードは、ニューラルネットワークのバックプロパゲーション（逆伝播）アルゴリズムの一部です。各層の重みとバイアスの勾配を計算しています。具体的には、以下のように動作します：

1. `for l in range(2, self.num_layers):`  
   2番目の層から最後の層までループします。

2. `z = zs[-l]`  
   現在の層の入力（活性化関数を通す前の値）を取得します。

3. `sp = sigmoid_prime(z)`  
   シグモイド関数の導関数を計算します。

4. `delta = np.dot(self.weights[-l+1].transpose(), delta) * sp`  
   次の層の誤差を現在の層に伝播させ、シグモイド関数の導関数を掛け合わせて現在の層の誤差を計算します。

5. `nabla_b[-l] = delta`  
   現在の層のバイアスの勾配を更新します。

6. `nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())`  
   現在の層の重みの勾配を更新します。

7. `return (nabla_b, nabla_w)`  
   計算されたバイアスと重みの勾配を返します。

このコードは、ニューラルネットワークの学習プロセスにおいて、誤差を逆伝播させて各パラメータの勾配を計算するために使用されます。

## 出力

> 出力: コスト関数の勾配は次のように与えられます:
$$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$
そして
$$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$

```python
    def update_mini_batch(self, mini_batch, eta):
        # バイアスと重みの勾配を初期化
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        
        # ミニバッチ内の各データに対して逆伝播を行い、勾配を累積
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        
        # 重みとバイアスを更新
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
```

## 最終版

これは短い記事です。そして、その大部分はコードと数式を示しているだけです。しかし、私にとってはそれで十分です。これを書く前は、はっきりと理解していませんでした。書いたり、コードや本からスニペットをコピーしたりした後、その大部分を理解しました。Yin Wang先生からの自信を得て、*Neural Networks and Deep Learning*という本の約30%を読み、Andrej Karpathyのスタンフォード講義とAndrew Ngのコースを聞き、友人Qiと議論し、Anaconda、numpy、Theanoライブラリをいじって数年前のコードを動かすことで、今では理解しています。

重要なポイントの一つは、次元です。すべての記号と変数の次元を知る必要があります。そして、それは単に微分可能な計算を行うだけです。最後に、Yin Wangの引用で締めくくりましょう：

> 機械学習は非常に有用で、ある意味で美しい理論です。なぜなら、それは単に化粧を施した微積分学だからです！それはニュートンやライプニッツの古くて偉大な理論を、よりシンプルでエレガントで強力な形にしたものです。機械学習は基本的に微積分学を使って関数を導出し、フィットさせることであり、ディープラーニングはより複雑な関数をフィットさせることです。

> 人工知能には「知能」はなく、ニューラルネットワークには「ニューラル」はなく、機械学習には「学習」はなく、ディープラーニングには「深さ」はありません。ディープラーニングには「深さ」はないのです。この分野で実際に機能しているのは「微積分」と呼ばれるものです。ですから、私はこの分野を「微分可能な計算」と呼び、モデルを構築するプロセスを「微分可能なプログラミング」と呼ぶことを好みます。