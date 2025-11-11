---
audio: false
generated: true
lang: de
layout: post
title: Oracle-Datenbank - Benutzerkonto
translated: true
type: note
---

Der Fehler `ORA-28000: The account is locked` tritt auf, wenn versucht wird, eine Verbindung zu einer Oracle-Datenbank herzustellen (z. B. über einen Thin-JDBC-Treiber) und das verwendete Benutzerkonto gesperrt wurde. Dies geschieht typischerweise aufgrund zu vieler fehlgeschlagener Anmeldeversuche, manueller Sperrung durch einen Administrator oder einer Richtlinie zur Kontoverfall. Um das Problem zu beheben, müssen Sie das Konto entsperren und gegebenenfalls das Passwort zurücksetzen oder den Kontostatus überprüfen. Im Folgenden finden Sie die Schritte zur Lösung dieses Problems bei der Verbindung zu einer Oracle-Datenbank.

---

### Schritte zur Behebung von ORA-28000

#### 1. **Fehler überprüfen**
   Wenn dieser Fehler in einer JDBC-Verbindung auftritt, könnte er wie folgt aussehen:
   ```
   java.sql.SQLException: ORA-28000: The account is locked
   ```
   Dies bestätigt, dass das Problem beim Datenbankkonto liegt, nicht bei der JDBC-Konfiguration selbst (z. B. URL, Treiber oder WebSphere-Datenquelleneinstellungen).

#### 2. **Als berechtigter Benutzer anmelden**
   Um das Konto zu entsperren, benötigen Sie Zugriff auf einen Datenbankbenutzer mit Administratorrechten (z. B. `SYS`, `SYSTEM` oder einen Benutzer mit der `DBA`-Rolle). Verbinden Sie sich mit der Datenbank über ein Tool wie SQL*Plus, SQL Developer oder einen JDBC-Client:
   ```bash
   sqlplus / as sysdba
   ```
   ODER
   ```bash
   sqlplus system/<password>@<service_name>
   ```
   Ersetzen Sie `<password>` und `<service_name>` durch Ihre tatsächlichen Anmeldedaten und den Datenbank-Service-Namen (z. B. `ORCL`).

#### 3. **Kontostatus überprüfen**
   Führen Sie die folgende SQL-Abfrage aus, um den Status des gesperrten Kontos zu überprüfen:
   ```sql
   SELECT username, account_status, lock_date
   FROM dba_users
   WHERE username = 'YOUR_USERNAME';
   ```
   - Ersetzen Sie `YOUR_USERNAME` durch den Benutzernamen, mit dem Sie sich verbinden möchten (z. B. `myuser`).
   - Sehen Sie sich die Spalte `ACCOUNT_STATUS` an. Wenn dort `LOCKED` oder `LOCKED(TIMED)` steht, ist das Konto gesperrt.

   Beispielausgabe:
   ```
   USERNAME   ACCOUNT_STATUS   LOCK_DATE
   ---------- ---------------- -------------------
   MYUSER     LOCKED           24-MAR-25 10:00:00
   ```

#### 4. **Konto entsperren**
   Um das Konto zu entsperren, führen Sie diesen SQL-Befehl als berechtigter Benutzer aus:
   ```sql
   ALTER USER your_username ACCOUNT UNLOCK;
   ```
   Beispiel:
   ```sql
   ALTER USER myuser ACCOUNT UNLOCK;
   ```

#### 5. **(Optional) Passwort zurücksetzen**
   Falls das Passwort möglicherweise abgelaufen ist oder Sie vermuten, dass es falsch ist, setzen Sie es gleich zurück:
   ```sql
   ALTER USER your_username IDENTIFIED BY new_password;
   ```
   Beispiel:
   ```sql
   ALTER USER myuser IDENTIFIED BY mynewpass123;
   ```
   - Aktualisieren Sie nach dem Zurücksetzen das Passwort in Ihrer WebSphere `server.xml` (oder wo auch immer die JDBC-Datenquelle konfiguriert ist) und verschlüsseln Sie es erneut, falls erforderlich (siehe Ihre vorherige Frage für die AES-Verschlüsselungsschritte).

#### 6. **Änderungen committen (falls erforderlich)**
   In den meisten Fällen werden `ALTER USER`-Befehle sofort wirksam und erfordern keinen `COMMIT`. Wenn Sie sich jedoch in einer transaktionsintensiven Umgebung befinden, stellen Sie sicher, dass kein Rollback erfolgt, indem Sie die Sitzung oder bei Bedarf die Datenbank neu starten.

