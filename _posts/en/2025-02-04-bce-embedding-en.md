---
audio: false
lang: en
layout: post
title: 'BCEmbedding: Bilingual Embedding for RAG'
translated: false
---

[<https://github.com/netease-youdao/BCEmbedding](https://github.com/netease-youdao/BCEmbedding)

```bash
git clone git@github.com:netease-youdao/BCEmbedding.git
cd BCEmbedding
pip install -v -e .
```

```python
from BCEmbedding import EmbeddingModel

# list of sentences
sentences = ['sentence_0', 'sentence_1']

# init embedding model
model = EmbeddingModel(model_name_or_path="maidalun1020/bce-embedding-base_v1")

# extract embeddings
embeddings = model.encode(sentences)
```