---
audio: false
generated: true
lang: de
layout: post
title: Latex-Rendering in Hugo
translated: true
type: note
---

Das beschriebene Problem tritt in **Jekyll** auf, wenn **Kramdown** mit **MathJax** als Mathematik-Engine verwendet wird. Kramdown interpretiert, wenn es mit `math_engine: mathjax` konfiguriert ist, Klammern `( )` im Markdown-Inhalt als LaTeX-Begrenzer für inline-Mathematik (z.B. `\( \)`), was normalen Text, der Klammern enthält, zerstören kann. Dies liegt daran, dass MathJax so eingerichtet ist, dass es `\( \)` oder `$ $` für inline-Mathematik parst, wie in Ihrer Konfiguration gezeigt.

In **Hugo** tritt dieses Problem standardmäßig weniger wahrscheinlich auf, aber es hängt davon ab, wie Sie Hugos Markdown-Prozessor und die MathJax-Integration konfigurieren. Im Folgenden werde ich erklären, warum Hugo dieses Problem in den meisten Fällen vermeidet, wie man es in Jekyll verhindern oder beheben kann und wie man sicherstellt, dass es in Hugo nicht auftritt.

---

### **Hat Hugo dieses Problem?**
Hugo vermeidet dieses Problem typischerweise, weil:
1.  **Markdown-Prozessor**: Hugo verwendet **Goldmark** (oder optional Blackfriday) als standardmäßigen Markdown-Renderer, der MathJax oder LaTeX-Parsing nicht standardmäßig aktiviert. Solange Sie Hugo nicht explizit so konfigurieren, dass er MathJax verwendet und inline-Mathematik-Begrenzer wie `\( \)` einrichtet, werden normale Klammern `( )` in Ihrem Inhalt nicht als LaTeX fehlinterpretiert.
2.  **MathJax-Integration**: Hugo parst LaTeX nicht nativ. Wenn Sie MathJax-Unterstützung wünschen, müssen Sie MathJax-Skripte (wie das von Ihnen bereitgestellte) manuell zu den Templates Ihres Themes hinzufügen (z.B. in `layouts/partials/head.html`) und die Begrenzer konfigurieren. Die Flexibilität von Hugo erlaubt es Ihnen, zu steuern, wie MathJax Inhalte verarbeitet, und so ein automatisches Parsen von `( )` zu vermeiden, es sei denn, es ist explizit aktiviert.
3.  **Shortcodes für Mathematik**: Hugo-Nutzer implementieren LaTeX-Rendering oft mit Shortcodes (z.B. `{{< math >}}...{{< /math >}}`), die mathematische Inhalte explizit kennzeichnen und so verhindern, dass normale Klammern fälschlicherweise für LaTeX gehalten werden.

Zusammenfassend lässt sich sagen, dass Hugo dieses Problem nicht haben wird, es sei denn, Sie konfigurieren MathJax mit den gleichen inline-Begrenzern (`\( \)`) und aktivieren das automatische Parsen ohne entsprechende Schutzmaßnahmen. Durch die Verwendung von Shortcodes oder das Vermeiden von `\( \)` als Begrenzer kann Hugo dieses Problem komplett umgehen.

---

### **Behebung des Problems in Jekyll**
In Jekyll tritt das Problem auf, weil die Kramdown-Einstellung `math_engine: mathjax` in Kombination mit Ihrer MathJax-Konfiguration dazu führt, dass `( )` als LaTeX geparst werden. So können Sie es beheben:

#### **1. MathJax Inline-Begrenzer ändern**
Ändern Sie die MathJax-Konfiguration, um andere inline-Mathematik-Begrenzer zu verwenden, wie z.B. `$ $`, anstelle von `\( \)`, um Konflikte mit normalen Klammern zu vermeiden. Aktualisieren Sie das Skript im HTML-Code Ihrer Jekyll-Site (z.B. in `_includes/head.html`):

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [['$','$']], // Verwenden Sie $ $ für inline-Mathematik
      displayMath: [['$$','$$'], ['\[','\]']],
      processEscapes: true // Erlaubt das Escapen von $, um es literal zu verwenden
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": { linebreaks: { automatic: true } },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```

-   **Warum es funktioniert**: Durch das Entfernen von `['\(','\)']` aus `inlineMath` interpretiert MathJax `( )` nicht mehr als LaTeX-Begrenzer und erhält sie für normalen Text. Die Einstellung `processEscapes: true` erlaubt es Ihnen, `\$` in Markdown zu schreiben, um ein literal `$` anzuzeigen, falls nötig.
-   **In Ihrem Markdown**: Verwenden Sie `$x^2$` für inline-Mathematik anstelle von `\(x^2\)`. Zum Beispiel:
    ```markdown
    Dies ist eine Formel: $x^2 + y^2 = z^2$. Normaler Text (wird nicht geparst).
    ```

