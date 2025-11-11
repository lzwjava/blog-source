---
audio: false
generated: true
lang: de
layout: post
title: Lochkarten-Erinnerungen mit Supabase
translated: true
type: note
---

Ich helfe Ihnen dabei, den vorhandenen GitHub Actions-Workflow und das Python-Skript zu modifizieren, um Stempelzeiterinnerungen von Mittwoch bis Freitag zu implementieren, mit Erinnerungen alle 5 Minuten während 12–15 Uhr (Stempeln zum Arbeitsbeginn) und 18–21 Uhr (Stempeln zum Arbeitsende) SGT, die stoppen, wenn eine "punch"-Nachricht via Telegram empfangen wird. Wir werden Supabase verwenden, um Stempelstatus zu verfolgen und redundante Erinnerungen zu vermeiden.

Unten finden Sie die vollständigen Anleitungen und den Code:

---

### GitHub Actions Workflow
Der Workflow muss alle 5 Minuten während der angegebenen Zeitfenster in SGT (UTC+8) laufen:
- Stempeln zum Arbeitsbeginn: 12–15 Uhr SGT = 4–7 Uhr UTC
- Stempeln zum Arbeitsende: 18–21 Uhr SGT = 10–13 Uhr UTC
- Tage: Mittwoch bis Freitag (3-5 in Cron-Syntax)

Wir verwenden einen einzelnen Cron-Zeitplan, der diese Stunden kombiniert, und lassen das Skript die Aktion bestimmen.

```yaml
name: Stempelzeiterinnerungen

on:
  schedule:
    # Läuft alle 5 Minuten von 4-7 Uhr und 10-13 Uhr UTC, Mi-Fr
    # 4-7 Uhr UTC = 12-15 Uhr SGT, 10-13 Uhr UTC = 18-21 Uhr SGT
    - cron: '*/5 4-7,10-13 * * 3-5'

  workflow_dispatch:
    inputs:
      job_name:
        description: 'Job to run (punch_reminder, send_message)'
        required: true
        default: 'punch_reminder'
      message:
        description: 'Custom message for send_message job (optional)'
        required: false
        default: 'This is a manual trigger test message from GitHub Actions.'

  push:
    branches: ["main"]
    paths:
      - 'scripts/release/location_bot.py'
      - '.github/workflows/location.yml'

concurrency:
  group: 'punch_reminder'
  cancel-in-progress: false

jobs:
  punch_reminder_job:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_LOCATION_BOT_API_KEY: ${{ secrets.TELEGRAM_LOCATION_BOT_API_KEY }}
      SUPABASE_URL: ${{ secrets.SUPABASE_URL }}
      SUPABASE_KEY: ${{ secrets.SUPABASE_KEY }}

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
      with:
        fetch-depth: 5

    - name: Set up Python 3.13.2
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2"

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.simple.txt

    - name: Run punch reminder script (Scheduled)
      run: python scripts/release/location_bot.py --job punch_reminder
      if: github.event_name == 'schedule'

    - name: Run punch reminder script (Manual Trigger)
      run: python scripts/release/location_bot.py --job punch_reminder
      if: github.event_name == 'workflow_dispatch' && github.event.inputs.job_name == 'punch_reminder'

    - name: Run Telegram script for custom message (Manual Trigger)
      run: python scripts/release/location_bot.py --job send_message --message "${{ github.event.inputs.message }}"
      if: github.event_name == 'workflow_dispatch' && github.event.inputs.job_name == 'send_message'

    - name: Notify on push to main branch
      run: python scripts/release/location_bot.py --job send_message --message "Code changes for punch reminder bot pushed to main branch."
      if: github.event_name == 'push'
```

---

### Python-Skript
Das Skript wird:
- Die aktuelle SGT-Zeit prüfen, um zu bestimmen, ob es sich um das Fenster für Stempeln zum Arbeitsbeginn oder Arbeitsende handelt
- Supabase verwenden, um Stempelstatus zu verfolgen
- Telegram-Updates für "punch"-Nachrichten abrufen
- Erinnerungen senden, wenn die Stempelung nicht aufgezeichnet wurde

Aktualisieren Sie Ihre `requirements.simple.txt` um:
```
requests
supabase
pytz
```

Hier ist das modifizierte Skript:

