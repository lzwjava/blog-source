---
audio: false
generated: true
lang: de
layout: post
title: Testen des NPM-Registers
translated: true
---

Um zu testen, ob Ihr NPM-Registry funktioniert, insbesondere da es einen Benutzernamen und ein Passwort erfordert, können Sie einige einfache Schritte befolgen, um dessen Konnektivität, Authentifizierung und Fähigkeit, Pakete zu bereitstellen, zu überprüfen. Da es sich um ein privates Registry handelt (wie durch die Anmeldeinformationen impliziert), müssen Sie sicherstellen, dass die Authentifizierung korrekt eingerichtet ist, bevor Sie die Paketinstallation testen. Hier ist eine vollständige Anleitung zum Testen Ihres Registries, zusammen mit einigen empfohlenen NPM-Paketen, die Sie versuchen können zu installieren.

---

### Schritte zum Testen des Registries

1. **Authentifizierung einrichten**
   - Da das Registry einen Benutzernamen und ein Passwort erfordert, müssen Sie sich anmelden, um Ihren NPM-Client zu authentifizieren.
   - Führen Sie den folgenden Befehl in Ihrem Terminal aus, wobei Sie `<registry-url>` durch die tatsächliche URL Ihres Registries ersetzen:
     ```
     npm login --registry=<registry-url>
     ```
   - Sie werden aufgefordert, Ihren Benutzernamen und Ihr Passwort (und möglicherweise eine E-Mail, abhängig vom Registry) einzugeben. Nach Abschluss speichert dies ein Authentifizierungstoken in Ihrer `.npmrc`-Datei und ermöglicht den Zugriff auf das Registry.

2. **Verbindung zum Registry überprüfen**
   - Verwenden Sie den Befehl `npm ping`, um zu überprüfen, ob das Registry erreichbar ist:
     ```
     npm ping --registry=<registry-url>
     ```
   - Wenn dies erfolgreich ist, bestätigt dieser Befehl, dass der Registry-Server läuft und antwortet. Sie sehen normalerweise eine Ausgabe wie "Ping success: <registry-url>". Wenn es fehlschlägt, könnte es ein Verbindungsproblem geben oder die URL könnte falsch sein.

3. **Authentifizierung überprüfen**
   - Um sicherzustellen, dass Ihr Benutzername und Passwort korrekt eingerichtet sind, verwenden Sie den Befehl `npm whoami`:
     ```
     npm whoami --registry=<registry-url>
     ```
   - Dies sollte Ihren Benutzernamen zurückgeben, wenn die Authentifizierung erfolgreich ist. Wenn es fehlschlägt oder einen Fehler zurückgibt (z. B. "nicht authentifiziert"), überprüfen Sie Ihre Anmeldeinformationen oder den Anmeldeschritt erneut.

4. **Paketinstallation testen**
   - Versuchen Sie, ein Paket zu installieren, um zu bestätigen, dass das Registry Pakete bereitstellen kann. Da es sich um ein privates Registry handelt, müssen Sie ein Paket installieren, von dem Sie wissen, dass es darauf vorhanden ist. Wenn das Registry jedoch das öffentliche NPM-Registry proxyt (eine gängige Einrichtung für private Registries wie Verdaccio), können Sie mit beliebten öffentlichen Paketen testen.
   - Beispielbefehl:
     ```
     npm install <package-name> --registry=<registry-url>
     ```
   - Ersetzen Sie `<package-name>` durch ein Paket, das in Ihrem Registry verfügbar ist (mehr zu Paketempfehlungen unten).

---

### Einige NPM-Pakete zum Ausprobieren

Da dies ein privates Registry ist, kann ich nicht genau wissen, welche Pakete verfügbar sind. Hier sind jedoch einige Vorschläge basierend auf gängigen Szenarien:

- **Wenn das Registry das öffentliche NPM-Registry proxyt:**
  - Viele private Registries sind so konfiguriert, dass sie das öffentliche Registry spiegeln, was den Zugriff auf öffentliche Pakete nach der Authentifizierung ermöglicht. In diesem Fall können Sie versuchen, bekannte öffentliche Pakete zu installieren:
    - `lodash`: Eine beliebte Utility-Bibliothek.
      ```
      npm install lodash --registry=<registry-url>
      ```
    - `express`: Ein weit verbreiteter Web-Framework für Node.js.
      ```
      npm install express --registry=<registry-url>
      ```
    - `react`: Eine beliebte Bibliothek zum Erstellen von Benutzeroberflächen.
      ```
      npm install react --registry=<registry-url>
      ```
  - Wenn diese erfolgreich installiert werden, bestätigt dies, dass das Registry funktioniert und Pakete bereitstellen kann.

- **Wenn das Registry nur private Pakete hostet:**
  - Sie müssen ein Paket installieren, von dem Sie wissen, dass es in Ihrem privaten Registry vorhanden ist. Überprüfen Sie dies bei Ihrem Team oder der Dokumentation/Web-Oberfläche des Registries (falls verfügbar) auf einen Paketnamen. Zum Beispiel:
    - Wenn es ein Paket namens `my-org-utils` gibt, versuchen Sie:
      ```
      npm install my-org-utils --registry=<registry-url>
      ```
  - Ohne spezifische Paketnamen kann ich keine genauen privaten Pakete auflisten, daher verwenden Sie eines, das für Ihre Organisation relevant ist.

---

### Hinweise und Fehlerbehebung

- **Erfolgsindikatoren**: Wenn `npm ping` funktioniert, `npm whoami` Ihren Benutzernamen zurückgibt und ein Paket ohne Fehler installiert wird, funktioniert Ihr Registry korrekt.
- **Gängige Probleme**:
  - **Authentifizierungsfehler**: Führen Sie `npm login` erneut aus, wenn `npm whoami` fehlschlägt.
  - **Paket nicht gefunden**: Stellen Sie sicher, dass das Paket im Registry vorhanden ist. Wenn Sie ein öffentliches Paket verwenden und es fehlschlägt, proxyt Ihr Registry möglicherweise nicht das öffentliche Registry.
  - **Verbindungsprobleme**: Überprüfen Sie die `<registry-url>` und Ihre Netzwerkeinstellungen erneut, wenn `npm ping` fehlschlägt.
- **Globale Änderungen vermeiden**: Um Ihre globale NPM-Konfiguration nicht zu beeinflussen, können Sie in einem neuen Verzeichnis mit einer lokalen `.npmrc`-Datei testen, aber die oben genannten Befehle mit der `--registry`-Flagge sind für das Testen ausreichend.

Durch das Befolgen dieser Schritte und das Ausprobieren der empfohlenen Pakete können Sie bestätigen, dass Ihr Registry betriebsbereit ist und Authentifizierung und Paketabruf korrekt handelt. Wenn Sie spezifische Paketnamen aus Ihrem Registry haben, verwenden Sie diese anstelle der hier bereitgestellten öffentlichen Beispiele.