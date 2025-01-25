---
audio: true
lang: ja
layout: post
title: DeepSeek APIの使い方
translated: true
---

1ヶ月で1500万トークン使用し、約23.5元かかりました。

以下は1日の使用量です：

| タイプ              | トークン数    |
|-------------------|-----------|
| 入力 (キャッシュヒット)  | 946,816   |
| 入力 (キャッシュミス) | 2,753,752 |
| 出力            | 3,100,977 |

計算は以下の通りです：

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

したがって、タスクによってトークンの使用量は主に入力（キャッシュミス）と出力に依存します。

この結果は予想されるコストと一致しています。

[DeepSeek API 料金](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg){: .responsive }
*出典: 自作スクリーンショット*{: .caption }