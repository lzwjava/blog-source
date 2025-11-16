---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Resumen del Conjunto de Datos de Common Crawl de Octubre de 2025
translated: true
type: note
---

Esta tabla es el resumen oficial del **rastreo de Common Crawl de octubre de 2025**, específicamente del conjunto de datos etiquetado **CC-MAIN-2025-43**. Common Crawl es un proyecto sin ánimo de lucro que rastrea toda la web pública cada mes o dos y publica los datos en bruto de forma gratuita para que investigadores, empresas y cualquier otra persona pueda utilizarlos (por ejemplo, para entrenar modelos de lenguaje extenso como GPT, LLaMA, Grok, etc.).

Aquí se explica qué significa cada parte de la tabla:

### Datos básicos
- **Nombre**: CC-MAIN-2025-43 → el 43.er rastreo semanal publicado en 2025, realizado aproximadamente en octubre de 2025.
- **Tamaño**: Se capturaron 2.610 millones de páginas web individuales.

### Los diferentes tipos de datos y lo que contienen

| Tipo de Datos          | Qué es                                                                                      | Tamaño total sin comprimir | N.º de archivos | Tamaño comprimido |
|------------------------|---------------------------------------------------------------------------------------------|----------------------------|-----------------|-------------------|
| **WARC**               | Los datos brutos y completos del rastreo (respuestas HTTP completas: cabeceras + HTML + recursos incrustados) | ~ cientos de TiB           | 100,000         | 97.73 TiB         |
| **WAT**                | Metadatos extraídos de los archivos WARC (p. ej., enlaces salientes, idioma, longitud del contenido, etc.) en formato JSON |                            | 100,000         | 18.39 TiB         |
| **WET**                | Solo el texto plano extraído (sin etiquetas HTML, sin texto repetitivo, solo texto limpio)  |                            | 100,000         | 7.38 TiB          |
| **Archivos Robots.txt**| Todos los archivos robots.txt que se obtuvieron durante el rastreo                          |                            | 100,000         | 0.15 TiB          |
| **Respuestas no 200**  | Respuestas que no fueron exitosas (404s, 500s, redirecciones, etc.)                         |                            | 100,000         | 3.07 TiB          |
| **Archivos de índice de URL** | Índice que permite buscar en qué archivo WARC se encuentra una URL específica (formato antiguo) |                            | 302             | 0.20 TiB          |
| **Índice de URL columnar** | Índice columnar más nuevo y rápido (formato Parquet) para herramientas de big-data como Spark, DuckDB, etc. |                            | 900             | 0.23 TiB          |

### Por qué existen los diferentes formatos
- Si solo quieres entrenar un modelo de lenguaje → normalmente descargas los archivos **WET** (texto ya limpiado, tamaño más pequeño).
- Si necesitas el HTML completo, imágenes, CSS, etc. → descargas los archivos **WARC** (los más grandes).
- Si necesitas metadatos (enlaces, idioma detectado, etc.) sin el HTML completo → **WAT**.
- Los índices te permiten encontrar páginas sin tener que escanear los 100,000 archivos.

### Cómo están organizados los archivos
Todo está dividido en 100, seguido por **segmentos** (aproximadamente 1 TiB comprimidos cada uno para WARC). Cada segmento contiene muchos archivos .warc.gz (o .wat.gz, .wet.gz) más pequeños. Los archivos *.paths.gz que ves en la lista son solo archivos de texto que contienen la lista completa de URL de S3 para cada tipo.

Puedes acceder a todo de forma gratuita en AWS S3 en:
`s3://commoncrawl/crawl-data/CC-MAIN-2025-43/`
(o vía HTTPS: https://data.commoncrawl.org/)

En resumen: Este es uno de los conjuntos de datos web abiertos más grandes del mundo (2.610 millones de páginas de octubre de 2025), disponible gratuitamente en diferentes formas procesadas, y la tabla simplemente te indica el tamaño de cada versión procesada y dónde encontrar las listas de archivos.