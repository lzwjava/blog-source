---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Corriger la touche Fn + F5 dans VSCode sur Mac
translated: true
type: note
---

Si appuyer sur **Fn + F5** sur votre Mac dans Visual Studio Code (VSCode) n'a aucun effet lorsque vous essayez de lancer l'**Extension Development Host**, cela est probablement dû à la configuration de la touche `Fn` et des touches de fonction sur votre Mac, à un conflit dans les raccourcis clavier de VSCode, ou à une mauvaise configuration de votre environnement de développement d'extension. Ci-dessous, j'expliquerai pourquoi cela peut arriver et comment le résoudre.

### Pourquoi **Fn + F5** ne fonctionne pas sur votre Mac

1. **Comportement des touches de fonction sur Mac** :
   - Sur les claviers Mac, les touches de fonction (F1–F12) sont souvent assignées par défaut à des fonctions système (par exemple, F5 peut contrôler la luminosité du clavier ou la lecture multimédia).
   - La touche `Fn` est utilisée pour accéder au comportement « standard » des touches de fonction (par exemple, `Fn + F5` envoie le véritable signal de la touche F5 au lieu d'une fonction système).
   - Si `Fn + F5` ne déclenche pas l'action attendue dans VSCode, les paramètres de clavier de votre Mac ou les raccourcis clavier de VSCode n'interprètent peut-être pas correctement l'entrée.

2. **Conflit ou mauvaise configuration des raccourcis clavier de VSCode** :
   - VSCode n'a peut-être pas `F5` (ou `Fn + F5`) mappé à la commande « Run Extension » pour lancer l'Extension Development Host.
   - Une autre extension ou un raccourci personnalisé pourrait écraser `F5`.

3. **Problème de configuration du développement d'extension** :
   - Si votre projet d'extension VSCode n'est pas correctement configuré (par exemple, `launch.json` manquant ou incorrect), appuyer sur `F5` (avec ou sans `Fn`) ne lancera pas l'Extension Development Host.

4. **Paramètres système macOS** :
   - macOS pourrait intercepter la touche `F5` pour une fonction système, ou le comportement de la touche `Fn` pourrait être personnalisé d'une manière qui affecte la capacité de VSCode à la détecter.

### Étapes pour résoudre le problème de **Fn + F5** ne fonctionnant pas dans VSCode sur Mac

#### 1. **Vérifier les paramètres clavier de macOS**
   - **Activer le comportement standard des touches de fonction** :
     - Allez dans **Préférences Système > Clavier**.
     - Cochez la case **« Utiliser les touches F1, F2, etc. comme des touches de fonction standard »**.
     - Si cette option est activée, vous pouvez appuyer directement sur `F5` (sans `Fn`) pour envoyer le signal de la touche F5 à VSCode. Essayez d'appuyer sur `F5` seul pour voir si cela lance l'Extension Development Host.
     - Si cette option n'est pas cochée, vous devez appuyer sur `Fn + F5` pour envoyer F5, car `F5` seul peut contrôler une fonction système (par exemple, la luminosité du clavier).
   - **Tester le comportement de F5** :
     - Ouvrez un éditeur de texte (par exemple, TextEdit) et appuyez sur `F5` et `Fn + F5`. Si `F5` seul déclenche une action système (comme la luminosité) et que `Fn + F5` ne fait rien, la touche `Fn` fonctionne comme prévu pour envoyer le signal F5 standard.
   - **Réinitialiser la NVRAM/PRAM** (si nécessaire) :
     - Redémarrez votre Mac et maintenez enfoncées les touches `Cmd + Option + P + R` jusqu'à entendre la sonnerie de démarrage deux fois (ou jusqu'à ce que le logo Apple apparaisse deux fois sur les Mac plus récents). Cela réinitialise les paramètres liés au clavier et peut résoudre les problèmes de détection.