#### **2. Klammern in Markdown escapen**
Wenn Sie `\( \)` als Begrenzer beibehalten möchten, escapen Sie Klammern in Ihrem Markdown-Inhalt, um zu verhindern, dass Kramdown/MathJax sie als LaTeX parst. Verwenden Sie einen Backslash `\` vor jeder Klammer:

```markdown
Normaler Text \(keine Formel\). Dies ist eine echte Formel: \(x^2 + y^2\).
```

-   **Ausgabe**: Das escapete `\(keine Formel\)` wird als `(keine Formel)` gerendert, während `\(x^2 + y^2\)` als LaTeX-Formel gerendert wird.
-   **Nachteil**: Dies erfordert das manuelle Escapen jedes Vorkommens von `( )` in Ihrem Inhalt, was mühsam sein kann.

#### **3. MathJax für bestimmte Seiten deaktivieren**
Wenn Sie MathJax nur auf bestimmten Seiten benötigen (z.B. für mathelastige Posts), deaktivieren Sie es standardmäßig und aktivieren Sie es nur dort, wo es benötigt wird:
-   Entfernen Sie das MathJax-Skript aus Ihrem globalen `_layouts/default.html` oder `_includes/head.html`.
-   Fügen Sie eine bedingte Include in Ihrem Layout oder Page-Front Matter hinzu. Zum Beispiel in `_layouts/post.html`:

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

-   Aktivieren Sie MathJax in Ihrem Markdown-File-Front Matter nur für bestimmte Seiten:
    ```yaml
    ---
    title: Mein Mathe-Post
    mathjax: true
    ---
    ```

-   **Warum es funktioniert**: Seiten ohne `mathjax: true` laden MathJax nicht, daher werden `( )` nicht als LaTeX geparst.

#### **4. Eine andere Mathematik-Engine verwenden**
Wechseln Sie von MathJax zu einer anderen, von Kramdown unterstützten Mathematik-Engine, wie **KaTeX**, die schneller ist und weniger wahrscheinlich Klammern fehlinterpretiert, es sei denn, sie ist explizit dafür konfiguriert. Installieren Sie KaTeX in Ihrer Jekyll-Site:
-   Fügen Sie KaTeX-Skripte zu `_includes/head.html` hinzu:
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
-   Aktualisieren Sie `_config.yml`:
    ```yaml
    kramdown:
      math_engine: katex
      input: GFM
      syntax_highlighter: rouge
    ```

-   **Warum es funktioniert**: KaTeX ist strenger beim Parsen und verwendet standardmäßig `$ $` für inline-Mathematik, was Konflikte mit `( )` reduziert. Es ist außerdem schneller als MathJax.

---

### **Sicherstellen, dass Hugo das Problem vermeidet**
Um MathJax in Hugo zu verwenden, ohne auf das `( )`-Parsing-Problem zu stoßen, befolgen Sie diese Schritte:

1.  **MathJax zu Hugo hinzufügen**:
    -   Platzieren Sie das MathJax-Skript in den Partials Ihres Themes (z.B. `layouts/partials/head.html`):
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
    -   Aktivieren Sie MathJax in bestimmten Seiten, indem Sie es zum Front Matter hinzufügen:
        ```yaml
        ---
        title: Mein Mathe-Post
        mathjax: true
        ---
        ```

2.  **Shortcodes für Mathematik verwenden**:
    Erstellen Sie einen Shortcode (z.B. `layouts/shortcodes/math.html`), um mathematische Inhalte explizit zu umschließen:
    ```html
    {{ if .IsNamedParams }}
      <span class="math">{{ .Get "content" | safeHTML }}</span>
    {{ else }}
      <span class="math">{{ .Inner | safeHTML }}</span>
    {{ end }}
    ```
    Verwenden Sie ihn in Ihrem Markdown:
    ```markdown
    Normaler Text (wird nicht geparst). Formel: {{< math >}}$x^2 + y^2${{< /math >}}.
    ```
    -   **Warum es funktioniert**: Shortcodes stellen sicher, dass nur explizit markierte Inhalte als Mathematik verarbeitet werden, wodurch `( )` in normalem Text unberührt bleiben.

3.  **KaTeX stattdessen verwenden**:
    Hugo-Nutzer bevorzugen oft KaTeX wegen seiner Geschwindigkeit. Fügen Sie KaTeX zu `layouts/partials/head.html` hinzu:
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
    Aktivieren Sie es im Front Matter:
    ```yaml
    math: true
    ```
    Verwenden Sie `$ $` für inline-Mathematik, um `( )`-Konflikte zu vermeiden.

---

### **Empfehlung**
-   **Für Jekyll**: Wechseln Sie zu `$ $`-Begrenzern für MathJax oder verwenden Sie KaTeX, um `( )`-Parsing-Probleme zu vermeiden. Das Escapen von Klammern ist ein Fallback, aber für große Sites weniger praktikabel.
-   **Für Hugo**: Sie werden wahrscheinlich nicht auf dieses Problem stoßen, es sei denn, Sie konfigurieren MathJax explizit mit `\( \)`-Begrenzern. Verwenden Sie Shortcodes oder KaTeX für das Mathematik-Rendering, um sicherzustellen, dass normale Klammern sicher sind.

Wenn Sie von Jekyll zu Hugo migrieren und Ihre mathematischen Inhalte behalten möchten, empfehle ich die Verwendung von KaTeX in Hugo mit Shortcodes für explizite Kontrolle. Lassen Sie mich wissen, wenn Sie Hilfe bei der Einrichtung von Hugos MathJax/KaTeX-Integration oder bei der Konvertierung der mathematischen Inhalte Ihrer Jekyll-Site benötigen!