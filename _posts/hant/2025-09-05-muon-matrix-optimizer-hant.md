---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 緲子：結構感知矩陣優化器
translated: true
type: note
---

「Muon」在 Kimi 中指的是一種先進的最佳化器——具體而言，是訓練 Kimi K2 語言模型時使用的**結構感知、矩陣正交化最佳化器**。

---

### 什麼是 Muon 最佳化器？

1. **矩陣感知最佳化**
   與 AdamW 或 SGD 不同，Muon 將權重矩陣視為幾何實體，而非獨立的純量參數。它應用 **Newton–Schulz 迭代** 來正交化動量平均梯度，從而產生條件良好、平衡的更新，同時尊重矩陣的行與列結構 ([Medium][1], [kellerjordan.github.io][2])。

2. **透過 Newton–Schulz 進行正交化**
   Muon 不使用計算成本高昂的奇異值分解 (SVD)，而是採用快速的迭代方法 (Newton–Schulz) 來近似梯度的最近正交矩陣。這使得更新在**譜範數約束**下進行，保留了能量並將學習均勻分散到所有方向 ([Medium][1], [kellerjordan.github.io][2])。

3. **流程調整**
   標準的更新流程——**梯度 → 動量 → 參數更新**——被替換為：
   **梯度 → 動量 → Newton–Schulz 正交化 → 參數更新**。
   此修改提升了二維參數矩陣的訓練效率與穩定性 ([Medium][3], [kellerjordan.github.io][2])。

4. **實際應用中的高效能**
   儘管增加了少量計算開銷，Muon 帶來了顯著的加速效果：

   * 在 NanoGPT 速度競賽中創下紀錄，訓練時間縮短約 35% ([kellerjordan.github.io][2])。
   * 在大型語言模型訓練中，結合權重衰減與每參數 RMS 調整後，展現良好的擴展性 ([arXiv][4])。

5. **堅實的理論基礎**
   近期研究支持了 Muon 的收斂特性、權重衰減的益處以及最佳批次大小。研究證實了在實際應用場景中，Muon 具有更緊密的理論界限和效率 ([arXiv][5])。

---

### Muon 在 **Kimi K2** 中的角色

Kimi K2 是 Moonshot AI 的 **專家混合模型**，擁有 **1 兆總參數**（激活 320 億），專為代理能力最佳化。它在知識、推理和編程基準測試中表現卓越，部分歸功於使用 Muon（以及一個稱為 **MuonClip** 的變體）進行訓練 ([Hugging Face][6], [Poe][7])。

* **MuonClip 最佳化器** 指的是在超大規模應用 Muon 的同時，解決此類大型模型固有的穩定性挑戰 ([Hugging Face][6], [Poe][7])。
* 該最佳化器是實現大型詞元資料集（約 15.5 兆詞元）**零訓練不穩定性**並達成最先進成果的關鍵 ([Hugging Face][6])。

---

### 總結（依要求不使用表格）

* **Muon** = 「MomentUm Orthogonalized by Newton–Schulz」——一種以正交化更新取代原始梯度更新的最佳化器，改善了矩陣參數的學習動態。
* 它保留了結構，確保了平衡的更新，並透過迭代正交化而非成本高昂的分解來保持效率。
* **Kimi K2** 利用 Muon（及 MuonClip）突破了大規模 MoE 訓練的極限，以穩定性和計算效率實現了頂尖性能。

---

如果您想深入了解，請告訴我——例如 Muon 與 AdamW 在訓練軌跡上的比較、MuonClip 如何為 MoE 調整演算法，或是 Newton–Schulz 方法在程式碼中的運作方式！

[1]: https://medium.com/%40gauritr01/the-truth-about-kimi-k2-pretraining-muon-optimizer-moe-unpacked-43554527d94a?utm_source=chatgpt.com "The Truth About KIMI K2 Pretraining: Muon Optimizer ..."
[2]: https://kellerjordan.github.io/posts/muon/?utm_source=chatgpt.com "Muon: An optimizer for hidden layers in neural networks"
[3]: https://medium.com/%40jenwei0312/going-beyond-adamw-a-practical-guide-to-the-muon-optimizer-93d90e91dbd3?utm_source=chatgpt.com "Going Beyond AdamW: A Practical Guide to the Muon ..."
[4]: https://arxiv.org/html/2502.16982v1?utm_source=chatgpt.com "Muon is Scalable for LLM Training"
[5]: https://arxiv.org/abs/2507.01598?utm_source=chatgpt.com "Convergence Bound and Critical Batch Size of Muon Optimizer"
[6]: https://huggingface.co/moonshotai/Kimi-K2-Base?utm_source=chatgpt.com "moonshotai/Kimi-K2-Base"
[7]: https://poe.com/Kimi-K2?utm_source=chatgpt.com "Kimi-K2"