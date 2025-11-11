---
audio: false
generated: true
lang: de
layout: post
title: Markdown-Rendering mit MathJax oder KaTeX
translated: true
type: note
---

Um LaTeX-Mathematikdarstellung mit **Markdown**-Darstellung auf einer Webseite zu kombinieren, verwenden Sie typischerweise eine JavaScript-Bibliothek (wie **MathJax** oder **KaTeX**) zusammen mit einem Markdown-Parser, der die Standard-Markdown-Syntax verarbeiten kann. Das Ziel ist es, Benutzern zu ermöglichen, mathematische Formeln in LaTeX innerhalb von Markdown zu schreiben und sie korrekt auf der Seite darzustellen.

Hier ist eine Anleitung, wie Sie dies erreichen können:

### 1. **Markdown-Darstellung mit MathJax oder KaTeX**

Sie können einen **Markdown-Parser** wie **marked.js** oder **remarkable.js** verwenden, um den grundlegenden Markdown-Inhalt darzustellen. Nachdem der Markdown-Inhalt gerendert wurde, verwenden Sie MathJax oder KaTeX, um die LaTeX-Mathematik darin zu rendern.

Nachfolgend finden Sie einen schrittweisen Ansatz, um dies zu erreichen.

---

### **Schritt 1: Bibliotheken einbinden**

Sie müssen sowohl einen **Markdown-Parser** als auch eine **Mathematik-Rendering-Bibliothek** (MathJax oder KaTeX) in Ihre HTML-Datei einbinden.

So können Sie sie einbinden:

```html
<!-- KaTeX (oder MathJax) für LaTeX-Rendering einbinden -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.css">
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.js"></script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/contrib/auto-render.min.js"></script>

<!-- Einen Markdown-Parser (wie marked.js) einbinden -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.0.10/marked.min.js"></script>
```

Alternativ, wenn Sie **MathJax** anstelle von KaTeX bevorzugen, können Sie MathJax wie folgt einbinden:

```html
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

---

### **Schritt 2: Einrichten des Markdown-zu-LaTeX-Rendering-Prozesses**

Jetzt können Sie Ihre HTML-Struktur schreiben und JavaScript verwenden, um den Markdown zu rendern und anschließend alle LaTeX-Formeln innerhalb dieses Markdowns zu verarbeiten.

Hier ist ein einfaches Beispiel:

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Markdown + Math Rendering</title>

  <!-- KaTeX für Mathematik-Rendering einbinden -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/contrib/auto-render.min.js"></script>

  <!-- marked.js für Markdown-Rendering einbinden -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.0.10/marked.min.js"></script>
</head>
<body>

  <h1>Markdown + Math Rendering Beispiel</h1>

  <!-- Textarea für Markdown-Eingabe -->
  <textarea id="markdownInput" rows="10" cols="50">
Dies ist ein Markdown-Editor. Sie können LaTeX-Matheformeln wie folgt hinzufügen:

Inline-Mathematik: \( E = mc^2 \)

Block-Mathematik:
\[
\int_0^1 x^2 \, dx = \frac{1}{3}
\]
  </textarea>

  <hr>

  <!-- Container für gerenderten Markdown -->
  <div id="markdownOutput"></div>

  <script>
    // Funktion zum Rendern von Markdown + Mathematik
    function renderMarkdown() {
      // Holt die eingegebenen Markdown-Daten
      const markdownText = document.getElementById('markdownInput').value;

      // Rendert den Markdown-Inhalt
      const htmlContent = marked(markdownText);

      // Fügt das gerenderte HTML in die Ausgabe-Div ein
      document.getElementById('markdownOutput').innerHTML = htmlContent;

      // Rendert die Mathematik im HTML-Inhalt mit KaTeX
      renderMathInElement(document.getElementById('markdownOutput'), {
        delimiters: [
          { left: "\\(", right: "\\)", display: false }, // inline math
          { left: "\\[", right: "\\]", display: true }   // block math
        ]
      });
    }

    // Ruft die renderMarkdown-Funktion beim Laden der Seite und bei Änderungen der Eingabe auf
    renderMarkdown();
    document.getElementById('markdownInput').addEventListener('input', renderMarkdown);
  </script>
</body>
</html>
```

