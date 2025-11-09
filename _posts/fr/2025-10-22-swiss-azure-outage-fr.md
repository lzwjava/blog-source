---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Panne majeure d’Azure en Suisse Nord
translated: true
type: note
---

### Panne Azure dans la région Suisse Nord : 26-27 septembre 2025

Cet incident a été une perturbation majeure à l'échelle de la plateforme dans la région Suisse Nord, affectant plusieurs zones de disponibilité. Il a duré environ 22 heures, commençant à 23:54 UTC le 26 septembre et se résolvant complètement à 21:59 UTC le 27 septembre. Bien que la plupart des services aient été rétablis vers 04:00 UTC le 27 septembre, certains problèmes résiduels ont nécessité une intervention manuelle plus tard dans la journée.

#### Cause Racine
La panne provenait d'un changement de configuration planifié des certificats utilisés pour autoriser la communication dans l'infrastructure des équilibreurs de charge logiciels. L'un des nouveaux certificats avait une **valeur malformée** qui n'a pas été détectée lors de la validation. Ce changement a suivi un chemin de déploiement accéléré, qui l'a déployé de manière inattendue sur plusieurs zones sans déclencher les dispositifs de sécurité sanitaire. En conséquence :
- Les équilibreurs de charge ont perdu la connectivité avec les ressources de stockage et les nœuds.
- Les machines virtuelles affectées ont détecté des déconnexions de disque prolongées et se sont arrêtées automatiquement pour éviter la corruption des données.
- Cela s'est propagé aux services dépendants, amplifiant l'impact.

#### Services Affectés
La perturbation a touché un large éventail de services Azure hébergés en Suisse Nord, notamment :
- **Infrastructure de base** : Azure Storage, Azure Virtual Machines (VMs), Azure Virtual Machine Scale Sets (VMSS)
- **Bases de données** : Azure Cosmos DB, Azure SQL Database, Azure SQL Managed Instance, Azure Database for PostgreSQL
- **Calcul et applications** : Azure App Service, Azure API Management, Azure Kubernetes Service (AKS), Azure Databricks
- **Réseau et sécurité** : Azure Application Gateway, Azure Firewall, Azure Cache for Redis
- **Analytique et surveillance** : Azure Synapse Analytics, Azure Data Factory, Azure Stream Analytics, Azure Data Explorer, Azure Log Analytics, Microsoft Sentinel
- **Autres** : Azure Backup, Azure Batch, Azure Site Recovery, Azure Application Insights

Les services dépendant de ceux-ci (par exemple, les applications personnalisées) ont également été impactés, entraînant une indisponibilité généralisée ou une dégradation des performances.

#### Chronologie et Atténuation
- **23:54 UTC, 26 sep** : L'impact commence après le déploiement du changement de configuration.
- **00:08 UTC, 27 sep** : La surveillance automatisée détecte le problème.
- **00:12 UTC, 27 sep** : Début de l'enquête par les équipes Azure Storage et Networking.
- **02:33 UTC, 27 sep** : Annulation du changement de configuration.
- **03:40 UTC, 27 sep** : L'annulation du certificat est terminée.
- **04:00 UTC, 27 sep** : La majorité des services se rétablissent automatiquement ; des problèmes résiduels sont identifiés (par exemple, certaines machines virtuelles dans des états arrêtés/malsains en raison de conditions de concurrence ou de signaux d'arrêt mal interprétés).
- **06:19–14:15 UTC, 27 sep** : Développement et validation des scripts de récupération ; exécution de redémarrages ciblés pour les ressources affectées telles que les machines virtuelles SQL Managed Instance, les machines virtuelles Trusted Launch et les clusters Service Fabric.
- **16:15 UTC, 27 sep** : Récupération partielle pour les problèmes résiduels.
- **21:59 UTC, 27 sep** : Récupération complète confirmée après les validations finales.

La plupart des ressources se sont rétablies automatiquement après le rétablissement de la connectivité, mais des sous-ensembles (par exemple, les machines virtuelles avec des extensions personnalisées) ont nécessité des redémarrages manuels pour résoudre les problèmes de séquence de démarrage.

#### Enseignements Tirés et Améliorations
L'examen préliminaire de l'incident par Microsoft met en lumière des correctifs proactifs :
- Ajout d'audit aux systèmes de déploiement et suppression des pipelines accélérés risqués (terminé).
- Amélioration des mesures de sécurité avec des annulations automatiques (terminé).
- À venir : Une meilleure surveillance de l'intégrité des ressources (d'ici novembre 2025) et des processus de récupération résilients pour minimiser le travail manuel.

Cet événement souligne les risques liés aux changements de configuration dans une infrastructure partagée, mais la réponse d'Azure a limité la perte de données et a permis une récupération rapide et étendue.

[Historique des statuts Azure](https://azure.status.microsoft/en-us/status/history/)