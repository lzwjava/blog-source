---
audio: false
generated: true
lang: de
layout: post
title: Validierung von SSL-Zertifikaten in Insomnia
translated: true
type: note
---

Um den Fehler "SSL peer certificate or SSH remote key was not OK" in Insomnia zu beheben, tritt dieser Fehler typischerweise auf, wenn Insomnia das SSL-Zertifikat des Servers, mit dem Sie eine Verbindung herstellen möchten, nicht überprüfen kann. Nachfolgend finden Sie Schritt-für-Schritt-Lösungen zur Behebung des Problems:

### 1. **Deaktivieren der SSL-Zertifikatsvalidierung (Nur für lokale Entwicklung)**
Wenn Sie mit einem lokalen Entwicklungsserver arbeiten, der ein selbstsigniertes oder ungültiges SSL-Zertifikat verwendet, können Sie die Zertifikatsvalidierung in Insomnia deaktivieren:
- Öffnen Sie Insomnia und gehen Sie zu **Application** > **Preferences**.
- Navigieren Sie zum Abschnitt **Request / Response**.
- Deaktivieren Sie das Kontrollkästchen **Validate certificates**.
- Wiederholen Sie Ihre Anfrage.

**Wichtig**: Diese Option umgeht Sicherheitsprüfungen und sollte **ausschließlich für Tests oder die lokale Entwicklung verwendet werden**. Verwenden Sie sie nicht für Produktionsumgebungen, da sie Ihre Verbindung anfällig macht.

---

### 2. **Überprüfen Sie das SSL-Zertifikat des Servers**
Der Fehler könnte auf ein Problem mit dem SSL-Zertifikat des Servers hinweisen (z. B. abgelaufen, selbstsigniert oder Hostname-Fehlanpassung). So überprüfen Sie es:
- Öffnen Sie die URL des Servers in einem Webbrowser.
- Klicken Sie auf das Schloss-Symbol in der Adressleiste, um die Zertifikatdetails anzuzeigen.
- Stellen Sie sicher, dass das Zertifikat gültig ist, nicht abgelaufen ist und mit dem Domainnamen übereinstimmt.
- Wenn das Zertifikat ungültig oder fehlerhaft konfiguriert ist, wenden Sie sich an den Server-Administrator, um es zu reparieren.

---

### 3. **Importieren Sie ein Client-Zertifikat (falls erforderlich)**
Wenn der Server ein Client-Zertifikat zur Authentifizierung benötigt, müssen Sie dies in Insomnia konfigurieren:
- Gehen Sie in Insomnia zu **Client Certificates** (zugänglich vom Haupt-Dashboard oder den Einstellungen).
- Klicken Sie auf **Add Certificate**.
- Importieren Sie Ihre Zertifikatsdatei (unterstützte Formate sind PFX oder PEM).
- Weisen Sie es der spezifischen Domain oder dem Hostnamen zu, mit dem Sie sich verbinden.
- Testen Sie die Anfrage erneut.

---

### 4. **Aktualisieren Sie Insomnia**
SSL-bezogene Probleme könnten auf einen Fehler in einer älteren Version von Insomnia zurückzuführen sein. Um sicherzustellen, dass Sie die neueste Version verwenden:
- Prüfen Sie auf Updates unter **Application** > **About** oder laden Sie die neueste Version von der offiziellen Insomnia-Website herunter.
- Installieren Sie das Update und wiederholen Sie Ihre Anfrage.

---

### 5. **Testen mit Curl**
Wenn die oben genannten Schritte das Problem nicht beheben, testen Sie die Anfrage außerhalb von Insomnia, um das Problem zu isolieren:
- Öffnen Sie ein Terminal und verwenden Sie den `curl`-Befehl mit der gleichen URL und den gleichen Parametern (z. B. `curl -v https://example.com`).
- Wenn `curl` ebenfalls fehlschlägt, liegt das Problem wahrscheinlich an der Konfiguration des Servers und nicht an Insomnia.
- Wenn `curl` erfolgreich ist, könnte dies auf ein spezifisches Problem mit Insomnia hinweisen, das Sie an das Support-Team melden können.

---

### Zusammenfassung
Beginnen Sie damit, die SSL-Validierung zu deaktivieren, wenn es sich um einen lokalen Server handelt. Überprüfen Sie dann das Server-Zertifikat oder konfigurieren Sie ein Client-Zertifikat, falls erforderlich. Stellen Sie sicher, dass Insomnia auf dem neuesten Stand ist, und verwenden Sie `curl` zur weiteren Fehlerbehebung, falls nötig. Diese Schritte sollten die meisten Fälle des Fehlers "SSL peer certificate or SSH remote key was not OK" beheben.

Wenn das Problem weiterhin besteht, könnte es an einer serverseitigen Fehlkonfiguration oder einem seltenen Fehler in Insomnia liegen. Lassen Sie mich wissen, wenn Sie weitere Hilfe benötigen!