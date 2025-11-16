---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Configuration du proxy Hugging Face XetHub
translated: true
type: note
---

Oui — **Rust reqwest prend absolument en charge une configuration explicite du proxy**, et le client XetHub de Hugging Face (écrit en Rust) le permet également.
MAIS : Hugging Face ne **expose pas** d'API Python pour vous permettre de transmettre directement les paramètres de proxy.
À la place, XetHub s'appuie sur des **variables d'environnement** que reqwest lit automatiquement.

Voici à quoi ressemble la configuration explicite du proxy pour reqwest :

---

# ✔ Comment reqwest détecte les proxies (officiel)

Reqwest utilise automatiquement les **variables d'environnement** suivantes :

* `https_proxy`
* `http_proxy`
* `all_proxy`

La minuscule est importante.
Reqwest **ignore** les variables en majuscules (`HTTPS_PROXY`) sauf si un certain flag de fonctionnalité est activé au moment de la compilation.

**Hugging Face XetHub utilise le reqwest par défaut → minuscules uniquement.**

Cela signifie :

```
export https_proxy="http://127.0.0.1:7890"
export http_proxy="http://127.0.0.1:7890"
```

est la seule configuration de proxy explicite garantie de fonctionner avec XetHub.

---

# ✔ Comment HuggingFace XetHub charge la configuration du proxy

Lorsque Python exécute `load_dataset`, il déclenche un binaire Rust qui :

1. Recherche les variables d'environnement de proxy en minuscules
2. Réécrit les URLs
3. Ouvre les connexions via reqwest
4. Télécharge des morceaux de fichiers depuis `https://transfer.xethub.hf.co`

Si ces variables d'environnement ne sont pas définies, ou accessibles → connexion refusée.

---

# ✔ Forcer manuellement reqwest à utiliser un proxy (code de référence)

Juste pour montrer ce que reqwest ferait en interne :

```rust
let proxy = reqwest::Proxy::https("http://127.0.0.1:7890")?;
let client = reqwest::Client::builder()
    .proxy(proxy)
    .build()?;
```

Le client XetHub de Hugging Face *fait quelque chose d'équivalent*, mais déclenché par les variables d'environnement.

---

# ✔ Configuration de proxy explicite complète qui fonctionne toujours avec reqwest (compatible HF)

Exécutez **toutes** ces commandes :

```bash
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
export all_proxy="http://127.0.0.1:7890"
```

Utilisez un proxy `http`, pas `socks5`, car :

* Le support socks de reqwest est optionnel
* Le binaire client XetHub n'a pas été compilé avec pour HF

Donc socks peut échouer silencieusement.

---

# ✔ Vérifier que votre proxy est utilisé

Essayez :

```bash
env | grep proxy
```

Si vous voyez des minuscules → bon.

Puis :

```bash
curl -I https://transfer.xethub.hf.co --proxy http://127.0.0.1:7890
```

Si curl réussit → reqwest réussira.

---

# Résumé

* Les datasets Hugging Face sont parfois téléchargés via **XetHub** (client Rust reqwest)
* Reqwest ne respecte par défaut que les variables de proxy en **minuscules**
* Vous devez les définir explicitement
* Utilisez un proxy **HTTP**, pas SOCKS
* `HF_HUB_DISABLE_XETHUB=1` peut contourner complètement reqwest si nécessaire

---

Si vous voulez, je peux préparer un :

* script "correctif proxy HF" en une commande
* configuration persistante pour votre `.bashrc`
* script de auto-détection pour confirmer si reqwest utilise le proxy

Dites-le-moi simplement.