---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Hôte d'Extension de Lancement dans VSCode
translated: true
type: note
---

Pour appuyer sur **F5** dans Visual Studio Code (VSCode) pour lancer l’**Extension Development Host** afin de développer une extension VSCode, suivez ces étapes :

1. **Ouvrez votre projet d’extension dans VSCode** :
   - Assurez-vous d’avoir un projet d’extension VSCode configuré. Celui-ci inclut généralement un fichier `package.json` avec les configurations d’extension nécessaires (par exemple, `contributes`, `activationEvents`).
   - Ouvrez le dossier contenant votre projet d’extension dans VSCode en sélectionnant `Fichier > Ouvrir un dossier` ou en utilisant `Ctrl+K, Ctrl+O` (Windows/Linux) ou `Cmd+K, Cmd+O` (Mac).

2. **Vérifiez la configuration de votre extension** :
   - Assurez-vous d’avoir un fichier `package.json` valide dans la racine de votre projet avec au moins les champs suivants :
     ```json
     {
       "name": "your-extension-name",
       "displayName": "Your Extension Name",
       "description": "Description of your extension",
       "version": "0.0.1",
       "engines": {
         "vscode": "^1.60.0"
       },
       "categories": ["Other"],
       "activationEvents": ["*"],
       "main": "./extension.js",
       "contributes": {}
     }
     ```
   - Assurez-vous d’avoir un fichier `extension.js` (ou équivalent) comme point d’entrée pour votre code d’extension.
   - Installez les dépendances en exécutant `npm install` dans le terminal intégré (`Ctrl+``) si votre extension utilise des modules Node.js.

3. **Appuyez sur F5 pour lancer l’Extension Development Host** :
   - Appuyez sur **F5** de votre clavier pendant que votre projet d’extension est ouvert dans VSCode.
   - Cela démarre l’**Extension Development Host**, une fenêtre VSCode séparée où votre extension est chargée pour les tests.
   - VSCode va automatiquement :
     - Construire votre extension (si vous utilisez TypeScript, il compile les fichiers `.ts` en `.js`).
     - Lancer une nouvelle instance de VSCode avec votre extension activée.
     - Ouvrir un débogueur attaché au processus Extension Host.

4. **Configuration du débogage** :
   - VSCode utilise un fichier `launch.json` dans le dossier `.vscode` pour configurer le débogage. S’il n’existe pas, VSCode en créera un automatiquement lorsque vous appuierez sur F5 pour la première fois.
   - Un `launch.json` typique pour une extension ressemble à ceci :
     ```json
     {
       "version": "0.2.0",
       "configurations": [
         {
           "name": "Run Extension",
           "type": "extensionHost",
           "request": "launch",
           "args": ["--extensionDevelopmentPath=${workspaceFolder}"],
           "outFiles": ["${workspaceFolder}/out/**/*.js"],
           "preLaunchTask": "npm: watch"
         }
       ]
     }
     ```
   - Assurez-vous que la `preLaunchTask` (si présente) correspond à une tâche dans votre `tasks.json` (par exemple, pour compiler TypeScript).

5. **Testez votre extension** :
   - Dans la fenêtre Extension Development Host, votre extension devrait être active. Testez ses fonctionnalités (par exemple, commandes, contributions d’interface) comme défini dans votre `package.json` et votre code.
   - Utilisez la **Console de débogage** dans la fenêtre principale de VSCode pour voir les journaux ou les erreurs de votre extension.

6. **Dépannage** :
   - Si F5 ne fonctionne pas :
     - Assurez-vous que Node.js et npm sont installés, car ils sont requis pour le développement d’extensions.
     - Vérifiez que vous avez installé les dépendances de l’API d’extension VSCode (`npm install @types/vscode`).
     - Vérifiez que la configuration `launch.json` pointe vers les chemins corrects.
     - Si vous voyez des erreurs, vérifiez le panneau **Sortie** (sélectionnez "Extension" dans la liste déroulante) dans la fenêtre Extension Development Host.
   - Si l’Extension Host ne se lance pas, assurez-vous que votre projet n’a pas d’erreurs de syntaxe dans `package.json` ou votre fichier d’extension principal.

**Notes supplémentaires** :
- Vous pouvez également démarrer l’Extension Development Host en ouvrant le panneau **Exécuter et déboguer** (`Ctrl+Shift+D` ou `Cmd+Shift+D` sur Mac) et en sélectionnant « Run Extension » dans la liste déroulante, puis en cliquant sur le bouton de lecture vert.
- Pour recharger l’Extension Host après avoir apporté des modifications, utilisez `Ctrl+R` (Windows/Linux) ou `Cmd+R` (Mac) dans la fenêtre Extension Development Host, ou redémarrez-la avec F5.

Pour plus de détails, consultez le guide officiel de développement d’extensions VSCode :  
[VS Code Extension Development](https://code.visualstudio.com/api/get-started/your-first-extension)