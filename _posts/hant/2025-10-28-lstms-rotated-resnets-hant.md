---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 長短期記憶網絡只是旋轉的殘差網絡
translated: true
type: note
---

在他榮獲NeurIPS 2024時間考驗獎的演講中，Ilya Sutskever 回顧了2014年論文《使用神經網絡進行序列到序列學習》的關鍵洞見與失誤。他在「我們搞錯的部分」中特別指出，曾推動機器翻譯等早期序列建模突破的LSTM（長短期記憶網絡）存在過度複雜化與根本局限性。

### 關於LSTM的核心誤解
我們當時將LSTM視為專為序列數據設計的全新複雜架構——某種需要深度學習研究者精心設計以處理時間依賴性、梯度消失和循環特性的「特殊」產物。但Sutskever解釋道，實際情況遠比這簡單：**LSTM本質上是旋轉了90度的ResNet（殘差網絡）**。

- **ResNet**（2015年提出）透過跳躍連接（殘差）讓信息直接跨層流動，從而使更深的網絡能穩定訓練，徹底革新了圖像處理領域
- LSTM（1997年提出）則在*時間維度*實現了類似功能：其門控機制與細胞狀態如同殘差連接，讓梯度與信息能在長序列中傳播而不衰減。這與ResNet原理相同——只是從空間維度（如圖像像素）「旋轉」至時間維度（如句子中的詞語）

Sutskever打趣道：「對不熟悉的人來說，LSTM是深度學習研究者在Transformer出現前無奈使用的方案。它基本上就是旋轉了90度的ResNet...而且誕生更早，可說是帶有積分器與乘法運算的略微複雜版ResNet。」這個比喻強調LSTM並非革命性創舉，而是殘差思想在循環網絡中的早期優雅實踐。

### 此事為何重要（以及問題出在哪裡）
- **卓有成效的部分**：LSTM在當時展現出驚人的擴展能力，使seq2seq模型在翻譯任務上擊敗傳統統計方法。其殘差設計讓深度循環網絡得以訓練，正如後來在前饋網絡中的效果
- **我們失誤之處（及LSTM衰落原因）**：我們低估了LSTM的序列處理特性會成為擴展瓶頸。與可並行化的ResNet或Transformer不同，LSTM需逐步處理數據，導致其難以應對海量數據集或長上下文。此外，其過度複雜的設計（如多重門控機制）後被Transformer的注意力機制簡化取代。到2017年，Transformer的出現暴露了這些局限，使研究重心轉向具備更優並行能力與長距離依賴處理能力的自注意力機制

回顧來看，「錯誤」並非發明LSTM——它們曾是劃時代的過渡方案——而在於我們將其視為序列建模的終極解答，未能及時意識到殘差連接的通用價值，延遲了向並行化架構的演進。

這種視角將LSTM重新定義為理解跳躍連接如何突破多維度深度限制的奠基性里程碑，而非過時技術。

[《使用神經網絡進行序列到序列學習：十年回顧——演講稿與視頻》](https://kingy.ai/news/sequence-to-sequence-learning-with-neural-networks-what-a-decade-transcript-video/)  
[Ilya Sutskever NeurIPS 2024 完整演講](https://www.youtube.com/watch?v=1yvBqasHLZs)  
[Ilya NeurIPS 2024 演講深度解析](https://dlyog.com/papers/one_internet_v1)