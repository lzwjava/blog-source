---
audio: false
generated: true
lang: de
layout: post
title: 'Liquibase: Datenbankschemaverwaltung'
translated: true
type: note
---

Hier ist eine umfassende Anleitung zur Verwendung von **Liquibase** in einer Spring Boot-Anwendung, um Ihre Datenbankschema-Änderungen effektiv zu verwalten:

---

### 1. Liquibase-Abhängigkeit hinzufügen
Um zu beginnen, müssen Sie die Liquibase-Abhängigkeit in Ihr Projekt aufnehmen. Wenn Sie **Maven** verwenden, fügen Sie dies Ihrer `pom.xml` hinzu:

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
```

Für **Gradle** fügen Sie dies Ihrer `build.gradle` hinzu:

```groovy
implementation 'org.liquibase:liquibase-core'
```

Dies bindet die Liquibase-Kernbibliothek in Ihr Projekt ein.

---

### 2. Liquibase konfigurieren
Liquibase verwendet eine **Changelog-Datei**, um Datenbankschema-Änderungen zu verwalten. Standardmäßig sucht Spring Boot nach einer Datei namens `db/changelog/db.changelog-master.yaml`, `db/changelog/db.changelog-master.xml` oder `db/changelog/db.changelog-master.sql` im Classpath. Sie können diesen Speicherort anpassen, indem Sie eine Eigenschaft in Ihrer `application.properties` (oder `application.yml`) hinzufügen:

```properties
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

Dies teilt Spring Boot mit, wo es Ihre Changelog-Datei finden kann.

---

### 3. Eine Changelog-Datei erstellen
Die Changelog-Datei definiert die Änderungen, die Sie auf Ihre Datenbank anwenden möchten. Sie können sie in Formaten wie XML, YAML oder SQL schreiben. Hier ist ein Beispiel für eine **XML-Changelog-Datei** unter `src/main/resources/db/changelog/db.changelog-master.xml`:

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

Dieses Beispiel erstellt eine Tabelle `users` mit drei Spalten: `id`, `username` und `email`. Jedes `<changeSet>` repräsentiert einen Satz von anzuwendenden Änderungen.

---

### 4. Ihre Spring Boot-Anwendung ausführen
Wenn Sie Ihre Spring Boot-Anwendung starten, führt Liquibase automatisch folgende Schritte aus:
- Liest die Changelog-Datei.
- Prüft, welche Changesets bereits angewendet wurden (verfolgt in einer Tabelle namens `DATABASECHANGELOG`).
- Führt alle neuen Changesets gegen Ihre Datenbank aus.

Es ist kein zusätzlicher Code erforderlich – die Auto-Konfiguration von Spring Boot erledigt dies für Sie.

---

### 5. Liquibase anpassen (Optional)
Sie können das Verhalten von Liquibase mit Eigenschaften in `application.properties` anpassen. Hier sind einige gängige Optionen:

```properties
spring.liquibase.enabled=true          # Liquibase aktivieren oder deaktivieren
spring.liquibase.drop-first=false      # Datenbank vor dem Anwenden von Änderungen löschen (mit Vorsicht verwenden)
spring.liquibase.contexts=dev,prod     # Changesets nur in bestimmten Kontexten ausführen
```

Diese Einstellungen ermöglichen es Ihnen, Liquibase an Ihre Umgebung oder Ihren Workflow anzupassen.

---

### 6. Erweiterte Funktionen nutzen
Liquibase bietet leistungsstarke Funktionen zur Verbesserung des Schema-Managements:
- **Kontexte und Labels**: Steuern Sie, welche Changesets in bestimmten Umgebungen ausgeführt werden (z.B. `dev` vs. `prod`).
- **Preconditions**: Stellen Sie sicher, dass bestimmte Bedingungen (z.B. eine Tabelle existiert) erfüllt sind, bevor ein Changeset angewendet wird.
- **Rollbacks**: Definieren Sie, wie ein Changeset bei Bedarf rückgängig gemacht werden kann.
- **Refactoring**: Nutzen Sie integrierte Unterstützung für komplexe Datenbankänderungen (z.B. das Umbenennen von Spalten).

Ein Beispiel für das Hinzufügen eines Kontexts zu einem Changeset:

```xml
<changeSet id="2" author="your-name" context="dev">
    <addColumn tableName="users">
        <column name="created_at" type="timestamp"/>
    </addColumn>
</changeSet>
```

Dieses Changeset wird nur im Kontext `dev` ausgeführt.

---

### 7. Mit einer In-Memory-Datenbank testen
Verwenden Sie für Tests Liquibase in Kombination mit einer In-Memory-Datenbank wie H2. Fügen Sie die H2-Abhängigkeit hinzu:

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

Konfigurieren Sie dann Ihre `application.properties` für Tests:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

Liquibase wendet Ihre Änderungen während der Tests auf die In-Memory-Datenbank an.

---

### 8. Changelog unter Versionskontrolle stellen
Speichern Sie Ihre Changelog-Dateien zusammen mit Ihrem Anwendungscode unter Versionskontrolle (z.B. Git). Dies stellt sicher, dass sich Ihr Datenbankschema synchron mit Ihrer Codebasis entwickelt, was Bereitstellungen und Rollbacks vorhersehbarer macht.

---

### Zusammenfassung
So verwenden Sie Liquibase in einer Spring Boot-Anwendung:
1. Fügen Sie die Liquibase-Abhängigkeit hinzu.
2. Konfigurieren Sie den Speicherort der Changelog-Datei.
3. Erstellen Sie eine Changelog-Datei mit Ihren Datenbankänderungen.
4. Führen Sie Ihre Anwendung aus – Liquibase erledigt den Rest.

Liquibase ist ein robustes Tool zur strukturierten, versionskontrollierten Verwaltung von Datenbankschema-Änderungen, das nahtlos in Spring Boot integriert ist.