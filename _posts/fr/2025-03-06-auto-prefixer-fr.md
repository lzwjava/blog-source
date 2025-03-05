---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser Autoprefixer
translated: true
---

Je vais expliquer comment utiliser Autoprefixer dans le développement frontend. Autoprefixer est un plugin PostCSS qui ajoute automatiquement des préfixes de fournisseurs à votre CSS, garantissant ainsi la compatibilité multi-navigateurs.

Voici les principales méthodes pour intégrer Autoprefixer dans votre flux de travail frontend :

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

# Ajouter aux scripts de package.json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```

3. Avec des outils de construction :

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
      grid: true, // Activer les préfixes de grille
      flexbox: 'no-2009' // Options de support de flexbox
    })
  ]
}
```

5. Exemple d'utilisation en CSS
```css
/* Entrée */
.container {
  display: flex;
  justify-content: space-between;
}

/* Sortie (après Autoprefixer) */
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
```

Fonctionnalités clés et conseils :
- Ajoute automatiquement des préfixes en fonction des données de Can I Use
- Contrôlé par browserslist (généralement dans package.json)
- Supprime les préfixes obsolètes des anciens CSS
- Fonctionne avec les fonctionnalités CSS modernes comme les propriétés personnalisées

Exemple de base de browserslist dans package.json :
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

Choisissez la méthode d'intégration en fonction de la configuration existante de votre projet (Webpack, Vite, etc.). Les approches Webpack ou Vite sont les plus courantes dans le développement frontend moderne car elles s'intègrent bien aux processus de construction existants.