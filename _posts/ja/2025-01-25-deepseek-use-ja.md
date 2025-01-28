---
audio: true
lang: ja
layout: post
title: DeepSeek API使用
translated: true
---

## DeepSeek

一ヶ月で1500万トークンは約23.5 CNYになります。

一日の使用状況は以下の通りです：

| タイプ              | トークン    |
|-------------------|-----------|
| 入力（キャッシュヒット）  | 946,816   |
| 入力（キャッシュミス） | 2,753,752 |
| 出力            | 3,100,977 |

計算は以下の通りです：

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

したがって、タスクによっては、トークンの使用量は主に入力（キャッシュミス）と出力に依存します。

この結果は予想されるコストに一致します。

[DeepSeek API 価格](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*元絵：自スクリーンショット*{: .caption }

## Mistral

一日のMistralアカウントの使用状況は以下の通りです（モデル：`mistral-large-2411`）：

| タイプ   | トークン  | コスト（USD） |
|--------|---------|------------|
| 合計  | 772,284 | 3.44       |
| 出力 | 474,855 | 2.85       |
| 入力  | 297,429 | 0.59       |

Mistralモデルの価格は以下の通りです：

| モデル                 | 入力（USD per million tokens） | 出力（USD per million tokens） |
|-----------------------|------------------------------|---------------------------------|
| `mistral-large-2411`  | 2                            | 6                               |
| `mistral-small-latest`| 0.2                          | 0.6                             |