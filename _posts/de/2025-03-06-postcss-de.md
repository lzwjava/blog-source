---
audio: false
generated: true
lang: de
layout: post
title: Verwenden von PostCSS zum Transformieren von CSS
translated: true
type: note
---

Ich erkläre, wie man PostCSS in einem Frontend-Projekt verwendet. PostCSS ist ein Tool zur Transformation von CSS mit JavaScript-Plugins, das Funktionen wie Autoprefixing, Minification und Unterstützung für zukünftige CSS-Syntax bietet. Hier ist eine Schritt-für-Schritt-Anleitung:

### 1. **Richten Sie Ihr Projekt ein**
Stellen Sie sicher, dass Sie ein Frontend-Projekt mit installiertem Node.js haben. Falls nicht, initialisieren Sie eines:
```bash
mkdir my-project
cd my-project
npm init -y
```

### 2. **Installieren Sie PostCSS und die erforderlichen Tools**
Installieren Sie PostCSS, die PostCSS CLI und alle gewünschten Plugins (z.B. `autoprefixer` für Vendor-Prefixes oder `cssnano` für Minification):
```bash
npm install --save-dev postcss postcss-cli autoprefixer cssnano
```

### 3. **Erstellen Sie eine CSS-Datei**
Erstellen Sie eine Quell-CSS-Datei, z.B. `src/styles.css`:
```css
/* src/styles.css */
.container {
  display: flex;
  transition: all 0.3s ease;
}
```

### 4. **Konfigurieren Sie PostCSS**
Erstellen Sie eine `postcss.config.js`-Datei im Stammverzeichnis Ihres Projekts, um die Plugins anzugeben:
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'), // Fügt Vendor-Prefixes hinzu
    require('cssnano')({ preset: 'default' }) // Minifiziert CSS
  ]
};
```

### 5. **Fügen Sie ein Build-Skript hinzu**
Fügen Sie in Ihrer `package.json` ein Skript hinzu, um Ihr CSS mit PostCSS zu verarbeiten:
```json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```
- `src/styles.css`: Eingabedatei
- `dist/styles.css`: Ausgabedatei

### 6. **Führen Sie PostCSS aus**
Führen Sie den Build-Befehl aus:
```bash
npm run build:css
```
Dies verarbeitet `src/styles.css` und gibt das transformierte CSS in `dist/styles.css` aus. Zum Beispiel könnte `autoprefixer` Präfixe hinzufügen und `cssnano` es minifizieren:
```css
/* dist/styles.css */
.container{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-transition:all .3s ease;transition:all .3s ease}
```

### 7. **Integrieren Sie es in ein Build-Tool (Optional)**
Für einen robusteren Setup integrieren Sie PostCSS in Tools wie Webpack, Vite oder Gulp:

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

### 8. **Beobachten Sie Änderungen (Optional)**
Um CSS während der Entwicklung automatisch zu verarbeiten, modifizieren Sie Ihr `package.json`-Skript:
```json
"scripts": {
  "watch:css": "postcss src/styles.css -o dist/styles.css --watch"
}
```
Führen Sie `npm run watch:css` aus, um auf Dateiänderungen zu achten.

### 9. **Gängige Plugins**
Hier sind einige beliebte PostCSS-Plugins:
- `autoprefixer`: Fügt Vendor-Prefixes basierend auf Browserunterstützung hinzu.
- `cssnano`: Minifiziert CSS.
- `postcss-preset-env`: Ermöglicht die Verwendung zukünftiger CSS-Funktionen heute.
- `postcss-import`: Löst `@import`-Regeln auf.
Installieren Sie sie nach Bedarf:
```bash
npm install --save-dev postcss-preset-env postcss-import
```
Fügen Sie sie zur `postcss.config.js` hinzu:
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

### Beispielhafter Workflow
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
3. Erhalten Sie verarbeitetes CSS in `dist/styles.css` mit Präfixen, aufgelösten Variablen und Minification.

### Tipps
- Verwenden Sie `--map` in der CLI (`postcss src/styles.css -o dist/styles.css --map`), um Source Maps für das Debugging zu generieren.
- Überprüfen Sie die Plugin-Dokumentation für spezifische Konfigurationsoptionen.
- Kombinieren Sie es mit einem Frontend-Framework (React, Vue, etc.), indem Sie das ausgegebene CSS mit Ihrem HTML oder Bundler verlinken.

Lassen Sie mich wissen, wenn Sie Hilfe mit einem bestimmten Setup oder Plugin benötigen!