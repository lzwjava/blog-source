---
audio: false
date: 2025-09-13
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Derniers Modèles d'IA et Leurs Applications
translated: true
type: note
---

Voici un résumé de ce que nous *savons* (à partir de mi-septembre 2025) sur le GPT-5, Gemini 2.5 Pro, le GPT-5 mini, et comment ils sont utilisés, y compris dans Copilot / les modèles premium :

---

## GPT-5 (OpenAI)

* **Date de sortie** : 7 août 2025. ([OpenAI][1])
* **Description** : Un LLM unifié avec un raisonnement amélioré, moins d'hallucinations, de meilleures performances en programmation, en mathématiques, en rédaction, en santé, en perception visuelle, etc. Il inclut une version « GPT-5 pro » pour les tâches plus exigeantes. ([OpenAI][1])
* **Raisonnement / réflexion** : GPT-5 possède un mécanisme interne (« rapide » vs « raisonnement approfondi ») et les utilisateurs peuvent sélectionner « GPT-5 thinking » ou utiliser des invites comme « réfléchis bien à ceci » pour demander un raisonnement plus approfondi. ([OpenAI][1])
* **Niveaux d'accès / limitations** :

  * Tous les utilisateurs de ChatGPT y ont accès (gratuit et payant). ([OpenAI][1])
  * Les utilisateurs gratuits ont un usage plus limité, et après un certain seuil, ils peuvent être basculés vers une version plus légère (« GPT-5 mini »). ([OpenAI][1])
  * Les utilisateurs payants (Plus, Pro, Team, Enterprise, EDU) bénéficient de limites d'utilisation plus élevées ; les utilisateurs Pro obtiennent le « GPT-5 pro ». ([OpenAI][1])

---

## Gemini 2.5 Pro (Google)

* **Sortie / disponibilité** :

  * Gemini 2.5 Pro (expérimental) a été annoncé pour la première fois le 25 mars 2025. ([blog.google][2])
  * La version stable (« disponibilité générale ») de Gemini 2.5 Pro est sortie le 17 juin 2025. ([Google Cloud][3])
* **Capacités** : C'est le modèle le plus avancé de la famille Gemini 2.5 de Google. Il dispose notamment d'une grande fenêtre de contexte (1 million de tokens), d'un raisonnement solide, de capacités en programmation, de support multilingue, etc. ([blog.google][2])

---

## GPT-5 mini

* **Description / date** : GPT-5 mini est une version plus légère/rapide du GPT-5 qui est devenue disponible dans GitHub Copilot (préversion publique) à la mi-août 2025. ([The GitHub Blog][4])
* **Où et comment** : Il est disponible dans GitHub Copilot Chat (sur github.com), dans VS Code, sur GitHub Mobile (iOS/Android). Il apparaîtra également dans le sélecteur de modèles pour les utilisateurs. ([The GitHub Blog][4])
* **Requêtes premium / coût** : Il ne consomme *pas* les « requêtes premium » dans les forfaits payants de GitHub Copilot. Autrement dit, utiliser GPT-5 mini n'utilise pas le quota de « requêtes premium ». ([The GitHub Blog][4])

---

## Comment ils sont utilisés dans **Copilot / Premium / Microsoft / GitHub**

* **GitHub Copilot** :

  * Tous les forfaits Copilot (y compris Gratuit) ont maintenant accès à GPT-5 mini. ([The GitHub Blog][4])
  * Le GPT-5 (version complète) n'est disponible que sur les forfaits Copilot payants. ([The GitHub Blog][5])
  * Le sélecteur de modèles permet aux utilisateurs de choisir entre GPT-5, GPT-5 mini, etc., selon leur forfait et les paramètres de leur organisation. ([The GitHub Blog][4])

* **Microsoft Copilot / Copilot Studio / 365 Copilot** :

  * Microsoft prend en charge l'utilisation de GPT-5 dans ses produits Copilot. Par exemple, les créateurs utilisant Copilot Studio peuvent sélectionner GPT-5, et il existe un routage automatique entre les différentes variantes de GPT-5 (chat vs raisonnement), etc. ([Microsoft Developer][6])
  * Les fonctionnalités premium nécessitent généralement des abonnements payants. L'utilisation de GPT-5, ou des modèles à plus grande capacité, ou ceux avec plus de raisonnement, sont souvent restreints aux utilisateurs payants ou aux niveaux entreprise. ([OpenAI][1])

---

Si vous le souhaitez, je peux également me pencher sur les **comparaisons de performances** (GPT-5 vs Gemini 2.5 Pro, etc.), ou sur les **fonctionnalités futures/annoncées**. Voulez-vous cela ?

[1]: https://openai.com/index/introducing-gpt-5/?utm_source=chatgpt.com "Introducing GPT-5"
[2]: https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/?utm_source=chatgpt.com "Gemini 2.5: Our most intelligent AI model"
[3]: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions?utm_source=chatgpt.com "Model versions and lifecycle | Generative AI on Vertex AI"
[4]: https://github.blog/changelog/2025-08-13-gpt-5-mini-now-available-in-github-copilot-in-public-preview/?utm_source=chatgpt.com "GPT-5 mini now available in GitHub Copilot in public preview"
[5]: https://github.blog/changelog/2025-09-09-openai-gpt-5-and-gpt-5-mini-are-now-generally-available-in-github-copilot/?utm_source=chatgpt.com "OpenAI GPT-5 and GPT-5 mini are now generally available ..."
[6]: https://developer.microsoft.com/blog/gpt-5-for-microsoft-developers?utm_source=chatgpt.com "GPT-5 for Microsoft Developers"