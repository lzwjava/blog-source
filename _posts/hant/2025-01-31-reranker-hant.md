---
audio: true
generated: false
image: false
lang: hant
layout: post
title: 重排器
translated: true
---

[bge-reranker](https://huggingface.co/BAAI/bge-reranker-v2-m3)

```python
from FlagEmbedding import FlagReranker
reranker = FlagReranker('BAAI/bge-reranker-base', use_fp16=True) # 將 use_fp16 設置為 True 可以加快計算速度，但會稍微降低性能

score = reranker.compute_score(['query', 'passage'])
print(score) # -5.65234375

# 可以通過設置 "normalize=True" 將分數映射到 0-1 范圍內，這將對分數應用一個 sigmoid 函數。
score = reranker.compute_score(['query', 'passage'], normalize=True)
print(score) # 0.003497010252573502

scores = reranker.compute_score([['what is panda?', 'hi'], ['what is panda?', 'The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.']])
print(scores) # [-8.1875, 5.26171875]

# 可以通過設置 "normalize=True" 將分數映射到 0-1 范圍內，這將對分數應用一個 sigmoid 函數。
scores = reranker.compute_score([['what is panda?', 'hi'], ['what is panda?', 'The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.']], normalize=True)
print(scores) # [0.00027803096387751553, 0.9948403768236574]
```

錯誤

```bash
(mpsFileLoc): /AppleInternal/Library/BuildRoots/b11baf73-9ee0-11ef-b7b4-7aebe1f78c73/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShadersGraph/mpsgraph/MetalPerformanceShadersGraph/Core/Files/MPSGraphUtilities.mm:233:0: error: 'mps.add' op requires the same element type for all operands and results
(mpsFileLoc): /AppleInternal/Library/BuildRoots/b11baf73-9ee0-11ef-b7b4-7aebe1f78c73/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShadersGraph/mpsgraph/MetalPerformanceShadersGraph/Core/Files/MPSGraphUtilities.mm:233:0: note: see current operation: %10 = "mps.add"(%8, %9) : (tensor<1x7x1xf16>, tensor<1xf32>) -> tensor<*xf32>
```

[FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding)