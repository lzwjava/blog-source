---
audio: false
generated: true
lang: fr
layout: post
title: Plugin Maven Surefire
translated: true
type: note
---

Voici une explication du **Maven Surefire Plugin**, qui est un composant clé dans les projets basés sur Maven pour exécuter les tests unitaires pendant le processus de build. Cette explication couvre son objectif, sa configuration, son utilisation et ses options de personnalisation.

---

## Qu'est-ce que le Maven Surefire Plugin ?

Le **Maven Surefire Plugin** est un plugin Apache Maven conçu pour exécuter les tests unitaires pendant le cycle de vie du build. Il s'intègre parfaitement à la phase `test` de Maven et est déclenché automatiquement lorsque vous exécutez des commandes comme `mvn test`, `mvn package` ou `mvn install`. Le plugin prend en charge les frameworks de test populaires tels que JUnit (versions 3, 4 et 5) et TestNG, et il génère des rapports de test pour aider les développeurs à évaluer les résultats des tests.

### Fonctionnalités principales
- Exécute les tests dans un processus JVM séparé pour l'isolation.
- Prend en charge plusieurs frameworks de test (JUnit, TestNG, etc.).
- Génère des rapports de test dans des formats comme XML et texte brut.
- Offre la flexibilité de sauter des tests, d'exécuter des tests spécifiques ou de personnaliser l'exécution.

---

## Configuration de base dans `pom.xml`

Le plugin Surefire est inclus par défaut dans le cycle de vie de build de Maven, vous n'avez donc pas besoin de le configurer pour une utilisation basique. Cependant, vous pouvez le déclarer explicitement dans votre fichier `pom.xml` pour spécifier une version ou personnaliser son comportement.

### Configuration minimale
Si vous n'ajoutez aucune configuration, Maven utilise le plugin avec les paramètres par défaut :
- Les tests se trouvent dans `src/test/java`.
- Les fichiers de test suivent les modèles de nommage comme `**/*Test.java`, `**/Test*.java` ou `**/*Tests.java`.

### Déclaration explicite
Pour personnaliser le plugin ou garantir une version spécifique, ajoutez-le dans la section `<build><plugins>` de votre `pom.xml`. Voici un exemple :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M5</version> <!-- Utilisez la dernière version -->
        </plugin>
    </plugins>
</build>
```

---

## Exécuter les tests avec Surefire

Le plugin est lié à la phase `test` du cycle de vie Maven. Voici comment l'utiliser :

### Exécuter tous les tests
Pour exécuter tous les tests unitaires, lancez :

```
mvn test
```

### Exécuter les tests dans un build plus large
Les tests sont exécutés automatiquement lorsque vous lancez des commandes qui incluent la phase `test`, telles que :

```
mvn package
mvn install
```

### Sauter les tests
Vous pouvez sauter l'exécution des tests en utilisant des drapeaux en ligne de commande :
- **Sauter l'exécution des tests** : `-DskipTests`
  ```
  mvn package -DskipTests
  ```
- **Sauter la compilation et l'exécution des tests** : `-Dmaven.test.skip=true`
  ```
  mvn package -Dmaven.test.skip=true
  ```

---

## Personnaliser le plugin Surefire

Vous pouvez adapter le comportement du plugin en ajoutant une section `<configuration>` dans le `pom.xml`. Voici quelques personnalisations courantes :

### Inclure ou exclure des tests spécifiques
Spécifiez quels tests exécuter ou ignorer en utilisant des modèles :
```xml
<configuration>
    <includes>
        <include>**/My*Test.java</include>
    </includes>
    <excludes>
        <exclude>**/SlowTest.java</exclude>
    </excludes>
</configuration>
```

### Exécuter les tests en parallèle
Accélérez l'exécution en lançant les tests simultanément :
```xml
<configuration>
    <parallel>methods</parallel>
    <threadCount>2</threadCount>
</configuration>
```
*Remarque* : Assurez-vous que vos tests sont thread-safe avant d'activer cette option.

### Passer des propriétés système
Définissez des propriétés pour la JVM de test :
```xml
<configuration>
    <systemPropertyVariables>
        <propertyName>propertyValue</propertyName>
    </systemPropertyVariables>
</configuration>
```

### Générer des rapports
Par défaut, les rapports sont sauvegardés dans `target/surefire-reports`. Pour un rapport HTML, utilisez le `maven-surefire-report-plugin` :
```xml
<reporting>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-report-plugin</artifactId>
            <version>3.0.0-M5</version>
        </plugin>
    </plugins>
</reporting>
```
Exécutez `mvn surefire-report:report` pour générer le rapport HTML.

---

## Gérer les échecs de test

### Faire échouer le build en cas d'échec de test
Par défaut, un test qui échoue provoque l'échec du build. Pour ignorer les échecs et continuer :
```
mvn test -Dmaven.test.failure.ignore=true
```

### Réexécuter les tests échoués
Gérez les tests flaky en réessayant les échecs :
```xml
<configuration>
    <rerunFailingTestsCount>2</rerunFailingTestsCount>
</configuration>
```
Cela réexécute les tests échoués jusqu'à 2 fois.

---

## Utiliser Surefire avec les frameworks de test

Le plugin prend en charge divers frameworks de test avec une configuration minimale :

### JUnit 4
Aucune configuration supplémentaire n'est nécessaire ; Surefire détecte automatiquement les tests JUnit 4.

### JUnit 5
Ajoutez la dépendance JUnit 5 :
```xml
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.8.1</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
Utilisez la version 2.22.0 ou ultérieure de Surefire pour une prise en charge complète.

### TestNG
Ajoutez la dépendance TestNG :
```xml
<dependencies>
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <version>7.4.0</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
Surefire exécutera automatiquement les tests TestNG.

---

## Notes importantes

- **Emplacement des tests** : Les tests doivent être dans `src/test/java`, avec les ressources dans `src/test/resources`.
- **Conventions de nommage** : Les modèles par défaut incluent `**/*Test.java`, `**/Test*.java`, etc., mais ceux-ci peuvent être personnalisés.
- **Version du plugin** : Utilisez une version récente (par exemple, 3.0.0-M5) pour les dernières fonctionnalités et la prise en charge des frameworks.

---

## Résumé

Le **Maven Surefire Plugin** est essentiel pour exécuter les tests unitaires dans les projets Maven. Pour l'utiliser :
1. Comptez sur son comportement par défaut ou déclarez-le explicitement dans `pom.xml` pour la personnalisation.
2. Exécutez les tests avec `mvn test` ou dans le cadre de builds plus larges comme `mvn package`.
3. Personnalisez-le avec des options comme les modèles d'inclusion/exclusion, l'exécution parallèle ou les propriétés système.
4. Gérez les échecs en sautant des tests, en les ignorant ou en réexécutant les tests flaky.
5. Assurez la compatibilité avec votre framework de test (JUnit, TestNG) en ajoutant les bonnes dépendances.

Ce plugin offre une manière robuste et flexible de gérer les tests unitaires dans vos projets Maven !