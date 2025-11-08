---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Base de données de séries temporelles distribuée OpenTSDB
translated: true
type: note
---

OpenTSDB est une base de données de séries temporelles (TSDB) open source, distribuée et évolutive, conçue pour stocker, indexer et interroger de grands volumes de données numériques horodatées, telles que les métriques des systèmes de surveillance. Elle a été initialement développée par Benoit Sigoure chez StumbleUpon (maintenant une partie d'eBay) pour gérer des ensembles de données massifs sans perdre la granularité des données, et elle est construite sur Apache HBase pour son stockage backend, tirant parti de la nature distribuée de HBase pour une mise à l'échelle horizontale sur les clusters.

### Fonctionnalités principales
- **Évolutivité** : Peut gérer des milliards de points de données par jour en répartissant les données sur plusieurs nœuds, sans point de défaillance unique.
- **Modèle de données** : Stocke les données sous forme de paires clé-valeur où les clés incluent un horodatage, un nom de métrique et des tags (par exemple, pour la catégorisation comme "cpu.usage" avec des tags pour l'hôte et la région). Cela permet une interrogation flexible sans schémas prédéfinis.
- **Composants** :
  - **Time Series Daemon (TSD)** : Le serveur principal qui gère l'ingestion, l'interrogation et les interactions via l'API HTTP.
  - Outils en ligne de commande pour l'import/export de données et l'administration.
- **Interrogation** : Prend en charge des requêtes de type SQL via son API, avec des fonctions d'agrégation (par exemple, somme, moyenne) sur des plages de temps. Elle s'intègre avec des outils de visualisation comme Grafana.
- **Cas d'usage** : Principalement pour la surveillance et l'observabilité dans les domaines du DevOps, de l'IoT, de la finance et du suivi des performances, où des taux d'ingestion élevés et une rétention à long terme sont critiques.

Elle est légère, ne nécessitant aucun moteur de stockage personnalisé, et reste activement maintenue sur GitHub. Bien que puissante pour les environnements big data, elle peut nécessiter une expertise HBase pour la configuration et peut être gourmande en ressources pour les déploiements plus petits.

### Références
- [Site officiel d'OpenTSDB](https://opentsdb.net/)
- [Dépôt GitHub](https://github.com/OpenTSDB/opentsdb)
- [Comprendre OpenTSDB sur Medium](https://medium.com/analytics-vidhya/understanding-opentsdb-a-distributed-and-scalable-time-series-database-e4efc7a3dbb7)