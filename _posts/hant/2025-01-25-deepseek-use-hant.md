---
audio: true
lang: hant
layout: post
title: DeepSeek API 使用指南
translated: true
---

一個月內，1500萬個token花費了我約23.5元人民幣。

這是我一天的使用情況：

| 類型              | 令牌數    |
|-------------------|-----------|
| 輸入（緩存命中）  | 946,816   |
| 輸入（緩存未命中） | 2,753,752 |
| 輸出              | 3,100,977 |

計算如下：

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

因此，根據任務的不同，令牌的使用量主要取決於輸入（緩存未命中）和輸出。

這一結果與預期成本相符。

[深度搜索API定價](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg){: .responsive }
*來源：自截圖*{: .caption }