---
audio: true
lang: en
layout: post
title: DeepSeek API Usage
---

In one month, 15 million tokens cost me approximately 23.5 CNY.

This was my usage in one day:

| Type              | Tokens    |
|-------------------|-----------|
| Input (Cache Hit)  | 946,816   |
| Input (Cache Miss) | 2,753,752 |
| Output            | 3,100,977 |

The calculation is as follows:

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

So, depending on the task, the token usage largely depends on the input (cache miss) and output.

This result aligns with the expected cost.

[DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg){: .responsive }
*Source: Self-Screenshot*{: .caption }
