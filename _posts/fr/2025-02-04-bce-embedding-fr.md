---
audio: false
lang: fr
layout: post
title: 'BCEmbedding : Intégration bilingue pour RAG'
translated: true
---

[<https://github.com/netease-youdao/BCEmbedding](https://github.com/netease-youdao/BCEmbedding)

```bash
git clone git@github.com:netease-youdao/BCEmbedding.git
cd BCEmbedding
pip install -v -e .
```

```python
from BCEmbedding import EmbeddingModel

# liste de phrases
sentences = ['sentence_0', 'sentence_1']

# initialisation du modèle d'embedding
model = EmbeddingModel(model_name_or_path="maidalun1020/bce-embedding-base_v1")

# extraction des embeddings
embeddings = model.encode(sentences)
```
