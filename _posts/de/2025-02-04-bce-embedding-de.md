---
audio: false
lang: de
layout: post
title: 'BCEmbedding: Bilinguale Einbettung für RAG'
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

# Liste von Sätzen
sentences = ['sentence_0', 'sentence_1']

# Embedding-Modell initialisieren
model = EmbeddingModel(model_name_or_path="maidalun1020/bce-embedding-base_v1")

# Embeddings extrahieren
embeddings = model.encode(sentences)
```
