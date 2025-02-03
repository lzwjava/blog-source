---
audio: false
lang: es
layout: post
title: 'BCEmbedding: Incrustación Bilingüe para RAG'
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

# lista de oraciones
sentences = ['sentence_0', 'sentence_1']

# inicializar modelo de embedding
model = EmbeddingModel(model_name_or_path="maidalun1020/bce-embedding-base_v1")

# extraer embeddings
embeddings = model.encode(sentences)
```
