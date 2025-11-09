---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Bases de l'Éditeur Vi pour Red Hat Linux
translated: true
type: note
---

Vi est un éditeur de texte puissant, piloté par le clavier, qui est standard sur les systèmes Linux, y compris Red Hat Enterprise Linux (RHEL). Il est léger et efficace pour éditer des fichiers de configuration, des scripts, et plus encore. Sous Red Hat, la commande `vi` pointe généralement vers `vim` (Vi IMproved), qui ajoute des fonctionnalités comme la coloration syntaxique. Ce guide couvre les bases pour les débutants.

## Installation
Vi est préinstallé sur la plupart des systèmes Red Hat. Si vous avez besoin du paquet complet `vim` (ou s'il est manquant), installez-le via le gestionnaire de paquets :

- Pour RHEL 7/8 :  
  ```
  sudo yum install vim
  ```

- Pour RHEL 9+ :  
  ```
  sudo dnf install vim
  ```

Après l'installation, vous pouvez utiliser `vi` ou `vim` de manière interchangeable.

## Démarrer Vi
1. Ouvrez un terminal.
2. Exécutez `vi nomdufichier.txt` (remplacez `nomdufichier.txt` par le chemin de votre fichier).  
   - Si le fichier existe, il s'ouvre pour édition.  
   - Sinon, un nouveau fichier vide est créé.  
3. Pour ouvrir sans fichier (pour s'entraîner) : `vi`.  
Vi démarre en **mode commande** (le mode par défaut). Vous verrez un écran vide ou le contenu du fichier avec un curseur en haut à gauche.

## Comprendre les Modes
Vi a trois modes principaux—passer de l'un à l'autre est essentiel :
- **Mode Commande** : Mode par défaut pour la navigation, la suppression et la plupart des actions. Appuyez sur `Esc` pour entrer/revenir ici depuis d'autres modes.
- **Mode Insertion** : Pour taper/éditer du texte. Entrez depuis le mode commande (par exemple, appuyez sur `i`).
- **Mode Ex** : Pour les commandes avancées comme la sauvegarde. Entrez en tapant `:` en mode commande.

Les commandes sont sensibles à la casse. Préfixez par des nombres pour répéter les actions (par exemple, `3dd` supprime 3 lignes).

## Navigation de Base (en Mode Commande)
Utilisez les touches de la rangée principale pour déplacer le curseur—pas besoin de souris :
- `h` : Gauche d'un caractère
- `j` : Bas d'une ligne
- `k` : Haut d'une ligne
- `l` : Droite d'un caractère
- `w` : Avant d'un mot
- `b` : Arrière d'un mot
- `0` (zéro) : Début de ligne
- `$` : Fin de ligne
- `gg` : Haut du fichier
- `G` : Bas du fichier
- `Ctrl + F` : Page suivante
- `Ctrl + B` : Page précédente

## Entrer en Mode Insertion et Éditer
Depuis le mode commande, appuyez sur l'une de ces touches pour passer en mode insertion et commencer à taper :
- `i` : Insère avant le curseur
- `I` : Insère au début de la ligne
- `a` : Ajoute après le curseur
- `A` : Ajoute à la fin de la ligne
- `o` : Nouvelle ligne en dessous
- `O` : Nouvelle ligne au-dessus

Pour quitter le mode insertion : Appuyez sur `Esc` (retour au mode commande).

Commandes d'édition courantes (en mode commande) :
- **Supprimer** :
  - `x` : Supprime le caractère sous le curseur
  - `X` : Supprime le caractère avant le curseur
  - `dd` : Supprime la ligne courante
  - `dw` : Supprime le mot courant
  - `D` : Supprime jusqu'à la fin de la ligne
- **Copier (Yank)** :
  - `yy` : Copie la ligne courante
  - `y` : Copie la sélection (après `v` pour sélectionner)
- **Coller** :
  - `p` : Colle après le curseur
  - `P` : Colle avant le curseur
- **Annuler** :
  - `u` : Annule la dernière modification
  - `U` : Annule toutes les modifications sur la ligne courante
- **Répéter** : `.` (répète la dernière commande)

## Sauvegarder et Quitter
Ce sont des **commandes Ex**—tapez `:` en mode commande, puis la commande, et appuyez sur `Entrée` :
- `:w` : Sauvegarde (écrit) les modifications
- `:q` : Quitte (si aucune modification)
- `:wq` ou `ZZ` (en mode commande) : Sauvegarde et quitte
- `:q!` : Quitte sans sauvegarder (force l'abandon des modifications)
- `:w nomdufichier` : Sauvegarde sous un nouveau nom de fichier

Si vous êtes bloqué, `:q!` vous permet de sortir en sécurité.

## Rechercher et Remplacer
- Recherche avant : `/motif` (par exemple, `/erreur`), puis `n` pour le prochain résultat, `N` pour le précédent.
- Recherche arrière : `?motif`.
- Remplacer tout : `:%s/ancien/nouveau/g` (remplacement global ; ajoutez `c` pour confirmation, par exemple, `:%s/ancien/nouveau/gc`).

## Conseils pour les Utilisateurs Red Hat
- Personnalisez dans `~/.vimrc` (créez-le si nécessaire) :  
  ```
  set number          # Affiche les numéros de ligne
  syntax on           # Coloration syntaxique
  set tabstop=4       # Largeur des tabulations
  set autoindent      # Auto-indentation
  ```
  Éditez avec `vi ~/.vimrc`, ajoutez les lignes, puis `:wq`.
- Pour plusieurs fichiers : `vi fichier1.txt fichier2.txt`, changez avec `:n` (suivant) ou `:prev` (précédent).
- Entraînez-vous dans un fichier test pour éviter les erreurs dans les fichiers système.

Vi demande de la pratique mais devient intuitif. Commencez simplement et utilisez `Esc` souvent !

## Références
[How to get started with the Vi editor - Red Hat](https://www.redhat.com/en/blog/get-started-vi-editor)  
[LFCS #2: How to Install and Use Vi/Vim as a Full Text Editor in Linux](https://www.tecmint.com/vi-editor-usage/)  
[vi Editor in Linux - GeeksforGeeks](https://www.geeksforgeeks.org/linux-unix/vi-editor-unix/)