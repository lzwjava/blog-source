---
audio: true
generated: false
image: false
lang: fr
layout: post
title: Tester l'API Mistral
translated: true
type: post
---

Cet article est un test rapide de l'API Mistral. J'utilise le modèle `mistral-small-2501` pour ce test. Le code ci-dessous montre comment appeler l'API et obtenir une réponse.

```python
import os
import requests
from dotenv import load_dotenv
import argparse

load_dotenv()

def call_mistral_api(prompt, model="mistral-small-2501"):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Erreur: la variable d'environnement MISTRAL_API_KEY n'est pas définie.")
        return None

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(response_json)
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            return content
        else:
            print(f"Erreur de l'API Mistral: Format de réponse invalide: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur de l'API Mistral: {e}")
        if e.response:
            print(f"Code de statut de la réponse: {e.response.status_code}")
            print(f"Contenu de la réponse: {e.response.text}")
        return None

def call_codestral_api(prompt, model="codestral-latest"):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Erreur: la variable d'environnement MISTRAL_API_KEY n'est pas définie.")
        return None

    url = "https://api.mistral.ai/v1/fim/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "prompt": prompt,
        "suffix": "return a + b",
        "max_tokens": 64,
        "temperature": 0
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(response_json)
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            return content
        else:
            print(f"Erreur de l'API Codestral: Format de réponse invalide: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur de l'API Codestral: {e}")
        if e.response:
            print(f"Code de statut de la réponse: {e.response.status_code}")
            print(f"Contenu de la réponse: {e.response.text}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test des API Mistral et Codestral.")
    parser.add_argument("--type", type=str, default="mistral", choices=["mistral", "codestral"], help="Type d'API à appeler (mistral ou codestral)")
    args = parser.parse_args()

    if args.type == "mistral":
        prompt = "what's your cutting point of knowledge"
        response = call_mistral_api(prompt)
        if response:
            print(f"Réponse: {response}")
    elif args.type == "codestral":
        prompt = "def f("
        response = call_codestral_api(prompt, model="codestral-latest")
        if response:
            print(f"Réponse: {response}")
```