---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Analyse de cas de panne AWS Octobre 2025
translated: true
type: note
---

### Panne AWS du 20 octobre 2025 : Analyse détaillée de l'incident

La panne AWS du 20 octobre 2025 a été une perturbation majeure originaire de la région US East (N. Virginia) (us-east-1), le centre de données le plus vaste et le plus critique d'AWS. Elle a commencé tard le 19 octobre (PDT) et a duré environ 16 heures, affectant plus de 140 services et se propageant à l'échelle mondiale en raison des dépendances sur cette région. L'incident a mis en lumière des vulnérabilités dans la résolution DNS, les interdépendances de services et les processus de reprise, impactant des millions d'utilisateurs à travers des applications, sites web et services. Voici une analyse basée sur le post-mortem officiel d'AWS et les rapports contemporains.

#### Chronologie
La panne s'est déroulée en phases, commençant par la détection et escaladant vers des défaillances en cascade avant une reprise progressive. Principales étapes (toutes les heures en PDT) :

| Heure | Événement |
|------|-------|
| 23h49 (19 oct) | Taux d'erreur et latences accrus détectés sur plusieurs services AWS dans us-east-1. |
| 00h11 (20 oct) | AWS signale publiquement des taux d'erreur élevés ; les premiers rapports d'utilisateurs augmentent sur des sites de surveillance comme DownDetector. |
| 00h26 | Le problème est identifié comme des échecs de résolution DNS pour les endpoints API de DynamoDB dans us-east-1. |
| 01h26 | Taux d'erreur élevés confirmés spécifiquement pour les APIs DynamoDB, y compris les Global Tables. |
| 02h22 | Atténuations initiales appliquées ; premiers signes de reprise. |
| 02h24 | Problème DNS de DynamoDB résolu, déclenchant une reprise partielle des services – mais des défaillances de lancement EC2 et des échecs de vérification de santé des Network Load Balancer (NLB) apparaissent. |
| 03h35 | DNS entièrement atténué ; la plupart des opérations DynamoDB réussissent, mais les lancements EC2 restent perturbés dans toutes les Zones de Disponibilité (AZ). |
| 04h08 | Travaux en cours sur les erreurs EC2 et les délais d'interrogation Lambda pour les SQS Event Source Mappings. |
| 05h48 | Reprise partielle des lancements EC2 dans certaines AZ ; les arriérés SQS commencent à se résorber. |
| 06h42 | Atténuations déployées à travers les AZ ; AWS met en place une limitation du débit (rate limiting) sur les nouveaux lancements d'instances EC2 pour stabiliser. |
| 07h14 | Les erreurs d'API et les problèmes de connectivité persistent sur plusieurs services ; les défaillances impactant les utilisateurs atteignent leur pic (ex. : pannes d'applications). |
| 08h04 | L'enquête se concentre sur le réseau interne d'EC2. |
| 08h43 | Cause racine des problèmes réseau identifiée : défaillance dans le sous-système interne d'EC2 responsable de la surveillance de la santé des NLB. |
| 09h13 | Atténuations supplémentaires pour les vérifications de santé des NLB. |
| 09h38 | Vérifications de santé des NLB entièrement rétablies. |
| 10h03 – 12h15 | Améliorations progressives des lancements EC2 ; les invocations Lambda et la connectivité se stabilisent par phases dans les AZ. |
| 13h03 – 14h48 | Limitations de débit réduites ; traitement des arriérés pour des services comme Redshift, Amazon Connect et CloudTrail. |
| 15h01 | Normalité opérationnelle complète rétablie pour tous les services ; des arriérés mineurs (ex. : AWS Config, Redshift) devraient être résolus dans les heures suivantes. |
| 15h53 | AWS déclare la panne résolue. |

Les rapports d'utilisateurs sur des plateformes comme DownDetector ont atteint un pic vers 6h PDT, avec plus de 5 000 incidents avant de diminuer.

#### Cause Racine
La panne provenait d'un échec de résolution DNS affectant les endpoints de service DynamoDB dans us-east-1. DynamoDB, un service de base de données NoSQL, agit comme un "plan de contrôle" (control plane) critique pour de nombreuses fonctionnalités AWS — gérant les métadonnées, les sessions et le routage. Lorsque le DNS n'a pas pu résoudre ces endpoints, les APIs DynamoDB ont subi des latences et des erreurs accrues.

Ce problème initial a été résolu rapidement, mais il a déclenché une cascade :
- Les lancements d'instances EC2 ont échoué en raison de leur dépendance à DynamoDB pour le stockage des métadonnées.
- Un bogue sous-jacent dans le sous-système interne d'EC2 (responsable de la surveillance de la santé des NLB) a exacerbé les problèmes de connectivité réseau, entraînant des défaillances plus larges dans l'équilibrage de charge et les appels d'API.
- Les efforts de reprise ont impliqué une limitation de débit (ex. : restriction des lancements EC2 et des invocations Lambda) pour éviter la surcharge, mais les nouvelles tentatives des services dépendants ont amplifié la pression.

