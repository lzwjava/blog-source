---
audio: false
generated: true
lang: fr
layout: post
title: Function Compute sur Alibaba Cloud
translated: true
---

J'utilise le service Function Compute d'Alibaba Cloud pour générer un trafic qui semble normal, ce qui aide à masquer l'activité de mon serveur proxy face au GFW. J'ai déployé un serveur de bande passante à côté de mon proxy, et cette fonction Function Compute effectue une requête à l'API de bande passante toutes les minutes. Cela crée un mélange de trafic normal et de trafic proxy.

```python
from flask import Flask, request, jsonify
import requests
import concurrent.futures

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

# Fonction pour appeler l'API externe
def call_bandwidth_api():
    try:
        response = requests.get('https://www.lzwjava.xyz/bandwidth')
        response.raise_for_status()  # Lève une exception en cas d'erreur HTTP
        return True  # Indique un succès
    except Exception as e:
        print("Erreur lors de la récupération des données de bande passante:", e)
        return False  # Indique un échec

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # Log de l'ID de la requête et d'autres détails
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    data = request.stream.read()
    print("Path: " + path)
    print("Data: " + str(data))

    # Initialisation des compteurs
    total_calls = 10  # Nombre total d'appels API à effectuer
    successful_calls = 0  # Suivi des appels API réussis

    # Utilisation de ThreadPoolExecutor pour appeler l'API 10 fois en parallèle
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Soumission des tâches à l'exécuteur
        futures = [executor.submit(call_bandwidth_api) for _ in range(total_calls)]

        # Attente de la fin de toutes les tâches et comptage des succès
        for future in concurrent.futures.as_completed(futures):
            if future.result():  # Si l'appel a réussi
                successful_calls += 1

    # Log de la fin de la requête
    print("FC Invoke End RequestId: " + rid)

    # Retour du nombre d'appels et des appels réussis
    return jsonify({
        "message": "Hello, World!",
        "total_calls": total_calls,
        "successful_calls": successful_calls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```