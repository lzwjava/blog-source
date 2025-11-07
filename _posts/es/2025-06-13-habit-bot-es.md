---
audio: false
generated: false
image: false
lang: es
layout: post
title: Construyendo un Bot de Hábitos con Mistral
translated: true
type: post
---

En esta publicación de blog, exploramos la creación de un Bot de Hábitos diseñado para enviar recordatorios automatizados utilizando Python y GitHub Actions. Este bot aprovecha la API de Telegram para mensajería y se integra con Mistral AI para generar mensajes contextualmente relevantes. Al programar tareas con GitHub Actions, el bot fomenta hábitos consistentes a través de notificaciones oportunas. Repasaremos la configuración, desde la configuración del entorno hasta la escritura de scripts y la implementación, proporcionando una guía práctica para automatizar tu sistema de seguimiento de hábitos.

## Código

```python
import os
import requests
import argparse
import re
import datetime
from dotenv import load_dotenv
import random

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Variables de entorno
TELEGRAM_HABIT_BOT_API_KEY = os.environ.get("TELEGRAM_HABIT_BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

# Límite de longitud de mensajes en Telegram
TELEGRAM_MAX_LENGTH = 4096

def send_telegram_message(bot_token, chat_id, message):
    """Envía un mensaje a un chat de Telegram usando la API de Telegram Bot."""
    if not bot_token or not chat_id:
        print("Error: TELEGRAM_HABIT_BOT_API_KEY o TELEGRAM_CHAT_ID no están configurados.")
        return False
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # Eliminar asteriscos de Markdown y URLs para garantizar compatibilidad con Telegram
    message_no_stars = message.replace('*', '')
    url_pattern = re.compile(r'(https?://[^\s]+)')
    message_no_links = url_pattern.sub('', message_no_stars)
    # Dividir el mensaje si excede el límite de longitud de Telegram
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
            print(f"Mensaje de Telegram enviado exitosamente ({len(part)} caracteres).")
        except requests.exceptions.RequestException as e:
            print(f"Error al enviar mensaje de Telegram: {e}")
            success = False
    return success


def call_mistral_api(prompt, model="mistral-large-latest"):
    """Llama a la API de Mistral para generar una respuesta."""
    if not MISTRAL_API_KEY:
        print("Error: La variable de entorno MISTRAL_API_KEY no está configurada.")
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
        "temperature": 0.7,  # Ajustar temperatura para creatividad
        "max_tokens": 300  # Limitar longitud de la respuesta
    }
    try:
        print(f"Llamando a la API de Mistral con modelo: {model}")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"Contenido de la API de Mistral: {content}")
            return content
        print(f"Error en la API de Mistral: {e}")
        return None

def generate_copilot_message():
    """Genera un mensaje técnico que fomenta el uso de Copilot mediante la API de Mistral."""
    prompt = (
        f"Genera una oración técnica única y específica para un ingeniero de backend"
        "Selecciona aleatoriamente una tecnología de: Java, Spring Boot, Control-M, IBM WebSphere, Maven, multithreading, Nexus, Windows, JVM, Service-NOW, Python, IA o DevOps, Linux. Algoritmos y Banca "
        "Formato como '¿Atascado con [desafío específico]? ¡Pregúntale a Copilot!' o '¿Problemas con [tarea]? ¡Encuentra ayuda con Copilot!' "
        "Asegura variedad en los desafíos (ej. configuración, depuración, optimización). "
        "Manténlo bajo 300 caracteres, evita Markdown o URLs, y solo muestra la oración."
    )
    message = call_mistral_api(prompt)
    if message:
        return message.strip()[:300]
    return "¿Atascado configurando la fecha de orden en Control-M? ¡Pregúntale a Copilot!"

def main():
    parser = argparse.ArgumentParser(description="Bot de Recordatorios de Hábitos en Telegram")
    parser.add_argument("--job", choices=["send_reminder", "send_message"], required=True, help="Tarea a realizar")
    parser.add_argument("--message", type=str, help="Mensaje a enviar para la tarea 'send_message'")
    args = parser.parse_args()

    if args.job == "send_reminder":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = generate_copilot_message()
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("Error: TELEGRAM_HABIT_BOT_API_KEY o TELEGRAM_CHAT_ID no están configurados.")
    elif args.job == "send_message":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "¡Mensaje de prueba predeterminado del bot!"
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("Error: TELEGRAM_HABIT_BOT_API_KEY o TELEGRAM_CHAT_ID no están configurados.")

if __name__ == "__main__":
    main()
```

## Acción de GitHub

```yaml
name: Hábito

on:
  schedule:
    # Ejecutar cada 10 minutos (0, 10, 20, 30, 40, 50 minutos pasada la hora) de 05:00–13:00 UTC, Lun–Vie
    # 05:00–13:00 UTC = 13:00–21:00 hora de Beijing (UTC+8)
    - cron: '0,10,20,30,40,50 5-13 * * 1-5'

  workflow_dispatch:
    # Permitir activación manual para pruebas
    inputs:
      message:
        description: 'Mensaje personalizado para pruebas (opcional)'
        required: false
        default: 'Mensaje de prueba desde GitHub Actions.'
      job:
        description: 'Tarea a ejecutar (opcional)'
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
      - name: Checkout del repositorio
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Configurar Python 3.13
        uses: actions/setup-python@v4
        with:
          python-version: "3.13"

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Ejecutar script de recordatorio de hábitos (Programado)
        run: python scripts/bot/habit_bot.py --job send_reminder
        if: github.event_name == 'schedule'

      - name: Ejecutar script de recordatorio de hábitos (Activación Manual)
        run: python scripts/bot/habit_bot.py --job ${{ github.event.inputs.job }} --message "${{ github.event.inputs.message }}"
        if: github.event_name == 'workflow_dispatch'

      - name: Notificar en push a la rama main
        run: python scripts/bot/habit_bot.py --job send_message --message "Cambios en el código del bot de hábitos subidos a la rama main."
        if: github.event_name == 'push'
```