#### 7. **Verbindung testen**
   Versuchen Sie erneut, eine Verbindung mit Ihrer JDBC-Anwendung oder einem einfachen Test herzustellen:
   ```java
   import java.sql.Connection;
   import java.sql.DriverManager;

   public class TestJDBC {
       public static void main(String[] args) throws Exception {
           String url = "jdbc:oracle:thin:@//localhost:1521/ORCL";
           String user = "myuser";
           String password = "mynewpass123";
           Connection conn = DriverManager.getConnection(url, user, password);
           System.out.println("Connection successful!");
           conn.close();
       }
   }
   ```
   - Aktualisieren Sie `url`, `user` und `password` entsprechend Ihrer Umgebung.
   - Wenn dies funktioniert, passen Sie Ihre WebSphere-Datenquellenkonfiguration entsprechend an.

#### 8. **Profilrichtlinien überprüfen (zukünftige Sperren verhindern)**
   Das Konto könnte aufgrund einer Sicherheitsrichtlinie im Profil des Benutzers gesperrt worden sein (z. B. `FAILED_LOGIN_ATTEMPTS` oder `PASSWORD_LOCK_TIME`). Überprüfen Sie das dem Benutzer zugewiesene Profil:
   ```sql
   SELECT profile
   FROM dba_users
   WHERE username = 'YOUR_USERNAME';
   ```
   Untersuchen Sie dann die Grenzwerte des Profils:
   ```sql
   SELECT resource_name, limit
   FROM dba_profiles
   WHERE profile = 'YOUR_PROFILE_NAME';
   ```
   Suchen Sie nach:
   - `FAILED_LOGIN_ATTEMPTS`: Anzahl fehlgeschlagener Versuche vor der Sperrung (z. B. `10`).
   - `PASSWORD_LOCK_TIME`: Dauer der Sperre (z. B. `1` Tag).

   Um diese Einstellungen zu lockern (falls angemessen), ändern Sie das Profil:
   ```sql
   ALTER PROFILE your_profile_name LIMIT
       FAILED_LOGIN_ATTEMPTS UNLIMITED
       PASSWORD_LOCK_TIME UNLIMITED;
   ```
   Beispiel:
   ```sql
   ALTER PROFILE DEFAULT LIMIT FAILED_LOGIN_ATTEMPTS UNLIMITED;
   ```

#### 9. **WebSphere neu starten (falls erforderlich)**
   Wenn Sie WebSphere verwenden und das Datenquellen-Passwort aktualisiert haben, starten Sie den Anwendungsserver neu, um sicherzustellen, dass die Änderungen wirksam werden:
   - Für Liberty: `./bin/server stop` und `./bin/server start`.
   - Für traditionelles WebSphere: Verwenden Sie die Admin Console oder `stopServer.sh`/`startServer.sh`.

---

### Häufige Ursachen für ORA-28000
- **Zu viele fehlgeschlagene Anmeldeversuche**: Überprüfen Sie die Anwendungsprotokolle oder WebSphere-Protokolle (z. B. `SystemOut.log`) auf vorherige Verbindungsfehler.
- **Manuelle Sperre**: Ein Administrator hat das Konto möglicherweise absichtlich gesperrt (`ALTER USER myuser ACCOUNT LOCK`).
- **Abgelaufenes Konto**: In einigen Umgebungen werden Konten gesperrt, wenn Passwörter ablaufen. Überprüfen Sie `EXPIRY_DATE` in `dba_users`.

---

### Tipps zur Fehlerbehebung
- Wenn Sie keinen `SYS`- oder `SYSTEM`-Zugriff haben, wenden Sie sich an Ihren Datenbankadministrator, um das Konto entsperren zu lassen.
- Stellen Sie sicher, dass die JDBC-URL, der Benutzername und das Passwort in `server.xml` korrekt sind, bevor Sie es erneut versuchen.
- Wenn das Problem weiterhin besteht, überprüfen Sie, ob der Oracle-Listener läuft:
  ```bash
  lsnrctl status
  ```

Lassen Sie mich wissen, wenn Sie auf weitere Fehler stoßen oder Hilfe bei einem bestimmten Schritt benötigen!