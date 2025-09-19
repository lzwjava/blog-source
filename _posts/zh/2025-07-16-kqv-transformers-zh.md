---
audio: false
generated: false
image: false
lang: zh
layout: post
title: KQV、Transformer 与 GPT
translated: true
---

## 我是如何理解 Transformer 中的 KQV 机制的

*2025.07.16*

在阅读了 [Transformer 中的 K、Q、V 机制](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en) 后，我大致理解了 K（Key）、Q（Query）和 V（Value）的作用。

Q 代表查询（Query），K 代表键（Key），V 代表值（Value）。对于一个句子来说，Query 是一个矩阵，存储了某个 token 需要向其他 token 提问的信息。Key 代表 token 的描述，Value 则代表 token 的实际含义矩阵。

它们有特定的形状，因此需要知道它们的维度和细节。

我大约在 2025 年 6 月初理解了这一点。我最早在 2023 年底接触到这个概念。当时我看过一些文章，比如 [《The Illustrated Transformer》](https://jalammar.github.io/illustrated-transformer/)，但并没有理解多少。

大约两年后，我发现现在更容易理解了。在这两年里，我主要专注于后端开发和准备专科考试，没有花太多时间学习机器学习。不过，我偶尔会在开车或做其他事情时思考这些概念。

这让我想到时间的作用。我们第一次接触某些知识时，可能理解不深，但它会成为思考的起点。

随着时间的推移，我发现对于知识和发现来说，第一次接触时很难理解或思考透彻。但之后再回顾时，似乎更容易学习和掌握。

其中一个原因是，在 AI 时代，学习变得更容易，因为你可以深入探索任何细节或方面来解决疑问。同时也有更多相关的 AI 视频可供参考。更重要的是，你会发现有很多人正在基于这些知识学习和构建项目，比如 [llama.cpp](https://github.com/ggml-org/llama.cpp)。

Georgi Gerganov 的故事非常鼓舞人心。作为一名 2021 年左右才开始学习机器学习的新手，他在 AI 社区产生了巨大的影响。

这样的事情会一次又一次地发生。因此，对于强化学习和最新的 AI 知识，尽管我目前还无法投入太多时间，但我认为可以抽出一些时间快速学习，并多加思考。大脑会自行完成剩下的工作。

---

## 从神经网络到 GPT

*2023.09.28*

### YouTube 视频

Andrej Karpathy - 从零开始构建 GPT：代码逐步实现

Umar Jamil - 注意力是你所需要的（Transformer） - 模型解释（包括数学）、推理与训练

StatQuest with Josh Starmer - Transformer 神经网络，ChatGPT 的基础，清晰解释！！！

Pascal Poupart - CS480/680 课程 19：注意力与 Transformer 网络

The A.I. Hacker - Michael Phi - Transformer 神经网络插图指南：逐步解释

### 我的学习过程

在读完《神经网络与深度学习》一书的一半内容后，我开始复现手写数字识别的神经网络示例。我在 GitHub 上创建了一个仓库：[https://github.com/lzwjava/neural-networks-and-zhiwei-learning](https://github.com/lzwjava/neural-networks-and-zhiwei-learning)。

这才是真正的难点所在。如果能够完全从零开始编写代码而不抄袭任何内容，那么理解就会非常深入。

我的复现代码仍然缺少 `update_mini_batch` 和反向传播的实现。不过，通过仔细观察数据加载、前向传播和评估阶段的变量，我对向量、维度、矩阵和形状有了更深的理解。

之后，我开始学习 GPT 和 Transformer 的实现。通过词嵌入和位置编码，文本被转换为数字。本质上，这与识别手写数字的简单神经网络并无不同。

Andrej Karpathy 的讲座《从零开始构建 GPT》非常出色。他解释得非常好。

第一个原因是它确实是从零开始。我们首先看到如何生成文本，一开始是模糊且随机的。第二个原因是 Andrej 能够用非常直观的方式解释事物。他花了几个月时间做 nanoGPT 项目。

我突然有了一个判断讲座质量的新想法：作者是否真的能亲自编写这些代码？我为什么不理解？作者遗漏了哪些主题？除了那些精美的图表和动画，它们有什么缺点和不足？

回到机器学习本身。如 Andrej 所提到的，dropout、残差连接、自注意力、多头注意力、掩码注意力。

通过观看更多上述视频，我开始逐渐理解了一些内容。

通过正弦和余弦函数的位置编码，我们得到一些权重。通过词嵌入，我们将单词转换为数字。

$$
    PE_{(pos,2i)} = \sin(pos/10000^{2i/d_{model}}) \\
    PE_{(pos,2i+1)} = \cos(pos/10000^{2i/d_{model}})
$$

> The pizza came out of the oven and it tasted good.

在这个句子中，算法如何知道“it”指的是 pizza 还是 oven？如何计算句子中每个单词的相似度？

我们需要一组权重。如果使用 Transformer 网络进行翻译任务，每次输入一个句子，它能输出另一种语言的对应句子。

关于这里的点积。我们使用点积的一个原因是点积会考虑向量中的每一个数字。如果使用平方点积呢？我们先对数字进行平方，再进行点积。如果进行某种反向点积呢？

关于这里的掩码，我们将矩阵中一半的数字设为负无穷。然后使用 softmax 将值范围限制在 0 到 1 之间。如果我们将左下角的数字设为负无穷呢？

### 计划

继续阅读代码、论文和观看视频。保持兴趣，跟随好奇心。

[https://github.com/karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)

[https://github.com/jadore801120/attention-is-all-you-need-pytorch](https://github.com/jadore801120/attention-is-all-you-need-pytorch)