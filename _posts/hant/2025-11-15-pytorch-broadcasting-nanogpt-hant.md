---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 理解NanoGPT中的PyTorch廣播機制
translated: true
type: note
---

很好的問題！這確實是初次閱讀 NanoGPT 或 GPT-2 程式碼時常見的困惑點。

讓我們仔細看看形狀：

```python
tok_emb = self.transformer.wte(idx)    # 形狀：(B, T, n_embd)
pos_emb = self.transformer.wpe(pos)    # 形狀：(T, n_embd)   ← 只有一維！
```

如何能將 `(B, T, n_embd)` + `(T, n_embd)` 相加？

**答案：PyTorch 會自動在批次維度上廣播位置嵌入。**

當 PyTorch 遇到：
```python
tok_emb + pos_emb
```
它會將 `pos_emb`（形狀 `(T, n_embd)`）視為 `(1, T, n_embd)`，然後將其**廣播**以匹配 `(B, T, n_embd)`。

因此這個加法運算變成：
```
(B, T, n_embd)
     + 
(1, T, n_embd)   ← 通過廣播自動添加
     =
(B, T, n_embd)
```

這正是原始 GPT-2 和所有現代 transformer 實現的工作原理——位置嵌入在批次中的所有序列之間是共享的。

您可以在 Python 中驗證此操作：

```python
import torch
B, T, C = 2, 3, 768
tok_emb = torch.randn(B, T, C)
pos_emb = torch.randn(T, C)

result = tok_emb + pos_emb
print(result.shape)  # → torch.Size([2, 3, 768])
```

沒有錯誤，完美運行。

所以在 NanoGPT（以及原始 GPT-2）中，這行程式碼是 100% 正確且有意為之的：

```python
x = self.transformer.drop(tok_emb + pos_emb)
```

它依賴於 PyTorch 的廣播機制——簡潔、高效且符合標準做法。

不需要使用 `pos_emb.unsqueeze(0)` 或其他任何操作。廣播機制優雅地完成了這項工作。