---
audio: true
lang: de
layout: post
title: Analyse der Sperrung von Proxy-Servern
translated: true
---

## Können APIs in Proxy-Servern GFW-Sperren umgehen?

Ich betreibe einen einfachen Server auf meiner Shadowsocks-Instanz mit dem folgenden Code:

```python
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
```

```python
app = Flask(__name__)
CORS(app)  # CORS für alle Routen aktivieren
```

@app.route('/bandwidth', methods=['GET'])
def get_bandwidth():
    # Führe den vnstat-Befehl aus, um die Verkehrsstatistiken im 5-Minuten-Intervall für eth0 zu erhalten
    result = subprocess.run(['vnstat', '-i', 'eth0', '-5', '--json'], capture_output=True, text=True)
    data = result.stdout

    # Gib die erfassten Daten als JSON-Antwort zurück
    return jsonify(data)

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Und ich verwende nginx, um den Port 443 zu bedienen, wie unten gezeigt:

```bash
server {
    listen 443 ssl;
    server_name www.some-domain.xyz;
```

    ssl_certificate /etc/letsencrypt/live/www.some-domain.xyz/fullchain.pem; # verwaltet von 
    # ...
    location / {

```nginx
        proxy_pass http://127.0.0.1:5000/;
        # ...
    }
}
```

Dieses Server-Programm stellt Netzwerkdaten bereit, und ich verwende den Server als meinen Proxy-Server, wodurch ich meinen Online-Status auf meinem Blog mithilfe der Netzwerkdaten anzeigen kann.

Interessanterweise wurde der Server seit mehreren Tagen nicht von der Great Firewall (GFW) oder anderen Netzwerkkontrollsystemen gesperrt. Normalerweise würde der von mir eingerichtete Proxy-Server innerhalb von ein oder zwei Tagen gesperrt werden. Der Server führt ein Shadowsocks-Programm auf einem Port wie 51939 aus, sodass er mit Shadowsocks-Datenverkehr gemischt mit regulärem API-Datenverkehr arbeitet. Diese Mischung scheint die GFW dazu zu veranlassen, zu glauben, dass der Server kein dedizierter Proxy ist, sondern ein normaler Server, was dazu führt, dass die IP nicht gesperrt wird.

Diese Beobachtung ist faszinierend. Es scheint, dass die Great Firewall (GFW) eine spezifische Logik verwendet, um Proxy-Datenverkehr von regulärem Datenverkehr zu unterscheiden. Während viele Websites wie Twitter und YouTube in China blockiert sind, bleiben zahlreiche ausländische Websites – wie die internationaler Universitäten und Unternehmen – zugänglich.

Dies deutet darauf hin, dass die GFW wahrscheinlich auf Regeln basiert, die zwischen normalem HTTP/HTTPS-Datenverkehr und Proxy-bezogenem Datenverkehr unterscheiden. Server, die beide Arten von Datenverkehr verarbeiten, scheinen Sperren zu vermeiden, während Server, die nur Proxy-Datenverkehr verarbeiten, mit höherer Wahrscheinlichkeit blockiert werden.

Eine Frage ist, welchen Zeitraum die GFW nutzt, um Daten für Sperrungen zu sammeln – ob es ein Tag oder eine Stunde ist. Während dieses Zeitraums wird überprüft, ob der Datenverkehr ausschließlich von einem Proxy stammt. Wenn dies der Fall ist, wird die IP des Servers gesperrt.

Ich besuche oft mein Blog, um zu überprüfen, was ich geschrieben habe, aber in den kommenden Wochen wird sich mein Fokus auf andere Aufgaben verlagern, anstatt Blogbeiträge zu schreiben. Dies wird meinen Zugriff auf die `bandwidth` API über Port 443 reduzieren. Wenn ich feststelle, dass ich erneut gesperrt werde, sollte ich ein Programm schreiben, das regelmäßig auf diese API zugreift, um die GFW auszutricksen.

Hier ist die überarbeitete Version Ihres Textes mit verbesserter Struktur und Klarheit:

## Wie die Große Firewall (GFW) funktioniert.

### Schritt 1: Anfragen protokollieren

```python
import time
```

# Datenbank zur Speicherung von Anfragedaten
request_log = []

# Funktion zum Protokollieren von Anfragen
def log_request(source_ip, target_ip, target_port, body):
    request_log.append({
        'source_ip': source_ip,
        'target_ip': target_ip,
        'target_port': target_port,
        'body': body,
        'timestamp': time.time()
    })
```

Die Funktion `log_request` zeichnet eingehende Anfragen mit wesentlichen Informationen wie der Quell-IP, der Ziel-IP, dem Zielport, dem Anfragekörper und dem Zeitstempel auf.

### Schritt 2: Überprüfen und Sperren von IPs

```python
# Funktion zur Überprüfung von Anfragen und zum Sperren von IPs
def check_and_ban_ips():
    banned_ips = set()
```

    # Über alle protokollierten Anfragen iterieren
    for request in request_log:
        if is_illegal(request):
            banned_ips.add(request['target_ip'])
        else:
            banned_ips.discard(request['target_ip'])

    # Verbote auf alle identifizierten IPs anwenden
    ban_ips(banned_ips)
```

Die Funktion `check_and_ban_ips` durchläuft alle protokollierten Anfragen, identifiziert und sperrt IPs, die mit illegalen Aktivitäten in Verbindung stehen.

### Schritt 3: Definition, was eine Anfrage illegal macht

```python
# Funktion zur Simulation der Überprüfung, ob eine Anfrage illegal ist
def is_illegal(request):
    # Platzhalter für die tatsächliche Logik zur Überprüfung illegaler Anfragen
    # Zum Beispiel: Überprüfung des Anfragekörpers oder des Ziels
    return "illegal" in request['body']
```

Hier überprüft `is_illegal`, ob der Anfragekörper das Wort "illegal" enthält. Dies kann je nachdem, was als illegale Aktivität gilt, zu einer komplexeren Logik erweitert werden.

### Schritt 4: Sperren der identifizierten IPs

```python
# Funktion zum Sperren einer Liste von IPs
def ban_ips(ip_set):
    for ip in ip_set:
        print(f"IP wird gesperrt: {ip}")
```

Sobald illegale IPs identifiziert wurden, verbietet die Funktion `ban_ips` sie, indem sie ihre IP-Adressen ausgibt (oder in einem echten System könnte sie sie blockieren).

### Schritt 5: Alternative Methode zur Überprüfung und Sperrung von IPs basierend auf 80 % illegalen Anfragen

```python
# Funktion zur Überprüfung von Anfragen und zum Sperren von IPs basierend auf 80% illegalen Anfragen
def check_and_ban_ips():
    banned_ips = set()
    illegal_count = 0
    total_requests = 0
```

    # Über alle protokollierten Anfragen iterieren
    for request in request_log:
        total_requests += 1
        if is_illegal(request):
            illegal_count += 1

    # Wenn 80 % oder mehr der Anfragen illegal sind, sperre diese IPs
    if total_requests > 0 and (illegal_count / total_requests) >= 0.8:
        for request in request_log:
            if is_illegal(request):
                banned_ips.add(request['target_ip'])

    # Verbote auf alle identifizierten IPs anwenden
    ban_ips(banned_ips)
```

Diese alternative Methode bewertet, ob eine IP gesperrt werden sollte, basierend auf dem Prozentsatz der illegalen Anfragen. Wenn 80 % oder mehr der Anfragen von einer IP illegal sind, wird sie gesperrt.

### Schritt 6: Erweiterte Überprüfung auf illegale Anfragen (z. B. Shadowsocks- und Trojan-Protokoll-Erkennung)

```python
def is_illegal(request):
    # Überprüfen, ob die Anfrage das Shadowsocks-Protokoll verwendet (der Körper enthält binäre Daten)
    if request['target_port'] == 443:
        if is_trojan(request):
            return True
    elif is_shadowsocks(request):
        return True
    return False
```

Die Funktion `is_illegal` überprüft nun auch spezifische Protokolle wie Shadowsocks und Trojan:
- **Shadowsocks**: Wir könnten verschlüsselte oder binärähnliche Daten im Anfragekörper überprüfen.
- **Trojan**: Wenn die Anfrage über Port 443 (HTTPS) kommt und bestimmte Muster aufweist (z. B. Trojan-Verkehrsmerkmale), wird sie als illegal gekennzeichnet.

### Schritt 7: Beispiel für rechtliche Anfragen

Beispielsweise sind Anfragen wie `GET https://some-domain.xyz/bandwidth` sicherlich legal und werden den Sperrmechanismus nicht auslösen.

### Schritt 8: Merkmale des Proxy-Server-Datenverkehrs

Proxyserver haben sehr unterschiedliche Verkehrsmerkmale im Vergleich zu regulären Web- oder API-Servern. Die GFW muss zwischen dem normalen Web-Server-Verkehr und dem Proxy-Server-Verkehr unterscheiden, der völlig anders aussehen kann.

### Schritt 9: Maschinelles Lernen und KI-Modelle für intelligente Erkennung

Angesichts der Vielzahl von Anfragen und Antworten, die das Internet durchlaufen, könnte die GFW (Great Firewall) KI- und Machine-Learning-Modelle einsetzen, um Verkehrsmuster zu analysieren und illegales Verhalten intelligent zu erkennen. Indem das System mit verschiedenen Verkehrstypen trainiert und fortschrittliche Techniken verwendet werden, könnte es den Verkehr effektiver basierend auf beobachteten Mustern blockieren oder filtern.

