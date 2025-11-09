---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Présentation de Google Cloud Run
translated: true
type: note
---

### Qu'est-ce que Google Cloud Run ?

Google Cloud Run est une plateforme serverless entièrement gérée sur Google Cloud Platform (GCP) conçue pour exécuter des applications conteneurisées. Elle permet aux développeurs de déployer et de mettre à l'échelle du code sans se soucier de l'infrastructure sous-jacente, en gérant automatiquement l'approvisionnement, la mise à l'échelle et la maintenance. Elle prend en charge les requêtes HTTP/HTTPS sans état, les charges de travail event-driven et passe à zéro instance lorsqu'elle est inactive, ce qui la rend très rentable.

### Fonctionnalités et capacités principales
- **Déploiement par conteneurs** : Exécutez n'importe quel langage ou framework dans un conteneur standard (par exemple, Docker), avec une prise en charge intégrée des services HTTP/gRPC, des travaux en arrière-plan et du traitement asynchrone.
- **Mise à l'échelle automatique et paiement à l'usage** : Passe de zéro à des milliers d'instances en fonction du trafic ; vous ne payez que pour l'utilisation réelle (CPU, mémoire et requêtes).
- **Intégrations** : Fonctionne parfaitement avec d'autres services GCP comme Cloud Build (pour CI/CD), Cloud SQL (bases de données), Pub/Sub (messagerie), Artifact Registry (stockage de conteneurs) et les outils d'IA pour les tâches accélérées par GPU.
- **Sécurité et réseau** : Authentification intégrée (IAM), connectivité VPC et binary authorization pour des déploiements sécurisés.
- **Niveau gratuit** : Jusqu'à 2 millions de requêtes par mois sans frais.

### Scénarios d'utilisation typiques
Cloud Run est idéal pour les applications modernes et event-driven où la flexibilité et la faible surcharge sont essentielles. Voici quelques exemples courants :
- **Applications Web et APIs** : Héberger des microservices sans état, des API RESTful ou des applications web complètes (par exemple, un backend Node.js servant du contenu dynamique depuis une base de données). Il excelle pour les sites e-commerce ou les backends mobiles qui gèrent un trafic variable.
- **Travaux par lots et traitement de données** : Exécuter des tâches planifiées comme des pipelines ETL (extract, transform, load) ou des files d'attente de traitement d'image/vidéo, déclenchées par Cloud Scheduler ou Pub/Sub.
- **Charges de travail IA/ML** : Héberger de grands modèles de langage (LLM) comme Llama 3.1 ou Gemma 2 pour l'inférence en temps réel, tels que des chatbots, de la reconnaissance d'image ou du transcodage vidéo. La prise en charge des GPU le rend adapté aux tâches nécessitant beaucoup de calcul.
- **Migrations serverless** : Transitionner depuis des VM ou Kubernetes (par exemple, via Knative) pour réduire les coûts – des entreprises comme Telegraph Media Group ont rapporté des économies de 90 % sur les coûts et les émissions de carbone après leur migration.

En résumé, c'est une excellente solution pour les développeurs qui souhaitent la puissance de Kubernetes sans la charge opérationnelle, en particulier pour les charges de travail irrégulières ou imprévisibles.

[Documentation Cloud Run](https://cloud.google.com/run)