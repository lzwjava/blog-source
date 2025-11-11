---
audio: false
generated: true
lang: fr
layout: post
title: Guide du contrôle de source de VS Code
translated: true
type: note
---

Visual Studio Code (VS Code) dispose d'une prise en charge intégrée robuste du contrôle de code source, permettant aux développeurs de gérer des systèmes de contrôle de version (VCS) comme Git, Mercurial et autres directement dans l'éditeur. Ce guide fournit un aperçu complet de l'utilisation du contrôle de code source dans VS Code, en se concentrant sur Git, car c'est le VCS le plus couramment utilisé, et couvre la configuration, les fonctionnalités clés, les workflows et l'utilisation avancée.

### Aperçu du Contrôle de Code Source dans VS Code
La vue Contrôle de code source de VS Code fournit une interface intuitive pour interagir avec les systèmes de contrôle de version. Elle s'intègre à Git par défaut et prend en charge les extensions pour d'autres VCS. La vue Contrôle de code source affiche les modifications, permet la mise en stage, le commit, le branchement, la fusion, et plus encore, le tout sans quitter l'éditeur. Voici un guide étape par étape pour tirer parti efficacement du contrôle de code source.

### 1. **Configuration du Contrôle de Code Source dans VS Code**
Pour utiliser le contrôle de code source, vous devez avoir Git installé et un repository initialisé. Voici comment le configurer :

