---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: FlashAttention Resuelve el Cuello de Botella de Memoria de los Transformadores
translated: true
type: note
---

### Antecedentes: Los desafíos de la atención estándar en los Transformers

Los Transformers, la base de modelos como GPT y BERT, dependen en gran medida del mecanismo de autoatención para procesar secuencias. En la autoatención, dadas secuencias de entrada representadas como la matriz de consultas \\(Q\\), la matriz de claves \\(K\\) y la matriz de valores \\(V\\) (cada una de forma \\(N \times d\\), donde \\(N\\) es la longitud de la secuencia y \\(d\\) es la dimensión de la cabeza, típicamente 64-128), la salida de atención \\(O\\) se calcula como:

\\[
S = QK^T \in \mathbb{R}^{N \times N}, \quad P = \softmax(S) \in \mathbb{R}^{N \times N}, \quad O = PV \in \mathbb{R}^{N \times d},
\\]

donde \\(\softmax\\) se aplica por filas, y \\(S\\) a menudo se escala por \\(\tau = 1 / \sqrt{d}\\) para mayor estabilidad. Operaciones adicionales como el enmascaramiento causal (para modelos autoregresivos) y dropout son comunes.

Esta formulación es elegante pero computacionalmente costosa. Las matrices intermedias \\(S\\) y \\(P\\) son \\(N \times N\\), lo que conduce a una **complejidad de tiempo y memoria cuadrática** \\(O(N^2)\\) en la longitud de la secuencia \\(N\\). Para contextos largos (por ejemplo, \\(N = 4096\\) en GPT-2 o hasta 128k en los LLM modernos), esto se convierte en un cuello de botella severo:

- **Demanda de Memoria**: En las GPUs, la memoria de alto ancho de banda (HBM) es el almacenamiento principal, pero materializar \\(S\\) y \\(P\\) puede exceder la HBM disponible (por ejemplo, 40-80 GB en A100/H100). En \\(N=4096\\), \\(d=64\\), esto solo consume ~1-2 GB solo para los intermedios, más las entradas/salidas/activaciones, a menudo causando errores de falta de memoria (OOM).
- **Limitaciones de Velocidad**: La atención está limitada por la memoria, no por el cómputo. Las GPUs modernas (por ejemplo, NVIDIA A100) tienen ~1.5 TB/s de ancho de banda de HBM pero ~19 TFLOPS de cómputo—sin embargo, operaciones como softmax requieren leer/escribir la matriz completa \\(N^2\\) múltiples veces (por ejemplo, 4-6 accesos a HBM por elemento en los pases forward/backward). Esto resulta en tiempos de ejecución que escalan cuadráticamente: por ejemplo, pase forward ~36 ms en \\(N=4096\\) en PyTorch, backward ~88 ms.
- **Barreras en Entrenamiento/Generación**: Durante el entrenamiento, los gradientes requieren almacenar \\(P\\) para el pase backward, duplicando la memoria. Para la inferencia, los contextos largos (por ejemplo, 64k tokens) son inviables sin aproximaciones como atención dispersa o métodos de bajo rango (por ejemplo, Reformer, Linformer), que intercambian exactitud por eficiencia pero a menudo tienen un rendimiento inferior debido a que ignoran los costos de E/S.

FlashAttention (introducido en 2022 por Tri Dao et al.) aborda estos problemas al repensar el algoritmo para que sea **consciente de la E/S**, aprovechando la jerarquía de memoria de la GPU (SRAM rápida ~20 MB vs. HBM lenta) sin aproximaciones.

### Ideas Centrales: Mosaico (Tiling), Fusión de Kernels y Softmax en Línea (Online)

FlashAttention calcula la atención **exacta** (sin aproximaciones) mediante:

1.  **Mosaico (Tiling)**: En lugar de materializar las matrices completas \\(N \times N\\), divide \\(Q, K, V\\) en pequeños bloques que caben en la SRAM. \\(Q\\) se divide en \\(T_r = \lceil N / B_r \rceil\\) bloques de filas de tamaño \\(B_r \times d\\) (por ejemplo, \\(B_r \approx 64-256\\)), y \\(K, V\\) en \\(T_c = \lceil N / B_c \rceil\\) bloques de columnas de tamaño \\(B_c \times d\\) (por ejemplo, \\(B_c \approx 128-1024\\)). Los tamaños de bloque se eligen dinámicamente según la capacidad de la SRAM \\(M\\) (por ejemplo, \\(B_c \approx M / (4d)\\)) para maximizar la reutilización.

