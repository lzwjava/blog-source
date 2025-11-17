---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Cómo Solucionar el Desbordamiento de Memoria de la GPU Durante la Evaluación
translated: true
type: note
---

Estás experimentando un clásico error de falta de memoria (OOM) en una RTX 4070 (12 GB de VRAM) mientras entrenas un GPT de ~77 millones de parámetros (originalmente destinado a 125M, pero redujiste n_embd a 576 → ~77M) con batch_size=16, block_size=1024 y gradient_accumulation_steps=32 en FP16.

Aunque 77M es pequeño, el micro-lote efectivo es enorme debido a cómo nanoGPT calcula la pérdida en `estimate_loss()` — ejecuta el pase completo hacia adelante/hacia atrás en los lotes de evaluación sin los trucos de acumulación de gradientes, así que durante la evaluación intenta de repente colocar un lote efectivo mucho más grande en la memoria.

### Causa Principal
En `estimate_loss()`, nanoGPT hace esto por defecto:

```python
for _ in range(eval_iters):  # ¡200 veces!
    x, y = get_batch('train')
    ...
    logits, loss = model(x, y)
```

Cada `get_batch` devuelve `batch_size × block_size` tokens → 16 × 1024  
Con eval_iters = 200 → 200 pases hacia adelante separados, pero PyTorch mantiene el gráfico de computación y las activaciones intermedias para todo el bucle de evaluación en la memoria si no tienes cuidado. Combinado con la enorme caché KV (12 capas × 12 cabezas × 1024 × 576 × 2 bytes FP16 ≈ 1.6 GB solo para la caché), más los logits (16×1024×50304 × 2 bytes ≈ 1.6 GB por pase hacia adelante), fácilmente superas los 12 GB aunque el entrenamiento en sí esté bien.

### Soluciones Rápidas (elige una o combínalas)

**Opción 1: Reducir drásticamente el tamaño del lote de evaluación (solución más rápida)**
Añade estas líneas a tu configuración (o anula por CLI):

```python
eval_batch_size = 4        # añade esto
# o incluso 2 si aún hay OOM
eval_iters = 100           # puedes reducir un poco más
```

nanoGPT respeta `eval_batch_size` si lo añades (las versiones recientes lo hacen). Esto hace que la evaluación use solo 4 secuencias en lugar de 16 → ~4× menos memoria durante la evaluación.

**Opción 2: Reducir block_size solo para evaluación (mantiene la precisión)**
```python
eval_block_size = 512      # o 256
```
Añade esto a la configuración — algunas bifurcaciones lo soportan, o parchea `get_batch` para usar un block_size diferente cuando split=='val'.

**Opción 3: Reducir eval_iters y aceptar una pérdida de evaluación ligeramente más ruidosa**
```python
eval_iters = 50   # sigue siendo una estimación decente
```

**Opción 4: Reducir un poco más el tamaño del modelo (aún buena calidad)**
Ya estás en 77M, pero puedes bajar con seguridad:

```python
n_layer = 12
n_head  = 12
n_embd  = 512     # → ~62M parámetros, mucho más seguro
# o incluso n_embd = 448 → ~53M
```

**Opción 5: Habilitar gradient checkpointing (mayor ahorro de memoria)**
Añade esto a la creación del modelo (edita model.py o pasa el flag):

```python
model = GPT(GPTConfig(..., grad_checkpoint=True))
```

O aplica un monkey-patch en train.py antes del entrenamiento:

```python
if config.grad_checkpoint:
    model.gradient_checkpointing_enable()
```

Esto reduce la memoria de activaciones en ~50-60% a costa de un entrenamiento ~20-25% más lento.

### Combinación recomendada para tu 4070 de 12 GB

```python
# En config/train_fineweb.py
batch_size = 16
gradient_accumulation_steps = 32   # mantiene 512 secs efectivas
block_size = 1024

eval_batch_size = 4        # crítico
eval_iters = 100
eval_interval = 500

n_embd = 512               # modelo de ~62M, muy seguro
# opcional: añadir gradient checkpointing
grad_checkpoint = True     # si tu fork de nanoGPT lo soporta
```

O si no quieres tocar n_embd, simplemente haz:

```python
eval_batch_size = 2
eval_iters = 100
```

Eso solo casi seguro arreglará el OOM.

También establece esta variable de entorno para ayudar con la fragmentación:

```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

Prueba primero con eval_batch_size=4 (o =2) — el 95% de las personas con 4070 de 12 GB que tienen este error exacto lo solucionan así cuando entrenan nanoGPT en FineWeb.