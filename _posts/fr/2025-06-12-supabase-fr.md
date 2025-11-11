---
audio: false
generated: true
lang: fr
layout: post
title: Rappels par Cartes Perforées avec Supabase
translated: true
type: note
---

Je vais vous aider à modifier le workflow GitHub Actions existant et le script Python pour implémenter des rappels de pointeuse du mercredi au vendredi, avec des rappels toutes les 5 minutes entre 12h et 15h (pointage d'entrée) et 18h à 21h (pointage de sortie) SGT, qui s'arrêtent lorsqu'un message "punch" est reçu via Telegram. Nous utiliserons Supabase pour suivre les états de pointage afin d'éviter les rappels redondants.

Voici les instructions complètes et le code :

---

### Workflow GitHub Actions
Le workflow doit s'exécuter toutes les 5 minutes pendant les fenêtres horaires spécifiées en SGT (UTC+8) :
- Pointage d'entrée : 12h-15h SGT = 4h-7h UTC
- Pointage de sortie : 18h-21h SGT = 10h-13h UTC
- Jours : Mercredi à vendredi (3-5 dans la syntaxe cron)

Nous utiliserons une seule planification cron combinant ces heures et laisserons le script déterminer l'action.

```yaml
name: Rappels Pointeuse

on:
  schedule:
    # Exécution toutes les 5 minutes de 4h-7h et 10h-13h UTC, mer.-ven.
    # 4h-7h UTC = 12h-15h SGT, 10h-13h UTC = 18h-21h SGT
    - cron: '*/5 4-7,10-13 * * 3-5'

  workflow_dispatch:
    inputs:
      job_name:
        description: 'Job à exécuter (punch_reminder, send_message)'
        required: true
        default: 'punch_reminder'
      message:
        description: 'Message personnalisé pour le job send_message (optionnel)'
        required: false
        default: 'Ceci est un message de test manuel depuis GitHub Actions.'

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
    - name: Checkout du dépôt
      uses: actions/checkout@v4
      with:
        fetch-depth: 5

    - name: Configurer Python 3.13.2
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2"

    - name: Installer les dépendances
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.simple.txt

    - name: Exécuter le script de rappel (Planifié)
      run: python scripts/release/location_bot.py --job punch_reminder
      if: github.event_name == 'schedule'

    - name: Exécuter le script de rappel (Déclenchement Manuel)
      run: python scripts/release/location_bot.py --job punch_reminder
      if: github.event_name == 'workflow_dispatch' && github.event.inputs.job_name == 'punch_reminder'

    - name: Exécuter le script Telegram pour message personnalisé (Déclenchement Manuel)
      run: python scripts/release/location_bot.py --job send_message --message "${{ github.event.inputs.message }}"
      if: github.event_name == 'workflow_dispatch' && github.event.inputs.job_name == 'send_message'

    - name: Notifier en cas de push sur la branche main
      run: python scripts/release/location_bot.py --job send_message --message "Modifications du code pour le bot de rappel de pointeuse poussées sur la branche main."
      if: github.event_name == 'push'
```

---

### Script Python
Le script va :
- Vérifier l'heure SGT actuelle pour déterminer si c'est la fenêtre de pointage d'entrée ou de sortie
- Utiliser Supabase pour suivre les états de pointage
- Récupérer les mises à jour Telegram pour les messages "punch"
- Envoyer des rappels si le pointage n'a pas été enregistré

Mettez à jour votre `requirements.simple.txt` pour inclure :
```
requests
supabase
pytz
```

Voici le script modifié :

```python
import os
import requests
import datetime
import pytz
from supabase import create_client
import argparse

# Charger les variables d'environnement
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY")
TELEGRAM_CHAT_ID = "610574272"  # Votre ID de chat

def send_telegram_message(bot_token, chat_id, message):
    """Envoie un message à un chat Telegram en utilisant l'API Telegram Bot."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Erreur lors de l'envoi du message Telegram : {response.status_code} - {response.text}")

def send_reminder(action):
    """Envoie un message de rappel de pointage."""
    message = f"⏰ *Rappel :* Veuillez pointer {action.replace('_', ' ')} en envoyant 'punch' à ce bot."
    send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)

def main():
    parser = argparse.ArgumentParser(description="Bot Telegram de Rappel de Pointeuse")
    parser.add_argument('--job', choices=['punch_reminder', 'send_message'], required=True, help="Job à effectuer")
    parser.add_argument('--message', type=str, help="Message à envoyer pour le job 'send_message'")
    args = parser.parse_args()

    if args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "Message test par défaut de votre bot !"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"Message envoyé : {message}")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY et TELEGRAM_CHAT_ID ne sont pas définis.")
        return

    elif args.job == 'punch_reminder':
        # Initialiser Supabase
        supabase = create_client(os.environ['SUPABASE_URL'], os.environ['SUPABASE_KEY'])

        # Obtenir l'heure actuelle en SGT (UTC+8)
        sgt = pytz.timezone('Asia/Singapore')
        now_utc = datetime.datetime.utcnow()
        now_sgt = now_utc.replace(tzinfo=pytz.utc).astimezone(sgt)
        today_sgt = now_sgt.date()

        # Définir les fenêtres horaires
        punch_in_start = datetime.time(12, 0)  # 12h SGT
        punch_in_end = datetime.time(15, 0)    # 15h SGT
        punch_out_start = datetime.time(18, 0) # 18h SGT
        punch_out_end = datetime.time(21, 0)   # 21h SGT

        current_time = now_sgt.time()

        # Déterminer la fenêtre actuelle
        if punch_in_start <= current_time <= punch_in_end:
            window = 'punch_in'
        elif punch_out_start <= current_time <= punch_out_end:
            window = 'punch_out'
        else:
            window = None

        if not window:
            print("En dehors des fenêtres de rappel de pointage.")
            return

        # Récupérer l'enregistrement de pointage du jour
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # Vérifier si le pointage est déjà effectué
        if window == 'punch_in' and punch_record and punch_record['punch_in_time']:
            print("Déjà pointé aujourd'hui.")
            return
        if window == 'punch_out' and punch_record and punch_record['punch_out_time']:
            print("Déjà pointé sortie aujourd'hui.")
            return

        # Récupérer le dernier ID de mise à jour Telegram traité
        state_response = supabase.table('telegram_state').select('last_update_id').eq('id', 1).execute()
        last_update_id = state_response.data[0]['last_update_id'] if state_response.data else 0

        # Obtenir les nouvelles mises à jour Telegram
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
                # Traiter le message "punch"
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

        # Mettre à jour last_update_id
        if max_update_id > last_update_id:
            supabase.table('telegram_state').update({
                'last_update_id': max_update_id
            }).eq('id', 1).execute()

        # Re-récupérer l'enregistrement de pointage pour vérifier l'état le plus récent
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # Envoyer un rappel si le pointage n'est pas enregistré
        if window == 'punch_in' and (not punch_record or not punch_record['punch_in_time']):
            send_reminder('punch_in')
        elif window == 'punch_out' and (not punch_record or not punch_record['punch_out_time']):
            send_reminder('punch_out')

if __name__ == '__main__':
    main()
```

---

### Configuration Supabase
Nous allons créer deux tables dans Supabase pour gérer les états de pointage et les mises à jour Telegram.

#### Instructions SQL
Exécutez ces commandes SQL dans l'éditeur SQL de Supabase :

```sql
-- Table pour stocker les enregistrements de pointage quotidiens
CREATE TABLE punch_records (
    date DATE PRIMARY KEY,
    punch_in_time TIMESTAMP,
    punch_out_time TIMESTAMP
);

-- Table pour suivre l'état de Telegram
CREATE TABLE telegram_state (
    id INTEGER PRIMARY KEY,
    last_update_id BIGINT NOT NULL DEFAULT 0
);

-- Initialiser telegram_state avec une seule ligne
INSERT INTO telegram_state (id, last_update_id) VALUES (1, 0);
```

#### Étapes d'exécution
1. Connectez-vous à votre tableau de bord Supabase.
2. Naviguez vers **SQL Editor**.
3. Collez et exécutez le code SQL ci-dessus pour créer et initialiser les tables.

---

### Variables d'Environnement
Assurez-vous que ces secrets sont définis dans votre dépôt GitHub sous **Settings > Secrets and variables > Actions > Secrets** :
- `TELEGRAM_LOCATION_BOT_API_KEY` : Votre jeton de bot Telegram.
- `SUPABASE_URL` : L'URL de votre projet Supabase (ex. `https://xyz.supabase.co`).
- `SUPABASE_KEY` : Votre clé anon Supabase (trouvée dans **Settings > API**).

---

### Fonctionnement
1. **Planification** : Le workflow s'exécute toutes les 5 minutes pendant 12h-15h et 18h-21h SGT (ajusté en UTC) du mercredi au vendredi.
2. **Vérification de l'heure** : Le script vérifie l'heure SGT actuelle pour déterminer si c'est la fenêtre de pointage d'entrée ou de sortie.
3. **Gestion d'état** :
   - Vérifie `punch_records` pour les pointages du jour.
   - Si déjà pointé (ex. `punch_in_time` est défini pendant 12h-15h), aucun rappel n'est envoyé.
4. **Mises à jour Telegram** :
   - Récupère les mises à jour depuis le dernier `update_id` traité.
   - Si un message "punch" est trouvé, met à jour `punch_records` avec l'heure actuelle pour le pointage d'entrée ou de sortie.
   - Met à jour `telegram_state` avec le dernier `update_id`.
5. **Rappels** : Envoie un rappel toutes les 5 minutes si le pointage n'a pas été enregistré pour la fenêtre actuelle.

---

### Tests
- **Déclenchement Manuel** : Utilisez `workflow_dispatch` avec `job_name: punch_reminder` pour tester manuellement.
- **Telegram** : Envoyez "punch" à votre bot pendant la fenêtre pour arrêter les rappels pour cette session.
- **Supabase** : Vérifiez la table `punch_records` pour confirmer que les heures de pointage sont enregistrées.

Cette configuration remplace la logique basée sur la localisation par des rappels de pointage basés sur le temps, en tirant parti de Supabase pour la gestion d'état persistante dans les contraintes de GitHub Actions.