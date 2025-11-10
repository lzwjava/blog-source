---
audio: false
generated: true
lang: es
layout: post
title: Los nombres de paquetes de Java no pueden comenzar con números
translated: true
type: note
---

En Java, un **package name no puede comenzar con un número**. Según las Convenciones de Nomenclatura de Java y la Especificación del Lenguaje Java:

- Los nombres de los paquetes deben ser identificadores válidos.
- Un identificador válido en Java debe comenzar con una letra (A-Z o a-z), un guión bajo (`_`) o un signo de dólar (`$`).
- Los números (0-9) están permitidos en los identificadores, pero solo **después** del primer carácter.

Por ejemplo:
- Nombres de paquete válidos: `com.example`, `my_package`, `a123`
- Nombres de paquete inválidos: `123example`, `1package`

Si intentas usar un nombre de paquete que comienza con un número, el compilador de Java generará un error de sintaxis. Para solucionar esto, puedes:
- Comenzar el nombre del paquete con una letra o un guión bajo, por ejemplo, `a123.example` o `_123.example`.
- Usar un nombre descriptivo que siga las convenciones, como `com.example.project123`.

Esta regla garantiza la coherencia y compatibilidad en el sistema de nomenclatura de Java.