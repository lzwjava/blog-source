---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Panne majeure de Google Cloud Platform
translated: true
type: note
---

### Aperçu
Le 12 juin 2025, Google Cloud Platform (GCP) a connu une panne majeure mondiale d'une durée d'environ 7,5 heures (de 10:51 PDT à 18:18 PDT). L'incident provenait d'un bogue dans une nouvelle fonctionnalité introduite dans le système Service Control de Google, spécifiquement liée aux vérifications des politiques de quota. Cela a entraîné la propagation mondiale d'une mise à jour de quota automatisée non valide, conduisant à des rejets d'API généralisés et des surcharges de tâches, en particulier dans les régions à fort trafic comme us-central1 (Iowa). La panne a perturbé l'accès à de nombreux services GCP, aux produits Google Workspace et aux applications tierces dépendant de l'infrastructure GCP, résultant en plus de 1,4 million de rapports d'utilisateurs sur Downdetector.

### Chronologie
(Tous les horaires en US/Pacific, PDT)

- **10:51 AM** : La panne commence avec une augmentation des erreurs 503 dans les requêtes API externes pour plusieurs produits GCP et Google Workspace, causant des problèmes d'accès intermittents.
- **11:46 AM** : Les équipes d'ingénierie confirment des impacts étendus sur les services ; l'enquête est en cours.
- **12:09 PM** : Les atténuations commencent ; récupération dans la plupart des régions sauf us-central1.
- **12:41 PM** : La cause racine est identifiée comme étant des données de politique de quota non valides ; une solution de contournement est mise en place pour les vérifications de quota.
- **1:16 PM** : Récupération complète de l'infrastructure dans toutes les régions sauf us-central1 et la multi-région US.
- **2:00 PM** : Signes de récupération dans us-central1 ; atténuation complète attendue dans l'heure.
- **3:16 PM** : La plupart des produits GCP sont rétablis, mais des problèmes résiduels persistent dans Dataflow, Vertex AI et Personalized Service Health.
- **5:06 PM** : Dataflow et Personalized Service Health résolus ; problèmes avec Vertex AI toujours en cours avec une estimation de résolution à 22h00.
- **6:27 PM** : Vertex AI entièrement rétabli dans toutes les régions.
- **6:18 PM** : L'incident se termine officiellement avec la restauration complète des services.

L'atténuation principale a pris environ 3 heures, mais les arriérés et les erreurs résiduels ont étendu l'impact total à 7,5 heures.

### Cause Racine
La panne a été déclenchée par une faille dans la fonctionnalité Service Control, qui gère les quotas et politiques des API. Un système automatisé a inséré une politique de quota non valide contenant des champs vides ou nuls dans la base de données. En raison de la réplication mondiale (conçue pour une cohérence quasi instantanée), ces données corrompues se sont propagées dans le monde entier en quelques secondes. Lorsque les requêtes API atteignaient la vérification de quota, cela a entraîné des exceptions de pointeur nul et des rejets (augmentation des erreurs 503 et 5xx). Dans les grandes régions comme us-central1, l'afflux de requêtes ayant échoué a provoqué de graves surcharges de tâches et des défaillances en cascade dans les services dépendants. La nouvelle fonctionnalité manquait de validation suffisante pour les cas limites comme les champs vides, et le système n'a pas "échoué ouvertement" (permettant aux requêtes de continuer pendant les vérifications).

### Services Affectés
La panne a impacté un large éventail de produits Google et de services externes s'appuyant sur GCP. Les services principaux de GCP et Google Workspace ont connu des degrés variables de perturbation, incluant des échecs d'API et des problèmes d'accès à l'interface utilisateur (les ressources de streaming et IaaS sont restées non affectées).

