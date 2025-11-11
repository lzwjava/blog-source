---
audio: false
generated: true
lang: de
layout: post
title: Python Requests Bibliothek
translated: true
type: note
---

Um Postman vollständig durch die Python `requests` Bibliothek zu ersetzen, können Sie alle gängigen HTTP-Operationen durchführen, wie das Senden verschiedener Arten von Anfragen, das Verwalten von Headern, das Arbeiten mit JSON-Daten, das Hochladen von Dateien, die Verwendung von Proxys und das Überprüfen von Antworten. Im Folgenden führe ich Sie Schritt für Schritt durch Beispiele für jede dieser Funktionalitäten, um Ihnen eine vollständige und praktische Anleitung zu bieten.

### Schritt 1: Installieren der Requests-Bibliothek
Stellen Sie sicher, dass die `requests`-Bibliothek installiert ist, bevor Sie beginnen. Führen Sie diesen Befehl in Ihrem Terminal aus:

```bash
pip install requests
```

Lassen Sie uns nun in die Beispiele eintauchen.

---

### HTTP-Anfragen senden
Die `requests`-Bibliothek unterstützt alle HTTP-Methoden wie GET, POST, PUT, DELETE usw. So senden Sie eine einfache GET- und POST-Anfrage:

#### GET-Anfrage
```python
import requests

# Sende eine GET-Anfrage
response = requests.get('https://api.example.com/data')

# Gib den Statuscode und den Antworttext aus
print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

#### POST-Anfrage
```python
# Sende eine POST-Anfrage ohne Daten
response = requests.post('https://api.example.com/submit')

print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

---

### Header hinzufügen
Header werden häufig für Authentifizierung, Content-Types oder benutzerdefinierte Metadaten verwendet. Übergeben Sie sie als Wörterbuch an den `headers`-Parameter.

```python
# Definiere benutzerdefinierte Header
headers = {
    'Authorization': 'Bearer my_token',
    'Content-Type': 'application/json',
    'User-Agent': 'MyApp/1.0'
}

# Sende eine GET-Anfrage mit Headern
response = requests.get('https://api.example.com/data', headers=headers)

print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Response Body:", response.text)
```

---

