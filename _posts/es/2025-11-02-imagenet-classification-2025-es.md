---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Avances en la Clasificación de ImageNet en 2025
translated: true
type: note
---

El estado del arte (SOTA) en ImageNet (específicamente en el conjunto de validación ImageNet-1K para clasificación de imágenes) ha continuado avanzando de manera constante desde las mejoras dramáticas posteriores a 2012. A noviembre de 2025, los modelos líderes logran precisiones top-1 de alrededor del 91%, lo que corresponde a una tasa de error top-1 de ~9%. Las precisiones top-5 son aún más altas, superando típicamente el 99%, para una tasa de error top-5 inferior al 1%.

### Modelos SOTA Clave (Top-5 del Ranking de Papers With Code)
Esta es una instantánea de los mejores modelos actuales (ajustados finamente en ImageNet-1K), basada en la precisión top-1. Las precisiones top-5 no siempre se reportan explícitamente para estos modelos de muy alto rendimiento (ya que se saturan cerca de niveles perfectos), pero la comparación con arquitecturas recientes similares sugiere errores top-5 inferiores al 1% para todos:

| Rango | Modelo | Precisión Top-1 | Prec. Top-5 Aprox. | Parámetros | Notas |
|------|--------|----------------|---------------------|------------|-------|
| 1 | CoCa (ajuste fino) | 91.0% (9.0% error) | ~99.5% (<0.5% error) | 2.1B | Modelo multimodal imagen-texto; destaca en configuración zero-shot (86.3% top-1) y con codificador congelado (90.6% top-1). |
| 2 | Model Soups (BASIC-L) | 90.98% (9.02% error) | ~99.4% (<0.6% error) | ~1B | Promedio de ensamblaje de modelos con ajuste fino para una robustez mejorada. |
| 3 | Model Soups (ViT-G/14) | 90.94% (9.06% error) | ~99.4% (<0.6% error) | 1.8B | Basado en ViT; fuerte generalización a datos fuera de distribución. |
| 4 | DaViT-Giant | 90.4% (9.6% error) | ~99.3% (<0.7% error) | 1.4B | ViT de atención dual; entrenado con 1.5B pares de imagen-texto. |
| 5 | ConvNeXt V2-Huge | 88.9% (11.1% error) | ~99.0% (~1.0% error) | 660M | Revitalización de CNN con preentrenamiento de autoencoder enmascarado; eficiente para dispositivos edge. |

### Aclaración sobre el "<3% Hoy"
- Esto se refiere a la **tasa de error top-5**, no a la top-1. Los puntos de referencia previos a 2012 (por ejemplo, SVMs) rondaban el 25% de error top-5. Para 2017 (SENet), bajó a ~2.3%. Los modelos SOTA modernos lo han llevado por debajo del 1%, haciendo que las predicciones top-5 sean esencialmente confiables para la mayoría de los casos de uso del mundo real.
- El error top-1 sigue siendo más alto (~9%) porque exige que coincida la predicción *exacta* principal, lo cual es más estricto y más sensible a casos extremos como imágenes ambiguas.

El progreso se ha ralentizado en los últimos años debido a la saturación del conjunto de datos; las ganancias ahora provienen de un preentrenamiento masivo (por ejemplo, en ImageNet-21K o datos a escala web) y técnicas como el ensamblaje de modelos o la destilación. El rendimiento de un experto humano se estima en ~5% de error top-1 (o 2-12% top-5, variando según el estudio), por lo que la IA ha superado a los humanos en este punto de referencia.

[Benchmark de ImageNet (Papers With Code)](https://paperswithcode.com/sota/image-classification-on-imagenet)  
[Clasificación de Imágenes: Modelos State-of-the-Art en 2025 (HiringNet)](https://hiringnet.com/image-classification-state-of-the-art-models-in-2025)  
[CoCa: Contrastive Captioners are Image-Text Foundation Models (arXiv)](https://arxiv.org/abs/2205.01917)