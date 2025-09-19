---
audio: false
generated: false
image: false
lang: de
layout: post
title: GFW, Proxy-APIs und VPN-Erkennung
translated: true
---

### Inhaltsverzeichnis

1. [Können APIs in Proxy-Servern GFW-Sperren umgehen?](#können-apis-in-proxy-servern-gfw-sperren-umgehen)
   - Mischung aus Proxy- und API-Verkehr vermeidet GFW-Sperren
   - GFW unterscheidet zwischen Proxy- und normalem HTTP/HTTPS-Verkehr
   - GFW sperrt wahrscheinlich basierend auf ausschließlich Proxy-Verkehr
   - GFW nutzt ein Zeitfenster für die Verkehrsdatenanalyse
   - Regelmäßiger Zugriff auf die API kann Erkennung verhindern

2. [Wie die Great Firewall (GFW) funktioniert.](#wie-die-great-firewall-gfw-funktioniert)
   - GFW protokolliert Anfragen mit Quellen- und Zieldaten
   - Sperrt IPs, die mit illegalen Aktivitäten in Verbindung stehen
   - Nutzt Regeln zur Erkennung spezifischer Protokolle
   - Kann basierend auf dem Prozentsatz illegaler Anfragen sperren
   - Setzt KI für intelligente Verkehrsmustererkennung ein

3. [Analyse der ChatGPT-iOS-VPN-Erkennung](#analyse-der-chatgpt-ios-vpn-erkennung)
   - ChatGPT iOS funktioniert nun mit einigen VPNs
   - Zugriff hängt vom Standort des VPN-Servers ab
   - Erkennung basiert auf spezifischen IP-Adressen
   - Einige Cloud-Provider-IPs sind gesperrt

---

## Können APIs in Proxy-Servern GFW-Sperren umgehen?

Ich betreibe einen einfachen Server auf meiner Shadowsocks-Instanz mit folgendem Code:

```python
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # CORS für alle Routen aktivieren

@app.route('/bandwidth', methods=['GET'])
def get_bandwidth():
    # Führt den vnstat-Befehl aus, um die 5-Minuten-Intervall-Verkehrsstatistiken für eth0 zu erhalten
    result = subprocess.run(['vnstat', '-i', 'eth0', '-5', '--json'], capture_output=True, text=True)
    data = result.stdout

    # Gibt die erfassten Daten als JSON-Antwort zurück
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Und ich nutze nginx, um Port 443 wie folgt bereitzustellen:

```bash
server {
    listen 443 ssl;
    server_name www.some-domain.xyz;

    ssl_certificate /etc/letsencrypt/live/www.some-domain.xyz/fullchain.pem; # verwaltet von
    # ...
    location / {
        proxy_pass http://127.0.0.1:5000/;
        # ...
    }
}
```

Dieses Serverprogramm stellt Netzwerkdaten bereit, und ich nutze den Server als meinen Proxy-Server, um meinen Online-Status auf meinem Blog mithilfe der Netzwerkdaten anzuzeigen.

Interessanterweise wurde der Server bisher nicht von der Great Firewall (GFW) oder anderen Netzwerkkontrollsystemen gesperrt – und das bereits seit mehreren Tagen. Normalerweise würde der von mir eingerichtete Proxy-Server innerhalb von ein oder zwei Tagen gesperrt werden. Der Server führt ein Shadowsocks-Programm auf einem Port wie 51939 aus, sodass er mit gemischtem Shadowsocks- und normalem API-Verkehr arbeitet. Diese Mischung scheint die GFW dazu zu bringen, den Server nicht als dedizierten Proxy, sondern als normalen Server einzustufen, wodurch eine Sperrung der IP verhindert wird.

Diese Beobachtung ist faszinierend. Es scheint, dass die GFW spezifische Logik verwendet, um Proxy-Verkehr von normalem Verkehr zu unterscheiden. Während viele Websites wie Twitter und YouTube in China blockiert sind, bleiben zahlreiche ausländische Websites – wie die von internationalen Universitäten und Unternehmen – zugänglich.

Dies deutet darauf hin, dass die GFW wahrscheinlich auf Regeln basiert, die zwischen normalem HTTP/HTTPS-Verkehr und Proxy-Verkehr unterscheiden. Server, die beide Verkehrstypen abwickeln, scheinen Sperren zu entgehen, während Server, die ausschließlich Proxy-Verkehr verarbeiten, eher blockiert werden.

Eine Frage ist, welchen Zeitraum die GFW für die Datensammlung zur Sperrung verwendet – ob es sich um einen Tag oder eine Stunde handelt. Während dieses Zeitraums erkennt sie, ob der Verkehr ausschließlich von einem Proxy stammt. Falls ja, wird die IP des Servers gesperrt.

Ich besuche meinen Blog oft, um zu überprüfen, was ich geschrieben habe, aber in den kommenden Wochen werde ich mich auf andere Aufgaben konzentrieren, statt Blogbeiträge zu verfassen. Dadruch verringert sich mein Zugriff auf die `bandwidth`-API über Port 443. Falls ich feststelle, dass ich erneut gesperrt werde, sollte ich ein Programm schreiben, das regelmäßig auf diese API zugreift, um die GFW zu täuschen.

---

## Wie die Great Firewall (GFW) funktioniert.

### Schritt 1: Protokollierung von Anfragen

```python
import time

# Datenbank zur Speicherung von Anfragedaten
request_log = []

# Funktion zur Protokollierung von Anfragen
def log_request(source_ip, target_ip, target_port, body):
    request_log.append({
        'source_ip': source_ip,
        'target_ip': target_ip,
        'target_port': target_port,
        'body': body,
        'timestamp': time.time()
    })
```

Die Funktion `log_request` zeichnet eingehende Anfragen mit wesentlichen Informationen wie Quellen-IP, Ziel-IP, Ziel-Port, Anfragekörper und Zeitstempel auf.

### Schritt 2: Überprüfung und Sperrung von IPs

```python
# Funktion zur Überprüfung von Anfragen und Sperrung von IPs
def check_and_ban_ips():
    banned_ips = set()

    # Iteration über alle protokollierten Anfragen
    for request in request_log:
        if is_illegal(request):
            banned_ips.add(request['target_ip'])
        else:
            banned_ips.discard(request['target_ip'])

    # Sperrung aller identifizierten IPs
    ban_ips(banned_ips)
```

Die Funktion `check_and_ban_ips` durchläuft alle protokollierten Anfragen, identifiziert und sperrt IPs, die mit illegalen Aktivitäten in Verbindung stehen.

### Schritt 3: Definition illegaler Anfragen

```python
# Funktion zur Simulation der Überprüfung, ob eine Anfrage illegal ist
def is_illegal(request):
    # Platzhalter für tatsächliche Logik zur Überprüfung illegaler Anfragen
    # Beispiel: Überprüfung des Anfragekörpers oder des Ziels
    return "illegal" in request['body']
```

Hier überprüft `is_illegal`, ob der Anfragekörper das Wort "illegal" enthält. Dies kann auf komplexere Logik erweitert werden, je nachdem, was als illegale Aktivität gilt.

### Schritt 4: Sperrung identifizierter IPs

```python
# Funktion zur Sperrung einer Liste von IPs
def ban_ips(ip_set):
    for ip in ip_set:
        print(f"Sperre IP: {ip}")
```

Sobald illegale IPs identifiziert wurden, sperrt die Funktion `ban_ips` diese, indem sie deren IP-Adressen ausgibt (oder in einem echten System blockiert).

### Schritt 5: Alternative Methode zur Überprüfung und Sperrung von IPs basierend auf 80 % illegalen Anfragen

```python
# Funktion zur Überprüfung von Anfragen und Sperrung von IPs basierend auf 80 % illegalen Anfragen
def check_and_ban_ips():
    banned_ips = set()
    illegal_count = 0
    total_requests = 0

    # Iteration über alle protokollierten Anfragen
    for request in request_log:
        total_requests += 1
        if is_illegal(request):
            illegal_count += 1

    # Wenn 80 % oder mehr der Anfragen illegal sind, werden diese IPs gesperrt
    if total_requests > 0 and (illegal_count / total_requests) >= 0.8:
        for request in request_log:
            if is_illegal(request):
                banned_ips.add(request['target_ip'])

    # Sperrung aller identifizierten IPs
    ban_ips(banned_ips)
```

Diese alternative Methode bewertet, ob eine IP gesperrt werden sollte, basierend auf dem Prozentsatz illegaler Anfragen. Wenn 80 % oder mehr der Anfragen von einer IP illegal sind, wird sie gesperrt.

### Schritt 6: Erweiterte Überprüfung illegaler Anfragen (z. B. Shadowsocks- und Trojan-Protokoll-Erkennung)

```python
def is_illegal(request):
    # Überprüft, ob die Anfrage das Shadowsocks-Protokoll verwendet (Körper enthält binäre Daten)
    if request['target_port'] == 443:
        if is_trojan(request):
            return True
    elif is_shadowsocks(request):
        return True
    return False
```

Die Funktion `is_illegal` überprüft nun auch spezifische Protokolle wie Shadowsocks und Trojan:
- **Shadowsocks**: Es könnte nach verschlüsselten oder binären Daten im Anfragekörper gesucht werden.
- **Trojan**: Wenn die Anfrage über Port 443 (HTTPS) erfolgt und bestimmte Muster aufweist (z. B. Trojan-Verkehrscharakteristika), wird sie als illegal markiert.

### Schritt 7: Beispiel für legale Anfragen

Anfragen wie `GET https://some-domain.xyz/bandwidth` sind zweifellos legal und lösen keinen Sperrmechanismus aus.

### Schritt 8: Verkehrscharakteristika von Proxy-Servern

Proxy-Server weisen völlig andere Verkehrscharakteristika auf als normale Web- oder API-Server. Die GFW muss zwischen normalem Webserver-Verkehr und Proxy-Server-Verkehr unterscheiden können, die völlig unterschiedlich aussehen können.

### Schritt 9: Maschinelles Lernen und KI-Modelle für intelligente Erkennung

Angesichts der Vielzahl von Anfragen und Antworten, die durch das Internet gehen, könnte die GFW KI und maschinelle Lernmodelle einsetzen, um Verkehrsmuster zu analysieren und illegalen Verkehr intelligent zu erkennen. Durch das Training des Systems an einer Vielzahl von Verkehrstypen und den Einsatz fortschrittlicher Techniken könnte es Verkehr effektiver sperren oder filtern, basierend auf beobachteten Mustern.

---

## Update

Trotz meiner Bemühungen wird mein Proxy-Server weiterhin gesperrt. Um dies zu umgehen, habe ich eine Problemumgehung mit der Funktion „Reverse-IP“ von Digital Ocean implementiert, die es mir ermöglicht, schnell eine neue IP-Adresse zuzuweisen, sobald eine Sperrung auftritt.

---

## Analyse der ChatGPT-iOS-VPN-Erkennung

*26.12.2024*

Heute habe ich entdeckt, dass die ChatGPT-iOS-App nun das Einloggen mit einem VPN in China ermöglicht. Früher wurde eine Sperrmeldung angezeigt, wie im folgenden Beispiel:

Allerdings funktioniert es seit heute problemlos mit einem VPN.

Ich erinnere mich, dass bei der ersten Veröffentlichung der ChatGPT-iOS-App die Nutzung mit einem VPN kein Problem darstellte. Später wurde die VPN-Erkennung strenger, sodass ein Login schwierig wurde. Zum Glück scheint diese Einschränkung kürzlich gelockert worden zu sein.

Bei weiteren Tests stellte ich fest, dass ich mit einem DigitalOcean-VPN in der Region Singapur nicht auf die App zugreifen konnte. Bei der Nutzung von VPNs aus Taiwan oder dem Vereinigten Königreich (bereitgestellt von https://zhs.cloud) funktionierte es jedoch einwandfrei.

Es scheint, dass die ChatGPT-iOS-VPN-Erkennung auf bestimmten IP-Adressen basiert. Einige Cloud-Provider oder bestimmte IP-Adressen sind gesperrt, was das inkonsistente Verhalten je nach Standort des VPN-Servers erklären könnte.

![](assets/images/chatgpt/block.jpg){: .responsive }

![](assets/images/chatgpt/c1.png){: .responsive }