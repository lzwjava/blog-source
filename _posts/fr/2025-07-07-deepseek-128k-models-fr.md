---
audio: false
generated: true
lang: fr
layout: post
title: Les modèles à 128 000 tokens de DeepSeek en 2025
translated: true
type: note
---

En juin 2025, DeepSeek dispose d'une gamme de modèles avec des longueurs de contexte impressionnantes, exploitant souvent leur architecture Mixture-of-Experts (MoE) pour l'efficacité. Voici un aperçu :

*   **DeepSeek-R1 :** Ce modèle, publié en janvier 2025, est reconnu pour prendre en charge une longueur de contexte de **128 000 tokens** (ou 131 072 tokens dans certains benchmarks). Il est particulièrement performant en mathématiques, en programmation et en raisonnement structuré grâce à son post-entraînement par Reinforcement Learning (RL).
*   **DeepSeek-V3 :** Publié en décembre 2024, DeepSeek-V3, y compris son modèle de base, prend également en charge une longueur de contexte de **128 000 tokens**. C'est un puissant modèle MoE avec 671 milliards de paramètres au total (37 milliards actifs par requête).
*   **DeepSeek-Coder-V2 :** Ce modèle MoE axé sur le code, publié en juillet 2024, dispose d'une fenêtre de contexte significative de **128 000 tokens**. Il prend en charge un large éventail de langages de programmation (338).
*   **DeepSeek-V2 :** Lancé en mai 2024, DeepSeek-V2 revendique une longueur de contexte de **128 000 tokens**. Ce modèle MoE vise un entraînement économique et une inférence efficace.
*   **DeepSeek-V2.5 :** Publié en septembre 2024, ce modèle combine des capacités générales et de programmation et prend également en charge une fenêtre de contexte de **128 000 tokens**.

**Considérations importantes :**

*   **Longueur de Contexte Native vs. Limites de l'API :** Bien que certains modèles DeepSeek aient une longueur de contexte native allant jusqu'à 163 840 tokens, l'API DeepSeek peut limiter la fenêtre de contexte disponible pour des modèles spécifiques (par exemple, "deepseek-chat" et "deepseek-reasoner" ont actuellement une limite de contexte de 64K via leur API). Si vous avez besoin du contexte complet, l'exécution des modèles localement ou l'utilisation de fournisseurs d'API autorisant des contextes plus longs pourrait être nécessaire.
*   **Dégradation des Performances :** Comme pour d'autres grands modèles de langage, bien que les modèles puissent annoncer des fenêtres de contexte très longues, les performances (précision, raisonnement) peuvent parfois se dégrader lorsqu'elles sont poussées à leur longueur maximale absolue. DeepSeek R2, par exemple, devrait résoudre la baisse de performance de 15 % observée dans R1 à sa fenêtre de contexte maximale de 128 000 tokens.

En résumé, DeepSeek est un acteur important dans l'espace des LLM à contexte long, avec plusieurs modèles en juin 2025 offrant une fenêtre de contexte de 128K tokens, les rendant adaptés au traitement d'entrées extensives et de tâches complexes.