#### 2. **Vérifier les raccourcis clavier de VSCode**
   - Ouvrez VSCode et allez dans **Code > Préférences > Raccourcis clavier** (`Cmd+K, Cmd+S`).
   - Dans la barre de recherche, tapez `F5` ou `Run Extension`.
   - Cherchez la commande **« Debug: Start Debugging »** ou **« Run Extension »** (associée au lancement de l'Extension Development Host).
   - Assurez-vous qu'elle est mappée à `F5`. Sinon, double-cliquez sur la commande, appuyez sur `F5` (ou `Fn + F5` si nécessaire), et enregistrez le nouveau raccourci.
   - Vérifiez les conflits : Recherchez d'autres commandes liées à `F5` ou `Fn + F5` et supprimez-les ou réaffectez-les.
   - Réinitialisez les raccourcis si nécessaire : Cliquez sur les trois points (`...`) dans l'éditeur de Raccourcis clavier et sélectionnez **Reset Keybindings**.

#### 3. **Vérifier la configuration de votre projet d'extension**
   - Assurez-vous que votre projet d'extension est correctement configuré :
     - Ouvrez le dossier de votre projet d'extension dans VSCode (doit contenir `package.json` et `extension.js` ou équivalent).
     - Vérifiez que `package.json` possède les champs requis :
       ```json
       {
         "name": "your-extension-name",
         "displayName": "Your Extension Name",
         "version": "0.0.1",
         "engines": {
           "vscode": "^1.60.0"
         },
         "categories": ["Other"],
         "activationEvents": ["*"],
         "main": "./extension.js"
       }
       ```
   - Vérifiez la présence d'un fichier `.vscode/launch.json` :
     - S'il n'existe pas, VSCode devrait en créer un lorsque vous appuyez sur `F5`. Sinon, créez-le manuellement dans le dossier `.vscode` avec :
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
     - Assurez-vous que la `preLaunchTask` (par exemple, `npm: watch`) correspond à une tâche dans `.vscode/tasks.json` si vous utilisez TypeScript ou une étape de build.
   - Exécutez `npm install` dans le terminal VSCode (`Cmd+``) pour vous assurer que les dépendances (par exemple, `@types/vscode`) sont installées.

#### 4. **Tester le lancement de l'Extension Development Host**
   - Avec votre projet d'extension ouvert, essayez d'appuyer sur `F5` (ou `Fn + F5` si le paramètre « Utiliser F1, F2, etc. comme touches de fonction standard » est désactivé).
   - Alternativement, ouvrez le panneau **Run and Debug** (`Cmd+Shift+D`), sélectionnez **« Run Extension »** dans le menu déroulant et cliquez sur le bouton de lecture vert.
   - Si l'Extension Development Host ne se lance pas :
     - Vérifiez le panneau **Output** (`Cmd+Shift+U`) et sélectionnez **« Extension »** dans le menu déroulant pour voir les erreurs éventuelles.
     - Vérifiez la **Debug Console** pour les erreurs liées à votre extension ou au processus de débogage.
     - Assurez-vous que Node.js est installé (`node -v` dans le terminal) et que votre projet n'a pas d'erreurs de syntaxe.

#### 5. **Tester avec un clavier différent**
   - Connectez un clavier USB externe à votre Mac et appuyez sur `F5` (ou `Fn + F5`) dans VSCode.
   - Si cela fonctionne, le problème vient peut-être du matériel ou du firmware du clavier intégré de votre Mac. Vérifiez les mises à jour du firmware du clavier auprès du fabricant de votre Mac (par exemple, Apple Software Update).

#### 6. **Mettre à jour VSCode et macOS**
   - Assurez-vous que VSCode est à jour : Allez dans **Code > Check for Updates** ou téléchargez la dernière version sur le site web de VSCode.
   - Mettez à jour macOS : Allez dans **Préférences Système > Général > Mise à jour de logiciel** pour installer les mises à jour disponibles, car elles peuvent inclure des correctifs pour les pilotes de clavier.

#### 7. **Désactiver les extensions ou logiciels interférents**
   - **Extensions VSCode** :
     - Désactivez toutes les extensions : Exécutez `code --disable-extensions` dans un terminal, puis ouvrez VSCode et réessayez `F5`.
     - Si cela fonctionne, réactivez les extensions une par une pour identifier celle qui pose problème.
   - **Logiciels tiers** :
     - Vérifiez les outils de remappage de clavier comme Karabiner-Elements ou BetterTouchTool. Ouvrez leurs paramètres et assurez-vous que `F5` ou `Fn + F5` n'est pas remappé.
     - Désactivez temporairement ces outils pour tester.

#### 8. **Journaux de débogage**
   - Activez les outils de développement de VSCode pour inspecter les événements clavier :
     - Ouvrez VSCode, appuyez sur `Cmd+Option+I` pour ouvrir les Developer Tools.
     - Allez dans l'onglet **Console** et appuyez sur `Fn + F5`. Cherchez les journaux d'événements clavier pour voir si VSCode reçoit la bonne entrée.
   - Si aucun événement clavier n'est enregistré, le problème se situe probablement au niveau du système (macOS ou matériel du clavier).

### Si le problème persiste
   - Fournissez plus de détails :
     - La version de macOS (par exemple, Ventura, Sonoma).
     - La version de VSCode (vérifiez via **Code > About Visual Studio Code**).
     - Le type de clavier (par exemple, clavier intégré du MacBook, modèle de clavier externe).
     - Si `F5` ou `Fn + F5` fonctionne dans d'autres applications (par exemple, est-ce que `F5` actualise un navigateur ?).
     - Les messages d'erreur dans le panneau **Output** ou la **Debug Console** de VSCode.
   - Essayez de créer un projet d'extension minimal pour isoler le problème :
     - Exécutez `yo code` (nécessite Yeoman et le générateur VSCode : `npm install -g yo generator-code`) pour générer une nouvelle extension.
     - Ouvrez le nouveau projet dans VSCode et appuyez sur `F5` pour voir si cela lance l'Extension Development Host.

[VS Code Extension Development](https://code.visualstudio.com/api/get-started/your-first-extension)  
[Mac Keyboard Settings](https://support.apple.com/guide/mac-help/change-the-behavior-of-the-function-keys-mchlp2882/mac)  
[VS Code Keybindings](https://code.visualstudio.com/docs/getstarted/keybindings)