---
audio: false
generated: true
lang: fr
layout: post
title: 'JDK 24 : Fonctionnalités et mises à jour principales'
translated: true
type: note
---

### Introduction au JDK 24

Le Java Development Kit (JDK) 24 est une version fonctionnelle de la plateforme Java SE (Standard Edition), officiellement publiée le 18 mars 2025 en tant que Implementation de Référence de la version 24, spécifiée par la JSR 399 dans le Java Community Process. Elle poursuit le cycle de publication de six mois d'Oracle, offrant un ensemble robuste d'améliorations pour accroître la productivité des développeurs, les performances et la sécurité. Le JDK 24 inclut 24 JDK Enhancement Proposals (JEPs), le plus grand nombre de fonctionnalités depuis le début du calendrier de publication basé sur le temps en 2018, ce qui en fait une étape significative dans l'évolution de Java. Il sert de tremplin vers le JDK 25, la prochaine version Long-Term Support (LTS) prévue pour septembre 2025.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://openjdk.org/projects/jdk/24/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### Statut Long-Term Support (LTS)

Le JDK 24 **n'est pas** une version Long-Term Support (LTS). C'est une version à support à court terme, ne bénéficiant que de six mois de support de niveau Premier d'Oracle, jusqu'en septembre 2025, date à laquelle il sera remplacé par le JDK 25. En revanche, les versions LTS comme le JDK 21 (septembre 2023) et le futur JDK 25 (septembre 2025) reçoivent au moins cinq ans de support Premier, ce qui les rend préférables pour la stabilité en entreprise. Le cycle LTS d'Oracle a lieu tous les deux ans, le JDK 21 étant la dernière LTS et le JDK 25 étant la prochaine.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)

### Publication et Stabilité

