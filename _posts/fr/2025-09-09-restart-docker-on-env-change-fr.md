---
audio: false
date: 2025-09-09
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Redémarrage des conteneurs Docker après modification de l'environnement
translated: true
type: note
---

Lorsque vous modifiez le fichier `.env`, Docker ne recharge pas automatiquement ces variables d'environnement. Vous devez redémarrer les conteneurs pour qu'ils prennent en compte les nouvelles valeurs. Pour votre installation LibreChat, vous pouvez procéder comme suit :

1. Assurez-vous de vous trouver dans le même répertoire que votre fichier `docker-compose.yml`.
2. Exécutez :

```bash
docker compose down
docker compose up -d
```

Cela arrêtera et supprimera les conteneurs en cours d'exécution, puis les recréera avec les nouvelles valeurs du fichier `.env`.

---

### Alternative : redémarrage uniquement

Si vous ne souhaitez pas tout arrêter complètement, vous pouvez forcer les conteneurs à récupérer les nouvelles variables d'environnement en reconstruisant :

```bash
docker compose up -d --force-recreate
```

Ou si vous avez également modifié des Dockerfiles ou des dépendances, ajoutez `--build` :

```bash
docker compose up -d --build
```

---

✅ En résumé :

* Après avoir modifié le fichier `.env`, **recréez** toujours les conteneurs (`down` + `up` ou `up --force-recreate`).
* Un simple `docker compose restart` ne rechargera pas les nouvelles valeurs des variables d'environnement, il redémarre simplement avec les anciennes.

Souhaitez-vous également que je vous montre comment **vérifier** que vos conteneurs LibreChat utilisent les nouvelles valeurs des variables d'environnement (par exemple avec `docker inspect` ou `docker exec env`) ?