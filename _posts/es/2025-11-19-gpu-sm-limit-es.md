---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Límite de SM de GPU para Sintonía Automática Máxima
translated: true
type: note
---

La advertencia "Not enough SMs to use max_autotune_gemm" proviene del backend TorchInductor de PyTorch (utilizado en `torch.compile` con `mode="max-autotune"` o modos de autosintonización agresivos similares). Indica que tu GPU tiene menos *Streaming Multiprocessors* (SMs) que el umbral requerido para las opciones de autosintonización de GEMM (multiplicación de matrices) más exhaustivas, que buscan en un espacio enorme de configuraciones de kernels Triton/CUTLASS para obtener el máximo rendimiento.

PyTorch considera una GPU "lo suficientemente grande" solo si tiene un número sustancial de SMs (típicamente ≥68–80, dependiendo de la versión exacta de PyTorch; por ejemplo, RTX 3080/3090 están en el límite, A100/H100/RTX 4090 están cómodamente por encima). En GPUs más pequeñas (por ejemplo, RTX 3060, 3070, 2080 Ti, T4, etc.), desactiva la ruta completa `max_autotune_gemm` para evitar tiempos de compilación excesivos o elecciones subóptimas.

### Por qué ocurre y su impacto
- La autosintonización evalúa muchas variantes de kernels en tiempo de compilación. La autosintonización completa de GEMM necesita suficiente paralelismo (SMs) para que las plantillas más agresivas sean rentables.
- La advertencia es **inofensiva** — la compilación aún tiene éxito, y obtienes un buen rendimiento (pero no el máximo absoluto). Otra autosintonización (partes no GEMM, búsqueda de GEMM menos agresiva) aún se ejecuta.
- **No** significa relleno/ineficiencia debido al tamaño del lote o la arquitectura del modelo de la manera en que podrías pensar. La interpretación sugerida por el usuario es cercana pero no del todo precisa aquí — esta advertencia específica es puramente sobre el tamaño de la GPU, no sobre el relleno de entrada/forma.

### Cómo mejorarlo o solucionarlo
1. **Usa una GPU con más SMs** (mejor solución para el máximo rendimiento real):
   - Mínimo recomendado para `max_autotune_gemm` completo confiable: RTX 4090 (128 SMs), A100 (108 SMs), H100 (132+ SMs), o tarjetas más nuevas de centro de datos.
   - Las tarjetas de consumo por debajo de ~80 SMs (por ejemplo, RTX 3070 = 46 SMs, RTX 3080 = 68 SMs) activarán esto.

   | Ejemplo de GPU | Cuenta de SM | ¿max_autotune_gemm completo? |
   |------------------|----------|--------------------------|
   | RTX 3060/3070    | 46–58   | No                       |
   | RTX 3080/3090    | 68–82   | En el límite (a veces sí) |
   | RTX 4090         | 128     | Sí                      |
   | A100             | 108     | Sí                      |
   | H100             | 132+    | Sí                      |

2. **Cambia el modo de torch.compile** (no se necesita cambio de hardware):
   - Usa `mode="max-autotune-no-cudagraphs"` — mantiene la mayoría de los beneficios de la autosintonización pero omite los CUDA graphs y la ruta GEMM condicionada por los SMs. A menudo es casi tan rápido con tiempos de compilación mucho más cortos en GPUs más pequeñas.
   - O `mode="reduce-overhead"` — más ligero, usa CUDA graphs para baja latencia, bueno para inferencia.
   - Ejemplo:
     ```python
     compiled_model = torch.compile(model, mode="max-autotune-no-cudagraphs", fullgraph=True)
     ```

3. **Habilita matmuls de alta precisión** (ayuda en cualquier modo/GPU):
   ```python
   torch.set_float32_matmul_precision("high")  # o "highest"
   ```
   Esto permite TensorFloat-32 / mejores kernels cuBLAS.

4. **Forzar una sintonización más agresiva de todos modos** (no oficial, no soportado):
   - Modificar el cheque en el código fuente de PyTorch (editar `torch/_inductor/utils.py` o parchear en tiempo de ejecución) para bajar el umbral de SMs. Arriesgado y puede perjudicar el rendimiento o aumentar enormemente el tiempo de compilación.

5. **Otros consejos generales para mejor alineación/eficiencia** (no relacionados con esta advertencia exacta pero abordan tu preocupación sobre el relleno):
   - Rellena las dimensiones del lote/secuencia a múltiplos de 8/16/32 si es posible (común para *Tensor Cores*).
   - Aumenta el tamaño del lote si tu carga de trabajo lo permite — los GEMMs más grandes utilizan mejor la GPU.
   - Para cargas de trabajo centradas en inferencia, considera alternativas como vLLM, TensorRT-LLM, o Hugging Face Optimum si las limitaciones de `torch.compile` persisten.

En la mayoría de los casos del mundo real, la diferencia de rendimiento por la falta de `max_autotune_gemm` completo es pequeña (unos pocos porcentajes), y `max-autotune-no-cudagraphs` te lleva al 95%+ del camino en GPUs de consumo.

[PyTorch Inductor utils.py source](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/utils.py)
[Torch.compile warning discussion](https://discuss.pytorch.org/t/torch-compile-warning-not-enough-sms-to-use-max-autotune-gemm-mode/184405)
[Dissecting torch.compile](https://themlsurgeon.substack.com/p/dissecting-torchcompile-surgical)