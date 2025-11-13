---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: La Brecha Entre el Rendimiento Teórico y el Real
translated: true
type: note
---

La discrepancia surge porque los **FLOPS teóricos máximos** (operaciones de punto flotante por segundo) miden el rendimiento aritmético bruto en condiciones ideales—asumiendo una utilización perfecta de todas las unidades de ejecución, sin cuellos de botella de memoria y con ancho de banda infinito. En cargas de trabajo reales (especialmente en IA/entrenamiento/inferencia), el rendimiento está limitado por **ineficiencias del subsistema de memoria**, no solo por la capacidad de cálculo. Las GPU Fermi de 2010 (por ejemplo, la GTX 480) eran particularmente malas en esto, inflando la brecha "esperada" cuando se comparan con tarjetas modernas como la RTX 4090.

### Razones Clave por las que Fermi No Aprovechaba sus FLOPS Teóricos
1. **Jerarquía de Caché Deficiente y Coalescencia de Memoria**
   - Fermi solo tenía 64 KB de caché L1 por SM (compartida con los registros) y una L2 minúscula de 768 KB (en todo el chip).
   - Sin coherencia de caché adecuada; los accesos a la memoria global no estaban coalescidos → **~10–30% de ancho de banda efectivo** en kernels reales.
   - Las GPU modernas (Ampere/Ada) tienen **L1 masiva (192 KB/SM)**, **cachés de textura dedicadas** y **precarga agresiva**, logrando un 70–90% del ancho de banda teórico.

2. **DDR5/GDDR5 de Alta Latencia y Bajo Ancho de Banda con ECC**
   - Fermi: ~170 GB/s GDDR5, **bus de 384 bits pero con sobrecarga de ECC** → ~130 GB/s efectivos.
   - RTX 4090: **1 TB/s GDDR6X**, 384 bits pero **sin penalización por ECC en modo consumidor**, más **mejor compresión**.
   - Los kernels de IA reales están **limitados por la memoria** (por ejemplo, GEMM con matrices grandes); los FLOPS no importan si los datos se estancan.

3. **Archivo de Registros y Planificación de Warp Ineficientes**
   - Fermi: 32k registros de 32 bits/SM → **máx. 1536 hilos** pero solo **~50% de ocupación** en la práctica debido al desbordamiento de registros.
   - Ada: archivo de registros de 256 KB → **2048 hilos/SM**, ocupación cercana al 100%.
   - Menos divergencia, mejor extracción de ILP.

4. **Estrangulamiento Térmico/de Energía**
   - GTX 480: 250 W TDP, **se estrangulaba fuertemente bajo carga sostenida** (los relojes bajaban un 10–20%).
   - RTX 4090: 450 W pero **~3x mejor rendimiento por vatio** gracias al proceso de 4 nm, DLSS y aumento dinámico.

### Ganancias Reales Medidas (Cargas de Trabajo de IA)

| Métrica | GTX 480 (Fermi, 2010) | RTX 4090 (Ada, 2022) | Aceleración |
|--------|------------------------|----------------------|---------|
| TFLOPS FP32 (pico) | 1.35 | 82.6 | **61x** |
| TFLOPS FP16 (pico) | ~0.7 (emulado) | 330 (Tensor) | **>400x** |
| **Entrenamiento ResNet-50 (img/s)** | ~60 | ~1,050 | **~17x** |
| **Inferencia GPT-2 (tokens/s)** | ~8 | ~140 | **~17x** |
| **Stable Diffusion (it/s)** | <0.1 | ~1.6 | **>16x** |

*Fuentes: documentos de NVIDIA, benchmarks MLPerf, AnandTech.*

### Conclusión
Los FLOPS teóricos asumían que Fermi podía mantener ~70% de utilización—no podía (real ~15–25%). Las arquitecturas modernas cierran esa brecha hasta **~70–90%**, por lo que **el cómputo efectivo escala más cerca de la Ley de Moore + mejoras de arquitectura** (~10–17x en 12 años), no los 60x+ que sugieren los FLOPS pico. El resto es "rendimiento en el papel".