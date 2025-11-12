---
audio: false
generated: true
lang: de
layout: post
title: Hinzufügen des Oracle JDBC-Treibers zum Squirrel SQL Client
translated: true
type: note
---

Um den Oracle JDBC-Treiber zum Squirrel SQL Client hinzuzufügen, befolgen Sie diese detaillierten Schritte. Dieser Prozess umfasst die Konfiguration des Treibers und das Einrichten eines Verbindungsalias für Ihre Oracle-Datenbank.

### Schritt 1: Benötigte Datei finden
Sie benötigen die Oracle JDBC-Treiberdatei, speziell `ojdbc.jar`. Diese Datei enthält die notwendigen Klassen, damit Squirrel SQL Client eine Verbindung zu einer Oracle-Datenbank herstellen kann. Stellen Sie sicher, dass Sie diese Datei heruntergeladen haben (z.B. von der Oracle-Website oder von Ihrem Datenbankadministrator) und ihren Speicherort auf Ihrem System kennen.

### Schritt 2: Squirrel SQL Client starten
Öffnen Sie die Squirrel SQL Client Anwendung auf Ihrem Computer.

### Schritt 3: Auf den Treiber-Tab zugreifen
Suchen Sie auf der linken Seite der Squirrel SQL Client Oberfläche nach dem Tab **Drivers** und klicken Sie darauf. In diesem Abschnitt können Sie die für die Anwendung verfügbaren JDBC-Treiber verwalten.

### Schritt 4: Neuen Treiber hinzufügen
- Klicken Sie im Drivers-Tab auf die **"+"** Schaltfläche, um den Dialog "Add Driver" zu öffnen.

### Schritt 5: Treiber benennen
- Geben Sie im Feld "Name" des "Add Driver" Dialogs **Oracle Thin Driver** ein. Dies ist ein beschreibender Name, um den Oracle-Treiber innerhalb von Squirrel SQL Client zu identifizieren.

### Schritt 6: Die `ojdbc.jar` Datei hinzufügen
- Wechseln Sie innerhalb des "Add Driver" Dialogs zum Tab **Extra Class Path**.
- Klicken Sie auf die Schaltfläche **Add**.
- Navigieren Sie zum Speicherort der `ojdbc.jar` Datei auf Ihrem System, wählen Sie sie aus und bestätigen Sie, um sie zum Classpath des Treibers hinzuzufügen.

### Schritt 7: Java-Treiberklasse angeben
- Geben Sie im Feld "Class Name" die Java-Treiberklasse ein: **oracle.jdbc.OracleDriver**. Dies teilt Squirrel SQL Client mit, welche Klasse aus der `ojdbc.jar` Datei verwendet werden soll, um Oracle-Datenbankverbindungen zu handhaben.

### Schritt 8: Beispiel-URL angeben
- Optional können Sie ein Beispiel-URL-Format für die Verbindung zu einer Oracle-Datenbank angeben:
  - **Für die Verbindung über SID**: `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - **Für die Verbindung über Service Name**: `jdbc:oracle:thin:@//HOST[:PORT]/DB`
- Ersetzen Sie `HOST`, `PORT` und `DB` später bei der Einrichtung einer Verbindung (in der Alias-Konfiguration) durch tatsächliche Werte.

### Schritt 9: Treiberkonfiguration speichern
- Klicken Sie auf **OK**, um die Treibereinstellungen zu speichern und den "Add Driver" Dialog zu schließen. Der "Oracle Thin Driver" sollte nun im Drivers-Tab mit einem grünen Häkchen erscheinen, was anzeigt, dass er korrekt konfiguriert ist.

### Schritt 10: Alias für Ihre Datenbank erstellen
- Wechseln Sie zum Tab **Aliases** auf der linken Seite von Squirrel SQL Client.
- Klicken Sie auf die **"+"** Schaltfläche, um den Dialog "Add Alias" zu öffnen.

### Schritt 11: Alias konfigurieren
- Im Dialog "Add Alias":
  - **Name**: Geben Sie einen Namen für diese Verbindung ein (z.B. "My Oracle DB").
  - **Driver**: Wählen Sie **Oracle Thin Driver** aus dem Dropdown-Menü.
  - **URL**: Geben Sie die Verbindungs-URL für Ihre spezifische Oracle-Datenbank ein:
    - Über SID: `jdbc:oracle:thin:@HOST[:PORT]:DB`
    - Über Service Name: `jdbc:oracle:thin:@//HOST[:PORT]/DB`
    - Ersetzen Sie `HOST` (z.B. localhost oder IP-Adresse), `PORT` (Standard ist 1521) und `DB` (SID oder Service Name) mit den Details Ihrer Datenbank.
  - **Username**: Geben Sie den Datenbank-Benutzernamen ein.
  - **Password**: Geben Sie das Datenbank-Passwort ein.

### Schritt 12: Verbindung testen
- Klicken Sie im "Add Alias" Dialog auf die Schaltfläche **Test**, um zu überprüfen, ob Squirrel SQL Client mit den angegebenen Details eine Verbindung zu Ihrer Oracle-Datenbank herstellen kann. Bei Erfolg erscheint eine Bestätigungsmeldung.

### Schritt 13: Alias speichern
- Wenn der Verbindungstest erfolgreich war, klicken Sie auf **OK**, um den Alias zu speichern. Der neue Alias erscheint nun im Aliases-Tab.

### Schritt 14: Mit der Datenbank verbinden
- Wählen Sie im Aliases-Tab Ihren neu erstellten Alias aus (z.B. "My Oracle DB").
- Klicken Sie auf die Schaltfläche **Connect**, um eine Verbindung zu Ihrer Oracle-Datenbank herzustellen. Sobald die Verbindung besteht, können Sie mit Squirrel SQL Client beginnen, Abfragen an Ihre Datenbank zu senden.

### Zusammenfassung der wichtigsten Informationen
- **Benötigte Datei**: `ojdbc.jar`
- **Java-Treiberklasse**: `oracle.jdbc.OracleDriver`
- **URL-Formate**:
  - SID: `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - Service Name: `jdbc:oracle:thin:@//HOST[:PORT]/DB`

Indem Sie diese Schritte befolgen, haben Sie den Oracle JDBC-Treiber erfolgreich zum Squirrel SQL Client hinzugefügt und eine Verbindung zu Ihrer Oracle-Datenbank konfiguriert. Stellen Sie sicher, dass alle Details (Dateipfad, URL, Anmeldeinformationen) korrekt sind, um Verbindungsprobleme zu vermeiden.