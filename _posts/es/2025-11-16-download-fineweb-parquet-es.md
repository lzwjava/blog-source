---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descarga de archivos Parquet específicos de FineWeb
translated: true
type: note
---

Solo quieres descargar y usar algunos archivos parquet de un volcado específico de Common Crawl (como CC-MAIN-2013-20) en lugar del monstruo completo de FineWeb de 15T de tokens — ¡totalmente razonable! Aquí están las formas más fáciles de hacerlo en 2025.

### Método 1: Descarga Directa con huggingface_hub (Recomendado, Más Rápido)
Esto descarga solo los archivos parquet que quieres a máxima velocidad (~GB/s si habilitas hf-transfer).

```bash
# 1. Instala/actualiza
pip install -U "huggingface_hub[hf_transfer]"

# 2. Habilita la descarga rápida (¡muy importante!)
export HF_HUB_ENABLE_HF_TRANSFER=1   # Linux/macOS
# o en Windows PowerShell:
# $env:HF_HUB_ENABLE_HF_TRANSFER = "1"

# 3. Descarga solo los archivos parquet que quieres
huggingface-cli download HuggingFaceFW/fineweb \
    data/CC-MAIN-2013-20/000_00000.parquet \
    data/CC-MAIN-2013-20/000_00001.parquet \
    data/CC-MAIN-2013-20/000_00002.parquet \
    --repo-type dataset --local-dir fineweb-2013-20
```

Eso es todo — ahora tienes tres archivos parquet de ~2.15 GB en la carpeta `fineweb-2013-20/`.

### Método 2: Script de Python de Una Línea para Descargar Archivos Específicos
```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="HuggingFaceFW/fineweb",
    repo_type="dataset",
    allow_patterns=[
        "data/CC-MAIN-2013-20/000_00000.parquet",
        "data/CC-MAIN-2013-20/000_00001.parquet",
        # añade más si quieres
    ],
    local_dir="fineweb-2013-20"
)
```

### Cómo Leer los Archivos Parquet Localmente
```python
import pandas as pd
# o usa pyarrow para mayor velocidad + menor uso de memoria
import pyarrow.parquet as pq
import pyarrow.dataset as ds

# La forma más rápida (transmite sin cargar todo en la RAM)
dataset = ds.dataset("fineweb-2013-20/data/CC-MAIN-2013-20/", format="parquet")

for batch in dataset.to_batches(batch_size=1024):
    df = batch.to_pandas()
    for text in df["text"]:
        # haz lo que quieras: tokenizar, filtrar, escribir a jsonl, etc.
        print(text[:200])  # ejemplo
```

O simplemente con pandas (aceptable para unos pocos archivos):
```python
df = pd.read_parquet("fineweb-2013-20/data/CC-MAIN-2013-20/000_00000.parquet")
print(df.columns)  # ['text', 'id', 'dump', 'url', 'date', 'file_path', 'language', 'language_score', 'token_count']
print(df.iloc[0]["text"])
```

### Estadísticas Rápidas para CC-MAIN-2013-20
- ~207 archivos parquet × ~2.15 GB ≈ 422 GB total
- ~44 mil millones de tokens (buen tamaño para experimentos pequeños o medianos)
- Ya limpiados, deduplicados y filtrados por Hugging Face

Eso es todo lo que necesitas. Solo elige la cantidad de archivos `_0000XX.parquet` que quieras (están mezclados aleatoriamente), descarga solo esos y comienza a entrenar o filtrar inmediatamente.