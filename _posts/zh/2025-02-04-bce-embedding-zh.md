---
audio: false
lang: zh
layout: post
title: BCEmbedding：双语嵌入式检索增强生成
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

# 句子列表
sentences = ['sentence_0', 'sentence_1']

# 初始化嵌入模型
model = EmbeddingModel(model_name_or_path="maidalun1020/bce-embedding-base_v1")

# 提取嵌入向量
embeddings = model.encode(sentences)
```
