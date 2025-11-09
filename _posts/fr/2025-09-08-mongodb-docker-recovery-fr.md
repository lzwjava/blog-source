---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Guide de Récupération de Conteneur Docker MongoDB
translated: true
type: note
---

Merci — la sortie de `docker inspect` confirme que le conteneur est **Dead** et que votre répertoire de données MongoDB est un montage par liaison hôte :
`/Users/lzwjava/projects/LibreChat/data-node:/data/db:rw`.
C'est une bonne nouvelle — vos *fichiers de données MongoDB sont sur votre hôte macOS*, donc ils peuvent être sauvegardés avant que nous procédions à tout nettoyage destructif côté Docker.

Voici deux approches sûres. **L'approche A (recommandée)** conserve vos données et est plus simple : sauvegardez le répertoire de données de l'hôte, puis utilisez Docker Desktop → Dépannage → Nettoyer / Purger. **L'approche B (avancée / dernier recours)** consiste en une suppression de bas niveau de l'état de la machine virtuelle Docker. Je vais donner les commandes exactes pour que vous puissiez les copier/coller.

---

# Approche A — recommandée (sauvegarde des données de l'hôte, puis réinitialisation via Docker Desktop)

1. Confirmez que le répertoire de données de l'hôte existe et listez son contenu :

```bash
ls -la /Users/lzwjava/projects/LibreChat/data-node
```

2. Créez une sauvegarde tar de ce répertoire (cela préserve vos fichiers MongoDB) :

```bash
mkdir -p ~/docker-backups/librechat
tar -czvf ~/docker-backups/librechat/data-node-backup-$(date +%Y%m%dT%H%M%S).tgz -C /Users/lzwjava/projects/LibreChat data-node
# résultat : ~/docker-backups/librechat/data-node-backup-YYYYMMDDTHHMMSS.tgz
```

(Vous pouvez aussi copier le dossier au lieu d'utiliser tar si vous préférez `cp -a /Users/lzwjava/projects/LibreChat/data-node ~/docker-backups/librechat/data-node-copy`.)

3. Quittez Docker Desktop complètement :

```bash
osascript -e 'quit app "Docker"'
```

4. Ouvrez Docker Desktop → Dépannage (ou Préférences → Dépannage) → cliquez sur **Clean / Purge data** (ou **Reset to factory defaults** si l'option Clean n'est pas présente).

   * **Important** : Cela supprime les images Docker, les conteneurs et les volumes qui se trouvent dans la machine virtuelle Docker, mais cela **ne** supprimera **pas** les fichiers qui sont montés par liaison depuis votre hôte macOS (votre sauvegarde `/Users/.../data-node` garantit que vous êtes en sécurité).

5. Après la réinitialisation de Docker, redémarrez Docker Desktop, vérifiez que Docker fonctionne, puis relancez votre stack Compose :

```bash
open -a Docker
# attendez que Docker soit opérationnel
docker compose up -d
```

6. Vérifiez le conteneur Mongo et les données :

```bash
docker ps -a
# docker logs <new-mongo-container-id>  (si nécessaire)
```

Si quelque chose dans les étapes 5/6 semble incorrect, restaurez la sauvegarde : arrêtez tout conteneur mongo en cours d'exécution, déplacez ou supprimez le dossier data-node recréé et extrayez la sauvegarde dans `/Users/lzwjava/projects/LibreChat/data-node`.

---

# Approche B — avancée / dernier recours (suppression manuelle des fichiers de la machine virtuelle Docker Desktop)

À utiliser uniquement si vous *ne pouvez pas* utiliser l'interface de Nettoyage/Purge de Docker Desktop ou si cela n'a pas résolu le problème et que vous acceptez de perdre l'état interne de Docker.

1. Quittez Docker Desktop :

```bash
osascript -e 'quit app "Docker"'
```

2. Sauvegardez la configuration utilisateur de Docker Desktop (optionnel) :

```bash
cp -a ~/Library/Containers/com.docker.docker ~/Library/Containers/com.docker.docker.backup-$(date +%Y%m%dT%H%M%S)
```

3. Supprimez l'état interne de Docker Desktop (DESTRUCTIF — supprime les conteneurs/images à l'intérieur de la machine virtuelle Desktop) :

```bash
rm -rf ~/Library/Containers/com.docker.docker
rm -rf ~/.docker
```

4. Redémarrez Docker Desktop :

```bash
open -a Docker
```

5. Recréez votre stack :

```bash
docker compose up -d
```

Encore une fois — vos données Mongo montées par liaison hôte resteront intactes car elles résident dans `/Users/...` à moins que vous ne les supprimiez manuellement.

---

# Vérifications supplémentaires / commandes que vous pouvez coller ici si vous voulez que je les vérifie avant la réinitialisation

(Ces commandes sont non destructives.)

```bash
# montre que les données existent sur l'hôte
ls -la /Users/lzwjava/projects/LibreChat/data-node

# montre les images et les volumes pour planifier les sauvegardes
docker images
docker volume ls

# info docker & ps pour un diagnostic rapide
docker info
docker ps -a
```

Si vous collez la sortie `ls -la` pour le dossier `data-node`, je confirmerai que la sauvegarde semble saine. Si vous préférez, procédez avec l'Approche A : sauvegardez (étape 2) puis exécutez Docker Desktop → Dépannage → Clean / Purge — c'est la solution la plus propre et elle résout généralement l'erreur de suppression `overlay2` bloquée tout en gardant vos fichiers Mongo en sécurité.