2.  **Fusión de Kernels**: Todas las operaciones (matmul para \\(S\\), enmascaramiento, softmax, dropout, matmul para \\(O\\)) se fusionan en un único kernel de CUDA. Esto evita escribir intermedios a la HBM, reduciendo la E/S en ~50-70%. El kernel carga bloques de la HBM a la SRAM, calcula en el chip y escribe solo sumas parciales de vuelta—por ejemplo, una lectura/escritura de HBM por bloque en lugar de por elemento.

3.  **Softmax en Línea con Estadísticas**: Softmax no se puede calcular parcialmente sin la fila completa, por lo que FlashAttention utiliza una **descomposición asociativa** para el cálculo incremental. Para una fila dividida en bloques \\(x = [x^{(1)}; x^{(2)}]\\), se realiza un seguimiento de las estadísticas en ejecución:
    - Máximo por fila \\(m_i = \max_j S_{ij}\\),
    - Suma por fila de exponenciales \\(\ell_i = \sum_j \exp(S_{ij} - m_i)\\).

    Actualizando para un nuevo bloque \\(x^{(t)}\\) con estadísticas locales \\(\tilde{m}_t, \tilde{\ell}_t\\):
    \\[
    m_i^{\new} = \max(m_i, \tilde{m}_t), \quad \ell_i^{\new} = e^{m_i - m_i^{\new}} \ell_i + e^{\tilde{m}_t - m_i^{\new}} \tilde{\ell}_t.
    \\]
    El softmax parcial es entonces \\(\tilde{P}_{ij} = \exp(S_{ij} - m_i^{\new})\\), y la salida se acumula como \\(O_i \leftarrow \frac{\ell_i}{\ell_i^{\new}} e^{m_i - m_i^{\new}} O_i + \frac{\tilde{\ell}_t}{\ell_i^{\new}} e^{\tilde{m}_t - m_i^{\new}} \tilde{P}_{ij} V_j\\).

    Esto es numéricamente estable (coincide con softmax fusionado) y exacto, como se demuestra inductivamente: después de todos los bloques, \\(O = \softmax(S) V\\).

Estas ideas reducen la **memoria a \\(O(N)\\)** (entradas + salida + estadísticas \\(O(N)\\) como \\(m, \ell\\)) y los **accesos a HBM a \\(O(N^2 d / M)\\)**—subcuadrático, ya que cada elemento de \\(K/V\\) se lee una vez, y \\(Q/O\\) se lee \\(T_c \approx N d / M\\) veces.

### Pase Forward: Cálculo Bloque por Bloque

El pase forward (pseudocódigo en el Algoritmo 2 del artículo) itera sobre los bloques de columna de \\(K, V\\):

- Inicializar \\(O = 0^{N \times d}\\), \\(m = -\infty^N\\), \\(\ell = 0^N\\) en HBM.
- Para cada bloque de columna \\(j = 1\\) a \\(T_c\\):
  - Cargar \\(K_j, V_j\\) a SRAM (reutilizar a través de las filas).
  - Para cada bloque de fila \\(i = 1\\) a \\(T_r\\):
    - Cargar \\(Q_i, O_i, m_i, \ell_i\\) a SRAM.
    - Calcular \\(S_{ij} = \tau Q_i K_j^T\\) local (\\(B_r \times B_c\\)).
    - Enmascarar: \\(S_{ij}^{\masked} = \mask(S_{ij})\\) (por ejemplo, causal: triángulo inferior a \\(-\infty\\)).
    - Estadísticas de softmax local: \\(\tilde{m}_{ij} = \rowmax(S_{ij}^{\masked})\\), \\(\tilde{P}_{ij} = \exp(S_{ij}^{\masked} - \tilde{m}_{ij})\\), \\(\tilde{\ell}_{ij} = \rowsum(\tilde{P}_{ij})\\).
    - Actualizar estadísticas globales y salida usando las fórmulas anteriores, aplicando dropout a \\(\tilde{P}_{ij}\\).
    - Escribir \\(O_i, m_i, \ell_i\\) actualizados a HBM.

Esto fusiona todo: los FLOPs totales permanecen en \\(O(N^2 d)\\), pero la E/S cae dramáticamente (por ejemplo, 9x menos accesos que el estándar). Para atención causal, el enmascaramiento es barato (vectorizado). Dropout utiliza un estado RNG compartido \\(R\\) guardado para el backward.

### Pase Backward: Cálculo del Gradiente mediante Recomputación

El pase backward (Algoritmo 4) es más complicado, ya que los gradientes dependen de \\(P\\):

\\[
dP = dO \cdot V^T, \quad dS = P \odot (dP - \rowsum(dO \odot O)), \quad dQ = dS \cdot K, \quad dK = Q^T \cdot dS, \quad dV = P^T \cdot dO.
\\]

