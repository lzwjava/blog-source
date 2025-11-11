---
audio: false
generated: true
lang: fr
layout: post
title: TortoiseGit
translated: true
type: note
---

TortoiseGit est une extension shell Windows qui fournit une interface conviviale pour Git, le système de contrôle de version populaire. Il s'intègre directement dans l'Explorateur Windows, vous permettant d'effectuer des opérations Git via les menus contextuels. Ce guide couvre l'installation, la configuration et l'utilisation de TortoiseGit sur Windows, ainsi que les tâches courantes et les bonnes pratiques.

### Aperçu de TortoiseGit
TortoiseGit est construit au-dessus de msysGit (Git pour Windows) et fournit une interface graphique pour les commandes Git. Il est idéal pour les utilisateurs qui préfèrent une interface graphique aux opérations Git en ligne de commande. Les principales fonctionnalités incluent :
- Intégration du menu contextuel dans l'Explorateur Windows.
- Outils de diff et de fusion visuels.
- Prise en charge des workflows Git courants (commit, push, pull, branche, merge, etc.).
- Intégration avec les systèmes de suivi de problèmes et les outils externes populaires.

### Prérequis
Avant d'installer TortoiseGit, assurez-vous d'avoir :
- Un système d'exploitation Windows (Windows 10 ou ultérieur recommandé).
- Git pour Windows installé (TortoiseGit en dépend).
- Une compréhension basique des concepts Git (dépôts, commits, branches, etc.).

