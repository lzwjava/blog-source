---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Configuration de LibreChat sans Docker Compose
translated: true
type: note
---

Oui, vous pouvez configurer LibreChat sans Docker Compose en utilisant des commandes `docker run` individuelles ou même une méthode non-Docker (installation manuelle avec Node.js, Yarn, MongoDB et MeiliSearch). Cela évite de télécharger le binaire `docker-compose` lui-même (qui est petit, ~20-30 Mo, mais je suppose que vous faites référence aux téléchargements d'images totaux d'environ ~70 Mo+ pour les services de LibreChat). Cependant, les images Docker principales (par exemple, pour l'application, MongoDB, MeiliSearch) représentent toujours un total d'environ 500 Mo-1 Go lorsqu'elles sont téléchargées — Docker Compose n'est qu'un outil d'orchestration au-dessus de Docker, pas le principal consommateur de bande passante. Le téléchargement des images sur une connexion 4G/5G lente restera le goulot d'étranglement, mais vous pouvez l'atténuer.

Je vais décrire les options ci-dessous, en priorisant d'abord les conseils pour économiser la bande passante. Si les données mobiles sont très limitées, envisagez de vous connecter temporairement à un réseau WiFi ou d'utiliser une configuration pré-téléchargée sur une autre machine (par exemple, exporter/importer des images via `docker save`/`docker load`).

### Conseils pour Économiser la Bande Passante pour Toute Configuration Basée sur Docker
- **Pré-télécharger les images sur une connexion plus rapide** : Sur un autre appareil avec une meilleure connexion Internet, exécutez `docker pull node:20-alpine` (pour l'application), `docker pull mongo:7` (base de données), et `docker pull getmeili/meilisearch:v1.10` (recherche). Ensuite, sauvegardez-les dans des fichiers :
  ```
  docker save -o librechat-app.tar node:20-alpine
  docker save -o mongo.tar mongo:7
  docker save -o meili.tar getmeili/meilisearch:v1.10
  ```
  Transférez les fichiers .tar via USB/lecteur (total ~500-800 Mo compressés), puis sur votre machine Ubuntu : `docker load -i librechat-app.tar` etc. Aucun téléchargement en ligne nécessaire.
- **Utiliser des alternatives plus légères** : Pour les tests, ignorez MeiliSearch initialement (il est optionnel pour la recherche ; désactivez-le dans la configuration). L'image MongoDB fait ~400 Mo — utilisez une installation MongoDB locale à la place (voir la section non-Docker ci-dessous) pour économiser ~400 Mo.
- **Surveiller l'utilisation** : Utilisez `docker pull --quiet` ou des outils comme `watch docker images` pour suivre.
- **Proxy ou cache** : Si vous avez un miroir Docker Hub ou un proxy, configurez-le dans `/etc/docker/daemon.json` pour accélérer les téléchargements.

### Option 1 : Docker Pur (Sans Compose) – Équivalent à la Configuration Compose
Vous pouvez reproduire le comportement de `docker-compose.yml` avec `docker run` et `docker network`. Cela télécharge les mêmes images mais vous permet de contrôler chaque étape. Le téléchargement total reste d'environ ~700 Mo+ (construction de l'app + bases de données).

1. **Créer un réseau Docker** (isole les services) :
   ```
   docker network create librechat-network
   ```

2. **Exécuter MongoDB** (remplacez `your_mongo_key` par un mot de passe fort) :
   ```
   docker run -d --name mongodb --network librechat-network \
     -e MONGO_INITDB_ROOT_USERNAME=librechat \
     -e MONGO_INITDB_ROOT_PASSWORD=your_mongo_key \
     -v $(pwd)/data/mongodb:/data/db \
     mongo:7
   ```
   - Crée `./data/mongodb` pour la persistance.

3. **Exécuter MeiliSearch** (remplacez `your_meili_key`) :
   ```
   docker run -d --name meilisearch --network librechat-network \
     -e MEILI_MASTER_KEY=your_meili_key \
     -p 7700:7700 \
     -v $(pwd)/data/meili:/meili_data \
     getmeili/meilisearch:v1.10
   ```
   - Ignorez cette étape si la bande passante est limitée ; désactivez dans la configuration de l'application plus tard.

4. **Cloner et Construire/Exécuter l'Application LibreChat** :
   - Cloner le repo si ce n'est pas fait : `git clone https://github.com/danny-avila/LibreChat.git && cd LibreChat` (~50 Mo de téléchargement pour le repo).
   - Construire l'image (cela télécharge la base Node.js ~200 Mo et construit les couches de l'application) :
     ```
     docker build -t librechat-app .
     ```
   - L'exécuter (se lie à la base de données, utilise les variables d'environnement — créez un fichier `.env` comme dans ma réponse précédente) :
     ```
     docker run -d --name librechat --network librechat-network -p 3080:3080 \
       --env-file .env \
       -v $(pwd):/app \
       librechat-app
     ```
     - Dans `.env`, définissez `MONGODB_URI=mongodb://librechat:your_mongo_key@mongodb:27017/LibreChat` et `MEILI_HOST=http://meilisearch:7700` etc.

