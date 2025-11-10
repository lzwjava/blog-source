---
audio: false
generated: true
lang: fr
layout: post
title: Terminal GNOME avec répertoire personnalisé
translated: true
type: note
---

Pour personnaliser le titre de l'onglet du GNOME Terminal afin qu'il n'affiche que le répertoire courant (par exemple, `blog-server`) au lieu du format par défaut (par exemple, `lzw@lzw-MS:~/Projects/blog-server`), vous pouvez modifier l'invite de commande (prompt) ou les paramètres de titre du terminal. Voici comment procéder :

### Étapes pour définir le titre de l'onglet du GNOME Terminal afin qu'il n'affiche que le répertoire courant

1. **Modifier le fichier de configuration Bash** :
   Le GNOME Terminal utilise le shell Bash par défaut, et le titre de l'onglet est souvent dérivé de la variable `PS1` (prompt) ou d'une commande spécifique de définition du titre. Pour personnaliser le titre, vous pouvez modifier le fichier `~/.bashrc`.

2. **Modifier le titre du terminal** :
   Ajoutez une commande pour définir le titre du terminal sur le répertoire courant dans votre `~/.bashrc`. Ouvrez le fichier dans un éditeur de texte :

   ```bash
   nano ~/.bashrc
   ```

   Ajoutez les lignes suivantes à la fin du fichier :

   ```bash
   # Définir le titre de l'onglet du terminal sur le répertoire courant
   case "$TERM" in
   xterm*|rxvt*)
       PS1="\[\e]0;\W\a\]$PS1"
       ;;
   *)
       ;;
   esac
   ```

   **Explication** :
   - `\e]0;...` définit le titre du terminal.
   - `\W` représente le nom de base du répertoire courant (par exemple, `blog-server` au lieu du chemin complet `~/Projects/blog-server`).
   - `\a` est un caractère de cloche pour terminer la chaîne de titre.
   - Ce code vérifie si le terminal est compatible `xterm` (ce qu'est le GNOME Terminal) avant d'appliquer le changement.

3. **Appliquer les modifications** :
   Enregistrez le fichier et rechargez la configuration Bash :

   ```bash
   source ~/.bashrc
   ```

   Alternativement, fermez et rouvrez le terminal pour appliquer les modifications.

4. **Vérifier le résultat** :
   Naviguez vers un répertoire (par exemple, `cd ~/Projects/blog-server`), et le titre de l'onglet du terminal devrait maintenant afficher uniquement `blog-server`.

### Alternative : Modifier les paramètres de profil du GNOME Terminal
Si vous souhaitez personnaliser davantage le titre ou éviter de modifier `~/.bashrc`, vous pouvez utiliser les paramètres de profil du GNOME Terminal :

1. Ouvrez le GNOME Terminal.
2. Allez dans **Édition** > **Préférences** (ou **Terminal** > **Préférences**, selon votre version).
3. Sélectionnez le profil que vous utilisez (par exemple, "Unnamed" ou un profil personnalisé).
4. Allez dans l'onglet **Commande**.
5. Sous **Titre et commande**, définissez :
   - **Titre initial** : Laissez vide ou définissez une valeur générique.
   - **À la fin de la commande** : Choisissez **Conserver le titre initial** ou **Remplacer par la sortie de la commande**.
6. Dans la section **Commande**, activez **Exécuter une commande personnalisée au lieu de mon shell** et définissez la commande sur :

   ```bash
   bash --rcfile <(echo '. ~/.bashrc; PS1="\[\e]0;\W\a\]$PS1"')
   ```

   Cela garantit que le terminal utilise un prompt personnalisé qui définit le titre sur le répertoire courant.

7. Fermez la boîte de dialogue et testez en ouvrant un nouvel onglet ou en naviguant vers un répertoire.

### Notes
- Si vous utilisez un shell autre que Bash (par exemple, Zsh), vous devrez modifier le fichier de configuration équivalent (par exemple, `~/.zshrc`) et ajuster la syntaxe en conséquence. Pour Zsh, vous pouvez ajouter :

  ```zsh
  precmd() { echo -ne "\e]0;${PWD##*/}\a" }
  ```

- Si le titre ne se met pas à jour comme prévu, assurez-vous que votre émulateur de terminal est compatible `xterm` et qu'aucun autre script (par exemple, des paramètres `PS1` personnalisés dans `~/.bashrc`) ne remplace le titre.
- Pour des changements persistants sur tous les terminaux, assurez-vous que la configuration se trouve dans le profil shell de l'utilisateur ou dans les paramètres du GNOME Terminal.

Cela devrait vous donner un titre d'onglet affichant uniquement le nom du répertoire courant, comme `blog-server`. Faites-moi savoir si vous avez besoin de précisions supplémentaires !