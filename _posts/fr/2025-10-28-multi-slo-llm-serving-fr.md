---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Optimisation du service LLM multi-SLO
translated: true
type: note
---

### Aperçu
L'article « SLOs-Serve: Optimized Serving of Multi-SLO LLMs » présente SLOs-Serve, un système conçu pour servir efficacement les grands modèles de langage (LLM) dans des applications multi-étapes où chaque étape (par exemple, le pré-remplissage pour le traitement de l'entrée, le décodage pour la génération de tokens) et chaque application (par exemple, chatbots, assistants de codage) a des objectifs de niveau de service (SLO) spécifiques. Ces SLO garantissent une faible latence pour les aspects visant l'utilisateur, comme le temps jusqu'au premier token (TTFT) pour le pré-remplissage et le temps par token de sortie (TPOT) pour le décodage. Les systèmes de service traditionnels comme vLLM ou Sarathi-Serve privilégient le débit mais violent souvent ces SLO granulaires sous des ressources partagées, surtout lors de pics de charge ou de charges de travail mixtes.

### Défis et Contributions Principaux
Les auteurs identifient les défis du service multi-SLO :
- **Requêtes multi-étapes** : Les applications comme les LLM de raisonnement (SLO stricts pendant les phases de « réflexion ») ou les agents d'appel d'outils (boucles avec pré-remplissage/décodage stricts) nécessitent des garanties spécifiques à chaque étape.
- **Contention des ressources** : Les GPU partagés entraînent des violations de SLO dans des configurations colocalisées ou désagrégées.
- **Trafic irrégulier** : Les pics soudains submergent les ordonnanceurs.

Les contributions de SLOs-Serve incluent :
- Un ordonnanceur basé sur la programmation dynamique (DP) qui optimise les allocations de tokens (budget de pré-remplissage, tailles de lots) pour respecter les SLO tout en maximisant le débit.
- La prise en charge du pré-remplissage par blocs, du décodage spéculatif adaptatif aux SLO (personnalisation des longueurs de spéculation par niveau de SLO) et du contrôle d'admission souple (garantie des SLO pour les requêtes admises, report des autres).
- Une architecture distribuée avec routage multi-répliques et résilience aux pics, construite sur vLLM pour le traitement par lots et sur Ray pour l'orchestration.

| Application | SLO Pré-remplissage | SLO Décodage | Exemple |
|-------------|-------------|------------|---------|
| Récapitulation | Strict (ex. : ralentissement max 3x) | Lâche (TPOT 100ms) | Traitement de documents |
| Codage | Lâche | Strict (TPOT 50ms) | Génération de code |
| Chatbot | Lâche | Lâche | Requêtes interactives |
| Appel d'outils | Strict (boucles) | Strict (boucles), lâche (final) | Flux de travail agentiques |
| Raisonnement | Strict (réflexion) | Strict (réflexion), lâche (réponse) | Chaîne de pensée |

### Conception du Système
- **Ordonnanceur (Algorithme 1)** : Utilise la DP pour admettre les requêtes et planifier les lots, modélisant le temps d'exécution via un prédicteur inspiré de Roofline (précision R² > 0,8). Les états suivent la mémoire, le budget de pré-remplissage et les requêtes acceptées ; les transitions priorisent les délais les plus courts et l'atteinte des SLO.
- **Formation des Lots** : Taille dynamique (jusqu'à 512+ tokens) basée sur le TPOT le plus strict, permettant des lots plus grands pour un débit plus élevé sans violations de SLO.
- **Décodage Spéculatif** : Adapte les longueurs de spéculation (ex. : 1-10 tokens) par niveau de SLO pour augmenter le budget de pré-remplissage, résolu par énumération pour un équilibre optimal pré-remplissage/décodage.
- **Multi-Répliques et Pics** : Un contrôleur centralisé achemine les requêtes de manière proactive ; les requêtes inatteignables vont dans une file d'attente au mieux, préemptées si nécessaire.

La conception explore des compromis, comme des lots plus grands augmentant le débit mais risquant la latence (visualisé dans des figures montrant les régions réalisables pour les SLO).

### Évaluation
Testé sur 6 scénarios (chatbot, codage, récapitulation, mixte, appel d'outils, raisonnement) en utilisant des traces réelles (charges de travail Azure LLM) et des jeux de données (ShareGPT, HumanEval, etc.). Modèles : OPT-7B/13B/30B, ToolLlama-7B. Matériel : 4×A100 GPU (principal), jusqu'à 8×H100.

- **Gains de Capacité** : Amélioration moyenne de 2,2× par rapport à vLLM/Sarathi-Serve/DistServe (moyenne géométrique sur les scénarios). Par exemple, 2,4× en raisonnement, 2,1× en codage avec pics.
- **Mise à l'échelle** : Super-linéaire avec les répliques (jusqu'à 6,2× en appel d'outils sous pics) via le routage.
- **Ablations** : La spéculation ajoute 1,66×, le routage 1,19×, la gestion des pics 1,34×.
- Surcharge : <10ms par invocation de planification.

Les figures montrent que SLOs-Serve maintient les latences p99 près des cibles pendant les pics, tandis que les solutions de référence se dégradent.

### Conclusions
SLOs-Serve fait progresser le service des LLM en garantissant des multi-SLO dans des environnements divers et irréguliers, débloquant des gains d'efficacité de 2x+. Les travaux futurs pourraient s'étendre à des longueurs de décodage inconnues ou à plus d'étapes. Le système démontre qu'un ordonnancement personnalisé selon les SLO est essentiel pour les déploiements de LLM de qualité production.

[SLOs-Serve: Optimized Serving of Multi-SLO LLMs](https://arxiv.org/abs/2504.08784)