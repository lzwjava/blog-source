---
audio: false
lang: fr
layout: post
title: Activer l'enroulement de texte uniquement pour des extensions de fichiers spécifiques
translated: true
---

J'assume que vous demandez comment configurer Visual Studio Code (VS Code) pour activer l'enroulement des mots uniquement pour certaines extensions de fichiers. Voici comment vous pouvez y parvenir :

1. **Ouvrir les Paramètres de VS Code** :
   - Appuyez sur `Ctrl + ,` (ou `Cmd + ,` sur macOS) pour ouvrir les paramètres, ou allez dans `Fichier > Préférences > Paramètres`.

2. **Utiliser le Fichier de Paramètres JSON** :
   - Dans l'interface des Paramètres, cliquez sur l'icône `{}` en haut à droite pour ouvrir le fichier `settings.json`. Cela permet un contrôle plus granulaire.

3. **Configurer l'Enroulement des Mots par Type de Fichier** :
   - Ajoutez une configuration en utilisant la syntaxe `"[filetype]": {}` pour spécifier les paramètres pour des extensions de fichiers spécifiques. Par exemple, pour activer l'enroulement des mots uniquement pour les fichiers `.md` (Markdown) et `.txt` (Texte), vous pouvez ajouter quelque chose comme ceci :

   ```json
   {
       "editor.wordWrap": "off", // Par défaut : pas d'enroulement pour tous les fichiers
       "[markdown]": {
           "editor.wordWrap": "on" // Enroulement uniquement pour les fichiers .md
       },
       "[plaintext]": {
           "editor.wordWrap": "on" // Enroulement uniquement pour les fichiers .txt
       }
   }
   ```

4. **Explication** :
   - `"editor.wordWrap": "off"` définit la valeur par défaut globale à aucun enroulement.
   - `"[markdown]"` et `"[plaintext]"` sont des identifiants de langage pour les fichiers Markdown et texte brut, respectivement. Vous pouvez les remplacer par d'autres identifiants de langage comme `[javascript]`, `[python]`, etc., en fonction des extensions de fichiers que vous souhaitez cibler.
   - `"editor.wordWrap": "on"` active l'enroulement pour ces types de fichiers spécifiques.

5. **Trouver les Identifiants de Langage** :
   - Si vous n'êtes pas sûr de l'identifiant de langage pour une extension de fichier, ouvrez un fichier de ce type dans VS Code, cliquez sur le mode de langage dans le coin inférieur droit (par exemple, "Texte brut" ou "Python"), et notez l'identifiant affiché dans la palette de commandes lors de la sélection d'un langage.

6. **Enregistrer et Tester** :
   - Enregistrez le fichier `settings.json`, et VS Code appliquera les paramètres immédiatement. Ouvrez des fichiers avec différentes extensions pour confirmer le comportement.

Cette approche garantit que l'enroulement des mots est activé uniquement pour les types de fichiers que vous spécifiez, laissant tous les autres inchangés. Faites-moi savoir si vous avez besoin d'aide pour des extensions spécifiques !