```python
import os
import requests
import datetime
import pytz
from supabase import create_client
import argparse

# Umgebungsvariablen laden
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY")
TELEGRAM_CHAT_ID = "610574272"  # Ihre Chat-ID

def send_telegram_message(bot_token, chat_id, message):
    """Sendet eine Nachricht an einen Telegram-Chat mit der Telegram Bot API."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Error sending Telegram message: {response.status_code} - {response.text}")

def send_reminder(action):
    """Sendet eine Stempelzeiterinnerung."""
    message = f"⏰ *Erinnerung:* Bitte stempeln Sie {action.replace('_', ' ')} durch Senden von 'punch' an diesen Bot."
    send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)

def main():
    parser = argparse.ArgumentParser(description="Telegram Punch Reminder Bot")
    parser.add_argument('--job', choices=['punch_reminder', 'send_message'], required=True, help="Job to perform")
    parser.add_argument('--message', type=str, help="Message to send for 'send_message' job")
    args = parser.parse_args()

    if args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "Default test message from your bot!"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"Message sent: {message}")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID are not set.")
        return

    elif args.job == 'punch_reminder':
        # Supabase initialisieren
        supabase = create_client(os.environ['SUPABASE_URL'], os.environ['SUPABASE_KEY'])

        # Aktuelle Zeit in SGT (UTC+8) abrufen
        sgt = pytz.timezone('Asia/Singapore')
        now_utc = datetime.datetime.utcnow()
        now_sgt = now_utc.replace(tzinfo=pytz.utc).astimezone(sgt)
        today_sgt = now_sgt.date()

        # Zeitfenster definieren
        punch_in_start = datetime.time(12, 0)  # 12 Uhr SGT
        punch_in_end = datetime.time(15, 0)    # 15 Uhr SGT
        punch_out_start = datetime.time(18, 0) # 18 Uhr SGT
        punch_out_end = datetime.time(21, 0)   # 21 Uhr SGT

        current_time = now_sgt.time()

        # Aktuelles Fenster bestimmen
        if punch_in_start <= current_time <= punch_in_end:
            window = 'punch_in'
        elif punch_out_start <= current_time <= punch_out_end:
            window = 'punch_out'
        else:
            window = None

        if not window:
            print("Außerhalb der Stempelzeiterinnerungsfenster.")
            return

        # Stempelaufzeichnung für heute abrufen
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # Prüfen, ob bereits gestempelt wurde
        if window == 'punch_in' and punch_record and punch_record['punch_in_time']:
            print("Heute bereits zum Arbeitsbeginn gestempelt.")
            return
        if window == 'punch_out' and punch_record and punch_record['punch_out_time']:
            print("Heute bereits zum Arbeitsende gestempelt.")
            return

        # Letzte verarbeitete Telegram-Update-ID abrufen
        state_response = supabase.table('telegram_state').select('last_update_id').eq('id', 1).execute()
        last_update_id = state_response.data[0]['last_update_id'] if state_response.data else 0

        # Neue Telegram-Updates abrufen
        url = f"https://api.telegram.org/bot{TELEGRAM_LOCATION_BOT_API_KEY}/getUpdates"
        params = {"offset": last_update_id + 1, "timeout": 0}
        response = requests.get(url, params=params)
        updates = response.json().get('result', [])

        max_update_id = last_update_id
        for update in updates:
            if update['update_id'] > max_update_id:
                max_update_id = update['update_id']
            if ('message' in update and 
                update['message'].get('text', '').lower() == 'punch' and 
                str(update['message']['chat']['id']) == TELEGRAM_CHAT_ID):
                # "punch"-Nachricht verarbeiten
                if window == 'punch_in':
                    if not punch_record:
                        supabase.table('punch_records').insert({
                            'date': str(today_sgt),
                            'punch_in_time': now_utc.isoformat()
                        }).execute()
                    else:
                        supabase.table('punch_records').update({
                            'punch_in_time': now_utc.isoformat()
                        }).eq('date', str(today_sgt)).execute()
                elif window == 'punch_out':
                    if not punch_record:
                        supabase.table('punch_records').insert({
                            'date': str(today_sgt),
                            'punch_out_time': now_utc.isoformat()
                        }).execute()
                    else:
                        supabase.table('punch_records').update({
                            'punch_out_time': now_utc.isoformat()
                        }).eq('date', str(today_sgt)).execute()

        # last_update_id aktualisieren
        if max_update_id > last_update_id:
            supabase.table('telegram_state').update({
                'last_update_id': max_update_id
            }).eq('id', 1).execute()

        # Stempelaufzeichnung erneut abrufen, um den neuesten Status zu prüfen
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # Erinnerung senden, wenn Stempelung nicht aufgezeichnet wurde
        if window == 'punch_in' and (not punch_record or not punch_record['punch_in_time']):
            send_reminder('punch_in')
        elif window == 'punch_out' and (not punch_record or not punch_record['punch_out_time']):
            send_reminder('punch_out')

if __name__ == '__main__':
    main()
```

