---
audio: false
generated: true
image: false
lang: es
layout: post
title: Lista de Elementos para el Modo Oscuro de Angular
translated: true
type: note
---

Cuando implementas un modo oscuro en un frontend de Angular, normalmente comenzarás con `body`, `select` y `option`, pero hay bastantes otros elementos HTML comunes que querrás rediseñar para que el tema se sienta consistente. Aquí tienes una lista práctica:

### Nivel de Página y Contenedores

* `html`, `body` → color de fondo y de texto.
* `div`, `section`, `article`, `aside`, `header`, `footer`, `main`, `nav` → establecer colores de fondo y de texto (especialmente si tienen fondos blancos por defecto).

### Texto y Encabezados

* `h1, h2, h3, h4, h5, h6` → asegúrate de que el texto sea visible contra el fondo oscuro.
* `p`, `span`, `a` → ajusta el color del texto, los colores al pasar el cursor sobre los enlaces y los estados de los enlaces visitados.

### Formularios y Entradas

* `input[type="text"], input[type="password"], input[type="email"], textarea` → fondo, color de texto y borde.
* `input[type="checkbox"], input[type="radio"]` → a veces necesitan un manejo especial para la visibilidad.
* `select, option` → como mencionaste, tanto el fondo como el color del texto.
* `button` → fondo, borde y color del texto, más los estados hover/active.
* `label` → asegúrate de que el texto contraste con el fondo oscuro.
* `fieldset, legend` → fondo y borde.

### Listas y Tablas

* `ul, ol, li` → color del texto.
* `table` → fondo, color del borde y color del texto.
* `thead, tbody, tr, th, td` → ajustes individuales para fondos y bordes.

### Elementos Interactivos

* `details, summary` → fondo y texto.
* `dialog` → fondo y texto.
* `mark` → los colores de resaltado deben funcionar en oscuro (el amarillo por defecto puede ser demasiado brillante).

### Media y Varios

* `hr` → color del borde (por defecto suele ser demasiado claro sobre oscuro).
* `code, pre` → color de fondo y del texto para la legibilidad.
* `blockquote` → color de fondo y del borde.
* `progress, meter` → colores de la pista y del valor.

---

💡 **Mejor práctica**: En lugar de usar `!important` en todas partes, define variables CSS para los colores (`--bg-color`, `--text-color`, etc.) y cámbialas cuando el modo oscuro esté activo (por ejemplo, añadiendo una clase `.dark-mode` al `body`). De esa manera, los componentes de Angular y los elementos personalizados también pueden integrarse limpiamente en el tema.

¿Te gustaría que redacte un **fragmento de CSS base** para el modo oscuro (con variables) que puedas incorporar a tu proyecto de Angular como punto de partida?