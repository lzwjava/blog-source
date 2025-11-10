---
audio: false
generated: true
image: false
lang: de
layout: post
title: Sicheres Upgrade von Open WebUI jetzt
translated: true
type: note
---

Verstanden. Hier sind die sicheren, unkomplizierten Methoden, um Open WebUI zu aktualisieren.

## Falls Sie mit `pip` installiert haben (Ihr Fall)

```bash
# 1) (Empfohlen) Aktivieren Sie die Umgebung, die Sie für Open WebUI verwenden
#    z.B. conda:
conda activate open-webui
#    oder venv:
# source ~/open-webui-venv/bin/activate

# 2) Auf die neueste Version aktualisieren
python3.11 -m pip install -U open-webui

# 3) (Optional) Falls der pip-Cache Probleme verursacht
python3.11 -m pip cache purge
python3.11 -m pip install --no-cache-dir -U open-webui

# 4) Überprüfen Sie, was installiert wurde
python3.11 -m pip show open-webui
```

Laut offizieller Dokumentation reicht `pip install -U open-webui` aus, um auf die neueste Version zu aktualisieren. ([Open WebUI][1])

### Halten Sie Ihre Daten/Einstellungen persistent

Wenn Sie den Server starten, können Sie ein Datenverzeichnis festpinnen, damit Aktualisierungen es nicht betreffen:

```bash
# macOS/Linux
DATA_DIR="$HOME/.open-webui" open-webui serve
# Windows (PowerShell)
$env:DATA_DIR="C:\open-webui\data"; open-webui serve
```

Dies spiegelt die Empfehlung der Dokumentation wider, `DATA_DIR` zu setzen (oder `uvx … @latest serve` mit derselben Variable zu verwenden), damit Ihre Chats/Konfiguration außerhalb der Paketinstallation liegen. ([Open WebUI][2])

> Tipp: Wenn Sie zuvor ohne `DATA_DIR` gearbeitet haben, verwenden Sie es jetzt; Open WebUI verwendet diesen Ordner fortan.

## Falls Sie Docker verwendet haben (der Vollständigkeit halber)

```bash
# Alten Container stoppen & entfernen (Daten befinden sich im benannten Volume)
docker rm -f open-webui

# Neuestes Image herunterladen
docker pull ghcr.io/open-webui/open-webui:main

# Container mit vorhandenem Volume neu starten
docker run -d -p 3000:8080 \
  -v open-webui:/app/backend/data \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main
```

Dies ist der vom Projekt empfohlene manuelle Update-Vorgang; Ihre Daten bleiben im `open-webui` Docker-Volume erhalten. ([Open WebUI][3])

## Überprüfen Sie, was "latest" ist

Sie können das neueste Release auf GitHub Releases vor/nach der Aktualisierung bestätigen. ([GitHub][4])

Falls Fehler auftreten (z.B. Python-Version-Konflikt), stellen Sie sicher, dass Sie für die pip-Methode Python 3.11 verwenden, was das Projekt ausdrücklich empfiehlt. ([GitHub][5])

Soll ich Ihre aktuelle Umgebung überprüfen oder Upgrade-Fehlerausgaben interpretieren? Fügen Sie sie hier ein und ich werde die Fehlerbehebung durchführen.

[1]: https://docs.openwebui.com/getting-started/quick-start/?utm_source=chatgpt.com "️ Quick Start"
[2]: https://docs.openwebui.com/?utm_source=chatgpt.com "Open WebUI: Home"
[3]: https://docs.openwebui.com/getting-started/updating/?utm_source=chatgpt.com "Updating Open WebUI"
[4]: https://github.com/open-webui/open-webui/releases?utm_source=chatgpt.com "Releases · open-webui/open-webui"
[5]: https://github.com/open-webui/open-webui?utm_source=chatgpt.com "open-webui/open-webui: User-friendly AI Interface ..."