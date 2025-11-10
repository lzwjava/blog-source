---
audio: false
generated: true
image: false
lang: de
layout: post
title: Persistente HTTP-Sitzungen mit Python Requests
translated: true
type: note
---

Eine `Session` in Pythons `requests`-Bibliothek ist eine Möglichkeit, bestimmte Parameter wie Cookies, Header und Authentifizierung über mehrere HTTP-Anfragen hinweg beizubehalten. Sie bietet eine praktische Schnittstelle für wiederholte Anfragen an denselben Server oder verwandte Endpunkte, während der Zustand erhalten bleibt, die Effizienz verbessert und der Code vereinfacht wird. Im Folgenden werde ich erklären, wie `requests.Session` funktioniert, seine Hauptmerkmale vorstellen und Beispiele zur Veranschaulichung der Nutzung liefern.

## Was ist eine `requests.Session`?

Die `requests`-Bibliothek wird häufig für HTTP-Anfragen in Python verwendet. Während Sie eigenständige Funktionen wie `requests.get()` oder `requests.post()` nutzen können, erlaubt ein `Session`-Objekt die Erstellung einer persistenten Sitzung, die Konfigurationen (z.B. Cookies, Header oder Authentifizierungsdaten) über mehrere Anfragen hinweg beibehält. Dies ist besonders nützlich für die Interaktion mit Websites oder APIs, die zustandsbehaftete Interaktionen erfordern, wie das Aufrechterhalten einer Login-Sitzung oder die Wiederverwendung von TCP-Verbindungen.

Ein `Session`-Objekt:
- Behält Cookies über Anfragen hinweg bei.
- Wiederverwendet zugrundeliegende TCP-Verbindungen (mittels Connection Pooling) für eine bessere Leistung bei mehreren Anfragen an denselben Host.
- Ermöglicht das Setzen von Standardparametern (z.B. Header, Timeouts), die für alle mit der Sitzung gestellten Anfragen gelten.
- Unterstützt Authentifizierung und benutzerdefinierte Konfigurationen.

## Wie funktioniert `Session`?

Wenn Sie ein `Session`-Objekt erstellen, agiert es als Container für Ihre HTTP-Anfragen. Hier ist eine Aufschlüsselung der Funktionsweise:

1. **Persistente Cookies**: Wenn Sie eine Anfrage mit einer `Session` stellen, werden alle vom Server gesetzten Cookies (z.B. Sitzungs-Cookies nach dem Login) in der Sitzung gespeichert und automatisch bei nachfolgenden Anfragen mitgesendet. Dies ist entscheidend für die Zustandserhaltung, z.B. um eingeloggt zu bleiben.

2. **Connection Pooling**: Für Anfragen an denselben Host verwendet die `Session` dieselbe TCP-Verbindung wieder, was Latenz und Overhead im Vergleich zur Erstellung neuer Verbindungen für jede Anfrage reduziert.

3. **Standardparameter**: Sie können Attribute wie Header, Authentifizierung oder Timeouts am `Session`-Objekt setzen, und diese werden auf alle mit dieser Sitzung gestellten Anfragen angewendet, sofern sie nicht überschrieben werden.

4. **Anpassbar**: Sie können Proxies, SSL-Verifizierung konfigurieren oder sogar benutzerdefinierte Adapter mounten (z.B. für Wiederholungen oder benutzerdefinierten Transport), um zu steuern, wie Anfragen behandelt werden.

## Grundlegende Verwendung

Hier ist ein einfaches Beispiel, wie `requests.Session` verwendet wird:

```python
import requests

# Eine Sitzung erstellen
session = requests.Session()

# Standard-Header für alle Anfragen in dieser Sitzung setzen
session.headers.update({'User-Agent': 'MyApp/1.0'})

# Eine GET-Anfrage stellen
response1 = session.get('https://api.example.com/data')
print(response1.json())

# Eine weitere Anfrage stellen; Cookies und Header werden wiederverwendet
response2 = session.post('https://api.example.com/submit', data={'key': 'value'})
print(response2.json())

# Sitzung schließen, um Ressourcen freizugeben
session.close()
```

In diesem Beispiel:
- Eine `Session` wird erstellt und ein benutzerdefinierter `User-Agent`-Header für alle Anfragen gesetzt.
- Die Sitzung verwaltet Cookies automatisch. Wenn `response1` ein Cookie setzt, wird es mit `response2` mitgesendet.
- Die Sitzung verwendet die Verbindung zu `api.example.com` wieder, was die Leistung verbessert.

## Hauptmerkmale und Beispiele

### 1. **Cookies beibehalten**
Sitzungen sind besonders nützlich für Websites, die Cookies zur Zustandserhaltung verwenden, wie z.B. Login-Sitzungen.

