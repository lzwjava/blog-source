---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Ouvrir Sublime Text depuis la CLI
translated: true
type: note
---

### Ouvrir Sublime Text depuis la ligne de commande (CLI)

Sublime Text n'inclut pas de commande `sublime` (ou `subl`) intégrée par défaut sur macOS (ce que vous semblez utiliser, d'après votre référence à `open -a`). Cependant, il existe une méthode officielle et simple pour l'ajouter en utilisant le script `subl` fourni avec Sublime. C'est plus propre que d'utiliser la commande `open`. Je vais vous présenter les options ci-dessous, en commençant par l'approche recommandée.

#### 1. **Installer la commande CLI officielle `subl` (Recommandé)**
Sublime Text inclut un exécutable `subl` dans son bundle d'application que vous pouvez symlinker vers un répertoire dans votre PATH (comme `/usr/local/bin`). Cela vous permet d'exécuter `subl .` (pour ouvrir le répertoire courant) ou `subl fichier.txt` depuis n'importe où dans le terminal.

**Étapes pour macOS (Sublime Text 3 ou 4) :**
- Ouvrez le Terminal.
- Exécutez cette commande pour créer le symlink (cela nécessite les privilèges d'admin, vous serez donc invité à saisir votre mot de passe) :
  ```
  sudo ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl
  ```
  - Si vous utilisez Sublime Text 3, le chemin peut être légèrement différent : `"/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl"` (ajustez le numéro de version si nécessaire).
  - Si `/usr/local/bin` n'est pas dans votre PATH, ajoutez-le à votre profil shell (par exemple, `~/.zshrc` ou `~/.bash_profile`) :
    ```
    echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```

- Testez-le : Naviguez vers un répertoire (par exemple, `cd ~/Desktop`) et exécutez :
  ```
  subl .
  ```
  Cela devrait ouvrir Sublime Text avec le dossier courant chargé.

Si le chemin du symlink ne fonctionne pas (par exemple, à cause de différences de version), vérifiez l'emplacement exact :
- Exécutez `find /Applications/Sublime\ Text.app -name subl` pour localiser le binaire.

**Pourquoi c'est bien :**
- C'est officiel et léger—aucun outil tiers n'est nécessaire.
- Fonctionne à l'échelle du système, comme une vraie CLI.
- Sublime Text 4 a même une option dans la console (View > Show Console) pour exécuter `sublime_installation` ou similaire, mais le symlink est la méthode la plus fiable.

**Si vous êtes sur Linux ou Windows :**
- Linux : Processus de symlink similaire—par exemple, `sudo ln -s /opt/sublime_text/sublime_text /usr/local/bin/subl`.
- Windows : Ajoutez `C:\Program Files\Sublime Text\sublime_text.exe` à votre PATH, ou utilisez un fichier batch pour `subl`.

#### 2. **Solution de secours : Utiliser la commande `open` (Aucune installation nécessaire)**
Si vous ne voulez pas vous embêter avec des symlinks ou le PATH, la commande `open` intégrée à macOS fonctionne très bien pour un usage basique. Elle est déjà disponible partout.

- Pour ouvrir le répertoire courant dans Sublime :
  ```
  open -a "Sublime Text" .
  ```
  - Note : Utilisez `"Sublime Text"` (avec un espace) si c'est le nom de votre application. Si c'est juste "Sublime.app", ajustez en conséquence. Vous pouvez vérifier le nom exact dans `/Applications/`.

- Pour ouvrir un fichier spécifique :
  ```
  open -a "Sublime Text" nomdufichier.txt
  ```

- Créez un alias pour plus de commodité : Ajoutez ceci à votre profil shell (`~/.zshrc` ou `~/.bash_profile`) pour imiter `subl` :
  ```
  alias subl='open -a "Sublime Text"'
  ```
  Puis rechargez avec `source ~/.zshrc` et utilisez `subl .` comme d'habitude.

**Pour/Contre :**
- Très simple et sans configuration.
- Mais c'est spécifique à macOS et moins flexible (par exemple, pas de moyen simple de spécifier des lignes ou des projets comme avec `subl`).

#### Dépannage
- **Commande introuvable ?** Assurez-vous que votre PATH inclut `/usr/local/bin` (exécutez `echo $PATH` pour vérifier).
- **Application non trouvée ?** Vérifiez que Sublime est dans `/Applications/`. S'il est ailleurs (par exemple, via Homebrew : `brew install --cask sublime-text`), ajustez les chemins.
- **Problèmes de permissions ?** Le symlink a besoin de sudo, mais une fois configuré, c'est bon.
- Si vous utilisez un gestionnaire de paquets comme Homebrew, vous pouvez installer Sublime via `brew install --cask sublime-text`, et il pourrait gérer la CLI pour vous.

Cela devrait vous permettre de bien démarrer ! Si vous rencontrez des erreurs ou si vous précisez votre OS/version, je peux affiner les étapes.