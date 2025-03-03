---
audio: false
generated: true
lang: de
layout: post
title: GitHubs Markdown-Styling
translated: true
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass zur Verwendung des "github-markdown-css" npm-Pakets zunächst mit `npm install github-markdown-css` installiert wird.
- Forschungen deuten darauf hin, dass Sie dann die CSS-Datei in Ihr Projekt importieren und Ihren Markdown-Inhalt in ein div mit der Klasse "markdown-body" einbetten.
- Die Beweise sprechen dafür, optionale Breite und Einrückung anzupassen, um GitHubs Stil zu entsprechen, und sicherzustellen, dass ein DOctype vorhanden ist, um Styling-Probleme zu vermeiden.

### Installation
Beginnen Sie mit der Installation des Pakets mit npm in Ihrem Projektverzeichnis:
- Führen Sie `npm install github-markdown-css` aus, um es zu Ihren Abhängigkeiten hinzuzufügen.

### Verwendung
Nach der Installation integrieren Sie das CSS in Ihr Projekt:
- Importieren Sie die CSS-Datei, z. B. in JavaScript/React mit `import 'github-markdown-css';`.
- Betten Sie Ihren gerenderten Markdown-Inhalt in ein `<div class="markdown-body">...</div>` ein, um die Stile anzuwenden.
- Optional können Sie CSS für Breite und Einrückung hinzufügen, um GitHubs Aussehen nachzuahmen:
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
- Stellen Sie sicher, dass Ihr HTML einen DOctype enthält (z. B. `<!DOCTYPE html>`), um Probleme mit dem Quirks-Modus zu vermeiden, die das Styling beeinflussen könnten.

### Unerwartetes Detail
Sie könnten nicht erwarten, dass das Paket auch die Erstellung benutzerdefinierter CSS über ein verwandtes Paket, [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css), unterstützt, falls Sie angepasste Stile benötigen.

---

### Umfragehinweis: Umfassender Leitfaden zur Verwendung des github-markdown-css npm-Pakets

Dieser detaillierte Leitfaden untersucht die Verwendung des "github-markdown-css" npm-Pakets, das entwickelt wurde, um GitHubs Markdown-Stil in Webprojekten nachzuahmen. Er bietet einen Schritt-für-Schritt-Ansatz zur Installation und Integration sowie zusätzliche Überlegungen für die optimale Nutzung, insbesondere in verschiedenen Entwicklungsumgebungen wie React oder einfachem HTML. Die Informationen stammen aus der offiziellen Paketdokumentation, GitHub-Repositories und verwandten Webressourcen, was ein umfassendes Verständnis für Entwickler aller Niveaus gewährleistet.

#### Hintergrund und Zweck
Das "github-markdown-css"-Paket, das von [sindresorhus](https://github.com/sindresorhus) gepflegt wird, bietet einen minimalen Satz von CSS, um GitHubs Markdown-Rendering-Stil nachzuahmen. Dies ist besonders nützlich für Entwickler, die ihren Markdown-Inhalt, wie Dokumentationen oder Blogbeiträge, konsistent mit GitHubs vertrautem und sauberem Aussehen darstellen möchten. Das Paket wird weit verbreitet verwendet, mit über 1.168 anderen Projekten im npm-Register, was seine Beliebtheit und Zuverlässigkeit als von kürzlichen Updates zeigt.

#### Installationsprozess
Um zu beginnen, müssen Sie das Paket über npm, den Node.js-Paketmanager, installieren. Der Befehl ist einfach:
- Führen Sie `npm install github-markdown-css` in Ihrem Projektverzeichnis aus. Dies fügt das Paket Ihrem `node_modules`-Ordner hinzu und aktualisiert Ihre `package.json` mit der Abhängigkeit.

Die neueste Version des Pakets, Stand der letzten Überprüfung, ist 5.8.1, veröffentlicht vor etwa drei Monaten, was auf eine aktive Wartung und Updates hinweist. Dies stellt die Kompatibilität mit modernen Webentwicklungsmethoden und -frameworks sicher.

#### Integration und Verwendung
Nach der Installation ist der nächste Schritt die Integration des CSS in Ihr Projekt. Das Paket bietet eine Datei namens `github-markdown.css`, die Sie je nach Projektaufbau importieren können:

- **Für JavaScript/Moderne Frameworks (z. B. React, Vue):**
  - Verwenden Sie eine Import-Anweisung in Ihren JavaScript- oder TypeScript-Dateien, wie z. B. `import 'github-markdown-css';`. Dies funktioniert gut mit Bundlern wie Webpack oder Vite, die CSS-Imports nahtlos verarbeiten.
  - In React könnten Sie Beispiele sehen, in denen Entwickler es in einer Komponentendatei importieren, um sicherzustellen, dass die Stile global oder nach Bedarf eingeschränkt verfügbar sind.

- **Für einfaches HTML:**
  - Verknüpfen Sie die CSS-Datei direkt im Kopfbereich Ihres HTML:
    ```html
    <link rel="stylesheet" href="node_modules/github-markdown-css/github-markdown.css">
    ```
  - Beachten Sie, dass der Pfad je nach Projektstruktur variieren kann; stellen Sie sicher, dass der relative Pfad korrekt auf den `node_modules`-Ordner zeigt.

Nach dem Import wenden Sie die Stile an, indem Sie Ihren gerenderten Markdown-Inhalt in ein `<div>` mit der Klasse "markdown-body" einbetten. Zum Beispiel:
```html
<div class="markdown-body">
  <h1>Einhörner</h1>
  <p>Alles über Einhörner</p>
</div>
```
Diese Klasse ist entscheidend, da das CSS Elemente innerhalb von `.markdown-body` ansteuert, um GitHub-ähnliche Stile anzuwenden, einschließlich Typografie, Codeblöcke, Tabellen und mehr.

#### Styling-Betrachtungen
Um das Aussehen von GitHubs Markdown vollständig nachzuahmen, sollten Sie die Breite und Einrückung für die `.markdown-body`-Klasse festlegen. Die Dokumentation schlägt vor:
- Eine maximale Breite von 980px mit 45px Einrückung auf größeren Bildschirmen und 15px Einrückung auf mobilen Geräten (Bildschirme ≤ 767px).
- Dies können Sie mit folgendem CSS erreichen:
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
Dies stellt die Anpassungsfähigkeit sicher und stimmt mit GitHubs Design überein, was die Lesbarkeit und Benutzererfahrung verbessert.

#### Technische Hinweise und Best Practices
- **DOctype-Anforderung:** Die Dokumentation hebt potenzielle Styling-Probleme hervor, wie z. B. Tabellen im Dunklem Modus, die falsch gerendert werden, wenn der Browser in den Quirks-Modus wechselt. Um dies zu verhindern, fügen Sie immer einen DOctype an den Anfang Ihres HTML ein, wie z. B. `<!DOCTYPE html>`. Dies stellt eine standardskonforme Rendering und vermeidet unerwartetes Verhalten sicher.
- **Markdown-Analyse:** Während das Paket CSS bereitstellt, analysiert es kein Markdown zu HTML. Sie benötigen einen Markdown-Analyser wie [marked.js](https://marked.js.org/) oder [react-markdown](https://github.com/remarkjs/react-markdown) für React-Projekte, um Markdown-Text in HTML umzuwandeln, der dann mit diesem CSS gestylt werden kann.
- **Erstellung benutzerdefinierter CSS:** Für fortgeschrittene Benutzer ermöglicht das verwandte Paket [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) die Erstellung benutzerdefinierter CSS, was für spezifische Themen oder Anpassungen nützlich sein könnte. Dies ist ein unerwartetes Detail für diejenigen, die annehmen könnten, dass das Paket nur für die direkte Verwendung gedacht ist.

#### Verwendung in spezifischen Kontexten
- **React-Projekte:** In React ist es üblich, `github-markdown-css` mit `react-markdown` zu kombinieren. Nach der Installation beider Pakete importieren Sie das CSS und verwenden die Komponente:
  ```javascript
  import React from 'react';
  import ReactMarkdown from 'react-markdown';
  import 'github-markdown-css';

  const MarkdownComponent = () => (
    <div className="markdown-body">
      <ReactMarkdown># Hallo, Welt!</ReactMarkdown>
    </div>
  );
  ```
  Stellen Sie sicher, dass Sie auch das Breite- und Einrückungs-CSS wie oben gezeigt für das vollständige GitHub-Styling festlegen.

- **Einfaches HTML mit CDN:** Für schnelle Prototypen können Sie eine CDN-Version verwenden, die auf [cdnjs](https://cdnjs.com/libraries/github-markdown-css) verfügbar ist, indem Sie direkt verknüpfen:
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css">
  ```
  Dann wenden Sie die `.markdown-body`-Klasse wie zuvor an.

#### Potenzielle Probleme und Lösungen
- **Styling-Konflikte:** Wenn Ihr Projekt andere CSS-Frameworks (z. B. Tailwind, Bootstrap) verwendet, stellen Sie sicher, dass keine Spezifitätskonflikte auftreten. Die `.markdown-body`-Klasse sollte die meisten Stile überschreiben, aber testen Sie gründlich.
- **Dunkler Modus:** Das Paket unterstützt den dunklen Modus, aber stellen Sie sicher, dass Ihr Markdown-Analyser und Ihre Projektkonfiguration das Umschalten des Themas korrekt handhaben, insbesondere für Codeblöcke und Tabellen.
- **Browser-Kompatibilität:** Aufgrund der weit verbreiteten Verwendung des Pakets ist die Kompatibilität in der Regel gut, aber testen Sie immer in den wichtigsten Browsern (Chrome, Firefox, Safari), um eine konsistente Darstellung sicherzustellen.

#### Vergleichende Analyse
Im Vergleich zu anderen Markdown-CSS-Optionen wie [Markdown CSS](https://markdowncss.github.io/) hebt sich "github-markdown-css" durch seine direkte Nachahmung von GitHubs Stil hervor, was es ideal für Dokumentationen macht, die GitHubs Aussehen spiegeln. Es bietet jedoch keine eingebauten Themenoptionen ohne zusätzliche Anpassungen, im Gegensatz zu einigen Alternativen, die mehrere Themen direkt aus der Box bieten.

#### Tabelle: Wichtige Funktionen und Überlegungen

| Funktion                  | Beschreibung                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Installationsbefehl      | `npm install github-markdown-css`                                           |
| CSS-Import-Methode        | `import 'github-markdown-css';` oder `<link>` in HTML                         |
| Erforderliche Klasse      | `.markdown-body` für die Anwendung des Stylings                                    |
| Breite und Einrückung     | Max 980px, 45px Einrückung (Desktop); 15px Einrückung (Mobil ≤ 767px)            |
| DOctype-Anforderung      | Wichtig, um Quirks-Modus zu vermeiden und eine korrekte Darstellung sicherzustellen                  |
| Erstellung benutzerdefinierter CSS | Möglich über [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) |
| Kompatibilität           | Funktioniert mit Markdown-Analysern wie marked.js, react-markdown; breite Browser-Unterstützung |

#### Schlussfolgerung
Die Verwendung von "github-markdown-css" ist für Entwickler, die GitHubs Markdown-Stil nachahmen möchten, einfach. Durch die Befolgung der Installations- und Integrationsschritte und die Berücksichtigung zusätzlicher Styling- und technischer Hinweise können Sie ein konsistentes und professionelles Aussehen für Ihren Markdown-Inhalt erreichen. Für fortgeschrittene Anpassungen erkunden Sie das Erstellungs-Paket und testen Sie immer auf Kompatibilität und Rendering-Probleme, insbesondere in komplexen Projekten.

#### Wichtige Zitate
- [github-markdown-css npm-Paket-Seite](https://www.npmjs.com/package/github-markdown-css)
- [Das minimale CSS, um GitHub Markdown-Stil nachzuahmen GitHub-Repo](https://github.com/sindresorhus/github-markdown-css)
- [GitHub Markdown CSS Demo-Seite](https://sindresorhus.com/github-markdown-css/)
- [Erstellen Sie das CSS für github-markdown-css npm-Paket](https://www.npmjs.com/package/generate-github-markdown-css)
- [github-markdown-css CDN von cdnjs](https://cdnjs.com/libraries/github-markdown-css)