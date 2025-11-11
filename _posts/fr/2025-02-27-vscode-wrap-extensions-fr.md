---
audio: false
generated: true
lang: fr
layout: post
title: Activer le retour à la ligne pour des extensions de fichier spécifiques
translated: true
type: note
---

Je suppose que vous demandez comment configurer Visual Studio Code (VS Code) pour activer le retour à la ligne seulement pour des extensions de fichier spécifiques. Voici comment procéder :

1. **Ouvrir les Paramètres de VS Code** :
   - Appuyez sur `Ctrl + ,` (ou `Cmd + ,` sur macOS) pour ouvrir les paramètres, ou allez dans `Fichier > Préférences > Paramètres`.

2. **Utiliser le Fichier de Paramètres JSON** :
   - Dans l'interface des paramètres, cliquez sur l'icône `{}` dans le coin supérieur droit pour ouvrir le fichier `settings.json`. Cela permet un contrôle plus granulaire.

3. **Configurer le Retour à la Ligne par Type de Fichier** :
   - Ajoutez une configuration en utilisant la syntaxe `"[typefichier]": {}` pour spécifier les paramètres pour des extensions de fichier spécifiques. Par exemple, pour activer le retour à la ligne seulement pour les fichiers `.md` (Markdown) et `.txt` (Texte), vous pouvez ajouter quelque chose comme ceci :

   ```json
   {
       "editor.wordWrap": "off", // Par défaut : pas de retour à la ligne pour tous les fichiers
       "[markdown]": {
           "editor.wordWrap": "on" // Retour à la ligne seulement pour les fichiers .md
       },
       "[plaintext]": {
           "editor.wordWrap": "on" // Retour à la ligne seulement pour les fichiers .txt
       }
   }
   ```

4. **Explication** :
   - `"editor.wordWrap": "off"` définit la valeur par défaut globale à "sans retour à la ligne".
   - `"[markdown]"` et `"[plaintext]"` sont des identifiants de langage pour les fichiers Markdown et texte brut, respectivement. Vous pouvez les remplacer par d'autres identifiants de langage comme `[javascript]`, `[python]`, etc., en fonction des extensions de fichier que vous souhaitez cibler.
   - `"editor.wordWrap": "on"` active le retour à la ligne pour ces types de fichier spécifiques.

5. **Trouver les Identifiants de Langage** :
   - Si vous n'êtes pas sûr de l'identifiant de langage pour une extension de fichier, ouvrez un fichier de ce type dans VS Code, cliquez sur le mode de langage dans le coin inférieur droit (par exemple, "Plain Text" ou "Python"), et notez l'identifiant affiché dans la palette de commandes lors de la sélection d'un langage.

6. **Sauvegarder et Tester** :
   - Sauvegardez le fichier `settings.json`, et VS Code appliquera les paramètres immédiatement. Ouvrez des fichiers avec différentes extensions pour confirmer le comportement.

Cette approche garantit que le retour à la ligne est activé uniquement pour les types de fichier que vous spécifiez, laissant tous les autres inchangés. Faites-moi savoir si vous avez besoin d'aide pour des extensions spécifiques !

---

Si vous travaillez avec des fichiers `.log` dans Visual Studio Code et que vous souhaitez activer le retour à la ligne spécifiquement pour eux, vous devez vous assurer que VS Code reconnaît ces fichiers comme un mode de langage distinct. Par défaut, les fichiers `.log` n'ont pas forcément un identifiant de langage unique comme `[log]`—ils sont souvent traités comme du texte brut (`[plaintext]`). Cependant, vous pouvez configurer ce comportement. Voici comment le gérer :

