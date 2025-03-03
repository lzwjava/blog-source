---
audio: false
generated: true
lang: de
layout: post
title: SQuirreL SQL Client und DB2-Datenbank
translated: true
---

Um Ihre IBM DB2 JCC JAR-Datei (`db2jcc.jar`) in SQuirreL SQL Client zu verwenden und eine Verbindung zu einer DB2-Datenbank herzustellen, befolgen Sie diese detaillierten Schritte. Dieser Prozess umfasst die Konfiguration des DB2-Treibers in SQuirreL und die Einrichtung eines Verbindungs-Alias.

---

### Schritt 1: Überprüfen der JAR-Datei
- Stellen Sie sicher, dass Sie die richtige DB2 JDBC-Treiber JAR-Datei haben. Die von Ihnen erwähnte Datei, `db2jcc.jar`, ist normalerweise die richtige für IBM DB2, obwohl einige Setups möglicherweise `db2jcc4.jar` verwenden, abhängig von der Version.
- Überprüfen Sie, ob Ihre DB2-Installation eine zusätzliche Lizenzdatei (z. B. `db2jcc_license_cisuz.jar`) erfordert. Falls ja, finden Sie diese Datei ebenfalls, da sie benötigt werden könnte, um lizenzbezogene Fehler bei der Verbindung zu vermeiden.

---

### Schritt 2: Konfigurieren des DB2-Treibers in SQuirreL SQL Client
1. **SQuirreL SQL Client öffnen**:
   - Starten Sie die Anwendung auf Ihrem System.

2. **Auf den Treiber-Tab zugreifen**:
   - Klicken Sie im linken Bereich auf den **Treiber** Tab, um die Liste der verfügbaren Datenbanktreiber anzuzeigen.

3. **DB2-Treiber finden oder hinzufügen**:
   - Suchen Sie nach einem vorhandenen DB2-Treiber in der Liste (z. B. "IBM DB2 App Driver"). Er könnte mit einem roten X markiert sein, wenn er nicht richtig konfiguriert ist.
   - Wenn er vorhanden ist, können Sie ihn ändern. Wenn nicht, müssen Sie einen neuen Treiber erstellen:
     - **Existierenden Treiber ändern**: Doppelklicken Sie auf den DB2-Treiber-Eintrag.
     - **Neuen Treiber hinzufügen**: Klicken Sie auf das **+** Symbol im Treiber-Tab, um den "Treiber hinzufügen"-Assistenten zu öffnen.

4. **Treiber-Einstellungen konfigurieren**:
   - **Name**: Geben Sie einen beschreibenden Namen ein, wie z. B. "IBM DB2 JCC Treiber."
   - **Beispiel-URL**: Setzen Sie dies auf `jdbc:db2://<host>:<port>/<database>` (Sie werden dies später für Ihre spezifische Datenbank anpassen).
   - **Klassenname**: Geben Sie `com.ibm.db2.jcc.DB2Driver` ein (dies ist die Standard-Treiberklasse für DB2 JDBC).

5. **JAR-Datei hinzufügen**:
   - Gehen Sie zum **Extra Class Path** Tab im Treiber-Konfigurationsfenster.
   - Klicken Sie auf **Hinzufügen**, dann durchsuchen Sie den Speicherort Ihrer `db2jcc.jar` Datei.
   - Wenn Sie eine Lizenz-JAR (z. B. `db2jcc_license_cisuz.jar`) haben, klicken Sie erneut auf **Hinzufügen** und fügen Sie diese ebenfalls hinzu.

6. **Konfiguration speichern**:
   - Klicken Sie auf **OK**, um die Treiber-Einstellungen zu speichern. Der DB2-Treiber sollte nun im Treiber-Tab mit einem Häkchen erscheinen, was bedeutet, dass er richtig konfiguriert ist.

---

### Schritt 3: Erstellen eines Datenbank-Alias
1. **Zum Alias-Tab wechseln**:
   - Klicken Sie im linken Bereich auf den **Alias** Tab, der Ihre Datenbankverbindungen verwaltet.

2. **Neuen Alias hinzufügen**:
   - Klicken Sie auf das **+** Symbol, um den "Alias hinzufügen"-Assistenten zu öffnen.

3. **Alias konfigurieren**:
   - **Name**: Geben Sie Ihrer Verbindung einen Namen (z. B. "Meine DB2-Datenbank").
   - **Treiber**: Wählen Sie aus der Dropdown-Liste den DB2-Treiber, den Sie in Schritt 2 konfiguriert haben (z. B. "IBM DB2 JCC Treiber").
   - **URL**: Geben Sie die Verbindungs-URL für Ihre Datenbank im Format ein:
     ```
     jdbc:db2://<host>:<port>/<database>
     ```
     Ersetzen Sie `<host>` (z. B. `localhost` oder die IP-Adresse Ihres Servers), `<port>` (z. B. `50000`, der Standard-DB2-Port) und `<database>` (Ihr Datenbankname) durch Ihre tatsächlichen Details. Zum Beispiel:
     ```
     jdbc:db2://localhost:50000/mydb
     ```
   - **Benutzername** und **Kennwort**: Geben Sie Ihre DB2-Datenbank-Anmeldeinformationen ein.

4. **Speichern und verbinden**:
   - Klicken Sie auf **OK**, um den Alias zu speichern.
   - Klicken Sie im Alias-Tab doppelt auf Ihren neuen Alias, um eine Verbindung herzustellen. Geben Sie Ihr Kennwort ein, wenn Sie dazu aufgefordert werden.

---

### Potenzielle Probleme und Lösungen
- **Lizenzfehler**:
  - Wenn Sie einen Fehler wie "The IBM Data Server for JDBC and SQLJ license was invalid" sehen, stellen Sie sicher, dass die Lizenz-JAR (z. B. `db2jcc_license_cisuz.jar`) zum Extra Class Path des Treibers hinzugefügt wurde.
- **Klasse nicht gefunden Fehler**:
  - Wenn SQuirreL meldet "Could not find class com.ibm.db2.jcc.DB2Driver", überprüfen Sie:
    - Die `db2jcc.jar` Datei ist korrekt zum Extra Class Path hinzugefügt.
    - Der Klassenname ist auf `com.ibm.db2.jcc.DB2Driver` gesetzt, ohne Rechtschreibfehler.
- **Mehrere JAR-Konflikte**:
  - Vermeiden Sie das Hinzufügen mehrerer Versionen des DB2 JDBC-Treibers (z. B. sowohl `db2jcc.jar` als auch `db2jcc4.jar`) zum Extra Class Path, da dies zu Konflikten führen kann. Verwenden Sie nur die JARs, die für Ihre DB2-Version erforderlich sind.
- **Falsches URL-Format**:
  - Überprüfen Sie die Syntax Ihrer Verbindungs-URL. Eine fehlerhafte URL (z. B. fehlender Port oder falscher Datenbankname) verhindert die Verbindung.

---

Durch die Befolgung dieser Schritte sollten Sie in der Lage sein, SQuirreL SQL Client so zu konfigurieren, dass er Ihre `db2jcc.jar` Datei verwendet und erfolgreich eine Verbindung zu Ihrer DB2-Datenbank herstellt. Wenn Sie auf Probleme stoßen, überprüfen Sie die oben genannten Fehlerbehebungs-Tipps oder stellen Sie sicher, dass Ihr Datenbankserver von Ihrem Netzwerk aus zugänglich ist.