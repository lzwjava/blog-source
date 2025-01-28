---
audio: true
lang: zh
layout: post
title: 深度探测API使用
translated: true
---

## DeepSeek

在一个月里，1500万个token大约花费我23.5元人民币。

我的一天的使用情况如下：

| 类型              |  Token数 |
|-------------------|-----------|
| 输入（缓存命中）  | 946,816   |
| 输入（缓存未命中）| 2,753,752 |
| 输出              | 3,100,977 |

计算方法如下：

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

因此，根据任务的不同，token的使用主要取决于输入（缓存未命中）和输出。

这个结果与预期的费用一致。

[DeepSeek API 定价](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*来源：自拍*{: .caption }

## Mistral

在一个天中，我的Mistral账户使用情况如下（模型：`mistral-large-2411`）：

| 类型   |  Token数  | 费用 (USD) |
|--------|-----------|--------------|
| 总计   | 772,284   | 3.44         |
| 输出   | 474,855   | 2.85         |
| 输入   | 297,429   | 0.59         |

Mistral模型的定价如下：

| 模型                 | 输入（每千万token的USD） | 输出（每千万token的USD） |
|----------------------|----------------------------|-------------------------|
| `mistral-large-2411` | 2                           | 6                       |
| `mistral-small-latest`| 0.2                        | 0.6                     |