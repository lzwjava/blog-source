---
audio: false
generated: true
lang: fr
layout: post
title: Problème Font Awesome
translated: true
type: note
---

L'erreur "can't resolve .../fonts/fontawesome-webfont.woff2" se produit généralement lorsque le fichier CSS de Font Awesome référence un fichier de police (comme `fontawesome-webfont.woff2`) qui ne peut pas être trouvé dans le chemin spécifié. Ce problème survient souvent dans les projets utilisant npm, Webpack ou d'autres module bundlers. Voici les étapes pour résoudre cette erreur :

---

### 1. Vérifier l'installation de Font Awesome
Assurez-vous que Font Awesome est correctement installé dans votre projet.

- **Si vous utilisez npm** :
  ```bash
  npm install @fortawesome/fontawesome-free
  ```
  Ceci installe la version gratuite de Font Awesome.

- Vérifiez que le package est listé dans votre `package.json` :
  ```json
  "dependencies": {
    "@fortawesome/fontawesome-free": "^6.x.x"
  }
  ```

---

### 2. Vérifier le chemin des fichiers de police dans le CSS
L'erreur se produit souvent parce que le fichier `fontawesome.css` référence les fichiers de police dans un chemin relatif (par exemple, `../fonts/fontawesome-webfont.woff2`) qui ne correspond pas à la structure de fichiers de votre projet ou à votre processus de build.

- **Localisez le fichier CSS** :
  Trouvez le fichier CSS de Font Awesome dans `node_modules/@fortawesome/fontawesome-free/css/all.css` (ou similaire).

- **Inspectez la déclaration @font-face** :
  Ouvrez le fichier CSS et cherchez la règle `@font-face`. Elle pourrait ressembler à ceci :
  ```css
  @font-face {
    font-family: 'FontAwesome';
    src: url('../fonts/fontawesome-webfont.woff2') format('woff2'),
         url('../fonts/fontawesome-webfont.woff') format('woff');
  }
  ```

- **Vérifiez les fichiers de police** :
  Vérifiez si les fichiers de police référencés existent dans `node_modules/@fortawesome/fontawesome-free/webfonts/`. Le dossier `webfonts` contient typiquement des fichiers comme `fontawesome-webfont.woff2`.

---

### 3. Corriger les problèmes de chemin
Si les fichiers de police ne sont pas résolus, vous devrez peut-être ajuster la manière dont les chemins sont gérés dans votre processus de build.

#### Option 1 : Copier les fichiers de police vers votre répertoire public
Copiez manuellement les fichiers de police vers un répertoire accessible par votre application (par exemple, `public/fonts` ou `src/fonts`).

- **Copiez les fichiers** :
  ```bash
  mkdir -p public/fonts
  cp -r node_modules/@fortawesome/fontawesome-free/webfonts/* public/fonts/
  ```

- **Mettez à jour le CSS** :
  Modifiez le fichier `fontawesome.css` pour pointer vers le nouvel emplacement des polices :
  ```css
  @font-face {
    font-family: 'FontAwesome';
    src: url('/fonts/fontawesome-webfont.woff2') format('woff2'),
         url('/fonts/fontawesome-webfont.woff') format('woff');
  }
  ```

- Alternativement, utilisez un préprocesseur CSS ou un post-processeur pour réécrire les chemins.

#### Option 2 : Configurer Webpack (ou autres bundlers)
Si vous utilisez Webpack, assurez-vous qu'il peut résoudre et charger les fichiers de police.

- **Installez file-loader ou url-loader** :
  ```bash
  npm install file-loader --save-dev
  ```

- **Mettez à jour la configuration Webpack** (`webpack.config.js`) :
  Ajoutez une règle pour gérer les fichiers de police :
  ```javascript
  module: {
    rules: [
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: 'fonts/',
              publicPath: '/fonts/',
            },
          },
        ],
      },
    ],
  }
  ```

- Assurez-vous que le CSS de Font Awesome est importé dans votre JavaScript :
  ```javascript
  import '@fortawesome/fontawesome-free/css/all.css';
  ```

#### Option 3 : Utiliser un CDN
Si vous ne voulez pas bundler les fichiers de police, vous pouvez utiliser un CDN pour charger Font Awesome.

