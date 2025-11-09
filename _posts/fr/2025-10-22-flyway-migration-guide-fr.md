---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de Migration de Base de Données Flyway
translated: true
type: note
---

### Introduction à Flyway
Flyway est un outil open-source populaire pour gérer les migrations de schéma de base de données de manière contrôlée par version. Il vous permet d'appliquer des modifications incrémentielles à votre base de données (comme créer des tables, modifier des colonnes ou insérer des données) de manière reproductible et sécurisée. Dans les applications Java, Flyway peut être intégré via son API, souvent exécutée au démarrage de l'application pour s'assurer que le schéma de la base de données est à jour avant que votre code n'interagisse avec elle. Il fonctionne avec la plupart des bases de données via JDBC (par exemple, PostgreSQL, MySQL, Oracle).

### Étape 1 : Ajouter la dépendance Flyway
Ajoutez Flyway à votre fichier de build. Utilisez l'édition open-source sauf si vous avez besoin des fonctionnalités enterprise.

**Maven (`pom.xml`)** :
```xml
<dependencies>
    <dependency>
        <groupId>org.flywaydb</groupId>
        <artifactId>flyway-core</artifactId>
        <version>11.14.1</version> <!-- Vérifiez la dernière version -->
    </dependency>
    <!-- Ajoutez le pilote JDBC de votre base de données, par exemple pour PostgreSQL -->
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
        <version>42.7.3</version>
    </dependency>
</dependencies>
```

**Gradle (`build.gradle`)** :
```groovy
dependencies {
    implementation 'org.flywaydb:flyway-core:11.14.1'
    // Ajoutez le pilote JDBC de votre base de données
    implementation 'org.postgresql:postgresql:42.7.3'
}
```

Vous aurez également besoin du pilote JDBC pour votre base de données cible.

### Étape 2 : Configurer Flyway
Flyway utilise une API fluide pour la configuration. Les paramètres clés incluent les détails de connexion à la base de données, les emplacements des scripts de migration et les rappels optionnels.

Dans votre code Java, créez une instance `Flyway` :
```java
import org.flywaydb.core.Flyway;

public class DatabaseMigration {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "username";
        String password = "password";

        Flyway flyway = Flyway.configure()
                .dataSource(url, user, password)
                .locations("classpath:db/migration")  // Dossier pour les scripts SQL (par défaut : db/migration)
                .load();
    }
}
```
- `locations` : Pointe vers l'emplacement de stockage de vos fichiers de migration (par exemple, `src/main/resources/db/migration` pour le classpath).
- Autres configurations courantes : `.baselineOnMigrate(true)` pour établir une baseline des schémas existants, ou `.table("flyway_schema_history")` pour personnaliser la table d'historique.

### Étape 3 : Écrire les scripts de migration
Les scripts de migration sont des fichiers SQL placés à l'emplacement configuré (par exemple, `src/main/resources/db/migration`). Flyway les applique dans l'ordre.

#### Conventions de nommage
- **Migrations versionnées** (pour les modifications de schéma ponctuelles) : `V<version>__<description>.sql` (par exemple, `V1__Create_person_table.sql`, `V2__Add_age_column.sql`).
  - Format de version : Utilisez des traits de soulignement pour les segments (par exemple, `V1_1__Initial.sql`).
- **Migrations répétables** (pour les tâches récurrentes comme les vues) : `R__<description>.sql` (par exemple, `R__Update_view.sql`). Celles-ci s'exécutent à chaque fois si elles sont modifiées.
- Les fichiers sont appliqués dans l'ordre lexicographique.

#### Exemples de scripts
Créez ces fichiers dans `src/main/resources/db/migration`.

**V1__Create_person_table.sql** :
```sql
CREATE TABLE person (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO person (id, name) VALUES (1, 'John Doe');
```

**V2__Add_age_column.sql** :
```sql
ALTER TABLE person ADD COLUMN age INT;
```

**R__Populate_names.sql** (répétable) :
```sql
UPDATE person SET name = CONCAT(name, ' (Updated)') WHERE id = 1;
```

Flyway suit les migrations appliquées dans une table `flyway_schema_history`.

Pour une logique complexe ne convenant pas au SQL, utilisez les migrations basées sur Java (implémentez `org.flywaydb.core.api.migration.java.JavaMigration`).

### Étape 4 : Exécuter les migrations par programme
Appelez `migrate()` pour appliquer les migrations en attente. Intégrez cela au démarrage de votre application (par exemple, dans `main()` ou un `@PostConstruct` Spring).

```java
import org.flywaydb.core.Flyway;
import org.flywaydb.core.api.FlywayException;

public class DatabaseMigration {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "username";
        String password = "password";

        Flyway flyway = Flyway.configure()
                .dataSource(url, user, password)
                .locations("classpath:db/migration")
                .load();

        try {
            flyway.migrate();  // Applique toutes les migrations en attente
            System.out.println("Base de données migrée avec succès !");
        } catch (FlywayException e) {
            System.err.println("Échec de la migration : " + e.getMessage());
            // Gérer l'erreur (par exemple, quitter ou effectuer un rollback)
        }

        // Maintenant, démarrez le reste de votre application
    }
}
```

- `migrate()` : Applique les migrations versionnées dans l'ordre, puis les répétables.
- Autres commandes : `flyway.info()` pour le statut, `flyway.repair()` pour corriger les problèmes, `flyway.validate()` pour vérifier la cohérence.
- Exécutez ceci avant toute opération sur la base de données pour garantir la compatibilité du schéma.

### Bonnes pratiques
- Gardez les migrations idempotentes (sûres à réexécuter).
- Testez les migrations sur une copie des données de production.
- Utilisez le contrôle de version pour les fichiers de migration.
- Pour Spring Boot, ajoutez `spring-boot-starter-jdbc` et définissez `spring.flyway.enabled=true` dans `application.properties` pour la configuration automatique.

### Références
- [Documentation de l'API Flyway (Java)](https://documentation.red-gate.com/fd/api-java-277579358.html)
- [Documentation des migrations Flyway](https://documentation.red-gate.com/fd/migrations-271585107.html)
- [Démarrage avec Flyway](https://documentation.red-gate.com/fd/getting-started-with-flyway-184127223.html)