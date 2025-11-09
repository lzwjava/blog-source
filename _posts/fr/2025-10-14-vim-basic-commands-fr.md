---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Tutoriel des commandes de base de Vim
translated: true
type: note
---

Vim (abréviation de Vi IMproved) est un éditeur de texte modal puissant, souvent installé par défaut sur de nombreux systèmes Linux comme Red Hat. Il est piloté au clavier et très efficace une fois les bases maîtrisées. Vim possède trois modes principaux : **Normal** (pour la navigation et les commandes, mode par défaut), **Insertion** (pour taper du texte) et **Visuel** (pour sélectionner du texte). Appuyez sur `Échap` pour revenir au mode Normal depuis n'importe où.

Le meilleur moyen d'apprendre de manière pratique est d'exécuter `vimtutor` dans votre terminal — cela lance un tutoriel interactif.

## 1. Ouvrir et fermer Vim
- Ouvrir ou créer un fichier : `vim nomdufichier.txt` (par exemple, `vim notes.txt`).
- Quitter sans sauvegarder : Dans le mode Normal, tapez `:q!` et appuyez sur Entrée.
- Quitter Vim : Voir la section sur la sauvegarde ci-dessous.

## 2. Modes
- **Mode Normal** : Mode par défaut — utilisé pour les commandes. Appuyez sur `Échap` pour y entrer.
- **Mode Insertion** : Appuyez sur `i` (insérer avant le curseur) ou `a` (ajouter après le curseur) pour y entrer. Vous verrez `-- INSERT --` en bas.
- **Mode Visuel** : Appuyez sur `v` pour sélectionner du texte.
- **Mode Ligne de commande** : Appuyez sur `:` pour y entrer (pour sauvegarder, quitter, rechercher).

## 3. Navigation (en mode Normal)
Utilisez ces touches au lieu des flèches pour plus d'efficacité :
- `h` : Un caractère à gauche
- `j` : Une ligne vers le bas
- `k` : Une ligne vers le haut
- `l` : Un caractère à droite
- `w` : Avancer au début du mot suivant
- `b` : Reculer au début du mot précédent
- `0` : Début de la ligne
- `$` : Fin de la ligne
- `gg` : Haut du fichier
- `G` : Bas du fichier
- `:n` : Aller à la ligne n (par exemple, `:5`)
- Préfixe avec des nombres : `5j` (descendre de 5 lignes)

Activer les numéros de ligne : `:set number`

## 4. Insertion et édition de texte
- Entrer en mode Insertion :
  - `i` : Insérer avant le curseur
  - `I` : Insérer au début de la ligne
  - `a` : Ajouter après le curseur
  - `A` : Ajouter à la fin de la ligne
  - `o` : Nouvelle ligne en dessous (passe en mode Insertion)
  - `O` : Nouvelle ligne au-dessus (passe en mode Insertion)
- Quitter le mode Insertion : `Échap`
- Remplacer un seul caractère : `r` (puis tapez le nouveau caractère)
- Annuler : `u`
- Rétablir : `Ctrl + r`
- Répéter la dernière commande : `.`

## 5. Suppression, copie et collage
- Supprimer un caractère : `x`
- Supprimer une ligne : `dd`
- Supprimer une plage : `:3,5d` (lignes 3 à 5)
- Copier (yanker) une ligne : `yy`
- Copier le texte sélectionné : En mode Visuel (`v`), surlignez avec les flèches, puis `y`
- Coller après le curseur : `p`
- Coller avant le curseur : `P`
- Sélectionner du texte : `v` (caractère par caractère), puis déplacez le curseur ; `Échap` pour quitter le mode Visuel.

## 6. Sauvegarde et fermeture
- Sauvegarder : `:w`
- Sauvegarder et quitter : `:wq` ou `:x` ou `ZZ` (deux fois Z majuscule)
- Forcer la sauvegarde et quitter : `:wq!`
- Quitter sans sauvegarder : `:q!` ou `ZQ`

## 7. Recherche
- Recherche vers l'avant : `/motif` (par exemple, `/bonjour`), puis Entrée ; `n` pour le suivant.
- Recherche vers l'arrière : `?motif`
- Remplacer : `:%s/ancien/nouveau/g` (remplace tous les "ancien" par "nouveau")

## Conseils rapides
- Aide : `:help` ou `:h mot-clé`
- Fractionner l'écran : `:split nomdufichier` (horizontal) ou `:vsplit nomdufichier` (vertical) ; `Ctrl + w w` pour alterner.
- Entraînez-vous dans un fichier test pour éviter les erreurs.
- Coloration syntaxique : `:syntax on`

Ceci couvre l'essentiel pour vous permettre de modifier rapidement des fichiers. Pour en savoir plus, explorez `:help` dans Vim ou les ressources ci-dessous.

[Getting started with Vim: The basics](https://opensource.com/article/19/3/getting-started-vim)
[Basic Vim Commands](https://www.geeksforgeeks.org/linux-unix/basic-vim-commands/)
[Vim Cheat Sheet](https://vim.rtorr.com/)