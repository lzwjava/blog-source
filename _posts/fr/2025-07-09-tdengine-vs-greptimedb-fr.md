---
audio: false
generated: true
lang: fr
layout: post
title: 'TDengine contre GreptimeDB : Les Rivales des Séries Temporelles'
translated: true
type: note
---

Oui, TDengine et GreptimeDB sont définitivement des concurrents dans le domaine des bases de données de séries temporelles. Les deux se positionnent comme des bases de données de séries temporelles open source et hautes performances, avec des cas d'utilisation cibles similaires.

**Domaines clés de concurrence :**

1.  **Revendications de performance** : Les deux bases de données présentent des revendications de performance solides dans leurs benchmarks. TDengine affirme qu'elle "consomme 26,9 fois moins d'espace disque que TimescaleDB, et 4,5 fois moins qu'InfluxDB" et qu'elle "a le temps de réponse aux requêtes le plus rapide dans tous les scénarios". De même, GreptimeDB affirme que son "débit d'écriture est plus de 2 fois supérieur à celui d'InfluxDB" et qu'il "montre des avantages significatifs en performance de requête lors du traitement de grands ensembles de données".

2.  **Marchés cibles** : TDengine se concentre sur la comparaison avec d'autres bases de données de séries temporelles majeures comme InfluxDB, TimescaleDB, Prometheus, OpenTSDB et QuestDB, tandis que GreptimeDB se positionne comme une "base de données d'observabilité unifiée et économique pour les métriques, les logs et les traces".

3.  **Concurrence sur les benchmarks** : Les deux bases de données apparaissent dans les benchmarks de bases de données de séries temporelles, TDengine étant parmi les fournisseurs qui "se sont montrés comme les plus rapides à l'ingestion".

**Différences clés :**

-   **Focus** : TDengine semble plus axé sur les cas d'utilisation traditionnels des séries temporelles et les scénarios IoT, tandis que GreptimeDB met l'accent sur l'observabilité unifiée (métriques, logs, traces) dans une seule base de données.
-   **Architecture** : TDengine souligne son "utilisation approfondie des caractéristiques des données de séries temporelles telles que la nature structurée, l'absence de transactions, les suppressions ou mises à jour peu fréquentes, et une charge de travail lourde en écriture, légère en lecture".
-   **Stockage** : Le coût de stockage de GreptimeDB est noté comme étant "nettement inférieur à celui d'Elasticsearch, la taille des données persistées n'étant que 50 % de celle de ClickHouse".

Les deux bases de données sont en concurrence directe avec les mêmes acteurs établis (InfluxDB, TimescaleDB, ClickHouse) et ciblent des charges de travail de séries temporelles similaires, sensibles à la performance, ce qui en fait des concurrents évidents dans ce domaine.