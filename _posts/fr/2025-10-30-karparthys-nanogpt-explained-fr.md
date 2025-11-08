---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: NanoGPT et Nanochat de Karpathy expliqués
translated: true
type: note
---

### Aperçu
**nanoGPT** et **nanochat** sont tous deux des projets open-source créés par Andrej Karpathy (ancien responsable IA chez OpenAI/Tesla) pour enseigner le fonctionnement interne des grands modèles de langage (LLM) via des implémentations minimalistes et from-scratch en PyTorch. Ce sont des outils pédagogiques plutôt que des systèmes prêts pour la production, privilégiant la simplicité et la lisibilité aux optimisations.

- **nanoGPT** (publié en 2023) : Un framework léger pour entraîner des modèles de type transformer GPT sur des données textuelles brutes, se concentrant uniquement sur la phase de pré-entraînement.
- **nanochat** (publié en octobre 2025) : Une évolution complète et full-stack de nanoGPT, permettant l'entraînement de bout en bout, le fine-tuning, l'inférence et le déploiement d'une IA conversationnelle de type ChatGPT.

### Différences Clés
Voici une comparaison côte à côte :

| Aspect               | nanoGPT                                                                 | nanochat                                                                 |
|----------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Objectif Principal** | Pré-entraînement d'un modèle GPT sur du texte non structuré (ex: jeu de données Shakespeare). | Pipeline complet : Pré-entraînement + fine-tuning pour le chat + inférence dans une interface web. |
| **Portée**           | Implémentation minimale d'un transformer (~400 lignes de code cœur). Pas d'interface de chat. | ~8 000 lignes au total, incluant un fine-tuning de type RLHF, l'échantillonnage et une démo de chat basée sur Streamlit. |
| **Entra