#### Principaux Produits Google Cloud Affectés
- **Compute & Stockage** : Google Compute Engine, Cloud Storage, Persistent Disk.
- **Bases de données** : Cloud SQL, Cloud Spanner, Cloud Bigtable, Firestore.
- **Données & Analytique** : BigQuery, Dataflow, Dataproc, Vertex AI (incluant Online Prediction et Feature Store).
- **Réseau & Sécurité** : Cloud Load Balancing, Cloud NAT, Identity and Access Management (IAM), Cloud Security Command Center.
- **Outils Développeur** : Cloud Build, Cloud Functions, Cloud Run, Artifact Registry.
- **IA/ML** : Vertex AI Search, Speech-to-Text, Document AI, Dialogflow.
- **Autres** : Apigee, Cloud Monitoring, Cloud Logging, Resource Manager API.

#### Principaux Produits Google Workspace Affectés
- Gmail, Google Drive, Google Docs, Google Meet, Google Calendar, Google Chat.

#### Services Tiers Impactés
De nombreuses applications grand public et d'entreprise hébergées ou partiellement dépendantes de GCP ont connu des interruptions :
- **Spotify** : Streaming et accès à l'application perturbés pour ~46 000 utilisateurs.
- **Discord** : Problèmes de chat vocal et de connectivité des serveurs.
- **Fitbit** : Synchronisation et fonctionnalités de l'application interrompues.
- **Autres** : OpenAI (ChatGPT), Shopify, Snapchat, Twitch, Cloudflare (problèmes DNS en cascade), Anthropic, Replit, Microsoft 365 (partiel), Etsy, Nest.

L'échelle mondiale a amplifié l'impact, car GCP alimente une partie significative de l'infrastructure backend d'Internet.

### Résolution
Les équipes d'ingénierie de Google ont rapidement identifié la politique non valide et ont mis en œuvre une solution de contournement pour les vérifications de quota, permettant aux requêtes API de continuer sans validation pendant la crise. Cela a permis de rétablir la plupart des régions vers 12h48 PDT. Pour us-central1, des atténuations ciblées de la surcharge ont été appliquées, suivies par un déblocage manuel des arriérés dans les services affectés comme Dataflow et Vertex AI. La surveillance a confirmé la récupération complète à 18h18 PDT. Aucune perte de données n'est survenue, mais certains services ont connu des retards temporaires.

### Impact
- **Échelle** : Plus de 1,4 million de rapports sur Downdetector, mettant en lumière une perturbation mondiale en temps réel.
- **Économique** : Des milliards de dollars de perte de productivité potentielle pour les entreprises ; Spotify a rapporté une frustration des utilisateurs pendant les heures de pointe.
- **Réputation** : A souligné les risques de la concentration dans le cloud, avec des appels pour de meilleures stratégies multi-cloud.

### Leçons Tirées et Mesures Préventives
Google a publié un post-mortem détaillé mettant l'accent sur la résilience :
- **Changements d'Architecture** : Modulariser Service Control pour isoler les défaillances et permettre des modes "d'échec ouvert".
- **Validation des Données** : Propagation incrémentielle des changements globaux avec pré-validation ; tests améliorés pour les entrées non valides.
- **Protections de Déploiement** : Fonctionnalités de drapeaux obligatoires pour les mises à jour critiques ; analyse statique et gestion des erreurs améliorées.
- **Surveillance & Communication** : S'assurer que les outils de détection des pannes restent opérationnels de manière indépendante ; alertes automatisées plus rapides pour les clients.
- **Plus Large** : Temporisation aléatoire (backoff) dans la logique de nouvelle tentative pour empêcher les cascades de surcharge.

Ces étapes visent à prévenir des incidents similaires, avec des audits continus des systèmes de quota.

[Rapport d'Incident Google Cloud](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW)  
[Analyse de Panne ThousandEyes](https://www.thousandeyes.com/blog/google-cloud-outage-analysis-june-12-2025)  
[Rapport Ookla Downdetector](https://www.ookla.com/articles/google-cloud-outage-june-2025)  
[Analyse ByteByteGo](https://blog.bytebytego.com/p/how-the-google-cloud-outage-crashed)  
[Explication de la Cause Racine sur Medium](https://medium.com/@tahirbalarabe2/%EF%B8%8Fhow-a-single-google-cloud-bug-caused-global-internet-outage-on-june-12-2025-652a83ad9e68)