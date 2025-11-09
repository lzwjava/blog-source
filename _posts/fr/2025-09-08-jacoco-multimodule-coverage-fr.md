---
audio: false
date: 2025-09-08
generated: true
image: false
lang: fr
layout: post
title: Stratégie de Rapport de Couverture Multi-Module JaCoCo
translated: true
type: note
---

Absolument. Votre analyse est tout à fait juste, en particulier concernant les complexités de JaCoCo avec les tests d'intégration externes. Exécuter la construction deux fois n'est effectivement pas idéal.

La stratégie que vous recherchez consiste à centraliser l'exécution des tests, puis à agréger les résultats. Vous êtes très proche du but, et le but `aggregate` est en effet le bon outil, mais il doit être appliqué d'une manière spécifique pour ce scénario.

Voici la stratégie recommandée : **Générer un seul fichier de couverture (`.exec`) dans votre module d'application web, puis utiliser un module de reporting dédié et séparé pour créer un rapport unique et agrégé pour tous les modules concernés.**

Cette approche est propre, évolutive et évite les constructions redondantes.

-----

## Le Concept Central

Lorsque votre application `PlaygroundWeb` s'exécute sur Jetty avec l'agent JaCoCo, l'agent instrumente **toutes les classes chargées par le classloader de l'application**. Cela inclut les classes de `PlaygroundWeb` lui-même *et* toutes ses dépendances, comme `PlaygroundUtils.jar`.

Par conséquent, le seul fichier `jacoco-it.exec` généré lors de la construction de `PlaygroundWeb` contient déjà les données de couverture pour **les deux modules**. Le défi consiste simplement à indiquer à l'outil de reporting JaCoCo où trouver le code source de tous les modules dont il a besoin pour construire le rapport HTML final.

-----

## Une Stratégie Évolutive en 4 Étapes

Voici un guide étape par étape pour restructurer votre projet afin d'obtenir un reporting de couverture agrégé et propre.

### Étape 1 : Créer un Module de Reporting Dédié

Commencez par créer un nouveau module exclusivement pour l'agrégation. C'est une bonne pratique Maven qui permet de séparer les préoccupations.

1.  Dans votre `pom.xml` racine (`PlaygroundLib`), ajoutez le nouveau module :
    ```xml
    <modules>
        <module>PlaygroundUtils</module>
        <module>PlaygroundWeb</module>
        <module>PlaygroundReports</module> </modules>
    ```
2.  Créez un nouveau répertoire `PlaygroundReports` à la racine avec son propre `pom.xml`.

Votre nouvelle structure de projet ressemblera à ceci :

```
.
├── PlaygroundReports
│   └── pom.xml
├── PlaygroundUtils
│   └── pom.xml
├── PlaygroundWeb
│   └── pom.xml
└── pom.xml
```

### Étape 2 : Configurer le `pom.xml` du Module de Reporting

Ce nouveau `pom.xml` est là où la magie opère. Il dépendra de tous les modules que vous souhaitez voir dans le rapport et exécutera le but `report-aggregate`.

**`PlaygroundReports/pom.xml` :**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.lzw</groupId>
        <artifactId>PlaygroundLib</artifactId>
        <version>1.0</version>
    </parent>
    <artifactId>PlaygroundReports</artifactId>
    <packaging>pom</packaging>
    <name>PlaygroundReports</name>

    <dependencies>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundWeb</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundUtils</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <executions>
                    <execution>
                        <id>aggregate-report</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>report-aggregate</goal>
                        </goals>
                        <configuration>
                            <dataFiles>
                                <dataFile>${project.basedir}/../PlaygroundWeb/target/jacoco-it.exec</dataFile>
                            </dataFiles>
                            <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### Étape 3 : Simplifier le Module `PlaygroundWeb`

Votre module `PlaygroundWeb` n'est maintenant responsable que de **générer les données de couverture**, et non de produire le rapport. Vous pouvez supprimer l'exécution de `jacoco:report` de son `pom.xml`.

**`PlaygroundWeb/pom.xml` (modifications uniquement) :**

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>prepare-agent</id>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
            <configuration>
                <propertyName>jacoco.it.agent</propertyName>
                <destFile>${project.build.directory}/jacoco-it.exec</destFile>
            </configuration>
        </execution>
        </executions>
</plugin>

<plugin>
    <groupId>org.eclipse.jetty</groupId>
    <artifactId>jetty-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>start-jetty</id>
            <phase>pre-integration-test</phase>
            <goals>
                <goal>start</goal>
            </goals>
            <configuration>
                <daemon>true</daemon>
                <jvmArgs>
                    ${jacoco.it.agent}
                </jvmArgs>
                </configuration>
        </execution>
        </executions>
</plugin>
```

*Note :* J'ai légèrement modifié la configuration de `prepare-agent` pour utiliser une propriété (`jacoco.it.agent`) et la référencer ensuite dans `jetty-maven-plugin`. C'est une manière robuste de passer la chaîne de l'agent. La configuration précédente dans votre `pom.xml` était également correcte, mais celle-ci rend l'intention plus claire.

### Étape 4 : Nettoyer `PlaygroundUtils`

Le module `PlaygroundUtils` n'a besoin d'aucune configuration du plugin JaCoCo pour les tests d'intégration. Son code est couvert via `PlaygroundWeb`, et le reporting est géré par `PlaygroundReports`. Vous pouvez supprimer toute propriété ou plugin lié à JaCoCo de son `pom.xml`.

-----

## Comment Cela Résout le Problème

1.  **Construction Unique :** Vous exécutez `mvn clean verify` depuis le répertoire racine une seule fois.
2.  **Cycle de Vie Correct :**
      * Maven construit `PlaygroundUtils`.
      * Maven construit `PlaygroundWeb`, démarre Jetty avec l'agent JaCoCo, exécute vos tests Python (qui sollicitent le code dans les deux modules), arrête Jetty, et produit `PlaygroundWeb/target/jacoco-it.exec`.
      * Maven construit `PlaygroundReports`. Dans la phase `verify`, le but `report-aggregate` s'exécute. Il trouve le fichier `.exec` de `PlaygroundWeb` et, grâce aux dépendances, il sait où trouver le code source de `PlaygroundWeb` et `PlaygroundUtils`.
      * Il génère **un seul rapport HTML unifié** avec la couverture pour les deux modules.
3.  **Évolutivité :** Si vous ajoutez dix modules de bibliothèque supplémentaires, il vous suffit de les ajouter comme dépendances dans le `PlaygroundReports/pom.xml`. La logique centrale ne change pas. C'est la solution propre et évolutive que vous recherchiez.