AWS a confirmé qu'il ne s'agissait pas d'une cyberattaque mais d'un dysfonctionnement lié à l'infrastructure, possiblement lié à une mise à jour défectueuse de la base de données DNS ou à une défaillance du système de sauvegarde. L'effet domino mondial s'est produit car us-east-1 héberge des plans de contrôle clés pour des services comme IAM et Lambda, même pour les ressources d'autres régions.

#### Services Affectés
Plus de 142 services AWS ont été impactés, principalement ceux dépendant de DynamoDB, EC2, ou des endpoints us-east-1. Catégories principales :

- **Bases de données & Stockage** : DynamoDB (principal), RDS, Redshift, SQS (arriérés).
- **Calcul & Orchestration** : EC2 (lancements), Lambda (invocations, interrogation), ECS, EKS, Glue.
- **Réseau & Équilibrage de charge** : Network Load Balancer (vérifications de santé), API Gateway.
- **Surveillance & Gestion** : CloudWatch, CloudTrail, EventBridge, IAM (mises à jour), AWS Config.
- **Autres** : Amazon Connect, Athena, et des fonctionnalités globales comme DynamoDB Global Tables.

Tous les services n'étaient pas complètement hors service — beaucoup ont connu des erreurs partielles ou des retards — mais la nature interconnectée a fait que même des problèmes mineurs se sont propagés.

#### Impacts
La panne a perturbé environ 1/3 des applications dépendantes d'Internet, affectant plus de 100 millions d'utilisateurs dans le monde. Exemples notables :
- **Réseaux sociaux & Médias** : Snapchat (échecs de connexion), Reddit (pannes), Twitch (problèmes de streaming).
- **Jeux vidéo** : Roblox (plantages de serveurs), Fortnite (échecs d'appariement).
- **Finance & Paiements** : Venmo, banques comme Lloyds (retards de transaction), HMRC (services fiscaux britanniques).
- **Commerce de détail & E-commerce** : Certaines parties du site de vente au détail d'Amazon lui-même ; enregistrement des compagnies aériennes (ex. : retards Delta, United).
- **Autres** : Appareils Alexa (défaillances vocales), Twilio (dysfonctionnements des communications).

Les estimations économiques évaluent les pertes à plus de 500 millions de dollars, avec une augmentation de 300 % des analyses de cybersécurité due à la panique des utilisateurs. Cela a souligné la centralisation d'Internet : us-east-1 traite environ 30 % du trafic AWS, ce qui en fait un point de fragilité unique malgré les conceptions multi-AZ.

#### Résolution et Enseignements Tirés
AWS a résolu le problème grâce à des atténuations ciblées : corrections DNS, correctifs du sous-système pour EC2/NLB et réductions progressives des limitations de débit. Après l'incident, ils ont conseillé :
- De réessayer les requêtes ayant échoué.
- De vider les caches DNS.
- De répartir les ressources sur plusieurs AZ/régions (ex. : via les Auto Scaling Groups).
- D'utiliser les quotas de service et la mise en cache (caching) pour amortir l'impact des nouvelles tentatives.

Les enseignements plus larges incluent le besoin d'une meilleure redondance dans les plans de contrôle, d'une détection d'anomalie pilotée par l'IA pour un triage plus rapide et de stratégies cloud diversifiées. AWS s'est engagé à fournir une analyse complète de la cause racine (RCA) aux clients, soulignant que de tels événements, bien que rares, révèlent les défis de mise à l'échelle à l'hyperscale.

Ce fut la panne la plus disruptive dans us-east-1 depuis 2021, mais la reprise a été plus rapide que les précédents historiques grâce aux outils automatisés.

#### Références
- [AWS Health Dashboard: Service Health - Oct 20, 2025](https://health.aws.amazon.com/health/status?eventID=arn:aws:health:us-east-1::event/MULTIPLE_SERVICES/AWS_MULTIPLE_SERVICES_OPERATIONAL_ISSUE/AWS_MULTIPLE_SERVICES_OPERATIONAL_ISSUE_BA540_514A652BE1A)
- [AWS Outage Analysis: October 20, 2025](https://www.thousandeyes.com/blog/aws-outage-analysis-october-20-2025)
- [Amazon's massive AWS outage points to a key weakness in the modern internet](https://finance.yahoo.com/news/amazons-massive-aws-outage-points-to-a-key-weakness-in-the-modern-internet-145418180.html)
- [What caused Amazon's AWS outage, and why did so many major apps go offline?](https://www.aljazeera.com/news/2025/10/21/what-caused-amazons-aws-outage-and-why-did-so-many-major-apps-go-offline)
- [AWS Outage on October 20: How a DNS Glitch in DynamoDB Disrupted the Internet](https://medium.com/@ansababy/aws-outage-on-october-20-how-a-dns-glitch-in-dynamodb-disrupted-the-internet-40e1f0440a12)
- [Update - AWS services operating normally](https://www.aboutamazon.com/news/aws/aws-service-disruptions-outage-update)
- [AWS was down — live updates following massive outage](https://www.tomsguide.com/news/live/amazon-outage-october-2025)