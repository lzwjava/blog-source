---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Cuantización de 4 bits para LLM eficientes
translated: true
type: note
---

### ¿Qué es la cuantización de 4 bits (en el contexto de QLoRA o GPTQ)?

La cuantización de 4 bits es una técnica para reducir drásticamente la huella de memoria de los modelos de lenguaje grandes (LLMs) almacenando cada peso usando solo 4 bits en lugar de la precisión habitual de 16 bits (FP16/BF16) o 32 bits (FP32).

Modelos normales (precisión completa):
- FP32: 4 bytes por parámetro → modelo de 7B ≈ 28 GB
- FP16/BF16: 2 bytes por parámetro → modelo de 7B ≈ 14 GB

Cuantización de 4 bits:
- ~0.5 bytes por parámetro → modelo de 7B ≈ 3.5–4 GB (aproximadamente 1/4 a 1/8 del tamaño original dependiendo del método exacto)

Hoy en día comúnmente se ven dos enfoques principales de 4 bits:

| Método | Nombre completo | Artículo principal / año | Caso de uso típico | Características principales |
|----------|----------------------------|-------------------|-----------------------------------|---------------------------------------------------------------------------------------|
| GPTQ | GPTQ | 2023 | Cuantización post-entrenamiento (solo inferencia) | One-shot, muy preciso, no necesita reentrenamiento. Redondea los pesos a 4 bits después del entrenamiento. |
| QLoRA | Quantized Low-Rank Adaptation | 2023 (Jun) | Fine-tuning eficiente / ajuste por instrucción | Combina almacenamiento de 4 bits + adaptadores LoRA + optimizadores paginados. Permite fine-tuning de modelos de 65B+ en una sola GPU de 24–48 GB. |

#### QLoRA en más detalle (a lo que la gente usualmente se refiere cuando dice "4-bit QLoRA")
QLoRA hace cuatro cosas inteligentes a la vez:

1.  Cuantización 4-bit NormalFloat (NF4)
    - Un tipo de datos especial de 4 bits optimizado para pesos distribuidos normalmente (la mayoría de los pesos de los LLMs son ≈ Gaussianos después del entrenamiento).
    - Mejor que INT4 simple; teóricamente óptimo para datos distribuidos normalmente.

2.  Doble cuantización
    - Incluso las constantes de cuantización (factores de escala) se cuantizan de FP16 → 8-bit, ahorrando unos pocos MB más.

3.  Optimizadores paginados
    - Los estados del optimizador (momentos de AdamW) se almacenan en la RAM de la CPU y se paginan a la GPU con memoria unificada de NVIDIA. Previene OOM durante el entrenamiento.

4.  Adaptadores LoRA
    - Solo entrena pequeñas matrices de bajo rango (r=64 o menos) mientras que el modelo base de 4 bits permanece congelado.

Resultado: Puedes hacer fine-tuning completo de un modelo de 65B como Llama/Mistral en una sola RTX A6000 de 48 GB o incluso un modelo de 70B en una sola A100 de 80 GB con QLoRA, mientras que el fine-tuning normal completo necesitaría 8×A100s o más.

#### GPTQ (el centrado en inferencia)
- Se realiza después de que termina el entrenamiento.
- Utiliza información de segundo orden (Hessiana) para minimizar el error de redondeo al comprimir los pesos a 4 bits.
- Extremadamente preciso — usualmente <0.1 de degradación de perplexity vs FP16.
- Popular con herramientas como AutoGPTQ, ExLlama, vLLM y llama.cpp (GGUF también tiene modos estilo GPTQ).

### Gradient Checkpointing (también llamado "activation checkpointing")

Una técnica completamente separada para ahorrar memoria utilizada durante el entrenamiento.

Cómo funciona:
- Normalmente, la retropropagación necesita almacenar todas las activaciones intermedias del pase forward → la memoria crece linealmente con la profundidad del modelo/tamaño del lote/longitud de la secuencia.
- El Gradient Checkpointing intercambia computación por memoria:
  - Durante el pase forward, solo guarda unas pocas activaciones de "punto de control" (checkpoint).
  - Durante el pase backward, re-calcula las activaciones faltantes sobre la marcha.

Ahorro típico de memoria: 50–80% de la memoria de activación, a costa de un entrenamiento ~20–30% más lento.

Casi siempre se usa junto con QLoRA o cualquier fine-tuning de modelo grande porque incluso con pesos de 4 bits, las activaciones aún saturan la memoria de la GPU.

### Resumen TL;DR

"Cuántización de 4 bits (estilo QLoRA o GPTQ) + gradient checkpointing" es la receta moderna para:

- Ejecutar o hacer fine-tuning de modelos enormes (33B, 70B, 405B) en GPUs de consumo o una sola GPU empresarial.
- 4 bits estilo QLoRA → fine-tuning con uso de memoria de GPU muy bajo.
- 4 bits estilo GPTQ → inferencia rápida con uso de memoria de GPU muy bajo.
- Gradient Checkpointing → hace posible el backward pass en secuencias largas sin OOM.

Juntos son la razón por la que ves a gente haciendo fine-tuning de Llama-3-70B en una sola 3090/4090 hoy en día.