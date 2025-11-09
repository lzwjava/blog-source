---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-sonnet-4
title: Résoudre les problèmes de curseur croisé dans VSCode
translated: true
type: note
---

Le changement du curseur de la souris en une croix/symbole plus (十字架) dans VSCode indique généralement que VSCode est dans un mode spécial ou qu'il y a un problème de configuration. Voici les causes et solutions les plus courantes :

## Causes courantes :

1. **Mode de sélection de colonne** : Vous avez peut-être accidentellement activé le mode de sélection en colonne/bloc
   - Essayez d'appuyer sur `Alt + Shift + I` ou `Ctrl + Shift + Alt + Touches de direction` pour quitter ce mode

2. **Conflit d'extension** : Certaines extensions peuvent modifier le comportement du curseur
   - Essayez de désactiver temporairement les extensions : `Ctrl + Shift + P` → "Developer: Reload Window"
   - Ou démarrez VSCode en mode sans échec : `code --disable-extensions`

3. **Outils de zoom/sélection** : Vous avez peut-être activé un outil de zoom ou de sélection
   - Appuyez plusieurs fois sur la touche `Échap`
   - Essayez `Ctrl + Z` pour annuler les actions récentes

4. **Problème de focus du terminal** : Si le terminal a le focus, cela peut modifier le comportement du curseur
   - Cliquez dans la zone de l'éditeur pour refaire le focus
   - Essayez `Ctrl + 1` pour focaliser sur l'éditeur

## Corrections rapides :

1. **Redémarrer VSCode** : Simple mais souvent efficace
   - `Ctrl + Shift + P` → "Developer: Reload Window"

2. **Vérifier les paramètres de la souris** :
   - Allez dans Fichier → Préférences → Paramètres
   - Recherchez "cursor" et vérifiez les paramètres liés au curseur

3. **Réinitialiser l'espace de travail** :
   - Fermez VSCode
   - Supprimez le dossier `.vscode` dans votre projet (s'il est présent)
   - Rouvrez le projet

4. **Vérifier le problème à l'échelle du système** :
   - Testez si le problème du curseur apparaît dans d'autres applications
   - Si oui, il peut s'agir d'un problème de paramètre GNOME/système

Essayez d'abord d'appuyer plusieurs fois sur `Échap`, puis redémarrez VSCode. Cela résout généralement le problème du curseur en croix.