5. **Accéder** : `http://localhost:3080`. Logs : `docker logs -f librechat`.

- **Arrêt/Nettoyage** : `docker stop mongodb meilisearch librechat && docker rm them`.
- **Avantages/Inconvénients** : Identique à Compose, mais plus manuel. Toujours lourd en données pour les téléchargements/constructions d'images.

### Option 2 : Installation Non-Docker (Manuelle, Sans Téléchargement d'Images) – Recommandée pour la Faible Bande Passante
Installez les dépendances nativement sur Ubuntu. Cela évite toute surcharge Docker (~0 Mo pour les conteneurs ; seulement les téléchargements de paquets via apt/yarn, totalisant ~200-300 Mo). Utilise indirectement vos configurations Python/Node système.

#### Prérequis (À Installer Une Fois)
```
sudo apt update
sudo apt install nodejs npm mongodb-org redis meilisearch git curl build-essential python3-pip -y  # Paquet officiel MongoDB ; binaire MeiliSearch ~50 Mo
sudo systemctl start mongod redis meilisearch
sudo systemctl enable mongod redis meilisearch
```
- Node.js : Si ce n'est pas la v20+, installez via nvm : `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash`, puis `nvm install 20`.
- Yarn : `npm install -g yarn`.
- Configuration MongoDB : Modifiez `/etc/mongod.conf` pour le lier à localhost, redémarrez.

#### Étapes d'Installation
1. **Cloner le Dépôt** :
   ```
   cd ~/projects
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   ```

2. **Installer les Dépendances** :
   ```
   yarn install  # ~100-200 Mo de téléchargements pour les paquets
   ```

3. **Configurer `.env`** (copiez depuis `.env.example`) :
   - `cp .env.example .env && nano .env`
   - Changements clés :
     - Mongo : `MONGODB_URI=mongodb://localhost:27017/LibreChat` (créez un utilisateur de base de données si nécessaire via le shell `mongo`).
     - Meili : `MEILI_HOST=http://localhost:7700` et `MEILI_MASTER_KEY=your_key`.
     - Désactiver la recherche si vous ignorez Meili : `SEARCH=false`.
     - Ajoutez les clés d'IA selon les besoins.

4. **Construire et Exécuter** :
   - Dans un terminal : `yarn run backend` (démarre l'API sur le port 3090).
   - Dans un autre : `yarn run frontend` (démarre l'interface utilisateur sur le port 3080).
   - Ou utilisez PM2 pour la production : `yarn global add pm2 && pm2 start yarn --name backend -- run backend` etc.

5. **Accéder** : `http://localhost:3080`. Créez un compte et configurez.

- **Données** : MongoDB stocke dans `/var/lib/mongodb`, Meili dans `/var/lib/meilisearch`.
- **Dépannage** :
  - Authentification Mongo : Exécutez `mongo` et créez un utilisateur : `use LibreChat; db.createUser({user: 'librechat', pwd: 'yourpass', roles: ['readWrite']})`.
  - Ports/Pare-feu : `sudo ufw allow 3080,3090,7700`.
  - Mises à jour : `git pull && yarn install && restart services`.
- **Avantages** : Plus léger en bande passante (pas de conteneurs), utilise les ressources système directement. Inconvénients : Configuration plus délicate, risques potentiels de conflits de dépendances (par exemple, avec votre Python 3.13, mais Node est séparé).

Si les données mobiles sont extrêmement limitées, la méthode non-Docker est la meilleure — faites-la par étapes, en surveillant avec `du -sh` sur les répertoires. Pour les erreurs, partagez les logs (par exemple, de `yarn run backend`). Guide non-Docker officiel : https://docs.librechat.ai/install/installation/manual_install.html. Si vous avez besoin de l'intégration Ollama pour l'IA locale (économise les coûts d'API), installez-la séparément via leur script (~100 Mo). Faites-moi savoir pour des ajustements !