---
audio: true
generated: false
lang: fr
layout: post
title: Activer l'enroulement de texte uniquement pour des extensions de fichiers spécifiques
translated: true
---

J'assume que vous demandez comment configurer Visual Studio Code (VS Code) pour activer l'enroulement des mots uniquement pour certaines extensions de fichiers. Voici comment procéder :

1. **Ouvrir les paramètres de VS Code** :
   - Appuyez sur `Ctrl + ,` (ou `Cmd + ,` sur macOS) pour ouvrir les paramètres, ou allez dans `Fichier > Préférences > Paramètres`.

2. **Utiliser le fichier de paramètres JSON** :
   - Dans l'interface des paramètres, cliquez sur l'icône `{}` en haut à droite pour ouvrir le fichier `settings.json`. Cela permet un contrôle plus précis.

3. **Configurer l'enroulement des mots par type de fichier** :
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
   - `"editor.wordWrap": "off"` définit le comportement par défaut à pas d'enroulement.
   - `"[markdown]"` et `"[plaintext]"` sont des identifiants de langage pour les fichiers Markdown et texte brut, respectivement. Vous pouvez les remplacer par d'autres identifiants de langage comme `[javascript]`, `[python]`, etc., en fonction des extensions de fichiers que vous souhaitez cibler.
   - `"editor.wordWrap": "on"` active l'enroulement pour ces types de fichiers spécifiques.

5. **Trouver les identifiants de langage** :
   - Si vous n'êtes pas sûr de l'identifiant de langage pour une extension de fichier, ouvrez un fichier de ce type dans VS Code, cliquez sur le mode de langage dans le coin inférieur droit (par exemple, "Texte brut" ou "Python"), et notez l'identifiant affiché dans la palette de commandes lors de la sélection d'un langage.

6. **Enregistrer et tester** :
   - Enregistrez le fichier `settings.json`, et VS Code appliquera les paramètres immédiatement. Ouvrez des fichiers avec différentes extensions pour confirmer le comportement.

Cette approche garantit que l'enroulement des mots est activé uniquement pour les types de fichiers que vous spécifiez, laissant tous les autres inchangés. Faites-moi savoir si vous avez besoin d'aide pour des extensions spécifiques !

---

Si vous travaillez avec des fichiers `.log` dans Visual Studio Code et que vous souhaitez activer l'enroulement des mots spécifiquement pour eux, vous devrez vous assurer que VS Code les reconnaît comme un mode de langage distinct. Par défaut, les fichiers `.log` peuvent ne pas avoir un identifiant de langage unique comme `[log]` — ils sont souvent traités comme du texte brut (`[plaintext]`). Cependant, vous pouvez configurer ce comportement. Voici comment procéder :

### Option 1 : Utiliser `[plaintext]` si les fichiers `.log` sont du texte brut
Si vos fichiers `.log` sont reconnus comme du texte brut (vérifiez le mode de langage dans le coin inférieur droit de VS Code lorsqu'un fichier `.log` est ouvert), vous pouvez simplement utiliser `[plaintext]` :

```json
{
    "editor.wordWrap": "off", // Par défaut : pas d'enroulement
    "[plaintext]": {
        "editor.wordWrap": "on" // Activer pour les fichiers .txt et .log (si reconnus comme texte brut)
    }
}
```

- **Note** : Cela s'appliquera à tous les fichiers texte brut (par exemple, `.txt`, `.log`), pas seulement aux fichiers `.log`. Si cela est trop large, passez à l'Option 2.

### Option 2 : Associer les fichiers `.log` à un mode de langage personnalisé
Si vous souhaitez que `[log]` fonctionne comme un identifiant spécifique, vous devez indiquer à VS Code d'associer les fichiers `.log` à un mode de langage "Log". Voici comment :

1. **Installer une extension de fichier de log (optionnel)** :
   - Installez une extension comme "Log File Highlighter" depuis le marché VS Code. Cette extension assigne souvent aux fichiers `.log` un mode de langage spécifique (par exemple, `log`).
   - Après l'installation, vérifiez le mode de langage pour un fichier `.log` (coin inférieur droit). S'il indique "Log" ou similaire, vous pouvez utiliser `[log]` directement.

2. **Associer manuellement les fichiers `.log`** :
   - Si vous ne souhaitez pas d'extension, vous pouvez associer manuellement `.log` à un mode de langage via `files.associations` dans `settings.json` :
   ```json
   {
       "files.associations": {
           "*.log": "log" // Associe .log au mode de langage "log"
       },
       "editor.wordWrap": "off", // Par défaut : pas d'enroulement
       "[log]": {
           "editor.wordWrap": "on" // Activer pour les fichiers .log uniquement
       }
   }
   ```
   - **Caveat** : Le mode de langage `log` doit exister (par exemple, fourni par une extension ou VS Code). S'il n'existe pas, VS Code pourrait revenir au texte brut, et `[log]` ne fonctionnera pas comme prévu sans personnalisation supplémentaire.

3. **Vérifier le mode de langage** :
   - Ouvrez un fichier `.log`, cliquez sur le mode de langage dans le coin inférieur droit, et voyez ce qu'il est défini. S'il est `log` après vos modifications, `[log]` fonctionnera. S'il est toujours `plaintext`, utilisez `[plaintext]` ou ajustez l'association.

### Option 3 : Affiner avec des motifs de fichiers (le plus précis)
Pour un contrôle ultime, vous pouvez utiliser le paramètre `"files.associations"` pour cibler spécifiquement les fichiers `.log`, puis compter sur un mode de langage de secours comme `plaintext` uniquement pour `.log` :

```json
{
    "files.associations": {
        "*.log": "plaintext" // Force les fichiers .log à être traités comme du texte brut
    },
    "editor.wordWrap": "off", // Par défaut : pas d'enroulement
    "[plaintext]": {
        "editor.wordWrap": "on" // Activer pour .log (et .txt, si souhaité)
    }
}
```

- **Pour exclure `.txt`** : Si vous souhaitez que `.log` mais pas `.txt` s'enroule, vous aurez besoin d'une extension personnalisée ou d'une configuration plus avancée (par exemple, une extension VS Code pour définir un mode `log` unique), car VS Code ne distingue pas nativement `.log` de `.txt` sans configuration supplémentaire.

### Tester `[log]` directement
Si vous n'êtes pas sûr que `[log]` fonctionne directement (en raison d'une extension ou du comportement intégré de VS Code), essayez ceci :

```json
{
    "editor.wordWrap": "off",
    "[log]": {
        "editor.wordWrap": "on"
    }
}
```

Ouvrez un fichier `.log` et voyez si l'enroulement s'applique. S'il ne s'applique pas, le mode de langage n'est pas `log`, et vous devrez utiliser l'une des options ci-dessus.

### Recommandation
- **Le plus simple** : Utilisez `[plaintext]` si vous êtes d'accord pour que `.txt` et `.log` s'enroulent tous les deux.
- **Spécifique** : Installez une extension "Log File Highlighter", confirmez que le mode est `log`, et utilisez `[log]`.
- Faites-moi savoir quel mode de langage vos fichiers `.log` affichent, et je pourrai affiner la solution davantage !

---

J'ai testé la configuration ci-dessous, et elle fonctionne parfaitement.

```json
   {
       "editor.wordWrap": "off", // Par défaut : pas d'enroulement
       "[log]": {
           "editor.wordWrap": "on" // Activer pour les fichiers .log uniquement
       }
   }
```