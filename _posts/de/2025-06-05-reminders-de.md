---
audio: true
generated: false
image: false
lang: de
layout: post
title: Streamline-Erinnerungen via Telegram
translated: true
type: post
---

In diesem Projekt habe ich ein automatisiertes Erinnerungssystem mit GitHub Actions und einem Telegram-Bot eingerichtet, um meine täglichen und monatlichen Aufgaben im Blick zu behalten. Mithilfe von Cron-Zeitplänen habe ich Erinnerungen für arbeitsbezogene Aufgaben wie das Einchecken in WeCom, das Einreichen von Stundenzetteln und das Überprüfen von Gehältern konfiguriert, sowie für persönliche Aufgaben wie den Besuch bei der Familie, Einkäufe auf JD.com und sogar das gemeinsame Fernsehen mit meinem Partner. Das System verwendet ein Python-Skript, um Nachrichten über die Telegram-Bot-API zu senden, wobei Umgebungsvariablen sicher in GitHub Secrets gespeichert sind. Dieser Aufbau stellt sicher, dass ich keine wichtigen Fristen oder persönlichen Verpflichtungen verpasse und verbindet Technologie mit dem Alltag für maximale Effizienz.

```yaml
name: Erinnerungen

on:
  schedule:
    # Läuft alle 2 Stunden von 12 bis 20 Uhr (Peking-Zeit, UTC+8) von Mittwoch bis Freitag.
    - cron: '0 4,6,8,10,12 * * 3-5'
    # Läuft am 27. jedes Monats um 12 Uhr (Peking-Zeit, UTC+8).
    - cron: '0 4 27 * *'
    # Läuft am 30. jedes Monats um 14 Uhr (Peking-Zeit, UTC+8).
    - cron: '0 6 30 * *'
    # Läuft täglich um 1 Uhr Peking-Zeit (17 Uhr UTC des Vortages).
    - cron: '0 17 * * *'
    # Läuft täglich um 11 Uhr Peking-Zeit (3 Uhr UTC).
    - cron: '0 3 * * *'
    # Erinnert am nächsten Tag die Eltern zu besuchen: 21 Uhr Peking-Zeit (13 Uhr UTC) Di, Mi, Do.
    - cron: '0 13 * * 2-4'
    # Erinnert am nächsten Tag nach Hause zu gehen: 21 Uhr Peking-Zeit (13 Uhr UTC) So, Mo, Fr, Sa.
    - cron: '0 13 * * 0,1,5,6'
    # Erinnert an den Einkauf von Frischwaren direkt bei JD.com: 21 Uhr Peking-Zeit (13 Uhr UTC) Mittwoch.
    - cron: '0 13 * * 3'
    # Erinnert an den Einkauf von Schnelllieferessen bei JD.com: 21 Uhr Peking-Zeit (13 Uhr UTC) Freitag.
    - cron: '0 13 * * 5'
    # Erinnert an die Prüfung für den Associate Degree im März, April, September und Oktober jeden Montag um 13 Uhr Peking-Zeit (5 Uhr UTC).
    - cron: '0 5 * 3,4,9,10 1'
    # Erinnert wöchentlich an das Einreichen des Stundenzettels jeden Freitag um 17 Uhr Taipeh-Zeit (9 Uhr UTC).
    - cron: '0 9 * * 5'
    # Erinnert monatlich an das Einreichen des Lieferanten-Stundenzettels am 25. um 0 Uhr Taipeh-Zeit (16 Uhr UTC des Vortages).
    - cron: '0 16 25 * *'
    # Erinnert monatlich am 16. um 21 Uhr Taipeh-Zeit (13 Uhr UTC) die Familie um Unterstützung der Hypothekenzahlung zu bitten.
    - cron: '0 13 16 * *'
    # Erinnert jeden Freitag, Samstag und Sonntag um 22 Uhr Taipeh-Zeit (14 Uhr UTC) an das gemeinsame Fernsehen mit dem Partner.
    - cron: '0 14 * * 5,6,0'
    # Erinnert an das Entfernen des Parkausweises um 2 Uhr Peking-Zeit (18 Uhr UTC) Mi, Do, Fr.
    - cron: '0 18 * * 3,4,5'
  workflow_dispatch:  # Ermöglicht manuelle Auslösung

concurrency:
  group: 'erinnerungen'
  cancel-in-progress: false

jobs:
  send-reminders:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_BOT2_API_KEY: ${{ secrets.TELEGRAM_BOT2_API_KEY }}

    steps:
      - name: Repository auschecken
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Python 3.10.x einrichten
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: Abhängigkeiten installieren
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: Telegram-Skript für tägliche Eincheck-Erinnerungen ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "In WeCom einchecken"
        if: github.event.schedule == '0 4,6,8,10,12 * * 3-5'

      - name: Telegram-Skript für monatliche Hypotheken-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Hypothekenabzug vorbereiten"
        if: github.event.schedule == '0 4 27 * *'

      - name: Telegram-Skript für monatliche Gehaltsüberprüfung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Gehalt überprüfen"
        if: github.event.schedule == '0 6 30 * *'

      - name: Telegram-Skript für Schlaf-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Zeit zum Schlafen!"
        if: github.event.schedule == '0 17 * * *'

      - name: Telegram-Skript für Aufwach-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Zeit zum Aufwachen!"
        if: github.event.schedule == '0 3 * * *'

      - name: Telegram-Skript für Elternhaus-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Morgen zu den Eltern gehen!"
        if: github.event.schedule == '0 13 * * 2-4'

      - name: Telegram-Skript für eigenes Haus-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Morgen nach Hause gehen!"
        if: github.event.schedule == '0 13 * * 0,1,5,6'

      - name: Telegram-Skript für JD.com-Frischwaren-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Frischwaren direkt bei JD.com kaufen!"
        if: github.event.schedule == '0 13 * * 3'

      - name: Telegram-Skript für JD.com-Schnelllieferessen-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Schnelllieferessen bei JD.com kaufen!"
        if: github.event.schedule == '0 13 * * 5'

      - name: Telegram-Skript für Associate-Degree-Prüfungs-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Für Associate-Degree-Prüfung anmelden"
        if: github.event.schedule == '0 5 * 3,4,9,10 1'

      - name: Telegram-Skript für wöchentliche Stundenzettel-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Wöchentlichen Stundenzettel einreichen"
        if: github.event.schedule == '0 9 * * 5'

      - name: Telegram-Skript für Lieferanten-Stundenzettel-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Lieferanten-Stundenzettel einreichen"
        if: github.event.schedule == '0 16 25 * *'

      - name: Telegram-Skript für Hypotheken-Unterstützungs-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Familie um Hypothekenunterstützung bitten"
        if: github.event.schedule == '0 13 16 * *'

      - name: Telegram-Skript für TV-Erinnerung mit Partner ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Zeit, mit deinem Partner fernzusehen!"
        if: github.event.schedule == '0 14 * * 5,6,0'

      - name: Telegram-Skript für Parkausweis-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Parkausweis vom Autofenster entfernen"
        if: github.event.schedule == '0 18 * * 3,4,5'

      - name: Telegram-Skript für Testnachricht ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Dies ist eine Testnachricht von GitHub Actions."
        if: github.event_name == 'workflow_dispatch'
```

