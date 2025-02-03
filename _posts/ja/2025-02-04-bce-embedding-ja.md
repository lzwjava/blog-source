---
audio: false
lang: ja
layout: post
title: BCEmbedding：RAGのためのバイリンガル埋め込み
translated: true
---

[https://github.com/netease-youdao/BCEmbedding](https://github.com/netease-youdao/BCEmbedding)

```bash
git clone git@github.com:netease-youdao/BCEmbedding.git
cd BCEmbedding
pip install -v -e .
```

```python
from BCEmbedding import EmbeddingModel

# 文のリスト
sentences = ['sentence_0', 'sentence_1']

# embeddingモデルの初期化
model = EmbeddingModel(model_name_or_path="maidalun1020/bce-embedding-base_v1")

# embeddingの抽出
embeddings = model.encode(sentences)
```
