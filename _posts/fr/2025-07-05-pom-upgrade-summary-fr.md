---
audio: false
generated: true
lang: fr
layout: post
title: Mise à niveau des dépendances et plugins Maven
translated: true
type: note
---

Voici une liste des versions dans votre `pom.xml` qui peuvent être mises à niveau, ainsi que leurs dernières versions disponibles au 5 juillet 2025 :

**Dépendances :**

* `org.junit.jupiter:junit-jupiter-api`
    * Actuelle : `5.9.2`
    * Dernière version stable : `5.13.2` (Publiée le 24 juin 2025)
    * Dernière version preview : `6.0.0-M1` (Publiée le 27 juin 2025) - À considérer si vous souhaitez utiliser une version milestone.
* `org.junit.jupiter:junit-jupiter-engine`
    * Actuelle : `5.9.2`
    * Dernière version stable : `5.13.2` (Publiée le 24 juin 2025)
    * Dernière version preview : `6.0.0-M1` (Publiée le 27 juin 2025) - À considérer si vous souhaitez utiliser une version milestone.

**Plugins :**

* `org.apache.maven.plugins:maven-compiler-plugin`
    * Actuelle : `3.13.0`
    * Dernière : `3.14.0` (Publiée le 17 février 2025)
* `org.apache.maven.plugins:maven-jar-plugin`
    * Actuelle : `3.4.2`
    * Dernière : `3.4.2` (Aucune nouvelle version stable trouvée. Dernière publication le 16 juin 2024, mais la date actuelle est le 5 juillet 2025, donc cette version est toujours à jour).
* `com.diffplug.spotless:spotless-maven-plugin`
    * Actuelle : `2.44.5`
    * Dernière : `2.44.5` (Aucune nouvelle version stable trouvée. Dernière publication le 28 mai 2025, donc cette version est toujours à jour).
* `org.apache.maven.plugins:maven-checkstyle-plugin`
    * Actuelle : `3.6.0`
    * Dernière : `3.6.0` (Aucune nouvelle version stable trouvée. Dernière publication le 22 octobre 2024, donc cette version est toujours à jour).
    * **Note :** La dépendance `checkstyle` à l'intérieur de la configuration du plugin checkstyle peut être mise à jour :
        * Actuelle : `10.25.0`
        * Dernière : `10.26.1` (Publiée le 29 juin 2025)
* `org.apache.maven.plugins:maven-surefire-plugin`
    * Actuelle : `3.0.0-M7`
    * Dernière version stable : `3.5.3` (Publiée le 27 mars 2025) - Il s'agit d'un saut significatif depuis une version milestone.
* `org.codehaus.mojo:exec-maven-plugin`
    * Actuelle : `3.5.1`
    * Dernière : `3.5.1` (Aucune nouvelle version stable trouvée. Dernière publication le 27 mai 2025, donc cette version est toujours à jour).

**Résumé des mises à niveau :**

* **JUnit Jupiter API :** 5.9.2 -> 5.13.2 (ou 6.0.0-M1)
* **JUnit Jupiter Engine :** 5.9.2 -> 5.13.2 (ou 6.0.0-M1)
* **Maven Compiler Plugin :** 3.13.0 -> 3.14.0
* **Checkstyle (dépendance dans le plugin) :** 10.25.0 -> 10.26.1
* **Maven Surefire Plugin :** 3.0.0-M7 -> 3.5.3

**Considérations importantes avant la mise à niveau :**

* **Changements cassants :** Consultez toujours les notes de version pour chaque composant que vous prévoyez de mettre à niveau. Les augmentations de version majeure (comme de JUnit 5 à 6, ou de Surefire 3.0.0-M7 à 3.5.3) peuvent introduire des changements cassants qui nécessitent des modifications de code.
* **Compatibilité :** Assurez-vous que les nouvelles versions sont compatibles avec votre version de Java (JDK 21 dans votre cas) et les autres dépendances de votre projet.
* **Tests :** Après la mise à niveau, testez minutieusement votre application pour vous assurer que tout fonctionne toujours comme prévu.