```python
import os
import requests
from dotenv import load_dotenv
import json
import argparse

load_dotenv()

TELEGRAM_BOT2_API_KEY = os.environ.get("TELEGRAM_BOT2_API_KEY")
TELEGRAM_CHAT_ID = "610574272"

def send_telegram_message(bot_token, chat_id, message):
    """Sendet eine Nachricht an einen Telegram-Chat über die Telegram-Bot-API."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Fehler beim Senden der Telegram-Nachricht: {response.status_code} - {response.text}")

def get_chat_id(bot_token):
    """Ermittelt die Chat-ID der letzten an den Bot gesendeten Nachricht."""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    if response.status_code == 200:
        updates = response.json()
        print(json.dumps(updates, indent=4))
        if updates['result']:
            chat_id = updates['result'][-1]['message']['chat']['id']
            return chat_id
    return None

def send_reminder(message):
    """Sendet eine Erinnerungsnachricht an Telegram."""
    if TELEGRAM_BOT2_API_KEY and TELEGRAM_CHAT_ID:
        send_telegram_message(TELEGRAM_BOT2_API_KEY, TELEGRAM_CHAT_ID, f"Erinnerung: {message}")
    else:
        print("TELEGRAM_BOT2_API_KEY und TELEGRAM_CHAT_ID sind nicht gesetzt.")

def main():
    parser = argparse.ArgumentParser(description="Telegram-Bot-Skript")
    parser.add_argument('--job', choices=['get_chat_id', 'send_message'], required=True, help="Auszuführende Aufgabe")
    parser.add_argument('--message', help="Benutzerdefinierte Nachricht zum Senden", default=None)
    args = parser.parse_args()

    if args.job == 'get_chat_id':
        bot_token = TELEGRAM_BOT2_API_KEY
        chat_id = get_chat_id(bot_token)
        if chat_id:
            print(f"Chat-ID: {chat_id}")
        else:
            print("Chat-ID konnte nicht ermittelt werden.")

    elif args.job == 'send_message':
        if args.message:
            send_reminder(args.message)
        else:
            print("Keine Nachricht für die Aufgabe 'send_message' angegeben.")
            
if __name__ == '__main__':
    main()
```