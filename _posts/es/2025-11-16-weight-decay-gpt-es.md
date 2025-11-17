---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Decaimiento del Peso en el Entrenamiento de Modelos GPT
translated: true
type: note
---

La decaimiento de pesos (weight decay) es una técnica de regularización común utilizada al entrenar modelos GPT (y casi todos los modelos de lenguaje grandes) para prevenir el sobreajuste y mejorar la generalización.

### Lo que realmente hace
El decaimiento de pesos añade un término de penalización a la función de pérdida que empuja los pesos del modelo hacia valores más pequeños. Matemáticamente, si tu pérdida original es ℒ (por ejemplo, entropía cruzada), con decaimiento de pesos optimizas:

ℒ_total = ℒ + (λ / 2) × ||w||²

donde:
- w son los parámetros del modelo (pesos)
- ||w||² es la norma L2 al cuadrado de los pesos
- λ (lambda) es el coeficiente de decaimiento de pesos (típicamente 0.01 ~ 0.1 en el entrenamiento estilo GPT)

Este término adicional disuade al modelo de aprender pesos muy grandes a menos que reduzcan significativamente la pérdida original.

### Cómo se implementa en la práctica (AdamW)
En la mayoría de los entrenamientos de GPT (GPT-2, GPT-3 de OpenAI, LLaMA, Mistral, etc.), la gente NO usa Adam simple con regularización L2 estándar. En su lugar, usan AdamW (Adam con decaimiento de pesos desacoplado).

La diferencia clave:
- La regularización L2 estándar en Adam añade la penalización directamente en el gradiente.
- AdamW lo desacopla: aplica el decaimiento de pesos como un paso de actualización separado, lo que funciona mucho mejor con optimizadores adaptativos como Adam.

Así que cuando ves algo como esto en las configuraciones de entrenamiento:

```python
optimizer = AdamW(model.parameters(), lr=5e-5, weight_decay=0.1)
```

Ese 0.1 es la λ de arriba, y está usando la versión desacoplada correcta.

### Valores típicos en modelos reales estilo GPT

| Modelo / Paper       | Decaimiento de Pesos | Notas                                   |
|----------------------|----------------------|-----------------------------------------|
| GPT-2 (OpenAI)       | 0.01                 |                                         |
| GPT-3 (OpenAI)       | 0.1                  | Brown et al. 2020                       |
| LLaMA 1 & 2 (Meta)   | 0.1                  | A menudo combinado sin decaimiento en normas/sesgos |
| PaLM (Google)        | 0.1                  |                                         |
| Grok-1 (xAI)         | 0.1                  | De la configuración de lanzamiento abierto |
| Mistral / Mixtral    | 0.1                  |                                         |

### Matiz importante: ¿qué parámetros reciben decaimiento de pesos?
La práctica moderna (desde LLaMA) es aplicar el decaimiento de pesos solo a ciertas capas:
- Sí: Capas lineales (matrices de pesos), matriz de embeddings
- No: Términos de sesgo (bias), pesos de LayerNorm, cualquier parámetro 1D

Esto usualmente se hace con grupos de parámetros en PyTorch:

```python
decay = set()
no_decay = set()
for name, param in model.named_parameters():
    if "bias" in name or "layer_norm" in name or param.ndim == 1:
        no_decay.add(param)
    else:
        decay.add(param)

optimizer = AdamW([
    {"params": list(decay),   "weight_decay": 0.1},
    {"params": list(no_decay), "weight_decay": 0.0}
], lr=...)
```

### Por qué es importante para modelos a escala GPT
Con miles de millones o cientos de miles de millones de parámetros, los modelos pueden memorizar fácilmente los datos de entrenamiento. El decaimiento de pesos es una de las herramientas más simples y efectivas (junto con dropout, profundidad estocástica, etc.) para mantener la capacidad efectiva bajo control y mejorar el rendimiento posterior.

En resumen: el decaimiento de pesos ≈ regularización L2, pero implementado correctamente a través de AdamW y aplicado selectivamente, es un ingrediente estándar en virtualmente todas las recetas modernas de preentrenamiento estilo GPT.