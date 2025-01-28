---
audio: true
lang: zh
layout: post
title: 深度探索 API 使用
translated: true
---

一个月内，1500万个令牌花费了我约23.5人民币。

这是我一天的使用情况：

| 类型              | 令牌数    |
|-------------------|-----------|
| 输入（缓存命中）  | 946,816   |
| 输入（缓存未命中） | 2,753,752 |
| 输出            | 3,100,977 |

计算方法如下：

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

因此，根据任务不同，令牌的使用量主要取决于输入（缓存未命中）和输出。

这个结果与预期成本一致。

[DeepSeek API 定价](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*来源：自拍屏幕*{: .caption }