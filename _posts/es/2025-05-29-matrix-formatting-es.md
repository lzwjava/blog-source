---
audio: false
generated: true
lang: es
layout: post
title: Corrección del Formato de Matrices en el Blog de Jekyll
translated: true
type: note
---

El problema que estás enfrentando está relacionado con cómo Markdown (kramdown) procesa el contenido antes de que MathJax lo renderice. Las barras invertidas dobles (`\\`) en tu matriz están siendo interpretadas por Markdown antes de que MathJax llegue a ellas, lo que rompe el formato de la matriz.

Aquí hay algunas soluciones para solucionar esto:

### Solución 1: Escapar las barras invertidas
Puedes escapar cada barra invertida con otra barra invertida:

```latex
$A - I = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\\ 0 & 1 & 0 \\\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\\ 2 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$
```

### Solución 2: Usar `\\` dentro de bloques matemáticos
Para matemáticas en display (no en línea), usa `$$` o `\\\[ \\\]`:

```latex
$$
A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
```

### Solución 3: Usar etiquetas HTML para evitar el procesamiento de Markdown
Envuelve tus matemáticas en etiquetas HTML `div` para evitar el procesamiento de Markdown:

```html
<div>
$$
A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
</div>
```

### Solución 4: Modificar tu configuración de kramdown
Añade esto a tu `_config.yml` para evitar que kramdown procese los bloques matemáticos:

```yaml
kramdown:
  math_engine: mathjax
  syntax_highlighter: rouge
```

Luego puedes usar:

```latex
$$ A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
```

Prueba estas soluciones una por una para ver cuál funciona mejor con tu configuración de Jekyll. La solución más confiable es típicamente usar matemáticas en display (`$$` o `\\\[ \\\]`) en lugar de matemáticas en línea (`$`) para matrices y otras ecuaciones complejas.