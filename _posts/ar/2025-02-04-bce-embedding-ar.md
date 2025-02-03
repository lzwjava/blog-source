---
audio: false
lang: ar
layout: post
title: 'BCEmbedding: تضمين ثنائي اللغة لـ RAG'
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

# قائمة من الجمل
sentences = ['sentence_0', 'sentence_1']

# تهيئة نموذج التضمين
model = EmbeddingModel(model_name_or_path="maidalun1020/bce-embedding-base_v1")

# استخراج التضمينات
embeddings = model.encode(sentences)
```
