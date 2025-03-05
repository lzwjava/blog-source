---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser ShellJS pour exécuter des commandes shell
translated: true
---

ShellJS est une bibliothèque JavaScript qui fournit des commandes de shell Unix (comme `cp`, `mkdir`, `exec`, etc.) pour une utilisation dans les projets Node.js. Elle simplifie l'écriture de scripts multiplateformes en vous permettant d'exécuter des commandes de shell familières directement en JavaScript. Cependant, en ce qui concerne le développement frontend—qui fait généralement référence au code qui s'exécute dans le navigateur—ShellJS n'est pas directement applicable car il repose sur les API Node.js non disponibles dans l'environnement du navigateur. Ci-dessous, je vais expliquer pourquoi c'est le cas et comment vous pouvez toujours utiliser ShellJS de manière efficace dans le contexte des flux de travail de développement frontend.

### Pourquoi ShellJS ne peut pas s'exécuter directement dans le navigateur
- **Dépendance Node.js**: ShellJS est construit au-dessus du runtime Node.js, qui fournit des API pour l'accès au système de fichiers, l'exécution de processus et d'autres opérations au niveau du système. Ces API ne sont pas disponibles dans le navigateur en raison de son modèle de sécurité en sandbox.
- **Restrictions de sécurité du navigateur**: Les navigateurs empêchent JavaScript d'accéder au système de fichiers local ou d'exécuter des commandes arbitraires pour protéger les utilisateurs des scripts malveillants. Puisque les commandes ShellJS comme `exec` (pour exécuter des processus externes) ou `cp` (pour copier des fichiers) dépendent de ces capacités, elles ne peuvent pas fonctionner dans un environnement de navigateur.

En conséquence, vous ne pouvez pas utiliser ShellJS directement dans le JavaScript côté client qui s'exécute dans le navigateur. Cependant, ShellJS peut toujours jouer un rôle précieux dans le développement frontend en l'intégrant dans vos processus de construction ou vos outils de développement, qui s'exécutent généralement sur Node.js.

### Comment utiliser ShellJS dans les flux de travail de développement frontend
Bien que ShellJS ne s'exécute pas dans le navigateur, vous pouvez l'utiliser dans des scripts basés sur Node.js pour automatiser des tâches qui soutiennent votre développement frontend. Les projets frontend s'appuient souvent sur des outils de construction comme Webpack, Gulp ou Grunt, qui s'exécutent sur Node.js et peuvent intégrer ShellJS pour rationaliser les flux de travail. Voici comment faire :

#### 1. Installer ShellJS
Assurez-vous d'avoir Node.js installé sur votre système. Ensuite, ajoutez ShellJS à votre projet en utilisant npm ou yarn :

```bash
npm install shelljs
```

ou

```bash
yarn add shelljs
```

#### 2. Créer un script Node.js avec ShellJS
Rédigez un script qui utilise ShellJS pour effectuer des tâches pertinentes pour votre projet frontend, comme copier des fichiers, créer des répertoires ou exécuter des outils en ligne de commande. Enregistrez ce script sous forme de fichier `.js` (par exemple, `build.js`).

Voici un exemple de script qui prépare les actifs frontend :

```javascript
const shell = require('shelljs');

// Créer un répertoire de construction s'il n'existe pas
shell.mkdir('-p', 'build');

// Copier les fichiers HTML dans le répertoire de construction
shell.cp('-R', 'src/*.html', 'build/');

// Compiler Sass en CSS
shell.exec('sass src/styles.scss build/styles.css');

// Copier les fichiers JavaScript
shell.cp('-R', 'src/*.js', 'build/');
```

- **`shell.mkdir('-p', 'build')`**: Crée un répertoire `build`, avec `-p` pour s'assurer qu'il n'y a pas d'erreur s'il existe déjà.
- **`shell.cp('-R', 'src/*.html', 'build/')`**: Copie tous les fichiers HTML de `src` vers `build`, avec `-R` pour la copie récursive.
- **`shell.exec('sass src/styles.scss build/styles.css')`**: Exécute le compilateur Sass pour générer du CSS.

#### 3. Intégrer le script dans votre flux de travail
Vous pouvez exécuter ce script de plusieurs manières :
- **Directement via Node.js** :
  ```bash
  node build.js
  ```
- **En tant que script npm** : Ajoutez-le à votre `package.json` :
  ```json
  "scripts": {
    "build": "node build.js"
  }
  ```
  Ensuite, exécutez :
  ```bash
  npm run build
  ```
- **Avec des outils de construction** : Intégrez ShellJS dans des outils comme Gulp. Par exemple :
  ```javascript
  const gulp = require('gulp');
  const shell = require('shelljs');

  gulp.task('build', function(done) {
    shell.exec('sass src/styles.scss build/styles.css');
    shell.cp('-R', 'src/*.js', 'build/');
    done();
  });
  ```

#### 4. Cas d'utilisation dans le développement frontend
ShellJS peut automatiser diverses tâches dans votre flux de travail frontend :
- **Gestion des actifs** : Copier des images, des polices ou d'autres fichiers statiques dans un répertoire de construction.
- **Traitement CSS/JavaScript** : Exécuter des outils comme Sass, PostCSS ou UglifyJS via `shell.exec`.
- **Tests et linting** : Exécuter des runners de tests ou des linters (par exemple, `shell.exec('eslint src/*.js')`).
- **Préparation au déploiement** : Regrouper des fichiers ou nettoyer des répertoires (par exemple, `shell.rm('-rf', 'build/*')`).

### Exemple : Automatisation d'un processus de construction frontend
Imaginez que vous construisez une simple application web avec HTML, Sass et JavaScript. Voici comment vous pourriez utiliser ShellJS pour automatiser la construction :

**Structure du répertoire** :
```
project/
├── src/
│   ├── index.html
│   ├── styles.scss
│   └── app.js
├── build.js
└── package.json
```

**build.js** :
```javascript
const shell = require('shelljs');

// Nettoyer le répertoire de construction
shell.rm('-rf', 'build/*');

// Créer le répertoire de construction
shell.mkdir('-p', 'build');

// Copier HTML
shell.cp('src/index.html', 'build/');

// Compiler Sass
shell.exec('sass src/styles.scss build/styles.css');

// Copier JavaScript
shell.cp('src/app.js', 'build/');
```

**package.json** :
```json
{
  "scripts": {
    "build": "node build.js"
  },
  "dependencies": {
    "shelljs": "^0.8.5"
  }
}
```

Exécutez `npm run build`, et ShellJS préparera votre répertoire `build` avec les fichiers compilés et copiés, prêts pour le déploiement.

### Points clés
- **Non pour l'utilisation dans le navigateur** : ShellJS ne peut pas s'exécuter dans le navigateur en raison de sa dépendance à Node.js et aux opérations au niveau du système.
- **Parfait pour les scripts de construction** : Utilisez-le dans des scripts basés sur Node.js pour automatiser les tâches frontend comme la manipulation de fichiers et l'exécution de commandes.
- **Multiplateforme** : ShellJS garantit que vos scripts fonctionnent de manière cohérente sur Windows, Linux et macOS, ce qui en fait un choix idéal pour des environnements de développement diversifiés.

En intégrant ShellJS dans vos processus de construction alimentés par Node.js, vous pouvez améliorer votre flux de travail de développement frontend avec une automatisation puissante, même s'il ne s'exécute pas directement dans le navigateur.