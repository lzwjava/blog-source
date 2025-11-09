---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Pannes majeures d'AWS à travers l'histoire
translated: true
type: note
---

### Principales pannes dans l'histoire d'AWS

Amazon Web Services (AWS) alimente une grande partie d'Internet depuis 2006, mais comme toute infrastructure à grande échelle, elle a connu des perturbations occasionnelles. Les pannes sont peu fréquentes par rapport à ses vastes opérations, mais les plus importantes peuvent se répercuter sur les services dépendants, des médias sociaux aux plateformes financières. Le tableau ci-dessous résume les pannes historiques clés, en se concentrant sur les événements généralisés ou à fort impact. Elles sont tirées d'incidents documentés affectant plusieurs services ou des clients notables.

| Date               | Services/Régions affectés                     | Cause                                                          | Impact |
|--------------------|-----------------------------------------------|----------------------------------------------------------------|--------|
| 15 février 2008    | S3, EC2 (mondial)                             | Panne technique non spécifiée                                  | A perturbé le stockage d'images et l'hébergement pour divers sites web, marquant l'une des premières grandes pannes d'AWS. |
| 21 avril 2011      | Services multiples (US-East-1)                | Panne prolongée du centre de données                           | A mis hors service des sites très médiatisés comme Reddit et Quora pendant des heures, soulignant les préoccupations précoces concernant la fiabilité. |
| 28 février 2017    | EC2, S3, RDS et autres (US-East-1)            | Erreur humaine : commande mal saisie lors du débogage          | Panne de plusieurs heures ayant affecté Slack, Docker, Exora et d'autres ; pertes estimées à des centaines de millions de dollars ; le tableau de bord cloud d'AWS est également tombé en panne. |
| 7 décembre 2021    | Services du plan de contrôle incluant EC2, RDS, Lambda (US-East-1) | Bug logiciel dans le plan de contrôle lors du basculement, entraînant des défaillances en cascade | Panne la plus longue de l'histoire récente (8+ heures) ; a perturbé Netflix, Disney+, Capital One et des sites gouvernementaux ; une seconde panne plus petite le 15 décembre a affecté des services similaires. |
| 13 juin 2023       | EC2 et services associés (régions multiples)  | Problèmes régionaux non spécifiés                              | Temps d'arrêt étendu ayant touché des organes de presse (par exemple, Associated Press, Boston Globe) et des systèmes de transport (NY MTA), durant plusieurs heures. |
| 20 octobre 2025    | Points de terminaison DynamoDB, lancements EC2 et services multiples (US-East-1, avec répercussions mondiales) | Échec de résolution DNS pour les points de terminaison de service DynamoDB | Perturbation d'une journée (débutant tard le 19 octobre PDT, résolue dans l'après-midi du 20 octobre) ; a impacté Snapchat, Reddit, Roblox, Fortnite, des banques (par exemple, Lloyds) et HMRC ; a affecté des millions d'utilisateurs en bloquant l'accès à environ 1/3 des applications dépendantes d'Internet ; AWS a limité certaines opérations pour la récupération. |

Ces incidents résultent souvent d'erreurs humaines, de problèmes de réseau ou de facteurs environnementaux, et AWS a amélioré sa résilience grâce à des redondances comme les configurations multi-régions. La panne de 2025 souligne les risques persistants d'une dépendance excessive à US-East-1, la région la plus active d'AWS.

Pour plus de détails :
- [A History of AWS Cloud and Data Center Outages](https://www.datacenterknowledge.com/outages/a-history-of-aws-cloud-and-data-center-outages)
- [The Biggest AWS Outage in History: December 7, 2021](https://aws.plainenglish.io/the-biggest-aws-outage-in-history-the-december-7-2021-us-east-1-meltdown-and-lessons-learned-2efab5a02de5)
- [What caused the AWS outage](https://www.bbc.com/news/articles/cev1en9077ro)
- [AWS Update on October 2025 Outage](https://www.aboutamazon.com/news/aws/aws-service-disruptions-outage-update)