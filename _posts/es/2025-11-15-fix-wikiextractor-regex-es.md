---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Corregir Error de Expresión Regular de wikiextractor en Python 3.13
translated: true
type: note
---

El error que estás experimentando se debe a un problema de compatibilidad en el paquete `wikiextractor` con el manejo más estricto de los flags en línea de expresiones regulares en Python 3.13. Específicamente, el flag `(?i)` en el patrón de regex está siendo interpretado como un flag global, pero no está posicionado al principio mismo de la expresión, lo que genera el `re.PatternError`.

Para solucionarlo, edita el archivo `/home/lzw/.local/lib/python3.13/site-packages/wikiextractor/extract.py` y modifica la línea 378 (o la definición cercana de `ExtLinkBracketedRegex`) de la siguiente manera:

- Original: `'\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',`
- Actualizado: `'\\[(((?i:' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',`

Esto añade un `:` después de `(?i`, cambiándolo a un flag en línea local `(?i:...)` que aplica solo al grupo de coincidencia de protocolo, lo cual resuelve el error de análisis.

Adicionalmente, las advertencias `SyntaxWarning: invalid escape sequence '\\['` provienen de cadenas no raw que contienen escapes que Python 3.13 trata de manera más estricta (aunque no causan el fallo principal). Puedes ignorarlas por ahora, o actualizar esas cadenas a cadenas raw (por ejemplo, `r'\\['`) en el mismo archivo si te molestan.

Después de editar, vuelve a ejecutar `wikiextractor *.bz2`. Si el paquete está desactualizado, considera buscar actualizaciones mediante `pip install --upgrade wikiextractor` o usar un entorno virtual con una versión anterior de Python (por ejemplo, 3.10) como solución alternativa.