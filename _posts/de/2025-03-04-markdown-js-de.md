---
audio: false
generated: true
lang: de
layout: post
title: JavaScript-Bibliothek für Markdown
translated: true
---

Es scheint, dass Sie sich nach der Verwendung der `marked`-Bibliothek, Version `^0.3.6`, erkundigen, die eine JavaScript-Bibliothek zum Parsen von Markdown-Text und Konvertieren in HTML ist. Da Sie eine spezifische Version mit der `^0.3.6`-Notation (wahrscheinlich aus einer `package.json`-Datei in einem Node.js-Projekt) angeben, werde ich Sie durch die Verwendung dieser älteren Version führen. Beachten Sie, dass Version `0.3.6` ziemlich alt ist (veröffentlicht um 2016) und die Bibliothek seitdem erheblich weiterentwickelt wurde. Ich werde jedoch bei dem bleiben, was für diese Version funktioniert.

### Schritt 1: Installation
Wenn Sie in einer Node.js-Umgebung arbeiten, können Sie `marked` Version `0.3.6` mit npm installieren:

```bash
npm install marked@0.3.6
```

Das `^0.3.6` in einer `package.json` bedeutet, dass es `0.3.6` oder kompatible Patch-Updates (z.B. `0.3.7`) installiert, aber für Klarheit installiert der obige Befehl genau `0.3.6`.

### Schritt 2: Grundlegende Verwendung
Hier ist, wie Sie `marked` Version `0.3.6` in verschiedenen Umgebungen verwenden:

#### In Node.js
1. **Bibliothek einbinden**:
   Erstellen Sie eine Datei (z.B. `index.js`) und fügen Sie Folgendes hinzu:

   ```javascript
   var marked = require('marked');
   ```

2. **Markdown in HTML umwandeln**:
   Verwenden Sie die `marked()`-Funktion, indem Sie eine Markdown-Zeichenkette an sie übergeben. Zum Beispiel:

   ```javascript
   var markdownString = '# Hello World\nThis is **bold** text.';
   var html = marked(markdownString);
   console.log(html);
   ```

   **Ausgabe**:
   ```html
   <h1>Hello World</h1>
   <p>This is <strong>bold</strong> text.</p>
   ```

#### Im Browser
1. **Bibliothek einbinden**:
   Sie können einen CDN verwenden oder `marked@0.3.6` herunterladen und über ein `<script>`-Tag einbinden. Zum Beispiel, mit einem historischen CDN-Link (falls verfügbar) oder einer lokalen Datei:

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **Verwendung in JavaScript**:
   Nach dem Einbinden des Skripts steht `marked` global zur Verfügung:

   ```html
   <script>
     var markdownString = '# Hello World\nThis is **bold** text.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### Schritt 3: Optionen (für Version 0.3.6)
Version `0.3.6` unterstützt einige Anpassungsoptionen. Sie können ein Options-Objekt als zweites Argument an `marked()` übergeben. Hier ist ein Beispiel:

```javascript
var markdownString = '# Hello\nThis is *text* with `code`.';
var html = marked(markdownString, {
  gfm: true,         // GitHub Flavored Markdown aktivieren
  tables: true,      // GFM-Tabellen aktivieren
  breaks: false,     // Wenn true, fügt <br> bei einzelnen Zeilenumbrüchen ein
  pedantic: false,   // Wenn true, folgt strikter Markdown-Spezifikation
  sanitize: false,   // Wenn true, entfernt HTML-Tags zur Sicherheit
  smartLists: true,  // Verbessert die Listenanzeige
  smartypants: false // Wenn true, verwendet "smart" Typografie (z.B. geschweifte Anführungszeichen)
});
console.log(html);
```

### Wichtige Merkmale in 0.3.6
- **Grundlegendes Markdown**: Unterstützt Überschriften (`#`), Fett (`**`), Kursiv (`*`), Listen, Codeblöcke (```), usw.
- **GFM-Unterstützung**: GitHub Flavored Markdown (wie Tabellen und Aufgabenlisten) ist verfügbar, wenn `gfm: true` gesetzt ist.
- **Keine Renderer-Anpassung**: Im Gegensatz zu neueren Versionen unterstützt `0.3.6` keine benutzerdefinierten Renderer, sodass Sie auf die Standardausgabe beschränkt sind.

### Beispiel mit mehr Markdown
Hier ist ein vollständigeres Beispiel in Node.js:

```javascript
var marked = require('marked');

var markdown = `
# My Title
## Subtitle

- Item 1
- Item 2

\`\`\`
console.log("Hello");
\`\`\`

| Name  | Age |
|-------|-----|
| Alice | 25  |
| Bob   | 30  |
`;

var html = marked(markdown, { gfm: true, tables: true });
console.log(html);
```

**Ausgabe**:
```html
<h1>My Title</h1>
<h2>Subtitle</h2>
<ul>
<li>Item 1</li>
<li>Item 2</li>
</ul>
<pre><code>console.log("Hello");
</code></pre>
<table>
<thead>
<tr>
<th>Name</th>
<th>Age</th>
</tr>
</thead>
<tbody>
<tr>
<td>Alice</td>
<td>25</td>
</tr>
<tr>
<td>Bob</td>
<td>30</td>
</tr>
</tbody>
</table>
```

### Hinweise
- **Sanitisierung**: Wenn Sie Benutzereingaben rendern, setzen Sie `sanitize: true`, um rohe HTML-Tags zur Sicherheit zu entfernen (z.B. `<script>`-Tags). Dies ist jedoch in `0.3.6` grundlegend und nicht so robust wie moderne Alternativen.
- **Einschränkungen**: Diese Version fehlen Funktionen, die in späteren Veröffentlichungen hinzugefügt wurden (z.B. asynchrones Parsen, benutzerdefinierte Tokenizer), sodass Sie, wenn Sie mehr benötigen, ein Upgrade auf eine neuere Version wie `5.x` in Betracht ziehen sollten.
- **Fehlerbehebung**: Wenn es nicht funktioniert, stellen Sie sicher, dass die Bibliothek korrekt geladen wird und überprüfen Sie die Markdown-Syntax.