### **Erklärung des Codes:**

1. **Markdown-Parsing:**
   - Die `marked.js`-Bibliothek wird verwendet, um die eingegebenen Markdown-Daten (geschrieben in der `<textarea>`) in HTML umzuwandeln. Die Markdown-Syntax wird verarbeitet und in den Container `<div id="markdownOutput"></div>` umgewandelt.

2. **Mathematik-Rendering:**
   - Die LaTeX-Gleichungen im Markdown (inline `\( ... \)` und block `\[ ... \]`) werden mit der `renderMathInElement()`-Funktion von **KaTeX** gerendert.
   - **KaTeX** sucht nach `\( ... \)` für inline Mathematik und `\[ ... \]` für Block-Mathematik im HTML-Inhalt und rendert sie automatisch.

3. **Interaktiver Markdown-Editor:**
   - Während der Benutzer in die `<textarea>` tippt, wird die `renderMarkdown`-Funktion aufgerufen, um den Inhalt dynamisch zu aktualisieren, den Markdown zu parsen und die LaTeX-Formeln zu rendern.

---

### **Schritt 3: Anpassung für verschiedene Frontend-Frameworks**

Sie können diese Lösung an jedes Frontend-Framework wie **React**, **Vue** oder **Angular** anpassen. Hier ist beispielsweise eine **React**-Implementierung für Echtzeit-Markdown + LaTeX-Rendering:

#### **React-Beispiel**

1. **Installieren Sie KaTeX und marked via npm:**

```bash
npm install katex marked
```

2. **React-Komponente für Markdown + Mathematik-Rendering:**

```jsx
import React, { useState, useEffect } from 'react';
import marked from 'marked';
import katex from 'katex';
import 'katex/dist/katex.min.css';

const MarkdownEditor = () => {
  const [markdown, setMarkdown] = useState('');

  useEffect(() => {
    // Rendert mathematische Formeln mit KaTeX, nachdem die Komponente gemountet wurde
    renderMath();
  }, [markdown]);

  const renderMath = () => {
    const renderedHTML = marked(markdown);
    document.getElementById('markdownOutput').innerHTML = renderedHTML;

    // Rendert LaTeX-Matheformeln mit KaTeX
    katex.renderMathInElement(document.getElementById('markdownOutput'), {
      delimiters: [
        { left: "\\(", right: "\\)", display: false }, // inline math
        { left: "\\[", right: "\\]", display: true }   // block math
      ]
    });
  };

  return (
    <div>
      <h1>Markdown + Math Rendering</h1>
      <textarea
        value={markdown}
        onChange={(e) => setMarkdown(e.target.value)}
        rows="10"
        cols="50"
      />
      <hr />
      <div id="markdownOutput"></div>
    </div>
  );
};

export default MarkdownEditor;
```

In der React-Version verwenden wir die `marked`-Bibliothek, um den Markdown-Text in HTML umzuwandeln, und die `renderMathInElement()`-Funktion von KaTeX, um alle LaTeX-Matheformeln im HTML-Inhalt zu verarbeiten und darzustellen.

---

### **Zusammenfassung**
- Verwenden Sie einen **Markdown-Parser** (wie `marked.js`), um die Markdown-Syntax in HTML umzuwandeln.
- Verwenden Sie **MathJax** oder **KaTeX**, um LaTeX-Matheausdrücke, die in den Markdown-Inhalt eingebettet sind, darzustellen.
- Kombinieren Sie beides, indem Sie Markdown zu HTML rendern und mathematische Formeln dynamisch mit KaTeX/MathJax verarbeiten.

Dieser Ansatz ermöglicht es Benutzern, Markdown-Inhalte mit mathematischen Gleichungen in Echtzeit zu schreiben und in der Vorschau anzuzeigen, was perfekt für Anwendungen wie Blog-Editoren, Wissensdatenbanken oder Bildungstools ist!