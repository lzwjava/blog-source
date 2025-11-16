---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ナノGPTにおけるPyTorchブロードキャストの理解
translated: true
type: note
---

素晴らしい質問です！これはNanoGPTやGPT-2のコードを初めて見る際によくある混乱ポイントです。

形状を注意深く見てみましょう：

```python
tok_emb = self.transformer.wte(idx)    # 形状: (B, T, n_embd)
pos_emb = self.transformer.wpe(pos)    # 形状: (T, n_embd)   ← 1次元のみ！
```

`(B, T, n_embd)` + `(T, n_embd)` はどのように加算できるのでしょうか？

**答え：PyTorchがバッチ次元にわたって位置埋め込みを自動的にブロードキャストするからです。**

PyTorchは以下のコードを見ると：
```python
tok_emb + pos_emb
```
`pos_emb`（形状 `(T, n_embd)`）を `(1, T, n_embd)` であるかのように扱い、それを `(B, T, n_embd)` に一致するように**ブロードキャスト**します。

つまりこの加算は以下のようになります：
```
(B, T, n_embd)
     + 
(1, T, n_embd)   ← ブロードキャストによって自動的に追加
     =
(B, T, n_embd)
```

これはまさにオリジナルのGPT-2およびすべての現代的なトランスフォーマー実装が動作する方法です — 位置埋め込みはバッチ内のすべてのシーケンスで共有されます。

Pythonでこれが動作することを確認できます：

```python
import torch
B, T, C = 2, 3, 768
tok_emb = torch.randn(B, T, C)
pos_emb = torch.randn(T, C)

result = tok_emb + pos_emb
print(result.shape)  # → torch.Size([2, 3, 768])
```

エラーはなく、完璧に動作します。

したがってNanoGPT（およびオリジナルのGPT-2）では、この行は100%正しく意図されたものです：

```python
x = self.transformer.drop(tok_emb + pos_emb)
```

これはPyTorchのブロードキャスト機能に依存しています — クリーンで効率的、かつ標準的なプラクティスです。

`pos_emb.unsqueeze(0)` などは必要ありません。ブロードキャストがエレガントに仕事を処理します。