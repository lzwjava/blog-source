---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Konfiguration von Python Requests Proxy über .env
translated: true
type: note
---

### Verwendung einer `.env`-Datei zum Setzen von HTTP/HTTPS-Proxys für Python Requests

Die `requests`-Bibliothek in Python berücksichtigt automatisch Standard-Umgebungsvariablen wie `HTTP_PROXY` und `HTTPS_PROXY` für die Proxy-Konfiguration. Um diese sicher zu verwalten (z.B. ohne sie im Code festzuschreiben), können Sie sie in einer `.env`-Datei speichern und mit der `python-dotenv`-Bibliothek laden. Dies hält sensible Proxy-Daten aus Ihrem Code heraus.

#### Schritt 1: Erforderliche Pakete installieren
Sie benötigen `requests` (falls noch nicht installiert) und `python-dotenv` zum Laden der `.env`-Datei.

```bash
pip install requests python-dotenv
```

#### Schritt 2: Eine `.env`-Datei erstellen
Erstellen Sie im Stammverzeichnis Ihres Projekts eine Datei namens `.env` (ohne Erweiterung) und fügen Sie Ihre Proxy-Einstellungen hinzu. Verwenden Sie das Format `http://` oder `https://` für die Proxy-URL, inklusive Benutzername/Passwort falls erforderlich.

Beispiel `.env`-Inhalt:
```
HTTP_PROXY=http://benutzername:passwort@proxy-host:port
HTTPS_PROXY=https://benutzername:passwort@proxy-host:port
NO_PROXY=localhost,127.0.0.1,example.com  # Optional: Domains vom Proxy ausschließen
```

- `HTTP_PROXY`: Für HTTP-Datenverkehr.
- `HTTPS_PROXY`: Für HTTPS-Datenverkehr (oft identisch mit HTTP_PROXY).
- `NO_PROXY`: Durch Kommas getrennte Liste von Hosts/IPs, die den Proxy umgehen sollen.
- Hinweis: Umgebungsvariablen sind case-insensitiv, aber Großschreibung ist konventionell.

Fügen Sie `.env` zu Ihrer `.gitignore` hinzu, um das Committen sensibler Informationen zu vermeiden.

#### Schritt 3: Die `.env`-Datei in Ihrem Python-Skript laden
Laden Sie die Umgebungsvariablen am Anfang Ihres Skripts:

```python
from dotenv import load_dotenv
import requests

# Lade Variablen aus der .env-Datei
load_dotenv()  # Sucht standardmäßig im aktuellen Verzeichnis nach .env

# Jetzt eine Anfrage stellen – Proxys werden automatisch angewendet
response = requests.get('https://httpbin.org/ip')
print(response.json())
```

- `load_dotenv()` liest die `.env`-Datei und setzt die Variablen in `os.environ`.
- `requests` erkennt `HTTP_PROXY`/`HTTPS_PROXY` automatisch – es ist nicht nötig, ein `proxies`-Dictionary zu übergeben, außer zum Überschreiben.

#### Schritt 4: Proxy-Verwendung überprüfen (Optional)
Um zu bestätigen, dass die Proxys funktionieren, testen Sie mit einem Dienst wie httpbin.org:

```python
import requests
from dotenv import load_dotenv

load_dotenv()

proxies = requests.utils.get_environ_proxies('https://httpbin.org/ip')  # Geladene Proxys inspizieren
print("Geladene Proxys:", proxies)

response = requests.get('https://httpbin.org/ip')
print("Ihre IP über den Proxy:", response.json())
```

Dies sollte die IP des Proxy-Servers anzeigen, falls korrekt konfiguriert.

#### Häufige Probleme und Tipps
- **Proxy-Authentifizierung**: Fügen Sie `benutzername:passwort@` in der URL hinzu, falls benötigt.
- **SOCKS-Proxys**: Verwenden Sie das Präfix `socks5://` (erfordert `requests[socks]` Extra: `pip install requests[socks]`).
- **Überschreiben pro Anfrage**: Wenn Sie für einen bestimmten Aufruf andere Proxys benötigen, übergeben Sie ein Dictionary:
  ```python:disable-run
  proxies = {'http': 'http://custom-proxy:port', 'https': 'https://custom-proxy:port'}
  response = requests.get('url', proxies=proxies)
  ```
- **Umgebung**: Funktioniert unter Windows/Linux/macOS. Unter Windows verwenden Sie `set` in cmd oder PowerShell-Entsprechungen.
- **Sicherheit**: Committen Sie `.env` niemals zur Versionskontrolle.

Dieses Setup ist einfach, sicher und folgt Best Practices für umgebungsbasierte Konfiguration.

[Requests Dokumentation: Proxys](https://requests.readthedocs.io/en/latest/user/advanced/#proxies)  
[python-dotenv Dokumentation](https://github.com/theskumar/python-dotenv)