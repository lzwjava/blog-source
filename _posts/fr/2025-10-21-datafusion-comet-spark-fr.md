---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Apache DataFusion Comet Accélère Spark
translated: true
type: note
---

### Apache DataFusion Comet

Apache DataFusion Comet est un projet open source de la Fondation Apache Software qui sert d'accélérateur haute performance pour Apache Spark. Il est construit sur le moteur de requête Apache DataFusion et vise à améliorer les performances des charges de travail Spark—comme un traitement des données plus rapide et des insights plus précoces—tout en fonctionnant sur du matériel standard. Aucune modification de code n'est nécessaire pour l'intégration, et il accélère également les opérations Apache Iceberg impliquant des scans Parquet depuis Spark.

#### Fonctionnalités principales
- **Gains de performance** : Offre des accélérations significatives pour les requêtes. Par exemple, des benchmarks sur 22 requêtes TPC-H contre 100 Go de données Parquet montrent une amélioration globale de 2,2x (passant de 687 secondes à 302 secondes sur un seul exécuteur 8 cœurs). Des benchmarks TPC-DS sont également disponibles, avec des résultats reproductibles via les guides du projet.
- **Efficacité matérielle** : Fonctionne avec du matériel standard, évitant le besoin de GPU ou FPGA coûteux.
- **Compatibilité transparente** : Entièrement compatible avec les versions prises en charge d'Apache Spark, garantissant une intégration directe dans les configurations existantes.
- **Intégration étroite avec DataFusion** : Tire parti du moteur d'exécution de DataFusion pour une efficacité optimisée.
- **Piloté par la communauté** : Sous licence Apache License 2.0, avec une communauté active pour les contributions, y compris les corrections de bogues, les fonctionnalités et la documentation.

Le projet est activement maintenu, avec des ressources pour bien démarrer, des guides pour les contributeurs et des canaux communautaires comme Slack et Discord.

Pour plus de détails, y compris l'installation (via la documentation sur datafusion.apache.org) et le benchmarking, consultez le dépôt.

[Dépôt GitHub d'Apache DataFusion Comet](https://github.com/apache/datafusion-comet)