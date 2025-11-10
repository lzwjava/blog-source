---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Verwenden von requests.Session für persistente HTTP-Sitzungen
translated: true
type: note
---

### Wie requests.Session funktioniert

In der `requests`-Bibliothek von Python ist `requests.Session` eine Klasse, die es ermöglicht, eine persistente Sitzung über mehrere HTTP-Anfragen hinweg aufrechtzuerhalten. Sie bietet mehrere Vorteile gegenüber einzelnen `requests.get()`-Aufrufen oder ähnlichen:

- **Persistenz von Cookies**: Standardmäßig speichert und sendet sie automatisch Cookies, die vom Server empfangen wurden, in nachfolgenden Anfragen. Dies ermöglicht sitzungsbasierte Interaktionen, wie z. B. das einmalige Anmelden und authentifiziert bleiben.
- **Verbindungspooling**: Sie wiederverwendet zugrunde liegende TCP-Verbindungen für denselben Host, was die Leistung verbessert, indem der Overhead für das Aufbauen neuer Verbindungen vermieden wird.
- **Gemeinsame Konfigurationen**: Sie können Standard-Header, Authentifizierung, Proxys oder andere Parameter festlegen, die für alle Anfragen innerhalb der Sitzung gelten.
- **Im Hintergrund**: Sie verwendet die `urllib3`-Bibliothek für die HTTP-Abwicklung. Wenn Sie eine `Session` erstellen, initialisiert sie Attribute wie `cookies` (eine `RequestsCookieJar`-Instanz), `headers` und mehr. Beispielsweise werden Cookies aus einer Antwort automatisch in der nächsten Anfrage an dieselbe Domain eingeschlossen.

Hier ist ein einfaches Beispiel für das Erstellen und Verwenden einer Sitzung:

```python
import requests

# Eine Sitzung erstellen
session = requests.Session()

# Einen Standard-Header für alle Anfragen in dieser Sitzung setzen
session.headers.update({'User-Agent': 'MyApp/1.0'})

# Mehrere Anfragen stellen, die die Sitzung teilen
response1 = session.get('https://example.com/login')
response2 = session.post('https://example.com/data', data={'key': 'value'})

# Auf die in der Sitzung gespeicherten Cookies zugreifen
print(session.cookies)
```

Dies stellt sicher, dass Cookies (wie Session-IDs) transparent ohne manuelles Eingreifen behandelt werden.

### Python verwenden, um APIs von Java/Spring-Projekten aufzurufen

Um mit APIs zu interagieren, die mit Java/Spring erstellt wurden (typischerweise RESTful-Endpunkte über Spring MVC oder Spring Boot), verwenden Sie `requests.Session` genauso wie mit jeder anderen HTTP-API. Spring-Projekte stellen APIs oft über HTTP/HTTPS bereit, und `requests` kann Authentifizierung, CSRF-Tokens oder Ratenbegrenzung handhaben, falls implementiert.

- **Authentifizierung**: Spring könnte Spring Security mit Formularen, JWT oder OAuth verwenden. Für sitzungsbasierte Authentifizierung (z. B. über Login-Formulare) automatisiert `requests.Session` die Cookie-Behandlung nach einer Login-Anfrage.
- **Aufrufe tätigen**: Verwenden Sie Standard-HTTP-Methoden wie `GET`, `POST` usw. Wenn die Spring-API JSON-Payloads erfordert, übergeben Sie `json=your_data`.

Beispiel für das Anmelden an einer Spring-authentifizierten API und das Aufrufen eines weiteren Endpunkts:

```python
import requests

session = requests.Session()

# Anmelden (angenommen ein POST an /login mit Benutzername/Passwort)
login_payload = {'username': 'user', 'password': 'pass'}
response = session.post('https://spring-api.example.com/login', data=login_payload)

if response.ok:
    # Nun einen anderen API-Endpunkt aufrufen, Sitzungs-Cookies bleiben erhalten
    data_response = session.get('https://spring-api.example.com/api/data')
    print(data_response.json())
else:
    print("Login fehlgeschlagen")
```

Spring-APIs sind standardmäßig zustandslos, können aber Sitzungen über serverseitige Speicherung (z. B. in Tomcat oder eingebetteten Servern) verwalten. Stellen Sie sicher, dass Ihr Python-Client alle CORS-, CSRF- oder benutzerdefinierten Header handhabt, die von Spring benötigt werden.

### Beziehung zu JSESSIONID auf der Java/Spring-Seite

- **Was ist JSESSIONID?**: In Java-Webanwendungen (einschließlich Spring, die oft auf Servlet-Containern wie Tomcat läuft) ist JSESSIONID ein standardmäßiger HTTP-Cookie, der vom Container verwendet wird, um Benutzersitzungen zu verfolgen. Er wird gesetzt, wenn eine Sitzung erstellt wird (z. B. nach dem Login), und in Antworten zurückgesendet. Auf der Client-Seite schließen Browser (oder HTTP-Clients wie `requests`) ihn in nachfolgenden Anfragen ein, um den Zustand beizubehalten, wie z. B. Benutzerauthentifizierung oder Warenkorbdaten.
- **Wie es sich auf requests.Session bezieht**: `requests.Session` behandelt JSESSIONID wie jeden anderen Cookie – sie speichert ihn automatisch aus dem "Set-Cookie"-Header des Servers und schließt ihn in den "Cookie"-Header zukünftiger Anfragen ein. Dies ermöglicht eine nahtlose Interaktion mit zustandsbehafteten Spring-APIs ohne manuelles Parsen/Extrahieren von Cookies.
- **Serverseitige Behandlung**: Auf der Java/Spring-Seite verwaltet der ServletContext die Sitzungen. Wenn Ihr Python-Client eine Anfrage mit JSESSIONID sendet, ruft die HttpSession von Spring die zugehörigen serverseitigen Daten ab. Wenn sie abgelaufen oder ungültig ist, könnte Spring eine erneute Authentifizierung verlangen. Für sichere Sitzungen sollten Sie sicherstellen, dass Ihr Setup HTTPS verwendet, da JSESSIONID über HTTP anfällig für Diebstahl sein kann.
- **Mögliche Probleme**: Wenn Spring CSRF-Tokens oder andere Schutzmaßnahmen erzwingt, müssen Sie diese möglicherweise extrahieren und einbinden (z. B. aus versteckten Formularfeldern). Für zustandslose JWT-basierte Spring-APIs hilft `requests.Session` immer noch, indem sie Auth-Tokens in Headern persistent speichert, aber JSESSIONID wird weniger relevant.

Wenn Sie spezifische Fehler (z. B. 401 Unauthorized) beim Aufruf einer Spring-API erhalten, überprüfen Sie die Netzwerkprotokolle auf Cookie-Probleme oder aktivieren Sie das `requests`-Debugging mit `import logging; logging.basicConfig(level=logging.DEBUG)`. Für mehr zu Spring Security, konsultieren Sie die offizielle Dokumentation.