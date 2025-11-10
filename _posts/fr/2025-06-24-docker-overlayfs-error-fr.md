---
audio: false
generated: true
image: false
lang: fr
layout: post
model: google/gemini-2.5-flash
title: Résolution de l'Erreur de Suppression OverlayFS de Docker
translated: true
type: note
---

L'erreur que vous voyez, spécifiquement la ligne :
`Error response from daemon: container ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18: driver "overlay2" failed to remove root filesystem: readdirnames /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f/merged: readdirent merged: bad message`
indique un **problème avec le pilote de stockage de Docker**, spécifiquement **OverlayFS (overlay2)**, qui est souvent lié à un état du système de fichiers corrompu sur votre machine hôte. Cela se produit généralement lorsque le démon Docker ne peut pas accéder ou nettoyer correctement les fichiers du conteneur.

Voici une approche étape par étape pour résoudre ce problème, en commençant par les méthodes les moins invasives.

-----

## 1. Arrêter et supprimer de force le conteneur

Le conteneur `chat-mongodb` n'a pas pu être supprimé. Vous devrez cibler ce conteneur spécifique.

### A. Essayer une suppression forcée

Tentez de supprimer le conteneur à nouveau, mais cette fois en utilisant l'option de force (`-f`) pour vous assurer qu'il n'est pas en cours d'exécution et pour tenter une suppression plus agressive :

```bash
docker rm -f chat-mongodb
```

ou utilisez l'ID du conteneur :

```bash
docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18
```

### B. Arrêter la pile Docker Compose

Si le conteneur fait partie d'une pile plus large que vous essayez de démanteler (ce que le `[+] Running 3/3` suggère), essayez d'abord d'arrêter les services proprement avant de tenter à nouveau la suppression :

```bash
docker compose stop
# Puis réessayez la commande originale
# par exemple, docker compose down
```

-----

## 2. Redémarrer le démon Docker

Un simple redémarrage du service Docker peut souvent résoudre les erreurs transitoires du pilote de stockage et les fichiers de verrouillage.

### Pour les systèmes Linux (utilisant systemd) :

```bash
sudo systemctl restart docker
```

### Pour Docker Desktop (macOS/Windows) :

1.  Cliquez sur l'icône **Docker** dans votre barre d'état système/barre des menus.
2.  Allez dans **Troubleshoot** (ou **Settings** $\rightarrow$ **Daemon** $\rightarrow$ **Restart**).
3.  Cliquez sur **Restart**.

Après le redémarrage, essayez à nouveau de supprimer le conteneur.

-----

## 3. Nettoyer manuellement le répertoire corrompu

**⚠️ AVERTISSEMENT :** Cette étape implique une manipulation directe de la structure de fichiers interne de Docker et ne doit être **effectuée qu'en dernier recours** et **lorsque le démon Docker est ARRÊTÉ**. Une suppression manuelle incorrecte peut entraîner une corruption supplémentaire.

L'erreur pointe vers un répertoire spécifique dans le stockage OverlayFS : `/var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f/merged`.

1.  **Arrêtez le démon Docker :**

    ```bash
    sudo systemctl stop docker
    ```

2.  **Supprimez manuellement le répertoire problématique :**

    ```bash
    # Ne supprimez que le répertoire indiqué dans VOTRE message d'erreur
    sudo rm -rf /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f
    ```

    *Si vous ne trouvez pas le répertoire exact, vous devrez peut-être essayer un nettoyage plus général (voir l'étape suivante).*

3.  **Démarrez le démon Docker :**

    ```bash
    sudo systemctl start docker
    ```

4.  **Essayez à nouveau de supprimer le conteneur/la pile.**

-----

## 4. Nettoyer les données inutilisées

Si les étapes ci-dessus échouent, vous pouvez utiliser les commandes de nettoyage intégrées de Docker. Cette commande supprime tous les conteneurs arrêtés, tous les réseaux non utilisés par au moins un conteneur, toutes les images dangling et tout le cache de build.

```bash
docker system prune
```

**Remarque :** Cette commande demandera une confirmation et supprimera les données que vous pourriez souhaiter conserver si elles ne sont pas activement utilisées (par exemple, les conteneurs arrêtés). Utilisez `-a` pour supprimer toutes les images inutilisées (pas seulement les dangling).