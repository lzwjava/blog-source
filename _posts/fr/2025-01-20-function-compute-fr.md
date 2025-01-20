---
audio: true
lang: fr
layout: post
title: Function Compute sur Alibaba Cloud
translated: true
---

J'ai configuré une fonction en utilisant le service Function Compute d'Alibaba Cloud. Mon objectif est de générer un trafic qui semble normal pour aider à masquer l'activité de mon serveur proxy face au GFW. Pour ce faire, j'ai déployé un serveur de bande passante à côté de mon proxy. Maintenant, j'utilise le service Function Compute d'Alibaba Cloud pour effectuer une requête à cette API de bande passante toutes les minutes, créant ainsi un mélange de trafic normal et de trafic proxy.

```python
from flask import Flask, request, jsonify
import requests
import time

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # Enregistrer l'ID de la requête et d'autres détails
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    data = request.stream.read()
    print("Path: " + path)
    print("Data: " + str(data))

    # Initialiser les compteurs
    start_time = time.time()  # Enregistrer l'heure de début
    duration = 60  # Exécuter pendant 1 minute (60 secondes)
    total_calls = 0  # Suivre le nombre total d'appels API
    successful_calls = 0  # Suivre le nombre d'appels API réussis

    # Boucle pendant 1 minute
    while time.time() - start_time < duration:
        try:
            # Appeler l'API externe /bandwidth
            response = requests.get('https://www.lzwjava.xyz/bandwidth')
            response.raise_for_status()  # Lever une exception pour les erreurs HTTP
            successful_calls += 1  # Incrémenter le compteur d'appels réussis
        except Exception as e:
            print("Erreur lors de la récupération des données de bande passante:", e)
        finally:
            total_calls += 1  # Incrémenter le compteur total d'appels

        # Attendre 5 secondes avant la prochaine requête
        time.sleep(5)

    # Enregistrer la fin de la requête
    print("FC Invoke End RequestId: " + rid)

    # Retourner le nombre d'appels et d'appels réussis
    return jsonify({
        "message": "Hello, World!",
        "total_calls": total_calls,
        "successful_calls": successful_calls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```