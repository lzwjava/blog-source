---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Escalador de Gradientes para Entrenamiento de Precisión Mixta
translated: true
type: note
---

`torch.cuda.amp.GradScaler` es una clase utilitaria de PyTorch diseñada para **escalar automáticamente los gradientes** durante el entrenamiento de precisión mixta usando **Precisión Mixta Automática (AMP)**. Ayuda a prevenir el desbordamiento inferior (underflow) en los gradientes cuando se usan tensores `float16` (precisión media), que de otra manera podrían volverse demasiado pequeños para ser representados con precisión.

---

### ¿Por qué usar `GradScaler`?

En el entrenamiento de precisión mixta:
- Los **pases forward/backward** usan `float16` para mayor velocidad y ahorro de memoria.
- Los **gradientes** calculados en `float16` pueden volverse muy pequeños → **desbordamiento inferior a cero (underflow)**.
- `GradScaler` escala la **pérdida (loss)** por un factor (ej., 2¹⁵ = 32768) antes del pase backward.
- Los gradientes se escalan proporcionalmente → permanecen en un rango representable.
- Antes del paso del optimizador, los gradientes se **re-escalan** a la normalidad.

---

### Uso Básico

```python
import torch
from torch.cuda.amp import autocast, GradScaler

model = MyModel().cuda()
optimizer = torch.optim.Adam(model.parameters())
scaler = GradScaler()  # init_scale por defecto=2**16

for data, target in dataloader:
    optimizer.zero_grad()

    # 1. Autocast para el forward
    with autocast():
        output = model(data)
        loss = loss_fn(output, target)

    # 2. Escalar la pérdida y hacer backward
    scaler.scale(loss).backward()

    # 3. Re-escalar + paso del optimizador
    scaler.step(optimizer)

    # 4. Actualizar la escala para la siguiente iteración
    scaler.update()
```

---

### Métodos Clave

| Método | Propósito |
|-------|--------|
| `scaler.scale(loss)` | Escala la pérdida antes de `.backward()` |
| `scaler.step(optimizer)` | Re-escala los gradientes y llama a `optimizer.step()` |
| `scaler.update()` | Ajusta el factor de escala para la siguiente iteración |
| `scaler.unscale_(optimizer)` | Re-escala los gradientes manualmente (rara vez necesario) |
| `scaler.get_scale()` | Devuelve el factor de escala actual |

---

### Cómo funciona el Escalado (Internamente)

1. **Escala inicial**: Usualmente `2**16 = 65536`
2. Después de `backward()`, verifica si hay **inf/NaN** en los gradientes.
3. Si **no hay inf/NaN** → la escala puede **aumentar** (ej., ×2) la próxima vez.
4. Si **se encuentra inf/NaN** → omite `optimizer.step()`, **reduce la escala** (ej., ÷2), y lo reintenta más tarde.

Esto hace que el entrenamiento sea **robusto** ante desbordamientos ocasionales.

---

### Parámetros Comunes

```python
scaler = GradScaler(
    init_scale=2.**16,     # Escala inicial
    growth_factor=2.0,     # Multiplicar cuando no hay inf
    backoff_factor=0.5,    # Dividir cuando hay inf
    growth_interval=2000,  # Pasos antes de aumentar la escala
    enabled=True
)
```

---

### Ejemplo con Recorte de Gradientes (Gradient Clipping)

```python
scaler.scale(loss).backward()
scaler.unscale_(optimizer)  # Necesario re-escalar antes del clipping
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
scaler.step(optimizer)
scaler.update()
```

> **Nota**: Siempre usa `unscale_` **antes** del clipping o de inspeccionar los gradientes.

---

### Mejores Prácticas

- Usar con `torch.cuda.amp.autocast()`
- Envolver **solo el forward + la pérdida** en `autocast()`
- Llamar a `scaler.update()` **en cada iteración**
- Usar `torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction=True` para mayor velocidad

---

### Cuándo No Usarlo

- Entrenamiento en `float32` puro
- Entrenamiento en CPU
- Bucles de entrenamiento personalizados que manejan el escalado manualmente

---

### Documentación Oficial

[https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler](https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler)

---

¡Avísame si quieres un ejemplo completo de un bucle de entrenamiento o una comparación con escalado manual!