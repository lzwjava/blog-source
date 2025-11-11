---
audio: false
generated: true
lang: es
layout: post
title: Usar KaTeX en Jekyll
translated: true
type: note
---

Para usar KaTeX en lugar de MathJax en Jekyll con tu configuración actual, necesitarás reemplazar los scripts de MathJax con KaTeX y ajustar tu configuración de Jekyll. KaTeX es más rápido y ligero que MathJax, pero requiere un enfoque diferente ya que no admite todas las características de MathJax (por ejemplo, la numeración automática de ecuaciones es más manual). A continuación, se presenta una guía paso a paso para cambiar a KaTeX en tu sitio Jekyll:

### 1. Actualiza tu Configuración de Jekyll
Modifica tu `_config.yml` para usar KaTeX como el motor de matemáticas para Kramdown. Actualiza la sección `kramdown` de la siguiente manera:

```yaml
kramdown:
  math_engine: katex
  input: GFM
  syntax_highlighter: rouge
```

Esto le indica a Kramdown que renderice las expresiones matemáticas LaTeX usando KaTeX en lugar de MathJax.

### 2. Incluye KaTeX en tu HTML
Elimina los scripts de MathJax de tu HTML y reemplázalos con KaTeX. Puedes incluir KaTeX a través de una CDN. Añade lo siguiente a la sección `<head>` de tu archivo de diseño de Jekyll (por ejemplo, `_layouts/default.html`):

```html
<!-- KaTeX CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" integrity="sha384-nB0miv6/jRmo5SLY8cTjmnkA3wC7o1L0jOey4Cki5N3kdjdPD/mW59G1Qsxa8c3y" crossorigin="anonymous">

<!-- KaTeX JS -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" integrity="sha384-7zkKLzPD3M4y9W8FWsN4Z0yO5eLu8qUn0QHY6hZ2r3fDzqjk0McYc3vJrmE2h6cZ" crossorigin="anonymous"></script>

<!-- Extensión Auto-render (opcional, para renderizado automático de matemáticas) -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" integrity="sha384-43gviWU0YVjaDtb/GhzOouOXtZMP/7XUzwPTL0xF3iS9Ho94fSc31UyUyIDgWvB4" crossorigin="anonymous"></script>

<!-- Configuración de Auto-render -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: "$$", right: "$$", display: true}, // Matemáticas en bloque
        {left: "\\[", right: "\\]", display: true}, // Matemáticas en bloque
        {left: "\\(", right: "\\)", display: false}, // Matemáticas en línea
        {left: "$", right: "$", display: false} // Matemáticas en línea
      ],
      throwOnError: false
    });
  });
</script>
```

### 3. Elimina la Configuración de MathJax
Elimina el código relacionado con MathJax de tu archivo de diseño, incluyendo el bloque `<script type="text/x-mathjax-config">` y el script CDN de MathJax. KaTeX no usa una configuración como `tex2jax` de MathJax, y el script auto-render anterior maneja una funcionalidad similar.

### 4. Escribe Matemáticas en tu Markdown
Con KaTeX y Kramdown configurados, puedes escribir matemáticas LaTeX en tus archivos Markdown usando los mismos delimitadores que antes:

- **Matemáticas en línea**: Usa `$...$` o `\(...\)` (por ejemplo, `$E=mc^2$` o `\(E=mc^2\)`).
- **Matemáticas en bloque**: Usa `$$...$$` o `\[...\]` (por ejemplo, `$$E=mc^2$$` o `\[E=mc^2\]`).

Por ejemplo:

```markdown
Matemáticas en línea: $E=mc^2$ o \(E=mc^2\).

Matemáticas en bloque:
$$E=mc^2$$

o

\[E=mc^2\]
```

Kramdown con el motor de matemáticas KaTeX procesará estos en HTML que KaTeX renderiza.

### 5. Notas sobre KaTeX vs. MathJax
- **Numeración Automática de Ecuaciones**: KaTeX no admite la numeración automática de ecuaciones como `autoNumber: "AMS"` de MathJax. Si necesitas números de ecuación, debes añadirlos manualmente usando `\tag{}` en tu código LaTeX (por ejemplo, `$$E=mc^2 \tag{1}$$`).
- **Rendimiento**: KaTeX es significativamente más rápido que MathJax, lo que es ideal para sitios estáticos como Jekyll.
- **Conjunto de Características**: KaTeX admite menos comandos LaTeX que MathJax. Consulta las [funciones admitidas por KaTeX](https://katex.org/docs/supported.html) para asegurarte de que tus expresiones matemáticas sean compatibles.
- **Renderizado**: El script auto-render anterior imita el comportamiento de MathJax renderizando automáticamente las expresiones matemáticas dentro de los delimitadores especificados. Ajusta el array `delimiters` en el script si deseas cambiar o limitar los delimitadores.

### 6. Prueba tu Configuración
Ejecuta tu sitio Jekyll localmente (`jekyll serve`) y verifica que las expresiones matemáticas se rendericen correctamente. Si encuentras problemas:
- Revisa la consola del navegador en busca de errores relacionados con KaTeX.
- Asegúrate de que las URLs CDN de KaTeX estén actualizadas (las anteriores usan la versión 0.16.11, la más reciente según mi conocimiento).
- Confirma que tus archivos Markdown usen una sintaxis LaTeX compatible con KaTeX.

### 7. Opcional: Archivos Locales de KaTeX
Si prefieres alojar los archivos de KaTeX localmente para evitar la dependencia de la CDN:
1. Descarga `katex.min.css`, `katex.min.js` y `auto-render.min.js` de los [lanzamientos de KaTeX en GitHub](https://github.com/KaTeX/KaTeX/releases).
2. Colócalos en tu carpeta de assets de Jekyll (por ejemplo, `assets/katex/`).
3. Actualiza las etiquetas `<link>` y `<script>` para que apunten a tus archivos locales (por ejemplo, `/assets/katex/katex.min.css`).

### 8. Resolución de Problemas
- **Las matemáticas no se renderizan**: Asegúrate de que los scripts de KaTeX se carguen correctamente y de que `kramdown.math_engine` esté establecido en `katex`.
- **Problemas con los delimitadores**: Verifica que tus delimitadores en el script auto-render coincidan con los de tu Markdown.
- **Comandos no admitidos**: Si falla un comando LaTeX, consulta la documentación de KaTeX para los comandos admitidos o reescribe la expresión.

Si necesitas ayuda específica con una expresión matemática o configuración en particular, comparte los detalles y puedo ofrecerte una guía personalizada.