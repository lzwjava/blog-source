---
audio: false
generated: true
lang: de
layout: post
title: Behebung von Matrixformatierung im Jekyll-Blog
translated: true
type: note
---

Das Problem, das Sie haben, hängt damit zusammen, wie Markdown (kramdown) den Inhalt verarbeitet, bevor MathJax ihn rendert. Die doppelten Backslashes (`\\`) in Ihrer Matrix werden von Markdown interpretiert, bevor MathJax sie erreicht, was die Matrixformatierung zerstört.

Hier sind ein paar Lösungen, um dies zu beheben:

### Lösung 1: Escapen der Backslashes
Sie können jeden Backslash mit einem weiteren Backslash escapen:

```latex
$A - I = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\\ 0 & 1 & 0 \\\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\\ 2 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$
```

### Lösung 2: Verwenden Sie `\\` innerhalb von Math-Blöcken
Für Display-Mathematik (nicht inline) verwenden Sie `$$` oder `\\\[ \\\]`:

```latex
$$
A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
```

### Lösung 3: Verwenden Sie HTML-Tags, um die Markdown-Verarbeitung zu verhindern
Wickeln Sie Ihre Mathematik in HTML-`div`-Tags ein, um die Markdown-Verarbeitung zu verhindern:

```html
<div>
$$
A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
</div>
```

### Lösung 4: Ändern Sie Ihre Kramdown-Konfiguration
Fügen Sie dies zu Ihrer `_config.yml` hinzu, um zu verhindern, dass kramdown Math-Blöcke verarbeitet:

```yaml
kramdown:
  math_engine: mathjax
  syntax_highlighter: rouge
```

Dann können Sie verwenden:

```latex
$$ A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
```

Probieren Sie diese Lösungen nacheinander aus, um zu sehen, welche am besten mit Ihrem Jekyll-Setup funktioniert. Die zuverlässigste Lösung ist typischerweise, Display-Mathematik (`$$` oder `\\\[ \\\]`) anstelle von Inline-Mathematik (`$`) für Matrizen und andere komplexe Gleichungen zu verwenden.