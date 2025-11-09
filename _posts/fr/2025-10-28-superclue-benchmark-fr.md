---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: 'SuperCLUE : Benchmark pour les LLM chinois'
translated: true
type: note
---

SuperCLUE est une suite de référence complète conçue pour évaluer les grands modèles de langage (LLM) chinois. Il s'appuie sur la référence originale CLUE (Chinese Language Understanding Evaluation), en l'étendant pour évaluer les capacités avancées des LLM plutôt que seulement les modèles plus petits. Développé par l'équipe CLUEbenchmark—un effort collaboratif impliquant des chercheurs d'institutions comme l'Université Tsinghua et des entreprises de l'écosystème de l'IA chinois—SuperCLUE a été introduit pour la première fois en 2023 pour combler les lacunes dans l'évaluation des LLM chinois par rapport aux normes internationales.

### Caractéristiques principales
- **Domaines d'évaluation** : Il évalue les modèles selon quatre quadrants principaux :
  - Compréhension et génération du langage (ex. : compréhension de lecture, synthèse).
  - Compétences et connaissances professionnelles (ex. : raisonnement mathématique, programmation).
  - Intelligence agent (ex. : utilisation d'outils, planification).
  - Sécurité (ex. : détection des biais, alignement éthique).
- **Structure** : Décomposé en 12 tâches principales, avec des jeux de données comme SuperCLUE-Math6 pour les problèmes mathématiques à plusieurs étapes.
- **Objectif** : Aide à suivre les progrès de l'IA chinoise, en mettant en lumière à la fois les forces (ex. : traitement des nuances culturelles) et les lacunes par rapport aux modèles mondiaux comme la série GPT.
- **Mises à jour** : Depuis mi-2025, il est utilisé pour des bilans périodiques, les classements montrant que les modèles chinois comme Qwen et GLM réduisent l'écart avec les modèles internationaux.

La référence est open-source et activement maintenue, les évaluations étant souvent partagées via des articles arXiv et GitHub.

[SuperCLUE : A Comprehensive Chinese Large Language Model Benchmark](https://arxiv.org/abs/2307.15020)  
[SuperCLUE GitHub Repository](https://github.com/CLUEbenchmark/SuperCLUE)  
[ChinAI : SuperCLUE Benchmarks —2025 Midyear Check-in](https://chinai.substack.com/p/chinai-324-superclue-large-model)