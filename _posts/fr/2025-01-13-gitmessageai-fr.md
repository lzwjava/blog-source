---
audio: false
generated: false
lang: fr
layout: post
title: Messages de Commit Alimentés par l'IA
translated: true
---

Ce script Python doit être placé dans un répertoire inclus dans le PATH de votre système, tel que `~/bin`.

```python
import subprocess
import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse
import requests

load_dotenv()

def call_mistral_api(prompt):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Erreur : La variable d'environnement MISTRAL_API_KEY n'est pas définie.")
        return None

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "mistral-large-latest",
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
        if response_json and response_json['choices']:
            return response_json['choices'][0]['message']['content']
        else:
            print(f"Erreur de l'API Mistral : Format de réponse invalide : {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur de l'API Mistral : {e}")
        if e.response:
            print(f"Code de statut de la réponse : {e.response.status_code}")
            print(f"Contenu de la réponse : {e.response.text}")
        return None

def call_gemini_api(prompt):
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("Erreur : La variable d'environnement GEMINI_API_KEY n'est pas définie.")
        return None
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    params = {"key": gemini_api_key}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, json=payload, params=params)
        response.raise_for_status()  # Lève une exception pour les codes de statut mauvais
        response_json = response.json()
        if response_json and 'candidates' in response_json and response_json['candidates']:
            return response_json['candidates'][0]['content']['parts'][0]['text']
        else:
            print(f"Erreur de l'API Gemini : Format de réponse invalide : {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur de l'API Gemini : {e}")
        if e.response:
            print(f"Code de statut de la réponse : {e.response.status_code}")
            print(f"Contenu de la réponse : {e.response.text}")
        return None

def call_deepseek_api(prompt):
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("Erreur : La variable d'environnement DEEPSEEK_API_KEY n'est pas définie.")
        return None

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        if response and response.choices:
            commit_message = response.choices[0].message.content.strip()
            commit_message = commit_message.replace('`', '')
            return commit_message
        else:
            print("Erreur : Aucune réponse de l'API.")
            return None
    except Exception as e:
        print(f"Erreur pendant l'appel de l'API : {e}")
        print(e)
        return None

def gitmessageai(push=True, only_message=False, api='deepseek'):
    # Valider tous les changements
    subprocess.run(["git", "add", "-A"], check=True)

    # Obtenir un résumé bref des changements
    files_process = subprocess.run(["git", "diff", "--staged", "--name-only"], capture_output=True, text=True, check=True)
    changed_files = files_process.stdout

    if not changed_files:
        print("Aucun changement à valider.")
        return

    # Préparer l'invite pour l'IA
    prompt = f"""
Générer un message de validation concis au format Conventional Commits pour les changements de code suivants.
Utilisez l'un des types suivants : feat, fix, docs, style, refactor, test, chore, perf, ci, build, ou revert.
Si applicable, incluez une portée entre parenthèses pour décrire la partie de la base de code affectée.
Le message de validation ne doit pas dépasser 70 caractères.

Fichiers modifiés :
{changed_files}

Message de validation :
"""

    if api == 'deepseek':
        commit_message = call_deepseek_api(prompt)
        if not commit_message:
            return
    elif api == 'gemini':
        commit_message = call_gemini_api(prompt)
        if not commit_message:
            print("Erreur : Aucune réponse de l'API Gemini.")
            return
    elif api == 'mistral':
        commit_message = call_mistral_api(prompt)
        if not commit_message:
            print("Erreur : Aucune réponse de l'API Mistral.")
            return
    else:
        print(f"Erreur : API invalide spécifiée : {api}")
        return

    # Vérifier si le message de validation est vide
    if not commit_message:
        print("Erreur : Message de validation vide généré. Annulation de la validation.")
        return

    if only_message:
        print(f"Message de validation suggéré : {commit_message}")
        return

    # Valider avec le message généré
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Envoyer les changements
    if push:
        subprocess.run(["git", "push"], check=True)
    else:
        print("Changements validés localement, mais non envoyés.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générer un message de validation avec l'IA et valider les changements.")
    parser.add_argument('--no-push', dest='push', action='store_false', help='Valider les changements localement sans les envoyer.')
    parser.add_argument('--only-message', dest='only_message', action='store_true', help='Imprimer uniquement le message de validation généré par l\'IA.')
    parser.add_argument('--api', type=str, default='deepseek', choices=['deepseek', 'gemini', 'mistral'], help='API à utiliser pour la génération du message de validation (deepseek, gemini, ou mistral).')
    args = parser.parse_args()
    gitmessageai(push=args.push, only_message=args.only_message, api=args.api)
```

Ce script peut être appelé avec différentes API. Par exemple :

```bash
python ~/bin/gitmessageai.py
python ~/bin/gitmessageai.py --no-push
python ~/bin/gitmessageai.py --only-message
python ~/bin/gitmessageai.py --api gemini
python ~/bin/gitmessageai.py --api mistral --no-push
python ~/bin/gitmessageai.py --api deepseek --only-message
```

Ensuite, dans votre fichier `~/.zprofile`, ajoutez ce qui suit :

```bash
alias gpa='python ~/bin/gitmessageai.py'
alias gca='python ~/bin/gitmessageai.py --no-push'
alias gm='python ~/bin/gitmessageai.py --only-message'
```

Il y a plusieurs améliorations.

* L'une consiste à n'envoyer que les changements de noms de fichiers, et à ne pas lire les changements détaillés du fichier en utilisant `git diff`. Nous ne voulons pas donner trop de détails à l'API du service IA. Dans ce cas, nous n'en avons pas besoin, car peu de personnes liront attentivement les messages de validation.

* Parfois, l'API Deepseek échoue, car elle est très populaire récemment. Nous pourrions avoir besoin d'utiliser Gemini à la place.