---
audio: true
lang: ja
layout: post
title: ディープシーク API 使用法
translated: true
---

1ヶ月で、1500万トークンが私に約23.5 CNYかかりました。

これが1日の使用量です：

| 種類              | トークン数    |
|-------------------|---------------|
| 入力（キャッシュヒット）  | 946,816   |
| 入力（キャッシュミス） | 2,753,752 |
| 出力            | 3,100,977 |

計算は以下の通りです：

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

したがって、タスクによっては、トークンの使用量は入力（キャッシュミス）と出力に大きく依存します。

この結果は予想されるコストに一致します。

[DeepSeek API 料金](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*出典: 自分で撮影*{: .caption }