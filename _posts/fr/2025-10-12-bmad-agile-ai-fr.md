---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: 'BMAD Core : Fondation de Développement Agile en IA'
translated: true
type: note
---

BMAD Core est le composant fondamental de la Méthode BMAD (Breakthrough Method for Agile AI-Driven Development), un framework open-source conçu pour rationaliser le développement de logiciels assisté par l'IA (et extensible à d'autres domaines comme l'écriture créative ou la stratégie d'entreprise) en orchestrant des agents d'IA spécialisés dans un workflow agile.

### Aspects Clés de BMAD Core :
- **Rôle et Objectif** : Il agit comme une « fondation lean et rapide » qui standardise les agents d'IA, les workflows, les politiques et les modèles pour garantir des résultats prévisibles et de haute qualité. Cela résout les problèmes courants du développement IA, tels que la perte de contexte et la planisation incohérente, en utilisant des fichiers structurés Markdown/YAML pour les personas des agents, les tâches et les transferts.
- **Composants Principaux** :
  - **Agents** : Fichiers Markdown autonomes (par exemple, dans `bmad-core/agents/`) définissant des rôles comme BMAD Master (superviseur), Scrum Master (planification), Dev (codage) et QA (test). Chacun inclut des configurations YAML pour le persona, les commandes et les dépendances.
  - **Modèles et Markup** : Un langage de balisage personnalisé (défini dans `bmad-core/utils/template-format.md`) pour les prompts réutilisables et la logique de traitement, permettant la génération dynamique de documents sans tâches séparées.
  - **Configuration** : Centralisée dans des fichiers comme `core-config.yaml`, qui gère les clés API, les intégrations LLM (par exemple, OpenAI, Claude) et le chargement différé des ressources pour éviter la surcharge.
  - **Workflows** : Des plans directeurs basés sur YAML qui séquencent les tâches, les dépendances et les collaborations entre agents via des « fichiers de story » (par exemple, pour la création de PRD, la conception d'architecture et les cycles de développement itératifs).
- **Installation et Utilisation** : Configuration via Python (3.9+ requis) dans un répertoire de projet, créant un dossier caché `.bmad-core` avec tous les éléments essentiels. S'intègre avec des IDE comme Cursor ou VS Code pour des interactions transparentes avec les agents.
- **Extensibilité** : Prend en charge les « packs d'extension » pour des agents spécifiques à un domaine (par exemple, DevOps d'infrastructure ou développement de jeux), gardant le cœur générique et modulaire.

Le framework est hébergé sur GitHub (bmad-code-org/BMAD-METHOD) et privilégie le langage naturel par rapport au codage rigide, le rendant accessible aux développeurs solo ou aux équipes passant à l'échelle entreprise. Il a gagné en traction en 2025 pour le "vibe coding" et l'agilité agentique, bien que certains utilisateurs notent une courbe d'apprentissage pour la configuration initiale du PRD. Pour une configuration pratique, consultez la documentation officielle ou le site à bmadcodes.com.