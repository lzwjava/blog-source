---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Installation de LibreChat sur Ubuntu
translated: true
type: note
---

### Installation de LibreChat sur Ubuntu 24.04 LTS

LibreChat est une plateforme de chat IA open source qui prend en charge plusieurs modèles d'IA (par exemple, OpenAI, Gemini, Ollama) via une interface web. La méthode d'installation recommandée est d'utiliser Docker Compose, car elle est simple, gère automatiquement les dépendances comme MongoDB et MeiliSearch, et fonctionne de manière fiable sur Ubuntu. Votre système (Ubuntu 24.04.2 LTS avec Python 3.13.4) répond aux exigences, mais vous devrez d'abord installer Docker et Git.

#### Prérequis
1. **Mettez à jour votre système** :
   ```
   sudo apt update && sudo apt upgrade -y
   ```

2. **Installez Git** (s'il n'est pas déjà installé) :
   ```
   sudo apt install git -y
   ```

3. **Installez Docker et Docker Compose** :
   - Installez Docker :
     ```
     sudo apt install docker.io -y
     sudo systemctl start docker
     sudo systemctl enable docker
     sudo usermod -aG docker $USER
     ```
     Déconnectez-vous et reconnectez-vous (ou exécutez `newgrp docker`) pour que les changements de groupe prennent effet.
   - Installez Docker Compose (dernière version) :
     ```
     sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
     sudo chmod +x /usr/local/bin/docker-compose
     ```
     Vérifiez avec `docker-compose --version`.

#### Étapes d'installation
1. **Clonez le dépôt LibreChat** :
   ```
   cd ~/projects  # Ou votre répertoire préféré
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   ```

2. **Copiez et configurez le fichier d'environnement** :
   - Copiez le fichier d'exemple :
     ```
     cp .env.example .env
     ```
   - Modifiez `.env` avec un éditeur de texte (par exemple, `nano .env`). Paramètres clés à mettre à jour :
     - Définissez une clé maître MongoDB : Générez un mot de passe fort et définissez `MONGODB_URI=mongodb://mongodb:27017/LibreChat?authSource=admin` et `MONGODB_MASTER_KEY=votre_clé_générée_ici`.
     - Pour MeiliSearch : Définissez `MEILI_MASTER_KEY=votre_clé_générée_ici` (générez une clé forte).
     - Ajoutez les clés API d'IA si nécessaire (par exemple, `OPENAI_API_KEY=votre_clé_openai`). Pour les modèles locaux comme Ollama, aucune clé n'est requise initialement.
     - Sauvegardez et quittez. Pour toutes les options de configuration, reportez-vous à la documentation.

3. **Démarrez LibreChat avec Docker Compose** :
   ```
   docker-compose up -d
   ```
   - Cette commande télécharge les images, démarre les services (application LibreChat, MongoDB, MeiliSearch) et s'exécute en mode détaché.
   - Attendez qu'il soit complètement démarré (vérifiez avec `docker-compose logs -f`).

4. **Accédez à LibreChat** :
   - Ouvrez votre navigateur et allez à l'adresse `http://localhost:3080`.
   - Créez un compte sur la page de connexion.
   - Sélectionnez un modèle d'IA (configurez les endpoints dans les paramètres) et commencez à discuter.

#### Conseils post-installation
- **Arrêt/Mise à jour** : Exécutez `docker-compose down` pour arrêter, puis `git pull` et `docker-compose up -d --build` pour mettre à jour.
- **Persistance des données** : Les volumes sont créés automatiquement pour les données MongoDB (dans `./data/mongodb`).
- **Dépannage** :
  - En cas de conflit de ports, modifiez `docker-compose.yml` pour changer `3080:3080`.
  - Pour un accès sans interface graphique/serveur, utilisez l'IP de votre serveur (par exemple, `http://ip-de-votre-serveur:3080`) et assurez-vous que le pare-feu autorise le port 3080 (`sudo ufw allow 3080`).
  - Si vous utilisez des LLM locaux, installez Ollama séparément et ajoutez-le comme endpoint dans `.env`.
- **Alternative : Méthode NPM** (sans Docker) : Si vous préférez, installez manuellement Node.js 18+, Yarn, MongoDB et MeiliSearch, puis exécutez `yarn install` et `yarn run frontend` + `yarn run backend`. Mais Docker est fortement recommandé pour sa simplicité.

Cela devrait vous permettre de démarrer rapidement. Si vous rencontrez des erreurs, partagez le résultat pour obtenir plus d'aide !

[Documentation Officielle de LibreChat](https://docs.librechat.ai/install/installation/docker_compose.html)  
[Guide Docker pour Ubuntu](https://docs.librechat.ai/install/installation/docker_ubuntu.html)  
[Tutoriel It's FOSS](https://itsfoss.com/librechat-linux/)