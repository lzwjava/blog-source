---
audio: false
generated: false
image: false
lang: de
layout: post
title: KI-gestützte Git-Commit-Nachrichten
translated: true
---

Dieses Python-Skript sollte in einem Verzeichnis platziert werden, das im PATH Ihres Systems enthalten ist, wie z.B. `~/bin`.

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
        print("Fehler: MISTRAL_API_KEY Umgebungsvariable nicht gesetzt.")
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
            print(f"Mistral API Fehler: Ungültiges Antwortformat: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API Fehler: {e}")
        if e.response:
            print(f"Antwortstatuscode: {e.response.status_code}")
            print(f"Antwortinhalt: {e.response.text}")
        return None

def call_gemini_api(prompt):
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("Fehler: GEMINI_API_KEY Umgebungsvariable nicht gesetzt.")
        return None
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    params = {"key": gemini_api_key}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, json=payload, params=params)
        response.raise_for_status()  # Ausnahme für schlechte Statuscodes auslösen
        response_json = response.json()
        if response_json and 'candidates' in response_json and response_json['candidates']:
            return response_json['candidates'][0]['content']['parts'][0]['text']
        else:
            print(f"Gemini API Fehler: Ungültiges Antwortformat: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Gemini API Fehler: {e}")
        if e.response:
            print(f"Antwortstatuscode: {e.response.status_code}")
            print(f"Antwortinhalt: {e.response.text}")
        return None

def call_deepseek_api(prompt):
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("Fehler: DEEPSEEK_API_KEY Umgebungsvariable nicht gesetzt.")
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
            print("Fehler: Keine Antwort von der API.")
            return None
    except Exception as e:
        print(f"Fehler während des API-Aufrufs: {e}")
        print(e)
        return None

def gitmessageai(push=True, only_message=False, api='deepseek'):
    # Alle Änderungen stagen
    subprocess.run(["git", "add", "-A"], check=True)

    # Eine kurze Zusammenfassung der Änderungen abrufen
    files_process = subprocess.run(["git", "diff", "--staged", "--name-only"], capture_output=True, text=True, check=True)
    changed_files = files_process.stdout

    if not changed_files:
        print("Keine Änderungen zum Commit.")
        return

    # Das Prompt für die KI vorbereiten
    prompt = f"""
Erstelle eine prägnante Commit-Nachricht im Conventional Commits Format für die folgenden Codeänderungen.
Verwende einen der folgenden Typen: feat, fix, docs, style, refactor, test, chore, perf, ci, build, oder revert.
Falls zutreffend, füge einen Bereich in Klammern hinzu, um den betroffenen Teil der Codebasis zu beschreiben.
Die Commit-Nachricht sollte 70 Zeichen nicht überschreiten.

Geänderte Dateien:
{changed_files}

Commit-Nachricht:
"""

    if api == 'deepseek':
        commit_message = call_deepseek_api(prompt)
        if not commit_message:
            return
    elif api == 'gemini':
        commit_message = call_gemini_api(prompt)
        if not commit_message:
            print("Fehler: Keine Antwort von der Gemini API.")
            return
    elif api == 'mistral':
        commit_message = call_mistral_api(prompt)
        if not commit_message:
            print("Fehler: Keine Antwort von der Mistral API.")
            return
    else:
        print(f"Fehler: Ungültige API angegeben: {api}")
        return

    # Überprüfen, ob die Commit-Nachricht leer ist
    if not commit_message:
        print("Fehler: Leere Commit-Nachricht generiert. Commit abgebrochen.")
        return

    if only_message:
        print(f"Vorgeschlagene Commit-Nachricht: {commit_message}")
        return

    # Mit der generierten Nachricht committen
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Die Änderungen pushen
    if push:
        subprocess.run(["git", "push"], check=True)
    else:
        print("Änderungen lokal committet, aber nicht gepusht.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Commit-Nachricht mit KI generieren und Änderungen committen.")
    parser.add_argument('--no-push', dest='push', action='store_false', help='Änderungen lokal committen ohne zu pushen.')
    parser.add_argument('--only-message', dest='only_message', action='store_true', help='Nur die von der KI generierte Commit-Nachricht ausgeben.')
    parser.add_argument('--api', type=str, default='deepseek', choices=['deepseek', 'gemini', 'mistral'], help='API zur Generierung der Commit-Nachricht verwenden (deepseek, gemini oder mistral).')
    args = parser.parse_args()
    gitmessageai(push=args.push, only_message=args.only_message, api=args.api)
```

Dieses Skript kann mit verschiedenen APIs aufgerufen werden. Beispiel:

```bash
python ~/bin/gitmessageai.py
python ~/bin/gitmessageai.py --no-push
python ~/bin/gitmessageai.py --only-message
python ~/bin/gitmessageai.py --api gemini
python ~/bin/gitmessageai.py --api mistral --no-push
python ~/bin/gitmessageai.py --api deepseek --only-message
```

Dann fügen Sie in Ihrer `~/.zprofile` Datei folgendes hinzu:

```bash
alias gpa='python ~/bin/gitmessageai.py'
alias gca='python ~/bin/gitmessageai.py --no-push'
alias gm='python ~/bin/gitmessageai.py --only-message'
```

Es gibt mehrere Verbesserungen.

* Eine besteht darin, nur Dateinamenänderungen zu senden und nicht die detaillierten Änderungen der Dateien mit `git diff` zu lesen. Wir möchten dem API-Dienst der KI nicht zu viele Details geben. In diesem Fall benötigen wir es nicht, da nur wenige Personen Commit-Nachrichten sorgfältig lesen.

* Manchmal schlägt der Aufruf der Deepseek-API fehl, da sie in letzter Zeit sehr beliebt ist. Wir müssen möglicherweise Gemini stattdessen verwenden.