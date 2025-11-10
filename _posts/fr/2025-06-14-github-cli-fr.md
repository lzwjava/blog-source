---
audio: false
generated: true
lang: fr
layout: post
title: Installation de GitHub CLI
translated: true
type: note
---

Pour installer GitHub CLI (`gh`) sur Ubuntu et l'utiliser pour déclencher des workflows GitHub Actions avec la commande `gh workflow run`, suivez ces étapes :

### Étapes d'installation de GitHub CLI (`gh`) sur Ubuntu

1. **Ajouter le dépôt GitHub CLI et la clé GPG** :
   Exécutez les commandes suivantes dans votre terminal pour configurer le dépôt de paquets officiel GitHub CLI :

   ```bash
   (type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
   && sudo mkdir -p -m 755 /etc/apt/keyrings \
   && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
   && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
   && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   ```

   Ce script :
   - Installe `wget` s'il n'est pas déjà présent.
   - Crée un répertoire pour les keyrings APT.
   - Télécharge et ajoute la clé GPG GitHub CLI.
   - Configure le dépôt GitHub CLI pour votre système.

2. **Mettre à jour l'index des paquets et installer `gh`** :
   Mettez à jour votre liste de paquets et installez l'outil en ligne de commande `gh` :

   ```bash
   sudo apt update
   sudo apt install gh -y
   ```

3. **Vérifier l'installation** :
   Vérifiez que `gh` est installé correctement en exécutant :

   ```bash
   gh --version
   ```

   Vous devriez voir une sortie comme `gh version X.Y.Z (YYYY-MM-DD)`, confirmant l'installation.

4. **S'authentifier avec GitHub** :
   Avant d'utiliser `gh`, authentifiez-vous avec votre compte GitHub :

   ```bash
   gh auth login
   ```

   Suivez les invites :
   - Choisissez `GitHub.com` (ou votre serveur d'entreprise le cas échéant).
   - Sélectionnez votre protocole préféré (`HTTPS` ou `SSH` ; `SSH` est recommandé si vous avez une clé SSH configurée).
   - Choisissez la méthode d'authentification (le navigateur est le plus simple ; il ouvre une page web pour se connecter).
   - Copiez le code à usage unique fourni, collez-le dans le navigateur et autorisez `gh`.
   - Confirmez les paramètres par défaut ou ajustez-les si nécessaire.

   Après une authentification réussie, vous verrez un message de confirmation.

### Utilisation de `gh workflow run` pour GitHub Actions

La commande `gh workflow run` déclenche un workflow GitHub Actions. Voici comment l'utiliser :

1. **Naviguer vers votre dépôt** (optionnel) :
   Si vous êtes dans un dépôt Git local lié à GitHub, `gh` le détectera automatiquement. Sinon, spécifiez le dépôt avec l'option `--repo`.

2. **Lister les workflows disponibles** (optionnel) :
   Pour trouver l'ID ou le nom de fichier du workflow, exécutez :

   ```bash
   gh workflow list
   ```

   Cela affiche tous les workflows du dépôt, montrant leurs noms, IDs et statuts (par exemple, `active`).

3. **Exécuter un workflow** :
   Utilisez la commande `gh workflow run` avec le nom de fichier ou l'ID du workflow. Par exemple :

   ```bash
   gh workflow run workflow.yml
   ```

   Ou, en utilisant l'ID du workflow (par exemple, `123456`) :

   ```bash
   gh workflow run 123456
   ```

   Si le workflow accepte des entrées, fournissez-les avec l'option `--field` :

   ```bash
   gh workflow run workflow.yml --field key=value
   ```

   Pour spécifier une branche ou une référence, utilisez l'option `--ref` :

   ```bash
   gh workflow run workflow.yml --ref branch-name
   ```

4. **Surveiller le workflow** :
   Après le déclenchement, vérifiez le statut de l'exécution :

   ```bash
   gh run list
   ```

   Pour surveiller une exécution spécifique en temps réel, utilisez :

   ```bash
   gh run watch <run-id>
   ```

   Remplacez `<run-id>` par l'ID d'exécution de `gh run list`.

### Conseils de dépannage

- **Erreurs de signature GPG** : Si vous rencontrez des problèmes liés à GPG pendant `apt update`, consultez le suivi des problèmes de GitHub pour des correctifs (par exemple, `cli/cli#9569`) ou réessayez l'étape d'importation de clé.[](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- **Problèmes de pare-feu** : Si `keyserver.ubuntu.com` échoue, essayez :

   ```bash
   sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key C99B11DEB97541F0
   ```

   Ou installez `dirmngr` si nécessaire :

   ```bash
   sudo apt-get install dirmngr
   ```

  [](https://gist.github.com/Manoj-Paramsetti/dc957bdd6a4430275d0fc28a0dc43ae9)
- **Avertissement sur l'installation Snap** : GitHub déconseille d'utiliser le paquet Snap pour `gh` en raison de problèmes d'exécution. Tenez-vous à la méthode APT ci-dessus.[](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- **Portées d'authentification** : Si `gh workflow run` échoue en raison de permissions, assurez-vous que votre token a la portée `workflow`. Réauthentifiez-vous avec :

   ```bash
   gh auth refresh -s workflow
   ```

### Notes supplémentaires

- **Manuel GitHub CLI** : Pour plus de détails sur les commandes `gh`, exécutez `gh help` ou visitez le manuel officiel à [cli.github.com](https://cli.github.com).[](https://cli.github.com/manual/)
- **Exigences du workflow** : Assurez-vous que le fichier de workflow (par exemple, `workflow.yml`) existe dans le répertoire `.github/workflows/` de votre dépôt et qu'il est configuré pour des déclenchements manuels (par exemple, événement `workflow_dispatch`).
- **Méthodes d'installation alternatives** : Vous pouvez également installer `gh` via Homebrew (`brew install gh`) ou en téléchargeant les binaires depuis la [page des releases](https://github.com/cli/cli/releases), mais la méthode APT est recommandée pour Ubuntu.[](https://github.com/cli/cli)

Cette configuration vous permet de gérer efficacement les workflows GitHub Actions depuis la ligne de commande sur Ubuntu. Faites-moi savoir si vous avez besoin d'aide avec des commandes `gh` spécifiques ou des configurations de workflow !