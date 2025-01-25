---
audio: true
lang: zh
layout: post
title: DeepSeek API 使用指南
translated: true
---

一个月内，1500万tokens大约花费了我23.5元人民币。

这是我一天的使用情况：

| 类型              | Tokens    |
|-------------------|-----------|
| 输入（缓存命中）  | 946,816   |
| 输入（缓存未命中） | 2,753,752 |
| 输出            | 3,100,977 |

计算如下：

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

因此，根据任务的不同，token的使用量主要取决于输入（缓存未命中）和输出。

这一结果与预期成本相符。

[DeepSeek API 定价](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg){: .responsive }
*来源：自截图*{: .caption }