---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Corrección del Error de Expresiones Regulares en Python 3.13
translated: true
type: note
---

El error que estás viendo es causado por **Python 3.13**, que es más estricto con la sintaxis de expresiones regulares que las versiones anteriores.

Específicamente, esta línea en `wikiextractor/extract.py` (alrededor de la línea 378) ahora no es válida en Python 3.13:

```python
ExtLinkBracketedRegex = re.compile(
    '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
    re.S | re.U)
```

El problema es el flag en línea `(?i)` colocado en medio de la cadena después de la concatenación de cadenas. A partir de Python 3.12/3.13, **los flags en línea como `(?i)` ya no están permitidos en ningún lugar excepto al principio mismo del patrón de la expresión regular**.

### Solución Rápida (funciona en Python 3.13)

Edita el archivo:

```bash
~/.local/lib/python3.13/site-packages/wikiextractor/extract.py
```

Ve a la línea ~378 y reemplaza el bloque dañado con esta versión corregida:

```python
# Antigua forma dañada (falla en Python 3.13)
# ExtLinkBracketedRegex = re.compile(
#     '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
#     re.S | re.U)

# Versión corregida – mover el flag de insensibilidad a mayúsculas/minúsculas a los flags de re.compile
protocol_pattern = '|'.join(wgUrlProtocols)
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + protocol_pattern + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.IGNORECASE | re.DOTALL | re.UNICODE
)
```

O incluso más limpio (recomendado):

```python
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + '|'.join(wgUrlProtocols) + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.I | re.S | re.U
)
```

`re.I` es lo mismo que `re.IGNORECASE`, y se puede pasar como un flag en lugar de incrustar `(?i)` dentro del patrón.

### Soluciones alternativas

1. Usa Python 3.11 o 3.12 (más fácil si no quieres aplicar un parche)
   ```bash
   python3.11 -m pip install wikiextractor
   # luego ejecuta con python3.11 wikiextractor ...
   ```

2. Usa el fork mantenido que ya corrige la compatibilidad con Python 3.13:
   ```bash
   pip uninstall wikiextractor
   pip install git+https://github.com/attardi/wikiextractor.git
   ```

   El fork de Giuseppe Attardi ha sido actualizado para Python 3.12+ y funciona perfectamente en 3.13.

3. Usa la alternativa moderna y muy rápida (altamente recomendada para volcados grandes):
   ```bash
   pip install wikiextractor-ng   # o "wiki-dump-tools", "wikitextprocessor", etc.
   ```

Después de aplicar el parche o cambiar al fork corregido, tu comando funcionará nuevamente:

```bash
wikiextractor *.bz2
```

Déjame saber si quieres un parche de una sola línea o el comando `sed` exacto para corregirlo automáticamente.