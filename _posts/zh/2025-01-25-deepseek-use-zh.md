---
audio: true
lang: zh
layout: post
title: DeepSeek API 使用
translated: true
---

## DeepSeek

在一个月内，1500万个token大约花费了23.5元人民币。

我在一天的使用情况如下：

| 类型              | 消耗的Token |
|-------------------|-------------|
| 输入（缓存命中）  | 946,816     |
| 输入（缓存未命中）| 2,753,752   |
| 输出              | 3,100,977   |

计算如下：

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

因此，根据任务的不同，Token的消耗主要依赖于输入（缓存未命中）和输出。

这个结果与预期的费用一致。

[DeepSeek API 定价](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*来源：自拍*{: .caption }

## Mistral

模型: `mistral-large-2411`

在一天内，我的Mistral账户消耗了以下的Token：

| 类型  | 消耗的Token | 费用（USD） |
|-------|--------------|--------------|
| 总计  | 772,284      | 3.44         |
| 输出  | 474,855      | 2.85         |
| 输入  | 297,429      | 0.59         |

Mistral大模型的定价如下：

* 输入：每百万Token 2美元
* 输出：每百万Token 6美元