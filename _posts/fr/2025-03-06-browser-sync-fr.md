---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser BrowserSync
translated: true
type: note
---

BrowserSync est un outil fantastique pour rationaliser le développement front-end en synchronisant les actions du navigateur, en rechargeant automatiquement les fichiers et en fournissant un serveur de développement local. Voici un guide étape par étape sur la façon d'utiliser BrowserSync dans votre flux de travail front-end :

---

### 1. **Installer Node.js et npm**
BrowserSync est un outil Node.js, vous aurez donc besoin de Node.js et npm (Node Package Manager) installés. Si vous ne les avez pas encore :
- Téléchargez et installez-les depuis [nodejs.org](https://nodejs.org/).
- Vérifiez l'installation :
  ```bash
  node -v
  npm -v
  ```

---

### 2. **Installer BrowserSync**
Vous pouvez installer BrowserSync globalement ou localement dans votre projet.

#### Option 1 : Installation Globale
Exécutez cette commande dans votre terminal pour installer BrowserSync globalement :
```bash
npm install -g browser-sync
```
Cela vous permet d'utiliser la commande `browser-sync` depuis n'importe où.

#### Option 2 : Installation Locale (Recommandée pour les Projets)
Si vous préférez garder les dépendances liées à un projet spécifique :
```bash
npm install browser-sync --save-dev
```
Cela ajoute BrowserSync au dossier `node_modules` de votre projet et le liste dans le fichier `package.json`.

---

### 3. **Démarrer BrowserSync**
En fonction de votre configuration, vous pouvez utiliser BrowserSync de différentes manières :

#### Utilisation de Base (Fichiers Statiques)
Si vous travaillez avec des fichiers HTML, CSS et JS statiques, naviguez vers votre dossier de projet et exécutez :
```bash
browser-sync start --server --files "*.html, css/*.css, js/*.js"
```
- `--server` : Lance un serveur local (sert les fichiers du répertoire courant).
- `--files` : Surveille ces fichiers pour les modifications et recharge automatiquement le navigateur.

Par exemple, si la structure de votre dossier est :
```
my-project/
├── index.html
├── css/
│   └── style.css
└── js/
    └── script.js
```
L'exécution de la commande ci-dessus va :
- Démarrer un serveur à l'adresse `http://localhost:3000` (port par défaut).
- Ouvrir votre navigateur par défaut.
- Recharger la page à chaque modification de `index.html`, `style.css` ou `script.js`.

#### Mode Proxy (Serveur Existant)
Si vous utilisez un serveur backend (par exemple, Node.js, PHP ou Python), utilisez l'option proxy :
```bash
browser-sync start --proxy "http://localhost:8000" --files "*.html, css/*.css, js/*.js"
```
- `--proxy` : Proxy les requêtes vers votre serveur existant (remplacez `http://localhost:8000` par l'URL de votre serveur).
- BrowserSync superposera ses fonctionnalités (comme le rechargement automatique) par-dessus.

---

### 4. **Fonctionnalités Clés**
Une fois que BrowserSync fonctionne, vous obtenez :
- **Rechargement en Direct** : Les modifications apportées aux fichiers surveillés déclenchent un rafraîchissement instantané du navigateur.
- **Synchronisation Multi-Appareils** : Le défilement, les clics et les saisies de formulaire sont synchronisés sur tous les appareils connectés (par exemple, ordinateur de bureau, téléphone, tablette).
- **Tableau de Bord UI** : Accédez à un panneau de contrôle à l'adresse `http://localhost:3001` (par défaut) pour ajuster les paramètres ou arrêter le serveur.

---

### 5. **Intégrer avec les Outils de Build (Optionnel)**
Si vous utilisez des outils comme Gulp ou Webpack, BrowserSync peut s'intégrer de manière transparente.

#### Exemple avec Gulp
Installez Gulp et BrowserSync :
```bash
npm install --save-dev gulp browser-sync
```
Créez un fichier `gulpfile.js` :
```javascript
const gulp = require('gulp');
const browserSync = require('browser-sync').create();

gulp.task('serve', function() {
  browserSync.init({
    server: './', // Sert les fichiers du répertoire courant
  });

  gulp.watch(['*.html', 'css/*.css', 'js/*.js']).on('change', browserSync.reload);
});

gulp.task('default', gulp.series('serve'));
```
Exécutez-le :
```bash
gulp
```

---

### 6. **Commandes et Options Courantes**
- Changer le port : `--port 8080`
- Désactiver l'ouverture automatique : `--no-open`
- Surveiller des fichiers spécifiques : `--files "chemin/vers/fichiers/*"`
- Liste complète : Exécutez `browser-sync --help`

---

### 7. **Dépannage**
- **Port déjà utilisé** : Changez le port avec `--port <numéro>`.
- **Pas de rechargement** : Assurez-vous que les chemins de fichiers dans `--files` correspondent à la structure de votre projet.
- **Problèmes de permissions** : Si installé globalement, vous pourriez avoir besoin de `sudo` (par exemple, `sudo npm install -g browser-sync` sur Linux/macOS).

---

C'est tout ! BrowserSync est maintenant prêt à booster votre développement front-end. Commencez avec la commande de base, ajustez selon vos besoins et profitez d'un flux de travail plus fluide. Faites-moi savoir si vous avez besoin d'aide pour une configuration spécifique !