---
audio: false
date: 2025-09-09
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Configuration de OPENAI_REVERSE_PROXY dans LibreChat
translated: true
type: note
---

Compris 👍 Vous modifiez le fichier `.env` de LibreChat.
Ce fichier est exactement l'endroit où vous définissez `OPENAI_REVERSE_PROXY`.

---

### 1. À quoi sert cette variable

`OPENAI_REVERSE_PROXY` est utilisée si vous souhaitez que LibreChat route les requêtes API OpenAI via un serveur proxy (par exemple, si vous exécutez un proxy inverse auto-hébergé pour ajouter de la journalisation, de la mise en cache, du routage régional, ou pour contourner des restrictions).

---

### 2. Comment la configurer

Dans votre fichier `.env`, assignez-lui simplement l'URL de base de votre proxy inverse. Par exemple :

```ini
OPENAI_REVERSE_PROXY=https://votre-proxy.exemple.com/v1
```

Notes :

* L'URL doit pointer vers votre endpoint proxy qui imite l'API `/v1` d'OpenAI.
* N'incluez pas de `/` final sauf si votre proxy l'exige.
* Laissez-la vide (`OPENAI_REVERSE_PROXY=`) si vous n'utilisez pas de proxy.

---

### 3. Appliquer les modifications

Après avoir modifié le fichier `.env`, redémarrez vos conteneurs LibreChat pour qu'ils prennent en compte la nouvelle valeur :

```bash
docker compose down
docker compose up -d --force-recreate
```

---

### 4. Vérifier

Vous pouvez vérifier à l'intérieur du conteneur en cours d'exécution :

```bash
docker compose exec librechat env | grep OPENAI_REVERSE_PROXY
```

La commande devrait afficher la valeur que vous avez définie.

---

Avez-vous déjà une URL de proxy inverse (comme `https://openrouter.ai/api/v1` ou votre propre instance Nginx), ou souhaitez-vous que je vous montre comment en **configurer un** pour LibreChat ?