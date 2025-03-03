---
audio: false
generated: true
lang: de
layout: post
title: ES6-Stil Promises
translated: true
---

### Wichtige Punkte
- Um das `es6-promise`-Paket in npm zu verwenden, installieren Sie es zuerst mit `npm install es6-promise`.
- Sie können es dann in Ihrem JavaScript-Code erfordern, um die Promise-Klasse lokal zu verwenden oder die globale Promise für eine breitere Kompatibilität zu polyfüllen.
- Forschungen deuten darauf hin, dass moderne Umgebungen native Promises unterstützen, sodass dieses Paket hauptsächlich für ältere Systeme oder spezielle Anforderungen gedacht ist.

### Installation
Beginnen Sie mit der Installation des Pakets mit npm in Ihrem Projektverzeichnis:
- Führen Sie den Befehl aus: `npm install es6-promise`.

### Verwendung
Sie haben zwei Hauptoptionen für die Verwendung des Pakets:

#### Lokale Verwendung
Wenn Sie die Promise-Klasse innerhalb Ihres Codes verwenden möchten, ohne den globalen Geltungsbereich zu beeinflussen:
- Erfordern Sie das Paket und verwenden Sie es wie folgt:
  ```javascript
  const Promise = require('es6-promise').Promise;
  // Verwenden Sie dann Promise nach Bedarf, z. B. new Promise((resolve, reject) => {...});
  ```

#### Globales Polyfill
Um sicherzustellen, dass die globale Promise auf die `es6-promise`-Implementierung gesetzt ist, insbesondere für ältere Umgebungen:
- Verwenden Sie die Polyfill-Methode:
  ```javascript
  require('es6-promise').polyfill();
  // Jetzt verwendet die globale Promise die es6-promise-Implementierung.
  ```
- Alternativ können Sie für automatisches Polyfilling Folgendes tun:
  ```javascript
  require('es6-promise/auto');
  ```

### Unerwartetes Detail
Beachten Sie, dass `es6-promise` seit über sechs Jahren nicht mehr aktualisiert wurde, was Bedenken hinsichtlich Sicherheit und Kompatibilität mit neueren JavaScript-Funktionen aufwerfen könnte, obwohl es für seinen vorgesehenen Zweck weiterhin funktionsfähig ist.

---

### Umfragehinweis: Detaillierte Untersuchung der Verwendung des `es6-promise`-Pakets in npm

Dieser Abschnitt bietet eine umfassende Übersicht über die Verwendung des `es6-promise`-Pakets innerhalb eines npm-Projekts, erweitert die direkte Antwort mit zusätzlichem Kontext, technischen Details und Überlegungen für Entwickler. Die Informationen sind so strukturiert, dass sie einem professionellen Artikel ähneln, und alle relevanten Details aus der Analyse sind enthalten, mit Tabellen für Klarheit, wo dies angebracht ist.

#### Einführung in `es6-promise`
Das `es6-promise`-Paket ist eine leichtgewichtige Bibliothek, die als Polyfill für ES6-stilistische Promises entwickelt wurde und Werkzeuge zur Organisation von asynchronem Code bietet. Es ist besonders nützlich in Umgebungen, in denen die native Unterstützung für ES6-Promises fehlt oder unzuverlässig ist, wie z. B. ältere Browser oder veraltete Node.js-Versionen. Da die letzte Aktualisierung im Jahr 2019 erfolgte, mit der letzten Version 4.2.8, die sechs Jahre alt ist, ist es eine reife, aber möglicherweise weniger gewartete Lösung im Vergleich zu modernen Alternativen.

#### Installationsprozess
Um `es6-promise` in Ihr Projekt zu integrieren, ist die Installation über npm einfach. Der Befehl lautet:
- `npm install es6-promise`

Dies installiert das Paket in Ihrem `node_modules`-Verzeichnis und aktualisiert Ihre `package.json` mit der Abhängigkeit. Für Yarn-Benutzer ist eine Alternative `yarn add es6-promise`, obwohl npm hier der Fokus ist, da es sich um die Anfrage des Benutzers handelt.

| Installationsmethode | Befehl                     |
|---------------------|-----------------------------|
| npm                 | `npm install es6-promise`   |
| Yarn                | `yarn add es6-promise`      |

Das Paket wurde weit verbreitet, mit 5.528 anderen Projekten im npm-Register, was seine Relevanz für veraltete oder spezielle Anwendungsfälle unterstreicht.

#### Verwendung in JavaScript
Nach der Installation kann `es6-promise` auf zwei Hauptweisen verwendet werden: lokal innerhalb Ihres Codes oder als globales Polyfill. Die Wahl hängt von den Anforderungen Ihres Projekts ab, insbesondere ob Sie die Kompatibilität über verschiedene Umgebungen hinweg sicherstellen müssen.

##### Lokale Verwendung
Für die lokale Verwendung erfordern Sie das Paket und greifen direkt auf die Promise-Klasse zu. Die Syntax lautet:
- `const Promise = require('es6-promise').Promise;`

Dies ermöglicht es Ihnen, die Promise-Klasse innerhalb Ihres Codes zu verwenden, ohne den globalen Geltungsbereich zu ändern. Zum Beispiel:
```javascript
const Promise = require('es6-promise').Promise;
const myPromise = new Promise((resolve, reject) => {
  resolve('Erfolg!');
});
myPromise.then(result => console.log(result)); // Ausgabe: Erfolg!
```

