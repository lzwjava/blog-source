---
audio: false
generated: true
image: false
lang: es
layout: post
title: El detector de idiomas confundió el texto con nepalí
translated: true
type: note
---

Ah, ya veo — gracias por aclarar.

En el registro que pegaste:

```
Debug: raw langdetect output: [('ne', 0.9999953270916105)]
Debug: normalized langdetect output: [('ne', 0.9999953270916105)]
Debug: Detected languages: [('ne', 0.9999953270916105)]
```

Aquí **`ne` no es la palabra francesa** — en realidad es un **código de idioma** emitido por `langdetect`.

La librería `langdetect` a veces devuelve `"ne"` como el código ISO 639-1 para **Nepalí**.

* `"en"` = Inglés
* `"fr"` = Francés
* `"hi"` = Hindi
* `"ne"` = Nepalí

Así que en este caso, `langdetect` pensó que tu texto era Nepalí con una probabilidad de `~0.99999`.

Por eso tu validación falló con:

```
Translated text does not contain the target language 'hi' (detected: [('ne', 0.9999953270916105)])
```

👉 En resumen:

* `ne` aquí = código de idioma ISO **Nepalí**, no la palabra de negación francesa `"ne"`.
* Aparece cuando `langdetect` decide que tu entrada se parece al Nepalí.

¿Quieres que te muestre cómo **normalizar o reasignar** `ne` (Nepalí) en tu `_map_target_code` para que tu validador no falle cuando aparezcan idiomas inesperados?