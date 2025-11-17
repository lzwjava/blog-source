---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Désactiver le mode de remplacement de VS Code
translated: true
type: note
---

Dans Visual Studio Code, le comportement par défaut est le **mode Insertion** (la frappe insère du texte, poussant le texte existant vers l'avant).  
Le **mode Remplacement** (la frappe écrase le texte existant) est activé lorsque vous appuyez sur la touche **Insert** (Insérer) de votre clavier — cela permet de basculer entre le mode Insertion et le mode Remplacement.

### Comment revenir du mode Remplacement au mode Insertion

1. Appuyez simplement une fois sur la touche **Insert** (Insérer) de votre clavier.  
   → La barre d'état en bas à droite changera de **OVR** (Overwrite) à **INS** (Insert).

### Si vous ne voulez plus jamais entrer accidentellement en mode Remplacement

Vous pouvez désactiver complètement le basculement par la touche Insert :

#### Méthode 1 : Raccourci clavier (recommandé)
Appuyez sur `Ctrl + Maj + P` → tapez **"Toggle Insert/Overwrite"** → vous verrez la commande  
`Preferences: Toggle Insert on Paste and Overtype` ou similaire.  
Plus fiablement, utilisez ce paramètre direct :

#### Méthode 2 : Ajoutez ceci à votre `settings.json`
```json
// Désactiver la touche Insert pour basculer le mode remplacement
"editor.occurencesHighlight": true,
"editor.overtypeMode": false,

// C'est le paramètre clé :
"keyboard.dispatch": "keyCode"
```

En réalité, la solution la meilleure et la plus courante est :

```json
// Désactiver complètement la touche Insert dans VS Code
{
    "key": "insert",
    "command": "-editor.action.toggleOverwrite",
    "when": "editorTextFocus"
}
```

Ou simplement désactiver le remplacement globalement :

```json
"editor.occurrencesHighlight": true,
"editor.overwriteMode": false   // n'est pas un paramètre réel, à ignorer

// Vrai paramètre pour désactiver le basculement en mode remplacement :
"editor.insertSpaces": true,  // sans rapport

// Bonne méthode :
{
    "key": "insert",
    "command": "noop"   // ou supprimer le raccourci par défaut
}
```

#### Solution permanente la plus simple (la plus utilisée) :
1. Ouvrez les Paramètres (`Ctrl + ,`)
2. Recherchez **"overwrite"**
3. Décochez **Editor: Overtype** (s'il existe) ou mieux :
4. Ajoutez cette ligne à votre `settings.json` (Ctrl + Maj + P → "Preferences: Open Settings (JSON)") :

```json
// Désactiver complètement le basculement du mode remplacement par la touche Insert
{
    "key": "insert",
    "command": "-editor.action.toggleOverwrite"
}
```

Après avoir ajouté cela, la touche Insert ne fera rien dans VS Code, et vous resterez toujours en mode Insertion.

C'est la solution la plus courante et la plus fiable utilisée par les développeurs qui appuient accidentellement sur la touche Insert (surtout sur les ordinateurs portables avec de petits claviers à Taïwan/Asie où la touche Insert est facile à atteindre).

Faites-moi savoir si vous êtes sur macOS (utilise une touche différente) ou si vous voulez une solution par clic dans la barre d'état !