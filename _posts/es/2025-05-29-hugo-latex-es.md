---
audio: false
generated: true
lang: es
layout: post
title: Renderizado de Latex en Hugo
translated: true
type: note
---

El problema que describes surge en **Jekyll** cuando se usa **Kramdown** con **MathJax** como motor matemático. Kramdown, cuando se configura con `math_engine: mathjax`, interpreta los paréntesis `( )` en el contenido Markdown como delimitadores LaTeX para matemáticas en línea (por ejemplo, `\( \)`), lo que puede romper el texto normal que contiene paréntesis. Esto se debe a que MathJax está configurado para analizar `\( \)` o `$ $` para matemáticas en línea, como se muestra en tu configuración.

En **Hugo**, es menos probable que este problema ocurra por defecto, pero depende de cómo configures el procesador Markdown de Hugo y la integración de MathJax. A continuación, explicaré por qué Hugo evita este problema en la mayoría de los casos, cómo prevenirlo o solucionarlo en Jekyll y cómo asegurarse de que no suceda en Hugo.

---

### **¿Tiene Hugo este problema?**
Hugo normalmente evita este problema porque:
1.  **Procesador Markdown**: Hugo usa **Goldmark** (u opcionalmente Blackfriday) como su renderizador Markdown por defecto, que no habilita MathJax ni el análisis de LaTeX de forma predeterminada. A menos que configures explícitamente Hugo para usar MathJax y establezcas delimitadores de matemáticas en línea como `\( \)`, los paréntesis regulares `( )` en tu contenido no serán malinterpretados como LaTeX.
2.  **Integración MathJax**: Hugo no analiza LaTeX de forma nativa. Si deseas soporte para MathJax, debes agregar manualmente los scripts de MathJax (como el que proporcionaste) a las plantillas de tu tema (por ejemplo, en `layouts/partials/head.html`) y configurar los delimitadores. La flexibilidad de Hugo te permite controlar cómo MathJax procesa el contenido, evitando el análisis automático de `( )` a menos que se habilite explícitamente.
3.  **Shortcodes para Matemáticas**: Los usuarios de Hugo a menudo implementan el renderizado de LaTeX usando shortcodes (por ejemplo, `{{< math >}}...{{< /math >}}`), que designan explícitamente el contenido matemático, evitando que los paréntesis regulares se confundan con LaTeX.

En resumen, Hugo no tendrá este problema a menos que configures MathJax con los mismos delimitadores en línea (`\( \)`) y habilites el análisis automático sin las salvaguardas adecuadas. Al usar shortcodes o evitar `\( \)` como delimitadores, Hugo puede eludir este problema por completo.

---

### **Solucionar el problema en Jekyll**
En Jekyll, el problema ocurre porque la configuración `math_engine: mathjax` de Kramdown, combinada con tu configuración de MathJax, hace que `( )` se analicen como LaTeX. Aquí se explica cómo solucionarlo:

#### **1. Cambiar los delimitadores en línea de MathJax**
Modifica la configuración de MathJax para usar diferentes delimitadores de matemáticas en línea, como `$ $`, en lugar de `\( \)` para evitar conflictos con los paréntesis regulares. Actualiza el script en el HTML de tu sitio Jekyll (por ejemplo, en `_includes/head.html`):

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [['$','$']], // Usar $ $ para matemáticas en línea
      displayMath: [['$$','$$'], ['\[','\]']],
      processEscapes: true // Permitir escapar $ para usarlo literalmente
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": { linebreaks: { automatic: true } },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```

-   **Por qué funciona**: Al eliminar `['\(','\)']` de `inlineMath`, MathJax ya no interpreta `( )` como delimitadores LaTeX, preservándolos para texto regular. La configuración `processEscapes: true` te permite escribir `\$` en Markdown para mostrar un `$` literal si es necesario.
-   **En tu Markdown**: Usa `$x^2$` para matemáticas en línea en lugar de `\(x^2\)`. Por ejemplo:
    ```markdown
    Esta es una fórmula: $x^2 + y^2 = z^2$. Texto normal (no analizado).
    ```

