---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Résolution du Problème de Proxy Hugging Face XetHub
translated: true
type: note
---

Vos logs montrent quelque chose de très important :

**La connexion qui échoue ne va *pas* directement vers HuggingFace.**
Elle va vers **[https://transfer.xethub.hf.co](https://transfer.xethub.hf.co)** — c'est le backend *XetHub* de Hugging Face (client Rust `reqwest`), que le proxy que vous avez configuré **n'intercepte PAS automatiquement**.

Cela explique tout :

* Vous avez déjà configuré `HTTP_PROXY` pour Python → ça fonctionne
* Mais XetHub utilise **rust reqwest**, pas Python requests
* Rust reqwest **ignore les variables de proxy système sauf si vous définissez les variables minuscules HTTPS_PROXY**, ou utilise une configuration de proxy explicite

Donc : **votre environnement Python utilise le proxy, mais XetHub (le nouveau fournisseur de stockage de HF) ne le fait PAS**.

C'est pourquoi vous voyez :

```
ConnectError("Connection refused")
```

et des tentatives de reconnexion.

---

# Pourquoi cela arrive (version courte)

Hugging Face a récemment migré son stockage vers **XetHub**, qui utilise un client Rust.
Ce client respecte :

* `https_proxy`
* `http_proxy`

mais **pas toujours** les versions majuscules selon la compilation.

Vous avez configuré les majuscules ? → Il peut les ignorer.

---

# Solution (fonctionne de manière fiable en Chine)

## 1. Définissez les variables de proxy en minuscules ET majuscules

Dans votre shell **avant d'exécuter NanoGPT** :

```bash
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"

export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

Rust reqwest préfère les minuscules
Python requests préfère les majuscules
Définir les deux évite les problèmes.

Puis exécutez :

```bash
python data/openwebtext_10k/prepare.py
```

Vous devriez voir une vitesse de téléchargement correcte immédiatement.

---

# 2. Important si votre proxy est SOCKS5

Rust reqwest **ne prend pas en charge socks5** sauf s'il est compilé avec des fonctionnalités optionnelles.
Donc si votre proxy est socks5:// → il échouera.

Vous devez basculer vers le port proxy HTTP de votre client, généralement :

* Clash : 7890 (HTTP)
* V2RayN : 10809 (HTTP)

Utilisez HTTP, pas SOCKS.

---

# 3. Comment tester si la partie Rust utilise le proxy

Testez via `curl`, **pas Python**, car curl se comporte de manière similaire à Rust pour les règles de proxy :

```bash
curl -I https://transfer.xethub.hf.co --proxy http://127.0.0.1:7890
```

Si cela fonctionne → les téléchargements Rust fonctionneront aussi.

Si cela échoue → votre proxy ne peut pas atteindre le domaine `xethub.hf.co`.

---

# 4. Si vous voulez forcer Hugging Face à éviter XetHub

Vous pouvez définir la variable d'environnement :

```bash
export HF_HUB_DISABLE_XETHUB=1
```

Cela force l'ancien backend S3 de HuggingFace au lieu de XetHub, beaucoup plus compatible avec les proxy.

Puis :

```bash
python data/openwebtext_10k/prepare.py
```

C'est la solution la plus stable.

---

# Solution recommandée (compatible Chine)

Pour la fiabilité :

```bash
export HF_HUB_DISABLE_XETHUB=1

export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"

python data/openwebtext_10k/prepare.py
```

---

Si vous voulez, je peux vous fournir :

* Un script bash en un clic (`hf_proxy_on.sh`)
* Une configuration de proxy permanente dans `.bashrc`
* Des instructions pour mirror complètement OpenWebText localement et éviter les téléchargements futurs

Dites-le-moi simplement.