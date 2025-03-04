---
audio: false
generated: true
lang: de
layout: post
title: Oracle JDBC-Treiber zu Squirrel SQL Client hinzufügen
translated: true
---

Um den Oracle JDBC-Treiber zu Squirrel SQL Client hinzuzufügen, befolgen Sie diese detaillierten Schritte. Dieser Prozess umfasst die Konfiguration des Treibers und die Einrichtung eines Verbindungsalias für Ihre Oracle-Datenbank.

### Schritt 1: Die erforderliche Datei finden
Sie benötigen die Oracle JDBC-Treiberdatei, speziell `ojdbc.jar`. Diese Datei enthält die notwendigen Klassen, um Squirrel SQL Client eine Verbindung zu einer Oracle-Datenbank herzustellen. Stellen Sie sicher, dass Sie diese Datei heruntergeladen haben (z.B. von der Oracle-Website oder Ihrem Datenbankadministrator) und wissen, wo sie sich auf Ihrem System befindet.

### Schritt 2: Squirrel SQL Client starten
Öffnen Sie die Squirrel SQL Client-Anwendung auf Ihrem Computer.

### Schritt 3: Auf den Treiber-Tab zugreifen
Auf der linken Seite der Squirrel SQL Client-Oberfläche finden und klicken Sie auf den **Treiber** Tab. Dieser Abschnitt ermöglicht es Ihnen, die JDBC-Treiber zu verwalten, die der Anwendung zur Verfügung stehen.

### Schritt 4: Einen neuen Treiber hinzufügen
- Im Treiber-Tab klicken Sie auf die **"+"** Schaltfläche, um das Dialogfeld "Treiber hinzufügen" zu öffnen.

### Schritt 5: Den Treiber benennen
- Im Feld "Name" des Dialogfelds "Treiber hinzufügen" geben Sie **Oracle Thin Driver** ein. Dies ist ein beschreibender Name, um den Oracle-Treiber innerhalb von Squirrel SQL Client zu identifizieren.

### Schritt 6: Die `ojdbc.jar`-Datei hinzufügen
- Wechseln Sie zur Registerkarte **Extra Class Path** im Dialogfeld "Treiber hinzufügen".
- Klicken Sie auf die **Hinzufügen** Schaltfläche.
- Navigieren Sie zu dem Speicherort der `ojdbc.jar`-Datei auf Ihrem System, wählen Sie sie aus und bestätigen Sie, um sie zum Klassenpfad des Treibers hinzuzufügen.

### Schritt 7: Die Java-Treiberklasse angeben
- Im Feld "Klassenname" geben Sie die Java-Treiberklasse ein: **oracle.jdbc.OracleDriver**. Dies teilt Squirrel SQL Client mit, welche Klasse aus der `ojdbc.jar`-Datei verwendet werden soll, um Oracle-Datenbankverbindungen zu verwalten.

### Schritt 8: Eine Beispiel-URL angeben
- Optional können Sie ein Beispiel-URL-Format für die Verbindung zu einer Oracle-Datenbank angeben:
  - **Für die Verbindung über SID**: `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - **Für die Verbindung über den Servicenamen**: `jdbc:oracle:thin:@//HOST[:PORT]/DB`
- Ersetzen Sie `HOST`, `PORT` und `DB` durch tatsächliche Werte, wenn Sie später eine Verbindung einrichten (in der Alias-Konfiguration).

### Schritt 9: Die Treiberkonfiguration speichern
- Klicken Sie auf **OK**, um die Treibereinstellungen zu speichern und das Dialogfeld "Treiber hinzufügen" zu schließen. Der "Oracle Thin Driver" sollte nun im Treiber-Tab mit einem grünen Häkchen angezeigt werden, was darauf hinweist, dass er ordnungsgemäß konfiguriert ist.

### Schritt 10: Einen Alias für Ihre Datenbank erstellen
- Wechseln Sie zur Registerkarte **Aliases** auf der linken Seite von Squirrel SQL Client.
- Klicken Sie auf die **"+"** Schaltfläche, um das Dialogfeld "Alias hinzufügen" zu öffnen.

### Schritt 11: Den Alias konfigurieren
- Im Dialogfeld "Alias hinzufügen":
  - **Name**: Geben Sie einen Namen für diese Verbindung ein (z.B. "Meine Oracle DB").
  - **Treiber**: Wählen Sie **Oracle Thin Driver** aus dem Dropdown-Menü aus.
  - **URL**: Geben Sie die Verbindungs-URL für Ihre spezifische Oracle-Datenbank ein:
    - Über SID: `jdbc:oracle:thin:@HOST[:PORT]:DB`
    - Über Servicename: `jdbc:oracle:thin:@//HOST[:PORT]/DB`
    - Ersetzen Sie `HOST` (z.B. localhost oder IP-Adresse), `PORT` (Standard ist 1521) und `DB` (SID oder Servicename) durch die Details Ihrer Datenbank.
  - **Benutzername**: Geben Sie den Datenbankbenutzernamen ein.
  - **Kennwort**: Geben Sie das Datenbankkennwort ein.

### Schritt 12: Die Verbindung testen
- Klicken Sie auf die **Test** Schaltfläche im Dialogfeld "Alias hinzufügen", um zu überprüfen, ob Squirrel SQL Client eine Verbindung zu Ihrer Oracle-Datenbank mit den angegebenen Details herstellen kann. Bei Erfolg sehen Sie eine Bestätigungsmeldung.

### Schritt 13: Den Alias speichern
- Wenn der Test der Verbindung erfolgreich war, klicken Sie auf **OK**, um den Alias zu speichern. Der neue Alias wird nun im Alias-Tab angezeigt.

### Schritt 14: Mit der Datenbank verbinden
- Im Alias-Tab wählen Sie Ihren neu erstellten Alias (z.B. "Meine Oracle DB") aus.
- Klicken Sie auf die **Verbinden** Schaltfläche, um eine Verbindung zu Ihrer Oracle-Datenbank herzustellen. Sobald die Verbindung hergestellt ist, können Sie mit der Abfrage Ihrer Datenbank mit Squirrel SQL Client beginnen.

### Zusammenfassung der wichtigsten Informationen
- **Erforderliche Datei**: `ojdbc.jar`
- **Java-Treiberklasse**: `oracle.jdbc.OracleDriver`
- **URL-Formate**:
  - SID: `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - Servicename: `jdbc:oracle:thin:@//HOST[:PORT]/DB`

Durch die Befolgung dieser Schritte haben Sie den Oracle JDBC-Treiber erfolgreich zu Squirrel SQL Client hinzugefügt und eine Verbindung zu Ihrer Oracle-Datenbank konfiguriert. Stellen Sie sicher, dass alle Details (Dateipfad, URL, Anmeldeinformationen) korrekt sind, um Verbindungsprobleme zu vermeiden.