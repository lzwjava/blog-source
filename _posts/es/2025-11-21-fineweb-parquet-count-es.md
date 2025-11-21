---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4.1-fast
title: Cantidad de Archivos Parquet del Conjunto de Datos FineWeb
translated: true
type: note
---

El conjunto de datos **FineWeb** (la versión en inglés de más de 15 billones de tokens en `HuggingFaceFW/fineweb`) contiene **aproximadamente entre 35.000 y 50.000** archivos `.parquet` en total.

### Desglose
- Consiste en **96** instantáneas de Common Crawl separadas (volcados, p. ej., `CC-MAIN-2013-20`, `CC-MAIN-2024-10`, etc.).
- Cada volcado se almacena en su propio subdirectorio bajo `/data/` y se divide en muchos archivos `.parquet` fragmentados con nombres como `000_00000.parquet`, `000_00001.parquet`, … (relleno con ceros, secuencial).
- El número de archivos parquet varía por volcado dependiendo de su tamaño:
  - Los volcados más pequeños/antiguos (como el ejemplo `CC-MAIN-2013-20` en tu script) a menudo tienen **~200–1.000** archivos.
  - Los volcados recientes más grandes pueden tener **varios miles** de archivos cada uno.
- No existe un total oficial único publicado, pero las estimaciones de la comunidad y los cálculos a partir de los tamaños de los volcados/recuentos de tokens sitúan consistentemente el **total general en torno a 35k–50k** archivos parquet en los 96 volcados (el conjunto de datos completo es de ~45–53 TB sin comprimir).

Tu script descarga los fragmentos del 11 al 20 (10 archivos) del volcado muy pequeño `CC-MAIN-2013-20`, que tiene muchos más que eso — muchos cientos de fragmentos en total solo para ese volcado.

Si quieres el recuento exacto, puedes calcularlo mediante programación con la API de Hugging Face Hub (p. ej., usando `huggingface_hub.list_repo_files`), pero los números aproximados anteriores son los que la gente suele usar al descargar o procesar el conjunto de datos completo.

[Ficha del conjunto de datos FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb)  
[Árbol de datos de FineWeb (volcado de ejemplo)](https://huggingface.co/datasets/HuggingFaceFW/fineweb/tree/main/data)