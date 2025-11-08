---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résumé des mises à jour de l'extension GitHub Copilot
translated: true
type: note
---

### Extension GitHub Copilot pour VS Code (Version 1.388.0)

La version 1.388.0 de l'extension GitHub Copilot a été publiée le 24 octobre 2025. Il s'agit d'une mise à jour mineure axée sur des améliorations de stabilité et de compatibilité, notamment avec la dernière version de VS Code (1.105). Les notes de publication spécifiques ne sont pas détaillées publiquement sur le marketplace ou le blog GitHub, mais des rapports d'utilisateurs indiquent des corrections pour des problèmes tels que des insertions de code non souhaitées lors de la génération en ligne et des complétions de balises supplémentaires lors de l'abandon de suggestions. Elle s'intègre parfaitement avec les fonctionnalités récentes de Copilot, y compris les modes agent améliorés et les sélections de modèles.

#### Principales mises à jour des 6 derniers mois (Mai–Octobre 2025)
Les améliorations majeures de GitHub Copilot sont généralement annoncées en parallèle des versions mensuelles de VS Code. Voici un résumé des mises à jour significatives pour l'extension et les fonctionnalités associées durant cette période :

- **Octobre 2025 (VS Code 1.105 / Extension ~1.388)** :
  - L'intégration OpenAI Codex est désormais disponible dans VS Code Insiders pour les abonnés Copilot Pro+, permettant une synthèse de code avancée directement dans l'éditeur.
  - Nouvelle interface "mission control" pour assigner, orienter et suivre les tâches de l'agent de codage Copilot entre les sessions.
  - La vue Sessions Agent a été étendue pour prendre en charge l'interface en ligne de commande (CLI) GitHub Copilot pour gérer les agents locaux et basés sur le cloud.

- **Septembre 2025 (VS Code 1.104 / Extension ~1.38x)** :
  - Déploiement du modèle expérimental GitHub Copilot-SWE dans VS Code Insiders, optimisé pour l'édition de code, le refactoring et les petites transformations. Il est axé sur les tâches et fonctionne dans n'importe quel mode Chat ; des instructions détaillées sont recommandées pour de meilleurs résultats.
  - Amélioration du chat en ligne pour les erreurs de terminal, avec de meilleures explications et corrections.

- **Août 2025 (VS Code 1.103 / Extension ~1.37x)** :
  - Amélioration des suggestions de message de commit avec une conscience contextuelle multi-lignes et une intégration avec @workspace pour générer des structures de projet entières.
  - Améliorations légères du chat en ligne pour des interactions plus rapides sans ouvrir de vues complètes.

- **Juillet 2025 (VS Code 1.102 / Extension ~1.36x)** :
  - Meilleure coordination des modifications multi-fichiers via des instructions uniques, analysant la structure du projet pour des changements cohérents.
  - Dépréciation des anciens modèles (certaines variantes de Claude, OpenAI et Gemini) au profit d'options plus récentes et plus rapides comme GPT-4.1.

- **Juin 2025 (VS Code 1.101 / Extension ~1.35x)** :
  - Introduction de fichiers d'instructions et de prompts pour personnaliser le comportement de Copilot avec des directives réutilisables et des connaissances organisationnelles.
  - Extension de l'intégration GitHub Pull Requests : Assignez des PRs/issues à Copilot directement depuis les vues VS Code, avec une nouvelle requête "Copilot on My Behalf" pour le suivi.

- **Mai 2025 (VS Code 1.100 / Extension ~1.34x)** :
  - Ajout de la prise en charge du Model Context Protocol (MCP) au mode agent, permettant l'utilisation de clés API personnalisées pour des modèles tiers.
  - Modifications d'agent plus rapides grâce à OpenAI GPT-4.1 et Anthropic Claude Sonnet, en particulier pour les gros fichiers.
  - Améliorations de la recherche dans le dépôt pour la découverte sémantique de code et les suggestions à l'échelle de la base de code.

Ces mises à jour mettent l'accent sur les workflows agentiques, les performances des modèles et l'intégration transparente avec l'écosystème de VS Code. Pour l'historique complet de l'extension, consultez le VS Code Marketplace. Les annonces majeures sont souvent liées aux cycles mensuels de VS Code.

[GitHub Copilot in VS Code gets upgraded](https://github.blog/changelog/2025-10-28-github-copilot-in-visual-studio-code-gets-upgraded/)  
[Copilot-SWE model rolling out to Visual Studio Code Insiders](https://github.blog/changelog/2025-09-22-copilot-swe-model-rolling-out-to-visual-studio-code-insiders/)  
[GitHub Copilot in VS Code April release (v1.100)](https://github.blog/changelog/2025-05-08-github-copilot-in-vs-code-april-release-v1-100/)  
[GitHub Copilot in VS Code March release (v1.99)](https://github.blog/changelog/2025-04-03-github-copilot-in-vs-code-march-release-v1-99/)  
[September 2025 (version 1.105) - Visual Studio Code](https://code.visualstudio.com/updates)  
[GitHub Copilot Marketplace Page](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)