- Remplacez l'import local par un lien CDN dans votre HTML :
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
  ```

- Supprimez l'import local du CSS de Font Awesome de votre code.

---

### 4. Vérifier la sensibilité à la casse
Les chemins de fichiers sont sensibles à la casse sur certains systèmes (par exemple, Linux). Assurez-vous que les noms de fichiers et les chemins dans votre CSS correspondent exactement aux noms de fichiers réels.

- Par exemple, si le fichier est `fontawesome-webfont.woff2`, mais que le CSS référence `FontAwesome-WebFont.woff2`, cela échouera.

---

### 5. Vider le cache et reconstruire
Parfois, des caches obsolètes causent des problèmes de résolution.

- Videz le cache npm :
  ```bash
  npm cache clean --force
  ```

- Supprimez `node_modules` et `package-lock.json`, puis réinstallez :
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  ```

- Reconstruisez votre projet :
  ```bash
  npm run build
  ```

---

### 6. Alternative : Utiliser Font Awesome via SCSS
Si vous utilisez SCSS, vous pouvez importer les fichiers SCSS de Font Awesome et configurer le chemin des polices.

- Installez Font Awesome comme indiqué ci-dessus.
- Importez le SCSS dans votre fichier SCSS principal :
  ```scss
  $fa-font-path: '~@fortawesome/fontawesome-free/webfonts';
  @import '~@fortawesome/fontawesome-free/scss/fontawesome';
  @import '~@fortawesome/fontawesome-free/scss/solid';
  ```

- Assurez-vous que votre compilateur SCSS résout correctement le dossier `webfonts`.

---

### 7. Conseils de débogage
- **Vérifiez la console du navigateur** :
  Cherchez les erreurs 404 pour les fichiers de police et notez l'URL demandée.
- **Inspectez la sortie du build** :
  Vérifiez que les fichiers de police sont inclus dans le répertoire de sortie (par exemple, `dist/fonts/`).
- **Utilisez `resolve-url-loader`** :
  Si vous utilisez Webpack avec SCSS, installez `resolve-url-loader` pour aider à résoudre les URLs relatives :
  ```bash
  npm install resolve-url-loader --save-dev
  ```

---

### 8. Si vous utilisez un framework
Certains frameworks (par exemple, React, Vue, Angular) peuvent nécessiter une configuration supplémentaire :

- **React** :
  Assurez-vous d'importer le CSS dans votre `index.js` ou `App.js` :
  ```javascript
  import '@fortawesome/fontawesome-free/css/all.css';
  ```
  Utilisez la configuration Webpack ci-dessus si nécessaire.

- **Vue** :
  Si vous utilisez Vue CLI, ajoutez la règle Webpack à `vue.config.js` :
  ```javascript
  module.exports = {
    chainWebpack: (config) => {
      config.module
        .rule('fonts')
        .test(/\.(woff|woff2|eot|ttf|otf)$/)
        .use('file-loader')
        .loader('file-loader')
        .options({
          name: '[name].[ext]',
          outputPath: 'fonts/',
          publicPath: '/fonts/',
        });
    },
  };
  ```

- **Angular** :
  Ajoutez le CSS de Font Awesome à `angular.json` :
  ```json
  "styles": [
    "node_modules/@fortawesome/fontawesome-free/css/all.css",
    "src/styles.css"
  ]
  ```

---

### 9. Tester la correction
- Lancez votre serveur de développement :
  ```bash
  npm start
  ```
- Ouvrez votre application dans le navigateur et vérifiez que les icônes Font Awesome se chargent correctement sans erreurs dans la console.

---

### 10. Si le problème persiste
- **Vérifiez les versions conflictuelles** :
  Assurez-vous que vous ne mélangez pas différentes versions de Font Awesome (par exemple, v5 et v6).
- **Cherchez des problèmes similaires** :
  Recherchez des erreurs spécifiques à votre configuration (par exemple, Webpack, Create React App) sur Stack Overflow ou GitHub.
- **Fournissez plus de détails** :
  Si vous avez besoin d'aide supplémentaire, partagez :
  - La configuration de votre projet (par exemple, Webpack, React, etc.).
  - Le message d'erreur exact.
  - Des extraits de code pertinents (par exemple, comment vous importez Font Awesome).

---

Cela devrait résoudre l'erreur "can't resolve .../fonts/fontawesome-webfont.woff2". Faites-moi savoir si vous avez besoin d'aide pour une étape spécifique !