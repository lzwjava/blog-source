---
audio: false
generated: true
lang: fr
layout: post
title: 'Liquibase : Gestion du Schéma de Base de Données'
translated: true
type: note
---

Voici un guide complet sur **comment utiliser Liquibase** dans une application Spring Boot pour gérer efficacement les modifications du schéma de votre base de données :

---

### 1. Ajouter la Dépendance Liquibase
Pour commencer, vous devez inclure la dépendance Liquibase dans votre projet. Si vous utilisez **Maven**, ajoutez ceci à votre `pom.xml` :

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
```

Pour **Gradle**, ajoutez ceci à votre `build.gradle` :

```groovy
implementation 'org.liquibase:liquibase-core'
```

Cela intègre la bibliothèque core de Liquibase dans votre projet.

---

### 2. Configurer Liquibase
Liquibase utilise un **fichier de changelog** pour gérer les modifications du schéma de la base de données. Par défaut, Spring Boot recherche un fichier nommé `db/changelog/db.changelog-master.yaml`, `db/changelog/db.changelog-master.xml` ou `db/changelog/db.changelog-master.sql` dans le classpath. Vous pouvez personnaliser cet emplacement en ajoutant une propriété à votre `application.properties` (ou `application.yml`) :

```properties
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

Cela indique à Spring Boot où trouver votre fichier de changelog.

---

### 3. Créer un Fichier Changelog
Le fichier changelog définit les modifications que vous souhaitez appliquer à votre base de données. Vous pouvez l'écrire dans des formats comme XML, YAML ou SQL. Voici un exemple de fichier **changelog XML** situé à `src/main/resources/db/changelog/db.changelog-master.xml` :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.8.xsd">

    <changeSet id="1" author="your-name">
        <createTable tableName="users">
            <column name="id" type="int">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="username" type="varchar(255)"/>
            <column name="email" type="varchar(255)"/>
        </createTable>
    </changeSet>

</databaseChangeLog>
```

Cet exemple crée une table `users` avec trois colonnes : `id`, `username` et `email`. Chaque `<changeSet>` représente un ensemble de modifications à appliquer.

---

### 4. Exécuter Votre Application Spring Boot
Lorsque vous démarrez votre application Spring Boot, Liquibase effectue automatiquement les actions suivantes :
- Lit le fichier changelog.
- Vérifie quels changesets ont déjà été appliqués (suivis dans une table appelée `DATABASECHANGELOG`).
- Exécute tous les nouveaux changesets sur votre base de données.

Aucun code supplémentaire n'est nécessaire — l'auto-configuration de Spring Boot s'en charge pour vous.

---

### 5. Personnaliser Liquibase (Optionnel)
Vous pouvez ajuster le comportement de Liquibase en utilisant des propriétés dans `application.properties`. Voici quelques options courantes :

```properties
spring.liquibase.enabled=true          # Activer ou désactiver Liquibase
spring.liquibase.drop-first=false      # Supprimer la base de données avant d'appliquer les changements (à utiliser avec prudence)
spring.liquibase.contexts=dev,prod     # Exécuter les changesets uniquement dans des contextes spécifiques
```

Ces paramètres vous permettent d'adapter Liquibase à votre environnement ou flux de travail.

---

### 6. Tirer Parti des Fonctionnalités Avancées
Liquibase offre des fonctionnalités puissantes pour améliorer la gestion du schéma :
- **Contexts et Labels** : Contrôler quels changesets s'exécutent dans des environnements spécifiques (par exemple, `dev` vs `prod`).
- **Preconditions** : S'assurer que certaines conditions (par exemple, l'existence d'une table) sont remplies avant d'appliquer un changeset.
- **Rollbacks** : Définir comment annuler un changeset si nécessaire.
- **Refactoring** : Utiliser la prise en charge intégrée pour les modifications complexes de base de données (par exemple, renommer des colonnes).

Par exemple, pour ajouter un contexte à un changeset :

```xml
<changeSet id="2" author="your-name" context="dev">
    <addColumn tableName="users">
        <column name="created_at" type="timestamp"/>
    </addColumn>
</changeSet>
```

Ce changeset ne s'exécute que dans le contexte `dev`.

---

### 7. Tester avec une Base de Données en Mémoire
Pour les tests, associez Liquibase avec une base de données en mémoire comme H2. Ajoutez la dépendance H2 :

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

Puis configurez votre `application.properties` pour les tests :

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

Liquibase appliquera vos modifications à la base de données en mémoire pendant les tests.

---

### 8. Versionner Votre Changelog
Stockez vos fichiers changelog dans un système de contrôle de version (par exemple, Git) aux côtés de votre code d'application. Cela garantit que votre schéma de base de données évolue en phase avec votre codebase, rendant les déploiements et les retours en arrière plus prévisibles.

---

### Résumé
Pour utiliser Liquibase dans une application Spring Boot :
1. Ajoutez la dépendance Liquibase.
2. Configurez l'emplacement du fichier changelog.
3. Créez un fichier changelog avec vos modifications de base de données.
4. Exécutez votre application — Liquibase s'occupe du reste.

Liquibase est un outil robuste pour gérer les modifications du schéma de base de données de manière structurée et versionnée, parfaitement intégré à Spring Boot.