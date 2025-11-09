---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Le Potentiel de Rust pour le Big Data
translated: true
type: note
---

### Rust pour le Big Data (#rust2018)

**Auteur :** Andy Grove
**Publié le :** 28 janvier 2018

Cet article de blog est une réflexion prospective écrite dans le cadre de l'initiative "#rust2018", où l'auteur partage sa vision du rôle de Rust pour l'année à venir. Andy Grove, un développeur qui construit des systèmes de traitement de données distribués avec Apache Spark, soutient que Rust a un potentiel inexploité pour révolutionner le traitement du big data grâce à ses atouts fondamentaux en matière de sécurité mémoire, de performances et de prévisibilité—sans les écueils du ramasse-miettes ou des surcoûts d'exécution courants dans des langages comme Java.

#### Arguments clés pour Rust dans le Big Data
Grove commence par raconter son parcours avec Rust : présenté par un collègue il y a quelques années et conquis après avoir assisté à la RustConf en 2016. Il loue la capacité de Rust à éliminer les vulnérabilités de sécurité courantes comme les débordements de mémoire tampon tout en offrant une vitesse comparable au C. Pour le développement côté serveur, il met en avant les crates comme *futures* et *tokio* pour construire des applications asynchrones et évolutives. Mais sa véritable passion est le big data, où Rust pourrait résoudre les points sensibles des outils existants.

Dans son travail quotidien, Grove utilise Apache Spark, qui est devenu la solution de référence pour le traitement distribué des données mais a commencé comme un simple projet académique et a grandi grâce à des correctifs techniques héroïques. Les premières versions de Spark rencontraient des difficultés avec :
- **La surcharge de la sérialisation Java** : Le brassage des données entre les nœuds était lent et gourmand en mémoire.
- **Les pauses du ramasse-miettes (GC)** : Elles causaient des performances imprévisibles, conduisant à des erreurs "OutOfMemory" qui nécessitaient un réglage constant.

Le "Project Tungsten" de Spark (lancé vers 2014) a atténué ce problème en :
- Stockant les données hors du tas (off-heap) dans des formats binaires (par exemple, colonnaire comme Parquet) pour contourner le GC.
- Utilisant la génération de code en une seule étape (whole-stage code generation) pour optimiser l'exécution CPU via le bytecode.

Ces changements ont déplacé les goulots d'étranglement des particularités de la JVM vers les limites brutes du CPU, prouvant que les gains de performance proviennent de l'efficacité bas niveau plutôt que des abstractions de plus haut niveau.

L'hypothèse audacieuse de Grove : Si Spark avait été construit en Rust dès le départ, même une implémentation basique aurait assuré performance et fiabilité immédiatement. Le modèle de propriété de Rust garantit la sécurité mémoire sans GC, évitant ainsi l'encombrement de la sérialisation et les pauses erratiques. Finis les réglages fastidieux des paramètres JVM—juste une exécution rapide et prévisible. Il y voit une "opportunité unique" pour Rust de surpasser les solutions établies comme Spark, surtout à mesure que les volumes de données explosent.

#### Le projet DataFusion
Pour concrétiser cette vision, Grove a lancé **DataFusion**, un prototype de moteur de requête open-source en Rust. Au moment de la rédaction (début 2018), il est en version alpha mais démontre déjà :
- Une **API DataFrame** pour charger des fichiers Parquet et exécuter des opérations comme des filtres, des jointures et des agrégations (exemple : [parquet_dataframe.rs](https://github.com/andygrove/datafusion/blob/master/examples/parquet_dataframe.rs)).
- Une **API SQL** pour des requêtes déclaratives sur les mêmes données (exemple : [parquet_sql.rs](https://github.com/andygrove/datafusion/blob/master/examples/parquet_sql.rs)).

Il prévoit de travailler dessus pendant son temps libre tout au long de 2018 pour perfectionner ses compétences en Rust et construire quelque chose d'utile. Invitant la communauté à contribuer, il renvoie vers le dépôt : [github.com/apache/arrow-datafusion](https://github.com/apache/arrow-datafusion).

#### Mises à jour (en mai 2024)
L'article inclut un addendum rétrospectif mettant en lumière la croissance de DataFusion :
- Donné à Apache Arrow en février 2019.
- Ballista (couche d'exécution distribuée) annoncé en juillet 2019 : [Announcing Ballista](https://andygrove.io/2019/07/announcing-ballista/).
- Livre auto-édité *How Query Engines Work* (fév. 2020) démystifiant les internes de DataFusion/Ballista : [Lien Leanpub](https://leanpub.com/how-query-engines-work).
- Ballista donné à Apache Arrow en avril 2021.
- Apple a donné **DataFusion Comet** (mars 2024) pour booster Spark avec une accélération basée sur Rust : [Blog Arrow](https://arrow.apache.org/blog/2024/03/06/comet-donation/) et [GitHub](https://github.com/apache/datafusion-comet).
- Grove a rejoint Apple en avril 2024 pour travailler sur Comet.
- DataFusion est devenu un projet de premier niveau (Top-Level Project) au sein d'Apache en mai 2024 : [Blog Arrow](https://arrow.apache.org/blog/2024/05/07/datafusion-tlp/).

Grove conclut en encourageant les lecteurs à plonger dans le fonctionnement des moteurs de requête via son livre, positionnant Rust comme un facteur de changement pour les applications gourmandes en données.

[Rust is for Big Data (#rust2018)](https://andygrove.io/2018/01/rust-is-for-big-data/)