#### Prérequis
- **Installer Git** : Téléchargez et installez Git depuis [git-scm.com](https://git-scm.com/). Vérifiez l'installation en exécutant `git --version` dans un terminal.
- **Configurer Git** :
  ```bash
  git config --global user.name "Votre Nom"
  git config --global user.email "votre.email@example.com"
  ```
- **Installer VS Code** : Assurez-vous d'avoir la dernière version de VS Code installée depuis [code.visualstudio.com](https://code.visualstudio.com/).

#### Initialiser un Repository Git
1. Ouvrez un dossier de projet dans VS Code.
2. Ouvrez le Terminal (Ctrl+` ou Cmd+` sur macOS) et exécutez :
   ```bash
   git init
   ```
   Cela crée un dossier `.git` dans votre projet, l'initialisant comme un repository Git.
3. Alternativement, clonez un repository existant :
   ```bash
   git clone <repository-url>
   ```
   Puis ouvrez le dossier cloné dans VS Code.

#### Activer la Vue Contrôle de Code Source
- Ouvrez la vue Contrôle de code source en cliquant sur l'icône Contrôle de code source dans la Barre d'activité (la troisième icône en partant du haut, ressemblant à une branche) ou en appuyant sur `Ctrl+Shift+G` (Windows/Linux) ou `Cmd+Shift+G` (macOS).
- Si un repository Git est détecté, VS Code affiche la vue Contrôle de code source avec des options pour gérer les modifications.

### 2. **Utilisation de la Vue Contrôle de Code Source**
La vue Contrôle de code source est le centre névralgique pour les tâches de contrôle de version. Elle montre :
- **Modifications** : Fichiers modifiés, ajoutés ou supprimés depuis le dernier commit.
- **Modifications en Stage** : Fichiers prêts à être commités.
- **Boîte de Message de Commit** : Où vous saisissez les messages de commit.
- **Actions** : Boutons pour committer, actualiser, et plus.

#### Workflow Courant
1. **Effectuer des Modifications** : Modifiez les fichiers dans votre projet. VS Code détecte automatiquement les modifications et les liste sous "Modifications" dans la vue Contrôle de code source.
2. **Mettre en Stage les Modifications** :
   - Cliquez sur l'icône `+` à côté d'un fichier pour le mettre en stage, ou utilisez l'option `Stage All Changes` (menu des trois points > Stage All Changes).
   - La mise en stage prépare les modifications pour le prochain commit.
3. **Rédiger un Message de Commit** :
   - Saisissez un message descriptif dans la zone de texte en haut de la vue Contrôle de code source.
   - Exemple : `Add user authentication feature`.
4. **Commiter les Modifications** :
   - Cliquez sur l'icône en forme de coche ou appuyez sur `Ctrl+Enter` (Windows/Linux) ou `Cmd+Enter` (macOS) pour committer les modifications en stage.
   - Utilisez le menu des trois points pour choisir entre `Commit All`, `Commit Staged`, ou `Commit All and Push`.
5. **Pousser vers le Remote** :
   - Si connecté à un repository distant (ex: GitHub), poussez les modifications en utilisant l'option `Push` dans le menu des trois points ou exécutez `git push` dans le terminal.

### 3. **Fonctionnalités Clés du Contrôle de Code Source dans VS Code**
VS Code fournit plusieurs fonctionnalités pour rationaliser le contrôle de version :

#### Vue Diff
- Cliquez sur un fichier sous "Modifications" pour ouvrir une vue diff côte à côte, montrant les modifications par rapport au dernier commit.
- Utilisez les actions inline pour mettre en stage ou ignorer des lignes spécifiques.

#### Gestion des Branches
- Changer de branche : Cliquez sur le nom de la branche dans la barre d'état en bas à gauche ou utilisez le menu des branches de la vue Contrôle de code source (trois points > Branch > Checkout to...).
- Créer une nouvelle branche : Sélectionnez `Create Branch` dans le menu des branches, saisissez un nom et confirmez.
- Fusionner des branches : Utilisez `Branch > Merge Branch` et sélectionnez la branche à fusionner dans la branche actuelle.

#### Pull et Fetch
- **Pull** : Synchronisez les modifications depuis le repository distant en utilisant l'option `Pull` dans le menu des trois points.
- **Fetch** : Récupérez les modifications distantes sans les fusionner en utilisant `Fetch`.

#### Résoudre les Conflits
- Lors de fusions ou de pulls, des conflits peuvent survenir. VS Code met en évidence les conflits dans les fichiers et fournit une interface de résolution de conflits inline :
  - Choisissez `Accept Current Change`, `Accept Incoming Change`, `Accept Both Changes`, ou modifiez le fichier manuellement.
  - Mettez en stage et committez le fichier résolu.

#### Extension Git Lens
Pour des fonctionnalités Git avancées, installez l'extension **GitLens** :
- Visualisez l'historique des commits, les annotations blame et les modifications de fichiers.
- Accédez à des insights du repository comme les commits récents et les stashes.
- Installez via la vue Extensions (`Ctrl+Shift+X` ou `Cmd+Shift+X`).

### 4. **Utilisation Avancée**
#### Stasher les Modifications
- Sauvegardez temporairement les modifications non commitées :
  - Allez dans le menu des trois points > Stash > Stash.
  - Appliquez ou récupérez les stashes plus tard via le même menu.
- Utile pour changer de branche sans committer un travail incomplet.

#### Commandes Git dans le Terminal
- Pour les tâches non directement prises en charge dans l'UI, utilisez le terminal intégré :
  ```bash
  git rebase <branch>
  git cherry-pick <commit>
  git log --oneline
  ```

#### Personnalisation du Contrôle de Code Source
- **Paramètres** : Ajustez le comportement du contrôle de code source dans les paramètres de VS Code (`Ctrl+,` ou `Cmd+,`) :
  - `git.autoRepositoryDetection` : Active/désactive la détection automatique des repositories Git.
  - `git.enableSmartCommit` : Committe toutes les modifications lorsqu'aucun fichier n'est en stage.
- **Fournisseurs SCM** : Installez des extensions pour d'autres VCS comme Mercurial ou SVN.

#### Intégration GitHub
- Utilisez l'extension **GitHub Pull Requests and Issues** pour gérer les PRs et les issues directement dans VS Code.
- Authentifiez-vous avec GitHub via le menu Accounts (coin inférieur gauche) pour pousser/tirer depuis les repositories GitHub.

### 5. **Exemple de Workflow : Créer et Pousser une Feature Branch**
Voici un exemple pratique d'un workflow Git courant dans VS Code :


# Exemple de Workflow Git dans VS Code

## Étapes pour Créer et Pousser une Feature Branch

1. **Créer une Nouvelle Branche** :
   - Dans la vue Contrôle de code source, cliquez sur le nom de la branche dans la barre d'état ou utilisez le menu des trois points > Branch > Create Branch.
   - Nommez la branche, par exemple `feature/add-login`.
   - VS Code bascule vers la nouvelle branche.

2. **Effectuer et Mettre en Stage les Modifications** :
   - Modifiez les fichiers (ex: ajoutez un composant de connexion à `src/Login.js`).
   - Dans la vue Contrôle de code source, les fichiers apparaissent sous "Modifications".
   - Cliquez sur l'icône `+` pour mettre en stage les modifications ou sélectionnez "Stage All Changes."

3. **Commiter les Modifications** :
   - Saisissez un message de commit, par exemple `Add login component`.
   - Cliquez sur la coche ou appuyez sur `Ctrl+Enter` (Windows/Linux) ou `Cmd+Enter` (macOS) pour committer.

4. **Pousser la Branche** :
   - Si aucun remote n'existe, ajoutez-en un :
     ```bash
     git remote add origin <repository-url>
     ```
   - Poussez la branche : Menu des trois points > Push, ou exécutez :
     ```bash
     git push -u origin feature/add-login
     ```

5. **Créer une Pull Request** :
   - Si vous utilisez GitHub, ouvrez le repository dans un navigateur ou utilisez l'extension GitHub Pull Requests pour créer une PR.
   - Liez la PR à la branche `feature/add-login`.

## Conseils
- Tirez régulièrement les mises à jour depuis la branche principale pour éviter les conflits.
- Utilisez des messages de commit descriptifs pour une meilleure collaboration.
- Installez GitLens pour des vues améliorées de l'historique des commits et du blame.


### 6. **Résolution des Problèmes Courants**
- **Git Non Détecté** : Assurez-vous que Git est installé et ajouté à votre PATH système. Redémarrez VS Code après l'installation.
- **Erreurs d'Authentification** : Configurez les clés SSH ou utilisez un token d'accès personnel pour GitHub/GitLab. Authentifiez-vous via le menu Accounts.
- **Conflits de Fusion** : Utilisez les outils de résolution de conflits inline ou modifiez les fichiers manuellement, puis mettez en stage et committez.
- **Lenteur des Performances** : Désactivez `git.autoRepositoryDetection` pour les grands projets ou utilisez GitLens pour des opérations Git optimisées.

### 7. **Bonnes Pratiques**
- **Commiter Souvent** : Faites de petits commits logiques pour suivre la progression.
- **Utiliser des Messages Descriptifs** : Suivez une convention comme `<type>(<scope>): <description>` (ex: `feat(auth): add login endpoint`).
- **Tirer Régulièrement** : Restez synchronisé avec le repository distant pour minimiser les conflits.
- **Sauvegarder les Stashes** : Avant d'appliquer les stashes, assurez-vous qu'ils ne vont pas écraser des modifications importantes.
- **Tirer Parti des Extensions** : Utilisez GitLens, Git History, ou Git Graph pour une fonctionnalité améliorée.

### 8. **Ressources Supplémentaires**
- **Documentation VS Code** : [Version Control in VS Code](https://code.visualstudio.com/docs/editor/versioncontrol)
- **Documentation Git** : [git-scm.com/doc](https://git-scm.com/doc)
- **Extension GitLens** : Disponible dans le VS Code Marketplace.
- **Extension GitHub Pull Requests** : Pour gérer les PRs et les issues.

Ce guide couvre les essentiels et les fonctionnalités avancées du contrôle de code source dans VS Code, avec un accent sur Git. En suivant ces étapes et bonnes pratiques, vous pouvez gérer efficacement les workflows de contrôle de version directement dans l'éditeur.