---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Éditeur de texte par défaut de Red Hat Enterprise Linux
translated: true
type: note
---

### Éditeur de texte par défaut dans Red Hat Enterprise Linux

Dans Red Hat Enterprise Linux (RHEL), l'éditeur de texte par défaut est **Vi** (souvent aliasé en **Vim**, qui signifie "Vi IMproved"). Vi est un éditeur de texte modal en ligne de commande qui est la norme sur les systèmes de type Unix depuis les années 1970. Il est léger, omniprésent et préinstallé sur la plupart des systèmes RHEL via les paquets `vim-minimal` ou `vim-enhanced`.

#### Pourquoi Vi/Vim ?
- Il est efficace pour les environnements serveur où les éditeurs graphiques ne sont pas pratiques.
- Les commandes sont basées sur le clavier : mode Insertion pour taper (`i`) et mode Commande pour éditer (par exemple, `dd` pour supprimer une ligne, `:wq` pour sauvegarder et quitter).
- Si vous êtes nouveau, il a une courbe d'apprentissage mais il est puissant une fois maîtrisé.

#### Vérification et utilisation
- Exécutez `vi nomdufichier.txt` (ou `vim nomdufichier.txt`) pour ouvrir un fichier.
- Pour vérifier votre éditeur par défaut actuel : `echo $EDITOR` (affiche généralement `/usr/bin/vi`).
- Si vous préférez autre chose (comme Emacs de votre requête précédente), définissez-le avec `export EDITOR=emacs` dans votre `~/.bashrc`.

Pour un démarrage rapide, tapez `vimtutor` pour lancer un tutoriel interactif.

[Comment débuter avec l'éditeur Vi - Red Hat](https://www.redhat.com/en/blog/get-started-vi-editor)  
[Compétences Linux : 9 tutoriels pour tirer le meilleur parti de votre éditeur de texte - Red Hat](https://www.redhat.com/en/blog/text-editor-roundup-2022)