### Installation
1. **Installer Git pour Windows** :
   - Téléchargez la dernière version depuis [Git for Windows](https://gitforwindows.org/) ou [Git SCM](https://git-scm.com/downloads).
   - Exécutez l'installateur et suivez les invites. Paramètres recommandés :
     - Utilisez l'éditeur par défaut (par exemple, Notepad) ou choisissez-en un comme VS Code.
     - Sélectionnez "Use Git from the Windows Command Prompt" pour l'accessibilité.
     - Choisissez "OpenSSL" pour le transport HTTPS.
     - Sélectionnez "Checkout as-is, commit as-is" pour les fins de ligne (sauf si vous travaillez avec des équipes multiplateformes).
   - Terminez l'installation.

2. **Installer TortoiseGit** :
   - Téléchargez la dernière version depuis [le site officiel de TortoiseGit](https://tortoisegit.org/download/).
   - Exécutez l'installateur :
     - Choisissez la langue et les composants par défaut.
     - Assurez-vous que Git pour Windows est détecté (TortoiseGit vous demandera s'il est manquant).
     - Installez TortoiseGitPlink (recommandé pour SSH) si nécessaire.
   - Redémarrez votre ordinateur si vous y êtes invité.

3. **Vérifier l'Installation** :
   - Faites un clic droit dans n'importe quel dossier de l'Explorateur Windows. Vous devriez voir des options TortoiseGit comme "Git Clone", "Git Create Repository here", etc.

### Configuration Initiale
Après l'installation, configurez TortoiseGit pour vos détails utilisateur et préférences :
1. **Définir les Informations Utilisateur** :
   - Faites un clic droit dans un dossier, sélectionnez **TortoiseGit > Settings**.
   - Dans la fenêtre des paramètres, naviguez vers **Git > Config**.
   - Entrez votre nom et email (identique à celui utilisé sur GitHub, GitLab, etc.) :
     ```
     Name: Votre Nom
     Email: votre.email@exemple.com
     ```
   - Cliquez sur **Apply** puis **OK**.

2. **Configurer SSH (Optionnel)** :
   - Si vous utilisez SSH pour les dépôts distants, configurez une clé SSH :
     - Ouvrez **PuTTYgen** (installé avec TortoiseGit).
     - Générez une nouvelle paire de clés SSH, sauvegardez la clé privée et copiez la clé publique.
     - Ajoutez la clé publique à votre service d'hébergement Git (par exemple, GitHub, GitLab).
     - Dans les paramètres de TortoiseGit, sous **Git > Remote**, sélectionnez TortoiseGitPlink comme client SSH.

3. **Définir les Outils de Diff et de Fusion** :
   - Dans **TortoiseGit > Settings > Diff Viewer**, choisissez un outil comme TortoiseGitMerge (par défaut) ou un outil externe comme Beyond Compare.
   - Pour la fusion, configurez sous **Merge Tool** (TortoiseGitMerge est recommandé pour les débutants).

### Utilisation de Base
Voici les opérations TortoiseGit courantes, accessibles via les menus contextuels du clic droit dans l'Explorateur Windows.

#### 1. **Cloner un Dépôt**
   - Faites un clic droit dans un dossier et sélectionnez **Git Clone**.
   - Dans la boîte de dialogue :
     - Entrez l'URL du dépôt (par exemple, `https://github.com/nomutilisateur/depot.git`).
     - Spécifiez le répertoire local pour le dépôt.
     - Optionnellement, sélectionnez une branche ou chargez les clés SSH.
   - Cliquez sur **OK** pour cloner le dépôt.

#### 2. **Créer un Nouveau Dépôt**
   - Naviguez vers un dossier, faites un clic droit et sélectionnez **Git Create Repository here**.
   - Cochez "Make it Bare" si vous créez un dépôt côté serveur (rare pour un usage local).
   - Cliquez sur **OK**. Un dossier `.git` est créé, initialisant le dépôt.

#### 3. **Valider les Modifications (Commit)**
   - Ajoutez des fichiers à votre dossier de dépôt.
   - Faites un clic droit sur le dossier ou les fichiers sélectionnés, puis choisissez **Git Commit -> "main"** (ou la branche actuelle).
   - Dans la boîte de dialogue de validation :
     - Entrez un message de validation décrivant les modifications.
     - Sélectionnez les fichiers à mettre en stage (cases à cocher).
     - Cliquez sur **OK** ou **Commit & Push** pour pousser les modifications vers le dépôt distant.

#### 4. **Pousser les Modifications (Push)**
   - Après avoir validé, faites un clic droit et sélectionnez **TortoiseGit > Push**.
   - Choisissez le dépôt distant et la branche.
   - Authentifiez-vous si demandé (nom d'utilisateur/mot de passe pour HTTPS ou clé SSH).
   - Cliquez sur **OK** pour pousser.

#### 5. **Récupérer les Modifications (Pull)**
   - Pour mettre à jour votre dépôt local avec les modifications distantes, faites un clic droit et sélectionnez **TortoiseGit > Pull**.
   - Sélectionnez la branche distante et cliquez sur **OK**.
   - Résolvez les conflits si vous y êtes invité (utilisez l'outil de fusion).

#### 6. **Créer et Changer de Branches**
   - Faites un clic droit et sélectionnez **TortoiseGit > Create Branch**.
   - Entrez un nom de branche et cliquez sur **OK**.
   - Pour changer de branche, faites un clic droit et sélectionnez **TortoiseGit > Switch/Checkout**, puis choisissez la branche.

#### 7. **Voir l'Historique**
   - Faites un clic droit et sélectionnez **TortoiseGit > Show Log**.
   - Visualisez l'historique des commits, y compris l'auteur, la date et les messages.
   - Faites un clic droit sur un commit pour voir les modifications, le réverter ou le cherry-pick.

#### 8. **Résoudre les Conflits de Fusion**
   - Lors d'un pull ou d'une fusion, si des conflits surviennent, TortoiseGit vous en informera.
   - Faites un clic droit sur les fichiers en conflit et sélectionnez **TortoiseGit > Resolve**.
   - Utilisez l'outil de fusion pour éditer les conflits manuellement, puis marquez-les comme résolus.
   - Validez les modifications résolues.

### Fonctionnalités Avancées
1. **Mettre de Côté les Modifications (Stash)** :
   - Pour sauvegarder temporairement les modifications non validées, faites un clic droit et sélectionnez **TortoiseGit > Stash Save**.
   - Pour récupérer les modifications mises de côté, sélectionnez **TortoiseGit > Stash Pop**.

2. **Rebaser** :
   - Faites un clic droit et sélectionnez **TortoiseGit > Rebase**.
   - Choisissez la branche sur laquelle rebaser et suivez les invites pour réordonner ou squasher les commits.

3. **Sous-modules** :
   - Pour gérer les sous-modules, faites un clic droit et sélectionnez **TortoiseGit > Submodule Update** ou **Add**.
   - Configurez les paramètres des sous-modules dans les paramètres de TortoiseGit.

4. **Bisect** :
   - Pour trouver un commit ayant introduit un bug, utilisez **TortoiseGit > Bisect Start**.
   - Marquez les commits comme "good" ou "bad" pour cibler le commit problématique.

### Bonnes Pratiques
- **Valider Souvent** : Faites de petits commits fréquents avec des messages clairs.
- **Tirer Régulièrement** : Maintenez votre dépôt local à jour pour éviter les conflits.
- **Utiliser des Branches** : Créez des branches de fonctionnalité pour les nouveaux travaux afin de maintenir la branche principale stable.
- **Sauvegarder les Clés SSH** : Stockez les clés SSH de manière sécurisée et sauvegardez-les.
- **Réviser les Modifications** : Utilisez la visionneuse de diff pour réviser les modifications avant de valider.

### Dépannage
- **Problèmes d'Authentification** : Assurez-vous que les clés SSH ou les identifiants sont correctement configurés dans votre service d'hébergement Git.
- **Conflits de Fusion** : Utilisez TortoiseGitMerge pour résoudre les conflits visuellement. Sauvegardez les fichiers avant de fusionner.
- **Menu Contextuel Manquant** : Vérifiez que TortoiseGit est correctement installé et que l'intégration à l'Explorateur est activée dans les paramètres.
- **Lenteur des Performances** : Désactivez les superpositions d'icônes inutiles dans **TortoiseGit > Settings > Icon Overlays**.

### Exemple de Workflow
Voici un exemple de workflow pour contribuer à un projet :

# Exemple de Workflow TortoiseGit

## 1. Cloner le Dépôt
- Faites un clic droit dans un dossier, sélectionnez **Git Clone**.
- Entrez l'URL du dépôt et le répertoire local.
- Cliquez sur **OK**.

## 2. Créer une Branche de Fonctionnalité
- Faites un clic droit, sélectionnez **TortoiseGit > Create Branch**.
- Nommez la branche (par exemple, `feature/ajouter-connexion`).
- Cliquez sur **OK** et basculez vers la nouvelle branche.

## 3. Effectuer des Modifications
- Modifiez les fichiers dans le dossier du dépôt.
- Faites un clic droit, sélectionnez **Git Commit -> "feature/ajouter-connexion"**.
- Rédigez un message de validation et mettez les fichiers en stage.
- Cliquez sur **Commit**.

## 4. Pousser les Modifications
- Faites un clic droit, sélectionnez **TortoiseGit > Push**.
- Choisissez la branche distante (par exemple, `origin/feature/ajouter-connexion`).
- Cliquez sur **OK**.

## 5. Créer une Pull Request
- Sur votre service d'hébergement Git (par exemple, GitHub), créez une pull request de votre branche vers la branche principale.
- Attendez la revue et la fusion.

## 6. Mettre à Jour le Dépôt Local
- Basculez vers la branche principale (**TortoiseGit > Switch/Checkout**).
- Tirez les mises à jour (**TortoiseGit > Pull**).

### Ressources
- **Documentation Officielle** : [Documentation TortoiseGit](https://tortoisegit.org/docs/)
- **Git pour Windows** : [Git SCM](https://git-scm.com/)
- **Tutoriels** : Recherchez "TortoiseGit tutorial" sur YouTube ou les blogs techniques pour des guides visuels.

TortoiseGit simplifie les opérations Git avec son interface intuitive, rendant le contrôle de version accessible aux utilisateurs Windows. Si vous avez besoin d'aide pour des tâches spécifiques ou des configurations avancées, faites-le moi savoir !