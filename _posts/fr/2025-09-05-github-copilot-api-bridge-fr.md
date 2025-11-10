---
audio: false
generated: true
image: false
lang: fr
layout: post
title: GitHub Copilot Pont API
translated: true
type: note
---

Vous êtes arrivé sur **ericc-ch/copilot-api**, un projet GitHub qui transforme **GitHub Copilot** en un serveur API local compatible avec les API **OpenAI** et **Anthropic** (par exemple, Claude).

Voici une explication plus claire — pas de tableaux, juste des faits :

---

### Qu'est-ce que c'est ?

* C'est un **proxy rétro-conçu** qui vous permet d'interagir avec GitHub Copilot en utilisant des endpoints familiers de type OpenAI comme `/v1/chat/completions`, `/v1/models` et `/v1/embeddings`. Vous pouvez également utiliser des endpoints compatibles Anthropic tels que `/v1/messages` ([GitHub][1]).

* Essentiellement, cela permet à des outils qui prennent en charge les API OpenAI ou Anthropic — comme Claude Code — d'utiliser GitHub Copilot comme backend ([GitHub][1]).

---

### Fonctionnalités principales

* **Compatibilité OpenAI & Anthropic** : Fonctionne comme la véritable API OpenAI ou Anthropic ([GitHub][1]).
* **Intégration Claude Code** : Prêt à être branché à Claude Code avec un flag `--claude-code` ([GitHub][1]).
* **Tableau de bord d'utilisation** : Surveillez votre utilisation de l'API Copilot et vos quotas via une interface web intégrée ([GitHub][1]).
* **Contrôles de limitation de débit et d'approbation** : Inclut des options pour la limitation de débit (`--rate-limit`), l'attente automatique (`--wait`), l'approbation manuelle (`--manual`) et le débogage (affichage des tokens) — excellent pour éviter les systèmes d'abus de GitHub ([GitHub][1]).
* **Prend en charge divers forfaits Copilot** : Les comptes individuels, professionnels ou entreprise fonctionnent tous ([GitHub][1]).

---

### Installation et utilisation

* **Prérequis** : Vous aurez besoin de Bun (≥ 1.2.x) et d'un abonnement GitHub Copilot ([GitHub][1]).
* **Options d'installation** :

  * **Docker** :

    ```bash
    docker build -t copilot-api .
    docker run -p 4141:4141 -v $(pwd)/copilot-data:/root/.local/share/copilot-api copilot-api
    ```

    Ou passez votre token GitHub directement via `GH_TOKEN` ([GitHub][1]).
  * **npx** :

    ```bash
    npx copilot-api@latest start --port 8080
    ```

    Ou `npx copilot-api@latest auth` juste pour l'authentification ([GitHub][1]).
* **Structure des commandes** :

  * `start` : Lance le serveur API (gère l'authentification si nécessaire).
  * `auth` : Déclenche la connexion GitHub sans exécuter le serveur.
  * `check-usage` : Affiche l'utilisation actuelle de Copilot dans votre terminal.
  * `debug` : Affiche les informations de diagnostic (versions, statut d'authentification, etc.), avec une sortie `--json` optionnelle ([GitHub][1]).

---

### Retours d'expérience

Des utilisateurs de Reddit ont donné leur avis :

> "Ce projet vous permet de transformer copilot en un endpoint compatible openai." ([Reddit][2])
> "C'est un projet génial pour créer votre …" ([Reddit][3])

---

 Mises en garde importantes

* **Non officiel et non supporté** : Ceci n'est **pas** un produit officiel GitHub et pourrait cesser de fonctionner à tout moment ([GitHub][1]).
* **Risque de détection d'abus** : Une utilisation intensive ou automatisée pourrait déclencher la protection contre les abus de GitHub et suspendre votre accès à Copilot ([GitHub][1]).
* **Problèmes potentiels de limitation de débit** : Certains utilisateurs ont signalé des erreurs comme `421 Misdirected Request`, et le mainteneur a mis en pause le développement pendant l'enquête ([GitHub][4]).

---

### Résumé (Pas besoin de tableaux)

* **Ce que ça fait** : Expose GitHub Copilot comme s'il s'agissait d'une API OpenAI/Anthropic.
* **Pourquoi c'est important** : Rend Copilot utilisable dans des outils attendant ces API — comme Claude Code.
* **Comment l'utiliser** : Installez via Docker ou npx ; exécutez les commandes pour démarrer, vous authentifier ou surveiller l'utilisation.
* **Procédez avec prudence** : C'est pratique, mais non officiel, et les limites de débit ou les protections de sécurité de GitHub peuvent entraver une utilisation intensive.

---

Faites-moi savoir si vous avez besoin d'aide pour le configurer, ou si vous êtes curieux de l'intégrer dans un projet ou un outil spécifique !

[1]: https://github.com/ericc-ch/copilot-api?utm_source=chatgpt.com "ericc-ch/copilot-api"
[2]: https://www.reddit.com/r/ChatGPTCoding/comments/1m6cqac/how_to_use_your_github_copilot_subscription_with/?utm_source=chatgpt.com "How to use your GitHub Copilot subscription with Claude ..."
[3]: https://www.reddit.com/r/ClaudeAI/comments/1lc21gk/using_github_copilot_as_a_provider_for_claude_code/?utm_source=chatgpt.com "Using GitHub Copilot as a provider for Claude Code"
[4]: https://github.com/ericc-ch/copilot-api/issues/7?utm_source=chatgpt.com "Issue #7 · ericc-ch/copilot-api - 421 Misdirected Request"