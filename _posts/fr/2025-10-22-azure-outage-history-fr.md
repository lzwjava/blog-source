---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Principales pannes Azure à travers l&#39;histoire
translated: true
type: note
---

Microsoft Azure, lancé en 2010, a connu plusieurs pannes importantes au fil des années, souvent dues à des erreurs de configuration, des défaillances matérielles ou des événements externes comme des intempéries. Vous trouverez ci-dessous un résumé chronologique des plus notables, en se concentrant sur celles ayant eu un impact étendu sur plusieurs régions ou services. Cette liste s'appuie sur des rapports officiels, des analyses historiques et des revues d'incidents, en indiquant les dates, les causes, les zones touchées et les durées lorsque disponibles.

| Date | Cause | Régions/Services affectés | Durée/Impact |
|------|-------|---------------------------|-----------------|
| 29 février 2012 | Bug de calcul d'année bissextile dans le code | Amérique du Nord (Azure Compute) | ~8 heures ; gestion des applications et services perturbée pour les utilisateurs. |
| 26 juillet 2012 | Périphérique réseau mal configuré | Europe de l'Ouest (Azure Compute) | >2 heures ; indisponibilité partielle en Europe. |
| 22 février 2013 | Certificat SSL expiré | Global (Azure Storage) | Plusieurs heures ; crédits de service accordés ; a également touché Xbox Live, Music et Video. |
| 30 octobre 2013 | Panne partielle de calcul (problème de throttling) | Mondial (Azure Compute, fonctions de gestion) | ~3-4 heures ; a affecté les téléchargements de fichiers et la gestion des sites. |
| 22 novembre 2013 | Problèmes de stockage et de réseau | Centre-Nord des États-Unis (Xbox Live) | Plusieurs heures le jour du lancement de la Xbox One ; faible impact client mais forte visibilité. |
| 19 novembre 2014 | Changement de configuration provoquant une boucle infinie dans le stockage Blob | Global (20+ services, dont Azure Storage) | ~6-10 heures ; capacité réduite dans plusieurs régions ; a impacté Xbox Live, MSN et Visual Studio Online. |
| 15 septembre 2016 | Panne DNS globale | Mondial (Azure DNS) | ~2 heures ; perturbations importantes des services. |
| 7 et 23 mars 2017 | Incidents multiples (réseau et stockage) | Global (Office 365, Skype, Xbox Live) | Jusqu'à 16+ heures chacun ; problèmes d'accès généralisés pour les utilisateurs. |
| 29 septembre 2017 | Déclenchement d'arrêts dû au dégagement de gaz d'extinction d'incendie lors d'une maintenance | Régions des États-Unis (divers services) | ~7 heures ; dysfonctionnements intermittents. |
| 4 septembre 2018 | Coup de foudre provoquant une surtension et une défaillance du refroidissement | Centre-Sud des États-Unis, multiples régions (40+ services) | >25 heures, certains effets jusqu'à 3 jours ; temps d'arrêt majeur pour de nombreux services. |
| 25 janvier 2020 | Défaillance d'une dépendance backend dans Azure SQL Database | Global (presque toutes les régions, y compris US Gov/DoD) | ~6 heures ; a touché SQL DB, Application Gateway, Bastion et Firewall. |
| 1 avril 2021 | Problème DNS étendu dans l'infrastructure réseau | Global (États-Unis, Europe, Asie, etc.) | ~1,5 heure ; a affecté les services dépendants du réseau principal. |
| 1 juin 2022 | Problèmes avec les journaux de connexion Azure Active Directory | Global (multiples régions) | ~9,5 heures ; a impacté AAD, Sentinel, Monitor et Resource Manager. |
| 29 juin 2022 | Instabilité backend non spécifiée | Global (des dizaines de régions) | ~24 heures par intermittence ; a affecté Firewall, Synapse, Backup, et plus. |
| 25 janvier 2023 | Commande de routeur défectueuse provoquant une perturbation réseau | Global (25+ régions, dont East US, West Europe) | ~3,5 heures ; latence et échecs dans M365 (Teams, Outlook), SharePoint et Office 365. |
| 9 juin 2023 | Attaque DDoS revendiquée par Anonymous Sudan | Global (Portail Azure et services cloud) | ~2,5 heures ; portail et services associés indisponibles. |
| 13 novembre 2024 | Échecs de résolution DNS pour Storage | Multiple (East US/2, Central US, West US/2, etc.) | ~8,5 heures ; a impacté Databricks et les comptes de stockage. |
| 26 décembre 2024 | Incident électrique dans une Zone de Disponibilité | Centre-Sud des États-Unis (Zone 03) | ~18 heures ; a touché Storage, les machines virtuelles, Cosmos DB, SQL DB, et plus. |
| 9 janvier 2025 | Panne réseau | East US 2 | >48 heures ; a affecté Databricks, Synapse, Functions, App Service et les machines virtuelles. |
| 10 septembre 2025 | Surcharge du service d'allocation due à un changement de throttling | East US 2 (Zones 02/03) | ~10,5 heures ; dégradation des opérations sur les machines virtuelles, impactant Backup, Batch, Kubernetes et Synapse. |
| 26-27 septembre 2025 | Valeur de certificat malformée dans un changement de configuration | Suisse Nord (multiples zones) | ~22 heures ; pannes généralisées dans API Management, App Service, Cosmos DB, les machines virtuelles et Sentinel. |
| 9 octobre 2025 | Défaut du plan de contrôle Azure Front Door | Europe et Afrique | ~8 heures ; latence/timeouts dans les portails et services (jusqu'à 17% de taux d'échec en Afrique). |
| 9 octobre 2025 | Suppression de configuration consécutive par des scripts d'automatisation | Global (portails de gestion) | ~4 heures ; problèmes d'accès au Portail Azure et autres suite à l'incident AFD. |

Ces incidents représentent une fraction des événements totaux mais sont les plus perturbateurs en termes d'étendue et de durée. Microsoft publie généralement des revues post-incident (PIR) pour en tirer des enseignements, et la disponibilité s'est améliorée au fil du temps, avec des SLA visant 99,99 % de temps de fonctionnement.

## Références
- [A History of Microsoft Azure Outages](https://www.datacenterknowledge.com/outages/a-history-of-microsoft-azure-outages)
- [Microsoft Azure Outage History Overview](https://statusgator.com/blog/azure-outage-history/)
- [Azure Status History](https://azure.status.microsoft/en-us/status/history/)
- [Microsoft Azure Wikipedia - Outages Section](https://en.wikipedia.org/wiki/Microsoft_Azure#Outages)