---
audio: false
generated: false
image: false
lang: de
layout: post
title: Einen Gewohnheitsbot mit Mistral bauen
translated: true
---

In diesem Blogbeitrag untersuchen wir die Erstellung eines Habit Bots, der automatisierte Erinnerungen mit Python und GitHub Actions versendet. Dieser Bot nutzt die Telegram API für Nachrichten und integriert Mistral AI, um kontextbezogene Aufforderungen zu generieren. Durch die Planung von Aufgaben mit GitHub Actions fördert der Bot konsequente Gewohnheiten durch zeitnahe Benachrichtigungen. Wir gehen Schritt für Schritt durch die Einrichtung, von der Konfiguration der Umgebung über das Skripting bis zur Bereitstellung, und bieten eine praktische Anleitung zur Automatisierung Ihres Gewohnheitstrackingsystems.

## Code

```python
import os
import requests
import argparse
import re
import datetime
from dotenv import load_dotenv
import random

# Lade Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Umgebungsvariablen
TELEGRAM_HABIT_BOT_API_KEY = os.environ.get("TELEGRAM_HABIT_BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

# Maximale Nachrichtenlänge für Telegram
TELEGRAM_MAX_LENGTH = 4096

def send_telegram_message(bot_token, chat_id, message):
    """Sendet eine Nachricht an einen Telegram-Chat über die Telegram Bot API."""
    if not bot_token or not chat_id:
        print("Fehler: TELEGRAM_HABIT_BOT_API_KEY oder TELEGRAM_CHAT_ID nicht gesetzt.")
        return False
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # Entferne Markdown-Sternchen und URLs für Telegram-Kompatibilität
    message_no_stars = message.replace('*', '')
    url_pattern = re.compile(r'(https?://[^\s]+)')
    message_no_links = url_pattern.sub('', message_no_stars)
    # Teile die Nachricht, falls sie die maximale Länge von Telegram überschreitet
    messages = []
    msg = message_no_links
    while len(msg) > TELEGRAM_MAX_LENGTH:
        split_idx = msg.rfind('\n', 0, TELEGRAM_MAX_LENGTH)
        if split_idx == -1 or split_idx < TELEGRAM_MAX_LENGTH // 2:
            split_idx = TELEGRAM_MAX_LENGTH
        messages.append(msg[:split_idx])
        msg = msg[split_idx:]
    messages.append(msg)
    success = True
    for part in messages:
        params = {
            "chat_id": chat_id,
            "text": part,
            "parse_mode": "Markdown"
        }
        try:
            response = requests.post(url, params=params)
            response.raise_for_status()
            print(f"Telegram-Nachrichtenteil erfolgreich gesendet ({len(part)} Zeichen).")
        except requests.exceptions.RequestException as e:
            print(f"Fehler beim Senden der Telegram-Nachricht: {e}")
            success = False
    return success


def call_mistral_api(prompt, model="mistral-large-latest"):
    """Ruft die Mistral API auf, um eine Antwort zu generieren."""
    if not MISTRAL_API_KEY:
        print("Fehler: MISTRAL_API_KEY Umgebungsvariable nicht gesetzt.")
        return None
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
    }
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,  # Passe die Temperatur für Kreativität an
        "max_tokens": 300  # Begrenze die Antwortlänge
    }
    try:
        print(f"Rufe Mistral API mit Modell auf: {model}")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral API Inhalt: {content}")
            return content
        print(f"Mistral API Fehler: Ungültiges Antwortformat: {response_json}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API Fehler: {e}")
        return None

def generate_copilot_message():
    """Generiert einen technischen Aufforderungssatz zur Nutzung von Copilot über die Mistral API."""
    prompt = (
        f"Generiere einen einzigartigen, spezifischen technischen Aufforderungssatz für einen Backend-Engineer."
        "Wähle zufällig eine Technologie aus: Java, Spring Boot, Control-M, IBM WebSphere, Maven, Multithreading, Nexus, Windows, JVM, Service-NOW, Python, AI oder DevOps, Linux. Algorithmen und Banking. "
        "Formatiere als 'Stecken Sie bei [spezifische Herausforderung] fest? Fragen Sie Copilot!' oder 'Probleme mit [Aufgabe]? Lassen Sie sich von Copilot helfen!' "
        "Sorge für Abwechslung bei den Herausforderungen (z.B. Konfiguration, Debugging, Optimierung). "
        "Halte es unter 300 Zeichen, vermeide Markdown oder URLs und gib nur den Satz aus."
    )
    message = call_mistral_api(prompt)
    if message:
        return message.strip()[:300]
    return "Stecken Sie bei der Konfiguration des Control-M Auftragsdatums fest? Fragen Sie Copilot!"

def main():
    parser = argparse.ArgumentParser(description="Telegram Habit Reminder Bot")
    parser.add_argument("--job", choices=["send_reminder", "send_message"], required=True, help="Ausführender Job")
    parser.add_argument("--message", type=str, help="Nachricht für 'send_message' Job")
    args = parser.parse_args()

    if args.job == "send_reminder":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = generate_copilot_message()
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("Fehler: TELEGRAM_HABIT_BOT_API_KEY oder TELEGRAM_CHAT_ID nicht gesetzt.")
    elif args.job == "send_message":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "Standard-Testnachricht vom Bot!"
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("Fehler: TELEGRAM_HABIT_BOT_API_KEY oder TELEGRAM_CHAT_ID nicht gesetzt.")

if __name__ == "__main__":
    main()
```

## GitHub Action

```yaml
name: Habit

on:
  schedule:
    # Führt alle 10 Minuten (0, 10, 20, 30, 40, 50 Minuten nach der vollen Stunde) von 05:00–13:00 UTC, Mo–Fr aus
    # 05:00–13:00 UTC = 13:00–21:00 Pekinger Zeit (UTC+8)
    - cron: '0,10,20,30,40,50 5-13 * * 1-5'

  workflow_dispatch:
    # Erlaubt manuelle Auslösung für Tests
    inputs:
      message:
        description: 'Benutzerdefinierte Nachricht für Tests (optional)'
        required: false
        default: 'Testnachricht von GitHub Actions.'
      job:
        description: 'Auszuführender Job (optional)'
        required: false
        default: 'send_message'

  push:
    branches: ["main"]
    paths:
      - 'scripts/bot/habit_bot.py'
      - '.github/workflows/habit_reminder.yml'

concurrency:
  group: 'habit_reminder'
  cancel-in-progress: false

jobs:
  habit_reminder_job:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_HABIT_BOT_API_KEY: ${{ secrets.TELEGRAM_HABIT_BOT_API_KEY }}
      TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
      MISTRAL_API_KEY: ${{ secrets.MISTRAL_API_KEY }}

    steps:
      - name: Repository auschecken
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Python 3.13 einrichten
        uses: actions/setup-python@v4
        with:
          python-version: "3.13"

      - name: Abhängigkeiten installieren
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Habit Reminder Skript ausführen (Geplant)
        run: python scripts/bot/habit_bot.py --job send_reminder
        if: github.event_name == 'schedule'

      - name: Habit Reminder Skript ausführen (Manuell)
        run: python scripts/bot/habit_bot.py --job ${{ github.event.inputs.job }} --message "${{ github.event.inputs.message }}"
        if: github.event_name == 'workflow_dispatch'

      - name: Bei Push auf main-Branch benachrichtigen
        run: python scripts/bot/habit_bot.py --job send_message --message "Codeänderungen für den Habit Bot wurden in den main-Branch gepusht."
        if: github.event_name == 'push'

```