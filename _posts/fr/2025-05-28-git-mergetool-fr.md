---
audio: false
generated: true
lang: fr
layout: post
title: Configuration de TortoiseGit comme outil de fusion Git
translated: true
type: note
---

Pour configurer TortoiseGit comme outil de fusion pour Git, vous devez configurer TortoiseGitMerge (l'outil de fusion inclus avec TortoiseGit) dans votre configuration Git. Voici les étapes pour y parvenir :

### Prérequis
- Assurez-vous que TortoiseGit est installé sur votre système. Vous pouvez le télécharger depuis [tortoisegit.org](https://tortoisegit.org).
- Vérifiez que l'exécutable TortoiseGitMerge est disponible (généralement situé dans `C:\Program Files\TortoiseGit\bin\TortoiseGitMerge.exe`).

### Étapes pour configurer TortoiseGitMerge comme Mergetool Git

1. **Ouvrir une Invite de Commandes ou Git Bash**
   - Vous pouvez utiliser l'Invite de Commandes Windows, PowerShell ou Git Bash pour exécuter les commandes de configuration Git nécessaires.

2. **Définir TortoiseGitMerge comme outil de fusion**
   Exécutez les commandes suivantes pour configurer Git afin qu'il utilise TortoiseGitMerge :

   ```bash
   git config --global merge.tool tortoisegitmerge
   git config --global mergetool.tortoisemerge.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -base:\"$BASE\" -theirs:\"$REMOTE\" -mine:\"$LOCAL\" -merged:\"$MERGED\""
   ```

   **Explication** :
   - `merge.tool tortoisegitmerge` : Définit le nom de l'outil de fusion sur `tortoisegitmerge` (vous pouvez choisir n'importe quel nom, mais c'est une convention).
   - `mergetool.tortoisemerge.cmd` : Spécifie la commande pour exécuter TortoiseGitMerge avec les paramètres appropriés :
     - `-base:"$BASE"` : Le fichier ancêtre commun.
     - `-theirs:"$REMOTE"` : Le fichier provenant de la branche en cours de fusion.
     - `-mine:"$LOCAL"` : Le fichier provenant de votre branche actuelle.
     - `-merged:"$MERGED"` : Le fichier de sortie où la fusion résolue sera enregistrée.
   - Utilisez des barres obliques (`/`) dans le chemin et échappez les guillemets si nécessaire, surtout si le chemin contient des espaces.

   **Remarque** : Ajustez le chemin (`C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe`) si TortoiseGit est installé dans un emplacement différent (par exemple, `E:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe`).

3. **Optionnel : Désactiver l'invite du Mergetool**
   Pour éviter d'être invité à chaque fois que vous exécutez `git mergetool`, vous pouvez désactiver l'invite :

   ```bash
   git config --global mergetool.prompt false
   ```

4. **Optionnel : S'assurer que TortoiseGitMerge est dans le PATH système**
   Si Git ne trouve pas TortoiseGitMerge, assurez-vous que son répertoire est dans la variable d'environnement PATH de votre système :
   - Faites un clic droit sur "Ce PC" ou "Poste de travail" → Propriétés → Paramètres système avancés → Variables d'environnement.
   - Sous "Variables système", trouvez et modifiez la variable `Path` pour inclure `C:\Program Files\TortoiseGit\bin`.
   - Alternativement, définissez explicitement le chemin dans la configuration Git :

     ```bash
     git config --global mergetool.tortoisemerge.path "C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe"
     ```

5. **Tester la configuration**
   - Créez un conflit de fusion dans un dépôt Git (par exemple, en fusionnant deux branches avec des modifications conflictuelles).
   - Exécutez la commande suivante pour lancer l'outil de fusion :

     ```bash
     git mergetool
     ```

   - TortoiseGitMerge devrait s'ouvrir, affichant une vue à trois volets avec les versions de base, theirs et mine du fichier en conflit. Le volet du bas est le résultat fusionné.

6. **Résoudre les conflits dans TortoiseGitMerge**
   - Dans la vue à trois volets, TortoiseGitMerge affiche :
     - **Volet gauche** : La version "theirs" (provenant de la branche en cours de fusion).
     - **Volet droit** : La version "mine" (provenant de votre branche actuelle).
     - **Volet central** : La version de base (ancêtre commun).
     - **Volet inférieur** : Le résultat fusionné où vous résolvez les conflits.
   - Faites un clic droit sur les sections conflictuelles pour choisir des options comme "Utiliser le bloc de texte de 'theirs'", "Utiliser le bloc de texte de 'mine'", ou modifiez manuellement le fichier fusionné.
   - Une fois résolu, enregistrez le fichier (Fichier → Enregistrer) et fermez TortoiseGitMerge.
   - Git marquera le fichier comme résolu si TortoiseGitMerge se ferme avec succès (code de sortie 0). Si vous y êtes invité, confirmez pour marquer le conflit comme résolu.

7. **Valider la fusion résolue**
   Après avoir résolu les conflits, validez les modifications :

   ```bash
   git commit
   ```

   **Remarque** : Si le conflit s'est produit pendant un rebasage ou un cherry-pick, utilisez les boîtes de dialogue TortoiseGit respectives (Rebase ou Cherry-pick) pour continuer le processus au lieu de la boîte de dialogue de validation standard.[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)

### Utiliser TortoiseGitMerge via l'interface graphique de TortoiseGit
Si vous préférez utiliser l'interface graphique de TortoiseGit pour résoudre les conflits :
1. Faites un clic droit sur le fichier en conflit dans l'Explorateur Windows.
2. Sélectionnez **TortoiseGit → Edit Conflicts**.
3. TortoiseGitMerge s'ouvrira, vous permettant de résoudre les conflits comme décrit ci-dessus.
4. Après l'enregistrement, faites à nouveau un clic droit et sélectionnez **TortoiseGit → Resolved** pour marquer le fichier comme résolu.
5. Validez les modifications en utilisant la boîte de dialogue Commit de TortoiseGit.

### Dépannage
- **Erreur : "Unsupported merge tool 'tortoisemerge'"**
  - Assurez-vous que le chemin vers `TortoiseGitMerge.exe` est correct et accessible.
  - Vérifiez que le nom de l'outil correspond exactement dans les configurations `merge.tool` et `mergetool.<tool>.cmd`.
  - Vérifiez que TortoiseGitMerge est dans le PATH ou défini explicitement en utilisant `mergetool.tortoisemerge.path`.[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **Espaces dans les chemins de fichiers**
  - Si les chemins de fichiers contiennent des espaces, la syntaxe de commande avec des guillemets échappés (comme montré ci-dessus) devrait les gérer correctement.[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **Utilisateurs de Cygwin**
  - Si vous utilisez Cygwin, ajustez le chemin pour utiliser le point de montage de Cygwin, par exemple :

    ```bash
    git config --global mergetool.tortoisemerge.cmd '"/cygdrive/c/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe" -base:"$BASE" -theirs:"$REMOTE" -mine:"$LOCAL" -merged:"$MERGED"'
    ```

    Cela tient compte de la structure de chemin `/cygdrive/c/` de Cygwin.[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)
- **TortoiseGitMerge introuvable**
  - Si vous utilisiez précédemment TortoiseMerge de TortoiseSVN, assurez-vous de pointer vers `TortoiseGitMerge.exe`, car le nom de l'exécutable a changé dans TortoiseGit version 1.8.[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/15881449/why-doesnt-tortoisemerge-work-as-my-mergetool)

### Notes supplémentaires
- TortoiseGitMerge prend en charge une vue à trois volets pour la résolution de conflits, ce qui est idéal pour la fusion. Il fusionne automatiquement les modifications non conflictuelles et met en évidence les conflits pour une résolution manuelle.[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://manios.org/2018/05/30/git-merge-conflicts-using-tortoise-git-merge-windows)
- Si vous souhaitez également utiliser TortoiseGitMerge comme outil de diff, configurez-le de manière similaire :

  ```bash
  git config --global diff.tool tortoisediff
  git config --global difftool.tortoisediff.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -mine:\"$REMOTE\" -base:\"$LOCAL\""
  ```

  Utilisez ensuite `git difftool` pour comparer les fichiers.[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)
- Pour les paramètres avancés, vous pouvez configurer TortoiseGit pour qu'il attende la fermeture de l'outil de fusion et marque automatiquement les fichiers comme résolus en fonction du code de sortie. Dans Paramètres de TortoiseGit → Programmes externes → Outil de fusion, sélectionnez "Bloquer TortoiseGit pendant l'exécution de l'outil de fusion externe" et activez "Trust exit code."[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-settings.html)

### Sources
- Documentation TortoiseGit :[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-merge.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)
- Stack Overflow et autres ressources web :[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)

En suivant ces étapes, vous devriez pouvoir utiliser TortoiseGitMerge efficacement comme votre mergetool Git, que ce soit depuis la ligne de commande ou via l'interface graphique de TortoiseGit.