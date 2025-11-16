---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Descarga de Wikipedia en Inglés
translated: true
type: note
---

Este es un listado de directorio de uno de los espejos de descarga oficiales de Wikimedia (normalmente https://dumps.wikimedia.org/enwiki/latest/).  
Contiene todas las diferentes formas en que puedes descargar los artículos actuales de Wikipedia en inglés (a principios de noviembre de 2025).

### Formatos principales y qué contienen realmente

| Patrón del nombre de archivo | Qué es | Tamaño aproximado (sin comprimir) | ¿Es mejor para entrenar LLMs? | Notas |
| --- | --- | --- | --- | --- |
| `enwiki-latest-pages-articles.xml.bz2` | Un único archivo gigante con **todos** los artículos + páginas de discusión, plantillas, redirecciones, etc. | ~85–90 GB sin comprimir | Sí, muy utilizado | El más fácil si tienes espacio y ancho de banda |
| `enwiki-latest-pages-articles1.xml-p1p41242.bz2`  … hasta … `enwiki-latest-pages-articles27.xml-…` | Los mismos datos, pero divididos en 27 fragmentos más pequeños (multistream) | Cada uno ~200–600 MB comprimidos → total aún ~85–90 GB sin comprimir | Sí, la opción más popular | Permite descargar en paralelo y reanudar fácilmente |
| `enwiki-latest-pages-articles-multistreamX.xml.bz2` (p.ej. multistream27) | Los archivos de datos comprimidos reales y enormes que pertenecen a la versión dividida anterior | 300–600 MB cada uno comprimidos | Estos son los archivos de datos reales que quieres | Necesitas estos + los archivos de índice |
| `enwiki-latest-pages-articles-multistreamX.xml.bz2.md5` / `.meta` | Archivos de suma de comprobación y metadatos pequeños | < 1 KB | No necesario para el texto | Solo para verificar las descargas |
| `enwiki-latest-pages-articles-multistream-indexX.xml.bz2` | Archivos de índice que indican qué artículo está en qué desplazamiento de byte en los archivos grandes de multistream | ~30–60 MB cada uno comprimidos | Requerido si usas multistream | Necesario para acceso aleatorio rápido; la mayoría de scripts de procesamiento los esperan |

### Recomendación: Lo que casi todo el mundo usa para entrenar modelos en 2025

La forma estándar de facto (utilizada por LLaMA, Mistral, Qwen, DeepSeek, Gemma, Phi, etc.) es:

Descargar los **27 archivos multistream + sus 27 archivos de índice**  
(es decir, todo lo que comienza con `enwiki-latest-pages-articlesXX.xml-p…p….bz2` y los coincidentes `…-indexXX…bz2`)

O incluso más simple: solo descarga el **único archivo gigante** si tu conexión y disco pueden manejarlo:

```
enwiki-latest-pages-articles.xml.bz2    ← 24.6 GB comprimido, ~85–90 GB sin comprimir
```

Ambos contienen exactamente los mismos datos XML en bruto (todos los artículos del espacio de nombres principal + muchas páginas extra).

### ¿Por qué no los archivos pequeños (multistream3.xml-p…, multistream4.xml-p… etc.)?
Esas son divisiones muy antiguas de 2010–2015 que solo contienen una pequeña fracción de Wikipedia (artículos que cayeron en ese rango de ID de página en aquel entonces). Se mantienen solo por razones históricas y básicamente son inútiles hoy en día.

### Comandos de inicio rápido (volcado de 2025)

Descarga paralela de los 27+27 archivos recomendados (la más rápida):

```bash
# Obtener la lista de archivos
wget -q https://dumps.wikimedia.org/enwiki/latest/ -O - | \
  grep -E 'enwiki-latest-pages-articles[0-9]+[02468]\.xml-p[0-9]+p[0-9]+\.bz2"' | \
  sed -e 's/.*href="//' -e 's/".*//' | \
  xargs -n1 -P10 wget https://dumps.wikimedia.org/enwiki/latest/

# También descargar los archivos de índice coincidentes
wget -q https://dumps.wikimedia.org/enwiki/latest/ -O - | \
  grep -E 'enwiki-latest-pages-articles-multistream-index' | \
  sed -e 's/.*href="//' -e 's/".*//' | \
  xargs -n1 -P10 wget https://dumps.wikimedia.org/enwiki/latest/
```

O simplemente el archivo único (lo más simple):

```bash
wget https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
```

Después de eso, normalmente lo procesas con herramientas como:
- wikiextractor (Python) → texto limpio
- el cargador de Wikipedia de Hugging Face `datasets` (ya hace todo por ti)
- los scripts de procesamiento de DeepSeek o EleutherAI, etc.

En resumen:  
Descarga el único archivo de 24 GB `enwiki-latest-pages-articles.xml.bz2` o los 27 archivos divididos + índices. Todo lo demás en esa lista son sumas de comprobación, basura antigua o metadatos que no necesitas para el entrenamiento.