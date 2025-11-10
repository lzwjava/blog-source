---
audio: false
generated: true
lang: es
layout: post
title: Redefinir el estilo de párrafo para peso medio
translated: true
type: note
---

Para cambiar todo el entorno `cvparagraph` para usar `\mdseries` en lugar de `\bodyfontlight`, necesitas redefinir el comando `\paragraphstyle`. Añade esto a tu preámbulo después de cargar la clase awesome-cv:

```latex
\renewcommand*{\paragraphstyle}{\fontsize{11pt}{1em}\mdseries\upshape\color{text}}
```

Esto cambiará el estilo de párrafo de:
- `\bodyfontlight` (que es peso ligero)

a:
- `\mdseries` (que es peso medio, similar al estilo de descripción)

De esta manera, todo tu entorno `cvparagraph` usará la serie de fuente de peso medio como lo hace `\descriptionstyle`.