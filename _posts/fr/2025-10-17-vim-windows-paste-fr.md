---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Coller dans Vim sous Windows
translated: true
type: note
---

## Coller dans Vim avec Git Bash sur Windows

Ah, je vois le problème—la commande `p` de Vim dans Git Bash (qui fonctionne sous Windows) peut être capricieuse, surtout lorsqu'il s'agit du presse-papiers système ou de texte externe. C'est un piège courant car Git Bash utilise MinTTY comme émulateur de terminal, et le comportement par défaut de Vim ne fonctionne pas toujours bien avec le presse-papiers de Windows. La commande `p` ne colle qu'à partir du tampon de copie *interne* de Vim (ce que vous avez copié avec `y` dans la même session Vim). Pour tout ce qui provient de l'extérieur de Vim (comme une copie depuis le Bloc-notes ou un navigateur), vous avez besoin du collage du terminal ou de l'intégration avec le presse-papiers.

Ne vous inquiétez pas—voici comment le gérer étape par étape, adapté à votre flux de travail "tout sélectionner, supprimer et coller dans un nouveau texte". Je vais couvrir le collage interne (qui devrait déjà fonctionner) et le collage externe.

### Vérification Rapide : Votre Vim Prend-il en Charge le Presse-papiers Système ?
D'abord, vérifiez si votre Vim peut accéder directement au presse-papiers Windows (cela résout beaucoup de problèmes) :
1. Ouvrez Git Bash.
2. Exécutez `vim --version | grep clipboard` (ou ouvrez Vim avec `vim`, puis tapez `:version` et cherchez `+clipboard`).
   - Si cela affiche `+clipboard`, parfait—vous pouvez utiliser `"+p` pour coller à partir du presse-papiers Windows.
   - Si c'est `-clipboard` ou rien, ce n'est pas pris en charge (courant dans le Vim fourni avec Git Bash). Passez aux méthodes de collage via le terminal ci-dessous.

S'il n'est pas pris en charge, envisagez d'installer un Vim complet pour Windows (par exemple, via Chocolatey : `choco install vim`) ou d'utiliser Neovim/WSL pour une meilleure intégration.

### 1. Collage Interne (Copier Dans Vim, Coller dans la Même Session)
C'est ce que mes instructions précédentes ciblaient—copier *à l'intérieur* de Vim et coller dans un nouveau fichier dans la *même* session. `p` devrait bien fonctionner ici, sans particularités liées à Git Bash :
- Dans `oldfile.txt` : `gg` (haut), `yG` (copier tout).
- `:e newfile.txt` (ouvrir un nouveau fichier dans le même Vim).
- `p` (coller). Cela place le contenu juste après le curseur.
- `:wq` pour sauvegarder.

Si `p` échoue toujours (par exemple, ne colle rien ou le texte est corrompu), c'est peut-être un problème de copie—essayez `"+yG` au lieu de `yG` si le presse-papiers est pris en charge, puis `"+p`.

### 2. Coller du Texte Externe dans Vim (Depuis les Applications Windows)
Si vous copiez depuis l'extérieur (par exemple, sélectionner tout dans le Bloc-notes, Ctrl+C, puis vouloir coller dans Vim) :
- **Méthode 1 : Utiliser le Collage Intégré de Git Bash (Le Plus Facile, Aucune Modification de Vim Nécessaire)**
  1. Ouvrez votre fichier : `vim newfile.txt`.
  2. Entrez en mode insertion : Appuyez sur `i`.
  3. Faites un clic droit dans la fenêtre Git Bash (cela colle directement depuis le presse-papiers Windows dans le terminal/Vim).
     - Raccourcis alternatifs : Touche `Insert`, ou activez le mode Édition rapide dans Git Bash (clic droit sur la barre de titre > Options > Édition rapide) puis utilisez Ctrl+Maj+V.
  4. Appuyez sur `Esc` pour quitter le mode insertion.
  - *Conseil Pro :* Si le collage de texte multi-lignes semble bizarre (retours à la ligne ou indentations supplémentaires), c'est souvent dû aux fins de ligne Windows (CRLF vs LF). Corrigez avec `:set ff=unix` dans Vim avant de coller, ou utilisez `:%s/\r$//g` après pour supprimer les retours chariot.

- **Méthode 2 : Si +clipboard est Pris en Charge (Directement dans Vim)**
  1. Copiez le texte en externe (Ctrl+C).
  2. En mode commande de Vim : `"+p` (colle depuis le presse-papiers système après le curseur) ou `"+P` (avant).
  3. Pour votre flux de travail : Après avoir supprimé dans l'ancien fichier, basculez vers le nouveau fichier et `"+p`.

### 3. Copier de Vim vers l'Extérieur (Copier Vers Windows)
- La copie interne (`y`) reste dans Vim—utilisez la copie du terminal pour l'extérieur.
- Sélectionnez le texte dans Vim : `v` (mode visuel), déplacez le curseur pour tout sélectionner (`ggVG`), puis `y`.
- Pour copier vers Windows : Clic droit > Modifier > Copier (ou surlignez et clic droit > Copier).
- Avec +clipboard : `"+y` au lieu de `y`, puis Ctrl+V ailleurs.

### Dépannage des Problèmes Courants de Collage Git Bash + Vim
- **Texte Corrompu (par ex., Lignes Partielles ou Espaces Supplémentaires) :** Désactivez le collage entre crochets dans Vim (`:set paste` avant d'entrer en mode insertion, puis collez, puis `:set nopaste`). Ou ajoutez `set paste` à `~/.vimrc` pour qu'il soit toujours activé (mais cela désactive certaines fonctionnalités comme l'auto-indentation).
- **Rien n'est Collé :** Assurez-vous d'être en mode insertion pour le collage via le terminal—`p` en mode commande est réservé au tampon interne.
- **Interférence de la Souris :** Si le clic droit sélectionne au lieu de coller, basculez avec un clic droit sur la barre de titre > Options > Souris > Édition rapide.
- **Pour Tout Supprimer Avant de Coller :** Dans votre flux de travail, après avoir copié, utilisez `:%d` pour vider le nouveau fichier, puis collez.

Cela devrait vous permettre de coller sans problème ! Si cela ne fonctionne toujours pas (par exemple, décrivez ce qui se passe exactement lorsque vous essayez `p`), ou si vous collez spécifiquement *depuis* des sources externes, faites-le moi savoir pour plus d'ajustements.

[How do you copy and paste into Git Bash](https://stackoverflow.com/questions/2304372/how-do-you-copy-and-paste-into-git-bash)  
[Copying from Windows clipboard in Vim](https://vi.stackexchange.com/questions/37599/copying-from-windows-clipboard)  
[How to copy paste contents in the vi editor](https://askubuntu.com/questions/256782/how-to-copy-paste-contents-in-the-vi-editor)