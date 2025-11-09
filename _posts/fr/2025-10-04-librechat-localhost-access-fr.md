---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Dépannage de l'Accès Localhost à LibreChat
translated: true
type: note
---

### Dépannage de l'accès à LibreChat sur localhost:3080

D'après vos logs, les images Docker ont été téléchargées avec succès (après quelques délais d'attente et nouvelles tentatives initiales), et 6 composants ont démarré : le réseau par défaut, `vectordb`, `chat-mongodb`, `chat-meilisearch`, `rag_api`, et `LibreChat`. Cependant, le service `api` (qui sert généralement le backend sur le port 3080) n'est pas listé dans les conteneurs démarrés—c'est probablement la raison pour laquelle vous ne pouvez pas accéder au site. Le conteneur `LibreChat` est probablement le frontend, qui dépend du backend `api`.

Les avertissements UID/GID suggèrent des problèmes de permissions potentiels qui pourraient empêcher le conteneur `api` de démarrer correctement. Voici un guide étape par étape pour diagnostiquer et résoudre ce problème.

#### 1. **Vérifier les conteneurs en cours d'exécution et les ports**
   Exécutez cette commande pour voir tous les conteneurs actifs, leur statut et le mappage des ports :
   ```
   docker ps
   ```
   - Recherchez un conteneur `api` (il pourrait s'appeler `librechat_api` ou similaire). S'il est manquant ou arrêté, c'est le problème.
   - Confirmez si le port `3080` est mappé (par exemple, `0.0.0.0:3080->3080/tcp`). Sinon, le service ne l'expose pas.
   - Si aucun conteneur n'affiche le port 3080, passez aux étapes suivantes.

#### 2. **Vérifier les logs des conteneurs**
   Inspectez les logs pour trouver des erreurs au démarrage, en particulier pour les services `api` et `LibreChat` :
   ```
   docker logs LibreChat
   docker logs api  # Ou docker logs librechat_api si le nom est différent
   docker logs rag_api  # En cas de problèmes de dépendance
   ```
   - Erreurs courantes : Permission denied (dû à UID/GID), échecs de connexion à MongoDB/Meilisearch, ou problèmes de liaison (par exemple, n'écoute pas sur 0.0.0.0).
   - Si les logs indiquent que le serveur démarre mais se lie uniquement à localhost à l'intérieur du conteneur, ajoutez `HOST=0.0.0.0` à votre fichier `.env`.

#### 3. **Définir UID et GID pour corriger les avertissements de permissions**
   Votre fichier `.env` (copié depuis `.env.example`) a probablement ces variables commentées. Des variables non définies peuvent entraîner l'échec silencieux des conteneurs en raison d'incohérences dans les permissions des fichiers.
   - Modifiez `.env` :
     ```
     UID=1000  # Exécutez `id -u` pour obtenir votre ID utilisateur
     GID=1000  # Exécutez `id -g` pour obtenir votre ID de groupe
     ```
   - Sauvegardez, puis redémarrez :
     ```
     docker compose down
     docker compose up -d
     ```
   Cela garantit que les volumes (comme config/logs) appartiennent à votre utilisateur.

#### 4. **Tester la connectivité**
   - Vérifiez si le port 3080 écoute localement :
     ```
     curl -v http://localhost:3080
     ```
     - Si la commande dépasse le délai ou si la connexion est refusée, le service ne fonctionne pas/n'est pas exposé.
   - Si `docker ps` montre le port mappé mais que curl échoue, vérifiez le pare-feu (par exemple, `sudo ufw status`) ou essayez `http://127.0.0.1:3080`.

#### 5. **Correctifs supplémentaires si nécessaire**
   - **Problèmes de téléchargement d'image** : Votre première tentative a généré une erreur "denied" pour `ghcr.io/v2/librechat/librechat/manifests/latest`. Si les téléchargements échouent à nouveau, authentifiez-vous auprès de GitHub Container Registry :
     ```
     echo $YOUR_GITHUB_TOKEN | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
     ```
     (Créez un token d'accès personnel sur github.com/settings/tokens avec la portée `read:packages`.)
   - **Utiliser le fichier Compose recommandé** : Le fichier `docker-compose.yml` par défaut est destiné aux builds locaux, qui peuvent être capricieux. Passez à `deploy-compose.yml` pour des images distantes stables :
     - Renommez ou sauvegardez votre `docker-compose.yml` actuel.
     - Utilisez `deploy-compose.yml` à la place : `docker compose -f deploy-compose.yml up -d`.
     - Assurez-vous que `.env` contient `HOST=0.0.0.0` et `NODE_ENV=production`.
   - **Redémarrage complet avec nettoyage** : Si vous êtes bloqué, nettoyez :
     ```
     docker compose down -v  # Supprime aussi les volumes
     docker system prune -f
     docker compose up -d
     ```
   - **Dépendances** : Confirmez que MongoDB et Meilisearch sont sains (`docker logs chat-mongodb`, etc.). Le service `api` en dépend.

Après ces étapes, réessayez d'accéder à http://localhost:3080. Si les logs affichent des erreurs spécifiques (par exemple, connexion Mongo), partagez-les pour obtenir une aide plus ciblée. Cette configuration fonctionne pour la plupart des utilisateurs une fois que UID/GID et les dépendances sont réglés.

[Local Docker Build Fails to Serve on localhost:3080](https://github.com/danny-avila/LibreChat/discussions/3425)  
[LibreChat Docker Docs](https://www.librechat.ai/docs/local/docker)  
[Env File Configuration (UID/GID)](https://www.librechat.ai/docs/configuration/dotenv)