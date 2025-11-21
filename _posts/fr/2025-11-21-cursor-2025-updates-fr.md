---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Fonctionnalités et mises à jour de Cursor 2025
translated: true
type: note
---

### Aperçu des nouvelles fonctionnalités récentes de Cursor

Cursor, l'éditeur de code propulsé par l'IA construit sur VS Code, a connu une évolution rapide en 2025, avec un accent majeur sur les workflows agentiques, le support multi-modèles et les intégrations transparentes. La plus grande mise à jour est **Cursor 2.0** (publié le 29 octobre 2025), qui introduit Composer—un modèle de codage propriétaire—et une interface repensée pour gérer plusieurs agents d'IA en parallèle. Cela fait passer l'éditeur du codage traditionnel à l'orchestration de tâches pilotées par l'IA, comme la construction autonome de fonctionnalités ou le débogage à travers les bases de code. Ci-dessous, je détaillerai les nouvelles fonctions clés, regroupées par version et catégorie, sur la base des annonces officielles et des rapports d'utilisateurs jusqu'au 21 novembre 2025.

### Versions majeures et nouvelles fonctions principales

#### Cursor 2.0 (29 octobre 2025) – Refonte axée sur les Agents
Cette version réinvente Cursor en tant que "gestionnaire de flotte d'agents", en mettant l'accent sur la délégation plutôt que sur le codage manuel. Ajouts clés :
- **Modèle Composer** : Le premier modèle de codage interne de Cursor, optimisé pour la vitesse et les grandes bases de code. Il utilise la recherche sémantique pour des modifications contextuelles, permettant la génération/modification de code en langage naturel. Il est 21 % plus sélectif dans ses suggestions mais a un taux d'acceptation 28 % plus élevé que les modèles précédents.
- **Interface Multi-Agents** : Exécutez jusqu'à 8 agents simultanément sur la même tâche (par exemple, un pour la planification, un autre pour les tests). Inclut une barre latérale "boîte de réception" pour surveiller la progression, examiner les diffs comme des pull requests et générer des agents avec différents modèles (par exemple, Claude Sonnet 4.5 vs GPT-5.1).
- **Contrôles de Navigateur Intégrés** : Les agents peuvent maintenant contrôler une instance Chrome intégrée—capturer des écrans, déboguer des problèmes d'interface utilisateur ou tester de bout en bout. Cette fonctionnalité est généralement disponible (GA) après la bêta, avec un support entreprise pour une utilisation sécurisée.
- **Mode Plan (Amélioré)** : Les agents génèrent automatiquement des plans modifiables pour les tâches, avec des outils pour la recherche dans la base de code et les exécutions de longue durée. Appuyez sur Maj + Tab pour commencer ; cela inclut des questions de clarification pour de meilleurs résultats.
- **Mode Vocal** : Dictez les prompts via la reconnaissance vocale ; des mots-clés d'envoi personnalisés déclenchent l'exécution des agents. Prend en charge l'élicitation MCP pour des entrées utilisateur structurées (par exemple, des schémas JSON pour les préférences).
- **Revue de Code Automatique** : Revues de diff intégrées pour chaque modification générée par l'IA, détectant les bogues avant la fusion.
- **Agents Cloud** : Exécutez des agents à distance (démarrage plus rapide, fiabilité améliorée) sans immobiliser votre machine locale. Gérez les flottes dans l'éditeur, idéal pour le travail hors ligne.

#### Mise à jour 1.7 (29 septembre 2025) – Optimisateurs de Workflow
- **Commandes Slash** : Actions rapides comme `/summarize` pour une compression de contexte à la demande (libère les limites de tokens sans nouveaux chats).
- **Hooks Personnalisés** : Automatisez les comportements des agents, par exemple, des scripts pré/post-tâche pour le linting ou les tests.
- **Règles d'Équipe** : Partagez les règles de la base de code (par exemple, Bugbot pour les revues automatisées) entre les équipes via les fichiers `.cursorrules`.
- **Support de la Barre des Menus et Liens Profonds** : Navigation plus facile et intégrations externes.

#### Faits marquants du début 2025 (Mai–Août)
- **Agents en Arrière-plan (0.50, 15 mai)** : Exécution de tâches en parallèle (par exemple, un agent refactorise pendant qu'un autre teste). Aperçu sur macOS/Linux.
- **Modèle d'Onglets Amélioré (Multiples Mises à Jour)** : Modifications multi-fichiers, fenêtres de contexte de plus de 1 million de tokens, et entraînement RL en ligne pour des autocomplétions plus intelligentes et rapides (par exemple, les hooks React, les requêtes SQL).
- **@folders et Modifications Inline** : Référencez des répertoires entiers dans les prompts ; CMD+K rafraîchi pour les changements de fichiers entiers avec recherche/remplacement précis.
- **Mode YOLO (Améliorations des Agents)** : Commandes de terminal autonomes, correction de lint et auto-débogage jusqu'à la résolution.

### Intégrations de Modèles
Cursor prend désormais en charge des modèles de pointe pour diverses tâches :
- **OpenAI (13 novembre 2025)** : GPT-5.1 (planification/débogage), GPT-5.1 Codex (codage ambitieux), GPT-5.1 Codex Mini (modifications efficaces).
- **Anthropic** : Sonnet 4 (22 mai 2025) et Sonnet-3.7 (24 février 2025) pour une compréhension supérieure de la base de code.
- **Google** : Gemini 2.5 Pro (10 juin 2025) pour une croissance rapide des intégrations.
- **Autres** : o3/o4-mini (17 avril 2025) pour un codage amélioré.

| Catégorie | Nouvelle Fonction Clé | Avantage | Version |
|----------|------------------|---------|---------|
| **Agents** | Parallélisme Multi-Agents | Déléguer des tâches à 2–8 agents ; comparer les résultats | 2.0 (Oct) |
| **Modèles** | Composer + Suite GPT-5.1 | Génération plus rapide et contextuelle | 2.0/Nov |
| **UI/Workflow** | Mode Plan + Navigateur Intégré | Planification auto + tests de bout en bout | 2.0/Sep |
| **Modifications** | Onglet Multi-Fichiers + Rafraîchissement Inline | Refactorisations plus intelligentes ; précision sur le fichier entier | Mai–Oct |
| **Collaboration** | Règles d'Équipe + Agents Cloud | Directives partagées ; exécution distante | Sep/Oct |

### Mises à jour Tarifaires et d'Accessibilité
- **Forfaits Simplifiés (16 juin 2025)** : Pro (20 $/mois pour une base de calcul, appels d'outils illimités) ; nouveau Ultra (200 $/mois, utilisation x20) pour les utilisateurs avancés.
- **Mode Max** : Accès basé sur les tokens aux capacités complètes des modèles (par exemple, contextes longs) sur tous les meilleurs modèles.

Ces fonctionnalités rendent Cursor idéal pour le développement piloté par les agents, réduisant le travail manuel jusqu'à 39 % dans les fusions de PR (selon une étude de l'Université de Chicago). Pour le journal des modifications complet, consultez [le site officiel de Cursor](https://cursor.com/changelog). Si vous êtes sur VS Code, la migration est transparente—téléchargez et expérimentez avec la vue agent de la version 2.0 pour un gain rapide.