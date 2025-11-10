---
audio: false
generated: true
image: false
lang: fr
layout: post
model: google/gemini-2.5-flash
title: Comment réparer la corruption OverlayFS de Docker sur macOS
translated: true
type: note
---

L'erreur que vous voyez, `driver "overlay2" failed to remove root filesystem: readdirnames /var/lib/docker/overlay2/.../merged: readdirent merged: bad message`, indique une corruption profonde du mécanisme de stockage de Docker (OverlayFS) souvent causée par une opération interrompue ou un problème du système de fichiers de la machine hôte.

Étant donné que vous êtes sur **macOS** (qui exécute Docker Desktop), le démon Docker et son stockage sont gérés dans une **Machine Virtuelle (VM) Linux** dédiée. Vous n'avez pas d'accès direct à `/var/lib/docker/overlay2` comme vous le feriez sur un Linux natif, ce qui rend la correction plus simple et plus sûre en se concentrant sur l'application Docker Desktop elle-même.

Voici la séquence d'étapes la plus sûre et la plus efficace pour résoudre ce problème sur macOS :

-----

## 1. Arrêter de force et Supprimer de force le Conteneur

Le conteneur qui a échoué est `chat-mongodb` (ID : `ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18`). Tout d'abord, essayez une suppression forcée en utilisant son nom ou son ID.

1.  **Arrêtez l'ensemble de la stack** (pour s'assurer qu'aucun processus en arrière-plan ne maintient un verrou) :

    ```bash
    docker compose stop
    ```

2.  **Supprimez de force le conteneur spécifique** en utilisant l'option `-f` :

    ```bash
    docker rm -f chat-mongodb
    # OU en utilisant l'ID :
    # docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18
    ```

3.  **Essayez de relancer votre commande d'origine** (`docker compose down` ou équivalent). Si l'erreur persiste, passez à l'étape 2.

-----

## 2. Redémarrer Docker Desktop

Un simple redémarrage efface souvent les problèmes de verrous transitoires ou les états corrompus au sein de la VM interne.

### Option A : Utilisation de la Barre des Menus (Recommandée)

1.  Cliquez sur l'icône **Docker Whale** dans la barre des menus de votre macOS.
2.  Sélectionnez **Restart**.

### Option B : Utilisation du Terminal

Vous pouvez forcer la fermeture et rouvrir l'application :

```bash
killall Docker && open /Applications/Docker.app
```

Après le redémarrage de Docker, attendez environ 30 secondes qu'il soit complètement démarré, puis essayez de relancer votre commande d'origine.

-----

## 3. Vider le Cache et les Données Inutilisées de Docker (Prune)

Si le redémarrage échoue, une commande de nettoyage puissante peut souvent résoudre les problèmes de corruption plus profonds en supprimant les composants inutilisés ou "dangling" qui pourraient être liés à l'erreur.

**AVERTISSEMENT :** Cette commande supprime tous les conteneurs arrêtés, les réseaux inutilisés et les images dangling. Si vous avez des conteneurs arrêtés que vous souhaitez conserver (sans les supprimer), sauvegardez-les ou ignorez cette étape.

Exécutez la commande suivante dans votre terminal :

```bash
docker system prune -a --volumes
```

  * **`-a`** (all) supprime toutes les images non utilisées (pas seulement les dangling).
  * **`--volumes`** supprime les volumes anonymes non utilisés (qui pourraient être la source de la corruption `overlay2`).

Il vous sera demandé de confirmer. Tapez `y` et appuyez sur Entrée. Une fois le nettoyage terminé, essayez de relancer votre commande d'origine.

-----

## 4. Réinitialiser Docker Desktop aux Paramètres d'Usine

C'est la **dernière solution** car elle **supprimera tous vos conteneurs, images et volumes** (y compris toutes les données locales que vous avez stockées dans des volumes non montés). Elle force un redémarrage complètement propre de la VM Docker interne.

1.  Cliquez sur l'icône **Docker Whale** dans la barre des menus de votre macOS.
2.  Allez dans **Settings (ou Preferences)** $\rightarrow$ **Troubleshoot**.
3.  Cliquez sur **Reset to factory settings...**

Après la réinitialisation, Docker redémarrera avec un état vierge, et vous devriez pouvoir exécuter votre commande `docker compose up` pour reconstruire votre environnement.