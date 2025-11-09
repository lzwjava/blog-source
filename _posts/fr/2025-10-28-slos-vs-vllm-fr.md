---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Comparaison des fonctionnalités SLOs-Serve et vLLM
translated: true
type: note
---

### Comparaison : SLOs-Serve vs. vLLM

SLOs-Serve étend vLLM en l'intégrant comme moteur de base pour le *batching* tout en ajoutant des couches pour garantir des SLO (Service Level Objective) multiples, le rendant plus adapté aux environnements de production avec des charges de travail diverses et sensibles à la latence. vLLM se concentre principalement sur l'inférence à haut débit pour des scénarios à SLO unique ou maximisant le débit, en utilisant des techniques comme PagedAttention pour l'efficacité mémoire. Ci-dessous se trouve une comparaison structurée basée sur les aspects clés du papier SLOs-Serve et de la conception de vLLM.

| Aspect                  | SLOs-Serve                                                                 | vLLM                                                                 |
|-------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------|
| **Objectif principal**  | Service multi-SLO pour les applications LLM multi-étapes (ex. : TTFT serré pour le *prefill* en raisonnement, TPOT serré pour le *decode* en codage). Gère les charges de travail mixtes et en rafale avec des garanties spécifiques par étape. | *Batching* à haut débit pour le *decoding* continu, optimisé pour les charges de travail liées à la mémoire via PagedAttention. Suppose des SLO uniformes ou priorise le débit agrégé. |
| **Gestion des SLO**    | Prise en charge explicite des SLO multiples : SLO par étape (*prefill*/*decode*) et par application (ex. : 50ms TPOT pour le codage vs. 100ms pour le chat). Utilise un contrôle d'admission souple pour rejeter/différer les requêtes violant les SLO. | Pas de support natif des SLO multiples ; repose sur des configurations statiques (ex. : taille de lot maximale). Les violations de SLO sont fréquentes sous contention (ex. : pics de latence >2x lors de rafales). |
| **Ordonnanceur**       | Basé sur la programmation dynamique (DP) : Optimise les budgets *prefill*, les tailles de lot et les longueurs de spéculation par niveau de SLO. Prédit le temps d'exécution avec un modèle Roofline (précision R² > 0,8). | Ordonnanceur à *batching* continu : Remplit de manière gourmande les requêtes dans des lots dynamiques, en se concentrant sur les charges de travail intensives en *decoding*. Aucune planification tenant compte des SLO. |
| **Optimisation du *Prefill*** | *Prefill* en morceaux avec spéculation adaptative (1-10 jetons par SLO). Alloue un "budget *prefill*" pour équilibrer avec le *decode*. | *Prefill* unique par requête ; prend en charge le *prefill* en morceaux mais sans adaptation SLO. Sujet à un blocage en tête de ligne dans les charges mixtes. |
| **Optimisation du *Decode*** | Taille de lot adaptative SLO (jusqu'à 512+ jetons) et *decoding* spéculatif adapté aux cibles TPOT. | *Decoding* continu efficace avec *batching* prospectif ; haut débit (ex. : 10-20x supérieur à Hugging Face) mais ignore les délais par requête. |
| **Gestion des ressources** | Routage multi-réplique via Ray ; résilience aux rafales avec files d'attente *best-effort* et préemption. Gère les configurations désagrégées. | Nœud unique ou distribution basique (via l'intégration Ray) ; pas de routage proactif ou d'allocation priorisée par SLO. |
| **Débit et Capacité**  | Gain de capacité moyen de 2,2× par rapport à vLLM (moyenne géométrique sur 6 scénarios : chatbot, codage, etc.). Ex. : 2,4× lors de rafales de raisonnement. Mise à l'échelle super-linéaire avec les répliques. | Référence pour le débit : Jusqu'à 24x plus rapide que les alternatives dans les traces intensives en *decoding*, mais se dégrade sous contraintes SLO (ex. : perte de capacité de 50% dans les charges de travail mixtes). |
| **Surcharge**          | <10ms par ordonnancement ; minimale grâce à l'efficacité de la DP (O(n) états). | Faible (<1ms pour le *batching*) ; mais manque de logique SLO, donc pas de surcharge ajoutée. |
| **Cas d'utilisation**  | Applications de production avec des SLA stricts : Agents d'appel d'outils, chaînes de raisonnement, trafic en rafale (ex. : traces Azure). | Débit recherche/développement : Service simple, génération de contexte long, charges uniformes. |
| **Limitations**        | Suppose des SLO/délais connus ; des extensions futures sont nécessaires pour les longueurs inconnues. Construit sur vLLM, hérite donc de ses forces en *decoding*. | Difficultés avec les SLO multiples/variables ; latences de queue élevées dans les configurations GPU partagées (p99 >2x la cible dans les évaluations). |
| **Implémentation**     | Prototype open-source sur vLLM + Ray ; prend en charge les modèles OPT/ToolLlama sur GPU A100/H100. | Open-source mature (GitHub) ; largement adopté, prend en charge 100+ modèles, déploiement facile. |

En résumé, vLLM excelle en efficacité brute pour un service orienté débit, mais est moins performant sur le respect des SLO dans des scénarios complexes du monde réel — ce qui conduit aux gains de 2x+ de SLOs-Serve via des optimisations ciblées. Si votre charge de travail est purement axée sur la maximisation du débit sans garanties de latence, vLLM reste plus simple et plus rapide à déployer.

[SLOs-Serve: Optimized Serving of Multi-SLO LLMs](https://arxiv.org/abs/2504.08784)  
[vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180)