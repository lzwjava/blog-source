---
audio: false
generated: true
lang: fr
layout: post
title: Défis de TiDB et alternatives pour 2025
translated: true
type: note
---

Les défis de conception de TiDB découlent de la tentative de mettre en œuvre les concepts de Google Spanner et F1 sans le matériel spécialisé qui les rend pratiques. Voici les problèmes clés :

## Problèmes de conception fondamentaux

**Dépendance matérielle** : TiDB utilise « l'allocateur d'horodatage introduit dans Percolator », mais « s'il y a plusieurs datacenters, surtout s'ils sont géographiquement distribués, la latence est très élevée » car il lui manque le matériel spécialisé d'horloge atomique de Google (TrueTime) qui rend la conception de Spanner efficace.

**Surcharge des ressources** : La nature distribuée de TiDB nécessite plus de ressources par rapport aux bases de données relationnelles traditionnelles, nécessitant plusieurs composants (serveurs TiDB, serveurs PD, nœuds TiKV) sur des machines séparées, ce qui augmente les coûts matériels et opérationnels.

**Complexité opérationnelle** : Il est difficile de résoudre les problèmes dans une base de données distribuée car les informations sur le système sont dispersées sur différentes machines.

## Ce que les gens utilisent à la place en 2025

D'après les résultats de recherche, les organisations choisissent plusieurs alternatives :

**Solutions Cloud-Native** : Beaucoup migrent vers des services entièrement managés comme Google Cloud SQL, Amazon Aurora et d'autres services de base de données cloud qui gèrent la complexité opérationnelle.

**Cas d'utilisation spécialisés** : Certaines entreprises comme Plaid étaient encore en transition vers TiDB mi-2025, mais elles faisaient face à des défis de migration importants, notamment la suppression des clés étrangères et l'application de clés primaires pour la compatibilité.

**Approches traditionnelles de partitionnement** : De nombreuses organisations reviennent à des stratégies éprouvées de partitionnement MySQL/PostgreSQL avec de meilleurs outils plutôt que de gérer la complexité du SQL distribué.

**Alternatives modernes** : Les entreprises explorent d'autres bases de données distribuées comme CockroachDB, YugabyteDB, ou des solutions sur mesure qui n'essaient pas de reproduire l'architecture de Spanner sans sa fondation matérielle.

Le problème fondamental est que TiDB a tenté de recréer les avantages de Spanner sans l'infrastructure spécialisée de Google, conduisant à une latence plus élevée, une complexité accrue et une surcharge opérationnelle qui surpassent souvent les avantages de la mise à l'échelle pour la plupart des cas d'utilisation.