---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser Autoprefixer
translated: true
type: note
---

Je vais expliquer comment utiliser Autoprefixer en développement frontend. Autoprefixer est un plugin PostCSS qui ajoute automatiquement les préfixes vendeurs à votre CSS, garantissant une compatibilité cross-browser.

Voici les principales méthodes pour intégrer Autoprefixer dans votre workflow frontend :

1. Utilisation avec npm (Approche la plus courante)
```bash
# Installer autoprefixer et postcss
npm install autoprefixer postcss --save-dev
```

2. Configuration de base avec PostCSS CLI
```bash
# Installer postcss-cli
npm install postcss-cli --save-dev

# Créer un fichier postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer')
  ]
}

# Ajouter aux scripts package.json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```

3. Avec les outils de build :

a) Webpack avec postcss-loader
```bash
npm install postcss-loader --save-dev
```

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader',
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: ['autoprefixer']
              }
            }
          }
        ]
      }
    ]
  }
}
```

b) Vite (support intégré)
```javascript
// vite.config.js
import autoprefixer from 'autoprefixer'

export default {
  css: {
    postcss: {
      plugins: [autoprefixer()]
    }
  }
}
```

4. Options de configuration
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer')({
      overrideBrowserslist: ['> 1%', 'last 2 versions'], // Navigateurs cibles
      grid: true, // Activer les préfixes grid
      flexbox: 'no-2009' // Options de support flexbox
    })
  ]
}
```

5. Exemple d'utilisation en CSS
```css
/* Input */
.container {
  display: flex;
  justify-content: space-between;
}

/* Output (après Autoprefixer) */
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
```

Fonctionnalités principales et conseils :
- Ajoute automatiquement les préfixes basés sur les données Can I Use
- Contrôlé par browserslist (généralement dans package.json)
- Supprime les préfixes obsolètes des anciens CSS
- Fonctionne avec les fonctionnalités CSS modernes comme les custom properties

Exemple basique de browserslist dans package.json :
```json
{
  "browserslist": [
    "> 1%",
    "last 2 versions",
    "not dead"
  ]
}
```

Pour exécuter :
```bash
# Avec PostCSS CLI
npx postcss src/*.css --dir dist

# Ou avec votre script npm
npm run build:css
```

Choisissez la méthode d'intégration en fonction de la configuration existante de votre projet (Webpack, Vite, etc.). Les approches Webpack ou Vite sont les plus courantes dans le développement frontend moderne car elles s'intègrent bien avec les processus de build existants.