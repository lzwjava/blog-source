---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descarga y Preparación de Datos de FineWeb
translated: true
type: note
---

### Descargar el archivo Parquet

La URL que proporcionaste apunta a un archivo Parquet específico del conjunto de datos FineWeb (un subconjunto limpiado de datos de CommonCrawl). Este archivo (`000_00000.parquet` del dump `CC-MAIN-2013-20`) contiene aproximadamente 1 millón de filas de texto web en inglés, donde cada fila incluye una columna `text` que ya está preprocesada para el entrenamiento de modelos de lenguaje (HTML eliminado, desduplicado, filtrado por calidad mediante herramientas como Trafilatura).

Para descargarlo:
- Usa la CLI de Hugging Face: `huggingface-cli download HuggingFaceFW/fineweb data/CC-MAIN-2013-20/000_00000.parquet --local-dir ./fineweb_data`
- O mediante Python con `huggingface_hub`:
  ```python
  from huggingface_hub import hf_hub_download

  file_path = hf_hub_download(
      repo_id="HuggingFaceFW/fineweb",
      filename="data/CC-MAIN-2013-20/000_00000.parquet",
      local_dir="./fineweb_data"
  )
  print(f"Descargado en: {file_path}")
  ```
Esto guarda el archivo de ~500MB localmente (ej., `./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet`).

Para el dump completo (cientos de archivos), usa `snapshot_download` como se muestra en la documentación del dataset, pero comienza con este archivo único para pruebas.

### Extraer el texto

La columna `text` de FineWeb es texto plano listo para entrenar—no es necesario analizar HTML o HTML crudo. Usa `pandas` o `pyarrow` para cargarlo eficientemente. Así es cómo:

1. **Instalar Dependencias** (si es necesario): `pip install pandas pyarrow datasets` (asumiendo que ya las tienes para la configuración de NanoGPT).

2. **Cargar el Archivo Parquet y Extraer el Texto**:
   ```python
   import pandas as pd
   import os

   # Ruta a tu archivo descargado
   parquet_path = "./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet"

   # Cargar el archivo Parquet (eficiente para archivos grandes)
   df = pd.read_parquet(parquet_path, columns=['text'])  # Cargar solo la columna de texto para ahorrar memoria

   # Extraer todo el texto en una lista (o iterar si la memoria es limitada)
   texts = df['text'].tolist()  # Lista de ~1M cadenas de texto

   # Opcional: Limpieza básica (FineWeb ya está limpio, pero normalizar espacios en blanco)
   import re
   def clean_text(text):
       if pd.isna(text):  # Saltar nulos (raro en FineWeb)
           return ''
       text = re.sub(r'\s+', ' ', text.strip())  # Colapsar espacios en blanco
       return text if len(text) > 10 else ''  # Filtrar textos muy cortos

   cleaned_texts = [clean_text(t) for t in texts if t]  # Aplicar filtro

   print(f"Se extrajeron {len(cleaned_texts)} muestras de texto")
   print("Muestra:", cleaned_texts[0][:200] + "...")  # Vista previa del primer texto
   ```

   - **Consejo de Memoria**: Este archivo tiene ~1M de filas, cada texto ~1-5k caracteres. En una máquina con 16GB de RAM, se carga bien. Para dumps más grandes, usa `pyarrow` para lectura por fragmentos:
     ```python
     import pyarrow.parquet as pq

     table = pq.read_table(parquet_path, columns=['text'])
     texts = table['text'].to_pylist()
     ```

   - **Alternativa con Streaming** (sin necesidad de descarga completa): Usa la librería `datasets` para iterar sin cargar todo:
     ```python
     from datasets import load_dataset

     # Cargar dump específico en modo streaming
     dataset = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)

     texts = []
     for i, sample in enumerate(dataset):
         if i >= 100000:  # Límite para pruebas
             break
         texts.append(sample['text'])

     # Limpiar como arriba
     ```

### Preparación para el Entrenamiento con NanoGPT

NanoGPT espera un único archivo de texto (ej., `input.txt`) con documentos concatenados separados por un token especial (como `"<|endoftext|>"`). Así es cómo formatear el texto extraído:

```python
# Después de extraer cleaned_texts desde arriba
with open('input.txt', 'w', encoding='utf-8') as f:
    for text in cleaned_texts:
        f.write(text + "\n<|endoftext|>\n")  # Separador por defecto de NanoGPT

print("¡Guardado en input.txt – listo para NanoGPT!")
```

- **¿Por Qué Este Formato?** El script `data.py` de NanoGPT leerá `input.txt`, lo codificará con tu tokenizador (ej., GPT-2) y creará divisiones de entrenamiento/validación. Cada documento termina con `"<|endoftext|>"` para evitar contaminación de contexto entre documentos.
- **Personalización**:
  - Filtrar por longitud: Añade `if 100 < len(text.split()) < 10000:` antes de escribir para mantener documentos de tamaño medio.
  - Subconjunto para Pruebas: Usa `cleaned_texts[:10000]` para una ejecución rápida de 10k muestras.
  - Comando de Entrenamiento: Una vez que `input.txt` esté listo, ejecuta `python train.py` en NanoGPT (ajusta `--dataset=input.txt` si es necesario).

Este único archivo da ~5-10B tokens—excelente para fine-tuning. Para más, descarga archivos Parquet adicionales y concaténalos. Si tienes problemas de memoria o necesitas ayuda con la configuración de NanoGPT, ¡comparte los detalles!

**Referencia**: [Ficha del Conjunto de Datos FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb)