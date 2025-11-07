---
audio: false
generated: false
image: false
lang: de
layout: post
title: Function Compute auf Alibaba Cloud
translated: true
type: post
---

Ich verwende Alibaba Cloud's Function Compute, um normal aussehenden Traffic zu generieren, was dabei hilft, die Aktivität meines Proxy-Servers vor der GFW zu verschleiern. Ich habe einen Bandbreiten-Server neben meinem Proxy bereitgestellt, und diese Function Compute-Funktion sendet jede Minute eine Anfrage an die Bandbreiten-API. Dadurch entsteht eine Mischung aus normalem und Proxy-Traffic.

```python
from flask import Flask, request, jsonify
import requests
import concurrent.futures

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

# Funktion zum Aufrufen der externen API
def call_bandwidth_api():
    try:
        response = requests.get('https://www.lzwjava.xyz/bandwidth')
        response.raise_for_status()  # Wirft eine Ausnahme bei HTTP-Fehlern
        return True  # Gibt Erfolg an
    except Exception as e:
        print("Fehler beim Abrufen der Bandbreitendaten:", e)
        return False  # Gibt Fehler an

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # Protokolliert die Request-ID und andere Details
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    data = request.stream.read()
    print("Pfad: " + path)
    print("Daten: " + str(data))

    # Initialisiert Zähler
    total_calls = 10  # Gesamtzahl der API-Aufrufe
    successful_calls = 0  # Zählt erfolgreiche API-Aufrufe

    # Verwendet ThreadPoolExecutor, um die API 10 Mal parallel aufzurufen
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Sendet Aufgaben an den Executor
        futures = [executor.submit(call_bandwidth_api) for _ in range(total_calls)]

        # Wartet auf den Abschluss aller Aufgaben und zählt die Erfolge
        for future in concurrent.futures.as_completed(futures):
            if future.result():  # Wenn der Aufruf erfolgreich war
                successful_calls += 1

    # Protokolliert das Ende der Anfrage
    print("FC Invoke End RequestId: " + rid)

    # Gibt die Anzahl der Aufrufe und erfolgreichen Aufrufe zurück
    return jsonify({
        "message": "Hello, World!",
        "total_calls": total_calls,
        "successful_calls": successful_calls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```