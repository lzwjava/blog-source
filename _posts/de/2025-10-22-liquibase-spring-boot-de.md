---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Integration von Liquibase mit Spring Boot
translated: true
type: note
---

## Integration von Liquibase mit Spring Boot

Liquibase ist ein beliebtes Open-Source-Tool zur versionskontrollierten Verwaltung von Datenbankschema-Änderungen (Migrationen). Spring Boot bietet eine ausgezeichnete Auto-Configuration-Unterstützung für Liquibase, was die Integration einfach macht. Diese Anleitung geht davon aus, dass Sie Spring Boot 3.x (das aktuellste Stand 2025) mit Maven verwenden, aber die Konzepte gelten auch für Gradle. Wir behandeln die Grundlagen Schritt für Schritt.

### Voraussetzungen
- Ein eingerichtetes Spring Boot-Projekt (z.B. über Spring Initializr).
- Eine Datenbank (z.B. H2 für Tests, PostgreSQL/MySQL für den Produktiveinsatz), konfiguriert in `application.properties`.

### Schritt 1: Liquibase-Abhängigkeit hinzufügen
Fügen Sie den Liquibase Spring Boot Starter in Ihre `pom.xml` ein. Dies bindet Liquibase nahtlos ein.

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId> <!-- Für Datenbankkonnektivität -->
</dependency>
```

Für Gradle, fügen Sie in `build.gradle` hinzu:
```groovy
implementation 'org.liquibase:liquibase-core'
implementation 'org.springframework.boot:spring-boot-starter-jdbc'
```

Führen Sie `mvn clean install` (oder `./gradlew build`) aus, um die Abhängigkeiten zu laden.

### Schritt 2: Liquibase konfigurieren
Spring Boot erkennt Liquibase automatisch, wenn Sie Changelog-Dateien am Standardort ablegen. Passen Sie die Konfiguration über `application.properties` (oder das `.yml`-Äquivalent) an.

Beispiel `application.properties`:
```properties
# Datenbank-Einrichtung (an Ihre DB anpassen)
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driver-class-name=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# Liquibase-Konfiguration
spring.liquibase.change-log=classpath:db/changelog/db.changelog-master.xml
spring.liquibase.enabled=true  # Standard ist true
spring.liquibase.drop-first=false  # Für Dev auf true setzen, um Schema beim Start zu löschen
```

- `change-log`: Pfad zu Ihrer Master-Changelog-Datei (Standard: `db/changelog/db.changelog-master.xml`).
- Aktivieren/Deaktivieren mit `spring.liquibase.enabled`.
- Für Kontexte/Profile verwenden Sie `spring.liquibase.contexts=dev`, um spezifische Changesets auszuführen.

### Schritt 3: Changelog-Dateien erstellen
Liquibase verwendet "Changelogs", um Schemaänderungen zu definieren. Erstellen Sie eine Verzeichnisstruktur unter `src/main/resources`:
```
src/main/resources/
└── db/
    └── changelog/
        ├── db.changelog-master.xml  # Master-Datei, die andere einschließt
        └── changes/
            ├── 001-create-users-table.xml  # Einzelne Änderungen
            └── 002-add-email-column.xml
```

#### Master-Changelog (`db.changelog-master.xml`)
Diese Datei schließt andere Changelogs ein:
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

#### Beispiel-Change (`001-create-users-table.xml`)
Definieren Sie eine Tabellenerstellung:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                                       http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.24.xsd">

    <changeSet id="001" author="yourname">
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

- Verwenden Sie XML, YAML, JSON oder SQL-Formate für Changelogs.
- Jedes `<changeSet>` ist eine Migration mit einer ID (zur Verfolgung).
- Führen Sie `java -jar target/your-app.jar` aus, um die App zu starten – Liquibase wendet Änderungen automatisch beim Bootstrap an.

### Schritt 4: Ausführung und Tests
- **Beim Start**: Spring Boot führt Liquibase aus, bevor Ihre App vollständig startet.
- **Rollback**: Verwenden Sie `spring.liquibase.rollback-file` oder die CLI für Tests.
- **CLI-Integration**: Für manuelle Ausführung fügen Sie das Liquibase Maven-Plugin hinzu:
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
  Führen Sie dann `mvn liquibase:update` aus.

- **Validierung**: Aktivieren Sie `spring.liquibase.validate-on-migrate=true`, um Changelogs zu prüfen.

### Häufige Tipps
- **Profile**: Verwenden Sie `@Profile("dev")` auf Beans bei Bedarf, aber Liquibase läuft global, sofern nicht gefiltert.
- **Preconditions**: Fügen Sie `<preConditions>` in Changesets ein, um den DB-Zustand zu prüfen.
- **SQL-Format**: Für rohes SQL erstellen Sie `.sql`-Dateien und schließen sie ein: `<sqlFile path="changes/create-users.sql" relativeToChangelogFile="true"/>`.
- **Fehlerbehebung**: Prüfen Sie die Logs auf Fehler (z.B. mit `liquibase`-Präfix). Stellen Sie sicher, dass die DB-URL korrekt ist.
- **Produktion**: Verwenden Sie Flyway, wenn Sie es bevorzugen, aber Liquibase glänzt bei komplexen Änderungen und Multi-DB-Unterstützung.

Für erweiterte Funktionen wie getaggte Rollbacks oder benutzerdefinierte Erweiterungen konsultieren Sie die Dokumentation.

### Referenzen
- [Spring Boot Liquibase Auto-Configuration](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#io.liquibase)
- [Liquibase Official Documentation](https://docs.liquibase.com/start/home.html)
- [Baeldung Spring Boot + Liquibase Tutorial](https://www.baeldung.com/liquibase-refactor-schema-of-jpa-entity-in-spring-boot)