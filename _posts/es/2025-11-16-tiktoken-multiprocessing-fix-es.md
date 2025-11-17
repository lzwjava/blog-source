---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Corrección del Error de Pickle en Multiprocesamiento de Tiktoken
translated: true
type: note
---

Tu error es muy común al usar `datasets.map(..., num_proc>1)` con un tokenizador personalizado (como el codificador Tiktoken usado en el script de nanoGPT para FineWeb) — el tokenizador carga el archivo BPE (`cl100k_base.tiktoken` o similar) y este manejador de archivo **no se puede serializar (pickle)** cuando se envía a subprocesos en Linux (multiprocesamiento basado en fork).

Los procesos hijos fallan inmediatamente → "Uno de los subprocesos ha terminado abruptamente".

### Solución Rápida (funciona el 99% del tiempo)

Edita `data/fineweb/prepare.py` y fuerza que la tokenización se ejecute **solo en el proceso principal**:

```python
# Alrededor de la línea 80-85, encuentra la llamada .map() y cambia num_proc=8 → num_proc=1

tokenized = raw_datasets.map(
    tokenize,
    num_proc=1,               # ← cambia esta línea (o simplemente elimina el argumento)
    desc="tokenizando los splits",
)
```

Será más lento (un solo núcleo), pero funcionará de forma confiable. En FineWeb-10B esto toma ~30-60 minutos dependiendo de tu CPU/disco.

### Mejor Solución (mantén el multiprocesamiento, sigue siendo rápido)

Haz que el tokenizador se cargue de forma diferida dentro del proceso worker en lugar de en el ámbito global.

Reemplaza la creación actual del tokenizador (alrededor de la línea 40-50) con este patrón:

```python
import tiktoken

# Elimina el encoder global = tiktoken.get_encoding("cl100k_base")

def get_encoder():
    """Carga el tokenizador de forma diferida en cada subproceso"""
    return tiktoken.get_encoding("cl100k_base")

def tokenize(example):
    enc = get_encoder()                                   # ← cargado por proceso
    ids = enc.encode_ordinary(example["text"])
    ids.append(enc.eot_token)  # o lo que sea que haga el script
    return {"ids": ids, "len": len(ids)}
```

Luego mantén `num_proc=8` (o cualquier número). De esta manera, cada worker carga su propia copia del archivo .tiktoken después del fork → no hay problemas de serialización.

### Alternativa Incluso Más Rápida (recomendada para ejecuciones repetidas)

Descarga previamente los fragmentos (shards) de FineWeb-Edu 10B/100B desde Hugging Face y usa el script actualizado de Karpathy que funciona directamente en los archivos parquet/arrow en lugar del archivo .txt gigante:

```bash
# Mucho más rápido y evita este error por completo
python data/fineweb/prepare_fineweb.py --version 10B
# o 100B
```

El nuevo script (añadido ~2024) usa el dataset oficial de HF y es seguro para multiprocesamiento.

### Resumen

| Solución                          | Velocidad | Complejidad | Recomendación |
|-----------------------------------|-----------|------------|----------------|
| `num_proc=1`                      | Lenta     | 1 línea    | Solución rápida |
| Encoder diferido dentro de tokenize() | Rápida | edición pequeña | Mejor para .txt |
| Usar nuevo script prepare_fineweb.py | Más Rápida | nuevo comando | Recomendado |

Elige una y superarás este error inmediatamente. ¡Dime qué ruta tomas y te daré el parche exacto si es necesario!