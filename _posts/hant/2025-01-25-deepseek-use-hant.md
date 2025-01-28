---
audio: true
lang: hant
layout: post
title: DeepSeek API 使用
translated: true
---

## DeepSeek

一個月內，1500萬個token花費我大約23.5 CNY。

這是我一天的使用情況：

| 類型            | 令牌數量  |
|-----------------|-----------|
| 輸入（命中快取）| 946,816    |
| 輸入（未命中快取）| 2,753,752 |
| 輸出              | 3,100,977 |

計算方式如下：

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

因此，依據任務的不同，令牌使用量主要取決於輸入（未命中快取）和輸出。

這個結果與預期的成本相符。

[DeepSeek API 定價](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*來源：自行截圖*{: .caption }

## Mistral

模型：`mistral-large-2411`

一天內，我的Mistral賬戶消耗了以下令牌：

| 類型   | 令牌數量  | 成本 (USD) |
|--------|-----------|------------|
| 總計   | 772,284   | 3.44       |
| 輸出   | 474,855   | 2.85       |
| 輸入   | 297,429   | 0.59       |

Mistral大型模型的定價如下：

* 輸入：每百萬令牌2 USD
* 輸出：每百萬令牌6 USD