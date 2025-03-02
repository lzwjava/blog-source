---
audio: true
generated: true
lang: es
layout: post
title: Prueba de la API de Grok
translated: true
---

- Está bien usar una tarjeta de Visa emitida por China.

- [https://console.x.ai](https://console.x.ai)

- `grok-2-latest` modelo: Entrada 2 USD por millón de tokens, Salida 10 USD por millón de tokens.

Código:

```python
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.environ.get("GROK_API_KEY")
if not GROK_API_KEY:
    raise ValueError("GROK_API_KEY variable de entorno no está configurada")

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
            "content": "Explicar cómo funciona la IA"
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
            print("Formato de respuesta inesperado: falta mensaje o contenido")
    else:
        print("No se encontraron opciones en la respuesta")
except requests.exceptions.RequestException as e:
    print(f"Error durante la solicitud de API: {e}")
    if e.response:
        print(f"Código de estado de la respuesta: {e.response.status_code}")
        print(f"Contenido de la respuesta: {e.response.text}")
except json.JSONDecodeError as e:
    print(f"Error al decodificar la respuesta JSON: {e}")
```