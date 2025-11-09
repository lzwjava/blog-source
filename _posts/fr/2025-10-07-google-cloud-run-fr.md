---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Introduction à Google Cloud Run
translated: true
type: note
---

Cloud Run est une plateforme de calcul serverless entièrement gérée dans GCP qui vous permet d'exécuter des conteneurs sans état directement sur l'infrastructure évolutive de Google. Elle est conçue pour les développeurs qui souhaitent déployer des applications sans se soucier des serveurs sous-jacents, du provisionnement ou de la mise à l'échelle. Que vous construisiez des applications web, des API, des microservices ou des charges de travail événementielles, Cloud Run gère l'infrastructure pour que vous puissiez vous concentrer sur le code.

### Fonctionnalités principales
- **Exécution Serverless** : Déployez du code conteneurisé (prenant en charge n'importe quel langage ou runtime) qui se met à l'échelle automatiquement de zéro à des milliers d'instances en fonction des requêtes entrantes ou du trafic.
- **Tarification à l'Usage** : Facturé uniquement pour les ressources que vous consommez — par requête ou par durée d'instance — ce qui le rend rentable pour les charges de travail variables.
- **Intégrations intégrées** : Fonctionne parfaitement avec d'autres services GCP comme Cloud SQL pour les bases de données, Cloud Storage pour les fichiers, Pub/Sub pour la messagerie, et plus encore. Il prend également en charge VPC pour le réseau privé.
- **Options de déploiement** :
  - Poussez une image de conteneur pré-construite depuis Artifact Registry ou Docker Hub.
  - Déployez directement depuis le code source en utilisant Cloud Build (prend en charge des langages comme Node.js, Python, Java, Go, .NET et Ruby).
  - Utilisez Cloud Run Functions pour des déploiements plus simples de type fonction-as-a-service.
- **Sécurité et Réseau** : Les services peuvent être publics ou privés (nécessitant une authentification), avec la prise en charge des points de terminaison HTTPS et des domaines personnalisés.
- **Modes supplémentaires** : Au-delà des services pilotés par les requêtes, il propose Jobs pour les tâches par lots (par exemple, des scripts planifiés ou du traitement de données) et Worker Pools pour les charges de travail de longue durée, non-HTTP.

Pour commencer, vous pouvez déployer via la Console GCP, l'interface de ligne de commande gcloud ou des pipelines CI/CD. Par exemple, construisez et déployez un simple conteneur "Hello World" en quelques minutes.

### La Console d'administration Cloud Run
La section Cloud Run dans la Console GCP fournit un tableau de bord intuitif pour gérer vos déploiements. Voici une répartition basée sur la vue Services que vous avez partagée :

- **Vue d'ensemble** : La page principale "Cloud Run > Services" liste tous vos services déployés dans un format de tableau. Elle commence par une bannière de recommandation utile comme "Exécutez votre application sur une plateforme entièrement gérée" pour encourager les démarrages rapides si vous êtes nouveau.

- **Colonnes du tableau** (comme indiqué dans votre extrait) :
  - **Nom** : L'identifiant unique pour chaque service (par exemple, "my-api").
  - **Type de déploiement** : Indique comment il a été déployé — par exemple, "Container" pour les images ou "Source" pour les déploiements basés sur le code.
  - **Req/sec** : Métrique en temps réel des requêtes par seconde pour surveiller la charge du trafic.
  - **Région** : La région GCP où le service s'exécute (par exemple, us-central1), affectant la latence et la conformité.
  - **Authentification** : Indique si le service est public (autoriser les accès non authentifiés) ou nécessite une authentification IAM.
  - **Entrée** : Contrôle le routage du trafic — par exemple, "Tous" pour interne/externe, ou restreint au seul trafic interne.
  - **Dernier déploiement** : Horodatage de la mise à jour la plus récente.
  - **Déployé par** : L'utilisateur ou le compte de service qui a effectué le déploiement.

- **Filtres et Actions** : Au-dessus du tableau, vous pouvez filtrer par n'importe laquelle de ces colonnes pour affiner votre liste. Utilisez le bouton "Créer un service" pour déployer de nouveaux services, ou cliquez sur un nom de service pour modifier les paramètres comme les limites de CPU/mémoire, les variables d'environnement, les configurations de mise à l'échelle ou les révisions pour le fractionnement du trafic.

Cette console facilite la surveillance des performances, la consultation des journaux et l'itération sur les déploiements sans quitter le navigateur. Pour une exploration pratique, naviguez vers [console.cloud.google.com/run](https://console.cloud.google.com/run) après avoir activé l'API.

[Qu'est-ce que Cloud Run](https://cloud.google.com/run/docs/overview/what-is-cloud-run)  
[Documentation Cloud Run](https://cloud.google.com/run/docs)