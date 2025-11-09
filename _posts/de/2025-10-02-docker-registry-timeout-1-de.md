---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: Fehlerbehebung bei Docker-Registry-Verbindungstimeouts
translated: true
type: note
---

Der Fehler, den Sie erhalten, `Error response from daemon: Get "https://registry-1.docker.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)`, weist darauf hin, dass der Docker-Client aufgrund eines Timeouts keine Verbindung zur Docker Hub Registry herstellen konnte. Dies könnte durch Netzwerkprobleme, Authentifizierungsprobleme oder Konfigurationsfehler verursacht werden. Da Sie versuchen, sich webbasiert anzumelden, gehen wir das Problem Schritt für Schritt durch.

### Schritte zur Problembehebung

1. **Netzwerkkonnektivität überprüfen**
   - Stellen Sie sicher, dass Ihre Internetverbindung stabil ist.
   - Testen Sie die Konnektivität zu Docker Hub, indem Sie ausführen:
     ```bash:disable-run
     ping registry-1.docker.io
     ```
     oder
     ```bash
     curl -v https://registry-1.docker.io/v2/
     ```
     Falls diese Befehle fehlschlagen, könnte ein Netzwerkproblem vorliegen (z.B. Firewall, Proxy oder DNS-Probleme).

2. **Webbasierte Authentifizierung überprüfen**
   - Die Meldung zeigt, dass Sie einen einmaligen Bestätigungscode (`LVFK-KCQX`) verwenden. Stellen Sie sicher, dass Sie:
     - Die `EINGABETASTE` gedrückt haben, um den Browser zu öffnen, oder manuell `https://login.docker.com/activate` besucht haben.
     - Den Code korrekt im Browser eingegeben haben.
     - Den Authentifizierungsprozess im Browser innerhalb des Timeout-Zeitraums abgeschlossen haben.
   - Falls sich der Browser nicht automatisch geöffnet hat, besuchen Sie die URL manuell und geben Sie den Code ein.
   - Falls die Authentifizierung fehlschlägt oder ein Timeout auftritt, starten Sie den Prozess neu:
     ```bash
     docker login
     ```

3. **Timeout-Probleme behandeln**
   - Der Timeout-Fehler deutet darauf hin, dass der Docker-Client keine Verbindung zur Registry herstellen konnte. Erhöhen Sie den Timeout, indem Sie die Umgebungsvariable `DOCKER_CLIENT_TIMEOUT` setzen:
     ```bash
     export DOCKER_CLIENT_TIMEOUT=120
     export COMPOSE_HTTP_TIMEOUT=120
     docker login
     ```
     Dies verlängert den Timeout auf 120 Sekunden.

4. **Auf Proxy- oder Firewall-Probleme prüfen**
   - Wenn Sie sich hinter einem Proxy befinden, konfigurieren Sie Docker für dessen Nutzung. Bearbeiten oder erstellen Sie `~/.docker/config.json` und fügen Sie hinzu:
     ```json
     {
       "proxies": {
         "default": {
           "httpProxy": "http://<proxy-host>:<proxy-port>",
           "httpsProxy": "https://<proxy-host>:<proxy-port>",
           "noProxy": "localhost,127.0.0.1"
         }
       }
     }
     ```
     Ersetzen Sie `<proxy-host>` und `<proxy-port>` mit Ihren Proxy-Details.
   - Falls eine Firewall den Zugriff blockiert, stellen Sie sicher, dass `registry-1.docker.io` und `login.docker.com` erlaubt sind.

5. **Credential Helper verwenden (Optional, aber empfohlen)**
   - Die Warnung über unverschlüsselte Anmeldedaten in `~/.docker/config.json` schlägt vor, einen Credential Helper einzurichten. Installieren Sie einen Credential Helper wie `docker-credential-pass` oder `docker-credential-secretservice`:
     - Für Linux mit `pass`:
       ```bash
       sudo apt-get install pass
       curl -fsSL https://github.com/docker/docker-credential-helpers/releases/download/v0.7.0/docker-credential-pass-v0.7.0-amd64.tar.gz | tar -xz
       sudo mv docker-credential-pass /usr/local/bin/
       ```
       Initialisieren Sie `pass`:
       ```bash
       gpg2 --gen-key
       pass init <your-gpg-key-id>
       ```
       Aktualisieren Sie `~/.docker/config.json`, um den Helper zu verwenden:
       ```json
       {
         "credsStore": "pass"
       }
       ```
     - Wiederholen Sie die Anmeldung nach der Konfiguration des Credential Helpers.

6. **Fallback auf Kommandozeilen-Anmeldung**
   - Falls die webbasierte Anmeldung weiterhin fehlschlägt, versuchen Sie die Anmeldung über die Kommandozeile mit Ihrem Docker Hub Benutzernamen und Passwort:
     ```bash
     docker login -u <your-username>
     ```
     Geben Sie Ihr Passwort oder ein Personal Access Token (PAT) ein, wenn Sie dazu aufgefordert werden. Sie können ein PAT in den Einstellungen Ihres Docker Hub Kontos generieren.

7. **Status des Docker Daemons prüfen**
   - Stellen Sie sicher, dass der Docker-Daemon läuft:
     ```bash
     sudo systemctl status docker
     ```
     Falls er nicht läuft, starten Sie ihn:
     ```bash
     sudo systemctl start docker
     ```

8. **Docker-Konfiguration löschen (Letzter Ausweg)**
   - Falls das Problem weiterhin besteht, sichern und löschen Sie die Docker-Konfigurationsdatei und versuchen Sie es erneut:
     ```bash
     mv ~/.docker/config.json ~/.docker/config.json.bak
     docker login
     ```

### Zusätzliche Hinweise
- **Docker Hub Status**: Prüfen Sie, ob Docker Hub Ausfälle hat, indem Sie `https://status.docker.com/` besuchen.
- **DNS-Probleme**: Falls `registry-1.docker.io` nicht aufgelöst wird, versuchen Sie, einen öffentlichen DNS wie Google (`8.8.8.8`) oder Cloudflare (`1.1.1.1`) in Ihren Netzwerkeinstellungen zu verwenden.
- **Docker-Version**: Stellen Sie sicher, dass Ihr Docker-Client auf dem neuesten Stand ist:
  ```bash
  docker --version
  ```
  Aktualisieren Sie Docker bei Bedarf, indem Sie den Anweisungen für Ihr Betriebssystem folgen.

### Referenzen
- [Docker Credential Store Dokumentation](https://docs.docker.com/go/credential-store/)
- [Docker Login Dokumentation](https://docs.docker.com/engine/reference/commandline/login/)
- [Docker Hub Status](https://status.docker.com/)