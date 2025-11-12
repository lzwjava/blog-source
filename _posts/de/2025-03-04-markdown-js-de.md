---
audio: false
generated: true
lang: de
layout: post
title: JavaScript-Bibliothek für Markdown
translated: true
type: note
---

Es scheint, als würden Sie nach der Verwendung der `marked`-Bibliothek, Version `^0.3.6`, fragen, einer JavaScript-Bibliothek zum Parsen von Markdown-Text und Konvertieren in HTML. Da Sie eine spezifische Version mit der Notation `^0.3.6` referenzieren (wahrscheinlich aus einer `package.json`-Datei in einem Node.js-Projekt), werde ich Sie durch die Verwendung dieser älteren Version von `marked` führen. Beachten Sie, dass Version `0.3.6` ziemlich alt ist (veröffentlicht um 2016) und sich die Bibliothek seitdem erheblich weiterentwickelt hat. Ich werde mich jedoch an das halten, was für diese Version funktioniert.

### Schritt 1: Installation
Wenn Sie in einer Node.js-Umgebung arbeiten, können Sie `marked` Version `0.3.6` mit npm installieren:

```bash
npm install marked@0.3.6
```

Das `^0.3.6` in einer `package.json` bedeutet, dass `0.3.6` oder kompatible Patch-Updates (z.B. `0.3.7`) installiert werden, aber zur Klarheit fixiert der Befehl oben die Version auf genau `0.3.6`.

### Schritt 2: Grundlegende Verwendung
So verwenden Sie `marked` Version `0.3.6` in verschiedenen Umgebungen:

#### In Node.js
1. **Bibliothek einbinden**:
   Erstellen Sie eine Datei (z.B. `index.js`) und fügen Sie Folgendes hinzu:

   ```javascript
   var marked = require('marked');
   ```

2. **Markdown in HTML konvertieren**:
   Verwenden Sie die Funktion `marked()`, indem Sie ihr einen Markdown-String übergeben. Zum Beispiel:

   ```javascript
   var markdownString = '# Hello World\nDies ist **fetter** Text.';
   var html = marked(markdownString);
   console.log(html);
   ```

   **Ausgabe**:
   ```html
   <h1>Hello World</h1>
   <p>Dies ist <strong>fetter</strong> Text.</p>
   ```

#### Im Browser
1. **Bibliothek einbinden**:
   Sie können eine CDN verwenden oder `marked@0.3.6` herunterladen und es über ein `<script>`-Tag einbinden. Zum Beispiel, unter Verwendung eines historischen CDN-Links (falls verfügbar) oder einer lokalen Datei:

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **In JavaScript verwenden**:
   Nachdem das Skript eingebunden wurde, ist `marked` global verfügbar:

   ```html
   <script>
     var markdownString = '# Hello World\nDies ist **fetter** Text.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### Schritt 3: Optionen (für Version 0.3.6)
Version `0.3.6` unterstützt einige Anpassungsoptionen. Sie können ein Options-Objekt als zweites Argument an `marked()` übergeben. Hier ist ein Beispiel:

```javascript
var markdownString = '# Hello\nDies ist *Text* mit `Code`.';
var html = marked(markdownString, {
  gfm: true,         // GitHub Flavored Markdown aktivieren
  tables: true,      // GFM-Tabellen aktivieren
  breaks: false,     // Wenn true, fügt <br> bei einzelnen Zeilenumbrüchen hinzu
  pedantic: false,   // Wenn true, folgt es der strikten Markdown-Spezifikation
  sanitize: false,   // Wenn true, entfernt es HTML-Tags aus Sicherheitsgründen
  smartLists: true,  // Verbessert die Listen-Darstellung
  smartypants: false // Wenn true, verwendet es "smarte" Typografie (z.B. geschweifte Anführungszeichen)
});
console.log(html);
```

### Wichtige Funktionen in 0.3.6
- **Grundlegendes Markdown**: Unterstützt Überschriften (`#`), Fett (`**`), Kursiv (`*`), Listen, Code-Blöcke (```), usw.
- **GFM-Unterstützung**: GitHub Flavored Markdown (wie Tabellen und Task-Listen) ist verfügbar, wenn `gfm: true` gesetzt ist.
- **Keine Renderer-Anpassung**: Im Gegensatz zu neueren Versionen unterstützt `0.3.6` keine benutzerdefinierten Renderer, Sie sind also auf die Standardausgabe beschränkt.

### Beispiel mit mehr Markdown
Hier ist ein umfassenderes Beispiel in Node.js:

```javascript
var marked = require('marked');

var markdown = `
# Mein Titel
## Untertitel

- Punkt 1
- Punkt 2

\`\`\`
console.log("Hello");
\`\`\`

| Name  | Alter |
|-------|-------|
| Alice | 25    |
| Bob   | 30    |
`;

var html = marked(markdown, { gfm: true, tables: true });
console.log(html);
```

**Ausgabe**:
```html
<h1>Mein Titel</h1>
<h2>Untertitel</h2>
<ul>
<li>Punkt 1</li>
<li>Punkt 2</li>
</ul>
<pre><code>console.log("Hello");
</code></pre>
<table>
<thead>
<tr>
<th>Name</th>
<th>Alter</th>
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
- **Sanitisierung**: Wenn Sie Benutzereingaben rendern, setzen Sie `sanitize: true`, um rohes HTML aus Sicherheitsgründen zu entfernen (z.B. `<script>`-Tags). Dies ist in `0.3.6` jedoch grundlegend und nicht so robust wie moderne Alternativen.
- **Einschränkungen**: Dieser Version fehlen Funktionen, die in späteren Versionen hinzugefügt wurden (z.B. asynchrones Parsen, benutzerdefinierte Tokenizer). Wenn Sie mehr benötigen, sollten Sie ein Upgrade auf eine neuere Version wie `5.x` in Betracht ziehen.
- **Debugging**: Wenn es nicht funktioniert, stellen Sie sicher, dass die Bibliothek korrekt geladen ist, und überprüfen Sie die Markdown-Syntax.