---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Copier le contenu d'un fichier dans Vi
translated: true
type: note
---

## Copier (ou déplacer) l'intégralité du contenu d'un fichier vers un nouveau fichier dans Vi

D'après votre utilisation de vi, je suppose que vous souhaitez sélectionner et copier/supprimer l'intégralité du contenu d'un fichier, puis le coller dans un nouveau fichier. Vi n'a pas de fonction "sélectionner tout" directe comme les éditeurs graphiques, mais vous pouvez y parvenir efficacement en **mode commande** (appuyez sur `Esc` pour vous assurer d'être dans ce mode). Je vais couvrir à la fois la **copie** (en laissant l'original intact) et le **couper/supprimer** (déplacer le contenu).

### Procédure pas à pas : Copier tout le contenu vers un nouveau fichier
1. Ouvrez votre fichier source :  
   ```
   vi ancienfichier.txt
   ```

2. Extraire (copier) l'intégralité du fichier :  
   - Tapez `gg` (aller en haut du fichier).  
   - Puis tapez `yG` (extraire de la position actuelle jusqu'à la fin du fichier).  
   *Alternative (spécifique à Vim, fonctionne avec vim de Red Hat) :* Tapez `:1,$y` et appuyez sur `Entrée` (extrait les lignes 1 à la fin).

3. Ouvrez le nouveau fichier :  
   - Tapez `:e nouveaufichier.txt` et appuyez sur `Entrée` (crée/ouvre le nouveau fichier).

4. Collez le contenu :  
   - Tapez `p` (colle après le curseur ; comme le fichier est vide, cela colle en haut).  
   *Alternative :* Tapez `P` pour coller avant le curseur.

5. Enregistrez et quittez le nouveau fichier :  
   - Tapez `:wq` et appuyez sur `Entrée`.

Le fichier original reste inchangé.

### Procédure pas à pas : Supprimer tout le contenu et le coller dans un nouveau fichier (Déplacer)
Cette méthode supprime le contenu original après l'avoir copié.

1. Ouvrez votre fichier source :  
   ```
   vi ancienfichier.txt
   ```

2. Extraire (copier) d'abord l'intégralité du fichier :  
   - `gg` puis `yG` (ou `:1,$y`).

3. Supprimez tout le contenu :  
   - Tapez `gg` (vers le haut).  
   - Puis `dG` (supprime de la position actuelle jusqu'à la fin).  
   *Alternative :* Tapez `:%d` et appuyez sur `Entrée` (supprime toutes les lignes).  
   Enregistrez si nécessaire : `:w` (écrase le fichier maintenant vide).

4. Ouvrez le nouveau fichier :  
   - Tapez `:e nouveaufichier.txt` et appuyez sur `Entrée`.

5. Collez :  
   - Tapez `p`.

6. Enregistrez et quittez :  
   - `:wq`.

### Conseils rapides
- Si vous supprimez accidentellement sans avoir extrait au préalable, utilisez `u` pour annuler.
- Pour effectuer cette opération entre fichiers sans en ouvrir un nouveau à chaque fois : Extrayez dans le premier fichier, puis utilisez `vi nouveaufichier.txt`, collez, et enregistrez.
- Pour les gros fichiers, ces commandes sont rapides car vi gère les tampons efficacement.

Pratiquez sur des fichiers tests pour vous familiariser !

[How to Copy Text to Another File in Vim](https://stackoverflow.com/questions/1239801/how-to-copy-to-the-end-of-the-line-in-vim)  
[Vim: Yank (copy) entire file](https://vim.fandom.com/wiki/Yank_%28copy%29_the_entire_file)