---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 如何學習Transformer中的KQV機制
translated: true
---

讀完 [K, Q, V Mechanism in Transformers](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en) 後，我大概理解了 K、Q 和 V 的運作方式。

Q 代表 Query，K 代表 Key，V 代表 Value。對於一句話，Query 是一個矩陣，儲存著它需要向其他 tokens 查詢的 token 值。Key 代表 tokens 的描述，而 Value 代表 tokens 的實際意義矩陣。

它們有特定的形狀，所以需要了解它們的維度和細節。

我大概是在 2025 年初理解這個概念的。我第一次接觸它是在 2023 年底左右。當時我讀了像 [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) 這樣的文章，但當時並沒有理解多少。

經過兩年時間，我發現現在理解起來比較容易。這兩年我主要專注於後端工作和準備副學士學位考試，沒有讀或學習太多關於機器學習的東西。不過，我偶爾在開車或做其他事情時，還是會思考這些概念。

這讓我想到時間的作用。我們可能第一次學習某些東西時，即使不太理解，但它仍然會成為我們思考的起點。

隨著時間推移，我發現對於知識和發現，第一次思考或理解某些東西可能很困難。但後來，學習和理解起來似乎變得容易了。

其中一個原因是，在 AI 時代，學習變得更容易，因為你可以深入任何細節或方面來解決你的疑問。也有更多相關的 AI 影片可供參考。更重要的是，你會看到有這麼多人在學習並基於此開發項目，例如 [llama.cpp](https://github.com/ggml-org/llama.cpp)。

Georgi Gerganov 的故事很鼓舞人心。作為一個從 2021 年開始學習機器學習的新手，他對 AI 社區產生了巨大影響。

這種事情會一再發生。因此，對於強化學習和最新的 AI 知識，即使我目前還沒有太多時間投入，我認為我可以找到一些時間快速學習，並嘗試多思考。大腦會做它的工作。