---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von PostCSS zur Transformation von CSS
translated: true
---

Ich erkläre, wie man PostCSS in einem Frontend-Projekt verwendet. PostCSS ist ein Werkzeug zur Transformation von CSS mit JavaScript-Plugins, das Funktionen wie Autoprefixing, Minifizierung und Unterstützung für zukünftige CSS-Syntax bietet. Hier ist eine Schritt-für-Schritt-Anleitung:

### 1. **Projekt einrichten**
Stellen Sie sicher, dass Sie ein Frontend-Projekt mit installiertem Node.js haben. Falls nicht, initialisieren Sie eines:
```bash
mkdir mein-projekt
cd mein-projekt
npm init -y
```

### 2. **PostCSS und erforderliche Tools installieren**
Installieren Sie PostCSS, die PostCSS-CLI und alle Plugins, die Sie verwenden möchten (z.B. `autoprefixer` für Anbieterpräfixe oder `cssnano` für Minifizierung):
```bash
npm install --save-dev postcss postcss-cli autoprefixer cssnano
```

### 3. **CSS-Datei erstellen**
Erstellen Sie eine Quell-CSS-Datei, z.B. `src/styles.css`:
```css
/* src/styles.css */
.container {
  display: flex;
  transition: all 0.3s ease;
}
```

### 4. **PostCSS konfigurieren**
Erstellen Sie eine `postcss.config.js`-Datei im Projektverzeichnis, um Plugins zu spezifizieren:
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'), // Fügt Anbieterpräfixe hinzu
    require('cssnano')({ preset: 'default' }) // Minifiziert CSS
  ]
};
```

### 5. **Build-Skript hinzufügen**
Fügen Sie in Ihrer `package.json` ein Skript hinzu, um Ihre CSS-Datei mit PostCSS zu verarbeiten:
```json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```
- `src/styles.css`: Eingabedatei
- `dist/styles.css`: Ausgabedatei

### 6. **PostCSS ausführen**
Führen Sie den Build-Befehl aus:
```bash
npm run build:css
```
Dies verarbeitet `src/styles.css` und gibt das transformierte CSS in `dist/styles.css` aus. Zum Beispiel fügt `autoprefixer` Präfixe hinzu und `cssnano` minifiziert es:
```css
/* dist/styles.css */
.container{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-transition:all .3s ease;transition:all .3s ease}
```

### 7. **Integration mit einem Build-Tool (optional)**
Für eine robustere Einrichtung integrieren Sie PostCSS mit Tools wie Webpack, Vite oder Gulp:

#### **Mit Vite**
Wenn Sie Vite verwenden, installieren Sie `postcss` und konfigurieren Sie es in `vite.config.js`:
```javascript
// vite.config.js
import postcss from 'postcss';
import autoprefixer from 'autoprefixer';

export default {
  css: {
    postcss: {
      plugins: [autoprefixer()]
    }
  }
};
```
Vite verarbeitet PostCSS automatisch, wenn Sie CSS-Dateien importieren.

#### **Mit Webpack**
Installieren Sie `postcss-loader`:
```bash
npm install --save-dev postcss-loader
```
Aktualisieren Sie Ihre `webpack.config.js`:
```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader']
      }
    ]
  }
};
```

### 8. **Änderungen überwachen (optional)**
Um CSS während der Entwicklung automatisch zu verarbeiten, ändern Sie das Skript in Ihrer `package.json`:
```json
"scripts": {
  "watch:css": "postcss src/styles.css -o dist/styles.css --watch"
}
```
Führen Sie `npm run watch:css` aus, um Dateiänderungen zu überwachen.

### 9. **Gängige Plugins**
Hier sind einige beliebte PostCSS-Plugins:
- `autoprefixer`: Fügt Anbieterpräfixe basierend auf der Browserunterstützung hinzu.
- `cssnano`: Minifiziert CSS.
- `postcss-preset-env`: Ermöglicht die Verwendung zukünftiger CSS-Funktionen.
- `postcss-import`: Löst `@import`-Regeln auf.
Installieren Sie sie nach Bedarf:
```bash
npm install --save-dev postcss-preset-env postcss-import
```
Fügen Sie sie zu `postcss.config.js` hinzu:
```javascript
module.exports = {
  plugins: [
    require('postcss-import'),
    require('postcss-preset-env'),
    require('autoprefixer'),
    require('cssnano')({ preset: 'default' })
  ]
};
```

### Beispiel-Workflow
1. Schreiben Sie modernes CSS in `src/styles.css`:
```css
@custom-media --viewport-medium (width >= 768px);

:root {
  --main-color: #1a73e8;
}

.container {
  color: var(--main-color);
  display: grid;
}

@media (--viewport-medium) {
  .container {
    grid-template-columns: 1fr 1fr;
  }
}
```
2. Führen Sie `npm run build:css` aus.
3. Erhalten Sie verarbeitetes CSS in `dist/styles.css` mit Präfixen, aufgelösten Variablen und Minifizierung.

### Tipps
- Verwenden Sie `--map` in der CLI (`postcss src/styles.css -o dist/styles.css --map`), um Quellkarten für das Debuggen zu generieren.
- Überprüfen Sie die Plugin-Dokumentation für spezifische Konfigurationsoptionen.
- Kombinieren Sie es mit einem Frontend-Framework (React, Vue usw.), indem Sie das ausgegebene CSS mit Ihrem HTML oder Bundler verknüpfen.