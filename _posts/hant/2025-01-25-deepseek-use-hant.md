---
audio: false
lang: hant
layout: post
title: Api 使用 Deepseek 與 Mistral
translated: true
---

## DeepSeek

一個月內，1500萬個token大約花了23.5 CNY。

這是我一天的使用量：

| 類型              | Tokens    |
|-------------------|-----------|
| 輸入 (Cache Hit)  | 946,816   |
| 輸入 (Cache Miss) | 2,753,752 |
| 輸出            | 3,100,977 |

計算如下：

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

因此，根據任務，token使用量主要取決於輸入（cache miss）和輸出。

這個結果與預期的成本一致。

[DeepSeek API 定價](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*來源：自拍*{: .caption }

## Mistral

Mistral模型的定價如下：

| 模型                 | 輸入 (每百萬token的USD) | 輸出 (每百萬token的USD) |
|-----------------------|------------------------------|---------------------------------|
| `mistral-large-2411`  | 2                            | 6                               |
| `mistral-small-latest`| 0.2                          | 0.6                             |

一天內，我的Mistral帳戶使用情況如下（模型：`mistral-large-2411`）：

| 類型   | Tokens  | 成本 (USD) |
|--------|---------|------------|
| 總計  | 772,284 | 3.44       |
| 輸出  | 474,855 | 2.85       |
| 輸入  | 297,429 | 0.59       |

對於`mistral-small-2409`模型，總使用量為1,022,407個token。

假設其中1/3是輸入token，2/3是輸出token：

有340,802個輸入token和681,605個輸出token。

因此，總成本計算如下：340,802 * 0.2 / 1,000,000 + 681,605 * 0.6 / 1,000,000 = 0.07 + 0.41 = 0.48 USD。

Mistral控制台報告的總使用成本為0.43 USD，大致與我們的計算相符。