---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4.1-fast
title: Resumen del Conjunto de Datos FineWeb 2013
translated: true
type: note
---

**CC-MAIN-2013-20** (volcado de verano de 2013) en el conjunto de datos FineWeb:

- **Número de archivos .parquet**: Aproximadamente **460–500**  
  (Los archivos están fragmentados con tamaños variables: muchos de ~1 GB, algunos más grandes de hasta ~2 GB. El directorio totaliza **422 GB**, por lo que 422 ÷ ~0.9 GB de promedio ≈ 460–480 fragmentos. La nomenclatura es secuencial `000_00000.parquet` hasta aproximadamente `000_004xx.parquet`.)

- **Tamaño total de todos los archivos parquet**: **422 GB**

- **Tokens cuando se codifican con un tokenizador estilo GPT** (cl100k_base usado para GPT-4, o el tokenizador más antiguo de GPT-2 usado en los informes de FineWeb):  
  **144.5 mil millones de tokens** (después de la canalización de limpieza, filtrado y deduplicación de FineWeb)

Nota: El volcado original sin procesar de Common Crawl era mucho más grande (~393 mil millones de tokens antes del filtrado), pero FineWeb conserva solo el texto en inglés de alta calidad, por lo que este antiguo volcado de 2013 se reduce tan drásticamente.

Si descargas el directorio completo (por ejemplo, mediante `huggingface-cli download` o un script que recorra todos los fragmentos), obtendrás ~422 GB de archivos parquet que contienen 144.5B de tokens listos para el entrenamiento.

[Ficha del conjunto de datos FineWeb (incluye tabla de tokens por volcado)](https://huggingface.co/datasets/HuggingFaceFW/fineweb)  
[Directorio CC-MAIN-2013-20 en HF (muestra el tamaño total)](https://huggingface.co/datasets/HuggingFaceFW/fineweb/tree/main/data/CC-MAIN-2013-20)