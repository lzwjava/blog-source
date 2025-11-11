---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von KaTeX in Jekyll
translated: true
type: note
---

Um KaTeX anstelle von MathJax in Jekyll mit Ihrem aktuellen Setup zu verwenden, müssen Sie die MathJax-Skripte durch KaTeX ersetzen und Ihre Jekyll-Konfiguration anpassen. KaTeX ist schneller und leichter als MathJax, erfordert jedoch einen anderen Ansatz, da es nicht alle Funktionen von MathJax unterstützt (z. B. ist die automatische Gleichungsnummerierung manueller). Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung, um in Ihrer Jekyll-Site zu KaTeX zu wechseln:

### 1. Aktualisieren Sie Ihre Jekyll-Konfiguration
Ändern Sie Ihre `_config.yml` so, dass KaTeX als Math-Engine für Kramdown verwendet wird. Aktualisieren Sie den `kramdown`-Abschnitt wie folgt:

```yaml
kramdown:
  math_engine: katex
  input: GFM
  syntax_highlighter: rouge
```

Dies weist Kramdown an, LaTeX-Mathematikausdrücke mit KaTeX anstelle von MathJax zu rendern.

### 2. Binden Sie KaTeX in Ihr HTML ein
Entfernen Sie die MathJax-Skripte aus Ihrem HTML und ersetzen Sie sie durch KaTeX. Sie können KaTeX über einen CDN einbinden. Fügen Sie Folgendes zum `<head>`-Abschnitt Ihrer Jekyll-Layout-Datei (z. B. `_layouts/default.html`) hinzu:

```html
<!-- KaTeX CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" integrity="sha384-nB0miv6/jRmo5SLY8cTjmnkA3wC7o1L0jOey4Cki5N3kdjdPD/mW59G1Qsxa8c3y" crossorigin="anonymous">

<!-- KaTeX JS -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" integrity="sha384-7zkKLzPD3M4y9W8FWsN4Z0yO5eLu8qUn0QHY6hZ2r3fDzqjk0McYc3vJrmE2h6cZ" crossorigin="anonymous"></script>

<!-- Auto-render extension (optional, für automatisches Rendern von Mathematik) -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" integrity="sha384-43gviWU0YVjaDtb/GhzOouOXtZMP/7XUzwPTL0xF3iS9Ho94fSc31UyUyIDgWvB4" crossorigin="anonymous"></script>

<!-- Auto-render configuration -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: "$$", right: "$$", display: true}, // Block-Mathematik
        {left: "\\[", right: "\\]", display: true}, // Block-Mathematik
        {left: "\\(", right: "\\)", display: false}, // Inline-Mathematik
        {left: "$", right: "$", display: false} // Inline-Mathematik
      ],
      throwOnError: false
    });
  });
</script>
```

### 3. Entfernen Sie die MathJax-Konfiguration
Löschen Sie den MathJax-bezogenen Code aus Ihrer Layout-Datei, einschließlich des `<script type="text/x-mathjax-config">`-Blocks und des MathJax-CDN-Skripts. KaTeX verwendet keine Konfiguration wie MathJaxs `tex2jax`, und das obige Auto-Render-Skript übernimmt eine ähnliche Funktionalität.

### 4. Schreiben Sie Mathematik in Ihr Markdown
Mit konfiguriertem KaTeX und Kramdown können Sie LaTeX-Mathematik in Ihren Markdown-Dateien mit denselben Begrenzungszeichen wie zuvor schreiben:

- **Inline-Mathematik**: Verwenden Sie `$...$` oder `\(...\)` (z. B. `$E=mc^2$` oder `\(E=mc^2\)`).
- **Display-Mathematik**: Verwenden Sie `$$...$$` oder `\[...\]` (z. B. `$$E=mc^2$$` oder `\[E=mc^2\]`).

Zum Beispiel:

```markdown
Inline-Mathematik: $E=mc^2$ oder \(E=mc^2\).

Display-Mathematik:
$$E=mc^2$$

oder

\[E=mc^2\]
```

Kramdown mit der KaTeX-Math-Engine verarbeitet diese zu HTML, das KaTeX rendert.

### 5. Hinweise zu KaTeX vs. MathJax
- **Automatische Gleichungsnummerierung**: KaTeX unterstützt keine automatische Gleichungsnummerierung wie MathJaxs `autoNumber: "AMS"`. Wenn Sie Gleichungsnummern benötigen, müssen Sie diese manuell mit `\tag{}` in Ihrem LaTeX-Code hinzufügen (z. B. `$$E=mc^2 \tag{1}$$`).
- **Leistung**: KaTeX ist deutlich schneller als MathJax, was ideal für statische Sites wie Jekyll ist.
- **Funktionsumfang**: KaTeX unterstützt weniger LaTeX-Befehle als MathJax. Überprüfen Sie die [KaTeX supported functions](https://katex.org/docs/supported.html), um sicherzustellen, dass Ihre Mathematikausdrücke kompatibel sind.
- **Rendering**: Das Auto-Render-Skript oben imitiert das Verhalten von MathJax, indem es automatisch Mathematikausdrücke innerhalb der angegebenen Begrenzungszeichen rendert. Passen Sie das `delimiters`-Array im Skript an, wenn Sie die Begrenzungszeichen ändern oder einschränken möchten.

### 6. Testen Sie Ihr Setup
Führen Sie Ihre Jekyll-Site lokal aus (`jekyll serve`) und verifizieren Sie, dass Mathematikausdrücke korrekt gerendert werden. Wenn Sie auf Probleme stoßen:
- Überprüfen Sie die Browser-Konsole auf KaTeX-bezogene Fehler.
- Stellen Sie sicher, dass die KaTeX-CDN-URLs aktuell sind (die oben verwendeten sind Version 0.16.11, die neueste zum Zeitpunkt meines Wissensstands).
- Bestätigen Sie, dass Ihre Markdown-Dateien eine gültige, KaTeX-kompatible LaTeX-Syntax verwenden.

### 7. Optional: Lokale KaTeX-Dateien
Wenn Sie KaTeX-Dateien lokal hosten möchten, um CDN-Abhängigkeiten zu vermeiden:
1. Laden Sie `katex.min.css`, `katex.min.js` und `auto-render.min.js` von den [KaTeX GitHub releases](https://github.com/KaTeX/KaTeX/releases) herunter.
2. Platzieren Sie sie in Ihrem Jekyll-Assets-Ordner (z. B. `assets/katex/`).
3. Aktualisieren Sie die `<link>`- und `<script>`-Tags, damit sie auf Ihre lokalen Dateien verweisen (z. B. `/assets/katex/katex.min.css`).

### 8. Fehlerbehebung
- **Mathematik wird nicht gerendert**: Stellen Sie sicher, dass die KaTeX-Skripte korrekt geladen werden und `kramdown.math_engine` auf `katex` gesetzt ist.
- **Probleme mit Begrenzungszeichen**: Verifizieren Sie, dass Ihre Begrenzungszeichen im Auto-Render-Skript mit denen in Ihrem Markdown übereinstimmen.
- **Nicht unterstützte Befehle**: Wenn ein LaTeX-Befehl fehlschlägt, überprüfen Sie die KaTeX-Dokumentation auf unterstützte Befehle oder schreiben Sie den Ausdruck um.

Wenn Sie spezielle Hilfe mit einem bestimmten Mathematikausdruck oder einer Konfiguration benötigen, teilen Sie die Details mit, und ich kann maßgeschneiderte Anleitung geben!