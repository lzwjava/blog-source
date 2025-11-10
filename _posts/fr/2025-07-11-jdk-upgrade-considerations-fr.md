---
audio: false
generated: true
lang: fr
layout: post
title: Modernisation d'une Base de Code Héritée vers un JDK Plus Récent
translated: true
type: note
---

La mise à niveau d'une base de code importante (des dizaines de milliers de lignes) de JDK 8 et Spring 5.2.2 vers un JDK plus récent comme 11, 17 ou 21 nécessite une planification minutieuse pour minimiser les perturbations, surtout compte tenu de l'utilisation des drivers IBM DB2 JCC, de la forte dépendance à Spring et du déploiement sur WebSphere Liberty. Ci-dessous, je vais décrire les considérations clés, incluant la compatibilité, les changements cassants potentiels, les étapes de migration et les recommandations. Puisque vous avez mentionné que vous pouvez aussi mettre à niveau Spring, je couvrirai les scénarios où cela pourrait être nécessaire ou bénéfique.

### Considérations générales pour la mise à niveau du JDK
- **Compatibilité ascendante et changements cassants** : Java vise une forte compatibilité ascendante, mais les mises à niveau depuis JDK 8 introduisent des changements qui pourraient affecter votre code :
  - **APIs supprimées/obsolètes** : JDK 9+ a supprimé des APIs internes comme `sun.misc.Unsafe` et certains packages `sun.*`. Si votre code (ou ses dépendances) les utilise, vous aurez besoin d'alternatives (par exemple via des alternatives à `Unsafe` dans des librairies tierces ou `VarHandle` de Java).
  - **Système de modules (JPMS depuis JDK 9)** : Encapsule les APIs internes, causant potentiellement des erreurs "illegal access". Utilisez les flags `--add-opens` ou `--add-exports` temporairement, mais visez un refactoring pour la modularité.
  - **Changements du Garbage Collection** : Le GC par défaut est passé de Parallel à G1 dans JDK 9, avec d'autres ajustements dans les versions ultérieures (par exemple, Shenandoah ou ZGC dans 11+). Testez l'impact sur les performances des parties gourmandes en mémoire.
  - **Autres changements** : Encapsulation renforcée, suppression du support des applets/plugins navigateur, mises à jour des Security Managers (obsolète en 17, supprimé en 21), et fonctionnalités du langage comme les records (14+), les classes sealed (17) et les virtual threads (21). Ces ajouts sont majoritairement non-cassants mais pourraient nécessiter des ajustements du code si la réflexion est utilisée intensivement.
  - De 8 à 11 : Changements modérés (par exemple, plus de modules Java EE comme JAXB, supprimés dans JDK 9 ; ajoutez-les comme dépendances).
  - De 11 à 17 : Perturbations moindres, principalement des améliorations comme un meilleur pattern matching.
  - De 17 à 21 : Changements cassants minimes ; principalement de nouvelles fonctionnalités comme le pattern matching pour switch (21) et pas de suppressions majeures.
