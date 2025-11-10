---
audio: false
generated: true
lang: de
layout: post
title: Erstellen Sie eine PostgreSQL-Datenbank
translated: true
type: note
---

Sie befinden sich bereits im PostgreSQL-Interaktivterminal (`psql`) als `postgres`-Benutzer, was großartig ist! Um eine Datenbank in PostgreSQL zu erstellen, können Sie den Befehl `CREATE DATABASE` verwenden. Hier ist eine Schritt-für-Schritt-Anleitung:

1. **Stellen Sie sicher, dass Sie in `psql` sind**:
   Das sind Sie bereits, wie durch die Eingabeaufforderung `postgres=#` gezeigt.

2. **Erstellen Sie eine Datenbank**:
   Verwenden Sie den folgenden Befehl, um eine neue Datenbank zu erstellen. Ersetzen Sie `mydatabase` durch Ihren gewünschten Datenbanknamen:

   ```sql
   CREATE DATABASE mydatabase;
   ```

   Dies erstellt eine Datenbank namens `mydatabase`.

3. **Überprüfen Sie, ob die Datenbank erstellt wurde**:
   Listen Sie alle Datenbanken zur Bestätigung auf:

   ```sql
   \l
   ```

   Dies zeigt eine Tabelle aller Datenbanken an, einschließlich `mydatabase`.

4. **Verbinden Sie sich mit der neuen Datenbank**:
   Um in der neuen Datenbank zu arbeiten, verbinden Sie sich mit:

   ```sql
   \c mydatabase
   ```

   Dies wechselt Ihre Sitzung zu `mydatabase`.

5. **Optional: Erstellen Sie einen Benutzer und erteilen Sie Berechtigungen**:
   Wenn ein bestimmter Benutzer diese Datenbank verwalten soll, erstellen Sie einen und gewähren Sie Berechtigungen:

   ```sql
   CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
   GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
   ```

   Ersetzen Sie `myuser` und `mypassword` durch Ihren gewünschten Benutzernamen und Ihr Passwort.

6. **Beenden Sie `psql`**:
   Wenn Sie fertig sind, beenden Sie mit:

   ```sql
   \q
   ```

### Hinweise:
- Der `Permission denied`-Fehler, den Sie gesehen haben (`could not change directory to "/home/lzw/projects/lzwjava.github.io"`), tritt auf, weil der `postgres`-Benutzer keinen Zugriff auf Ihr Home-Verzeichnis hat. Dies beeinflusst nicht die Datenbankerstellung, kann aber auftreten, wenn `psql` aus einem eingeschränkten Verzeichnis ausgeführt wird. Sie können dies vermeiden, indem Sie `psql` aus einem Verzeichnis ausführen, auf das der `postgres`-Benutzer Zugriff hat, oder indem Sie Verzeichniswechsel vermeiden (z.B. führen Sie `sudo -u postgres psql` aus `/tmp` aus).
- Der `ls`-Befehl, den Sie in `psql` versucht haben, ist nicht gültig. Verwenden Sie `\l`, um Datenbanken aufzulisten, oder `\dt`, um Tabellen innerhalb einer Datenbank aufzulisten.
- Stellen Sie sicher, dass der PostgreSQL-Dienst läuft (`sudo systemctl start postgresql.service`), was Sie bereits getan haben.

### Beispiel-Sitzung:
```sql
postgres=# CREATE DATABASE mydatabase;
CREATE DATABASE
postgres=# \l
                                  List of databases
   Name      |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-------------+----------+----------+-------------+-------------+-----------------------
 mydatabase  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
(4 rows)

postgres=# \c mydatabase
You are now connected to database "mydatabase" as user "postgres".
mydatabase=# \q
```

Wenn Sie weitere Hilfe benötigen (z.B. beim Einrichten von Tabellen, Benutzern oder beim Verbinden von einer Anwendung), lassen Sie es mich wissen!