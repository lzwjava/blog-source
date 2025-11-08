---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: イリヤ・サツケヴェールのAI関連書籍リスト
translated: true
type: note
---

OpenAIの共同創業者であるIlya Sutskeverは、2020年頃にJohn Carmackと共有した、深層学習とAIに関する約30の主要な論文、ブログ記事、コース、リソースからなる推奨読書リストを公開しました。彼はこれらをマスターすれば、この分野で「今日重要なことの90%」をカバーできると述べたとされています。完全な30項目の元のリストは公開されていませんが（いくつかの項目はメール削除により失われた可能性があります）、広く流通しているバージョンには、畳み込みネットワーク、リカレントネットワーク、トランスフォーマー、情報理論などにまたがる27の基礎的な項目が含まれています。以下は、明確にするためにカテゴリ別にグループ化した精選されたリストです。各項目には、タイトル、著者、年、タイプが含まれています。

### 畳み込みニューラルネットワーク
1. **CS231n: Convolutional Neural Networks for Visual Recognition** - Fei-Fei Li, Andrej Karpathy, Justin Johnson - 2017 - スタンフォード大学コース
2. **ImageNet Classification with Deep Convolutional Neural Networks (AlexNet)** - Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton - 2012 - 論文
3. **Deep Residual Learning for Image Recognition (ResNet)** - Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun - 2015 - 論文
4. **Identity Mappings in Deep Residual Networks** - Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun - 2016 - 論文
5. **Multi-Scale Context Aggregation by Dilated Convolutions** - Fisher Yu, Vladlen Koltun - 2015 - 論文

### リカレントニューラルネットワーク
6. **Understanding LSTM Networks** - Christopher Olah - 2015 - ブログ記事
7. **The Unreasonable Effectiveness of Recurrent Neural Networks** - Andrej Karpathy - 2015 - ブログ記事
8. **Recurrent Neural Network Regularization** - Wojciech Zaremba, Ilya Sutskever, Oriol Vinyals - 2014 - 論文
9. **Neural Turing Machines** - Alex Graves, Greg Wayne, Ivo Danihelka - 2014 - 論文
10. **Deep Speech 2: End-to-End Speech Recognition in English and Mandarin** - Dario Amodei et al. - 2016 - 論文
11. **Neural Machine Translation by Jointly Learning to Align and Translate (RNNsearch)** - Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio - 2015 - 論文
12. **Pointer Networks** - Oriol Vinyals, Meire Fortunato, Navdeep Jaitly - 2015 - 論文
13. **Order Matters: Sequence to Sequence for Sets (Set2Set)** - Oriol Vinyals, Samy Bengio, Manjunath Kudlur - 2016 - 論文
14. **A Simple Neural Network Module for Relational Reasoning (Relation Networks)** - Adam Santoro, David Raposo, David G. Barrett, Mateusz Malinowski, Razvan Pascanu, Peter Battaglia, Timothy Lillicrap - 2017 - 論文
15. **Relational Recurrent Neural Networks** - Adam Santoro, Ryan Faulkner, David Raposo, Jack Rae, Mike Chrzanowski, Theophane Weber, Daan Wierstra, Oriol Vinyals, Razvan Pascanu, Timothy Lillicrap - 2018 - 論文

### トランスフォーマー
16. **Attention Is All You Need** - Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin - 2017 - 論文
17. **The Annotated Transformer** - Sasha Rush et al. - 2017 (annotated 2020) - ブログ記事
18. **Scaling Laws for Neural Language Models** - Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, Dario Amodei - 2020 - 論文

### 情報理論
19. **A Tutorial Introduction to the Minimum Description Length Principle** - Peter Grünwald - 2004 - 書籍章
20. **Kolmogorov Complexity and Algorithmic Randomness (Chapter 14)** - Alexander Shen, Vladimir A. Uspensky, Nikolay Vereshchagin - 2017 - 書籍章
21. **The First Law of Complexodynamics** - Scott Aaronson - 2011 - ブログ記事
22. **Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton** - Scott Aaronson, Sean M. Carroll, Lauren Ouellette - 2014 - 論文
23. **Machine Super Intelligence** - Shane Legg - 2008 - 学位論文

### その他
24. **Keeping Neural Networks Simple by Minimizing the Description Length of the Weights** - Geoffrey E. Hinton, Drew van Camp - 1993 - 論文
25. **Variational Lossy Autoencoder** - Xi Chen, Diederik P. Kingma, Tim Salimans, Yan Duan, Prafulla Dhariwal, John Schulman, Ilya Sutskever, Pieter Abbeel - 2017 - 論文
26. **GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism** - Yanping Huang, Youlong Cheng, Ankur Bapna, Orhan Firat, Mia Xu Chen, Dehao Chen, HyoukJoong Lee, Jiquan Ngiam, Quoc V. Le, Yonghui Wu, Zhifeng Chen - 2018 - 論文
27. **Neural Message Passing for Quantum Chemistry** - Justin Gilmer, Samuel S. Schoenholz, Patrick F. Riley, Oriol Vinyals, George E. Dahl - 2017 - 論文

「欠落している」3項目については、メタ学習に関する論文（例: *Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks* by Chelsea Finn et al., 2017）や、Sutskeverの当時の講演内容に基づく自己対戦に関する強化学習の研究が推測されることが多いですが、これらは確認されていません。

[Deep learning reading list from Ilya Sutskever](https://github.com/dzyim/ilya-sutskever-recommended-reading)
[Summary of Ilya Sutskever's AI Reading List](https://tensorlabbet.com/2024/09/24/ai-reading-list/)
[The Lost Reading Items of Ilya Sutskever's AI Reading List](https://tensorlabbet.com/2024/11/11/lost-reading-items/)