#### **2. Escapar paréntesis en Markdown**
Si deseas mantener `\( \)` como delimitadores, escapa los paréntesis en tu contenido Markdown para evitar que Kramdown/MathJax los analice como LaTeX. Usa una barra invertida `\` antes de cada paréntesis:

```markdown
Texto normal \(no es una fórmula\). Esta es una fórmula real: \(x^2 + y^2\).
```

-   **Salida**: El texto escapado `\(no es una fórmula\)` se renderiza como `(no es una fórmula)`, mientras que `\(x^2 + y^2\)` se renderiza como una fórmula LaTeX.
-   **Desventaja**: Esto requiere escapar manualmente cada instancia de `( )` en tu contenido, lo que puede ser tedioso.

#### **3. Deshabilitar MathJax para páginas específicas**
Si solo necesitas MathJax en ciertas páginas (por ejemplo, para publicaciones con muchas matemáticas), desactívalo por defecto y habilítalo solo donde sea necesario:
-   Elimina el script de MathJax de tu `_layouts/default.html` global o `_includes/head.html`.
-   Agrega una inclusión condicional en tu diseño o en el front matter de la página. Por ejemplo, en `_layouts/post.html`:

```html
{% if page.mathjax %}
  <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      tex2jax: {
        inlineMath: [['$','$']],
        displayMath: [['$$','$$'], ['\[','\]']],
        processEscapes: true
      }
    });
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
{% endif %}
```

-   En el front matter de tu archivo Markdown, habilita MathJax solo para páginas específicas:
    ```yaml
    ---
    title: Mi publicación de matemáticas
    mathjax: true
    ---
    ```

-   **Por qué funciona**: Las páginas sin `mathjax: true` no cargarán MathJax, por lo que `( )` no se analizarán como LaTeX.

#### **4. Usar un motor matemático diferente**
Cambia de MathJax a otro motor matemático compatible con Kramdown, como **KaTeX**, que es más rápido y menos propenso a malinterpretar paréntesis a menos que se configure explícitamente. Instala KaTeX en tu sitio Jekyll:
-   Agrega los scripts de KaTeX a `_includes/head.html`:
    ```html
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/auto-render.min.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ]
        });
      });
    </script>
    ```
-   Actualiza `_config.yml`:
    ```yaml
    kramdown:
      math_engine: katex
      input: GFM
      syntax_highlighter: rouge
    ```

-   **Por qué funciona**: KaTeX es más estricto con el análisis y usa `$ $` para matemáticas en línea por defecto, reduciendo los conflictos con `( )`. También es más rápido que MathJax.

---

### **Asegurar que Hugo evite este problema**
Para usar MathJax en Hugo sin encontrarte con el problema de análisis de `( )`, sigue estos pasos:

1.  **Agregar MathJax a Hugo**:
    -   Coloca el script de MathJax en los partials de tu tema (por ejemplo, `layouts/partials/head.html`):
        ```html
        {{ if .Params.mathjax }}
        <script type="text/x-mathjax-config">
          MathJax.Hub.Config({
            tex2jax: {
              inlineMath: [['$','$']],
              displayMath: [['$$','$$'], ['\[','\]']],
              processEscapes: true
            },
            "HTML-CSS": { linebreaks: { automatic: true } },
            "CommonHTML": { linebreaks: { automatic: true } },
            TeX: { equationNumbers: { autoNumber: "AMS" } }
          });
        </script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
        {{ end }}
        ```
    -   Habilita MathJax en páginas específicas agregando en el front matter:
        ```yaml
        ---
        title: Mi publicación de matemáticas
        mathjax: true
        ---
        ```

2.  **Usar Shortcodes para Matemáticas**:
    Crea un shortcode (por ejemplo, `layouts/shortcodes/math.html`) para envolver explícitamente el contenido matemático:
    ```html
    {{ if .IsNamedParams }}
      <span class="math">{{ .Get "content" | safeHTML }}</span>
    {{ else }}
      <span class="math">{{ .Inner | safeHTML }}</span>
    {{ end }}
    ```
    Úsalo en tu Markdown:
    ```markdown
    Texto normal (no analizado). Fórmula: {{< math >}}$x^2 + y^2${{< /math >}}.
    ```
    -   **Por qué funciona**: Los shortcodes aseguran que solo el contenido marcado explícitamente se procese como matemáticas, dejando los `( )` en el texto regular intactos.

3.  **Usar KaTeX en su lugar**:
    Los usuarios de Hugo a menudo prefieren KaTeX por su velocidad. Agrega KaTeX a `layouts/partials/head.html`:
    ```html
    {{ if .Params.math }}
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/auto-render.min.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ]
        });
      });
    </script>
    {{ end }}
    ```
    Habilítalo en el front matter:
    ```yaml
    math: true
    ```
    Usa `$ $` para matemáticas en línea para evitar conflictos con `( )`.

---

### **Recomendación**
-   **Para Jekyll**: Cambia a los delimitadores `$ $` para MathJax o usa KaTeX para evitar problemas de análisis de `( )`. Escapar paréntesis es una solución alternativa pero menos práctica para sitios grandes.
-   **Para Hugo**: Es poco probable que encuentres este problema a menos que configures explícitamente MathJax con delimitadores `\( \)`. Usa shortcodes o KaTeX para el renderizado de matemáticas para garantizar que los paréntesis regulares estén seguros.

Si estás migrando de Jekyll a Hugo y deseas mantener tu contenido matemático, recomiendo usar KaTeX en Hugo con shortcodes para un control explícito. ¡Avísame si necesitas ayuda para configurar la integración de MathJax/KaTeX en Hugo o para convertir el contenido matemático de tu sitio Jekyll!