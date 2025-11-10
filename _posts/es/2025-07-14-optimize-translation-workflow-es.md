---
audio: false
generated: true
lang: es
layout: post
title: Optimización de Traducción con Hash de Párrafos
translated: true
type: note
---

### Reflexiones sobre la optimización de tu flujo de trabajo de traducción

Tu objetivo es claro: minimizar el uso de tokens de IA para traducir publicaciones de blog de Jekyll (escritas en Markdown) a 8 idiomas, volviendo a traducir solo los párrafos nuevos o modificados, mientras almacenas en caché los que no han cambiado. Quieres mantener Markdown para la edición, evitar bases de datos/JSON/YAML para el contenido principal y manejar elementos especiales como bloques de código (que no deben traducirse). Un enfoque basado en párrafos tiene sentido porque se alinea con cómo escribes y editas: las traducciones pueden ser más precisas contextualmente a ese nivel que a nivel de oraciones.

Desafíos clave:
- **Identificar cambios**: Sin diferencias de control de versiones, necesitas una forma de detectar lo que es nuevo/modificado/sin cambios. Aplicar hash a los párrafos (por ejemplo, usando SHA-256 en el texto en inglés normalizado) es eficiente y sin estado: no es necesario almacenar versiones antiguas completas.
- **Manejar la estructura de Markdown**: No puedes simplemente dividir en `\n\n` porque los bloques de código, encabezados, listas u otra sintaxis podrían romper las cosas. Un divisor simple basado en expresiones regulares podría funcionar para publicaciones básicas, pero un analizador ligero de Markdown es mejor para preservar la estructura y omitir partes no traducibles.
- **Almacenamiento en caché**: Mantenlo basado en archivos y simple (por ejemplo, un archivo JSON o un directorio de archivos) para evitar bases de datos. Almacena en caché por hash de párrafo, por idioma.
- **Ahorro de tokens**: Para publicaciones largas, esto podría reducir el uso entre un 80 y 90 % en ediciones menores, ya que solo los párrafos afectados llegan a la API de IA.
- **Casos extremos**: Párrafos agregados/eliminados (manejar aplicando hash nuevamente); ajustes menores (por ejemplo, correcciones de errores tipográficos) activarán la retraducción a menos que normalices los espacios en blanco/puntuación; los bloques de código o el código en línea deben excluirse; si los párrafos se reordenan, los hash no coincidirán, pero está bien si los tratas como "nuevos".
- **Integración**: Ejecuta esto como un script previo a la construcción en tu flujo de trabajo de Jekyll (por ejemplo, mediante un script de bash o un hook de Git). No hay necesidad de plugins de Jekyll si generas archivos Markdown traducidos por separado.

Esto es preferible a nivel de oración (menos contexto preciso para la IA) o de publicación completa (sin ahorros). YAML/JSON sería ciertamente engorroso para escribir ideas: mantente con Markdown.

### Mejor forma propuesta: Aplicación de hash a párrafos con almacenamiento en caché y análisis consciente de Markdown

Usa un script de Python para:
1. Analizar el Markdown en inglés en "unidades traducibles" (párrafos, excluyendo bloques de código, encabezados si se desea, etc.).
2. Aplicar hash al texto en inglés de cada unidad (normalizado, por ejemplo, eliminar espacios en blanco extra).
3. Verificar en un caché basado en archivos las traducciones existentes por hash/idioma.
4. Traducir las que faltan mediante tu herramienta de IA (por ejemplo, API de DeepSeek/Mistral).
5. Almacenar en caché las nuevas traducciones.
6. Reensamblar los archivos Markdown traducidos, preservando las partes no traducibles.

**Por qué esto es lo mejor**:
- **Simple y de baja sobrecarga**: Sin base de datos, solo archivos. Se ejecuta localmente/sin conexión excepto por las llamadas a la IA.
- **Flexible**: Maneja bloques de código omitiéndolos. Extensible a otros elementos de Markdown (por ejemplo, no traducir encabezados si son cortos).
- **Rentable**: Solo paga por párrafos nuevos o modificados. Para una publicación de 10 párrafos, editar uno ahorra ~90 % de tokens.
- **Mantenible**: Edita el Markdown en inglés de forma natural; el script maneja el resto.
- **Herramientas necesarias**: Python (probablemente lo tienes). Bibliotecas: `hashlib` (integrada para hash), `markdown` o `mistune` para análisis (si es necesario; comienza de forma simple con expresiones regulares para tu caso de "sin sintaxis especial").

#### Implementación paso a paso

1. **Configuración**:
   - Crea un archivo `translations_cache.json` (o un directorio como `cache/` con archivos hash.json para escalabilidad).
   - Estructura: `{ "hash1": { "fr": "texto traducido", "es": "...", ... }, "hash2": { ... } }`
   - Almacena esto en tu repositorio de blog (ignorar en git si es confidencial) o en un directorio separado.
   - Enumera tus 8 idiomas en el script (por ejemplo, ['fr', 'es', 'de', ...]).

