---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Résoudre les erreurs de suppression d'Overlay2 Docker
translated: true
type: note
---

Cette erreur signifie que Docker n'a pas réussi à supprimer le système de fichiers overlay2 du conteneur — le noyau/la VM a renvoyé une erreur d'E/S de bas niveau (`readdirent merged: bad message`). Sur macOS, cela se produit généralement lorsque la VM Docker ou le stockage overlay est dans un état défectueux. Voici des étapes sûres et ordonnées (du moins destructeur → plus agressif) que vous pouvez essayer pour récupérer.

**Important :** certaines commandes ci-dessous peuvent supprimer des données (images/volumes). Je marquerai les étapes destructrices et montrerai les commandes exactes afin que vous puissiez les copier/coller si vous le souhaitez.

---

# Vérifications rapides (sûr)

Dans un terminal, exécutez :

```bash
# afficher l'état du conteneur et l'id du conteneur problématique
docker ps -a --no-trunc | grep ccd89a3f36a1528cb923c90de8755faeb36e229c || true

# essayer une suppression forcée du conteneur
docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229c
```

Si `docker rm -f` réussit, vous avez terminé. Si cela échoue avec la même erreur overlay, continuez.

---

# Redémarrer Docker (Docker Desktop macOS) — étape suivante recommandée (sûr)

Quittez Docker Desktop complètement (utilisez l'icône de la baleine → Quitter) puis redémarrez-le. Ou depuis la ligne de commande :

```bash
# macOS — redémarrer Docker Desktop via AppleScript
osascript -e 'quit app "Docker"'
open -a Docker
```

Après le redémarrage de Docker, réessayez `docker compose down` ou `docker rm -f <id>`.

---

# Redémarrer l'hôte (très sûr)

Si un redémarrage est possible, redémarrer macOS résout souvent les problèmes de système de fichiers de la VM :

* Redémarrez le Mac, puis démarrez Docker Desktop et réessayez.

---

# Si l'échec persiste — utilisez les actions de dépannage de Docker Desktop (sûr / moyen)

Ouvrez Docker Desktop → Dépannage :

* Cliquez sur **Redémarrer Docker** (si vous ne l'avez pas déjà fait).
* Si cela échoue, essayez **Nettoyer / Purger les données** ou **Réinitialiser aux paramètres d'usine** — **avertissement :** cela supprime les images/conteneurs/volumes. À utiliser uniquement si vous pouvez vous permettre de perdre les données Docker locales.

---

# Si vous êtes sur Docker Engine (Linux) ou à l'aise avec un nettoyage manuel (destructeur)

**Ne faites ceci que si vous comprenez le risque de perte de données.**