- **Migration par étapes** : Ne passez pas directement à la version 21. Mettez à niveau de manière incrémentale (par exemple, 8 → 11 → 17 → 21) pour isoler les problèmes. Utilisez des outils comme OpenRewrite ou jdeps pour scanner les incompatibilités.
- **Tests et outils** :
  - Exécutez des tests complets (unitaires, d'intégration, de charge) sur le nouveau JDK. Des outils comme les plugins Maven/Gradle (par exemple, `maven-enforcer-plugin`) peuvent forcer la compatibilité.
  - Mettez à jour les outils de build : Assurez-vous que Maven/Gradle supporte le nouveau JDK (c'est généralement le cas, mais vérifiez les plugins comme Surefire).
  - Tests multi-versions : Utilisez Docker ou CI/CD (par exemple, GitHub Actions) pour tester avec plusieurs JDKs.
- **Dépendances et librairies** : Scannez toutes les librairies tierces pour la compatibilité. Utilisez des outils comme `mvn dependency:tree` ou OWASP Dependency-Check.
- **Performance et sécurité** : Les JDKs plus récents offrent de meilleures performances (par exemple, un démarrage plus rapide dans 17+), des correctifs de sécurité et un support à long terme (LTS : 11 jusqu'en 2026, 17 jusqu'en 2029, 21 jusqu'en 2031+).
- **Effort pour une grande base de code** : Avec une forte utilisation de Spring, concentrez-vous sur les composants gérés par Spring (par exemple, les beans, AOP). Prévoyez du temps pour le refactoring (par exemple, 1-2 semaines par saut de version majeur, proportionnellement à la taille du code).

### Considérations spécifiques par JDK cible
#### Mise à niveau vers JDK 11
- **Avantages** : LTS avec une bonne stabilité ; plus proche de JDK 8, donc moins de changements. Fin de vie approchant (2026), mais toujours largement supporté.
- **Inconvénients** : Ne dispose pas des fonctionnalités modernes comme les virtual threads (21) ou les GC améliorés (17+).
- **Compatibilité Spring** : Spring 5.2.2 fonctionne sur JDK 11, mais mettez à niveau vers Spring 5.3.x (dernière de la ligne 5.x) pour un meilleur support de JDK 11/17 et des correctifs de bugs. Aucun changement majeur de Spring nécessaire.
- **Driver DB2 JCC** : Compatible avec les versions récentes du driver (par exemple, 4.x+). Certains anciens drivers avaient des problèmes avec OpenJDK 11, donc mettez à jour vers la dernière version (par exemple, depuis le site d'IBM) et testez les connexions.
- **WebSphere Liberty** : Entièrement supporté (Liberty fonctionne sur JDK 8/11/17/21).
- **Changements clés depuis JDK 8** :
  - Ajoutez des dépendances pour les modules supprimés (par exemple, `javax.xml.bind:jaxb-api` pour JAXB).
  - Corrigez tout accès réflexif illégal (commun dans les anciennes librairies).
  - Comment migrer : Mettez à jour votre fichier de build (par exemple, Maven `<java.version>11</java.version>`), recompilez et exécutez les tests. Utilisez le Guide de Migration JDK 11 d'Oracle pour des vérifications étape par étape.
- **Effort** : Faible à moyen ; changements de code minimes si aucune API interne n'est utilisée.

#### Mise à niveau vers JDK 17
- **Avantages** : LTS actuel avec une forte adoption ; inclut des fonctionnalités comme les text blocks, les records et les switch améliorés. Meilleures performances que JDK 11.
- **Inconvénients** : SecurityManager déprécié (s'il est utilisé, prévoyez son retrait). Certaines librairies pourraient nécessiter des mises à jour.
- **Compatibilité Spring** : Spring 5.3.x supporte entièrement JDK 17 (testé sur les releases LTS). Mettez à niveau de 5.2.2 vers 5.3.x pour une compatibilité optimale—aucun changement cassant dans Spring lui-même.
- **Driver DB2 JCC** : Explicitement supporté dans les versions récentes (par exemple, JCC 4.29+ pour DB2 11.5). La documentation IBM confirme le support du runtime JDK 17 ; testez pour toute amélioration SQLJ.
- **WebSphere Liberty** : Entièrement supporté.
- **Changements clés depuis JDK 11** :
  - Encapsulation plus stricte ; plus d'avertissements sur les fonctionnalités dépréciées.
  - De nouvelles APIs (par exemple, `java.net.http` pour les clients HTTP/2) peuvent moderniser le code mais ne sont pas obligatoires.
  - Comment migrer : Après JDK 11, basculez vers 17 dans les builds. Utilisez les guides de migration pour vérifier les suppressions d'applets/corba (le cas échéant).
- **Effort** : Moyen ; s'appuie sur la migration vers JDK 11.

#### Mise à niveau vers JDK 21
- **Avantages** : Dernier LTS avec des fonctionnalités de pointe (par exemple, les virtual threads pour la concurrence, les sequenced collections). Meilleur pour la pérennité.
- **Inconvénients** : Nécessite une mise à niveau de Spring (voir ci-dessous) ; problèmes potentiels avec des librairies très anciennes.
- **Compatibilité Spring** : Spring 5.x ne supporte pas officiellement JDK 21 (le maximum est JDK 17). Vous devez mettre à niveau vers Spring 6.1+ (qui nécessite un socle JDK 17+). C'est un changement majeur :
  - **Migration Jakarta EE** : Spring 6 passe de Java EE (javax.*) à Jakarta EE 9+ (jakarta.*). Changez les imports (par exemple, `javax.servlet` → `jakarta.servlet`), mettez à jour les configurations et refactorez tout code lié à EE (par exemple, JPA, Servlets, JMS).
  - **Changements cassants** : Suppression des APIs dépréciées (par exemple, les anciens gestionnaires de transactions) ; support de la compilation AOT ; nécessite de mettre à jour les dépendances comme Hibernate (vers 6.1+).
  - **Guide de migration** : Suivez le guide officiel de Spring : Mettez à jour d'abord vers Spring 5.3.x, puis vers 6.0/6.1. Utilisez des outils comme les recettes OpenRewrite pour des échanges automatisés javax → jakarta. Pour votre grande base de code, cela pourrait impliquer des centaines de changements—testez par modules.
  - Si vous utilisez Spring Boot (sous-entendu par l'usage de Spring), Boot 3.x s'aligne avec Spring 6 et JDK 17+.
- **Driver DB2 JCC** : Compatible via la rétrocompatibilité avec le support JDK 17 ; mettez à jour vers le dernier driver (par exemple, 4.32+) et vérifiez.
- **WebSphere Liberty** : Entièrement supporté (jusqu'à JDK 24).
- **Changements clés depuis JDK 17** :
  - SecurityManager supprimé ; s'il est utilisé, remplacez-le par des alternatives.
  - Les nouvelles fonctionnalités comme les string templates (en preview) ne casseront pas le code existant.
  - Comment migrer : Construisez d'abord sur JDK 17, puis basculez. Aucun changement cassant délibéré majeur entre 17 et 21.
- **Effort** : Élevé si mise à niveau de Spring ; sinon similaire à 17.

### Considérations supplémentaires spécifiques au projet
- **Librairie IBM DB2 JCC** : Assurez-vous que votre version de driver correspond à la release DB2 (par exemple, pour DB2 11.5, utilisez JCC 4.29+). Testez les connexions JDBC, SQLJ, et toute requête personnalisée—les JDKs plus récents pourraient exposer des problèmes de charset ou de fuseau horaire.
- **Déploiement WebSphere Liberty** : Aucun blocage ; Liberty est flexible avec les JDKs. Mettez à jour server.xml si nécessaire pour les arguments JVM (par exemple, `--add-opens` pour les problèmes de modules). Testez les déploiements tôt.
- **Grande base de code et usage de Spring** : Priorisez les mises à niveau modulaires (par exemple, mettez à niveau les services core en premier). Si Spring est profondément intégré (par exemple, MVC, Data, Security), auditez les fonctionnalités dépréciées dans 5.2.2. Mettre à niveau Spring apporte des bénéfices comme un meilleur AOT et de l'observabilité mais ajoute un coût.
- **Risques et atténuations** : Indisponibilité due aux incompatibilités ; atténuez avec des plans de rollback. Prévoyez un budget pour le support vendor si vous utilisez DB2/Liberty commerciaux.
- **Coûts** : Temps (semaines à mois pour une migration complète), licensing potentiel (par exemple, JDKs commerciaux comme celui d'Oracle), et formation sur les nouvelles fonctionnalités.

### Recommandations
- **Chemin préféré** : Commencez avec JDK 11 ou 17 tout en conservant/mettant à niveau vers Spring 5.3.x—risque plus faible pour votre base de code. Passez à 21 seulement si vous avez besoin de ses fonctionnalités (par exemple, les virtual threads) et êtes prêt à mettre à niveau vers Spring 6 (ce qui pourrait prendre un effort significatif à cause des changements Jakarta).
- **Prochaines étapes** :
  1. Scannez le code avec jdeps/jlink pour identifier les problèmes.
  2. Configurez une branche pour tester la migration.
  3. Consultez les guides officiels : Oracle JDK Migration Guide, Spring Versions Wiki, IBM DB2 JDBC Downloads, Liberty Java Support.
  4. Si vous mettez à niveau Spring vers la version 6, suivez le guide de migration pour les changements Jakarta.

Si vous fournissez plus de détails (par exemple, des modules Spring spécifiques ou la version de DB2), je peux affiner davantage.