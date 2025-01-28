---
audio: true
lang: hant
layout: post
title: DeepSeek API 使用
translated: true
---

## DeepSeek

在一個月內，1500萬個 token 花我大約 23.5 CNY。

這是我一天的使用情況：

| 類型                | Tokens    |
|---------------------|-----------|
| 輸入（緩存命中）    | 946,816   |
| 輸入（緩存未命中）  | 2,753,752 |
| 輸出                | 3,100,977 |

計算如下：

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

因此，取決於任務，token 的使用大多數依賴於輸入（緩存未命中）和輸出。

這結果與預期的成本相符。

[DeepSeek API 定價](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*來源：自拍*{: .caption }

## Mistral

我一天的 Mistral 帳戶使用情況如下（模型：`mistral-large-2411`）：

| 類型   | Tokens  | 成本 (USD) |
|--------|---------|------------|
| 總計   | 772,284 | 3.44       |
| 輸出   | 474,855 | 2.85       |
| 輸入   | 297,429 | 0.59       |

Mistral 模型的定價如下：

| 模型                | 輸入 (USD 每百萬 token) | 輸出 (USD 每百萬 token) |
|---------------------|--------------------------|-------------------------|
| `mistral-large-2411`| 2                          | 6                       |
| `mistral-small-latest`| 0.2 | 0.6                       |