### Option 1 : Utiliser `[plaintext]` si les fichiers `.log` sont en Texte Brut
Si vos fichiers `.log` sont reconnus comme du texte brut (vérifiez le mode de langage dans le coin inférieur droit de VS Code lorsqu'un fichier `.log` est ouvert), vous pouvez simplement utiliser `[plaintext]` :

```json
{
    "editor.wordWrap": "off", // Par défaut : pas de retour à la ligne
    "[plaintext]": {
        "editor.wordWrap": "on" // Activer pour les fichiers .txt et .log (s'ils sont reconnus comme plaintext)
    }
}
```

- **Remarque** : Cela s'appliquera à tous les fichiers texte brut (par exemple, `.txt`, `.log`), pas seulement aux fichiers `.log`. Si c'est trop large, passez à l'Option 2.

### Option 2 : Associer les fichiers `.log` à un Mode de Langage Personnalisé
Si vous voulez que `[log]` fonctionne comme un identifiant spécifique, vous devez indiquer à VS Code d'associer les fichiers `.log` à un mode de langage "Log". Voici comment :

1. **Installer une Extension pour les Fichiers Log (Optionnel)** :
   - Installez une extension comme "Log File Highlighter" depuis le VS Code Marketplace. Cette extension assigne souvent aux fichiers `.log` un mode de langage spécifique (par exemple, `log`).
   - Après l'installation, vérifiez le mode de langage pour un fichier `.log` (coin inférieur droit). S'il indique "Log" ou similaire, vous pouvez utiliser `[log]` directement.

2. **Associer Manuellement les Fichiers `.log`** :
   - Si vous ne voulez pas d'extension, vous pouvez associer manuellement `.log` à un mode de langage via `files.associations` dans `settings.json` :
   ```json
   {
       "files.associations": {
           "*.log": "log" // Associe .log au mode de langage "log"
       },
       "editor.wordWrap": "off", // Par défaut : pas de retour à la ligne
       "[log]": {
           "editor.wordWrap": "on" // Activer seulement pour les fichiers .log
       }
   }
   ```
   - **Mise en garde** : Le mode de langage `log` doit exister (par exemple, fourni par une extension ou VS Code). S'il n'existe pas, VS Code pourrait revenir au texte brut, et `[log]` ne fonctionnera pas comme prévu sans personnalisation supplémentaire.

3. **Vérifier le Mode de Langage** :
   - Ouvrez un fichier `.log`, cliquez sur le mode de langage dans le coin inférieur droit, et voyez à quoi il est défini. S'il est sur `log` après vos modifications, `[log]` fonctionnera. S'il est toujours sur `plaintext`, utilisez `[plaintext]` ou ajustez l'association.

### Option 3 : Affiner avec des Modèles de Fichier (Plus Précis)**
Pour un contrôle ultime, vous pouvez utiliser le paramètre `"files.associations"` pour cibler spécifiquement les fichiers `.log`, puis vous reposer sur un mode de langage de repli comme `plaintext` seulement pour `.log` :

```json
{
    "files.associations": {
        "*.log": "plaintext" // Force les fichiers .log à être traités comme plaintext
    },
    "editor.wordWrap": "off", // Par défaut : pas de retour à la ligne
    "[plaintext]": {
        "editor.wordWrap": "on" // Activer pour .log (et .txt, si souhaité)
    }
}
```

- **Pour Exclure `.txt`** : Si vous voulez que `.log` mais pas `.txt` aient le retour à la ligne, vous auriez besoin d'une extension personnalisée ou d'une configuration plus avancée (par exemple, une extension VS Code pour définir un mode `log` unique), car VS Code ne distingue pas nativement `.log` de `.txt` sans configuration supplémentaire.

### Tester `[log]` Directement
Si vous n'êtes pas sûr que `[log]` fonctionne directement (en raison d'une extension ou du comportement intégré de VS Code), essayez ceci :

```json
{
    "editor.wordWrap": "off",
    "[log]": {
        "editor.wordWrap": "on"
    }
}
```

Ouvrez un fichier `.log` et voyez si le retour à la ligne s'applique. Si ce n'est pas le cas, le mode de langage n'est pas `log`, et vous devrez utiliser l'une des options ci-dessus.

### Recommandation
- **Le Plus Simple** : Utilisez `[plaintext]` si cela vous convient que `.txt` et `.log` aient tous deux le retour à la ligne.
- **Spécifique** : Installez une extension "Log File Highlighter", confirmez que le mode est `log`, et utilisez `[log]`.
- Faites-moi savoir quel mode de langage affichent vos fichiers `.log`, et je peux affiner la solution davantage !

---

J'ai testé la configuration ci-dessous, et elle fonctionne parfaitement.

```json
   {
       "editor.wordWrap": "off", // Par défaut : pas de retour à la ligne
       "[log]": {
           "editor.wordWrap": "on" // Activer seulement pour les fichiers .log
       }
   }
```