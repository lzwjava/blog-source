---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: ResNet 革新深度學習
translated: true
type: note
---

ResNet（殘差網路）是深度學習史上最重要的突破之一。它由微軟研究院的何愷明等人於2015年提出，並以驚人的 3.57% top-5 錯誤率（超越當時人類水平）贏得當年 ImageNet 競賽。

ResNet 之所以成為重大突破的原因如下：

1. **解決了「退化問題」（極深網路中的梯度消失/爆炸）**  
   在 ResNet 之前，人們認為「如果 20 層效果良好，56 層應該更好」。但實際上，堆疊更多層反而使準確度下降——這並非因為過度擬合，而是因為優化本身變得更加困難。ResNet 證明了可以訓練 100+ 層的網路（他們展示了 152 層，後續更發展至 1000+ 層），同時獲得更好的效能。

2. **殘差區塊 + 跳躍連接（核心概念）**  
   ResNet 不要求層直接學習 H(x)，而是學習殘差 F(x) = H(x) − x，因此區塊計算結果為 x + F(x)。  
   數學表達式：  
   y = F(x, {W_i}) + x  
   這種「恆等捷徑」讓梯度能透過跳躍連接直接流經網路，使極深度訓練成為可能。

3. **立即且巨大的實際影響**  
   - 成為 2016 年至 2020 年間幾乎所有頂尖視覺模型的主幹（至今仍廣泛使用）。  
   - 應用於物件檢測（Faster R-CNN + ResNet）、分割（DeepLab、Mask R-CNN）、生成模型（StyleGAN 等）、影片分析、醫學影像等領域。  
   - ResNet-50、ResNet-101、ResNeXt、Wide ResNet 及 ResNet-RS 等變體至今仍是 2025 年的標準基準模型。

4. **開啟「深度學習真正深化」的時代**  
   ResNet 之前：最佳 ImageNet 模型約為 20–30 層（VGG、GoogLeNet）。  
   ResNet 之後：100–1000+ 層成為常態。這種深度對於學習更豐富的特徵至關重要。

5. **極簡概念卻具有變革性**  
   該論文以簡潔著稱，僅透過一個巧妙技巧（跳躍連接 + 元素加法）實現突破。無需新穎的激活函數或損失函數——純粹是架構設計的洞見。

總而言之：ResNet 證明了只要架構設計得當，「更深層確實更好」的理念確實可行，並成為往後十年幾乎所有電腦視覺模型的預設起點。

即使在 Transformer 與 ConvNeXt/ViT 模型主導排行榜的 2025 年，ResNet-50 因其速度快、易理解且極度可靠，仍是最常用的基準主幹模型。

論文（仍值得一讀）：  
[Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)