Le JDK 24 est **une version stable, prête pour la production**, ayant atteint la General Availability (GA) le 18 mars 2025. Les binaires prêts pour la production sont disponibles auprès d'Oracle sous les Oracle No-Fee Terms and Conditions (NFTC) et la licence GNU General Public License (GPLv2) pour OpenJDK, les binaires d'autres fournisseurs suivant sous peu. La version comprend plus de 3 000 corrections de bogues et de plus petites améliorations au-delà des 24 JEPs, garantissant la stabilité pour une utilisation générale. Cependant, en tant que version non-LTS, elle vise principalement les développeurs désireux de tester de nouvelles fonctionnalités plutôt que les entreprises nécessitant une stabilité à long terme.[](https://openjdk.org/projects/jdk/24/)[](https://www.theregister.com/2025/03/18/oracle_jdk_24/)[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)

### Nouvelles fonctionnalités du JDK 24

Le JDK 24 introduit 24 JEPs, catégorisés en améliorations des bibliothèques principales, améliorations du langage, fonctionnalités de sécurité, optimisations de la machine virtuelle HotSpot JVM et outils Java. Parmi celles-ci, 14 sont des fonctionnalités permanentes, sept sont des fonctionnalités en aperçu, deux sont expérimentales et une est un module incubateur. Voici quelques-unes des fonctionnalités les plus notables, en mettant l'accent sur celles pertinentes pour les développeurs et les déploiements :

1.  **Stream Gatherers (JEP 485)** - Permanent
    - Améliore l'API Stream en introduisant l'interface `Gatherer`, permettant aux développeurs de définir des opérations intermédiaires personnalisées pour les pipelines de flux. Cela permet des transformations de données plus flexibles, complétant l'interface `Collector` existante pour les opérations terminales.
    - Exemple : Grouper des mots par longueur en utilisant `StreamGatherers.groupBy`.
    - Avantage : Simplifie le traitement complexe des flux pour les développeurs.[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

2.  **Ahead-of-Time Class Loading & Linking (JEP 483)** - Expérimental
    - Faisant partie de Project Leyden, cette fonctionnalité réduit les temps de démarrage des applications Java en pré-chargeant et en liant les classes dans un cache lors d'une phase préparatoire. Le cache est réutilisé à l'exécution, contournant les étapes coûteuses de chargement de classes.
    - Avantage : Améliore les performances pour les applications cloud et les microservices.[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

3.  **Compact Object Headers (JEP 450)** - Expérimental
    - Faisant partie de Project Lilliput, cela réduit la taille des en-têtes d'objets Java de 96–128 bits à 64 bits sur les architectures 64 bits, diminuant l'utilisation du tas et améliorant l'efficacité mémoire.
    - Avantage : Réduit l'empreinte mémoire et améliore la localité des données pour de meilleures performances.[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)[](https://www.happycoders.eu/java/java-24-features/)

4.  **Generational Shenandoah Garbage Collector (JEP 404)** - Permanent
    - Fait passer le mode générationnel du GC Shenandoah de l'état expérimental à une fonctionnalité de produit, améliorant le débit, la résistance aux pics de charge et l'utilisation de la mémoire en divisant les objets en générations jeunes et vieilles.
    - Avantage : Améliore les performances pour les charges de travail exigeantes.[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.infoworld.com/article/3846172/jdk-25-the-new-features-in-java-25.html)

5.  **Module Import Declarations (JEP 494)** - Deuxième Aperçu
    - Simplifie la programmation modulaire en permettant l'importation directe de tous les packages exportés par un module sans nécessiter de fichier `module-info.java` (par exemple, `import module java.sql;`).
    - Avantage : Réduit la surcharge pour les applications légères et le script, aidant les débutants et le prototypage rapide.[](https://codefarm0.medium.com/java-24-features-a-deep-dive-into-whats-coming-81e77382b39c)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

6.  **Flexible Constructor Bodies (JEP 492)** - Troisième Aperçu
    - Permet des instructions dans les constructeurs avant les appels `super()` ou `this()`, permettant de placer la logique d'initialisation des champs plus naturellement sans méthodes auxiliaires.
    - Avantage : Améliore la fiabilité et la lisibilité du code, en particulier pour la sous-classification.[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

7.  **Key Derivation Function (KDF) API (JEP 487)** - Aperçu
    - Introduit une API pour les fonctions de dérivation de clés cryptographiques comme HMAC-based Extract-and-Expand et Argon2, prenant en charge le hachage sécurisé des mots de passe et l'interaction avec le matériel cryptographique.
    - Avantage : Améliore la sécurité des applications nécessitant une cryptographie avancée.[](https://www.jrebel.com/blog/whats-new-java-24)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

8.  **Permanently Disable the Security Manager (JEP 486)** - Permanent
    - Supprime le Security Manager, déprécié dans le JDK 17, car il n'est plus le principal moyen de sécuriser les applications Java (remplacé par le sandboxing basé sur les conteneurs).
    - Note : Les applications s'appuyant sur le Security Manager peuvent nécessiter des changements architecturaux.[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

9.  **Late Barrier Expansion for G1 Garbage Collector (JEP 464)** - Permanent
    - Simplifie l'implémentation des barrières du GC G1 en déplaçant l'expansion plus tard dans le pipeline de compilation, réduisant le temps de compilation et améliorant la maintenabilité.
    - Avantage : Améliore les performances des applications utilisant le GC G1.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

10. **Quantum-Resistant Cryptography (JEP 452, 453)** - Aperçu
    - Introduit Module-Lattice-Based Key Encapsulation Mechanism (ML-KEM) et Digital Signature Algorithm (ML-DSA) pour protéger contre les attaques par calcul quantique.
    - Avantage : Future-proof les applications Java pour la sécurité post-quantique.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

11. **Scoped Values (JEP 480)** - Quatrième Aperçu
    - Permet de partager des données immuables au sein des threads et entre eux de manière plus sûre que les variables thread-local, améliorant la gestion de la concurrence.
    - Avantage : Simplifie le raisonnement sur le code concurrent.[](https://www.jrebel.com/blog/whats-new-java-24)

12. **Deprecate 32-bit x86 Port (JEP 501)** - Permanent
    - Déprécie le port 32-bit x86 pour sa suppression dans le JDK 25, avec le port Zero agnostique de l'architecture comme alternative pour les systèmes 32 bits.
    - Avantage : Réduit la surcharge de maintenance, en se concentrant sur les architectures modernes.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

13. **Vector API (JEP 489)** - Neuvième Incubateur
    - Continue d'affiner l'API Vector pour la programmation SIMD, avec des améliorations des opérations cross-lane et arithmétiques.
    - Avantage : Améliore les performances des applications à calcul intensif.[](https://www.infoq.com/news/2025/02/java-24-so-far/)

14. **Linking Run-Time Images without JMODs (JEP 493)** - Permanent
    - Permet à l'outil `jlink` de créer des images d'exécution personnalisées sans fichiers JMOD, réduisant la taille du JDK d'environ ~25 %.
    - Avantage : Améliore l'efficacité du déploiement pour les runtimes Java personnalisés.[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### Notes supplémentaires

-   **Fonctionnalités en Aperçu et Expérimentales** : De nombreuses fonctionnalités (par exemple, Scoped Values, KDF API) sont en phase d'aperçu ou expérimentale, permettant aux développeurs de tester et de fournir des retours avant qu'elles ne deviennent permanentes dans le JDK 25 ou ultérieur. Celles-ci peuvent changer avant leur finalisation.[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.infoq.com/news/2025/02/java-24-so-far/)
-   **Intégration de Projets** : Le JDK 24 introduit des éléments des projets OpenJDK comme Leyden (optimisation du démarrage), Lilliput (efficacité mémoire) et Panama (interopérabilité native), posant les bases de futures améliorations.[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)
-   **Sécurité et Dépréciation** : Des fonctionnalités comme la suppression du Security Manager et la dépréciation du port 32-bit x86 reflètent la focalisation d'Oracle sur la modernisation de Java en éliminant progressivement les composants obsolètes.[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### Conclusion

Le JDK 24 est une version stable et riche en fonctionnalités qui fait progresser les performances, la productivité des développeurs et la sécurité de Java. Bien que ce ne soit pas une version LTS, ses 24 JEPs offrent des améliorations significatives, dont beaucoup seront finalisées dans la prochaine version LTS, le JDK 25. Les développeurs peuvent tirer parti de fonctionnalités comme Stream Gatherers et Module Import Declarations pour des gains de productivité immédiats, tandis que les fonctionnalités expérimentales comme Compact Object Headers et Ahead-of-Time Class Loading signalent l'optimisation continue de Java pour les charges de travail modernes. Pour un usage en entreprise, il est recommandé de rester sur les versions LTS comme le JDK 21 ou d'attendre le JDK 25 en raison de leur support étendu.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

Pour plus de détails, visitez :
-   [Notes de publication d'Oracle JDK 24](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)
-   [OpenJDK JDK 24](https://openjdk.org/projects/jdk/24/)
-   [Conférence JavaOne 2025](https://www.oracle.com/javaone) pour les points forts des fonctionnalités[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)