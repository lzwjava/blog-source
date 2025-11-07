---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Construire un Bot d'Habitudes avec Mistral
translated: true
type: post
---

Dans cet article de blog, nous explorons la création d'un Habit Bot conçu pour envoyer des rappels automatisés en utilisant Python et GitHub Actions. Ce bot utilise l'API Telegram pour la messagerie et s'intègre à Mistral AI pour générer des invites contextuellement pertinentes. En planifiant des tâches avec GitHub Actions, le bot encourage des habitudes régulières grâce à des notifications opportunes. Nous détaillerons la configuration, de la mise en place de l'environnement au script et au déploiement, offrant ainsi un guide pratique pour automatiser votre système de suivi des habitudes.

## Code

```python
import os
import requests
import argparse
import re
import datetime
from dotenv import load_dotenv
import random

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Variables d'environnement
TELEGRAM_HABIT_BOT_API_KEY = os.environ.get("TELEGRAM_HABIT_BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

# Limite de longueur des messages Telegram
TELEGRAM_MAX_LENGTH = 4096

def send_telegram_message(bot_token, chat_id, message):
    """Envoie un message à un chat Telegram en utilisant l'API Telegram Bot."""
    if not bot_token or not chat_id:
        print("Erreur : TELEGRAM_HABIT_BOT_API_KEY ou TELEGRAM_CHAT_ID non définis.")
        return False
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # Supprimer les astérisques Markdown et les URL pour assurer la compatibilité avec Telegram
    message_no_stars = message.replace('*', '')
    url_pattern = re.compile(r'(https?://[^\s]+)')
    message_no_links = url_pattern.sub('', message_no_stars)
    # Diviser le message s'il dépasse la limite de longueur de Telegram
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
            print(f"Message Telegram envoyé avec succès ({len(part)} caractères).")
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de l'envoi du message Telegram : {e}")
            success = False
    return success


def call_mistral_api(prompt, model="mistral-large-latest"):
    """Appelle l'API Mistral pour générer une réponse."""
    if not MISTRAL_API_KEY:
        print("Erreur : la variable d'environnement MISTRAL_API_KEY n'est pas définie.")
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
        "temperature": 0.7,  # Ajuster la température pour la créativité
        "max_tokens": 300  # Limiter la longueur de la réponse
    }
    try:
        print(f"Appel de l'API Mistral avec le modèle : {model}")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"Contenu de l'API Mistral : {content}")
            return content
        print(f"Erreur de l'API Mistral : format de réponse invalide : {response_json}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur de l'API Mistral : {e}")
        return None

def generate_copilot_message():
    """Génère une phrase d'invite technique encourageant l'utilisation de Copilot via l'API Mistral."""
    prompt = (
        f"Génère une phrase d'invite technique unique et spécifique pour un ingénieur backend"
        "Sélectionne aléatoirement une technologie parmi : Java, Spring Boot, Control-M, IBM WebSphere, Maven, multithreading, Nexus, Windows, JVM, Service-NOW, Python, IA ou DevOps, Linux. Algorithmes et Banque "
        "Formate comme 'Bloqué sur [défi spécifique] ? Demande à Copilot !' ou 'En difficulté avec [tâche] ? Trouve Copilot pour t'aider !' "
        "Assure une variété dans les défis (par exemple, configuration, débogage, optimisation). "
        "Garde-la sous 300 caractères, évite Markdown ou les URL, et ne renvoie que la phrase."
    )
    message = call_mistral_api(prompt)
    if message:
        return message.strip()[:300]
    return "Bloqué sur la configuration de la date de commande Control-M ? Demande à Copilot !"

def main():
    parser = argparse.ArgumentParser(description="Bot de rappel d'habitudes Telegram")
    parser.add_argument("--job", choices=["send_reminder", "send_message"], required=True, help="Tâche à effectuer")
    parser.add_argument("--message", type=str, help="Message à envoyer pour la tâche 'send_message'")
    args = parser.parse_args()

    if args.job == "send_reminder":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = generate_copilot_message()
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("Erreur : TELEGRAM_HABIT_BOT_API_KEY ou TELEGRAM_CHAT_ID non définis.")
    elif args.job == "send_message":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "Message de test par défaut du bot !"
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("Erreur : TELEGRAM_HABIT_BOT_API_KEY ou TELEGRAM_CHAT_ID non définis.")

if __name__ == "__main__":
    main()
```

## Action GitHub

```yaml
name: Habitude

on:
  schedule:
    # Exécution toutes les 10 minutes (0, 10, 20, 30, 40, 50 minutes après l'heure) de 05:00 à 13:00 UTC, du lundi au vendredi
    # 05:00–13:00 UTC = 13:00–21:00 heure de Pékin (UTC+8)
    - cron: '0,10,20,30,40,50 5-13 * * 1-5'

  workflow_dispatch:
    # Permet un déclenchement manuel pour les tests
    inputs:
      message:
        description: 'Message personnalisé pour les tests (facultatif)'
        required: false
        default: 'Message de test depuis GitHub Actions.'
      job:
        description: 'Tâche à exécuter (facultatif)'
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
      - name: Vérifier le dépôt
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Configurer Python 3.13
        uses: actions/setup-python@v4
        with:
          python-version: "3.13"

      - name: Installer les dépendances
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Exécuter le script de rappel d'habitude (Planifié)
        run: python scripts/bot/habit_bot.py --job send_reminder
        if: github.event_name == 'schedule'

      - name: Exécuter le script de rappel d'habitude (Déclenchement manuel)
        run: python scripts/bot/habit_bot.py --job ${{ github.event.inputs.job }} --message "${{ github.event.inputs.message }}"
        if: github.event_name == 'workflow_dispatch'

      - name: Notifier en cas de push sur la branche main
        run: python scripts/bot/habit_bot.py --job send_message --message "Modifications du code pour le bot d'habitude poussées sur la branche main."
        if: github.event_name == 'push'

```