```python
import requests

# Eine Sitzung erstellen
session = requests.Session()

# Auf einer Website einloggen
login_data = {'username': 'user', 'password': 'pass'}
response = session.post('https://example.com/login', data=login_data)

# Auf eine geschützte Seite zugreifen; die Sitzung sendet automatisch das Login-Cookie mit
protected_page = session.get('https://example.com/protected')
print(protected_page.text)

# Sitzung schließen
session.close()
```

Hier speichert die Sitzung das Authentifizierungs-Cookie von der Login-Anfrage und sendet es mit der nachfolgenden Anfrage an die geschützte Seite mit.

### 2. **Standardparameter setzen**
Sie können Standard-Header, Authentifizierung oder andere Parameter für alle Anfragen in der Sitzung setzen.

```python
import requests
import functools

session = requests.Session()

# Standard-Header setzen
session.headers.update({
    'Authorization': 'Bearer my_token',
    'Accept': 'application/json'
})

# Standard-Timeout setzen
session.request = functools.partial(session.request, timeout=5)

# Anfragen stellen; Header und Timeout werden automatisch angewendet
response1 = session.get('https://api.example.com/endpoint1')
response2 = session.get('https://api.example.com/endpoint2')

session.close()
```

### 3. **Connection Pooling**
Wenn mehrere Anfragen an denselben Host gestellt werden, verwendet `Session` Verbindungen wieder, was effizienter ist als eigenständige Anfragen.

```python
import requests
import time

# Ohne Sitzung
start = time.time()
for _ in range(5):
    requests.get('https://api.example.com/data')
print(f"Without session: {time.time() - start} seconds")

# Mit Sitzung
session = requests.Session()
start = time.time()
for _ in range(5):
    session.get('https://api.example.com/data')
print(f"With session: {time.time() - start} seconds")
session.close()
```

Die sitzungsbasierten Anfragen sind typischerweise schneller, da sie die TCP-Verbindung wiederverwenden.

### 4. **Authentifizierung**
Sitzungen vereinfachen den Umgang mit Authentifizierung, wie HTTP Basic Auth oder benutzerdefinierte Token-basierte Authentifizierung.

```python
import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()
session.auth = HTTPBasicAuth('user', 'pass')

# Alle Anfragen werden Basic Auth beinhalten
response = session.get('https://api.example.com/protected')
print(response.json())

session.close()
```

### 5. **Benutzerdefinierte Adapter**
Sie können benutzerdefinierte Adapter mounten, um beispielsweise Wiederholungsversuche oder das Verbindungs-Pooling-Verhalten zu steuern.

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()

# Wiederholungsversuche konfigurieren
retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

# Eine Anfrage mit Wiederholungslogik stellen
response = session.get('https://api.example.com/unstable_endpoint')
print(response.json())

session.close()
```

Dieses Beispiel richtet automatische Wiederholungsversuche für bestimmte HTTP-Fehlercodes ein.

## Wann `Session` verwenden

Verwenden Sie `requests.Session`, wenn:
- Sie Zustand (z.B. Cookies) über mehrere Anfragen hinweg beibehalten müssen, wie z.B. für die Authentifizierung.
- Sie mehrere Anfragen an denselben Host stellen und von Connection Pooling profitieren möchten.
- Sie konsistente Konfigurationen (Header, Timeouts, etc.) über Anfragen hinweg anwenden möchten.
- Sie mit APIs oder Websites interagieren, die sitzungsbasierte Interaktionen erfordern.

Wenn Sie eine einzelne Anfrage stellen oder keinen Zustand beibehalten müssen, sind eigenständige `requests.get()` oder `requests.post()` ausreichend.

## Eine Sitzung schließen

Schließen Sie eine Sitzung immer, wenn Sie fertig sind, um Ressourcen (z.B. Verbindungen) freizugeben:

```python
session.close()
```

Alternativ können Sie eine Sitzung als Kontextmanager verwenden, um sicherzustellen, dass sie automatisch geschlossen wird:

```python
with requests.Session() as session:
    session.headers.update({'User-Agent': 'MyApp/1.0'})
    response = session.get('https://api.example.com/data')
    print(response.json())
# Sitzung wird automatisch geschlossen, wenn der Block verlassen wird
```

## Erweiterte Hinweise
- **Thread-Sicherheit**: `Session`-Objekte sind nicht thread-sicher. Wenn Sie Multithreading verwenden, erstellen Sie eine separate `Session` für jeden Thread.
- **Proxies**: Sie können Proxies für eine Sitzung mit `session.proxies = {'http': 'http://proxy.com', 'https': 'https://proxy.com'}` setzen.
- **SSL-Verifizierung**: Standardmäßig verifiziert `Session` SSL-Zertifikate. Zum Deaktivieren (nicht für die Produktion empfohlen) verwenden Sie `session.verify = False`.

## Referenzen
[Requests-Dokumentation](https://requests.readthedocs.io/en/latest/)  
[Requests Session-Objekte](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects)