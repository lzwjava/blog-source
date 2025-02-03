---
audio: false
lang: hi
layout: post
title: 'BCEmbedding: द्विभाषी एम्बेडिंग RAG के लिए'
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

# वाक्यों की सूची
sentences = ['sentence_0', 'sentence_1']

# एम्बेडिंग मॉडल आरंभ करें
model = EmbeddingModel(model_name_or_path="maidalun1020/bce-embedding-base_v1")

# एम्बेडिंग निकालें
embeddings = model.encode(sentences)
```
