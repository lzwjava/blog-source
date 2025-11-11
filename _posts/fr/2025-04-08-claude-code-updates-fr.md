---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Mises à Jour Majeures de Claude Code
translated: true
type: note
---

### Principales mises à jour de Claude Code

Claude Code, l'assistant de codage alimenté par l'IA d'Anthropic, a connu des améliorations significatives récemment, notamment autour de l'autonomie, de l'intégration et des fonctionnalités de l'interface utilisateur. D'après les dernières actualités (29 septembre 2025), la mise à jour clé se concentre sur l'activation d'un fonctionnement plus autonome, incluant une extension native pour VS Code, une interface de terminal améliorée (version 2.0) et une nouvelle fonctionnalité de points de contrôle pour gérer les tâches de longue durée. De plus, des fonctionnalités comme la possibilité d'activer/désactiver le mode "réflexion" semblent faire partie des améliorations en cours, permettant aux utilisateurs d'afficher ou de masquer les étapes de raisonnement de Claude pour des interactions plus épurées [1].

#### Autonomie et capacités d'agent
- **Extension native VS Code** : Permet une intégration transparente avec l'éditeur VS Code, permettant à Claude Code de fonctionner directement dans l'environnement de développement pour une édition et un débogage de code plus autonomes.
- **Interface de terminal v2.0** : Les améliorations incluent une meilleure gestion des permissions, de la gestion de la mémoire entre les tâches et de la coordination des sous-agents. Cela rend Claude Code plus performant pour équilibrer le contrôle de l'utilisateur avec les opérations automatisées lors de flux de travail complexes [1][2].
- **Points de contrôle** : Une nouvelle fonctionnalité pour sauvegarder la progression dans les tâches longues, permettant des pauses et des reprises sans perte de contexte. Cela permet d'exécuter des tâches s'étalant sur plusieurs jours ou sessions.

Ces changements s'appuient sur le SDK Claude Agent d'Anthropic, fournissant aux développeurs des outils pour créer des agents IA personnalisés qui reflètent l'infrastructure interne de Claude Code [2].

#### Autres changements notables
- **Intégration de la mise à niveau du modèle** : Claude Code utilise maintenant Claude Sonnet 4.5 par défaut, offrant des performances améliorées dans les tâches de codage sans changement de prix. Ce modèle est recommandé pour tous les produits Claude pour son alignement amélioré et ses hallucinations réduites [2].
- **Ajustements de l'interface utilisateur** : La fonctionnalité "Thinking off (tab to toggle)" semble être un interrupteur pour afficher ou masquer le processus de raisonnement interne de Claude, ce qui peut rationaliser la sortie. Cela correspond aux retours des utilisateurs sur la transparence et la facilité d'utilisation lors des sessions de codage [3].
- **Tentatives de correction de problèmes connus** : Les rapports selon lesquels Claude Code ajoute "2024" aux recherches en raison de dates de coupure des données d'entraînement sont en cours de traitement, bien que certains utilisateurs signalent des boges persistants. Une solution de contournement implique l'utilisation de hooks personnalisés pour mettre à jour la conscience de la date [3][4].

Pour tous les détails, installez ou vérifiez la dernière version—les mises à jour sont appliquées automatiquement pour tous les utilisateurs [1]. Si vous rencontrez des problèmes, assurez-vous que votre client est à jour. Pour les changements historiques, consultez les journaux des modifications de la communauté comme ClaudeLog, bien qu'ils puissent ne pas couvrir les toutes dernières fonctionnalités [5].

Citations :
[1] https://anthropic.com/news/enabling-claude-code-to-work-more-autonomously
[2] https://www.anthropic.com/news/claude-sonnet-4-5
[3] https://www.reddit.com/r/ClaudeAI/comments/1mtgjdi/claude_code_thinks_it_is_2024_and_keeps_web/
[4] https://medium.com/@dan.avila7/fixed-claude-codes-2024-tunnel-vision-with-a-simple-hook-cb32cfaf9b27
[5] https://www.claudelog.com/claude-code-changelog/