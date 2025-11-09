---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Comprendre les objectifs de niveau de service
translated: true
type: note
---

### Qu'est-ce qu'un Service Level Objective (SLO) ?

Un **Service Level Objective (SLO)** est un objectif mesurable qui définit le niveau de fiabilité, de performance ou de disponibilité souhaité pour un service ou un système. C'est un concept clé dans le domaine de la Site Reliability Engineering (SRE), où les SLOs servent d'objectifs internes pour garantir la satisfaction des utilisateurs sans surdimensionner les ressources.

#### Composants clés :
- **Service Level Indicator (SLI)** : La métrique réelle qui est mesurée (par exemple, la latence des requêtes, le taux d'erreur ou le pourcentage de disponibilité).
- **Valeur cible** : Un seuil ou une plage spécifique (par exemple, « 99,9 % des requêtes traitées en moins de 200 ms »).
- **Fenêtre temporelle** : La période sur laquelle le SLO est évalué (par exemple, une moyenne glissante sur 28 jours).

#### SLO vs. SLA :
- **SLO** : Objectifs internes et aspirationnels pour l'équipe d'ingénierie (par exemple, viser 99,95 % de disponibilité).
- **SLA** : Engagements contractuels externes envers les clients, souvent dérivés des SLOs avec des pénalités en cas de non-respect (par exemple, 99,9 % de disponibilité avec des crédits en cas de violation).

#### Dans le contexte des LLMs (par exemple, d'après SLOs-Serve) :
Dans le service des grands modèles de langage, les SLOs sont souvent spécifiques à une étape :
- **Time-to-First-Token (TTFT)** : SLO strict pour la pré-remplissage (traitement de l'entrée) dans les applications interactives comme les chatbots.
- **Tokens-Per-Output-Time (TPOT)** : SLO de décodage pour la vitesse de génération, variant selon la charge de travail (par exemple, 50 ms/jeton pour le codage vs 100 ms pour la synthèse).

Les SLOs aident à équilibrer le débit et la latence dans des environnements partagés, empêchant les violations lors de pics d'activité.

Pour une lecture plus approfondie :  
[SRE Book: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)  
[SLOs-Serve Paper](https://arxiv.org/abs/2504.08784)