---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Intégration de Liquibase avec Spring Boot
translated: true
type: note
---

## Intégration de Liquibase avec Spring Boot

Liquibase est un outil open-source populaire pour gérer les modifications de schéma de base de données (migrations) de manière versionnée. Spring Boot fournit une excellente prise en charge de la configuration automatique pour Liquibase, ce qui facilite son intégration. Ce guide suppose que vous utilisez Spring Boot 3.x (la dernière version en 2025) avec Maven, mais les concepts s'appliquent également à Gradle. Nous aborderons les bases étape par étape.

### Prérequis
- Un projet Spring Boot configuré (par exemple, via Spring Initializr).
- Une base de données (par exemple, H2 pour les tests, PostgreSQL/MySQL pour la production) configurée dans `application.properties`.

### Étape 1 : Ajouter la dépendance Liquibase
Incluez le starter Spring Boot pour Liquibase dans votre `pom.xml`. Cela récupère Liquibase et l'intègre de manière transparente.

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId> <!-- Pour la connectivité base de données -->
</dependency>
```

Pour Gradle, ajoutez dans `build.gradle` :
```groovy
implementation 'org.liquibase:liquibase-core'
implementation 'org.springframework.boot:spring-boot-starter-jdbc'
```

Exécutez `mvn clean install` (ou `./gradlew build`) pour récupérer les dépendances.

### Étape 2 : Configurer Liquibase
Spring Boot détecte automatiquement Liquibase si vous placez les fichiers de changelog à l'emplacement par défaut. Personnalisez via `application.properties` (ou l'équivalent `.yml`).

Exemple `application.properties` :
```properties
# Configuration base de données (ajuster pour votre BD)
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driver-class-name=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# Configuration Liquibase
spring.liquibase.change-log=classpath:db/changelog/db.changelog-master.xml
spring.liquibase.enabled=true  # La valeur par défaut est true
spring.liquibase.drop-first=false  # Mettre à true en dev pour supprimer le schéma au démarrage
```

- `change-log` : Chemin vers votre fichier changelog maître (par défaut : `db/changelog/db.changelog-master.xml`).
- Activez/désactivez avec `spring.liquibase.enabled`.
- Pour les contextes/profils, utilisez `spring.liquibase.contexts=dev` pour exécuter des changements spécifiques.

### Étape 3 : Créer les fichiers Changelog
Liquibase utilise des "changelogs" pour définir les modifications de schéma. Créez une structure de répertoire sous `src/main/resources` :
```
src/main/resources/
└── db/
    └── changelog/
        ├── db.changelog-master.xml  # Fichier maître incluant les autres
        └── changes/
            ├── 001-create-users-table.xml  # Changements individuels
            └── 002-add-email-column.xml
```

#### Changelog Maître (`db.changelog-master.xml`)
Celui-ci inclut d'autres changelogs :
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.24.xsd">

    <include file="changes/001-create-users-table.xml"/>
    <include file="changes/002-add-email-column.xml"/>
</databaseChangeLog>
```

#### Exemple de changement (`001-create-users-table.xml`)
Définir une création de table :
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                                       http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.24.xsd">

    <changeSet id="001" author="votrenom">
        <createTable tableName="users">
            <column name="id" type="bigint">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="name" type="varchar(255)">
                <constraints nullable="false"/>
            </column>
        </createTable>
    </changeSet>
</databaseChangeLog>
```

- Utilisez les formats XML, YAML, JSON ou SQL pour les changelogs.
- Chaque `<changeSet>` est une migration avec un ID (pour le suivi).
- Exécutez `java -jar target/your-app.jar` pour démarrer l'application — Liquibase applique les changements automatiquement lors du bootstrap.

### Étape 4 : Exécution et Tests
- **Au Démarrage** : Spring Boot exécute Liquibase avant que votre application ne démarre complètement.
- **Rollback** : Utilisez `spring.liquibase.rollback-file` ou la CLI pour les tests.
- **Intégration CLI** : Pour les exécutions manuelles, ajoutez le plugin Maven Liquibase :
  ```xml
  <plugin>
      <groupId>org.liquibase</groupId>
      <artifactId>liquibase-maven-plugin</artifactId>
      <version>4.24.0</version>
      <configuration>
          <changeLogFile>src/main/resources/db/changelog/db.changelog-master.xml</changeLogFile>
          <url>jdbc:h2:mem:testdb</url>
          <username>sa</username>
          <password></password>
      </configuration>
  </plugin>
  ```
  Puis exécutez `mvn liquibase:update`.

- **Validation** : Activez `spring.liquibase.validate-on-migrate=true` pour vérifier les changelogs.

### Conseils courants
- **Profils** : Utilisez `@Profile("dev")` sur les beans si nécessaire, mais Liquibase s'exécute globalement sauf s'il est filtré.
- **Préconditions** : Ajoutez `<preConditions>` dans les changesets pour vérifier l'état de la base de données.
- **Format SQL** : Pour le SQL brut, créez des fichiers `.sql` et incluez-les : `<sqlFile path="changes/create-users.sql" relativeToChangelogFile="true"/>`.
- **Dépannage** : Vérifiez les logs pour les erreurs (par exemple, préfixées par `liquibase`). Assurez-vous que l'URL de la base de données est correcte.
- **Production** : Utilisez Flyway si vous préférez, mais Liquibase excelle pour les changements complexes et la prise en charge multi-base de données.

Pour les fonctionnalités avancées comme les rollbacks tagués ou les extensions personnalisées, reportez-vous à la documentation.

### Références
- [Configuration automatique Spring Boot Liquibase](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#io.liquibase)
- [Documentation officielle de Liquibase](https://docs.liquibase.com/start/home.html)
- [Tutoriel Baeldung Spring Boot + Liquibase](https://www.baeldung.com/liquibase-refactor-schema-of-jpa-entity-in-spring-boot)