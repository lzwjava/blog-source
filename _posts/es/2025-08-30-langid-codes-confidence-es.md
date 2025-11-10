---
audio: false
generated: true
image: false
lang: es
layout: post
title: Códigos de Idioma Langid y Confianza
translated: true
type: note
---

En `langid`, la función `classify(texto)` devuelve una tupla `(idioma, confianza)` donde:

* **`idioma`** es un código de idioma ISO 639-1 de dos letras (a veces extendido con códigos de región como `zh-cn` o `zh-tw`).
* **`confianza`** es un valor flotante entre 0 y 1 que indica el nivel de confianza del modelo.

El conjunto de valores posibles para `idioma` proviene de los idiomas admitidos por `langid.py`. Incluye **97 idiomas** de forma predeterminada. Algunos ejemplos comunes:

* `en` → English
* `zh` / `zh-cn` / `zh-tw` → Chinese (genérico / Simplified / Traditional)
* `ja` → Japanese
* `ko` → Korean
* `fr` → French
* `de` → German
* `es` → Spanish
* `hi` → Hindi
* `ar` → Arabic
* `ru` → Russian

Y muchos otros: la lista completa cubre la mayoría de los idiomas principales del mundo (Afrikaans, Bengali, Greek, Hebrew, Italian, Portuguese, Swahili, Thai, Turkish, Vietnamese, etc.).

👉 Si lo deseas, puedo darte la **lista completa de los 97 códigos** admitidos por `langid`. ¿Te gustaría que la muestre?