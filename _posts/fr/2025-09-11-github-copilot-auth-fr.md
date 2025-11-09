---
audio: false
date: 2025-09-11
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Flux d'Authentification GitHub Copilot
translated: true
type: note
---

Bonne question — le flux d'authentification de GitHub Copilot est essentiellement une **autorisation par code d'appareil OAuth2** standard, mais avec quelques jetons spécifiques à GitHub ajoutés par-dessus pour le service Copilot lui-même. Laissez-moi décomposer cela étape par étape :

---

### 1. **Flux de l'appareil (`/login/device/code`)**

* Lorsque vous vous connectez pour la première fois, le client Copilot (par exemple, l'extension VS Code, le plugin JetBrains ou le CLI) appelle le point de terminaison OAuth de GitHub :

  ```
  POST https://github.com/login/device/code
  ```
* Il envoie le **client\_id** (spécifique à GitHub Copilot).
* GitHub répond avec :

  * `device_code` (code interne utilisé pour l'interrogation),
  * `user_code` (celui que vous voyez et entrez dans votre navigateur),
  * `verification_uri` (l'URL que vous visitez pour entrer le code),
  * `interval` (la fréquence à laquelle le client doit interroger).

---

### 2. **Interrogation pour le jeton d'accès**

* Le client Copilot interroge ensuite :

  ```
  POST https://github.com/login/oauth/access_token
  ```
* Il inclut le `device_code` et le `client_id`.
* Une fois que vous avez approuvé dans votre navigateur, GitHub renvoie :

  * `access_token` (un **jeton OAuth GitHub** avec une portée pour l'utilisation de Copilot),
  * `token_type=bearer`,
  * `expires_in` (durée de vie).

Ce `access_token` est un **jeton OAuth2 GitHub normal**.

---

### 3. **Échange contre un jeton `copilot_internal`**

* Le client Copilot ne peut pas appeler les APIs Copilot directement avec le jeton OAuth GitHub.
* Au lieu de cela, il l'échange avec le service Copilot :

  ```
  POST https://api.github.com/copilot_internal/v2/token
  Authorization: Bearer <GitHub OAuth access_token>
  ```
* La réponse est :

  ```json
  {
    "token": "<jeton copilot_internal>",
    "expires_at": "...",
    "user": { ... }
  }
  ```
* Ce **jeton `copilot_internal` v2** est ce que le client Copilot utilise pour communiquer avec le **service d'inférence Copilot** (par exemple, `https://copilot-proxy.githubusercontent.com`).

---

### 4. **Utilisation du jeton `copilot_internal`**

* Toutes les requêtes ultérieures de complétion ou de chat sont authentifiées avec :

  ```
  Authorization: Bearer <jeton copilot_internal>
  ```
* Ce jeton a une courte durée de vie (généralement \~1 heure) et est lié à votre compte GitHub et au statut de votre abonnement Copilot.
* Le client le rafraîchit périodiquement en rééchangeant le jeton d'accès OAuth GitHub.

---

✅ **En résumé :**

* `/login/device/code` → vous donne un code pour vous authentifier dans le navigateur.
* `/login/oauth/access_token` → vous donne un jeton OAuth GitHub.
* `/copilot_internal/v2/token` → échange cela contre un jeton Copilot à courte durée de vie, qui est la *vraie* credential utilisée pour les complétions.

---

Souhaitez-vous que je décrive également les **exemples exacts de requêtes/réponses** (avec les en-têtes et un exemple de JSON) afin que vous puissiez voir à quoi ressemblent les payloads en pratique ?