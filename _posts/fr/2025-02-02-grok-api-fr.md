---
audio: true
generated: false
image: false
lang: fr
layout: post
title: Tester l'API de Grok
translated: true
type: post
---

- Il est ok d'utiliser une carte Visa émise par la Chine.

- [https://console.x.ai](https://console.x.ai)

- `grok-2-latest` modèle: Entrée 2 USD par million de jetons, Sortie 10 USD par million de jetons.

Code:

```python
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.environ.get("GROK_API_KEY")
if not GROK_API_KEY:
    raise ValueError("GROK_API_KEY environment variable not set")

url = "https://api.x.ai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {GROK_API_KEY}"
}
data = {
    "model": "grok-2-latest",
    "messages": [
        {
            "role": "user",
            "content": "Explain how AI works"
        }
    ]
}

try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    json_response = response.json()
    if 'choices' in json_response and json_response['choices']:
        first_choice = json_response['choices'][0]
        if 'message' in first_choice and 'content' in first_choice['message']:
            print(first_choice['message']['content'])
        else:
            print("Format de réponse inattendu: message ou contenu manquant")
    else:
        print("Aucun choix trouvé dans la réponse")
except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requête API: {e}")
    if e.response:
        print(f"Code de statut de la réponse: {e.response.status_code}")
        print(f"Contenu de la réponse: {e.response.text}")
except json.JSONDecodeError as e:
    print(f"Erreur lors du décodage de la réponse JSON: {e}")
```