---
audio: true
lang: en
layout: post
title: Api Usage Of Deepseek And Mistral
---

## DeepSeek

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
![](assets/images/deepseek/d.jpg)
*Source: Self-Screenshot*{: .caption }

## Mistral


The pricing for Mistral models is as follows:

| Model                 | Input (USD per million tokens) |  Output (USD per million tokens) |
|-----------------------|------------------------------|---------------------------------|
| `mistral-large-2411`  | 2                            | 6                               |
| `mistral-small-latest`| 0.2                          | 0.6                             |

In one day, my Mistral account usage was as follows (Model: `mistral-large-2411`):

| Type   | Tokens  | Cost (USD) |
|--------|---------|------------|
| Total  | 772,284 | 3.44       |
| Output | 474,855 | 2.85       |
| Input  | 297,429 | 0.59       |


For model `mistral-small-2409`, 

Total usage: 1,022,407 tokens

Assuming 1/3 are input tokens and 2/3 are output tokens:

The number of input tokens is 340,802, and the number of output tokens is 681,605.

So the total cost is 340,802 * 0.2 / 1000000 + 681,605 * 0.6 / 1000000 = 0.07 + 0.41 = 0.48 USD.

