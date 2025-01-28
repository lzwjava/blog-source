---
audio: true
lang: ja
layout: post
title: 「DeepseekとMistralのAPI使用」
translated: true
---

## DeepSeek

一ヶ月で1500万トークンは約23.5 CNYでした。

1日の使用状況は以下の通りです：

| Type              | トークン数   |
|-------------------|--------------|
| Input (Cache Hit)  | 946,816      |
| Input (Cache Miss) | 2,753,752    |
| Output            | 3,100,977    |

計算方法は以下の通りです：

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

タスクにより、トークンの使用量は主にInput (Cache Miss)とOutputに依存します。

この結果は予想されるコストに一致します。

[DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*Source: Self-Screenshot*{: .caption }

## Mistral

Mistralアカウントの1日の使用状況は以下の通りです（モデル: `mistral-large-2411`）：

| Type   | トークン数  | コスト (USD) |
|--------|--------------|--------------|
| Total  | 772,284      | 3.44         |
| Output | 474,855      | 2.85         |
| Input  | 297,429      | 0.59         |

Mistralモデルの価格は以下の通りです：

| Model                 | Input (USD per million tokens) |  Output (USD per million tokens) |
|-----------------------|------------------------------|---------------------------------|
| `mistral-large-2411`  | 2                            | 6                               |
| `mistral-small-latest`| 0.2                          | 0.6                             |