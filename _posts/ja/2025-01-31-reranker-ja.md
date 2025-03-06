---
audio: true
generated: false
lang: ja
layout: post
title: 順位付け
translated: true
---

[bge-reranker](https://huggingface.co/BAAI/bge-reranker-v2-m3)

```python
from FlagEmbedding import FlagReranker
reranker = FlagReranker('BAAI/bge-reranker-base', use_fp16=True) # 設定 use_fp16 を True にすると、計算速度が速くなるが、若干の性能低下が発生します

score = reranker.compute_score(['query', 'passage'])
print(score) # -5.65234375

# スコアを 0-1 の範囲にマッピングするには、"normalize=True"を設定して、シグモイド関数をスコアに適用します。
score = reranker.compute_score(['query', 'passage'], normalize=True)
print(score) # 0.003497010252573502

scores = reranker.compute_score([['what is panda?', 'hi'], ['what is panda?', 'The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.']])
print(scores) # [-8.1875, 5.26171875]

# スコアを 0-1 の範囲にマッピングするには、"normalize=True"を設定して、シグモイド関数をスコアに適用します。
scores = reranker.compute_score([['what is panda?', 'hi'], ['what is panda?', 'The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.']], normalize=True)
print(scores) # [0.00027803096387751553, 0.9948403768236574]
```

エラー

```bash
(mpsFileLoc): /AppleInternal/Library/BuildRoots/b11baf73-9ee0-11ef-b7b4-7aebe1f78c73/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShadersGraph/mpsgraph/MetalPerformanceShadersGraph/Core/Files/MPSGraphUtilities.mm:233:0: エラー: 'mps.add'オペランドおよび結果に同じ要素タイプが必要です
(mpsFileLoc): /AppleInternal/Library/BuildRoots/b11baf73-9ee0-11ef-b7b4-7aebe1f78c73/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShadersGraph/mpsgraph/MetalPerformanceShadersGraph/Core/Files/MPSGraphUtilities.mm:233:0: 注意: 現在の操作を見てください: %10 = "mps.add"(%8, %9) : (tensor<1x7x1xf16>, tensor<1xf32>) -> tensor<*xf32>
```

[FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding)