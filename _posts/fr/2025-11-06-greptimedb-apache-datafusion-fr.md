---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: GreptimeDB S'appuie sur Apache DataFusion
translated: true
type: note
---

GreptimeDB, une base de données open-source cloud-native pour les séries temporelles conçue pour les données d'observabilité (comme les métriques, les logs et les traces), s'appuie sur Apache DataFusion comme dépendance centrale car son moteur de requêtes est fondamentalement construit sur DataFusion. DataFusion est un framework de planification, d'optimisation et d'exécution de requêtes performant et extensible, écrit en Rust, qui tire parti du format de données en colonnes en mémoire d'Apache Arrow pour un traitement efficace.

### Raisons principales de cette dépendance :
- **Performance et Efficacité** : DataFusion permet une exécution rapide des requêtes en utilisant le modèle de données zero-copy d'Arrow, ce qui minimise la surcharge de sérialisation et prend en charge les opérations vectorielles. Ceci est crucial pour traiter des volumes massifs de données de séries temporelles dans GreptimeDB sans compromettre la vitesse.
  
- **Extensibilité et Personnalisation** : GreptimeDB étend DataFusion pour ajouter des fonctionnalités spécifiques aux séries temporelles, telles que :
  - La prise en charge de PromQL (Prometheus Query Language) comme dialecte pour les requêtes d'observabilité.
  - Une syntaxe SQL améliorée adaptée aux charges de travail des séries temporelles.
  - L'intégration avec des index secondaires externes pour des recherches plus rapides.
  - Des règles d'optimisation spécifiques au domaine qui s'appliquent à diverses étapes de la requête (par exemple, la planification, la réécriture et l'exécution).

- **Architecture Modulaire** : DataFusion agit comme un framework flexible qui permet à GreptimeDB de gérer les requêtes à travers ses composants distribués (par exemple, en séparant le calcul du stockage). Cette modularité aide à construire des plans de requêtes personnalisés optimisés pour différents scénarios, comme l'analyse en temps réel ou les agrégations historiques.

- **Compatibilité avec l'Écosystème** : En héritant des fonctions intégrées de DataFusion (scalaires, de fenêtrage, de tableaux, etc.), GreptimeDB bénéficie d'un riche ensemble de capacités SQL prêtes à l'emploi, réduisant ainsi l'effort de développement tout en garantissant la compatibilité avec des écosystèmes de données plus larges comme Apache Arrow.

Sans DataFusion, GreptimeDB devrait réimplémenter un moteur de requêtes complet à partir de zéro, ce qui serait coûteux en ressources et plus difficile à maintenir. Au lieu de cela, cette dépendance accélère le développement et offre des performances de requêtes de qualité production.

[L'ingénieur de Greptime Ruihang Xia a présenté au séminaire CMUDB — Pratiques des bases de données Apache DataFusion](https://greptime.com/blogs/2024-12-19-apache-datafusion-database-practices)  
[Fonctions | Documentation GreptimeDB](https://docs.greptime.com/reference/sql/functions/overview/)