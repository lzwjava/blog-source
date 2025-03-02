---
audio: true
generated: true
lang: es
layout: post
title: Reranker
translated: true
---

[bge-reranker](https://huggingface.co/BAAI/bge-reranker-v2-m3)

```python
from FlagEmbedding import FlagReranker
reranker = FlagReranker('BAAI/bge-reranker-base', use_fp16=True) # Configurar use_fp16 en True acelera el cálculo con una ligera degradación del rendimiento

puntuación = reranker.compute_score(['consulta', 'pasa'])
print(puntuación) # -5.65234375

# Puedes mapear las puntuaciones en un rango de 0-1 estableciendo "normalize=True", lo que aplicará una función sigmoide a la puntuación.
puntuación = reranker.compute_score(['consulta', 'pasa'], normalize=True)
print(puntuación) # 0.003497010252573502

puntuaciones = reranker.compute_score([['¿qué es panda?', 'hola'], ['¿qué es panda?', 'El panda gigante (Ailuropoda melanoleuca), a veces llamado oso panda o simplemente panda, es una especie de oso endémica de China.']])
print(puntuaciones) # [-8.1875, 5.26171875]

# Puedes mapear las puntuaciones en un rango de 0-1 estableciendo "normalize=True", lo que aplicará una función sigmoide a la puntuación.
puntuaciones = reranker.compute_score([['¿qué es panda?', 'hola'], ['¿qué es panda?', 'El panda gigante (Ailuropoda melanoleuca), a veces llamado oso panda o simplemente panda, es una especie de oso endémica de China.']], normalize=True)
print(puntuaciones) # [0.00027803096387751553, 0.9948403768236574]
```

Error

```bash
(mpsFileLoc): /AppleInternal/Library/BuildRoots/b11baf73-9ee0-11ef-b7b4-7aebe1f78c73/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShadersGraph/mpsgraph/MetalPerformanceShadersGraph/Core/Files/MPSGraphUtilities.mm:233:0: error: la operación 'mps.add' requiere el mismo tipo de elemento para todos los operadores y resultados
(mpsFileLoc): /AppleInternal/Library/BuildRoots/b11baf73-9ee0-11ef-b7b4-7aebe1f78c73/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShadersGraph/mpsgraph/MetalPerformanceShadersGraph/Core/Files/MPSGraphUtilities.mm:233:0: nota: ver la operación actual: %10 = "mps.add"(%8, %9) : (tensor<1x7x1xf16>, tensor<1xf32>) -> tensor<*xf32>
```

[FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding)