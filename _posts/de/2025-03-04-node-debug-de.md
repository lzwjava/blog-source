---
audio: false
generated: true
lang: de
layout: post
title: Debugging in Node.js mit dem Debug-Paket
translated: true
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass "debug in npm" sich auf die Verwendung des "debug"-Pakets für das Protokollieren in Node.js-Projekten bezieht, die von npm verwaltet werden.
- Die Forschung deutet darauf hin, das Paket mit `npm install debug` zu installieren und es dann im Code mit einem Namensraum wie `require('debug')('myapp:component')` zu verwenden.
- Die Beweise sprechen dafür, dass die Debug-Ausgabe durch Setzen der `DEBUG`-Umgebungsvariable aktiviert wird, wie z.B. `DEBUG=myapp:component npm run start`.

### Installation und Verwendung des Debug-Pakets
Um das "debug"-Paket in Ihrem Node.js-Projekt zu verwenden, installieren Sie es zuerst mit npm:
- Führen Sie `npm install debug` im Projektverzeichnis aus.

Dann erfordern Sie in Ihrem JavaScript-Code das Paket und erstellen Sie eine Debug-Instanz mit einem Namensraum:
- Beispiel: `const debug = require('debug')('myapp:component'); debug('some message');`.

### Aktivieren der Debug-Ausgabe
Um die Debug-Nachrichten zu sehen, setzen Sie die `DEBUG`-Umgebungsvariable beim Ausführen Ihrer Anwendung:
- Beispielsweise führen Sie `DEBUG=myapp:component node app.js` oder `DEBUG=myapp:component npm run start` aus, wenn Sie ein npm-Skript verwenden.

### Steuerung der Namensräume
Sie können steuern, welche Debug-Nachrichten angezeigt werden, indem Sie Wildcards oder Ausschlüsse verwenden:
- Aktivieren Sie mehrere Namensräume mit `DEBUG=myapp:* node app.js`.
- Schließen Sie spezifische Namensräume mit `DEBUG=*,-myapp:exclude node app.js` aus.

---

### Umfragehinweis: Detaillierte Untersuchung der Verwendung von Debug in npm

Dieser Abschnitt bietet eine umfassende Übersicht über die Verwendung des "debug"-Pakets innerhalb von Node.js-Projekten, die von npm verwaltet werden, basierend auf verfügbaren Dokumentationen und Ressourcen. Der Fokus liegt auf der praktischen Implementierung, fortgeschrittenen Funktionen und Überlegungen für Entwickler, um ein gründliches Verständnis sowohl für Anfänger als auch für erfahrene Benutzer zu gewährleisten.

#### Einführung in Debug im npm-Kontext
Die Phrase "debug in npm" bezieht sich wahrscheinlich auf die Nutzung des "debug"-Pakets, eines leichtgewichtigen Debugging-Tools für Node.js- und Browserumgebungen, innerhalb von Projekten, die von npm (Node Package Manager) verwaltet werden. Angesichts der Prominenz des "debug"-Pakets in Suchergebnissen und seiner Relevanz für die Node.js-Entwicklung passt diese Interpretation zu den häufigen Entwicklerbedürfnissen für Protokollierung und Debugging in npm-verwalteten Projekten. Das Paket, derzeit in Version 4.4.0, wird weit verbreitet verwendet, mit über 55.746 anderen Projekten im npm-Register, was seinen Standardstatus im Ökosystem unterstreicht.

#### Installation und grundlegende Verwendung
Um zu beginnen, installieren Sie das "debug"-Paket mit npm:
- Befehl: `npm install debug`
- Dies fügt das Paket zu den `node_modules` Ihres Projekts hinzu und aktualisiert `package.json`.

In Ihrem JavaScript-Code erfordern Sie das Paket und initialisieren es mit einem Namensraum, um Debug-Nachrichten zu kategorisieren:
- Beispiel: `const debug = require('debug')('myapp:component');`.
- Verwenden Sie die Debug-Instanz, um Nachrichten zu protokollieren: `debug('some message');`.
- Der Namensraum, wie z.B. 'myapp:component', hilft, die Quelle der Nachrichten zu identifizieren, was das Filtern von Protokollen in großen Anwendungen erleichtert.

Um diese Debug-Nachrichten zu sehen, setzen Sie die `DEBUG`-Umgebungsvariable beim Ausführen Ihrer Anwendung:
- Beispiel: `DEBUG=myapp:component node app.js`.
- Wenn Ihre Anwendung über ein npm-Skript gestartet wird (z.B. `npm run start`), verwenden Sie: `DEBUG=myapp:component npm run start`.
- Diese Umgebungsvariable steuert, welche Namensräume aktiviert sind, und stellt sicher, dass selektives Debugging ohne Codeänderungen möglich ist.

#### Fortgeschrittene Funktionen und Konfiguration
Das "debug"-Paket bietet mehrere fortgeschrittene Funktionen für eine verbesserte Benutzerfreundlichkeit:

##### Steuerung des Namensraums und Wildcards
- Verwenden Sie Wildcards, um mehrere Namensräume zu aktivieren: `DEBUG=myapp:* node app.js` zeigt Debug-Nachrichten von allen Namensräumen an, die mit 'myapp:' beginnen.
- Schließen Sie spezifische Namensräume mit einem Minuszeichen aus: `DEBUG=*,-myapp:exclude node app.js` aktiviert alle Namensräume außer denen, die mit 'myapp:exclude' beginnen.
- Dieses selektive Debugging ist entscheidend, um sich auf spezifische Teile einer Anwendung zu konzentrieren, ohne von Protokollen überwältigt zu werden.

##### Farbcodierung und visuelle Analyse
- Die Debug-Ausgabe enthält eine Farbcodierung basierend auf Namensraumnamen, was die visuelle Analyse unterstützt.
- Farben sind standardmäßig aktiviert, wenn stderr ein TTY (Terminal) in Node.js ist, und können durch die Installation des `supports-color`-Pakets neben debug für eine breitere Farbpalette verbessert werden.
- In Browsern funktionieren Farben in WebKit-basierten Inspektoren, Firefox (Version 31 und höher) und Firebug, was die Lesbarkeit in Entwicklungstools verbessert.

##### Zeitunterschied und Leistungsanalysen
- Das Paket kann den Zeitunterschied zwischen Debug-Aufrufen anzeigen, vorangestellt mit "+NNNms", was für die Leistungsanalyse nützlich ist.
- Diese Funktion ist standardmäßig aktiviert und verwendet `Date#toISOString()`, wenn stdout kein TTY ist, was Konsistenz über verschiedene Umgebungen hinweg gewährleistet.

##### Umgebungsvariablen und Anpassung
Mehrere Umgebungsvariablen passen die Debug-Ausgabe an:
| Name             | Zweck                              |
|------------------|--------------------------------------|
| DEBUG            | Aktiviert/deaktiviert Namensräume          |
| DEBUG_HIDE_DATE  | Versteckt Datum in nicht-TTY-Ausgabe         |
| DEBUG_COLORS     | Erzwingt Farbverwendung in Ausgabe         |
| DEBUG_DEPTH      | Setzt Objektinspektions-Tiefe         |
| DEBUG_SHOW_HIDDEN| Zeigt versteckte Eigenschaften in Objekten   |

- Beispielsweise ermöglicht das Setzen von `DEBUG_DEPTH=5` eine tiefere Objektinspektion, was für komplexe Datenstrukturen nützlich ist.

##### Formatierer für benutzerdefinierte Ausgabe
Debug unterstützt benutzerdefinierte Formatierer für verschiedene Datentypen, was die Lesbarkeit der Protokolle verbessert:
| Formatter | Darstellung                      |
|-----------|-------------------------------------|
| %O        | Objekt schön drucken (mehrere Zeilen)|
| %o        | Objekt schön drucken (eine Zeile)   |
| %s        | Zeichenkette                              |
| %d        | Zahl (ganzzahlig/kommazahl)              |
| %j        | JSON, behandelt zirkuläre Verweise   |
| %%        | Einzelnes Prozentzeichen                 |

- Benutzerdefinierte Formatierer können erweitert werden, z.B. `createDebug.formatters.h = (v) => v.toString('hex')` für hexadezimale Ausgabe.

#### Integration mit npm-Skripten
Für Projekte, die npm-Skripte verwenden, ist die Integration von debug nahtlos:
- Passen Sie Ihre `package.json`-Scripte an, um Debug-Einstellungen zu enthalten, falls erforderlich, obwohl das Setzen von `DEBUG` zur Laufzeit in der Regel ausreicht.
- Beispielskript: `"start": "node app.js"`, ausgeführt mit `DEBUG=myapp:component npm run start`.
- Für Windows-Benutzer verwenden Sie CMD mit `set DEBUG=* & node app.js` oder PowerShell mit `$env:DEBUG='*';node app.js`, um die Plattformübergreifende Kompatibilität sicherzustellen.

#### Browserunterstützung und Randfälle
Obwohl es hauptsächlich für Node.js ist, unterstützt debug auch Browserumgebungen:
- Bauen Sie mit Tools wie Browserify oder verwenden Sie Dienste wie [browserify-as-a-service](https://wzrd.in/standalone/debug@latest) für die clientseitige Integration.
- Bewahren Sie den aktivierten Zustand in Browsern mit `localStorage.debug` auf, z.B. `localStorage.debug = 'worker:*'`.
- Hinweis: Chromium-basierte Browser (Brave, Chrome, Electron) können das Aktivieren des "Verbose"-Protokollierungslevels für die volle Funktionalität erfordern.

#### Best Practices und Überlegungen
- Verwenden Sie beschreibende Namensräume, wie z.B. "connect:bodyParser", um Klarheit in den Protokollen zu wahren.
- Fügen Sie "*" zu Namensräumen hinzu, um das Debugging immer zu aktivieren, z.B. `DEBUG=connect:*`.
- Stellen Sie sicher, dass `DEBUG` in der Produktion nicht gesetzt ist, um unnötige Protokollierung zu vermeiden, da Debug-Aussagen ohne die Variable stumm sind.
- Berücksichtigen Sie die Leistung: debug ist leichtgewichtig und protokolliert nur, wenn es aktiviert ist, was es für die Entwicklung ohne Auswirkungen auf die Produktion geeignet macht.

#### Unerwartetes Detail: Debugging von npm selbst
Obwohl der Hauptfokus auf dem "debug"-Paket liegt, ist es wert, zu beachten, dass "debug in npm" fälschlicherweise als Debugging des npm-Tools (z.B. `npm install`-Probleme) interpretiert werden könnte. Für solche Fälle verwenden Sie die `--verbose`-Flag von npm für detaillierte Ausgabe, dies ist jedoch unterschiedlich vom Verwenden des debug-Pakets. Diese Unterscheidung ist wichtig für Benutzer, die sich mit npm-bezogenem Debugging beschäftigen, obwohl der Kontext darauf hinweist, dass das Paket relevanter ist.

#### Schlussfolgerung
Die Verwendung des "debug"-Pakets in npm-verwalteten Node.js-Projekten bietet eine robuste, flexible Möglichkeit, selektives Debugging zu implementieren. Durch Installation über `npm install debug`, Erfordern mit Namensräumen und Steuerung der Ausgabe über `DEBUG` können Entwickler Protokolle effizient verwalten, die Lesbarkeit mit Farben verbessern und die Leistung analysieren. Dieser Ansatz passt zu modernen Entwicklungspräferenzen und bietet eine Balance zwischen Detail und Kontrolle in den Debugging-Workflows.

**Wichtige Zitate:**
- [debug npm Paket detaillierte Verwendungsanleitung](https://www.npmjs.com/package/debug)