---
audio: false
date: 2025-09-14
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Désactivation des Contournements d'Authentification LibreChat
translated: true
type: note
---

Réponse courte : vous ne pouvez pas désactiver complètement l'authentification dans LibreChat, mais vous pouvez résoudre le problème de "demande incessante de connexion" et obtenir une expérience proche du "sans connexion". Voici ce qui fonctionne réellement (et pourquoi) :

### 1) Vous ne pouvez pas désactiver entièrement l'authentification

Ceci est confirmé par le mainteneur : l'enregistrement peut être désactivé, mais le système d'authentification lui-même ne peut pas être désactivé. ([GitHub][1])

### 2) Pourquoi vous êtes continuellement déconnecté

Si vous accédez à votre instance via **HTTP** (ex : adresse IP LAN), les cookies sont marqués `secure` en production donc le navigateur ne les conserve pas ; vous êtes renvoyé vers la page de connexion. Utilisez **HTTPS** (même auto-signé) ou exécutez l'API en mode développement qui désactive les cookies sécurisés. ([GitHub][1])

### 3) Deux correctifs fiables

#### Option A — Correct/sécurisé (recommandé)

* Placez LibreChat derrière HTTPS (nginx/caddy/traefik ; un certificat auto-signé convient sur un LAN).
* Ensuite, augmentez les durées de session dans votre `.env` :

  ```
  SESSION_EXPIRY=1000 * 60 * 60 * 24       # 24h
  REFRESH_TOKEN_EXPIRY=(1000 * 60 * 60 * 24) * 30  # 30j
  ```
* Redémarrez les conteneurs après avoir modifié le fichier env.
  Cela vous garde connecté pendant des jours/semaines et corrige la perte de cookie. ([GitHub][2])

#### Option B — « Je suis sur un LAN privé et je veux juste que les déconnexions s'arrêtent »

* Créez un `docker-compose.override.yml` et exécutez l'API en mode développement (désactive les cookies sécurisés) :

  ```yaml
  services:
    api:
      command: npm run backend:dev
  ```
* `docker compose up -d` pour appliquer.
  Ceci est moins sécurisé (cookies non `secure`), mais cela arrête la reconnexion forcée via HTTP simple. ([librechat.ai][3])

### 4) Ajustements optionnels pour améliorer l'expérience

* **Désactivez les nouvelles inscriptions** pour un usage effectivement mono-utilisateur :

  ```
  ALLOW_REGISTRATION=false
  ```

  (Vous pouvez toujours ajouter des utilisateurs via `npm run create-user` si nécessaire.) ([librechat.ai][4])
* Conservez les autres paramètres d'authentification dans `.env` (indicateurs de connexion par email/réseaux sociaux) si vous souhaitez le chemin de connexion le plus simple. ([librechat.ai][5])

### 5) Checklist rapide pour votre cas (v0.8.0-rc3)

1. Décidez : Proxy HTTPS (meilleur) **ou** mode développement (solution rapide pour LAN).
2. Définissez des valeurs plus longues pour `SESSION_EXPIRY` et `REFRESH_TOKEN_EXPIRY` dans `.env`.
3. Redémarrez la stack pour que les changements du fichier env prennent effet.
4. (Optionnel) Désactivez l'enregistrement pour une sensation "mono-utilisateur".

Si vous le souhaitez, collez votre `docker-compose.yml` et `.env` actuels (sans les secrets). Je marquerai exactement ce qu'il faut ajouter/modifier pour votre configuration.

[1]: https://github.com/danny-avila/LibreChat/discussions/572 "[Question]: Require login every time refresh · danny-avila LibreChat · Discussion #572 · GitHub"
[2]: https://github.com/danny-avila/LibreChat/discussions/2571?utm_source=chatgpt.com "Is there a way to increase or disable the auto-logoff time?"
[3]: https://www.librechat.ai/blog/2024-05-16_unsecured_http "GitHub"
[4]: https://www.librechat.ai/docs/configuration/authentication "GitHub"
[5]: https://www.librechat.ai/docs/configuration/dotenv "GitHub"