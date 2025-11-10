---
audio: false
generated: true
lang: fr
layout: post
title: Configuration des clés SSH pour le déploiement JAR avec GitHub Actions
translated: true
type: note
---

Pour générer une clé SSH pour GitHub Actions afin de déployer un fichier JAR, suivez ces étapes :

1. **Générer une paire de clés SSH** :
   - Sur votre machine locale ou dans un environnement sécurisé, exécutez :
     ```bash
     ssh-keygen -t ed25519 -C "your_email@example.com" -f github-actions-deploy
     ```
   - Si votre système ne prend pas en charge Ed25519, utilisez :
     ```bash
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f github-actions-deploy
     ```
   - Appuyez sur Entrée pour accepter l'emplacement par défaut du fichier et définissez éventuellement une phrase secrète (recommandé pour la sécurité). Cela crée deux fichiers :
     - `github-actions-deploy` (clé privée)
     - `github-actions-deploy.pub` (clé publique)

2. **Ajouter la clé publique au serveur cible** :
   - Copiez la clé publique :
     ```bash
     cat github-actions-deploy.pub
     ```
   - Connectez-vous au serveur où vous déploierez le fichier JAR.
   - Ajoutez la clé publique au fichier `~/.ssh/authorized_keys` sur le serveur :
     ```bash
     echo "your-public-key-content" >> ~/.ssh/authorized_keys
     ```
   - Assurez-vous que le fichier `authorized_keys` a les bonnes permissions :
     ```bash
     chmod 600 ~/.ssh/authorized_keys
     ```

3. **Stocker la clé privée dans les Secrets GitHub** :
   - Allez dans votre dépôt GitHub : `Settings > Secrets and variables > Actions > Secrets`.
   - Cliquez sur **New repository secret**.
   - Nommez le secret (par exemple, `SSH_PRIVATE_KEY`).
   - Collez le contenu de la clé privée (`github-actions-deploy`) :
     ```bash
     cat github-actions-deploy
     ```
   - Sauvegardez le secret.

4. **Configurer le workflow GitHub Actions** :
   - Créez ou modifiez un fichier de workflow (par exemple, `.github/workflows/deploy.yml`).
   - Ajoutez une étape pour utiliser la clé SSH pour déployer le JAR. Voici un exemple de workflow :

     ```yaml
     name: Deploy JAR

     on:
       push:
         branches:
           - main

     jobs:
       deploy:
         runs-on: ubuntu-latest

         steps:
         - name: Checkout code
           uses: actions/checkout@v4

         - name: Set up Java
           uses: actions/setup-java@v4
           with:
             java-version: '17' # Ajustez à votre version de Java
             distribution: 'temurin'

         - name: Build JAR
           run: mvn clean package # Ajustez pour votre outil de build (ex: Gradle)

         - name: Install SSH Key
           uses: shimataro/ssh-key-action@v2
           with:
             key: ${{ secrets.SSH_PRIVATE_KEY }}
             known_hosts: 'optional-known-hosts' # Voir la note ci-dessous

         - name: Add Known Hosts
           run: |
             ssh-keyscan -H <server-ip-or-hostname> >> ~/.ssh/known_hosts
           # Remplacez <server-ip-or-hostname> par l'IP ou le nom d'hôte de votre serveur

         - name: Deploy JAR to Server
           run: |
             scp target/your-app.jar user@<server-ip-or-hostname>:/path/to/deploy/
             ssh user@<server-ip-or-hostname> "sudo systemctl restart your-service" # Ajustez pour votre processus de déploiement
     ```

   - **Notes** :
     - Remplacez `target/your-app.jar` par le chemin vers votre fichier JAR.
     - Remplacez `user@<server-ip-or-hostname>` par l'utilisateur SSH et l'adresse de votre serveur.
     - Ajustez la commande de déploiement (par exemple, `sudo systemctl restart your-service`) pour correspondre à la façon dont vous démarrez ou déployez le JAR sur votre serveur.
     - L'étape `known_hosts` est critique pour éviter les problèmes de vérification d'hôte SSH. Si vous connaissez la clé hôte du serveur, vous pouvez la pré-remplir dans l'étape `shimataro/ssh-key-action`, ou utiliser `ssh-keyscan` comme montré.

5. **Sécuriser le workflow** :
   - Assurez-vous que la clé privée n'est jamais exposée dans les logs ou les sorties.
   - Restreignez les permissions du dépôt pour empêcher l'accès non autorisé aux secrets.
   - Si vous utilisez une phrase secrète pour la clé SSH, ajoutez-la comme un autre secret et incluez-la dans l'étape `shimataro/ssh-key-action` :
     ```yaml
     with:
       key: ${{ secrets.SSH_PRIVATE_KEY }}
       passphrase: ${{ secrets.SSH_KEY_PASSPHRASE }}
       known_hosts: 'optional-known-hosts'
     ```

6. **Tester le workflow** :
   - Poussez un changement vers la branche `main` (ou la branche spécifiée dans le workflow).
   - Surveillez le workflow dans l'onglet **Actions** de votre dépôt GitHub pour vous assurer que le JAR est construit et déployé correctement.

7. **Dépannage** :
   - **Permission denied** : Vérifiez que la clé SSH est correctement ajoutée au `authorized_keys` du serveur et que l'utilisateur a la permission d'accéder au répertoire cible.
   - **Host verification failed** : Assurez-vous que l'étape `known_hosts` est correctement configurée avec l'IP ou le nom d'hôte du serveur.
   - **Build issues** : Confirmez que la version de Java et les commandes de build correspondent à la configuration de votre projet.

Cette configuration intègre de manière sécurisée un déploiement basé sur SSH dans votre workflow GitHub Actions pour déployer un fichier JAR. Si vous avez besoin d'ajustements spécifiques (par exemple, pour une configuration serveur particulière ou un outil de build spécifique), faites-le-moi savoir !