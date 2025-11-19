---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Agotamiento de Memoria Causa Congelamiento del Sistema
translated: true
type: note
---

Tu problema **no** es la GPU (la 4070 Ti apenas se está usando aquí). Este script es **puro CPU + RAM**, y el bloqueo + congelación de la GUI después de ~140M tokens es casi seguro porque **te estás quedando sin RAM** y el sistema comienza a hacer swapping intensivo al disco, lo que congela todo durante minutos u horas.

### Por qué ocurre en ~140M–200M tokens

Cada token → se almacena como uint16 → 2 bytes.

- 140 millones de tokens ≈ 280 MB
- 1 billón de tokens ≈ 2 GB
- 10 billones de tokens (FineWeb-10B completo) ≈ 20 GB
- 100B+ tokens (como muchas descargas de FineWeb/Edu) ≈ 200+ GB

Pero mira tu lista `all_tokens = []` en Python: las listas de Python tienen una sobrecarga masiva. Cada objeto entero ocupa ~28–32 bytes en Python de 64 bits (incluso si el valor cabe en uint16).

Uso real de memoria al construir la lista:
- ~150M tokens en una lista de Python → ~150M × 28–32 bytes ≈ **4–5 GB** solo para los objetos de la lista
- Luego haces `np.array(..., dtype=np.uint16)` → otros ~300 MB para el array compacto
- Pico total de RAM durante la conversión ≈ 5–6 GB + SO + sobrecarga del escritorio

Tienes 62.6 GB de RAM, ¿por qué se congela con solo 140M tokens?

Porque tu archivo de entrada `train_fineweb.txt` es probablemente **mucho más grande** de lo que piensas.

La gente a menudo descarga muestras de FineWeb-100B o incluso 1T y las nombra "train_fineweb.txt". Si tu archivo es, por ejemplo, la popular muestra FineWeb-Edu de 100B tokens (~200–300 GB de archivo de texto), el script seguirá leyendo indefinidamente, la lista `all_tokens` crecerá a decenas o cientos de miles de millones de tokens → cientos de GB de RAM → OOM → thrashing de swap → congelación completa del escritorio. Los ventiladores de la GPU giran porque el script sigue vivo (apenas), Python está atascado en el `extend()` o en la conversión final `np.array()`.

### Soluciones (elige una)

#### Mejor solución: Transmitir directamente a .bin sin mantener todos los tokens en RAM
Esta versión usa casi nada de RAM (pico < 1 GB incluso para texto de tamaño terabyte):

```python
# stream_tokenize_to_bin.py
import os
import numpy as np
import tiktoken

enc = tiktoken.get_encoding("gpt2")
CHUNK_SIZE = 1_000_000  # caracteres por chunk, ajustar si es necesario

def process_file(input_path: str, train_bin: str, val_bin: str, val_ratio=0.0005):
    temp_train = train_bin + '.tmp'
    temp_val = val_bin + '.tmp'

    total_tokens = 0
    val_tokens_written = 0
    val_target = None  # lo decidimos después del primer paso o aproximamos

    with open(input_path, "r", encoding="utf-8", errors='ignore') as f, \
         open(temp_train, "wb") as train_f, \
         open(temp_val, "wb") as val_f:

        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            tokens = enc.encode_ordinary(chunk)
            tokens_u16 = np.array(tokens, dtype=np.uint16)

            total_tokens += len(tokens_u16)

            # Aproximar la división de validación sobre la marcha (suficientemente bueno)
            if val_target is None and total_tokens > 10_000_000:
                val_target = int(total_tokens * val_ratio / (1 - val_ratio))

            if val_tokens_written < val_target:
                split_point = min(len(tokens_u16), val_target - val_tokens_written)
                val_f.write(tokens_u16[:split_point].tobytes())
                train_f.write(tokens_u16[split_point:].tobytes())
                val_tokens_written += split_point
            else:
                train_f.write(tokens_u16.tobytes())

            if total_tokens % 50_000_000 == 0:
                print(f"Procesados {total_tokens/1e6:.1f}M tokens")

    # Renombrar archivos temporales
    os.rename(temp_train, train_bin)
    os.rename(temp_val, val_bin)
    print(f"¡Hecho! Total ≈ {total_tokens/1e9:.2f}B tokens")
    print(f"train.bin y val.bin listos (sin explosión de RAM)")

if __name__ == "__main__":
    txt_file = "train_fineweb.txt"
    process_file(txt_file, "train.bin", "val.bin")
```

Esto transmite directamente al disco, nunca mantiene más de un chunk en memoria.

#### Si realmente quieres el estilo de script original pero seguro
Añade monitorización de memoria y fragmenta la salida:

```python
# añade esto en lugar de una lista gigante
MAX_TOKENS_PER_SHARD = 500_000_000  # ~1 GB por fragmento

shard_idx = 0
all_tokens = []

for chunk in iter(lambda: f.read(chunk_size), ""):
    if not chunk:
        break
    tokens = enc.encode_ordinary(chunk)
    all_tokens.extend(tokens)

    if len(all_tokens) >= MAX_TOKENS_PER_SHARD:
        arr = np.array(all_tokens, dtype=np.uint16)
        arr.tofile(f"train_shard_{shard_idx:04d}.bin")
        print(f"Fragmento {shard_idx} guardado - {len(arr)/1e6:.1f}M tokens")
        all_tokens.clear()
        shard_idx += 1
```

Luego simplemente concatena los fragmentos: `cat train_shard_*.bin > train.bin`

### Comprobación rápida de qué tan grande es realmente tu archivo
Ejecuta esto en la terminal:

```bash
du -h train_fineweb.txt          # tamaño legible
wc -c train_fineweb.txt          # bytes
ls -lh train_fineweb.txt
```

El texto de FineWeb-10B es ~20–25 GB, 100B es ~200–250 GB, etc.

### Resumen
Tu script muere porque las listas de Python consumen 15–20× más RAM que el array numpy final. Con archivos grandes de FineWeb rápidamente superas los 50+ GB → swap → escritorio congelado.

Usa la versión de streaming anterior: funciona en archivos de texto de 1TB+ con <2 GB de RAM y termina en unas pocas horas en un solo núcleo de CPU.

Tu 4070 Ti es inocente aquí; está esperando datos que nunca llegan porque la RAM está muerta.