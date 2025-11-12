---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser concurremment
translated: true
type: note
---

Il semble que vous demandiez comment utiliser "concurrently" dans le contexte du développement frontend. Cependant, "concurrently" est généralement un package Node.js utilisé pour exécuter plusieurs commandes ou scripts simultanément, souvent dans un contexte backend ou de workflow de développement plutôt que directement dans le code frontend. Vouliez-vous dire comment l'utiliser dans la configuration d'un projet frontend (par exemple, pour exécuter des scripts), ou faisiez-vous référence à autre chose comme les opérations concurrentes en JavaScript frontend (par exemple, les promesses, async/await) ? Je vais supposer le premier cas pour l'instant, mais n'hésitez pas à clarifier !

### Utilisation de `concurrently` dans un Projet Frontend

Si vous travaillez sur un projet frontend (par exemple, avec React, Vue ou Angular), `concurrently` est couramment utilisé en développement pour exécuter plusieurs processus simultanément—comme démarrer un serveur de développement et un watcher de build. Voici comment vous pouvez l'utiliser :

#### 1. Installer `concurrently`
D'abord, installez-le comme dépendance de développement dans votre projet :
```bash
npm install --save-dev concurrently
```

#### 2. Ajouter des Scripts dans `package.json`
Définissez les scripts que vous souhaitez exécuter simultanément dans votre `package.json`. Par exemple, si vous exécutez un serveur de développement frontend et un préprocesseur CSS comme Sass :
```json
{
  "scripts": {
    "start:frontend": "react-scripts start", // ou votre commande de dev frontend
    "watch:css": "sass --watch src/styles:dist/styles",
    "dev": "concurrently \"npm run start:frontend\" \"npm run watch:css\""
  }
}
```

- `start:frontend` : Exécute votre serveur de développement frontend (par exemple, React, Vite, etc.).
- `watch:css` : Surveille et compile vos fichiers CSS.
- `dev` : Utilise `concurrently` pour exécuter les deux commandes en même temps.

#### 3. Exécuter les Scripts Concurrents
Dans votre terminal, exécutez simplement :
```bash
npm run dev
```
Cela démarrera à la fois le serveur frontend et le watcher CSS simultanément. Vous verrez la sortie des deux processus dans le même terminal, et `concurrently` les maintiendra en cours d'exécution ensemble.

#### 4. Configuration Optionnelle
Vous pouvez personnaliser `concurrently` avec des options comme :
- `--kill-others` : Arrête tous les processus si l'un d'eux échoue.
- `--names` : Étiquette chaque processus pour une sortie plus claire.

Exemple avec des options dans `package.json` :
```json
"dev": "concurrently --names \"Frontend,CSS\" --kill-others \"npm run start:frontend\" \"npm run watch:css\""
```
La sortie pourrait ressembler à :
```
[Frontend] Démarrage du serveur frontend...
[CSS] Surveillance des fichiers CSS...
```

#### Cas d'Usage dans un Workflow Frontend
Imaginez que vous construisez une application React avec un serveur API séparé :
- Frontend : `npm run start` (serveur de développement React sur le port 3000).
- API : `npm run start:api` (par exemple, serveur Node.js sur le port 5000).
Avec `concurrently`, vous pouvez exécuter les deux :
```json
"dev": "concurrently \"npm run start\" \"npm run start:api\""
```

### Si Vous Vouliez Dire JavaScript Concurrent dans le Frontend
Si vous demandiez comment gérer les opérations concurrentes dans le code frontend (par exemple, récupérer plusieurs API à la fois), voici un exemple rapide utilisant `Promise.all` :
```javascript
async function fetchData() {
  const [userData, postsData] = await Promise.all([
    fetch('https://api.example.com/user').then(res => res.json()),
    fetch('https://api.example.com/posts').then(res => res.json())
  ]);
  console.log(userData, postsData);
}
fetchData();
```
Ceci exécute les appels API de manière concurrente et attend que les deux se résolvent.

### Clarifiez Si Nécessaire !
Faites-moi savoir si vous vouliez dire quelque chose de différent par "concurrently in frontend"—comme une bibliothèque spécifique, un framework ou un cas d'usage particulier—et j'adapterai la réponse en conséquence !