### JSON-Daten senden
Um JSON-Daten in einer POST-Anfrage zu senden (wie das Auswählen von JSON in Postman's Body-Tab), verwenden Sie den `json`-Parameter. Dies setzt automatisch den `Content-Type` auf `application/json`.

```python
# Definiere JSON-Daten
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# Sende eine POST-Anfrage mit JSON-Daten
response = requests.post('https://api.example.com/submit', json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
```

---

### Dateien hochladen
Um Dateien hochzuladen (ähnlich wie Postman's Form-Data-Option), verwenden Sie den `files`-Parameter. Öffnen Sie Dateien im Binärmodus (`'rb'`) und fügen Sie optional zusätzliche Formulardaten hinzu.

#### Einfacher Datei-Upload
```python
# Bereite Datei für den Upload vor
files = {
    'file': open('myfile.txt', 'rb')
}

# Sende POST-Anfrage mit Datei
response = requests.post('https://api.example.com/upload', files=files)

print("Status Code:", response.status_code)
print("Response Body:", response.text)

# Schließe die Datei manuell
files['file'].close()
```

#### Datei-Upload mit Formulardaten (Empfohlener Ansatz)
Die Verwendung einer `with`-Anweisung stellt sicher, dass die Datei automatisch geschlossen wird:
```python
# Zusätzliche Formulardaten
form_data = {
    'description': 'My file upload'
}

# Öffne und lade Datei hoch
with open('myfile.txt', 'rb') as f:
    files = {
        'file': f
    }
    response = requests.post('https://api.example.com/upload', data=form_data, files=files)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

---

### Proxys verwenden
Um Anfragen über einen Proxy zu routen (ähnlich wie Postman's Proxy-Einstellungen), verwenden Sie den `proxies`-Parameter mit einem Wörterbuch.

```python
# Definiere Proxy-Einstellungen
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# Sende eine Anfrage über einen Proxy
response = requests.get('https://api.example.com/data', proxies=proxies)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

---

### Antworten verarbeiten und überprüfen
Die `requests`-Bibliothek bietet einfachen Zugriff auf Antwortdetails wie Statuscodes, JSON-Daten, Header und Cookies. Sie können Pythons `assert`-Anweisungen verwenden, um Antworten zu validieren, ähnlich wie Postman's Test-Skripte.

#### JSON-Antworten parsen
```python
response = requests.get('https://api.example.com/data')

# Überprüfe Statuscode und parse JSON
if response.status_code == 200:
    data = response.json()  # Konvertiert die Antwort in ein Python-Dict/Liste
    print("JSON Data:", data)
else:
    print("Error:", response.status_code)
```

#### Antwortdetails überprüfen
```python
response = requests.get('https://api.example.com/data')

# Überprüfe Statuscode
assert response.status_code == 200, f"Erwartet 200, erhielt {response.status_code}"

# Parse JSON und überprüfe Inhalt
data = response.json()
assert 'key' in data, "Schlüssel nicht in der Antwort gefunden"
assert data['key'] == 'expected_value', "Wert stimmt nicht überein"

# Überprüfe Response-Header
assert 'Content-Type' in response.headers, "Content-Type-Header fehlt"
assert response.headers['Content-Type'] == 'application/json', "Unerwarteter Content-Type"

# Überprüfe Cookies
cookies = response.cookies
assert 'session_id' in cookies, "Session-ID-Cookie fehlt"

print("Alle Überprüfungen bestanden!")
```

#### Fehlerbehandlung
Wickeln Sie Anfragen in einen `try-except`-Block ein, um Netzwerk- oder HTTP-Fehler abzufangen:
```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # Löst eine Exception für 4xx/5xx Fehler aus
    data = response.json()
    print("Data:", data)
except requests.exceptions.RequestException as e:
    print("Anfrage fehlgeschlagen:", e)
```

---

### Umfassendes Beispiel
Hier ist ein vollständiges Beispiel, das Header, Datei-Upload, Proxys und Antwortüberprüfungen kombiniert:

```python
import requests

# Definiere Header
headers = {
    'Authorization': 'Bearer my_token'
}

# Formulardaten und Datei
form_data = {
    'description': 'My file upload'
}

# Proxy-Einstellungen
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# Sende Anfrage mit Datei-Upload
try:
    with open('myfile.txt', 'rb') as f:
        files = {'file': f}
        response = requests.post(
            'https://api.example.com/upload',
            headers=headers,
            data=form_data,
            files=files,
            proxies=proxies
        )
        response.raise_for_status()  # Überprüfe auf HTTP-Fehler

        # Parse und überprüfe Antwort
        data = response.json()
        assert 'upload_id' in data, "Upload-ID nicht in der Antwort gefunden"
        print("Upload erfolgreich, ID:", data['upload_id'])

except requests.exceptions.RequestException as e:
    print("Anfrage fehlgeschlagen:", e)
```

---

### Wiederverwendbare Funktionen (Ersetzen von Postman Collections)
Um Postman's gespeicherte Anfragen oder Collections nachzuahmen, kapseln Sie die Logik in Funktionen:

```python
def upload_file(file_path, description, token, proxy=None):
    headers = {'Authorization': f'Bearer {token}'}
    data = {'description': description}
    proxies = {'http': proxy, 'https': proxy} if proxy else None

    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(
                'https://api.example.com/upload',
                headers=headers,
                data=data,
                files=files,
                proxies=proxies
            )
            response.raise_for_status()
            data = response.json()
            assert 'upload_id' in data, "Upload-ID nicht gefunden"
            return data['upload_id']
    except requests.exceptions.RequestException as e:
        print("Anfrage fehlgeschlagen:", e)
        return None

# Verwendung
upload_id = upload_file('myfile.txt', 'My file upload', 'my_token', 'http://myproxy:8080')
if upload_id:
    print("Upload erfolgreich, ID:", upload_id)
```

---

### Zusätzliche Funktionen
- **Sessions**: Verwenden Sie `requests.Session()`, um Cookies oder Header über mehrere Anfragen hinweg beizubehalten.
- **Timeouts**: Fügen Sie Anfragen `timeout=5` (Sekunden) hinzu, um Hängen zu vermeiden.
- **Weiterleitungen**: Kontrollieren Sie mit `allow_redirects=True/False`.

---

### Zusammenfassung
Mit der `requests`-Bibliothek können Sie:
- HTTP-Anfragen senden (`get`, `post`, usw.)
- Header, JSON-Daten und Datei-Uploads einbeziehen
- Proxys verwenden
- Antworten parsen und überprüfen (Status, JSON, Header, Cookies)
- Code in wiederverwendbare Funktionen organisieren

Dies bietet Ihnen eine programmatische, flexible Alternative zu Postman, die sich für Skripting und Automatisierung eignet!