Almacenar \\(P\\) sería \\(O(N^2)\\), por lo que FlashAttention **recalcula los bloques sobre la marcha** (recomputación selectiva, como checkpointing pero en mosaico):

- Iterar de manera similar: para cada \\(j\\), cargar \\(K_j, V_j\\); inicializar \\(dK_j, dV_j = 0\\) locales.
- Para cada \\(i\\): recalcular \\(S_{ij}, P_{ij}\\) usando \\(m_i, \ell_i\\) guardadas; regenerar la máscara de dropout a partir de \\(R\\).
- Calcular gradientes locales: \\(dV_j += P_{ij}^{dropped^T} dO_i\\), \\(dP_{ij} = dO_i V_j^T \odot Z_{ij}\\) (máscara de dropout), \\(dS_{ij} = P_{ij} \odot (dP_{ij} - D_i)\\) donde \\(D_i = \rowsum(dO_i \odot O_i)\\).
- Acumular \\(dQ_i += \tau dS_{ij} K_j\\), \\(dK_j += \tau Q_i^T dS_{ij}\\).

Esto utiliza otros \\(O(N^2 d)\\) FLOPs pero solo \\(O(N)\\) memoria extra (sin almacenamiento de \\(P\\)). Total forward + backward: ~2-3x los FLOPs del estándar pero 2-4x más rápido debido al ahorro de E/S.

### Conciencia de E/S y Optimizaciones de GPU

Las GPUs tienen una jerarquía: registros/SRAM (rápida, pequeña) >> HBM (lenta, grande). La atención estándar satura la HBM con \\(\Theta(N^2)\\) accesos por pase. El mosaico de FlashAttention asegura:
- \\(K, V\\) cargados una vez (\\(O(N d)\\)).
- \\(Q, O\\) cargados \\(T_c \approx N / B_c \approx N d / M\\) veces (\\(O(N^2 d / M)\\)).
- Límite inferior: Ningún algoritmo exacto supera \\(\Omega(N^2 d^2 / M)\\) para \\(M\\) en rango medio.

Empírico: En A100, los bloqueos de HBM dominan el tiempo de ejecución; FlashAttention los reduce en un 50-80%, alcanzando el régimen limitado por cómputo. Soporta dispersidad por bloques (saltar bloques con máscara cero) para ganancias aún mayores (2-4x sobre el denso).

### Beneficios: Velocidad, Memoria e Impacto Derivado

- **Memoria**: Lineal \\(O(N d)\\), permitiendo secuencias de 64k+ en GPUs individuales (frente a 2k-4k estándar). Por ejemplo, 13 GB en \\(N=65k\\) frente a 200+ GB estándar.
- **Velocidad**: 2-4x de extremo a extremo en el entrenamiento de GPT/BERT; hasta 7x en atención pura. Por ejemplo, fwd/bwd combinados: 0.43 ms en \\(N=128\\) a 9s en \\(N=65k\\) (frente a PyTorch OOM).
- **Calidad**: Exacta, por lo que no hay caída en la perplejidad. Permite contextos más largos: ganancia de 0.7 puntos en perplejidad en GPT-2 a 4x de longitud; estado del arte en tareas de documentos largos (por ejemplo, 63% en Path-256 a 64k secuencias).
- **Extensiones**: FlashAttention-2 (2023) añade mejor paralelismo (hasta 2x más rápido); FlashAttention-3 (2024) utiliza asincronía/baja precisión para H100 (50% más rápido).

### Integración con PyTorch: Uso Transparente

PyTorch 2.0+ integra FlashAttention de forma nativa a través de `torch.nn.functional.scaled_dot_product_attention(q, k, v)`, que envía automáticamente al kernel fusionado si se cumplen las condiciones (por ejemplo, tensores contiguos, tipos de datos soportados). No se necesita CUDA personalizado:

```python
import torch
from torch.nn.functional import scaled_dot_product_attention

q, k, v = torch.randn(1, 8, 1024, 64, device='cuda')  # lote, cabezas, secuencia, dim
with torch.backends.cuda.sdp_kernel(enable_flash=True, enable_math=False):
    out = scaled_dot_product_attention(q, k, v, attn_mask=mask, dropout_p=0.1)
```

Esto maneja el enmascaramiento/dropout; vuelve al kernel math si no es compatible. Para modelos personalizados, es un reemplazo directo para los bucles de atención manuales, produciendo aceleraciones de 2-3x inmediatas.

FlashAttention revolucionó el entrenamiento de contextos largos, impulsando modelos como Llama-2 (4k→70B) y más allá.

[FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)  
[PyTorch 2.2: FlashAttention-v2 Integration](https://pytorch.org/blog/pytorch2-2/)  
[GitHub: Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)