2. **Análisis de Markdown**:
   - Para casos simples (párrafos + bloques de código): Usa procesamiento línea por línea para detectar bloques de código delimitados (``````` o `~~~`) y código con sangría (>3 espacios).
   - Recopila "párrafos" como bloques de líneas consecutivas que no son código y no están en blanco.
   - Mejor: Usa la biblioteca `markdown` de Python para convertir a HTML, luego extrae el texto, pero eso es con pérdida para el reensamblaje. En su lugar, usa `mistune` (un analizador rápido de Markdown) para obtener un AST (árbol de sintaxis abstracta), que te permite recorrer y modificar nodos traducibles (por ejemplo, nodos de 'párrafo').
   - Instala `mistune` si es necesario (pero tu entorno tiene lo básico; asume que puedes pip localmente).

3. **Aplicación de hash**:
   - Normalizar: `text.strip().lower()` o solo `.strip()` para ignorar cambios de espacios en blanco si se desea (pero eso podría pasar por alto ediciones intencionales).
   - Hash: `hashlib.sha256(normalized.encode()).hexdigest()`

4. **Traducción**:
   - Usa tu envoltorio de API de IA (por ejemplo, para DeepSeek: envía un mensaje como "Traduce este párrafo al francés: {text}").
   - Procesa por lotes si es posible, pero como los párrafos son pequeños, secuencial está bien.

5. **Reensamblaje**:
   - Reconstruye el Markdown reemplazando los bloques traducibles con traducciones nuevas/en caché, manteniendo intactos el código/encabezados.

6. **Ejecución del script**:
   - Ejecutar: `python translate_blog.py ruta/al/ingles.md`
   - Salidas: `ruta/al/fr.md`, `ruta/al/es.md`, etc.
   - Para Jekyll: Colócalos en `_posts/` con prefijos de idioma, o usa un plugin multilingüe como `jekyll-polyglot` para manejar.

#### Script de Python de ejemplo

Aquí hay una versión básica que usa análisis línea por línea (sin bibliotecas externas más allá de las integradas). Asume Markdown simple: párrafos separados por líneas en blanco, bloques de código delimitados. Actualiza a `mistune` para sintaxis compleja.

```python
import hashlib
import json
import os
import sys
# Asume que tienes una función de traducción por IA; reemplaza con tu llamada a la API de DeepSeek/Mistral
def ai_translate(text, lang):
    # Marcador de posición: devuelve el resultado de la llamada a la API
    return f"Translated to {lang}: {text}"  # Reemplazar con API real

CACHE_FILE = 'translations_cache.json'
LANGUAGES = ['fr', 'es', 'de', 'it', 'pt', 'zh', 'ja', 'ko']  # Tus 8 idiomas

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=4)

def compute_hash(text):
    normalized = text.strip()  # Personalizar la normalización
    return hashlib.sha256(normalized.encode('utf-8')).hexdigest()

def parse_markdown(md_text):
    lines = md_text.splitlines()
    blocks = []
    current_block = []
    in_code = False
    for line in lines:
        if line.strip().startswith('```') or line.strip().startswith('~~~'):
            in_code = not in_code
            if current_block:
                blocks.append(('text', '\n'.join(current_block)))
                current_block = []
            blocks.append(('code', line))
            continue
        if in_code:
            blocks.append(('code', line))
        else:
            if line.strip():  # No en blanco
                current_block.append(line)
            else:
                if current_block:
                    blocks.append(('text', '\n'.join(current_block)))
                    current_block = []
    if current_block:
        blocks.append(('text', '\n'.join(current_block)))
    return blocks

def translate_post(english_md_path):
    with open(english_md_path, 'r') as f:
        md_text = f.read()
    
    blocks = parse_markdown(md_text)
    cache = load_cache()
    
    for lang in LANGUAGES:
        translated_blocks = []
        for block_type, content in blocks:
            if block_type == 'code':
                translated_blocks.append(content)
            else:  # text
                h = compute_hash(content)
                if h not in cache:
                    cache[h] = {}
                if lang not in cache[h]:
                    translation = ai_translate(content, lang)
                    cache[h][lang] = translation
                translated_blocks.append(cache[h][lang])
        
        # Reensamblar con saltos de línea
        translated_md = '\n\n'.join(translated_blocks)  # Ajustar para formato Markdown
        output_path = english_md_path.replace('.md', f'_{lang}.md')
        with open(output_path, 'w') as f:
            f.write(translated_md)
    
    save_cache(cache)
    print("Translations updated.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py path/to/english.md")
    else:
        translate_post(sys.argv[1])
```

**Cómo usar**:
- Reemplaza `ai_translate` con tu lógica de API.
- Ejecuta en tu archivo de publicación después de las ediciones.
- Para encabezados/listas: Extiende `parse_markdown` para detectar (por ejemplo, líneas que comienzan con `#` o `-` como bloques separados).
- Si las publicaciones tienen imágenes/enlaces: permanecen sin cambios ya que están en bloques de texto.
- Consejo de normalización: Si quieres ignorar cambios menores de puntuación, usa expresiones regulares para eliminarlos antes de aplicar el hash.

#### Mejoras
- **Integración con Git**: Usa `git diff` para pre-identificar líneas cambiadas, pero aplicar hash es más simple.
- **Traducción por lotes**: Si la API lo admite, envía múltiples párrafos nuevos a la vez.
- **Manejo de errores**: Reintentar llamadas fallidas a la API; validar traducciones.
- **Análisis avanzado**: Pip `mistune` y usa su renderizador para personalizar (por ejemplo, omitir nodos 'code_block').
- **Pruebas**: Las colisiones de hash son raras con SHA-256; prueba en publicaciones de muestra.

Esto debería ahorrarte tokens sin complicar tu flujo de trabajo. Si tu Markdown es más complejo, comienza con esto e itera. ¡Avísame si necesitas ajustes o ayuda con la integración de la API!