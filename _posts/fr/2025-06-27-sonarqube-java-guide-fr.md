---
audio: false
generated: true
lang: fr
layout: post
title: Maîtriser SonarQube pour les projets Java et Spring
translated: true
type: note
---

# Guide complet pour utiliser SonarQube avec les projets Java et Spring

## Introduction
SonarQube est une plateforme open-source pour l'inspection continue de la qualité du code. Il effectue une analyse statique du code pour détecter les bogues, les odeurs de code, les vulnérabilités et calcule la couverture du code. Ce guide fournit une vue d'ensemble complète de la configuration et de l'utilisation de SonarQube dans un projet Java Spring, incluant l'installation, la configuration, l'intégration et les bonnes pratiques.

## Table des matières
1. [Qu'est-ce que SonarQube ?](#quest-ce-que-sonarqube)
2. [Prérequis](#prérequis)
3. [Installation de SonarQube](#installation-de-sonarqube)
4. [Configuration d'un projet Java Spring](#configuration-dun-projet-java-spring)
5. [Configuration de SonarQube pour le projet](#configuration-de-sonarqube-pour-le-projet)
6. [Exécution de l'analyse SonarQube](#exécution-de-lanalyse-sonarqube)
7. [Interprétation des résultats SonarQube](#interprétation-des-résultats-sonarqube)
8. [Bonnes pratiques](#bonnes-pratiques)
9. [Résolution des problèmes courants](#résolution-des-problèmes-courants)
10. [Conclusion](#conclusion)

## Qu'est-ce que SonarQube ?
SonarQube est un outil qui fournit une inspection continue de la qualité du code en analysant le code source pour :
- **Bogues** : Erreurs potentielles dans le code.
- **Odeurs de code** : Problèmes de maintenabilité pouvant conduire à de la dette technique.
- **Vulnérabilités** : Problèmes de sécurité pouvant être exploités.
- **Couverture du code** : Pourcentage de code couvert par les tests unitaires.
- **Duplications** : Blocs de code répétés pouvant être refactorisés.

Il prend en charge plusieurs langages, dont Java, et s'intègre parfaitement avec des outils de build comme Maven et Gradle, ainsi qu'avec les pipelines CI/CD.

## Prérequis
Avant de configurer SonarQube, assurez-vous d'avoir :
- **Java Development Kit (JDK)** : Version 11 ou ultérieure (SonarQube nécessite Java 11 ou 17).
- **Maven ou Gradle** : Outil de build pour le projet Java Spring.
- **Serveur SonarQube** : Version 9.9 LTS ou ultérieure (l'édition Community est suffisante pour la plupart des cas d'usage).
- **SonarScanner** : Outil CLI pour exécuter l'analyse.
- **Base de données** : SonarQube nécessite une base de données (par exemple, PostgreSQL, MySQL, ou H2 embarquée pour les tests).
- **Projet Spring** : Un projet Spring Boot ou Spring Framework fonctionnel.
- **IDE** : IntelliJ IDEA, Eclipse ou VS Code pour le développement.

## Installation de SonarQube

### Étape 1 : Télécharger et installer SonarQube
1. **Télécharger SonarQube** :
   - Visitez la [page de téléchargement de SonarQube](https://www.sonarqube.org/downloads/).
   - Choisissez l'édition Community (gratuite) ou une autre édition selon vos besoins.
   - Téléchargez le fichier ZIP (par exemple, `sonarqube-9.9.0.zip`).

2. **Extraire le ZIP** :
   - Dézippez le fichier téléchargé dans un répertoire, par exemple `/opt/sonarqube` ou `C:\sonarqube`.

3. **Configurer la base de données** :
   - SonarQube nécessite une base de données. Pour la production, utilisez PostgreSQL ou MySQL. Pour les tests, la base de données H2 embarquée est suffisante.
   - Exemple pour PostgreSQL :
     - Installez PostgreSQL et créez une base de données (par exemple, `sonarqube`).
     - Mettez à jour le fichier de configuration de SonarQube (`conf/sonar.properties`) :
       ```properties
       sonar.jdbc.url=jdbc:postgresql://localhost:5432/sonarqube
       sonar.jdbc.username=sonarqube_user
       sonar.jdbc.password=sonarqube_pass
       ```

4. **Démarrer SonarQube** :
   - Accédez au répertoire SonarQube (`bin/<plateforme>`).
   - Exécutez le script de démarrage :
     - Sur Linux/Mac : `./sonar.sh start`
     - Sur Windows : `StartSonar.bat`
   - Accédez à SonarQube à l'adresse `http://localhost:9000` (port par défaut).

5. **Se connecter** :
   - Identifiants par défaut : `admin/admin`.
   - Changez le mot de passe après la première connexion.

### Étape 2 : Installer SonarScanner
1. **Télécharger SonarScanner** :
   - Téléchargez-le depuis la [page SonarQube Scanner](https://docs.sonarqube.org/latest/analyzing-source-code/scanners/sonarscanner/).
   - Extrayez-le dans un répertoire, par exemple `/opt/sonar-scanner`.

2. **Configurer les variables d'environnement** :
   - Ajoutez SonarScanner à votre PATH :
     - Sur Linux/Mac : `export PATH=$PATH:/opt/sonar-scanner/bin`
     - Sur Windows : Ajoutez `C:\sonar-scanner\bin` au PATH système.

3. **Vérifier l'installation** :
   - Exécutez `sonar-scanner --version` pour confirmer l'installation.

## Configuration d'un projet Java Spring
Pour ce guide, nous utiliserons un projet Spring Boot avec Maven. Les étapes sont similaires pour les projets Gradle ou Spring non-Boot.

1. **Créer un projet Spring Boot** :
   - Utilisez [Spring Initializer](https://start.spring.io/) pour créer un projet avec :
     - Dépendances : Spring Web, Spring Data JPA, Base de données H2, Spring Boot Starter Test.
     - Outil de build : Maven.
   - Téléchargez et extrayez le projet.

2. **Ajouter des tests unitaires** :
   - Assurez-vous que votre projet a des tests unitaires pour mesurer la couverture du code.
   - Exemple de classe de test :
     ```java
     import org.junit.jupiter.api.Test;
     import org.springframework.boot.test.context.SpringBootTest;

     @SpringBootTest
     public class ApplicationTests {
         @Test
         void contextLoads() {
         }
     }
     ```

3. **Ajouter Jacoco pour la couverture du code** :
   - Ajoutez le plugin Maven JaCoCo au `pom.xml` pour générer les rapports de couverture de code :
     ```xml
     <plugin>
         <groupId>org.jacoco</groupId>
         <artifactId>jacoco-maven-plugin</artifactId>
         <version>0.8.8</version>
         <executions>
             <execution>
                 <goals>
                     <goal>prepare-agent</goal>
                 </goals>
             </execution>
             <execution>
                 <id>report</id>
                 <phase>test</phase>
                 <goals>
                     <goal>report</goal>
                 </goals>
             </execution>
         </executions>
     </plugin>
     ```

## Configuration de SonarQube pour le projet

1. **Créer un projet SonarQube** :
   - Connectez-vous à SonarQube (`http://localhost:9000`).
   - Cliquez sur **Create Project** > **Manually**.
   - Fournissez une **Project Key** (par exemple, `my-spring-project`) et un **Display Name**.
   - Générez un token pour l'authentification (par exemple, `my-token`).

2. **Configurer `sonar-project.properties`** :
   - À la racine de votre projet Spring, créez un fichier `sonar-project.properties` :
     ```properties
     sonar.projectKey=my-spring-project
     sonar.projectName=My Spring Project
     sonar.host.url=http://localhost:9000
     sonar.token=my-token
     sonar.java.binaries=target/classes
     sonar.sources=src/main/java
     sonar.tests=src/test/java
     sonar.junit.reportPaths=target/surefire-reports
     sonar.jacoco.reportPaths=target/jacoco.exec
     sonar.sourceEncoding=UTF-8
     ```

3. **Intégration Maven (Alternative)** :
   - Au lieu de `sonar-project.properties`, vous pouvez configurer SonarQube dans `pom.xml` :
     ```xml
     <properties>
         <sonar.host.url>http://localhost:9000</sonar.host.url>
         <sonar.token>my-token</sonar.token>
         <sonar.projectKey>my-spring-project</sonar.projectKey>
         <sonar.projectName>My Spring Project</sonar.projectName>
     </properties>
     <build>
         <plugins>
             <plugin>
                 <groupId>org.sonarsource.scanner.maven</groupId>
                 <artifactId>sonar-maven-plugin</artifactId>
                 <version>3.9.1.2184</version>
             </plugin>
         </plugins>
     </build>
     ```

## Exécution de l'analyse SonarQube

1. **Utilisation de SonarScanner** :
   - Accédez à la racine du projet.
   - Exécutez :
     ```bash
     sonar-scanner
     ```
   - Assurez-vous que les tests sont exécutés avant l'analyse (`mvn test` pour les projets Maven).

2. **Utilisation de Maven** :
   - Exécutez :
     ```bash
     mvn clean verify sonar:sonar
     ```
   - Cette commande compile le code, exécute les tests, génère les rapports de couverture et envoie les résultats à SonarQube.

3. **Vérifier les résultats** :
   - Ouvrez SonarQube (`http://localhost:9000`) et accédez à votre projet.
   - Consultez le tableau de bord pour voir les résultats de l'analyse.

## Interprétation des résultats SonarQube
Le tableau de bord SonarQube fournit :
- **Vue d'ensemble** : Résumé des problèmes, de la couverture et des duplications.
- **Problèmes** : Liste des bogues, vulnérabilités et odeurs de code avec leur sévérité (Blocker, Critical, Major, etc.).
- **Couverture du code** : Pourcentage de code couvert par les tests (via JaCoCo).
- **Duplications** : Blocs de code répétés.
- **Quality Gate** : Statut de réussite/échec basé sur des seuils prédéfinis (par exemple, couverture > 80 %).

### Exemples d'actions :
- **Corriger les bogues** : Traiter les problèmes critiques comme les déréférencements de pointeurs nuls.
- **Refactoriser les odeurs de code** : Simplifier les méthodes complexes ou supprimer le code inutilisé.
- **Améliorer la couverture** : Écrire des tests unitaires supplémentaires pour le code non couvert.

## Bonnes pratiques
1. **Intégrer avec CI/CD** :
   - Ajoutez l'analyse SonarQube à votre pipeline CI/CD (par exemple, Jenkins, GitHub Actions).
   - Exemple de workflow GitHub Actions :
     ```yaml
     name: CI with SonarQube
     on: [push]
     jobs:
       build:
         runs-on: ubuntu-latest
         steps:
           - uses: actions/checkout@v3
           - name: Set up JDK 11
             uses: actions/setup-java@v3
             with:
               java-version: '11'
           - name: Build and Analyze
             run: mvn clean verify sonar:sonar -Dsonar.host.url=http://localhost:9000 -Dsonar.token=${{ secrets.SONAR_TOKEN }}
     ```

2. **Définir des Quality Gates** :
   - Définissez des seuils pour la couverture du code, les bogues et les vulnérabilités dans SonarQube.
   - Exemple : Échouer la build si la couverture < 80 % ou s'il existe des problèmes critiques.

3. **Utiliser SonarLint** :
   - Installez le plugin SonarLint dans votre IDE (par exemple, IntelliJ IDEA) pour détecter les problèmes pendant le développement.

4. **Analyse régulière** :
   - Exécutez l'analyse SonarQube à chaque commit ou quotidiennement pour détecter les problèmes tôt.

5. **Personnaliser les règles** :
   - Adaptez les règles SonarQube aux besoins de votre projet (par exemple, désactivez les règles non pertinentes ou ajoutez des règles personnalisées).

## Résolution des problèmes courants
1. **Échec du téléchargement de l'analyse** :
   - Vérifiez `sonar.host.url` et `sonar.token` dans la configuration.
   - Assurez-vous que le serveur SonarQube est en cours d'exécution (`http://localhost:9000`).

2. **Aucune couverture de code** :
   - Vérifiez que le plugin JaCoCo est correctement configuré dans `pom.xml`.
   - Exécutez `mvn test` avant l'analyse pour générer `jacoco.exec`.

3. **Erreurs de connexion à la base de données** :
   - Confirmez les identifiants de la base de données dans `sonar.properties`.
   - Assurez-vous que le serveur de base de données est en cours d'exécution.

4. **Manque de mémoire** :
   - Augmentez la mémoire JVM dans `sonar.properties` :
     ```properties
     sonar.web.javaOpts=-Xmx2g -Xms1g
     ```

## Conclusion
SonarQube est un outil puissant pour maintenir la qualité du code dans les projets Java Spring. En l'intégrant à votre workflow de développement, vous pouvez détecter les problèmes tôt, améliorer la maintenabilité du code et garantir une sécurité robuste. Une analyse régulière, combinée à des bonnes pratiques comme l'intégration CI/CD et SonarLint, vous aidera à maintenir une base de code de haute qualité.