---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Utiliser l'outil en ligne de commande Subl
translated: true
type: note
---

### Utilisation de la commande `subl` dans Sublime Text

Bonne nouvelle — votre CLI `subl` est déjà installée et fonctionnelle (comme l'a montré le résultat de `--help`) ! Il s'agit de Sublime Text build 4200 (une version récente), et `subl` est l'interface en ligne de commande officielle pour ouvrir des fichiers, des répertoires, et plus encore. Elle est extrêmement polyvalente pour les développeurs et les utilisateurs avancés.

Je vais la détailler avec des exemples pratiques. Exécutez-les depuis n'importe quel répertoire dans votre terminal. La syntaxe de base est :
```
subl [arguments] [fichiers ou répertoires]
```

#### 1. **Utilisation de base : Ouvrir des fichiers ou des répertoires**
- **Ouvrir le répertoire courant** (le charge en tant que projet/dossier dans Sublime) :
  ```
  subl .
  ```
  - Cela ouvre une nouvelle fenêtre avec le contenu du dossier actuel.

- **Ouvrir un fichier spécifique** :
  ```
  subl monfichier.txt
  ```
  - Ouvre `monfichier.txt` dans la fenêtre par défaut (ou une nouvelle si vous le souhaitez).

- **Ouvrir plusieurs fichiers/répertoires** :
  ```
  subl fichier1.txt fichier2.js ~/Documents/monprojet/
  ```
  - Ouvre tous les éléments dans Sublime.

- **Ouvrir à une ligne/colonne spécifique** (utile pour sauter vers des erreurs) :
  ```
  subl monfichier.py:42          # Ouvre à la ligne 42
  subl monfichier.py:42:5        # Ouvre à la ligne 42, colonne 5
  ```

#### 2. **Arguments courants (d'après l'aide)**
Voici les drapeaux les plus utiles avec des exemples. Combinez-les selon les besoins (par exemple, `subl -n fichier.txt`).

- **`-n` ou `--new-window`** : Ouvre toujours dans une nouvelle fenêtre.
  ```
  subl -n monfichier.txt
  ```
  - Pratique si vous voulez garder vos sessions Sublime existantes séparées.

- **`-a` ou `--add`** : Ajoute des fichiers/dossiers à votre fenêtre Sublime *actuelle* (si elle est déjà ouverte).
  ```
  subl -a nouveaudossier/
  ```
  - Cela ne crée pas une nouvelle fenêtre — idéal pour constituer un espace de travail.

- **`-w` ou `--wait`** : Attend que vous fermiez le(s) fichier(s) dans Sublime avant que la commande terminal ne se termine.
  ```
  subl -w monfichier.txt
  ```
  - Utile dans les scripts (par exemple, après une compilation, ouvrir et attendre la relecture). Impliqué lors de la lecture depuis stdin.

- **`-b` ou `--background`** : Ouvre sans amener Sublime au premier plan (garde le focus sur votre terminal).
  ```
  subl -b monfichier.txt
  ```

- **`-s` ou `--stay`** : Garde Sublime en focus après avoir fermé le fichier (pertinent seulement avec `-w`).
  ```
  subl -w -s monfichier.txt
  ```
  - Empêche le retour automatique au terminal.

- **`--project <project>`** : Ouvre un fichier projet Sublime spécifique (`.sublime-project`).
  ```
  subl --project MonProjet.sublime-project
  ```
  - Les projets sauvegardent les espaces de travail, paramètres, etc. Créez-en un via Fichier > Sauvegarder le Projet dans Sublime.

- **`--command <command>`** : Exécute une commande Sublime (par exemple, une action de plugin) sans ouvrir de fichiers.
  ```
  subl --command "build"    # Déclenche la commande de compilation si vous avez un système de compilation configuré
  ```
  - Vérifiez la console de Sublime (View > Show Console) pour les commandes disponibles.

- **`--launch-or-new-window`** : Ouvre une nouvelle fenêtre seulement si Sublime n'est pas déjà en cours d'exécution.
  ```
  subl --launch-or-new-window .
  ```
  - Efficace pour des vérifications rapides sans encombrer votre écran.

- **Support Stdin** (éditer l'entrée redirigée) :
  ```
  echo "Hello World" | subl -   # Ouvre stdin dans Sublime pour édition
  subl - > output.txt          # Édite stdin et sauvegarde les modifications dans output.txt
  ```
  - Après édition dans Sublime, sauvegardez et fermez pour continuer.

- **`--safe-mode`** : Lance Sublime sans plugins ni paramètres personnalisés (pour le dépannage).
  ```
  subl --safe-mode monfichier.txt
  ```

- **Autres drapeaux** :
  - `-h` ou `--help` : Affiche l'aide que vous avez déjà vue.
  - `-v` ou `--version` : Affiche la version (par exemple, `subl -v`).

#### 3. **Astuces pour un usage quotidien**
- **Fichiers commençant par `-`** : Si un nom de fichier ressemble à un drapeau (par exemple, `-config`), utilisez `--` pour séparer :
  ```
  subl -- -config.json
  ```
- **Alias pour plus de commodité** : Ajoutez des raccourcis à votre profil de shell (`~/.zshrc` pour zsh, ou `~/.bash_profile` pour bash) :
  ```
  alias st='subl'     # Alias plus court
  alias stt='subl -n' # Pour de nouveaux onglets/fenêtres
  ```
  Rechargez avec `source ~/.zshrc`.
- **Dans les scripts/GIT** : Utilisez-la dans des hooks ou alias, par exemple, `git diff | subl -` pour examiner les changements.
- **Vs. `open`** : Maintenant que `subl` est configurée, elle est préférable à `open -a "Sublime Text"` car elle supporte les lignes, les projets, et des fonctionnalités plus avancées.
- **Dépannage** :
  - Si `subl` cesse de fonctionner, réexécutez l'installation du lien symbolique depuis ma réponse précédente.
  - Pour les gros projets, utilisez `-a` pour éviter les fenêtres multiples.
  - Sur macOS, en cas de problèmes de focus, essayez d'abord sans `-b`.

Cela couvre 90% de ce dont vous aurez besoin ! Commencez par `subl .` dans un dossier de projet et expérimentez. Si vous avez un workflow spécifique ou une erreur, partagez plus de détails pour un conseil personnalisé.