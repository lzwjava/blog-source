---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Extracción de Texto de Volcados de Wikipedia
translated: true
type: note
---

Aquí tienes las formas más comunes y efectivas de extraer texto plano de los archivos de volcado `.bz2` de Wikipedia como el tuyo (`enwiki-latest-pages-articles1.xml-p1p41242.bz2`).

### Herramientas y Métodos Recomendados (del más fácil al más eficiente)

#### 1. Usar wikiextractor (lo mejor para la mayoría – rápido y limpio)
Esta es la herramienta estándar que usa casi todo el mundo en NLP/ML para los volcados de Wikipedia.

```bash
# Instalar (una vez)
pip install wikiextractor

# Extraer texto (elimina plantillas, tablas, etc., da texto limpio por artículo)
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 --output wiki_text
```

- Salida: crea una carpeta `wiki_text/` con subcarpetas AA, AB, … que contienen archivos `.bz2` de JSON/texto limpio.
- Para obtener texto plano (un artículo por línea):
```bash
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 --processes 8 -o wiki_text --json
# Luego convertir JSON a texto plano si es necesario
find wiki_text -name '*' -exec cat {} \; | grep '"text":' | sed 's/.*"text": "//;s/"$//' > all_text.txt
```

#### 2. Usar WikiCorpus de gensim (excelente si estás haciendo NLP en Python)

```python
from gensim.corpora import WikiCorpus

# Esto maneja automáticamente .bz2 y extrae texto + tokeniza
wiki = WikiCorpus("enwiki-latest-pages-articles1.xml-p1p41242.bz2", dictionary=False)

# Iterar sobre los artículos
with open("output.txt", "w", encoding="utf-8") as f:
    for i, text in enumerate(wiki.get_texts()):
        f.write(" ".join(text) + "\n")
        if i % 10000 == 0:
            print(f"Procesados {i} artículos")
```

#### 3. bzip2 + grep/awk simple (rápido y sucio, sin limpieza)

```bash
# Solo descomprimir y ver el XML crudo
bzip2 -dc enwiki-latest-pages-articles1.xml-p1p41242.bz2 | less

# Extraer solo el contenido <text> (muy básico, conserva el markup de wiki)
bzip2 -dc enwiki-latest-pages-articles1.xml-p1p41242.bz2 | \
  sed -n '/<text /,/<\/text>/p' | \
  sed 's/<text[^>]*>//g;s/<\/text>//g' > raw_text_with_markup.txt
```

#### 4. Si tienes el volcado completo y lo quieres todo rápido (en paralelo)
Tu archivo es solo el primer fragmento (p1p41242), pero si luego tienes los ~30+ fragmentos:

```bash
# Extraer todo en paralelo
ls *.bz2 | xargs -P 8 -I {} wikiextractor {} --output wiki_extracted
```

### Resumen – Lo que te recomiendo ahora mismo:

```bash
pip install wikiextractor
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 -o extracted_wiki --bytes 1M --json
```

Esto te dará artículos limpios y legibles en unos minutos (tu archivo es de solo ~2-3 GB comprimido, así que muy manejable).

Dime si quieres:
- Solo el espacio de nombres principal (artículos reales, no páginas de discusión)
- Texto plano en lugar de JSON
- Salida tokenizada
- Wikipedia en chino en su lugar (zhwiki) – el proceso es idéntico

¡Feliz extracción! 🚀