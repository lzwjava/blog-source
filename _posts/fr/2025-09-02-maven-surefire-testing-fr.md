---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide de tests unitaires du plugin Maven Surefire
translated: true
type: note
---

Le **Maven Surefire Plugin** est le plugin qui exécute vos tests unitaires pendant la phase **test** du cycle de vie de construction Maven. C'est l'un des plugins Maven les plus couramment utilisés car presque tous les projets nécessitent des tests automatisés intégrés à leur processus de build.

---

## Qu'est-ce que c'est

* **Nom** : `maven-surefire-plugin`
* **Objectif** : Exécute les tests écrits avec des frameworks comme JUnit (3, 4, 5), TestNG, etc.
* **Phase** : Lié à la phase `test` du cycle de vie par défaut de Maven.
* **Sortie** : Génère des rapports de test (par défaut dans `target/surefire-reports`).

---

## Comment ça fonctionne

1. Lorsque vous exécutez `mvn test` ou `mvn package`, Maven invoque le plugin Surefire.
2. Il scanne votre répertoire `src/test/java` à la recherche des classes de test.
3. Par défaut, il recherche les fichiers correspondant aux conventions de nommage telles que :

   * `*Test.java`
   * `Test*.java`
   * `*Tests.java`
   * `*TestCase.java`
4. Il les exécute dans un classloader isolé.
5. Il écrit les résultats dans `target/surefire-reports` (texte brut, XML, et parfois HTML via des plugins de reporting).

---

## Utilisation de base

Vous pouvez le configurer dans votre `pom.xml` :

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>3.2.5</version> <!-- utilisez la dernière version stable -->
    </plugin>
  </plugins>
</build>
```

Après cela, exécutez simplement :

```bash
mvn test
```

---

## Configurations courantes

* **Modèles d'inclusion/exclusion** :

```xml
<configuration>
  <includes>
    <include>**/*MyTest.java</include>
  </includes>
  <excludes>
    <exclude>**/IntegrationTest.java</exclude>
  </excludes>
</configuration>
```

* **Propriétés système** :

```xml
<configuration>
  <systemPropertyVariables>
    <env>dev</env>
  </systemPropertyVariables>
</configuration>
```

* **Exécution de tests en parallèle** :

```xml
<configuration>
  <forkCount>2</forkCount>
  <reuseForks>true</reuseForks>
  <parallel>classes</parallel>
</configuration>
```

Ceci exécute les tests dans plusieurs processus JVM (forks) ou threads.

---

## Quand l'utiliser

* Chaque fois que vous souhaitez intégrer les **tests unitaires** dans votre cycle de vie Maven.
* Pour séparer les **tests unitaires (Surefire)** des **tests d'intégration (plugin Failsafe)** :

  * Surefire → tests unitaires (`mvn test`)
  * Failsafe → tests d'intégration (`mvn verify`)

---

✅ **En bref** : `maven-surefire-plugin` est le plugin incontournable pour l'exécution de tests unitaires dans les projets Maven. Vous le configurez dans `pom.xml`, l'exécutez avec `mvn test` et consultez les rapports dans `target/surefire-reports`.

---

Souhaitez-vous que j'explique également la **différence entre Surefire et Failsafe** (puisqu'ils sont souvent confondus) ?