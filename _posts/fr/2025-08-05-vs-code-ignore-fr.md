---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Exclure les fichiers ignorés dans VS Code
translated: true
type: note
---

Vous pouvez faire en sorte que « Aller au fichier » (Ouvrir rapidement, Ctrl + P) inclue les fichiers qui se trouvent dans votre `.gitignore` en modifiant trois paramètres dans votre `settings.json` :

1. **Demander à la recherche d'ignorer les règles de votre `.gitignore`**

   ```jsonc
   "search.useIgnoreFiles": false,      // ne pas respecter .gitignore
   "search.useGlobalIgnoreFiles": false // ne pas respecter votre gitignore global
   ```
2. **S'assurer que vos globs d'exclusion ne masquent pas ces fichiers**
   Par défaut, VS Code hérite de tous les modèles de `files.exclude` dans `search.exclude`. Si vous avez manuellement exclu les répertoires `.gitignore` là-dedans, réactivez-les :

   ```jsonc
   "search.exclude": {
     "**/.git": false,          // indexer .git (si vous le souhaitez)
     "**/.gitignore": false     // surtout ne pas masquer votre fichier .gitignore lui-même
     // …tout autre modèle que vous souhaitez remplacer
   }
   ```
3. **Recharger la fenêtre**
   Après avoir sauvegardé vos paramètres utilisateur ou d'espace de travail, exécutez **Developer: Reload Window** (⇧ ⌘ P → “Reload Window”) pour que l'indexeur de fichiers prenne en compte le changement.

Maintenant, lorsque vous appuierez sur Ctrl + P, vous verrez *tous* les fichiers par nom — ignorés ou non. ([stackoverflow.com][1])

[1]: https://stackoverflow.com/questions/62855190/how-do-you-include-git-ignored-files-in-vscode-quick-search?utm_source=chatgpt.com "How do you include git ignored files in VSCode quick search"