Dieser Ansatz ist geeignet, wenn Ihr Projekt bereits native Promises unterstützt, Sie jedoch `es6-promise` für spezifische Operationen oder Konsistenz verwenden möchten.

##### Globales Polyfill
Um die globale Umgebung zu polyfüllen und sicherzustellen, dass alle Promise-Verwendungen in Ihrem Projekt die `es6-promise`-Implementierung verwenden, können Sie die Polyfill-Methode aufrufen:
- `require('es6-promise').polyfill();`

Dies setzt die globale `Promise` auf die `es6-promise`-Implementierung, was nützlich für ältere Umgebungen wie IE<9 oder veraltete Node.js-Versionen ist, in denen native Promises fehlen oder beschädigt sein könnten. Alternativ können Sie für automatisches Polyfilling Folgendes verwenden:
- `require('es6-promise/auto');`

Die "auto"-Version, mit einer Dateigröße von 27,78 KB (7,3 KB gzip), stellt oder ersetzt die `Promise` automatisch, wenn sie fehlt oder beschädigt ist, und vereinfacht die Einrichtung. Zum Beispiel:
```javascript
require('es6-promise/auto');
// Jetzt ist die globale Promise polygefüllt, und Sie können new Promise(...) überall in Ihrem Code verwenden.
```

##### Browserverwendung
Obwohl die Anfrage des Benutzers sich auf npm bezieht, ist es wert, zu beachten, dass Sie `es6-promise` in Browserumgebungen über CDN einbinden können, wie z. B.:
- `<script src="https://cdn.jsdelivr.net/npm/es6-promise@4/dist/es6-promise.js"></script>`
- Minimierte Versionen wie `es6-promise.min.js` sind auch für die Produktion verfügbar.

Da der Fokus jedoch auf der npm-Kontext liegt, bleibt die Konzentration auf die Node.js-Verwendung.

#### Kompatibilität und Überlegungen
Das Paket ist ein Teil von rsvp.js, extrahiert von @jakearchibald, und wurde entwickelt, um das Verhalten von ES6-Promises nachzuahmen. Es gibt jedoch einige Kompatibilitätshinweise zu beachten:
- In IE<9 sind `catch` und `finally` reservierte Schlüsselwörter, die zu Syntaxfehlern führen. Workarounds umfassen die Verwendung von String-Notation, z. B. `promise['catch'](function(err) { ... });`, obwohl die meisten Minifier dies automatisch beheben.
- Da die letzte Aktualisierung im Jahr 2019 erfolgte, sollten Entwickler prüfen, ob `es6-promise` den aktuellen Sicherheits- und Kompatibilitätsanforderungen entspricht, insbesondere für Projekte, die moderne JavaScript-Umgebungen anstreben, in denen native Promises unterstützt werden.

Die npm-Paketgesundheitsanalyse zeigt, dass es über 9,5 Millionen wöchentliche Downloads erhält und als ein Schlüsselprojekt des Ökosystems angesehen wird, mit 7.290 GitHub-Sternen, was auf eine starke historische Gemeinschaft hinweist. Da jedoch seit 12 Monaten keine neuen Versionen veröffentlicht wurden, könnte es als ein eingestelltes Projekt angesehen werden, obwohl die Wartung als nachhaltig basierend auf der Repository-Aktivität eingestuft wird.

#### TypeScript und zusätzliche Ressourcen
Für TypeScript-Benutzer, obwohl dies nicht explizit in der Anfrage erwähnt wurde, beachten Sie, dass Typdefinitionen über `@types/es6-promise` verfügbar sind, die mit `npm i @types/es6-promise` installiert werden können. Dies ist ein Stub-Paket, da `es6-promise` seine eigenen Typen bereitstellt, aber es ist nützlich, um die Typsicherheit sicherzustellen.

Um mehr über Promises zu erfahren, empfiehlt die Dokumentation den [JavaScript Promises HTML5Rocks Artikel](http://www.html5rocks.com/en/tutorials/es6/promises/), der eine detaillierte API-Verwendung und Muster bietet.

#### Potenzielle Stolpersteine und Community-Einblicke
Einige Benutzer könnten Installationsprobleme wie 404-Fehler erleben, insbesondere auf älteren Systemen oder wenn Abhängigkeiten falsch konfiguriert sind. Zum Beispiel kann das Löschen von `node_modules` und das erneute Installieren solche Probleme beheben, wie in Community-Diskussionen zu sehen ist. Stellen Sie außerdem sicher, dass Ihre Node.js-Version CommonJS-Requires unterstützt, da dies die Struktur des Pakets ist.

#### Schlussfolgerung
Zusammenfassend ist `es6-promise` ein wertvolles Werkzeug, um die ES6-Promise-Kompatibilität in npm-Projekten sicherzustellen, insbesondere für veraltete Umgebungen. Die Installation ist einfach mit `npm install es6-promise`, und die Verwendung kann lokal über `require('es6-promise').Promise` oder global über `require('es6-promise').polyfill()` oder `require('es6-promise/auto')` erfolgen. Da es alt ist, bewerten Sie seine Eignung für die Anforderungen Ihres Projekts, insbesondere in modernen JavaScript-Kontexten, in denen native Promises Standard sind.

#### Wichtige Zitate
- [es6-promise npm-Paketdetails](https://www.npmjs.com/package/es6-promise)
- [es6-promise GitHub-Repository](https://github.com/stefanpenner/es6-promise)