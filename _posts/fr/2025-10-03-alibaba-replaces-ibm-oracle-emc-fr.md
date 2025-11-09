---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Alibaba Remplace IBM Oracle EMC
translated: true
type: note
---

### L'initiative « Remove IOE » d'Alibaba

La campagne « Remove IOE » (ou « 去IOE ») d'Alibaba, lancée vers 2008-2009, était un effort stratégique pour éliminer la dépendance aux piles logicielles propriétaires des fournisseurs **IBM**, **Oracle** et **EMC** (acronyme IOE). L'objectif était de réduire les coûts, d'améliorer l'évolutivité et de favoriser l'innovation en passant à des technologies open source et développées en interne. Cela était crucial pour la croissance du commerce électronique d'Alibaba, car les systèmes IOE étaient coûteux et moins flexibles pour une mise à l'échelle massive.

#### Ce qui a été supprimé : La pile IOE
Le terme « IOE » désignait une pile d'entreprise haut de gamme, étroitement intégrée et dominée par ces fournisseurs. Voici une répartition des composants clés qu'Alibaba a progressivement abandonnés :

1. **IBM (Matériel et Middleware)** :
   - **Principaux composants supprimés** :
     - Mainframes IBM (par exemple, zSeries ou System z) et serveurs haut de gamme comme les Power Systems.
     - Le système d'exploitation AIX d'IBM (variante Unix propriétaire).
     - IBM WebSphere (serveur d'applications/middleware pour les applications Java).
     - La base de données IBM DB2 dans certains cas (bien qu'Oracle était la cible principale pour les bases de données).
   - **Pourquoi les a-t-on supprimés ?** Le matériel IBM était fiable mais coûteux, créait un fort verrouillage vendor et n'était pas optimisé pour une mise à l'échelle horizontale de type cloud. Alibaba l'a remplacé par du matériel x86 standard moins cher (par exemple, des serveurs Intel/AMD exécutant Linux).

2. **Oracle (Base de données)** :
   - **Principaux composants supprimés** :
     - Oracle Database (base de données relationnelle d'entreprise, par exemple, Oracle 10g/11g RAC pour la haute disponibilité).
     - Les middlewares Oracle comme Oracle Fusion Middleware ou WebLogic Server.
   - **Pourquoi les a-t-on supprimés ?** Les frais de licence étaient exorbitants (évoluant avec les cœurs de CPU et les utilisateurs), et ce n'était pas idéal pour les énormes charges de travail de lecture/écriture d'Alibaba (par exemple, les pics de transactions sur Taobao). La nature propriétaire d'Oracle limitait la personnalisation.

3. **EMC (Stockage)** :
   - **Principaux composants supprimés** :
     - Les baies de stockage EMC Symmetrix ou Clariion (systèmes de stockage d'entreprise SAN/NAS).
   - **Pourquoi les a-t-on supprimés ?** Un stockage propriétaire coûteux avec verrouillage vendor ; difficile à mettre à l'échelle de manière linéaire pour des données au niveau du pétaoctet dans le commerce électronique.

La pile IOE globale était un écosystème « fermé » : des serveurs IBM exécutant AIX, la base de données Oracle par-dessus, stockée sur des baies EMC, avec le middleware IBM liant le tout. Cela était courant dans les entreprises traditionnelles mais constituait un goulot d'étranglement pour les besoins d'Alibaba.

#### Ce qui a remplacé la pile IOE
Alibaba a tout reconstruit sur des fondations open source, du matériel standard et des développements personnalisés. Principaux remplacements :

- **Couche Matériel/OS (Remplacement d'IBM)** :
  - Serveurs x86 standard (par exemple, de Dell, HP ou construits sur mesure).
  - Distributions Linux (initialement CentOS/RHEL ; plus tard, ALINUX propre à Alibaba Cloud).
  - Outils d'orchestration internes pour la gestion de clusters.

- **Couche Base de données (Remplacement d'Oracle)** :
  - **Début Open Source** : MySQL (Alibaba a beaucoup contribué ; c'est maintenant un fork de MySQL 5.5/5.6 avec des correctifs AliSQL pour la haute concurrence).
  - **Développements personnalisés** :
    - **OceanBase** : La base de données relationnelle distribuée d'Alibaba (NewSQL), conçue pour une fiabilité de niveau financier (prend en charge les transactions ACID à grande échelle). Elle est maintenant open source et utilisée dans Alipay d'Ant Group.
    - Tair/DRDS : Mise en cache mémoire (comme Redis) et partitionnement SQL distribué pour la mise à l'échelle horizontale.
  - Cela a permis de traiter des milliards de requêtes quotidiennes sans les coûts de licence d'Oracle.

- **Couche Stockage (Remplacement d'EMC)** :
  - Stockage distribué basé sur Ceph ou HDFS.
  - PolarFS d'Alibaba ou stockage par blocs/objets personnalisé sur des disques standard.
  - A évolué plus tard vers OSS (Object Storage Service) et EBS (Elastic Block Store) d'Alibaba Cloud.

- **Couche Middleware/Application** :
  - HSF (High-Speed Service Framework) pour les microservices (remplaçant WebSphere).
  - Apache Dubbo pour la découverte de services RPC.
  - Outils internes comme SOFA (Scalable Open Framework Architecture).

#### Impact et Héritage
- **Réduction des coûts** : Réduction initiale de 70 à 80 % des coûts matériels et de base de données.
- **Évolutivité** : A permis à Alibaba de gérer les pics du Double 11 (Jour des célibataires) (par exemple, plus de 500 000 commandes/seconde).
- **Innovation** : A stimulé l'activité cloud d'Alibaba (Alibaba Cloud, désormais la plus grande au monde selon certaines métriques) et les contributions open source (par exemple, OceanBase est utilisé par des banques dans le monde entier).
- **Calendrier** : Transition entièrement achevée vers 2012-2015 ; « Remove IOE » est devenu un mantra pour les entreprises technologiques chinoises.

Si vous avez des questions sur des points spécifiques (par exemple, les défis de migration ou la pile technique actuelle d'Alibaba), faites-le moi savoir pour plus de détails ! Sources : Blogs officiels d'Alibaba, discours de Jack Ma et rapports techniques de cette époque.