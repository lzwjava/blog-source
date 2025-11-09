---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Beheben von Docker GHCR TLS-Zeitüberschreitungsfehlern
translated: true
type: note
---

Der Fehler `Get "https://ghcr.io/v2/": net/http: TLS handshake timeout`, den du erhältst, deutet typischerweise auf ein Netzwerkproblem hin, wenn Docker versucht, Images aus der GitHub Container Registry (GHCR) zu pullen. Hier sind einige Schritte zur Fehlerbehebung:

---

### 1. **Überprüfe deine Internetverbindung**
- Stelle sicher, dass dein Rechner eine stabile Internetverbindung hat.
- Versuche, `https://ghcr.io` in deinem Browser aufzurufen, um zu bestätigen, dass du die Seite erreichen kannst.

---

### 2. **Überprüfe den Status des Docker Daemons**
- Starte den Docker-Daemon neu:
  ```bash
  sudo systemctl restart docker
  ```
- Überprüfe, ob Docker läuft:
  ```bash
  sudo systemctl status docker
  ```

---

### 3. **Konfiguriere die Docker-DNS-Einstellungen**
- Wenn du dich in einem Unternehmensnetzwerk oder hinter einem Proxy befindest, benötigt Docker möglicherweise benutzerdefinierte DNS-Einstellungen.
- Bearbeite oder erstelle die Datei `/etc/docker/daemon.json`:
  ```json
  {
    "dns": ["8.8.8.8", "1.1.1.1"]
  }
  ```
- Starte Docker neu:
  ```bash
  sudo systemctl restart docker
  ```

---

### 4. **Überprüfe die Proxy-Einstellungen**
- Wenn du einen Proxy verwendet, konfiguriere Docker für dessen Nutzung:
  ```bash
  mkdir -p ~/.docker
  echo '{
    "proxies": {
      "default": {
        "httpProxy": "http://your-proxy-address:port",
        "httpsProxy": "http://your-proxy-address:port",
        "noProxy": "localhost,127.0.0.1"
      }
    }
  }' > ~/.docker/config.json
  ```
- Ersetze `your-proxy-address:port` mit deinen tatsächlichen Proxy-Details.

---

### 5. **Versuche, das Image manuell zu pullen**
- Versuche, das Image manuell zu pullen, um zu sehen, ob das Problem weiterhin besteht:
  ```bash
  docker pull ghcr.io/librechat/librechat:latest
  ```
- Wenn es funktioniert, versuche es erneut mit `docker-compose up -d`.

---

### 6. **Überprüfe die Firewall-/Netzwerkbeschränkungen**
- Stelle sicher, dass deine Firewall oder dein Netzwerk den Zugriff auf `ghcr.io` nicht blockiert.
- Deaktiviere die Firewall vorübergehend zum Testen:
  ```bash
  sudo ufw disable
  ```
  (Aktiviere sie nach dem Testen wieder, falls nötig.)

---

### 7. **Aktualisiere Docker und Docker-Compose**
- Stelle sicher, dass du die neuesten Versionen verwendest:
  ```bash
  sudo apt update && sudo apt upgrade docker-ce docker-compose-plugin
  ```

---

### 8. **Setze die UID/GID-Umgebungsvariablen**
- Die Warnungen bezüglich `UID` und `GID` sind nicht kritisch, aber du kannst sie in deiner `.env`-Datei oder `docker-compose.yml` setzen, um die Warnungen zu unterdrücken:
  ```bash
  echo "UID=$(id -u)" >> .env
  echo "GID=$(id -g)" >> .env
  ```

---

### 9. **Verwende eine andere Registry Mirror (Optional)**
- Wenn GHCR konsistent nicht erreichbar ist, kannst du versuchen, einen Mirror zu verwenden (wird für Produktionsumgebungen jedoch nicht empfohlen):
  ```json
  {
    "registry-mirrors": ["https://mirror.example.com"]
  }
  ```
- Füge dies zur `/etc/docker/daemon.json` hinzu und starte Docker neu.

---

### 10. **Überprüfe die Zeitsynchronisierung**
- Stelle sicher, dass deine Systemzeit synchronisiert ist:
  ```bash
  sudo apt install ntp
  sudo systemctl restart ntp
  ```

---

### Befehlsübersicht



| Schritt | Befehl/Aktion |
|------|----------------|
| Docker neustarten | `sudo systemctl restart docker` |
| Docker Status prüfen | `sudo systemctl status docker` |
| DNS konfigurieren | `/etc/docker/daemon.json` bearbeiten |
| Image manuell pullen | `docker pull ghcr.io/librechat/librechat:latest` |
| UID/GID setzen | `echo "UID=$(id -u)" >> .env` |

---

Wenn das Problem nach dem Ausprobieren dieser Schritte weiterhin besteht, teile mir bitte die Ausgabe von:
```bash
docker info
```
und alle Fehlermeldungen mit, die du beim Ausführen der oben genannten Befehle siehst. Das wird bei der weiteren Diagnose helfen!