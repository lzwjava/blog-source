---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Conjuntos de Datos OpenWebText y Wikipedia en Torrent
translated: true
type: note
---

### Torrents del Conjunto de Datos OpenWebText

OpenWebText es una réplica de código abierto del conjunto de datos WebText de OpenAI, que consiste en ~38 GB de texto limpio extraído de enlaces de Reddit de alto karma (principalmente páginas web raspadas y filtradas por calidad). Es un corpus de texto a gran escala popular para entrenar modelos de lenguaje. Si bien el texto completo raspado no siempre está disponible directamente como un único torrent, aquí hay opciones confiables:

- **Lista de URLs (Filtrada, ~480MB)**: Una lista pre-filtrada de ~26 millones de URLs utilizadas para raspar OpenWebText. Puedes usar esto para descargar y procesar el texto tú mismo.
  - Torrent: [OpenWebText-urls-26M-filtered.xz](https://academictorrents.com/details/f5161721b322bca66ed74da32b963c1066e64312)
  - Fuente: Academic Torrents (sembrado por la comunidad).

- **Lista de URLs (Completa, ~1.75GB)**: Las URLs completas sin duplicar de las publicaciones de Reddit.
  - Torrent: [WebText dataset urls.txt.tar.gz](https://academictorrents.com/details/15f3494b2991e75194d3af72bf7afa5025a7abc3)
  - Fuente: Academic Torrents (sembrado por la comunidad).

- **Versión Tokenizada (~16GB)**: Archivos de texto tokenizados con GPT-2 del corpus raspado (395 archivos, listos para el entrenamiento de modelos).
  - Torrent: [OpenWebText (Gokaslan's distribution, 2019), GPT-2 Tokenized](https://academictorrents.com/details/36c39b25657ce1639ccec0a91cf242b42e1f01db)
  - Fuente: Academic Torrents (sembrado por OSUOSL y la comunidad).

Para el corpus de texto crudo completo, consulta el sitio oficial para descargas directas (no basadas en torrents) o usa las URLs anteriores con scripts de scraping del [repositorio de OpenWebText en GitHub](https://github.com/eukaryote31/openwebtext). Una versión mejorada, OpenWebText2 (~escala de múltiples TB), está disponible a través del [repositorio de EleutherAI](https://github.com/EleutherAI/openwebtext2) pero utiliza streaming en lugar de torrents.

### Torrents de Volcados de Wikipedia

Los volcados de Wikipedia son exportaciones mensuales en XML de toda la base de datos (artículos, revisiones, metadatos). La versión en inglés es masiva (~20-25 GB comprimidos para resúmenes, hasta 100+ GB para el historial completo). Los torrents son mantenidos por la comunidad (no oficiales pero verificados contra checksums oficiales) y sembrados desde los servidores de Wikimedia para confiabilidad. Siempre verifica las descargas contra los hashes de [dumps.wikimedia.org](https://dumps.wikimedia.org/enwiki/latest/).

El centro principal para torrents es la [página Meta-Wiki Data Dump Torrents](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki), que enumera los últimos volcados de Wikipedia en inglés (por ejemplo, enwiki-20251101). Aquí hay un resumen de los recientes:

| Fecha del Volcado | Tipo de Archivo | Tamaño Comprimido | Enlace del Torrent | Notas |
|-----------|-----------|-----------------|--------------|-------|
| 2025-11-01 | Pages-Articles (XML, solo resúmenes) | ~22GB | [enwiki-20251101-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | Formato multistream; más fácil para extracción de texto. |
| 2025-11-01 | Pages-Articles-History (XML, revisiones completas) | ~120GB | [enwiki-20251101-pages-meta-history*.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | Incluye todas las ediciones; dividido en streams para un manejo más fácil. |
| 2025-10-01 | Pages-Articles (XML, solo resúmenes) | ~21GB | [enwiki-20251001-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | Mensual anterior; bueno para comparación histórica. |

- **Colección Completa**: Navega por todos los torrents históricos de Wikipedia en inglés en la [Colección Wikipedia de Academic Torrents](https://academictorrents.com/collection/wikipedia) (incluye volcados antiguos hasta ~2010).
- **Formato Kiwix ZIM**: Si quieres una Wikipedia navegable sin conexión (HTML, ~100 GB), prueba [wikipedia_en_all_maxi_2024-01.zim.torrent](https://download.kiwix.org/zim/wikipedia/wikipedia_en_all_maxi_2024-01.zim.torrent) – sembrado por la comunidad, pero busca actualizaciones de 2025 en [descargas de Kiwix](https://download.kiwix.org/zim/wikipedia/).

Para procesar estos volcados en texto plano, usa herramientas como `wikiextractor` de Python. Los torrents reducen la carga del servidor y reanudan descargas interrumpidas – usa un cliente como qBittorrent. Si necesitas volcados para otros idiomas o subconjuntos, la página Meta-Wiki tiene filtros.