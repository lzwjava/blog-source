---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Entwicklungsabhängigkeiten und Build-Tools
translated: true
type: note
---

### DevDependencies
Dies sind Pakete, die während der Entwicklung verwendet werden und nicht im finalen Build enthalten sind.

- **babel-core** (6.13.0): Kern-Babel-Compiler zum Transpilieren von modernem JavaScript (ES6+) zu ES5 für breitere Browserkompatibilität.
- **babel-loader** (6.2.5): Webpack-Loader, der Babel zur JavaScript-Transformation in Build-Prozessen integriert.
- **babel-plugin-transform-runtime** (6.12.0): Babel-Plugin, das Laufzeit-Helfer wiederverwendet, um die Bundle-Größe in transpiliertem Code zu reduzieren.
- **babel-preset-es2015** (6.13.2): Babel-Preset zum Kompilieren von ES2015 (ES6)-Features zu ES5.
- **babel-runtime** (6.11.6): Laufzeit-Bibliothek, die Polyfills und Helfer für Babel-transpilierten Code bereitstellt.
- **cross-env** (^1.0.8): Setzt Umgebungsvariablen plattformübergreifend (z.B. NODE_ENV) ohne Shell-Unterschiede.
- **css-loader** (^0.23.1): Lädt und verarbeitet CSS-Dateien, löst Importe und Abhängigkeiten auf.
- **detect-indent** (4.0.0): Erkennt den Einrückungsstil (Leerzeichen/Tabs) von Dateien für konsistente Formatierung.
- **exports-loader** (^0.6.3): Macht Module-Exporte in verschiedenen Kontexten verfügbar (z.B. für nicht-AMD-Module).
- **extract-text-webpack-plugin** (^1.0.1): Extrahiert CSS aus JavaScript-Bundles in separate Dateien für bessere Performance.
- **file-loader** (0.9.0): Verarbeitet das Laden von Dateien (z.B. Bilder), indem sie in das Ausgabeverzeichnis ausgegeben und URLs zurückgegeben werden.
- **html-webpack-plugin** (^2.22.0): Generiert HTML-Dateien und injiziert gebündelte Assets, vereinfacht Single-Page-App-Setups.
- **rimraf** (^2.5.4): Plattformübergreifendes rekursives Löschen von Dateien (wie rm -rf unter Unix).
- **style-loader** (^0.13.1): Injiziert CSS über Style-Tags in den DOM für dynamisches Laden.
- **stylus** (^0.54.5): CSS-Präprozessor mit expressiver Syntax, kompiliert zu CSS.
- **stylus-loader** (^2.1.1): Webpack-Loader zur Verarbeitung von Stylus-Dateien in CSS.
- **url-loader** (0.5.7): Kodiert kleine Dateien (z.B. Bilder) inline als Base64 oder gibt größere aus; Fallback auf file-loader.
- **vue-hot-reload-api** (^1.2.0): Ermöglicht Hot Module Replacement für Vue.js-Komponenten während der Entwicklung.
- **vue-html-loader** (^1.0.0): Webpack-Loader zum Parsen von HTML-Templates in Vue Single-File Components.
- **vue-loader** (8.5.3): Lädt und verarbeitet Vue Single-File Components (.vue-Dateien) in JavaScript und CSS.
- **vue-style-loader** (^1.0.0): Verarbeitet CSS aus Vue-Komponenten, integriert mit style-loader.
- **webpack** (1.13.2): Module Bundler zum Erstellen und Optimieren von Web-Assets wie JS, CSS und Bildern.
- **webpack-dev-server** (1.14.0): Entwicklungsserver mit Live-Reloading und Hot Module Replacement.

### Dependencies
Dies sind Laufzeit-Pakete, die im finalen Anwendungsbuild enthalten sind.

- **debug** (^2.2.0): Debug-Utility mit namensraum-basierter Protokollierung und konditionaler Ausgabe (nur aktiviert via DEBUG-Umgebungsvariable).
- **es6-promise** (^3.0.2): Polyfill für die ES6 Promise-API in älteren Browsern/Umgebungen.
- **font-awesome** (^4.6.3): Beliebte Icon-Bibliothek, die skalierbare Vektor-Icons über CSS-Klassen bereitstellt.
- **github-markdown-css** (^2.4.0): CSS für das Styling von GitHub-flavored Markdown.
- **highlight.js** (^9.6.0): Syntax-Highlighter für Codeblöcke in mehreren Sprachen.
- **hls.js** (^0.7.6): JavaScript-Bibliothek zum Abspielen von HTTP Live Streaming (HLS)-Videos mit HTML5-Video.
- **inherit** (^2.2.6): Utility für klassische und prototypische Vererbung in JavaScript-Objekten.
- **jquery** (^3.1.0): Schnelle, funktionsreiche JavaScript-Bibliothek für DOM-Manipulation, AJAX und Events.
- **json-loader** (^0.5.4): Lädt JSON-Dateien als JavaScript-Module.
- **leancloud-realtime** (^3.2.3): SDK für LeanCloud's Echtzeit-Nachrichten- und Daten-Synchronisationsdienst.
- **marked** (^0.3.6): Markdown-Parser, der Markdown in HTML konvertiert.
- **moment** (^2.14.1): Datums-/Zeit-Manipulationsbibliothek zum Parsen, Validieren und Formatieren von Datumsangaben.
- **moment-timezone** (^0.5.7): Erweiterung für Moment.js zur Handhabung von Zeitzonen und Sommerzeit.
- **qiniu-js-sdk** (0.0.2): JavaScript-SDK für die Interaktion mit Qiniu Cloud Storage (Hoch-/Herunterladen von Dateien).
- **raw-loader** (^0.5.1): Webpack-Loader, der Dateien als Rohtext lädt (z.B. Text-Templates).
- **rupture** (^0.6.1): Media-Query-Erweiterung für Stylus, bietet Breakpoints für responsives Design.
- **sprintf-js** (^1.0.3): JavaScript sprintf-Implementierung für String-Formatierung mit Platzhaltern.
- **vue** (^1.0.26): Progressives MVVM-Framework zum Erstellen von Benutzeroberflächen (v1.x, welches älter ist).
- **vue-resource** (^0.6.1): HTTP-Client für Vue.js zur Vereinfachung von AJAX/API-Anfragen.
- **vue-router** (^0.7.13): Offizieller Router für Vue.js, ermöglicht Single-Page-Anwendungs-Navigation.
- **vue-spinner** (^1.0.2): Spinner/Lade-Komponenten-Bibliothek für Vue.js.
- **vue-weui** (^0.3.2): Vue.js-Wrapper für WeUI-Komponenten (UI-Bibliothek für WeChat-artige Oberflächen).
- **weixin-js-sdk** (^1.2.0): WeChat JavaScript-SDK zur Integration von WeChat-Web-Features (z.B. Teilen, Scannen).
- **weui** (^0.4.3): WeUI CSS-Framework zum Erstellen mobiler Oberflächen, inspiriert vom WeChat-Design.
- **word-color** (^1.2.0): Bibliothek zum Einfärben von Wörtern basierend auf Faktoren wie Hash oder Sprache, wahrscheinlich für Heatmap-artige Effekte.