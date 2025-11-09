---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Curseur VS Code en ligne
translated: true
type: note
---

### Rétablir le curseur en forme de ligne dans VS Code

J'ai compris — il semble que votre curseur soit passé en style bloc/rectangle (fréquent en mode de remplacement ou avec certains paramètres par défaut), mais vous préférez le style **ligne** verticale fine pour une édition plus facile. C'est un simple ajustement des paramètres. Suivez ces étapes précisément :

#### Via l'interface des paramètres (Plus simple) :
1. Ouvrez VS Code.
2. Appuyez sur `Ctrl + ,` (Windows/Linux) ou `Cmd + ,` (macOS) pour ouvrir les Paramètres.
3. Dans la barre de recherche en haut, tapez : **cursor style**.
4. Cherchez **Editor: Cursor Style** (sous Text Editor > Cursor).
5. Cliquez sur le menu déroulant et sélectionnez **Line** (cela pourrait actuellement indiquer "Block").
6. Le changement est instantané — essayez de taper dans un fichier pour voir le curseur fin en forme de ligne.

S'il ne se met toujours pas à jour, fermez et rouvrez VS Code, ou redémarrez-le complètement.

#### Via settings.json (Pour plus de précision) :
1. Ouvrez la Palette de commandes : `Ctrl + Shift + P` (ou `Cmd + Shift + P` sur macOS).
2. Tapez et sélectionnez : **Preferences: Open User Settings (JSON)**.
3. Ajoutez ou modifiez cette ligne à l'intérieur des `{}` (créez le fichier s'il est vide) :
   ```json:disable-run
   "editor.cursorStyle": "line"
   ```
4. Enregistrez le fichier (`Ctrl + S` ou `Cmd + S`).

#### Conseils supplémentaires :
- **Mode de remplacement ?** Si vous êtes accidentellement en mode "overwrite" (où il remplace les caractères), appuyez sur la touche **Insert** de votre clavier pour revenir au mode d'insertion.
- **Problème de clignotement ?** Si la ligne semble saccadée, recherchez **cursor blinking** dans les paramètres et réglez-le sur **Blink** ou **Smooth**.
- **Des extensions interfèrent ?** Désactivez temporairement des extensions comme Vim (vue Extensions > clic droit > Disable) pour tester.

Cela devrait vous redonner ce curseur en forme de ligne propre immédiatement. S'il reste en forme de rectangle après cela, partagez votre OS ou une capture d'écran pour une aide plus ciblée !

[Documentation sur le curseur VS Code](https://code.visualstudio.com/docs/editor/codebasics#_cursor-style)