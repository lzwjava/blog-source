---
audio: false
generated: true
lang: de
layout: post
title: Berechtigung für PostgreSQL-Datenbankzugriff
translated: true
type: note
---

Um einem Benutzer Zugriff auf eine Datenbank in PostgreSQL zu gewähren, müssen Sie die folgenden Schritte ausführen. Ich werde Sie durch den Prozess mit SQL-Befehlen in der psql-Kommandozeilenschnittstelle führen.

Verbinden mit PostgreSQL: Sie haben bereits eine Verbindung zu PostgreSQL mit dem postgres-Benutzer hergestellt, der in der Regel Superuser-Rechte besitzt.

Benutzer erstellen (falls noch nicht vorhanden): Wenn der Benutzer nicht existiert, können Sie einen mit dem folgenden Befehl erstellen. Ersetzen Sie username und password durch den gewünschten Benutzernamen und das Passwort.

```
CREATE USER username WITH PASSWORD 'password';
```

Datenbank erstellen (falls noch nicht vorhanden): Wenn die Datenbank nicht existiert, können Sie sie mit dem folgenden Befehl erstellen. Ersetzen Sie database_name durch den gewünschten Datenbanknamen.

```
CREATE DATABASE database_name;
```

Berechtigungen für die Datenbank erteilen: Um alle Berechtigungen für eine bestimmte Datenbank an den Benutzer zu erteilen, verwenden Sie den folgenden Befehl. Ersetzen Sie database_name und username durch die entsprechenden Namen.

```
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
```

Nutzung des Schemas erlauben: Wenn der Benutzer Zugriff auf ein bestimmtes Schema innerhalb der Datenbank haben soll, können Sie die Nutzung des Schemas erlauben. Ersetzen Sie schema_name und username durch die entsprechenden Namen.

```
GRANT USAGE ON SCHEMA schema_name TO username;
```

Berechtigungen für Tabellen erteilen: Um bestimmte Berechtigungen für Tabellen innerhalb eines Schemas zu erteilen, können Sie den folgenden Befehl verwenden. Ersetzen Sie schema_name, table_name und username durch die entsprechenden Namen.

```
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA schema_name TO username;
```

Berechtigungen wirksam machen: Wenn Sie Berechtigungen für Tabellen erteilt haben, müssen Sie möglicherweise auch Standardberechtigungen für zukünftige Tabellen festlegen.

```
ALTER DEFAULT PRIVILEGES IN SCHEMA schema_name GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO username;
```

Hier ist ein Beispiel, wie die Befehle aussehen könnten:

```
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE mydatabase;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
\c mydatabase
GRANT USAGE ON SCHEMA public TO myuser;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myuser;
```

Diese Befehle richten einen Benutzer mit vollem Zugriff auf eine bestimmte Datenbank und deren Tabellen ein. Passen Sie die Befehle entsprechend Ihren spezifischen Anforderungen und Sicherheitsrichtlinien an.