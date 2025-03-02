---
audio: false
generated: false
lang: de
layout: post
title: SSL-Zertifikatsvalidierung in Insomnia
translated: true
---

Um den Fehler "SSL peer certificate or SSH remote key was not OK" in Insomnia zu beheben, tritt dieser Fehler normalerweise auf, wenn Insomnia das SSL-Zertifikat des Servers, zu dem Sie eine Verbindung herstellen möchten, nicht überprüfen kann. Hier sind Schritt-für-Schritt-Lösungen, um dieses Problem zu beheben:

### 1. **SSL-Zertifikatsvalidierung deaktivieren (Nur für lokale Entwicklung)**
Wenn Sie mit einem lokalen Entwicklungsserver arbeiten, der ein selbstsigniertes oder ungültiges SSL-Zertifikat verwendet, können Sie die Zertifikatsvalidierung in Insomnia deaktivieren:
- Öffnen Sie Insomnia und gehen Sie zu **Anwendung** > **Einstellungen**.
- Navigieren Sie zum Abschnitt **Anfrage / Antwort**.
- Deaktivieren Sie das Kontrollkästchen mit der Bezeichnung **Zertifikate validieren**.
- Versuchen Sie es erneut mit Ihrer Anfrage.

**Wichtig**: Diese Option umgeht Sicherheitsprüfungen und sollte **nur für Tests oder lokale Entwicklung** verwendet werden. Verwenden Sie diese Option nicht in Produktionsumgebungen, da sie Ihre Verbindung verwundbar macht.

---

### 2. **SSL-Zertifikat des Servers überprüfen**
Der Fehler könnte auf ein Problem mit dem SSL-Zertifikat des Servers hinweisen (z.B. abgelaufen, selbstsigniert oder Hostnamen-Fehler). Um dies zu überprüfen:
- Öffnen Sie die URL des Servers in einem Webbrowser.
- Klicken Sie auf das Schloss-Symbol in der Adressleiste, um die Zertifikatdetails anzuzeigen.
- Stellen Sie sicher, dass das Zertifikat gültig ist, nicht abgelaufen ist und mit dem Domainnamen übereinstimmt.
- Wenn das Zertifikat ungültig oder falsch konfiguriert ist, kontaktieren Sie den Serveradministrator, um es zu beheben.

---

### 3. **Client-Zertifikat importieren (falls erforderlich)**
Wenn der Server ein Client-Zertifikat für die Authentifizierung benötigt, müssen Sie es in Insomnia konfigurieren:
- Gehen Sie in Insomnia zu **Client-Zertifikate** (über das Hauptdashboard oder die Einstellungen zugänglich).
- Klicken Sie auf **Zertifikat hinzufügen**.
- Importieren Sie Ihre Zertifikatsdatei (unterstützte Formate sind PFX oder PEM).
- Weisen Sie es der spezifischen Domain oder dem Hostnamen zu, mit dem Sie eine Verbindung herstellen.
- Testen Sie die Anfrage erneut.

---

### 4. **Insomnia aktualisieren**
SSL-bezogene Probleme könnten auf einen Fehler in einer älteren Version von Insomnia zurückzuführen sein. Stellen Sie sicher, dass Sie die neueste Version verwenden:
- Überprüfen Sie auf Updates unter **Anwendung** > **Über** oder laden Sie die neueste Version von der offiziellen Insomnia-Website herunter.
- Installieren Sie das Update und versuchen Sie es erneut mit Ihrer Anfrage.

---

### 5. **Mit Curl testen**
Wenn die obigen Schritte das Problem nicht beheben, testen Sie die Anfrage außerhalb von Insomnia, um das Problem zu isolieren:
- Öffnen Sie ein Terminal und verwenden Sie den `curl`-Befehl mit derselben URL und denselben Parametern (z.B. `curl -v https://example.com`).
- Wenn `curl` ebenfalls fehlschlägt, liegt das Problem wahrscheinlich in der Serverkonfiguration und nicht in Insomnia.
- Wenn `curl` erfolgreich ist, könnte dies auf ein spezifisches Problem mit Insomnia hinweisen, und Sie können es dem Support-Team melden.

---

### Zusammenfassung
Beginnen Sie damit, die SSL-Validierung zu deaktivieren, wenn es sich um einen lokalen Server handelt, überprüfen Sie dann das Zertifikat des Servers oder konfigurieren Sie ein Client-Zertifikat, falls erforderlich. Stellen Sie sicher, dass Insomnia auf dem neuesten Stand ist, und verwenden Sie `curl` zur weiteren Fehlerbehebung, falls notwendig. Diese Schritte sollten die meisten Fälle des Fehlers "SSL peer certificate or SSH remote key was not OK" beheben.

Wenn das Problem weiterhin besteht, könnte es sich um eine serverseitige Fehlkonfiguration oder einen seltenen Fehler in Insomnia handeln. Lassen Sie mich wissen, wenn Sie weitere Hilfe benötigen!