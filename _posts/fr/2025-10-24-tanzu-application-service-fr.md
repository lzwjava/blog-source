---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Présentation de VMware Tanzu Application Service
translated: true
type: note
---

## Introduction à VMware Tanzu Application Service for VMs (TAS for VMs)

VMware Tanzu Application Service for VMs (TAS for VMs) est une plateforme en tant que service (PaaS) commerciale construite sur le projet open-source Cloud Foundry. Elle est conçue pour simplifier le déploiement, la mise à l'échelle et la gestion d'applications cloud-natives, permettant aux développeurs de se concentrer sur l'écriture du code plutôt que sur la gestion de l'infrastructure. TAS for VMs permet un déploiement rapide des applications dans divers environnements, y compris sur site (comme vSphere) ou dans des clouds publics (AWS, Azure, GCP, OpenStack), et prend en charge à la fois les configurations auto-gérées et les fournisseurs commerciaux certifiés.

### Fonctionnalités Clés
- **Fondation Open-Source** : Tire parti de l'extensibilité de Cloud Foundry pour éviter le verrouillage fournisseur, en prenant en charge de multiples langages, frameworks et services.
- **Déploiement Automatisé** : Poussez les applications en utilisant des outils familiers (par exemple, CLI) sans modifier le code ; les applications sont empaquetées en "droplets" (bundles pré-compilés) pour un staging et une exécution rapides.
- **Évolutivité et Résilience** : Utilise Diego pour une distribution intelligente de la charge sur les machines virtuelles, la mise à l'échelle automatique et la tolérance aux pannes pour gérer les pics de trafic ou les défaillances.
- **Gestion des Utilisateurs** : Organise les équipes en "organisations" et "espaces" avec un accès basé sur les rôles (par exemple, admin, développeur) via les serveurs UAA (User Account and Authentication).
- **Intégration de Services** : Liez facilement les applications à des services comme des bases de données ou des API via des Service Brokers, sans modifier le code de l'application.
- **Surveillance et Journalisation** : Agrège les logs et les métriques via Loggregator dans un flux "Firehose" pour l'analyse en temps réel, l'alerte et l'intégration avec des outils.
- **Option d'Empreinte Réduite** : Une version légère qui s'exécute sur seulement 4 machines virtuelles (contre 13+ pour la version standard), idéale pour les petites équipes ou les tests, bien qu'avec certaines limitations d'échelle.
- **Infrastructure Flexible** : Déployée via BOSH (un outil d'automatisation) et gérée avec Tanzu Operations Manager pour une configuration rationalisée.

### Avantages
TAS for VMs accélère le time-to-market en permettant aux applications d'être mises en ligne en quelques minutes, avec une mise à l'échelle automatique et une accessibilité globale. Il réduit la surcharge liée à l'infrastructure, améliore la sécurité grâce à des espaces de travail compartimentés et favorise la portabilité — les applications s'exécutent de manière cohérente dans tous les environnements. En abstraisant la gestion des machines virtuelles, il réduit les coûts et la complexité, tandis que la communauté Cloud Foundry garantit une innovation et un support continus.

### Fonctionnement
Fondamentalement, TAS for VMs agit comme un PaaS multi-locataire :
1. **Déploiement** : Utilisez Tanzu Operations Manager pour configurer et déployer la plateforme sur des machines virtuelles gérées par BOSH.
2. **Cycle de Vie de l'Application** : Les développeurs poussent le code via la CLI ; le Cloud Controller le met en stage avec des buildpacks (pour la configuration spécifique au langage) dans des droplets, puis Diego met aux enchères et exécute les instances sur les machines virtuelles hôtes.
3. **Routage et Accès** : Gorouter gère le trafic entrant, équilibré en charge de manière externe ; UAA authentifie les utilisateurs.
4. **Opérations** : Les composants internes communiquent via la messagerie NATS et BOSH DNS ; les ressources comme les blobs et les configurations sont stockées dans GitHub, des blobstores ou MySQL.

TAS for VMs étend le Cloud Foundry open-source avec les fonctionnalités, le support et les certifications de niveau entreprise de VMware, ce qui en fait un choix robuste pour les charges de travail de production.

Pour plus de détails, consultez la documentation officielle : [Aperçu de TAS for VMs](https://techdocs.broadcom.com/us/en/vmware-tanzu/platform/tanzu-platform-for-cloud-foundry/6-0/tpcf/concepts-overview.html)