---
audio: false
generated: true
image: false
lang: es
layout: post
title: ASCII Hex UTF-8 Explicado Sencillamente
translated: true
type: note
---

Desglosémoslos claramente:

---

### ASCII

* **Definición**: ASCII (American Standard Code for Information Interchange) es una de las primeras codificaciones de caracteres.
* **Rango**: Usa **7 bits** (valores 0–127).
* **Significado**: Cada número corresponde a un carácter.
  Por ejemplo:

  * `65` → `"A"`
  * `97` → `"a"`
  * `48` → `"0"`
* **Limitación**: Solo cubre letras inglesas, dígitos, puntuación y códigos de control (como salto de línea).

---

### Hex (Representación Hexadecimal)

* **Definición**: Hex no es un conjunto de caracteres en sí mismo, sino una **representación numérica** (base-16) de datos.
* **Uso**: Se usa comúnmente para mostrar bytes de forma compacta y legible para humanos.
* **Ejemplo**:

  * ASCII `"A"` = decimal `65` = hex `41`.
  * ASCII `"B"` = decimal `66` = hex `42`.
  * Por lo tanto, el texto `"AB"` se ve como `41 42` en hex.

---

### UTF-8

* **Definición**: UTF-8 es un estándar de **codificación Unicode**.
* **Características**:

  * Longitud variable: codifica cada carácter en **1 a 4 bytes**.
  * Compatible con ASCII: los caracteres `0–127` son los mismos que en ASCII (1 byte).
  * Puede representar todos los caracteres Unicode (letras, símbolos, emojis, caracteres chinos, etc.).
* **Ejemplos**:

  * `"A"` → `41` (igual que ASCII).
  * `"中"` → `E4 B8 AD` (tres bytes en hex).
  * `"😊"` → `F0 9F 98 8A` (cuatro bytes en hex).

---

✅ **En resumen**:

* ASCII = código antiguo de 7 bits para caracteres en inglés.
* Hex = una forma de escribir números/bytes (base-16).
* UTF-8 = codificación moderna que incluye ASCII pero también admite todos los idiomas y símbolos.

---

¿Te gustaría que también te muestre un **ejemplo comparativo del mismo texto** (`"Hello 世界😊"`) en ASCII (donde sea posible), hex y UTF-8 para que puedas ver la diferencia directamente?