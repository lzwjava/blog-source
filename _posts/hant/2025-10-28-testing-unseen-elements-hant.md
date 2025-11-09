---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 以未見元素測試泛化能力
translated: true
type: note
---

在Ilya Sutskever獲得NeurIPS 2024 Test of Time Award的演講中，他回顧了2014年發表論文《Sequence to Sequence Learning with Neural Networks》（以及相關早期工作如他的RNN語言建模博士論文）時，談及早期構建泛化神經語言模型的努力。關鍵挑戰在於確保模型不僅能記憶訓練數據，還能處理新穎輸入——也就是避免過度擬合。

他所提及檢測這種情況的具體「樸素方法」，涉及在**未見過的單詞或n-gram（多詞序列）上測試模型，這些內容未出現在訓練語料庫（常稱為「數據庫」）中**。

### 為何採用這種方法？
- **早期語言模型中的過度擬合風險**：簡單基線模型如n-gram模型（例如bigram或trigram）經常透過僅在確切序列多次出現於訓練時才進行流暢預測來「過度擬合」。它們對任何新穎內容賦予近乎零的概率，無法實現泛化。
- **樸素檢測測試**：為檢查真實泛化（非過度擬合），在經過設計的保留驗證/測試集上進行訓練，該集合包含刻意設計的「未見過」元素：
  - 將常見短語替換為虛構但合理的短語（例如在他的論文中，測試對虛假引用如「(ABC et al., 2003)」的句子補全——由於其不自然的大寫和作者名，模型從未遇到過該字符串）。
  - 衡量模型是否賦予合理概率、生成連貫補全，或在面對新穎內容時保持低困惑度/BLEU分數。
- 若模型在這些未見過項目上失敗（例如高困惑度或不連貫輸出），但在已見訓練數據上表現優異，則為過度擬合（記憶特定內容而非學習模式）。若成功，則表示透過學習表徵（例如捕捉語法/語義的LSTM狀態）實現泛化。

### 其工作中的範例
- **在seq2seq論文（2014年）中**：他們使用固定詞彙表（8萬個法語單詞，16萬個英語單詞），將詞彙表外（OOV）單詞替換為「UNK」。為檢測泛化問題，他們對OOV出現情況懲罰BLEU分數，並繪製性能與「平均詞頻排名」（越罕見越類似未見過）的關係圖。LSTM在處理罕見/未見過單詞時表現良好且無退化，與基線模型不同。
- **在其博士論文（2013年，關於RNN語言建模）中**：針對結構化句子補全，他們在全新字符串上測試，如「(ABC et al., 2003)」（因罕見性在訓練中未出現）。乘法RNN（MRNN）泛化能力強健（例如正確預測年份/上下文），而n-gram基線模型除非存在完全匹配否則無法處理——凸顯其過度擬合問題。

這種「檢查未見過單詞/n-gram」測試是一種直觀的早期啟發方法，早於如dropout或驗證曲線等先進技術。Sutskever在演講中指出，這類見解推動了現代LLM的規模化發展，其中對海量未見過數據的泛化仍是核心。

[Sequence to Sequence Learning with Neural Networks (arXiv PDF)](https://arxiv.org/pdf/1409.3215.pdf)  
[Ilya Sutskever博士論文 (PDF)](https://www.cs.utoronto.ca/~ilya/pubs/ilya_sutskever_phd_thesis.pdf)  
[Ilya Sutskever NeurIPS 2024演講視頻](https://www.youtube.com/watch?v=YD-9NG1Ke5Y)