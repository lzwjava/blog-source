---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Cazando el byte malicioso
translated: true
type: note
---

### Por qué esto no encontró el byte malo
El resultado de `hexdump` que obtuviste coincidió con **el desplazamiento del archivo** (`000008d0`), no con un byte `\x8D` en el contenido real. Grep está buscando texto en toda la línea, y "8d" aparece en la dirección hexadecimal (ej. `08d0`), por lo que capturó esa línea irrelevante. Los bytes de datos allí (`6f 67 20 ...`) son solo ASCII normal para `"og = og_images[i"`, sin problemas.

### Mejores formas de buscar el `\x8D`
Prueba estos comandos en tu directorio del proyecto (junto a `_layouts/default.html`). Escanearán los bytes del archivo directamente.

1. **Hexdump Mejorado (Buscar Byte en los Datos)**:
   Esto busca ` 8d ` (con espacios alrededor para que coincida con bytes hexadecimales, no con desplazamientos):
   ```
   hexdump -C _layouts/default.html | grep ' 8d '
   ```
   - Si encuentra algo, verás el desplazamiento (columna izquierda) y los bytes circundantes. Anota el desplazamiento, luego salta a esa posición en tu editor (ej. VS Code: Ctrl+G > desplazamiento de byte / 16 para la línea aprox.).
   - Ejemplo de salida si hay coincidencia: `00001234  ...  8d  20  61  62  ... |... ab...|`

2. **Usar `xxd` (A menudo mejor que Hexdump)**:
   macOS tiene `xxd` incorporado:
   ```
   xxd _layouts/default.html | grep 8d
   ```
   - Similar: Coincide con "8d" en bytes hexadecimales. Si no hay salida, el byte no está allí (raro, pero posible si está en otro archivo).

3. **Búsqueda Binaria con Grep (Búsqueda Directa de Byte)**:
   ```
   grep -a -o -P '\x8d' _layouts/default.html | hexdump -C
   ```
   - Esto extrae coincidencias exactas con el byte y las vuelca en hexadecimal. Si está vacío, no hay `\x8D`.

4. **One-Liner en Ruby (Posición Precisa)**:
   Como sugerí antes—ejecuta esto para obtener el índice del byte:
   ```
   ruby -e "File.open('_layouts/default.html', 'rb') { |f| f.read.each_byte.with_index { |b, i| puts \"Found at byte #{i}: #{b.chr(Encoding::ASCII_8BIT).inspect}\" if b == 0x8D } }"
   ```
   - Salida como: `Found at byte 1234: "\x8D"`. Luego edita: Abre el archivo, ve al carácter ~1234 (o línea = 1234/80 aprox.), y borra el carácter invisible (puede parecer nada; selecciona/borra a su alrededor).

### ¿Si no hay coincidencias?
- El `\x8D` podría estar en un **archivo diferente** (ej., una publicación en `_posts/` renderizada via `{{ content }}` en el layout). Escanea todo el sitio:
  ```
  find . -name "*.md" -o -name "*.html" | xargs grep -l $'\x8D'
  ```
  (O usa el script de Ruby en cada archivo sospechoso.)
- O es un BOM/carácter invisible al inicio del archivo: Ábrelo en el editor, borra la primera línea si está vacía, guárdalo de nuevo en UTF-8.

Una vez que lo elimines, ejecuta `bundle exec jekyll serve --incremental` de nuevo. Si aún tienes problemas, pega la salida de uno de estos comandos (o del de Ruby), y lo resolveremos.

[Consejos de Hexdump para Buscar Bytes](https://unix.stackexchange.com/questions/38331/finding-bad-characters-in-hex-dump)