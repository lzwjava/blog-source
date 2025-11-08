---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration de Zed avec les raccourcis clavier d'Emacs
translated: true
type: note
---

### Configuration de l'éditeur Zed avec les raccourcis Emacs

Il semble que vous vouliez dire **Zed** (l'éditeur de code haute performance), car "éditeur Zig" ne fait pas référence à un outil standard—Zig est un langage de programmation sans éditeur intégré. Si ce n'est pas ce que vous aviez en tête, n'hésitez pas à préciser ! En supposant qu'il s'agit de Zed, il prend en charge nativement les raccourcis Emacs (étiquetés "Emacs (Beta)"). Cela couvre de nombreuses bases immédiatement, comme les déplacements (`Ctrl-b/f/n/p`) et l'édition (`Ctrl-d` pour supprimer un caractère, `Ctrl-k` pour couper jusqu'à la fin de la ligne). Vous pouvez l'activer facilement, puis personnaliser davantage si nécessaire.

#### Étape 1 : Activer le Keymap Emacs intégré
Le mode Emacs de Zed est prédéfini et ne nécessite pas de configuration manuelle des raccourcis pour les bases. Voici comment l'activer :

1. Ouvrez les paramètres de Zed :
   - macOS : `Cmd-,`
   - Windows/Linux : `Ctrl-,`

2. Dans l'interface des paramètres, recherchez "base keymap" et définissez-la sur **Emacs**.

   *Ou, modifiez directement dans `settings.json`* (ouvrez via `Cmd-Alt-,` sur macOS ou `Ctrl-Alt-,` sur Windows/Linux) :
   ```json
   {
     "base_keymap": "Emacs"
   }
   ```

   Enregistrez et rechargez Zed (`Cmd-R` ou `Ctrl-R`). C'est tout—le keymap beta Emacs s'active immédiatement.

   Alternativement, utilisez la palette de commandes (`Cmd-Maj-P` ou `Ctrl-Maj-P`), tapez "toggle base keymap," et sélectionnez Emacs.

Cela vous donne les réflexes musculaires de base d'Emacs sans travail supplémentaire. Pour une liste complète des raccourcis intégrés, consultez les fichiers de keymap par défaut de Zed dans le code source (par exemple via GitHub), mais les bases incluent :
- **Déplacement** : `Ctrl-b` (caractère gauche), `Ctrl-f` (caractère droit), `Ctrl-p` (ligne haute), `Ctrl-n` (ligne basse), `Alt-b/f` (mot précédent/suivant).
- **Édition** : `Ctrl-d` (supprimer caractère), `Ctrl-k` (couper jusqu'à la fin de la ligne), `Ctrl-y` (coller), `Ctrl-@` (poser la marque pour la région), `Ctrl-w` (couper la région).
- **Autre** : `Ctrl-x Ctrl-s` (enregistrer), `Ctrl-g` (annuler), `Ctrl-/` (annuler).

#### Étape 2 : Ajouter ou Personnaliser les Raccourcis de Base (Si Nécessaire)
Pour des ajustements ou un comportement plus proche d'Emacs (par exemple, une meilleure navigation début/fin ou par paragraphe), modifiez `keymap.json` :
- Ouvrez-le via la palette de commandes : Tapez "open keymap file."
- Chemin : `~/.config/zed/keymap.json` (macOS/Linux) ou `~\AppData\Roaming\Zed\keymap.json` (Windows).

Ajoutez les raccourcis sous forme de tableau JSON dans des contextes comme "Editor." Voici un **exemple minimal** pour les déplacements et l'édition de base (collez-le dans le tableau ; il est basé sur des configurations communautaires pour la compatibilité) :

```json
[
  {
    "context": "Editor",
    "bindings": {
      // Déplacement de base
      "ctrl-a": "editor::MoveToBeginningOfLine",
      "ctrl-e": "editor::MoveToEndOfLine",
      "ctrl-b": "editor::MoveLeft",
      "ctrl-f": "editor::MoveRight",
      "ctrl-p": "editor::MoveLineUp",
      "ctrl-n": "editor::MoveLineDown",
      "alt-b": "editor::MoveToPreviousWordStart",
      "alt-f": "editor::MoveToNextWordEnd",

      // Édition de base
      "ctrl-d": "editor::DeleteRight",
      "ctrl-k": "editor::CutToEndOfLine",
      "ctrl-y": "editor::Paste",
      "ctrl-w": "editor::Cut",
      "ctrl-@": ["editor::SetSelectionAnchor", { "selection_id": 0 }],  // Poser la marque
      "ctrl-x ctrl-x": "editor::FlipSelectionAnchor",  // Échanger point/marque

      // Navigation supplémentaire
      "ctrl-home": "editor::MoveToBeginning",
      "ctrl-end": "editor::MoveToEnd",
      "ctrl-g": "editor::Cancel"
    }
  }
]
```

- Enregistrez et rechargez Zed. Ceux-ci remplacent ou s'ajoutent au keymap Emacs de base.
- Testez dans un tampon d'édition. Pour les sélections, utilisez `Ctrl-Espace` (ou `Ctrl-@`) pour poser la marque, puis déplacez-vous pour sélectionner une région.
- Conseil pro : Combinez avec `vim_mode: false` dans settings.json pour éviter les conflits.

#### Conseils
- **Statut beta** : Le mode Emacs s'améliore (suivez les progrès [ici](https://github.com/zed-industries/zed/issues/4856)). Signalez les problèmes sur le GitHub de Zed.
- **Configurations personnalisées avancées** : Pour des configurations avancées (par exemple, changement de panneau avec `Ctrl-x o`), consultez les exemples de la communauté dans la discussion ci-dessous.
- Si vous voulez les modes Vim/Helix en plus, définissez `vim_mode: true` ou `helix_mode: true` dans les paramètres—ils se superposent.

Cela devrait vous donner 80 % des sensations de base d'Emacs. Commencez par le mode intégré, puis itérez !

[Documentation des Raccourcis Clavier](https://zed.dev/docs/key-bindings)  
[Configuration de Zed](https://zed.dev/docs/configuring-zed)  
[Discussion sur le Keymap Emacs](https://github.com/zed-industries/zed/discussions/6572)  
[Problème de Compatibilité Emacs](https://github.com/zed-industries/zed/issues/4856)