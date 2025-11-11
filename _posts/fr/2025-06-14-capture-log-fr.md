---
audio: false
generated: true
lang: fr
layout: post
title: Journal de Capture
translated: true
type: note
---

Dans GNOME Terminal, l'option « Sélectionner tout » (généralement accessible via `Édition > Sélectionner tout` ou `Ctrl+Maj+A`) ne sélectionne que le texte actuellement visible à l'écran. Pour sélectionner **tout le texte** du terminal, y compris le contenu dans le tampon de défilement (au-delà de ce qui est visible), vous pouvez utiliser l'une de ces méthodes :

### Méthode 1 : Augmenter le tampon de défilement et sélection manuelle
1. **Vérifier que le défilement est activé** :
   - Allez dans `Édition > Préférences du profil` dans GNOME Terminal.
   - Sous l'onglet « Défilement », assurez-vous que le tampon de défilement est réglé sur un nombre élevé ou « Illimité » pour capturer toute la sortie du terminal.
2. **Sélection manuelle** :
   - Remontez en haut de la sortie du terminal à l'aide de la souris ou de `Maj+Page précédente`.
   - Cliquez et faites glisser du haut vers le bas pour sélectionner tout le texte manuellement.
   - Alternativement, utilisez `Maj+Début` pour aller au début du tampon, puis cliquez et faites glisser ou utilisez `Maj+Fin` pour sélectionner jusqu'à la fin.

### Méthode 2 : Utiliser une commande pour capturer toute la sortie
Si vous souhaitez capturer toute la sortie du terminal (y compris le tampon de défilement), vous pouvez rediriger ou copier la sortie en utilisant une commande :
1. **Rediriger la sortie vers un fichier** :
   - Si vous connaissez la commande générant la sortie, relancez-la avec une redirection :
     ```bash
     command > output.txt
     ```
     Cela enregistre toute la sortie dans `output.txt`, que vous pouvez ensuite ouvrir et sélectionner.
2. **Utiliser `script` pour enregistrer une session de terminal** :
   - Démarrez une session d'enregistrement avec :
     ```bash
     script output.log
     ```
   - Exécutez vos commandes, puis tapez `exit` pour arrêter l'enregistrement.
   - Ouvrez `output.log` pour sélectionner tout le texte.

### Méthode 3 : Copier le tampon de défilement via une commande de terminal
1. Utilisez la commande `tee` ou similaire pour capturer la sortie pendant l'exécution des commandes :
   ```bash
   command | tee output.txt
   ```
   Cela affiche la sortie dans le terminal et l'enregistre dans `output.txt`.
2. Ouvrez le fichier dans un éditeur de texte pour sélectionner facilement tout le texte.

### Méthode 4 : Utiliser `tmux` ou `screen` pour un contrôle avancé
Si vous avez fréquemment besoin de capturer toute la sortie du terminal :
1. **Installer et utiliser `tmux`** :
   - Installez `tmux` :
     ```bash
     sudo apt install tmux  # Sur Debian/Ubuntu
     ```
   - Démarrez une session `tmux` :
     ```bash
     tmux
     ```
   - Exécutez vos commandes.
   - Entrez en mode défilement avec `Ctrl+b, [`, puis appuyez sur `Ctrl+a, Ctrl+e` pour sélectionner tout le texte dans le tampon.
   - Copiez avec `Ctrl+b, ]` (après avoir configuré `tmux` pour activer la copie).
2. **Sauvegarder le tampon tmux** :
   - Sauvegardez l'intégralité du tampon dans un fichier :
     ```bash
     tmux capture-pane -S - -E - -b 0 -J > output.txt
     ```
   - Ouvrez `output.txt` pour sélectionner tout le texte.

### Limitations
- GNOME Terminal lui-même n'a pas de fonction intégrée « sélectionner tout le tampon de défilement » via l'interface graphique.
- La taille du tampon de défilement peut limiter la quantité de texte disponible s'il n'est pas réglé sur illimité.
- Pour des sorties très volumineuses, l'utilisation de `tmux`, `screen` ou la redirection vers un fichier est plus fiable.

Si vous avez besoin de précisions supplémentaires ou d'aide pour une commande spécifique, faites-le-moi savoir !