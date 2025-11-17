---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Estructura de las diferencias de los archivos de volcado de Wikipedia
translated: true
type: note
---

La diferencia clave es cómo se divide el texto completo del artículo de Wikipedia en múltiples archivos — específicamente, si un archivo `.xml.bz2` contiene solo un flujo de revisiones (no multistream) o muchos flujos comprimidos agrupados juntos (multistream).

### 1. Volcados no multistream (estilo antiguo, o los archivos predeterminados "pages-articles")
Ejemplo de nombre de archivo:  
`enwiki-20251101-pages-articles1.xml-p1p41242.bz2`

- Cada archivo `.xml.bz2` contiene una porción de las páginas (ej., páginas 1–41242) en orden de ID de página.
- Dentro del archivo hay exactamente una secuencia continua `<page> … <page> …`.
- Todas las revisiones de una sola página están juntas dentro de esa única etiqueta de página (la revisión más reciente + las más antiguas si solicitaste "actual + historial").
- Para extraer un solo artículo, simplemente descomprimes y analizas el gran XML normalmente con cualquier herramienta XML/BZ2.
- `wget -c` funciona perfectamente de manera simple: reanuda exactamente donde se detuvo porque el archivo es un único flujo bzip2.

### 2. Volcados multistream (los archivos que contienen "multistream" en el nombre)
Ejemplo de nombre de archivo (el que enlazaste):  
`enwiki-20251101-pages-articles-multistream1.xml-p1p41242.bz2`

- Se cubre el mismo rango de páginas (p1p41242), pero el texto completo de cada revisión ya no se almacena dentro del archivo XML principal.
- En su lugar:
  - El archivo XML principal solo contiene metadatos (título, id, restricciones, marca de tiempo de la última revisión, etc.) y un puntero (desplazamiento de bytes + longitud) a donde reside el texto real de la revisión.
  - Los textos reales de las revisiones se almacenan por separado en muchos pequeños flujos comprimidos dentro del mismo archivo `.bz2` (de ahí "multistream").
- Normalmente hay un archivo complementario `...-multistream-index1.txt.bz2` que contiene los desplazamientos de bytes exactos para cada página/revisión, para que las herramientas puedan saltar directamente al flujo comprimido correcto y extraer solo ese texto sin descomprimir todo el archivo de 10–30 GB.

### ¿Por qué es importante esto para `wget -c`?

En la práctica, ambos comandos:

```bash
wget -c https://.../enwiki-20251101-pages-articles1.xml-p1p41242.bz2
wget -c https://.../enwiki-20251101-pages-articles-multistream1.xml-p1p41242.bz2
```

se comportan exactamente igual desde el punto de vista de wget: ambos son archivos bzip2 normales, por lo que la descarga reanudable con `-c` funciona perfectamente en ambos casos.

La diferencia solo aparece cuando comienzas a procesar el archivo descargado.

### Tabla Resumen

| Característica                       | No multistream (regular)                       | Multistream                                      |
|--------------------------------------|------------------------------------------------|--------------------------------------------------|
| El nombre de archivo contiene        | `-pages-articlesN.xml-...bz2`                 | `-pages-articles-multistreamN.xml-...bz2`       |
| Ubicación del texto del artículo     | Dentro del XML `<page><revision><text>...</text></revision></page>` | Fuera del XML, en flujos comprimidos separados |
| Tamaño del archivo (para el mismo rango de páginas) | Mucho más grande (a menudo 2–3×)              | Mucho más pequeño                               |
| Acceso aleatorio / extracción de una sola página | Muy lento (debe descomprimir todo el archivo) | Muy rápido (con el archivo de índice)           |
| Herramientas que lo entienden directamente | Cualquier analizador XML (SAX, xmltodict, etc.) | Herramientas de dump-generator de wikimedia, pywiki, mwxml, etc. |
| ¿Necesita archivo de índice complementario? | No                                             | Sí (`-multistream-index....txt.bz2`)            |
| Capacidad de reanudación con `wget -c` | Perfecta                                       | Perfecta (sigue siendo un archivo bzip2)        |

### Entonces, ¿cuál deberías descargar?

- Si solo quieres hacer un pase secuencial completo una vez (ej. entrenar un modelo de lenguaje), los archivos no multistream son más simples.
- Si alguna vez quieres buscar páginas individuales rápidamente, o te importa el espacio en disco y la velocidad de extracción, siempre prefiere el par multistream + índice. Casi todas las herramientas serias de procesamiento de Wikimedia (WikiExtractor, WikiCorpus de gensim, scripts de jawiki, etc.) esperan o recomiendan encarecidamente la versión multistream hoy en día.

Ambos archivos puedes reanudarlos con `wget -c` sin ningún problema; la parte "multistream" solo cambia lo que hay dentro del archivo, no cómo HTTP/wget lo ve.