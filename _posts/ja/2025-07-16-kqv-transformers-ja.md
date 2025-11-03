---
audio: false
generated: false
image: false
lang: ja
layout: post
title: ニューラルネットワーク、トランスフォーマー、GPT
translated: true
---

### 目次

1. [TransformerにおけるKQVメカニズムをどう学んだか](#how-i-learned-the-kqv-mechanism-in-transformers)
   - クエリ、キー、バリュー行列はトークンの相互作用を表す
   - 理解には次元と形状を知る必要がある
   - 時間とともに初期の概念が明確になる
   - AI時代は豊富な学習リソースを提供する
   - 感動的なストーリーが継続的な学習のモチベーションになる

2. [ニューラルネットワークからGPTへ](#from-neural-network-to-gpt)
   - ゼロからニューラルネットワークを再現して理解する
   - Transformerは埋め込みとエンコーディングを介してテキストを処理する
   - 自己注意は単語間の類似性を計算する
   - 基礎的な講義を視聴し、コードを読む
   - プロジェクトや論文を通して好奇心に従う

3. [ニューラルネットワークの仕組み](#how-neural-network-works)
   - 逆伝播アルゴリズムは重みとバイアスを更新する
   - 入力データはネットワーク層を介して活性化される
   - 順伝播はシグモイドを介して層の出力を計算する
   - 誤差計算が学習調整を導く
   - 次元理解は理解のために重要である

## TransformerにおけるKQVメカニズムをどう学んだか

*2025.07.16*

[TransformerにおけるK, Q, Vメカニズム](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en)を読んで、K、Q、Vがどのように機能するのか、なんとなく理解できました。

QはQuery（クエリ）、KはKey（キー）、VはValue（バリュー）の略です。文章の場合、Queryは他のトークンに尋ねる必要があるトークンの値を格納する行列です。Keyはトークンの説明を表し、Valueはトークンの実際の意味行列を表します。

これらは特定の形状を持っているため、その次元と詳細を知る必要があります。

私はこれを2025年6月初旬頃に理解しました。最初にそれについて学んだのは2023年末頃でした。その時、[The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)のような記事を読みましたが、あまり理解できませんでした。

約2年後、今では理解しやすくなっていることに気づきました。この2年間、私はバックエンドの仕事と準学士号の試験準備に集中しており、機械学習についてあまり読んだり学んだりしていませんでした。しかし、運転中や他のことをしているときに、時々これらの概念について考えを巡らせていました。

これは時間の効果を思い出させます。私たちは一見しただけでは多くのことを理解できないかもしれませんが、それでも思考の出発点を刺激します。

時間が経つにつれて、知識や発見については、最初から物事を考えたり理解したりするのは難しいと感じました。しかし後になって、学ぶことや知ることは容易になるようです。

一つの理由は、AI時代では、疑問を解決するためにあらゆる詳細や側面に深く入り込むことができるため、学習が容易になることです。関連するAI動画も増えています。さらに重要なことは、[llama.cpp](https://github.com/ggml-org/llama.cpp)のように、多くの人々がその上で学習し、プロジェクトを構築しているのを目にするからです。

Georgi Gerganovの物語は感動的です。2021年頃から機械学習の学習者としてスタートし、AIコミュニティに強力な影響を与えました。

このようなことは何度も起こるでしょう。したがって、強化学習や最新のAI知識については、まだ多くの時間を割くことはできませんが、素早く学び、それらについてたくさん考えるための時間を見つけることができると思います。脳がその役割を果たすでしょう。

---

## ニューラルネットワークからGPTへ

*2023.09.28*

### YouTube動画

Andrej Karpathy - Let's build GPT: from scratch, in code, spelled out.

Umar Jamil - Attention is all you need (Transformer) - Model explanation (including math), Inference and Training

StatQuest with Josh Starmer - Transformer Neural Networks, ChatGPT's foundation, Clearly Explained!!!

Pascal Poupart - CS480/680 Lecture 19: Attention and Transformer Networks

The A.I. Hacker - Michael Phi - Illustrated Guide to Transformers Neural Network: A step-by-step explanation

### 学習方法

「Neural Networks and Deep Learning」という本の半分を読んだ後、手書き数字を認識するニューラルネットワークの例を再現し始めました。GitHubにリポジトリを作成しました。https://github.com/lzwjava/neural-networks-and-zhiwei-learning

それが本当に難しい部分です。コードをコピーせずにゼロから書くことができれば、非常によく理解していることになります。

私の再現コードには、update_mini_batchとbackpropの実装がまだ欠けています。しかし、データの読み込み、順伝播、評価の段階で変数を注意深く観察することで、ベクトル、次元、行列、オブジェクトの形状についてよりよく理解できました。

そして、GPTとTransformerの実装を学び始めました。単語埋め込みと位置エンコーディングによって、テキストは数値に変わります。その後、本質的には、手書き数字を認識する単純なニューラルネットワークと何ら変わりはありません。

Andrej Karpathyの「Let's build GPT」という講義は非常に優れています。彼は物事をうまく説明してくれます。

最初の理由は、本当にゼロから構築しているからです。最初にテキストがどのように生成されるかを見ます。それは少し曖昧でランダムです。2番目の理由は、Andrejが非常に直感的に物事を説明できることです。AndrejはnanoGPTプロジェクトを数ヶ月間行いました。

講義の質を判断する新しいアイデアがあります。著者は本当にこれらのコードを書けるのか？なぜ私は理解できないのか、著者はどのトピックを省略しているのか？これらの美しい図やアニメーションの他に、彼らの欠点や欠陥は何なのか？

機械学習のトピック自体に戻りましょう。Andrejが言及しているように、dropout、残差接続、Self-Attention、Multi-Head Attention、Masked Attention。

上記の動画をさらに見ることで、少し理解し始めました。

sin関数とcos関数による位置エンコーディングによって、いくつかの重みを得ます。単語埋め込みによって、単語を数値に変換します。

$$
    PE_{(pos,2i)} = sin(pos/10000^{2i/d_{model}}) \\
    PE_{(pos,2i+1)} = cos(pos/10000^{2i/d_{model}}) 
$$

> The pizza came out of the oven and it tasted good.

この文では、アルゴリズムは「it」がピザを指すのかオーブンを指すのかをどうやって知るのでしょうか？文中のすべての単語間の類似性をどうやって計算するのでしょうか？

私たちは一連の重みを求めています。Transformerネットワークを使用して翻訳タスクを実行する場合、文を入力するたびに、別の言語の対応する文を出力できます。

ここでのドット積について。ここでドット積を使用する一つの理由は、ドット積がベクトルのすべての数値を考慮するからです。もし二乗ドット積を使用したらどうなるでしょうか？まず数値の二乗を計算し、それからドット積を行います。もし何らかの逆ドット積を行ったらどうなるでしょうか？

ここでのマスクについて、行列の半分を負の無限大に変更します。そしてsoftmaxを使用して値を0から1の範囲にします。左下の数値を負の無限大に変更したらどうなるでしょうか？

### 計画

引き続きコードや論文を読み、動画を視聴します。ただ楽しんで、好奇心に従います。

https://github.com/karpathy/nanoGPT

https://github.com/jadore801120/attention-is-all-you-need-pytorch

---

## ニューラルネットワークの仕組み

*2023.05.30*

ニューラルネットワークの核心について直接議論しましょう。つまり、逆伝播アルゴリズムです。

1. 入力 x: 入力層に対応する活性化 $$a^{1}$$ を設定します。
2. 順伝播: 各 l=2,3,…,L に対して $$z^{l} = w^l a^{l-1}+b^l$$ と $$a^{l} = \sigma(z^{l})$$ を計算します。
3. 出力誤差 $$\delta^{L}$$: ベクトル $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$ を計算します。
4. 誤差の逆伝播: 各 l=L−1,L−2,…,2 に対して $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$ を計算します。
5. 出力: コスト関数の勾配は $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$ と $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$ で与えられます。

これはMichael Nelsonの著書「Neural Networks and Deep Learning」から引用したものです。圧倒されるでしょうか？初めて見たときはそうかもしれません。しかし、1ヶ月ほど勉強すればそうではありません。説明させてください。

### 入力

5つのフェーズがあります。最初のフェーズは入力です。ここでは手書き数字を入力として使用します。私たちのタスクは、それらを認識することです。1つの手書き数字は784ピクセル、つまり28*28です。各ピクセルには、0から255の範囲のグレースケール値があります。したがって、活性化とは、何らかの関数を使用してそれを活性化し、処理の便宜のために元の値を新しい値に変更することを意味します。

例えば、現在、784ピクセルの画像を1000枚持っているとします。私たちは、それがどの数字を示しているかを認識するように訓練します。現在、その学習効果をテストするための画像を100枚持っています。プログラムが97枚の画像の数字を認識できれば、その精度は97%であると言えます。

したがって、1000枚の画像をループして、重みとバイアスを訓練します。新しい画像を学習させるたびに、重みとバイアスをより正確なものにします。

1つのバッチトレーニングの結果は、10個のニューロンに反映されます。ここで、10個のニューロンは0から9を表し、その値は0から1の範囲でその精度に対する自信を示します。

そして、入力は784個のニューロンです。どうすれば784個のニューロンを10個のニューロンに減らすことができるのでしょうか？ここにその方法があります。2つの層があると仮定しましょう。層とは何を意味するのでしょうか？つまり、最初の層には784個のニューロンがあります。2番目の層には10個のニューロンがあります。

784個のニューロンの各ニューロンに重みを与えます。例えば、

$$w_1, w_2, w_3, w_4, ... , w_{784}$$

そして最初の層に、バイアス、つまり $$b_1$$ を与えます。

そして、2番目の層の最初のニューロンの値は次のようになります。

$$w_1*a_1 + w_2*a_2+...+ w_{784}*a_{784}+b_1$$

しかし、これらの重みとバイアスは $$neuron^2_{1}$$（2番目の層の最初のニューロン）に対するものです。$$neuron^2_{2}$$ では、別の重みとバイアスのセットが必要です。

シグモイド関数はどうでしょう？上記の値を0から1にマッピングするためにシグモイド関数を使用します。

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

また、最初の層を活性化するためにシグモイド関数を使用します。つまり、グレースケール値を0から1の範囲に変更します。したがって、すべての層のすべてのニューロンは0から1の範囲の値を持つことになります。

したがって、私たちの2層ネットワークでは、最初の層に784個のニューロン、2番目の層に10個のニューロンがあります。重みとバイアスを得るためにそれを訓練します。

784 * 10個の重みと10個のバイアスがあります。2番目の層では、すべてのニューロンについて、その値を計算するために784個の重みと1個のバイアスを使用します。コードは次のようになります。

```python
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
```

### 順伝播

> 順伝播: 各 l=2,3,…,L に対して $$z^{l} = w^l a^{l-1}+b^l$$ と $$a^{l} = \sigma(z^{l})$$ を計算します。

ここで注意すべきは、最新の層の値、つまり $$a^{l-1}$$ と現在の層の重み $$w^l$$ とそのバイアス $$b^l$$ を使用して、シグモイド処理を行い、現在の層の値 $$a^{l}$$ を得るという点です。

コード:

```python
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x] 
        zs = [] 
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
```
### 出力誤差

> 出力誤差 $$\delta^{L}$$: ベクトル $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$ を計算します。

$$\nabla$$ の意味を見てみましょう。

> Del、またはnablaは、数学（特にベクトル解析）でベクトル微分演算子として使用される演算子で、通常はnabla記号 ∇ で表されます。

$$
\begin{eqnarray}
  w_k & \rightarrow & w_k' = w_k-\eta \frac{\partial C}{\partial w_k} \\
  b_l & \rightarrow & b_l' = b_l-\eta \frac{\partial C}{\partial b_l}
\end{eqnarray}
$$

ここで $$\eta $$ は学習率です。Cが重みとバイアスに対して微分される、つまりそれらの間の変化率を使用します。これが以下の`sigmoid_prime`です。

コード:

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

### 誤差の逆伝播

> 誤差の逆伝播: 各 l=L−1,L−2,…,2 に対して $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$ を計算します。

```python
     for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)
```

### 出力

> 出力: コスト関数の勾配は $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$
と $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$ で与えられます。

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

### 最後に

短い記事です。ほとんどの部分でコードと数式しか示されていません。しかし、私にとってはそれで十分です。書く前ははっきりとは理解していませんでした。コードや本からのスニペットを書き写したり、コピーしたりした後、そのほとんどを理解しました。Yin Wang先生から自信を得て、「Neural Networks and Deep Learning」という本の約30%を読み、Andrej Karpathyのスタンフォード大学の講義とAndrew Ngのコースを聞き、友人のQiと議論し、Anaconda、numpy、Theanoライブラリをいじって数年前のコードを動作させた後、今ではそれを理解しています。

重要な点の1つは次元です。すべての記号と変数の次元を知るべきです。そしてそれは単に微分可能な計算を行います。Yin Wangの引用で締めくくりましょう。

> 機械学習は本当に役に立ち、美しい理論とさえ言えるでしょう。なぜなら、それは化粧直しされた微積分に過ぎないからです！それは、よりシンプルでエレガントで強力な形になったニュートンとライプニッツの古く偉大な理論です。機械学習は基本的に微積分を使用して関数を導き出し、適合させることであり、深層学習はより複雑な関数を適合させることです。

> 人工知能には「知能」がなく、ニューラルネットワークには「ニューラル」がなく、機械学習には「学習」がなく、深層学習には「深さ」がありません。深層学習には「深さ」がありません。この分野で本当に機能しているのは「微積分」と呼ばれています。したがって、私はこの分野を「微分可能計算」と呼び、モデルを構築するプロセスを「微分可能プログラミング」と呼ぶことを好みます。