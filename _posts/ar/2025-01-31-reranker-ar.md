---
audio: true
generated: false
lang: ar
layout: post
title: رتب
translated: true
---

[bge-reranker](https://huggingface.co/BAAI/bge-reranker-v2-m3)

```python
from FlagEmbedding import FlagReranker
reranker = FlagReranker('BAAI/bge-reranker-base', use_fp16=True) # تعيين use_fp16 إلى True يسرع من الحساب مع بعض التدهور في الأداء

score = reranker.compute_score(['query', 'passage'])
print(score) # -5.65234375

# يمكنك تحويل الدرجات إلى نطاق 0-1 عن طريق تعيين "normalize=True"، والذي ستطبق فيه دالة sigmoid على الدرجة.
score = reranker.compute_score(['query', 'passage'], normalize=True)
print(score) # 0.003497010252573502

scores = reranker.compute_score([['ما هو الباندا؟', 'مرحبا'], ['ما هو الباندا؟', 'الباندا العملاق (Ailuropoda melanoleuca)، وأحيانًا يُعرف باسم الدب الباندا أو ببساطة الباندا، هو نوع من الدب الذي هو موطنه في الصين.']])
print(scores) # [-8.1875, 5.26171875]

# يمكنك تحويل الدرجات إلى نطاق 0-1 عن طريق تعيين "normalize=True"، والذي ستطبق فيه دالة sigmoid على الدرجة.
scores = reranker.compute_score([['ما هو الباندا؟', 'مرحبا'], ['ما هو الباندا؟', 'الباندا العملاق (Ailuropoda melanoleuca)، وأحيانًا يُعرف باسم الدب الباندا أو ببساطة الباندا، هو نوع من الدب الذي هو موطنه في الصين.']], normalize=True)
print(scores) # [0.00027803096387751553, 0.9948403768236574]
```

خطأ

```bash
(mpsFileLoc): /AppleInternal/Library/BuildRoots/b11baf73-9ee0-11ef-b7b4-7aebe1f78c73/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShadersGraph/mpsgraph/MetalPerformanceShadersGraph/Core/Files/MPSGraphUtilities.mm:233:0: خطأ: يحتاج 'mps.add' إلى نفس نوع العنصر لجميع المعاملات والمخرجات
(mpsFileLoc): /AppleInternal/Library/BuildRoots/b11baf73-9ee0-11ef-b7b4-7aebe1f78c73/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShadersGraph/mpsgraph/MetalPerformanceShadersGraph/Core/Files/MPSGraphUtilities.mm:233:0: ملاحظة: انظر إلى العملية الحالية: %10 = "mps.add"(%8, %9) : (tensor<1x7x1xf16>, tensor<1xf32>) -> tensor<*xf32>
```

[FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding)