---
audio: false
generated: true
image: false
lang: es
layout: post
title: Corrección del Validador que Clasificaba Incorrectamente Coreano como Chino
translated: true
type: note
---

Entendido — en esta salida de depuración:

```
Debug: raw langdetect output: [('ko', 0.9999995211930662)]
...
Idiomas detectados: [('ko', 0.9999995211930662)]
```

El código **`ko`** es el código de idioma ISO 639-1 para **Coreano**. 🇰🇷

Entonces `langdetect` está diciendo:

* Cree que el texto es coreano (`ko`)
* Con una probabilidad ≈ **0.9999995** (esencialmente 100%)

Eso explica el error: tu validador esperaba `"zh-tw"` (Chino tradicional), pero el detector decidió que la entrada parece coreano en su lugar.

👉 Recordatorio rápido del mapeo de `langdetect` / ISO 639-1:

* `zh` → Chino (no especificado)
* `zh-cn` → Chino simplificado (China)
* `zh-tw` (o `hant` en tu mapeo) → Chino tradicional (Taiwán)
* `ja` → Japonés
* `ko` → Coreano
* `ne` → Nepalí
* `hi` → Hindi

¿Quieres que sugiera cómo podrías **robustecer tu validador** para que no falle cuando `langdetect` clasifique incorrectamente (por ejemplo, permitiendo una alternativa si los caracteres del script objetivo son claramente chinos pero el código resulta ser `ko`)?