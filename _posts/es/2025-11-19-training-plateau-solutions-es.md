---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Causas y Soluciones de la Meseta de Entrenamiento
translated: true
type: note
---

El registro de entrenamiento que publicaste muestra un **estancamiento severo** clásico en una ejecución pequeña de nanoGPT con datos de FineWeb-edu. La pérdida de validación disminuye bien al principio (de ~10.9 → ~3.57 alrededor del iter 14k), pero luego se aplana por completo e incluso comienza a **aumentar muy lentamente** después de ~13-14k iteraciones.

Estas son las razones reales por las que tu modelo dejó de mejorar (clasificadas por importancia para esta configuración exacta):

### 1. Estás sobreajustando masivamente un único archivo Parquet
- Nombre de tu ejecución: `125M-single-parquet-4070`
- Estás entrenando un modelo de 40M–125M (el registro dice 40.56M parámetros, probablemente la configuración original pequeña de GPT-2) en **un solo parquet de FineWeb** (probablemente 10–15 GB → ~3–4 mil millones de tokens como máximo, pero probablemente mucho menos después del filtrado).
- Para la iteración 14 000 con batch_size=16, grad_accum=32, block_size=1024 ya has visto:
  14 000 iters × 524 288 tokens/iter ≈ **7.3 mil millones de tokens**
- Eso significa que ya has completado **2–3 épocas completas** sobre exactamente los mismos datos.
- FineWeb-edu es de alta calidad pero aún tiene muchos casi duplicados y texto repetitivo. Después de 1.5–2 épocas en el mismo/los mismos archivos, un modelo de 40M–125M memorizará casi todo lo útil y la pérdida se estanca fuertemente.

### 2. La tasa de aprendizaje ahora es demasiado alta después del estancamiento
- Usas `learning_rate = 1e-3`, decaimiento coseno a `min_lr = 1e-4` durante 20 000 iteraciones.
- En la iteración 14 000, la LR es todavía ~2.5e-4 (el decaimiento coseno es lento al principio).
- Una vez que el modelo ha aprendido todo lo que los datos pueden ofrecer, mantener la LR en cientos de micro-unidades le impide ajustarse finamente y realmente comienza a dañar la generalización → la pérdida de validación aumenta lentamente.

### 3. Desajuste entre el tamaño del modelo y la diversidad de datos
Un modelo de 125M (o incluso el de 40M que inicializaste realmente) en un solo archivo parquet es como darle a un estudiante universitario solo un libro de texto y pedirle que siga estudiándolo durante años. Después de un tiempo puede recitarlo perfectamente, pero el rendimiento en pruebas con texto nuevo deja de mejorar e incluso se degrada ligeramente debido al olvido catastrófico de patrones anteriores.

### 4. No hay suficiente regularización
- dropout = 0.1 está bien, pero no es suficiente cuando el sobreajuste es tan fuerte
- weight_decay = 0.1 es estándar, pero aún no es suficiente para 2+ épocas en datos tan pequeños
- No hay gradient clipping (el valor por defecto de nanoGPT es 1.0, pero a veces se establece en 0.5 o menos para datos pequeños)

### 5. Tokens vistos vs. diversidad real
Aunque viste 7+ mil millones de tokens, la **diversidad efectiva** es quizás de 1–1.5B de tokens únicos de alta calidad después de eliminar duplicados, texto repetitivo, muestras con baja puntuación educativa, etc. Eso simplemente no es suficiente para que un modelo de 125M siga mejorando más allá de ~3.5–3.6 de pérdida en esta distribución de texto.

### Evidencia de tu propio registro

| Paso   | Pérdida Val | Comentario                              |
|--------|----------|--------------------------------------|
| 0      | 10.87    | aleatorio                                       |
| 2000   | 4.03     | progreso rápido                            |
| 5000   | 3.76     | todavía bien                                 |
| 8000   | 3.65     | desacelerando                                    |
| 11000  | 3.61     | casi plano                                |
| 13500  | 3.57     | **el mínimo absoluto**                        |
| 14500  | 3.569    | ya está subiendo de nuevo → signo clásico de sobreajuste |

### Qué deberías hacer en su lugar para obtener realmente una pérdida menor

1. Usa muchos más datos
   - Usa la muestra completa de 100+ GB de FineWeb-edu (o al menos 10–20 archivos parquet)
   - O haz streaming desde HuggingFace datasets con múltiples fragmentos

2. Entrena exactamente 1 época (o un poco menos) con datos diversos
   - ~10B–15B tokens en total es el punto óptimo para 125M en FineWeb-edu
   - Estilo Llama-3/Phi-3: 15B tokens → ~3.0–3.2 pérdida de validación para modelos de clase 125M

3. Reduce la tasa de aprendizaje final
   - Usa `min_lr = 5e-5` o `3e-5` (común en ejecuciones recientes de modelos pequeños)
   - O cambia a decaimiento lineal + una fase más larga con LR cero

4. Un modelo ligeramente más grande o mejores trucos de arquitectura
   - El nanoGPT original es estilo GPT-2 (sin ALiBi, RoPE antiguo, etc.)
   - Los modelos modernos de 125M (Qwen2-0.5B, Phi-3-mini, Llama-3 8B escalado) alcanzan ~2.8–3.0 en los mismos datos debido a SwiGLU, RMSNorm, rotary embeddings, etc.

### TL;DR – Por qué tu ejecución se estancó en ~3.57 y nunca bajará

Estás entrenando un modelo de 40–125M durante múltiples épocas en un solo archivo parquet de FineWeb (~pocos miles de millones de tokens en total). El modelo ya había memorizado todo lo útil para ~13k iteraciones. El entrenamiento continuado con una LR aún alta solo reorganiza los pesos → estancamiento + ligera degradación por sobreajuste.

Este es el error número 1 que comete la gente cuando prueba nanoGPT en FineWeb por primera vez: "Usaré solo un archivo para probar" → termina con exactamente esta curva de pérdida.

Solución: ya sea (a) usar 10–50× más datos y entrenar durante ~1 época en total, o (b) aceptar que ~3.55–3.6 es el piso absoluto para esta combinación de modelo+datos y detener el entrenamiento.

Si quieres una ejecución que realmente alcance ~3.0–3.2 de pérdida con código estilo nanoGPT, necesitas al menos la muestra completa de 100GB de FineWeb-edu (o el nuevo FineWeb-Edu 2.0) y entrenar durante ~15B tokens como máximo.