---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Pannes majeures de Google Cloud Platform
translated: true
type: note
---

### Principales pannes dans l'histoire de Google Cloud Platform (GCP)

Google Cloud Platform a connu plusieurs pannes significatives depuis ses débuts, souvent dues à des bogues logiciels, des défaillances matérielles, des facteurs environnementaux ou des problèmes de capacité. Le tableau ci-dessous résume certaines des plus notables, sélectionnées pour leur ampleur, leur durée ou leur impact généralisé. Ces incidents sont tirés des archives historiques jusqu'à mi-2025.

| Date | Cause | Impact |
|------|--------|--------|
| 14 décembre 2020 | Réduction accidentelle de la capacité du système central de gestion des identifiants utilisateurs, affectant l'authentification basée sur OAuth. | Panne mondiale d'environ 90 minutes ; accès perturbé à Gmail, YouTube, Google Drive, les services GCP et des applications comme Pokémon GO pour des millions d'utilisateurs dans le monde. |
| Juillet 2022 | Vague de chaleur extrême (plus de 40°C) à Londres provoquant des défaillances du système de refroidissement dans la zone europe-west2-a. | Perturbations régionales pendant environ 24 heures ; a affecté Cloud Storage, BigQuery, Compute Engine, GKE et d'autres services, forçant des basculements vers d'autres régions. |
| 8 août 2022 | Incident électrique entraînant un incendie dans le centre de données de Council Bluffs, dans l'Iowa (sans lien avec les problèmes concurrents de recherche/cartes). | Intervention des pompiers localisée ; latence globale du service Cloud Logging pendant plusieurs jours, impactant la surveillance et le débogage pour les utilisateurs de GCP. |
| 28 avril 2023 | Infiltration d'eau et incendie dans un centre de données parisien, provoquant des défaillances multi-clusters dans europe-west9-a. | Perturbations généralisées en Europe, en Asie et dans les Amériques ; a touché VPC, l'équilibrage de charge, BigQuery et les services de réseau pendant plusieurs heures à plusieurs jours. |
| 7-8 août 2024 | Défaillances dans l'activation du service Cloud TPU lors de l'activation d'API pour Vertex AI. | Panne mondiale pendant environ 14 heures ; a bloqué les téléchargements de modèles de machine learning et l'entraînement dans Vertex AI dans toutes les régions majeures. |
| 23 octobre 2024 | Panne de courant et arc électrique dans la zone europe-west3-c (Francfort), dégradant l'infrastructure de refroidissement. | Panne régionale d'une demi-journée (environ 8 heures) ; arrêt partiel de l'infrastructure, avec diversion du trafic vers d'autres zones. |
| 7-8 janvier 2025 | Problèmes interconnectés incluant des échecs d'authentification SAML dans Apigee, des erreurs HTTP dans les API Vertex Gemini et des blocages de publication dans Pub/Sub. | Perturbations de plusieurs heures sur plus de 18 heures ; a affecté la gestion des API, l'inférence IA et la messagerie en temps réel across regions. |
| 12 juin 2025 | Bogue dans une nouvelle fonctionnalité de Service Control (vérifications des politiques de quota) provoquant des surcharges de tâches dans les grandes régions comme us-central1. | Panne mondiale d'environ 7 heures ; a mis hors service Spotify, Discord, Fitbit et de nombreux services dépendants de GCP, avec plus de 1,4 million de signalements. |

Ces incidents mettent en lumière les douleurs de croissance de GCP, des premiers problèmes d'App Engine à la fin des années 2000 aux défaillances systémiques plus récentes. Google publie généralement des post-mortems et des plans de correction, tels que la modularisation des composants pour "faire échouer ouvertement". Pour le statut le plus récent, consultez le [Tableau de santé des services Google Cloud](https://status.cloud.google.com/).

[A History of Google Cloud and Data Center Outages](https://www.datacenterknowledge.com/outages/a-history-of-google-cloud-and-data-center-outages)  
[Google services outages - Wikipedia](https://en.wikipedia.org/wiki/Google_services_outages)  
[Google Cloud Outage History | StatusGator](https://statusgator.com/blog/google-cloud-outage-history/)  
[The 10 Biggest Cloud Outages Of 2025 (So Far) - CRN](https://www.crn.com/news/cloud/2025/the-10-biggest-cloud-outages-of-2025-so-far)  
[Google Cloud Outage Analysis: June 12, 2025 - ThousandEyes](https://www.thousandeyes.com/blog/google-cloud-outage-analysis-june-12-2025)