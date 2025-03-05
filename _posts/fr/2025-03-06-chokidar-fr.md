---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation de Chokidar pour la surveillance des fichiers
translated: true
---

Chokidar est une bibliothèque Node.js principalement conçue pour la surveillance des fichiers côté serveur, donc l'utiliser directement dans le frontend (c'est-à-dire dans un environnement de navigateur) n'est pas son cas d'utilisation typique. Le navigateur n'a pas accès direct au système de fichiers comme Node.js, ce qui fait que Chokidar est plus adapté aux environnements backend ou de build. Cependant, si vous travaillez sur un projet où vous utilisez un bundler comme Webpack, Vite ou Parcel dans un environnement de développement, ou si vous construisez une application Electron (qui combine Node.js avec un frontend), vous pourriez utiliser Chokidar indirectement. Laissez-moi clarifier comment vous pourriez aborder cela en fonction du contexte.

### Pourquoi Chokidar ne fonctionne pas directement dans le navigateur
- Chokidar s'appuie sur les API Node.js comme `fs` (système de fichiers) pour surveiller les fichiers, qui ne sont pas disponibles dans un environnement de navigateur.
- Le code frontend s'exécute dans un environnement sandboxé (le navigateur), où l'accès au système de fichiers est restreint pour des raisons de sécurité.

### Scénarios possibles pour utiliser Chokidar dans un contexte "frontend"
Voici comment vous pourriez utiliser Chokidar de manière liée au développement frontend :

#### 1. **Pendant le développement avec un outil de build**
Si vous parlez d'utiliser Chokidar pour surveiller les fichiers (par exemple, pour le rechargement à chaud ou les mises à jour en direct) pendant le développement frontend, vous l'intégreriez dans votre processus de build plutôt que dans le runtime du navigateur.

Exemple avec un script Node.js personnalisé :
```javascript
const chokidar = require('chokidar');

// Surveiller les changements dans vos fichiers sources frontend
chokidar.watch('./src/**/*.{html,js,css}').on('all', (event, path) => {
  console.log(event, path);
  // Déclencher une nouvelle construction ou notifier votre serveur de développement frontend ici
});
```
- **Cas d'utilisation** : Vous pourriez l'associer à une connexion WebSocket pour pousser les mises à jour vers le navigateur pendant le développement.
- **Outils** : Combinez-le avec quelque chose comme `esbuild` ou un serveur de développement (par exemple, Vite a déjà une surveillance de fichiers intégrée, mais vous pourriez la personnaliser avec Chokidar).

#### 2. **Dans une application Electron**
Si votre "frontend" fait partie d'une application Electron, vous pouvez utiliser Chokidar dans le processus principal (Node.js) et communiquer les changements au processus de rendu (frontend).

Exemple :
```javascript
// main.js (processus principal Electron)
const { ipcMain } = require('electron');
const chokidar = require('chokidar');

chokidar.watch('./files').on('change', (path) => {
  ipcMain.send('file-changed', path); // Envoyer l'événement au rendu
});
```
```javascript
// renderer.js (Frontend)
const { ipcRenderer } = require('electron');

ipcRenderer.on('file-changed', (event, path) => {
  console.log(`Fichier changé : ${path}`);
  // Mettre à jour l'interface utilisateur en conséquence
});
```

#### 3. **Frontend avec un proxy backend**
Si vous construisez une application web et que vous souhaitez une fonctionnalité de surveillance de fichiers, vous exécuteriez Chokidar sur un backend Node.js et enverriez les mises à jour au frontend via WebSockets ou Server-Sent Events.

Exemple (Backend avec Express et WebSocket) :
```javascript
const express = require('express');
const WebSocket = require('ws');
const chokidar = require('chokidar');

const app = express();
const server = app.listen(3000);
const wss = new WebSocket.Server({ server });

chokidar.watch('./public').on('change', (path) => {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(`Fichier changé : ${path}`);
    }
  });
});
```
Frontend (exemple React) :
```javascript
const socket = new WebSocket('ws://localhost:3000');
socket.onmessage = (event) => {
  console.log(event.data); // "Fichier changé : ..."
  // Mettre à jour l'état ou l'interface utilisateur
};
```

### Installation
Pour utiliser Chokidar dans l'une de ces configurations, vous l'installeriez d'abord dans votre projet Node.js :
```bash
npm install chokidar
```

### Méthodes clés de Chokidar
- `chokidar.watch(path, [options])` : Commencer à surveiller un fichier ou un répertoire.
- Événements : `.on('add', callback)`, `.on('change', callback)`, `.on('unlink', callback)`, `.on('all', (event, path) => {})`.
- Options : `{ ignored: /node_modules/, persistent: true }` (personnalisez selon vos besoins).

### Si vous vouliez dire autre chose
Si vous ne travaillez pas du tout dans un environnement Node.js et que vous souhaitez un comportement de surveillance de fichiers purement dans le navigateur (par exemple, surveiller les changements de `<input type="file">`), faites-le moi savoir ! Cela impliquerait l'API `File` et les écouteurs d'événements, pas Chokidar.

Quel est votre configuration ou votre objectif spécifique ? Je peux adapter cela davantage !