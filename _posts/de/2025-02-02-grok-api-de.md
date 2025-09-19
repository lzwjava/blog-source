---
audio: true
generated: false
image: false
lang: de
layout: post
title: Testen Sie die Grok API
translated: true
---

- Es ist in Ordnung, eine von China ausgestellte Visa-Karte zu verwenden.

- [https://console.x.ai](https://console.x.ai)

- `grok-2-latest` Modell: Eingabe 2 USD pro Million Tokens, Ausgabe 10 USD pro Million Tokens.

Code:

```python
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.environ.get("GROK_API_KEY")
if not GROK_API_KEY:
    raise ValueError("GROK_API_KEY-Umgebungsvariable nicht gesetzt")

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
            "content": "Erkläre, wie KI funktioniert"
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
            print("Unerwartetes Antwortformat: Nachricht oder Inhalt fehlt")
    else:
        print("Keine Auswahlmöglichkeiten in der Antwort gefunden")
except requests.exceptions.RequestException as e:
    print(f"Fehler bei der API-Anfrage: {e}")
    if e.response:
        print(f"Antwortstatuscode: {e.response.status_code}")
        print(f"Antwortinhalt: {e.response.text}")
except json.JSONDecodeError as e:
    print(f"Fehler beim Dekodieren der JSON-Antwort: {e}")
```