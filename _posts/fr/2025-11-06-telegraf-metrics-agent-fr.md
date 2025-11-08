---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: 'Telegraf : Agent de Collecte de Métriques Open Source'
translated: true
type: note
---

Telegraf est un agent open source, piloté par des plugins, développé par InfluxData pour collecter, traiter, agréger et écrire des métriques, des journaux et d'autres données de télémétrie provenant de diverses sources. Il est léger, s'exécute comme un binaire unique et prend en charge plus de 300 plugins d'entrée (par exemple, pour les statistiques système, les bases de données comme MySQL/PostgreSQL, les services cloud comme AWS et les applications comme Apache Kafka) et plus de 50 plugins de sortie (par exemple, vers InfluxDB, Prometheus, Kafka ou Elasticsearch).

### Fonctionnalités principales
- **Architecture basée sur un agent** : Se déploie facilement sur des serveurs, des conteneurs ou des appareils IoT sans dépendances lourdes.
- **Extensible via des plugins** : Écrit en Go, permettant de créer des plugins personnalisés si nécessaire.
- **Fait partie de la stack TICK** : S'intègre parfaitement avec InfluxDB pour le stockage de données de séries chronologiques, Chronograf pour la visualisation et Kapacitor pour les alertes.
- **Cas d'usage** : Couramment utilisé dans le domaine DevOps pour la surveillance de l'infrastructure, le suivi des performances des applications et l'ingestion de données de capteurs IoT.

Il est gratuit sous licence MIT et activement maintenu, la dernière version stable fin 2025 étant la v1.29.x. Pour la configuration, consultez la documentation officielle sur [telegraf.influxdata.com](https://docs.influxdata.com/telegraf/). Si ce n'est pas le Telegraf auquel vous pensiez (par exemple, une marque ou un terme dans un autre contexte), fournissez plus de détails !