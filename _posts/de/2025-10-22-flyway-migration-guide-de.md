---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Flyway Datenbank-Migrationsleitfaden
translated: true
type: note
---

### Einführung in Flyway
Flyway ist ein beliebtes Open-Source-Tool zur Versionsverwaltung von Datenbankschema-Migrationen. Es ermöglicht Ihnen, inkrementelle Änderungen an Ihrer Datenbank (wie das Erstellen von Tabellen, Ändern von Spalten oder Einfügen von Daten) auf wiederholbare und sichere Weise anzuwenden. In Java-Anwendungen kann Flyway über seine API integriert werden, oft gestartet beim Anwendungsstart, um sicherzustellen, dass das Datenbankschema aktuell ist, bevor Ihr Code damit interagiert. Es funktioniert mit den meisten Datenbanken über JDBC (z.B. PostgreSQL, MySQL, Oracle).

### Schritt 1: Flyway-Abhängigkeit hinzufügen
Fügen Sie Flyway Ihrer Build-Datei hinzu. Verwenden Sie die Open-Source-Edition, es sei denn, Sie benötigen Enterprise-Funktionen.

**Maven (`pom.xml`)**:
```xml
<dependencies>
    <dependency>
        <groupId>org.flywaydb</groupId>
        <artifactId>flyway-core</artifactId>
        <version>11.14.1</version> <!-- Auf neueste Version prüfen -->
    </dependency>
    <!-- Fügen Sie Ihren Datenbank-JDBC-Treiber hinzu, z.B. für PostgreSQL -->
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
        <version>42.7.3</version>
    </dependency>
</dependencies>
```

**Gradle (`build.gradle`)**:
```groovy
dependencies {
    implementation 'org.flywaydb:flyway-core:11.14.1'
    // Fügen Sie Ihren Datenbank-JDBC-Treiber hinzu
    implementation 'org.postgresql:postgresql:42.7.3'
}
```

Sie benötigen auch den JDBC-Treiber für Ihre Zieldatenbank.

### Schritt 2: Flyway konfigurieren
Flyway verwendet eine flüssige API für die Konfiguration. Wichtige Einstellungen sind die Datenbankverbindungsdetails, Orte für Migrationsskripte und optionale Callbacks.

Erstellen Sie in Ihrem Java-Code eine `Flyway`-Instanz:
```java
import org.flywaydb.core.Flyway;

public class DatabaseMigration {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "username";
        String password = "password";

        Flyway flyway = Flyway.configure()
                .dataSource(url, user, password)
                .locations("classpath:db/migration")  // Ordner für SQL-Skripte (Standard: db/migration)
                .load();
    }
}
```
- `locations`: Zeigt auf den Speicherort Ihrer Migrationsdateien (z.B. `src/main/resources/db/migration` für den Classpath).
- Andere häufige Konfigurationen: `.baselineOnMigrate(true)` zum Baselinieren existierender Schemas oder `.table("flyway_schema_history")` zum Anpassen der History-Tabelle.

### Schritt 3: Migrationsskripte schreiben
Migrationsskripte sind SQL-Dateien, die am konfigurierten Ort abgelegt werden (z.B. `src/main/resources/db/migration`). Flyway wendet sie in Reihenfolge an.

#### Namenskonventionen
- **Versionierte Migrationen** (für einmalige Schemaänderungen): `V<Version>__<Beschreibung>.sql` (z.B. `V1__Create_person_table.sql`, `V2__Add_age_column.sql`).
  - Versionsformat: Verwenden Sie Unterstriche für Segmente (z.B. `V1_1__Initial.sql`).
- **Wiederholbare Migrationen** (für laufende Aufgaben wie Views): `R__<Beschreibung>.sql` (z.B. `R__Update_view.sql`). Diese werden bei jeder Änderung erneut ausgeführt.
- Dateien werden in lexikografischer Reihenfolge angewendet.

#### Beispielskripte
Erstellen Sie diese Dateien in `src/main/resources/db/migration`.

**V1__Create_person_table.sql**:
```sql
CREATE TABLE person (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO person (id, name) VALUES (1, 'John Doe');
```

**V2__Add_age_column.sql**:
```sql
ALTER TABLE person ADD COLUMN age INT;
```

**R__Populate_names.sql** (wiederholbar):
```sql
UPDATE person SET name = CONCAT(name, ' (Updated)') WHERE id = 1;
```

Flyway verfolgt angewendete Migrationen in einer `flyway_schema_history`-Tabelle.

Für komplexe Logik, die nicht für SQL geeignet ist, verwenden Sie Java-basierte Migrationen (implementieren Sie `org.flywaydb.core.api.migration.java.JavaMigration`).

### Schritt 4: Migrationen programmatisch ausführen
Rufen Sie `migrate()` auf, um ausstehende Migrationen anzuwenden. Integrieren Sie dies in den Start Ihrer App (z.B. in `main()` oder einem Spring `@PostConstruct`).

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
            flyway.migrate();  // Wendet alle ausstehenden Migrationen an
            System.out.println("Datenbank-Migration erfolgreich!");
        } catch (FlywayException e) {
            System.err.println("Migration fehlgeschlagen: " + e.getMessage());
            // Fehler behandeln (z.B. Beenden oder Rollback)
        }

        // Starten Sie nun den Rest Ihrer Anwendung
    }
}
```

- `migrate()`: Wendet versionierte Migrationen in Reihenfolge an, dann wiederholbare.
- Andere Befehle: `flyway.info()` für Status, `flyway.repair()` zum Beheben von Problemen, `flyway.validate()` zur Konsistenzprüfung.
- Führen Sie dies vor allen Datenbankoperationen aus, um Schema-Kompatibilität sicherzustellen.

### Best Practices
- Halten Sie Migrationen idempotent (sicher zum erneuten Ausführen).
- Testen Sie Migrationen auf einer Kopie der Produktionsdaten.
- Verwenden Sie Versionskontrolle für Migrationsdateien.
- Für Spring Boot: Fügen Sie `spring-boot-starter-jdbc` hinzu und setzen Sie `spring.flyway.enabled=true` in `application.properties` für die Auto-Konfiguration.

### Referenzen
- [Flyway API (Java) Dokumentation](https://documentation.red-gate.com/fd/api-java-277579358.html)
- [Flyway Migrations Dokumentation](https://documentation.red-gate.com/fd/migrations-271585107.html)
- [Flyway Getting Started](https://documentation.red-gate.com/fd/getting-started-with-flyway-184127223.html)