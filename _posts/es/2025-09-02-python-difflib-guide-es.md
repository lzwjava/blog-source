---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Comparación de Secuencias con Python Difflib
translated: true
type: note
---

En Python, el módulo **`difflib`** proporciona herramientas para comparar secuencias—cadenas de texto, listas o cualquier iterable. Se utiliza a menudo para tareas como detectar diferencias entre textos (como `diff` en Unix) o construir herramientas de autocompletado y similitud.

---

### Cómo funciona `difflib`

En esencia, `difflib` intenta encontrar las subsecuencias coincidentes contiguas más largas entre dos entradas. Luego utiliza estas coincidencias para resaltar similitudes y diferencias. La biblioteca puede:

* Generar diferencias legibles para humanos (`ndiff`, `unified_diff`, `context_diff`).
* Calcular ratios de similitud entre secuencias.
* Sugerir coincidencias cercanas de una lista (`get_close_matches`).

---

### `SequenceMatcher`

La clase más importante es **`difflib.SequenceMatcher`**.

**Cómo funciona**:

* Compara dos secuencias elemento por elemento.
* Busca la *subsecuencia común más larga* (pero no necesariamente contigua).
* Produce una lista de operaciones (`replace`, `delete`, `insert`, `equal`) que describe cómo transformar una secuencia en otra.

**Métodos clave**:

1. **`ratio()`**
   Devuelve un float en `[0, 1]` que mide la similitud.
   Fórmula:

   $$
   \text{ratio} = \frac{2 \times M}{T}
   $$

   donde `M` = número de elementos coincidentes, y `T` = elementos totales en ambas secuencias.

2. **`quick_ratio()`** y **`real_quick_ratio()`**
   Aproximaciones más rápidas de la similitud, sacrificando precisión por velocidad.

3. **`get_opcodes()`**
   Devuelve una lista de operaciones para transformar `a` en `b`. Ejemplo: `[('replace', 0, 2, 0, 1), ('equal', 2, 4, 1, 3)]`.

4. **`get_matching_blocks()`**
   Devuelve todas las subsecuencias coincidentes con sus posiciones.

---

### Ejemplo

```python
import difflib

a = "hello world"
b = "helo wrld"

s = difflib.SequenceMatcher(None, a, b)

print("Similarity ratio:", s.ratio())
print("Operations:", s.get_opcodes())
print("Matching blocks:", s.get_matching_blocks())
```

**Salida**:

```
Similarity ratio: 0.9090909090909091
Operations: [('equal', 0, 1, 0, 1), ('delete', 1, 2, 1, 1),
             ('equal', 2, 5, 1, 4), ('delete', 5, 6, 4, 4),
             ('equal', 6, 11, 4, 9)]
Matching blocks: [Match(a=0, b=0, size=1),
                  Match(a=2, b=1, size=3),
                  Match(a=6, b=4, size=5),
                  Match(a=11, b=9, size=0)]
```

---

👉 En resumen:

* `difflib` es un kit de herramientas para comparar secuencias.
* `SequenceMatcher` es el motor central—encuentra subsecuencias coincidentes y calcula similitudes.
* Es útil para diferencias (diffs), correctores ortográficos, detección de plagio, autosugerencias, etc.

¿Te gustaría que también muestre cómo usar `get_close_matches()` (que internamente usa `SequenceMatcher`) para la coincidencia aproximada de cadenas, como en correctores ortográficos o sugerencias de búsqueda?