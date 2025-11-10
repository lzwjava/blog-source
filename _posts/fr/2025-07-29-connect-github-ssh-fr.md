---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Se connecter à GitHub avec SSH
translated: true
type: note
---

Pour vous connecter à GitHub en utilisant SSH, suivez ces étapes basées sur la documentation GitHub fournie. Ce guide suppose que vous partez de zéro et inclut la vérification des clés existantes, la génération d'une nouvelle clé, son ajout à GitHub et le test de la connexion.

### 1. Vérifier l'existence de clés SSH
Avant de créer une nouvelle clé SSH, vérifiez si vous en avez déjà une :
- Ouvrez un terminal (sur macOS/Linux) ou Git Bash (sur Windows).
- Exécutez :
  ```bash
  ls -al ~/.ssh
  ```
- Recherchez des fichiers comme `id_rsa` et `id_rsa.pub` (ou similaires, par exemple `id_ed25519`, `id_ed25519.pub`). S'ils existent, vous avez peut-être déjà une clé. Si vous souhaitez utiliser une clé existante, passez à l'étape 3. Sinon, procédez pour générer une nouvelle clé.

### 2. Générer une nouvelle clé SSH
Si vous n'avez pas de clé SSH ou si vous en voulez une nouvelle :
- Dans votre terminal, générez une nouvelle clé SSH :
  ```bash
  ssh-keygen -t ed25519 -C "your_email@example.com"
  ```
  - Remplacez `your_email@example.com` par l'e-mail associé à votre compte GitHub.
  - Si votre système ne prend pas en charge `ed25519`, utilisez :
    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```
- Lorsque vous y êtes invité, appuyez sur Entrée pour enregistrer la clé à l'emplacement par défaut (`~/.ssh/id_ed25519` ou `~/.ssh/id_rsa`).
- Optionnellement, saisissez une phrase secrète pour plus de sécurité (ou appuyez sur Entrée pour ne pas en mettre).

### 3. Ajouter la clé SSH à l'agent SSH
L'agent SSH gère vos clés pour l'authentification :
- Démarrez l'agent SSH :
  ```bash
  eval "$(ssh-agent -s)"
  ```
- Ajoutez votre clé privée à l'agent :
  ```bash
  ssh-add ~/.ssh/id_ed25519
  ```
  - Si vous avez utilisé RSA, remplacez `id_ed25519` par `id_rsa`.
- Si vous avez défini une phrase secrète, vous serez invité à la saisir.

### 4. Ajouter la clé SSH à votre compte GitHub
- Copiez votre clé publique dans le presse-papiers :
  - Sur macOS :
    ```bash
    pbcopy < ~/.ssh/id_ed25519.pub
    ```
  - Sur Linux :
    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```
    Puis copiez manuellement la sortie.
  - Sur Windows (Git Bash) :
    ```bash
    cat ~/.ssh/id_ed25519.pub | clip
    ```
  - Si vous avez utilisé RSA, remplacez `id_ed25519.pub` par `id_rsa.pub`.
- Allez sur GitHub :
  - Connectez-vous à [GitHub](https://github.com).
  - Cliquez sur votre photo de profil (en haut à droite) → **Settings** → **SSH and GPG keys** → **New SSH key** ou **Add SSH key**.
  - Collez votre clé publique dans le champ « Key », donnez-lui un titre (par exemple, « Mon Portable ») et cliquez sur **Add SSH key**.

### 5. Tester votre connexion SSH
Vérifiez que votre clé SSH fonctionne avec GitHub :
- Exécutez :
  ```bash
  ssh -T git@github.com
  ```
- Si vous y êtes invité, confirmez en tapant `yes`.
- Vous devriez voir un message comme :
  ```
  Hi username! You've successfully authenticated, but GitHub does not provide shell access.
  ```
  Cela confirme que votre connexion SSH fonctionne.

### 6. Configurer Git pour utiliser SSH
Assurez-vous que votre dépôt Git utilise SSH pour l'authentification :
- Vérifiez l'URL distante de votre dépôt :
  ```bash
  git remote -v
  ```
- Si l'URL commence par `https://`, changez-la pour SSH :
  ```bash
  git remote set-url origin git@github.com:username/repository.git
  ```
  - Remplacez `username/repository` par votre nom d'utilisateur GitHub et le nom du dépôt.

### 7. Optionnel : Gérer les phrases secrètes des clés SSH
Si vous avez défini une phrase secrète, vous pouvez configurer l'agent SSH pour éviter de la ressaisir :
- Sur macOS, ajoutez votre clé au trousseau :
  ```bash
  ssh-add --apple-use-keychain ~/.ssh/id_ed25519
  ```
- Sur Linux/Windows, l'agent SSH demande généralement la phrase secrète une seule fois par session.

### 8. Optionnel : Utiliser le Forwarding de l'agent SSH ou les clés de déploiement
- **Forwarding de l'agent SSH** : Si vous déployez sur un serveur, activez le forwarding de l'agent pour utiliser vos clés SSH locales en toute sécurité. Ajoutez à votre `~/.ssh/config` :
  ```bash
  Host example.com
      ForwardAgent yes
  ```
  Remplacez `example.com` par le nom d'hôte de votre serveur.
- **Clés de déploiement** : Pour les scripts automatisés, générez une clé SSH distincte pour chaque serveur et ajoutez-la comme clé de déploiement dans les paramètres de votre dépôt GitHub.

### Dépannage
- Si `ssh -T git@github.com` échoue, assurez-vous que :
  - Votre clé publique est correctement ajoutée à GitHub.
  - L'agent SSH est en cours d'exécution et votre clé est ajoutée (`ssh-add -l` pour lister les clés chargées).
  - Les permissions des fichiers sont correctes :
    ```bash
    chmod 600 ~/.ssh/id_ed25519
    chmod 644 ~/.ssh/id_ed25519.pub
    ```
- Pour d'autres problèmes, consultez le guide de dépannage de GitHub.

Vous pouvez maintenant utiliser SSH pour interagir avec GitHub de manière sécurisée sans avoir à saisir vos informations d'identification à plusieurs reprises.

[Connecting to GitHub with SSH - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)