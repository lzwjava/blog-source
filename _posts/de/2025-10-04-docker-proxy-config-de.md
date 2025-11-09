---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Konfiguration der Docker-Daemon-Proxy-Einstellungen
translated: true
type: note
---

### Konfigurieren des Docker Daemons für Proxy-Einstellungen

Der Docker-Daemon kann so konfiguriert werden, dass er einen HTTP/HTTPS-Proxy für Operationen wie das Pullen von Images oder das Erstellen von Containers hinter einer Corporate Firewall verwendet. Dies geschieht durch das Bearbeiten (oder Erstellen) der Datei `/etc/docker/daemon.json`. Beachten Sie, dass diese Konfiguration für den Daemon selbst gilt (z.B. für `docker pull` oder `docker build`), nicht für einzelne Container (die Umgebungsvariablen oder Docker-Build-Args verwenden würden).

#### Voraussetzungen
- Sie benötigen Root- oder sudo-Zugriff auf einem Linux-System (dies ist das primäre Betriebssystem für die Docker-Daemon-Konfiguration; unter Windows/Mac mit Docker Desktop verwenden Sie stattdessen die GUI-Einstellungen).
- Docker ist installiert und läuft.
- Sie kennen die Details Ihres Proxy-Servers (z.B. `http://proxy.company.com:8080` für HTTP/HTTPS-Proxy und alle No-Proxy-Ausnahmen).

#### Schritt-für-Schritt-Konfiguration

1.  **Konfigurationsdatei für den Daemon finden oder erstellen**:
    - Öffnen Sie ein Terminal und navigieren Sie zu `/etc/docker/` (erstellen Sie das Verzeichnis, falls es nicht existiert: `sudo mkdir -p /etc/docker`).
    - Bearbeiten Sie die Datei `daemon.json` mit einem Texteditor (z.B. `sudo nano /etc/docker/daemon.json` oder `sudo vim /etc/docker/daemon.json`).
    - Wenn die Datei nicht existiert, erstellen Sie sie. Beginnen Sie mit einem leeren JSON-Objekt `{}`, wenn sie neu ist.

2.  **Proxy-Konfiguration hinzufügen**:
    - Fügen Sie einen Abschnitt `"proxies"` zur JSON-Datei hinzu. Hier ist ein grundlegendes Beispiel:

      ```json
      {
        "proxies": {
          "http-proxy": "http://proxy.company.com:8080",
          "https-proxy": "http://proxy.company.com:8080",
          "no-proxy": "localhost,127.0.0.1,*.company.com,10.0.0.0/8"
        }
      }
      ```

      - **Erklärungen**:
        - `"http-proxy"`: Die URL für den HTTP-Proxy (erforderlich für nicht-HTTPS-Anfragen).
        - `"https-proxy"`: Die URL für den HTTPS-Proxy (oft die gleiche wie der HTTP-Proxy).
        - `"no-proxy"`: Eine kommagetrennte Liste von Hosts/Domains/IP-Bereichen, die den Proxy umgehen sollten (z.B. lokale Adressen oder interne Domains). Dies verhindert Endlosschleifen.
        - Wenn Authentifizierung benötigt wird, verwenden Sie das Format `http://username:password@proxy.company.com:8080`.
        - Für SOCKS-Proxys verwenden Sie `"http-proxy": "socks5://proxy.company.com:1080"`.

      - Wenn `daemon.json` bereits vorhandene Inhalte hat (z.B. andere Einstellungen wie `"log-driver": "json-file"`), fügen Sie den Abschnitt `"proxies"` darin ein, ohne Schlüssel zu duplizieren. Stellen Sie eine gültige JSON-Syntax sicher (verwenden Sie bei Bedarf ein Tool wie `jsonlint` zur Validierung).

3.  **Speichern und Docker-Daemon neu starten**:
    - Speichern Sie die Datei.
    - Starten Sie den Docker-Dienst neu, um die Änderungen zu übernehmen:
      ```
      sudo systemctl restart docker
      ```
      - Auf älteren Systemen oder ohne systemd verwenden Sie `sudo service docker restart`.
    - Überprüfen Sie, ob der Daemon läuft:
      ```
      sudo systemctl status docker
      ```
      - Prüfen Sie die Logs bei Problemen: `sudo journalctl -u docker.service`.

4.  **Konfiguration überprüfen**:
    - Testen Sie, indem Sie ein Image pullen (was nun über Ihren Proxy geroutet werden sollte):
      ```
      docker pull hello-world
      ```
    - Überprüfen Sie, ob die Proxy-Einstellungen angewendet wurden, indem Sie die Daemon-Konfiguration inspizieren:
      ```
      docker info | grep -i proxy
      ```
      - Sie sollten eine Ausgabe wie die folgende sehen:
        ```
        HTTP Proxy: http://proxy.company.com:8080
        HTTPS Proxy: http://proxy.company.com:8080
        No Proxy: localhost,127.0.0.1,*.company.com,10.0.0.0/8
        ```
    - Wenn Sie Docker in einem Build-Kontext verwenden, testen Sie mit:
      ```
      docker build -t test-proxy .
      ```
      (Vorausgesetzt, es handelt sich um ein einfaches Dockerfile, das ein Basis-Image pulled.)

#### Zusätzliche Hinweise
- **Sicherheit**: Vermeiden Sie das Hartkodieren von Anmeldedaten in `daemon.json` auf gemeinsam genutzten Systemen. Verwenden Sie nach Möglichkeit Umgebungsvariablen oder Tools wie `docker config` für erweiterte Setups.
- **Häufige Probleme**:
  - **Syntaxfehler**: Ungültiges JSON verhindert das Starten des Daemons. Überprüfen Sie die Syntax mit `cat /etc/docker/daemon.json` und einem JSON-Validator.
  - **Firewall/SELinux**: Stellen Sie sicher, dass Ihr Proxy erreichbar ist und keine Sicherheitsmodule ihn blockieren.
  - **Docker-Version**: Dies funktioniert mit Docker 20.10+ (ältere Versionen verwendeten andere Umgebungsvariablen wie `HTTP_PROXY`). Überprüfen Sie Ihre Version mit `docker --version` und führen Sie bei Bedarf ein Upgrade durch.
  - **Registry-spezifische Proxys**: Für private Registries benötigen Sie möglicherweise eine zusätzliche Konfiguration unter `"registry-mirrors"` oder unsichere Registries in `daemon.json`.
- **Für Container**: Wenn Sie Proxy-Einstellungen *innerhalb* laufender Container (nicht des Daemons) benötigen, setzen Sie Umgebungsvariablen im Dockerfile (z.B. `ENV http_proxy=http://proxy.company.com:8080`) oder über `docker run -e http_proxy=...`.
- **Docker Desktop (Windows/Mac)**: Gehen Sie zu Einstellungen > Ressourcen > Proxys und aktivieren/konfigurieren Sie diese dort – keine JSON-Bearbeitung erforderlich.

Weitere Details finden Sie in der offiziellen Docker-Dokumentation: [Configure the Docker daemon](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file). Wenn Sie Fehler encounter, teilen Sie die genaue Ausgabe zur Fehlerbehebung!