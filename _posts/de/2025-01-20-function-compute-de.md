---
audio: true
lang: de
layout: post
title: Function Compute auf Alibaba Cloud
translated: true
---

Ich habe eine Funktion mit Alibaba Cloud's Function Compute eingerichtet. Mein Ziel ist es, normal aussehenden Traffic zu erzeugen, um die Aktivität meines Proxy-Servers vor der GFW zu verschleiern. Dazu habe ich einen Bandbreiten-Server neben meinem Proxy bereitgestellt. Nun verwende ich Alibaba Cloud's Function Compute, um jede Minute eine Anfrage an diese Bandbreiten-API zu stellen, wodurch eine Mischung aus normalem und Proxy-Traffic entsteht.

```python
from flask import Flask, request, jsonify
import requests
import time

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # Protokolliere die Request-ID und andere Details
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    data = request.stream.read()
    print("Path: " + path)
    print("Data: " + str(data))

    # Initialisiere Zähler
    start_time = time.time()  # Erfasse die Startzeit
    duration = 60  # Laufzeit von 1 Minute (60 Sekunden)
    total_calls = 0  # Verfolge die Gesamtanzahl der API-Aufrufe
    successful_calls = 0  # Verfolge die erfolgreichen API-Aufrufe

    # Schleife für 1 Minute
    while time.time() - start_time < duration:
        try:
            # Rufe die externe /bandwidth API auf
            response = requests.get('https://www.lzwjava.xyz/bandwidth')
            response.raise_for_status()  # Wirf eine Ausnahme bei HTTP-Fehlern
            successful_calls += 1  # Inkrementiere den Zähler für erfolgreiche Aufrufe
        except Exception as e:
            print("Fehler beim Abrufen der Bandbreitendaten:", e)
        finally:
            total_calls += 1  # Inkrementiere den Zähler für Gesamtaufrufe

        # Warte 5 Sekunden vor dem nächsten Aufruf
        time.sleep(5)

    # Protokolliere das Ende der Anfrage
    print("FC Invoke End RequestId: " + rid)

    # Gib die Anzahl der Aufrufe und erfolgreichen Aufrufe zurück
    return jsonify({
        "message": "Hello, World!",
        "total_calls": total_calls,
        "successful_calls": successful_calls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```