---

### Supabase-Einrichtung
Wir erstellen zwei Tabellen in Supabase, um Stempelstatus und Telegram-Updates zu verwalten.

#### SQL-Anweisungen
Führen Sie diese SQL-Befehle im Supabase SQL-Editor aus:

```sql
-- Tabelle zur Speicherung täglicher Stempelaufzeichnungen
CREATE TABLE punch_records (
    date DATE PRIMARY KEY,
    punch_in_time TIMESTAMP,
    punch_out_time TIMESTAMP
);

-- Tabelle zur Verfolgung des Telegram-Bot-Status
CREATE TABLE telegram_state (
    id INTEGER PRIMARY KEY,
    last_update_id BIGINT NOT NULL DEFAULT 0
);

-- telegram_state mit einer einzelnen Zeile initialisieren
INSERT INTO telegram_state (id, last_update_id) VALUES (1, 0);
```

#### Ausführungsschritte
1. Melden Sie sich in Ihrem Supabase-Dashboard an.
2. Navigieren Sie zum **SQL-Editor**.
3. Fügen Sie den obigen SQL-Code ein und führen Sie ihn aus, um die Tabellen zu erstellen und zu initialisieren.

---

### Umgebungsvariablen
Stellen Sie sicher, dass diese Secrets in Ihrem GitHub-Repository unter **Settings > Secrets and variables > Actions > Secrets** gesetzt sind:
- `TELEGRAM_LOCATION_BOT_API_KEY`: Ihr Telegram-Bot-Token.
- `SUPABASE_URL`: Ihre Supabase-Projekt-URL (z.B. `https://xyz.supabase.co`).
- `SUPABASE_KEY`: Ihr Supabase anon key (zu finden unter **Settings > API**).

---

### Funktionsweise
1. **Zeitplan**: Der Workflow läuft alle 5 Minuten während 12–15 Uhr und 18–21 Uhr SGT (angepasst an UTC) von Mittwoch bis Freitag.
2. **Zeitprüfung**: Das Skript prüft die aktuelle SGT-Zeit, um zu bestimmen, ob es sich im Fenster für Stempeln zum Arbeitsbeginn oder Arbeitsende handelt.
3. **Statusverwaltung**:
   - Prüft `punch_records` auf heutige Stempelungen.
   - Wenn bereits gestempelt wurde (z.B. `punch_in_time` ist während 12–15 Uhr gesetzt), wird keine Erinnerung gesendet.
4. **Telegram-Updates**:
   - Ruft Updates seit der letzten verarbeiteten `update_id` ab.
   - Wenn eine "punch"-Nachricht gefunden wird, aktualisiert es `punch_records` mit der aktuellen Zeit für Stempeln zum Arbeitsbeginn oder Arbeitsende.
   - Aktualisiert `telegram_state` mit der neuesten `update_id`.
5. **Erinnerungen**: Sendet alle 5 Minuten eine Erinnerung, wenn die Stempelung für das aktuelle Fenster nicht aufgezeichnet wurde.

---

### Tests
- **Manueller Auslöser**: Verwenden Sie `workflow_dispatch` mit `job_name: punch_reminder`, um manuell zu testen.
- **Telegram**: Senden Sie "punch" an Ihren Bot während des Fensters, um Erinnerungen für diese Sitzung zu stoppen.
- **Supabase**: Überprüfen Sie die Tabelle `punch_records`, um zu verifizieren, dass Stempelzeiten aufgezeichnet werden.

Dieser Setup ersetzt die standortbasierte Logik durch zeitbasierte Stempelzeiterinnerungen und nutzt Supabase für persistente Statusverwaltung innerhalb der Einschränkungen von GitHub Actions.