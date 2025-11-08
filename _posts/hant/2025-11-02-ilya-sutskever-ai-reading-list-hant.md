---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Ilya Sutskever 嘅人工智能閱讀清單
translated: true
type: note
---

OpenAI 共同創辦人 Ilya Sutskever 曾於 2020 年左右向 John Carmack 分享了一份包含約 30 篇關鍵論文、網誌文章、課程與資源的深度學習與 AI 推薦閱讀清單。據稱他當時表示，掌握這些內容將涵蓋該領域「當今 90% 的重要知識」。雖然完整的 30 項原始清單並未完全公開（部分項目可能因郵件刪除而遺失），但廣為流傳的版本收錄了 27 項基礎內容，涵蓋卷積網絡、循環網絡、變換器、信息論等領域。以下是經分類整理的清單，每項條目均包含標題、作者、年份與類型。

### 卷積神經網絡
1. **CS231n：用於視覺識別的卷積神經網絡** - Fei-Fei Li、Andrej Karpathy、Justin Johnson - 2017 - 斯坦福課程  
2. **使用深度卷積神經網絡進行 ImageNet 分類（AlexNet）** - Alex Krizhevsky、Ilya Sutskever、Geoffrey E. Hinton - 2012 - 論文  
3. **圖像識別中的深度殘差學習（ResNet）** - Kaiming He、Xiangyu Zhang、Shaoqing Ren、Jian Sun - 2015 - 論文  
4. **深度殘差網絡中的恆等映射** - Kaiming He、Xiangyu Zhang、Shaoqing Ren、Jian Sun - 2016 - 論文  
5. **透過擴張卷積實現多尺度上下文聚合** - Fisher Yu、Vladlen Koltun - 2015 - 論文  

### 循環神經網絡
6. **理解 LSTM 網絡** - Christopher Olah - 2015 - 網誌文章  
7. **循環神經網絡的驚人有效性** - Andrej Karpathy - 2015 - 網誌文章  
8. **循環神經網絡正則化** - Wojciech Zaremba、Ilya Sutskever、Oriol Vinyals - 2014 - 論文  
9. **神經圖靈機** - Alex Graves、Greg Wayne、Ivo Danihelka - 2014 - 論文  
10. **Deep Speech 2：端到端英語與普通話語音識別** - Dario Amodei 等 - 2016 - 論文  
11. **透過聯合學習對齊與翻譯實現神經機器翻譯（RNNsearch）** - Dzmitry Bahdanau、Kyunghyun Cho、Yoshua Bengio - 2015 - 論文  
12. **指針網絡** - Oriol Vinyals、Meire Fortunato、Navdeep Jaitly - 2015 - 論文  
13. **順序至關重要：針對集合的序列到序列模型（Set2Set）** - Oriol Vinyals、Samy Bengio、Manjunath Kudlur - 2016 - 論文  
14. **用於關係推理的簡單神經網絡模組（關係網絡）** - Adam Santoro、David Raposo、David G. Barrett、Mateusz Malinowski、Razvan Pascanu、Peter Battaglia、Timothy Lillicrap - 2017 - 論文  
15. **關係循環神經網絡** - Adam Santoro、Ryan Faulkner、David Raposo、Jack Rae、Mike Chrzanowski、Theophane Weber、Daan Wierstra、Oriol Vinyals、Razvan Pascanu、Timothy Lillicrap - 2018 - 論文  

### 變換器
16. **注意力就是一切** - Ashish Vaswani、Noam Shazeer、Niki Parmar、Jakob Uszkoreit、Llion Jones、Aidan N. Gomez、Łukasz Kaiser、Illia Polosukhin - 2017 - 論文  
17. **註解版變換器** - Sasha Rush 等 - 2017（註解版 2020） - 網誌文章  
18. **神經語言模型的縮放定律** - Jared Kaplan、Sam McCandlish、Tom Henighan、Tom B. Brown、Benjamin Chess、Rewon Child、Scott Gray、Alec Radford、Jeffrey Wu、Dario Amodei - 2020 - 論文  

### 信息論
19. **最小描述長度原理入門教程** - Peter Grünwald - 2004 - 書籍章節  
20. **柯氏複雜度與算法隨機性（第 14 章）** - Alexander Shen、Vladimir A. Uspensky、Nikolay Vereshchagin - 2017 - 書籍章節  
21. **複雜動力學第一定律** - Scott Aaronson - 2011 - 網誌文章  
22. **量化封閉系統中複雜度的興衰：咖啡自動機模型** - Scott Aaronson、Sean M. Carroll、Lauren Ouellette - 2014 - 論文  
23. **機器超智能** - Shane Legg - 2008 - 博士論文  

### 其他
24. **透過最小化權重描述長度保持神經網絡簡單性** - Geoffrey E. Hinton、Drew van Camp - 1993 - 論文  
25. **變分有損自編碼器** - Xi Chen、Diederik P. Kingma、Tim Salimans、Yan Duan、Prafulla Dhariwal、John Schulman、Ilya Sutskever、Pieter Abbeel - 2017 - 論文  
26. **GPipe：透過微批次流水線並行實現輕鬆擴展** - Yanping Huang、Youlong Cheng、Ankur Bapna、Orhan Firat、Mia Xu Chen、Dehao Chen、HyoukJoong Lee、Jiquan Ngiam、Quoc V. Le、Yonghui Wu、Zhifeng Chen - 2018 - 論文  
27. **用於量子化學的神經消息傳遞** - Justin Gilmer、Samuel S. Schoenholz、Patrick F. Riley、Oriol Vinyals、George E. Dahl - 2017 - 論文  

關於「遺失」的 3 項內容，外界普遍推測可能涉及元學習論文（例如 Chelsea Finn 等於 2017 年發表的《深度網絡快速適應的模型無關元學習》），或基於 Sutskever 同期演講中提及的自對弈強化學習研究，但這些均未獲證實。

[Ilya Sutskever 的深度學習閱讀清單](https://github.com/dzyim/ilya-sutskever-recommended-reading)  
[Ilya Sutskever 的 AI 閱讀清單摘要](https://tensorlabbet.com/2024/09/24/ai-reading-list/)  
[Ilya Sutskever 的 AI 閱讀清單遺失項目](https://tensorlabbet.com/2024/11/11/lost-reading-items/)