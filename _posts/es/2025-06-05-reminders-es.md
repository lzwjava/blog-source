---
audio: true
generated: false
image: false
lang: es
layout: post
title: Optimiza Recordatorios a través de Telegram
translated: true
type: post
---

En este proyecto, configuré un sistema de recordatorios automatizado utilizando GitHub Actions y un bot de Telegram para mantener mis tareas diarias y mensuales bajo control. Mediante el uso de horarios cron, configuré recordatorios para tareas laborales como fichar en WeCom, enviar hojas de horas y revisar salarios, así como tareas personales como visitar a la familia, comprar en JD.com e incluso ver la televisión con mi pareja. El sistema utiliza un script en Python para enviar mensajes a través de la API de bots de Telegram, con variables de entorno almacenadas de forma segura en GitHub Secrets. Esta configuración garantiza que nunca pierda plazos críticos ni compromisos personales, combinando tecnología con la vida cotidiana para una máxima eficiencia.

```yaml
name: Recordatorios

on:
  schedule:
    # Se ejecuta cada 2 horas desde las 12 PM hasta las 8 PM (hora de Beijing, UTC+8) de miércoles a viernes.
    - cron: '0 4,6,8,10,12 * * 3-5'
    # Se ejecuta el día 27 de cada mes a las 12 PM (hora de Beijing, UTC+8).
    - cron: '0 4 27 * *'
    # Se ejecuta el día 30 de cada mes a las 2 PM (hora de Beijing, UTC+8).
    - cron: '0 6 30 * *'
    # Se ejecuta todos los días a la 1 AM hora de Beijing (5 PM UTC del día anterior).
    - cron: '0 17 * * *'
    # Se ejecuta todos los días a las 11 AM hora de Beijing (3 AM UTC).
    - cron: '0 3 * * *'
    # Recordatorio para ir a casa de los padres al día siguiente: 9 PM hora de Beijing (1 PM UTC) martes, miércoles, jueves.
    - cron: '0 13 * * 2-4'
    # Recordatorio para ir a casa propia al día siguiente: 9 PM hora de Beijing (1 PM UTC) domingo, lunes, viernes, sábado.
    - cron: '0 13 * * 0,1,5,6'
    # Recordatorio para comprar productos frescos directamente en JD.com: 9 PM hora de Beijing (1 PM UTC) miércoles.
    - cron: '0 13 * * 3'
    # Recordatorio para comprar comida de entrega rápida en JD.com: 9 PM hora de Beijing (1 PM UTC) viernes.
    - cron: '0 13 * * 5'
    # Recordatorio para el examen de grado asociado en marzo, abril, septiembre y octubre cada lunes a la 1 PM hora de Beijing (5 AM UTC).
    - cron: '0 5 * 3,4,9,10 1'
    # Recordatorio para enviar la hoja de horas semanal cada viernes a las 5 PM hora de Taipei (9 AM UTC).
    - cron: '0 9 * * 5'
    # Recordatorio para enviar la hoja de horas del proveedor el día 25 de cada mes a las 12 AM hora de Taipei (4 PM UTC del día anterior).
    - cron: '0 16 25 * *'
    # Recordatorio para pedir a la familia que apoye el pago de la hipoteca el día 16 de cada mes a las 9 PM hora de Taipei (1 PM UTC).
    - cron: '0 13 16 * *'
    # Recordatorio para ver la televisión con la pareja cada viernes, sábado y domingo a las 10 PM hora de Taipei (2 PM UTC).
    - cron: '0 14 * * 5,6,0'
    # Recordatorio para quitar la pegatina del permiso de estacionamiento a las 2 AM hora de Beijing (6 PM UTC) miércoles, jueves, viernes.
    - cron: '0 18 * * 3,4,5'
  workflow_dispatch:  # Permite activación manual

concurrency:
  group: 'recordatorios'
  cancel-in-progress: false

jobs:
  enviar-recordatorios:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_BOT2_API_KEY: ${{ secrets.TELEGRAM_BOT2_API_KEY }}

    steps:
      - name: Verificar repositorio
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Configurar Python 3.10.x
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: Ejecutar script de Telegram para recordatorios de fichar diario
        run: python scripts/release/reminders_bot.py --job send_message --message "Fichar en WeCom"
        if: github.event.schedule == '0 4,6,8,10,12 * * 3-5'

      - name: Ejecutar script de Telegram para recordatorio mensual de hipoteca
        run: python scripts/release/reminders_bot.py --job send_message --message "Preparar deducción de hipoteca"
        if: github.event.schedule == '0 4 27 * *'

      - name: Ejecutar script de Telegram para recordatorio mensual de revisar salario
        run: python scripts/release/reminders_bot.py --job send_message --message "Revisar salario"
        if: github.event.schedule == '0 6 30 * *'

      - name: Ejecutar script de Telegram para recordatorio de dormir
        run: python scripts/release/reminders_bot.py --job send_message --message "¡Hora de dormir!"
        if: github.event.schedule == '0 17 * * *'

      - name: Ejecutar script de Telegram para recordatorio de despertar
        run: python scripts/release/reminders_bot.py --job send_message --message "¡Hora de despertar!"
        if: github.event.schedule == '0 3 * * *'

      - name: Ejecutar script de Telegram para recordatorio de casa de los padres
        run: python scripts/release/reminders_bot.py --job send_message --message "¡Ve a casa de tus padres mañana!"
        if: github.event.schedule == '0 13 * * 2-4'

      - name: Ejecutar script de Telegram para recordatorio de casa propia
        run: python scripts/release/reminders_bot.py --job send_message --message "¡Ve a tu casa mañana!"
        if: github.event.schedule == '0 13 * * 0,1,5,6'

      - name: Ejecutar script de Telegram para recordatorio de comprar productos frescos en JD.com
        run: python scripts/release/reminders_bot.py --job send_message --message "¡Compra productos frescos directamente en JD.com!"
        if: github.event.schedule == '0 13 * * 3'

      - name: Ejecutar script de Telegram para recordatorio de comida rápida en JD.com
        run: python scripts/release/reminders_bot.py --job send_message --message "¡Compra comida de entrega rápida en JD.com!"
        if: github.event.schedule == '0 13 * * 5'

      - name: Ejecutar script de Telegram para recordatorio de examen de grado asociado
        run: python scripts/release/reminders_bot.py --job send_message --message "Registrar examen de grado asociado"
        if: github.event.schedule == '0 5 * 3,4,9,10 1'

      - name: Ejecutar script de Telegram para recordatorio de hoja de horas semanal
        run: python scripts/release/reminders_bot.py --job send_message --message "Enviar hoja de horas semanal"
        if: github.event.schedule == '0 9 * * 5'

      - name: Ejecutar script de Telegram para recordatorio de hoja de horas del proveedor
        run: python scripts/release/reminders_bot.py --job send_message --message "Enviar hoja de horas del proveedor"
        if: github.event.schedule == '0 16 25 * *'

      - name: Ejecutar script de Telegram para recordatorio de apoyo familiar en hipoteca
        run: python scripts/release/reminders_bot.py --job send_message --message "Pedir a la familia que apoye el pago de la hipoteca"
        if: github.event.schedule == '0 13 16 * *'

      - name: Ejecutar script de Telegram para recordatorio de ver TV con la pareja
        run: python scripts/release/reminders_bot.py --job send_message --message "¡Hora de ver la televisión con tu pareja!"
        if: github.event.schedule == '0 14 * * 5,6,0'

      - name: Ejecutar script de Telegram para recordatorio de quitar pegatina de estacionamiento
        run: python scripts/release/reminders_bot.py --job send_message --message "Quitar la pegatina del permiso de estacionamiento del coche"
        if: github.event.schedule == '0 18 * * 3,4,5'

      - name: Ejecutar script de Telegram para mensaje de prueba
        run: python scripts/release/reminders_bot.py --job send_message --message "Este es un mensaje de prueba desde GitHub Actions."
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
    """Envía un mensaje a un chat de Telegram usando la API de bots de Telegram."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Error al enviar mensaje de Telegram: {response.status_code} - {response.text}")

def get_chat_id(bot_token):
    """Obtiene el ID del chat del último mensaje enviado al bot."""
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
    """Envía un mensaje de recordatorio a Telegram."""
    if TELEGRAM_BOT2_API_KEY and TELEGRAM_CHAT_ID:
        send_telegram_message(TELEGRAM_BOT2_API_KEY, TELEGRAM_CHAT_ID, f"Recordatorio: {message}")
    else:
        print("TELEGRAM_BOT2_API_KEY y TELEGRAM_CHAT_ID no están configurados.")

def main():
    parser = argparse.ArgumentParser(description="Script de Bot de Telegram")
    parser.add_argument('--job', choices=['get_chat_id', 'send_message'], required=True, help="Tarea a realizar")
    parser.add_argument('--message', help="Mensaje personalizado para enviar", default=None)
    args = parser.parse_args()

    if args.job == 'get_chat_id':
        bot_token = TELEGRAM_BOT2_API_KEY
        chat_id = get_chat_id(bot_token)
        if chat_id:
            print(f"ID del chat: {chat_id}")
        else:
            print("No se pudo obtener el ID del chat.")

    elif args.job == 'send_message':
        if args.message:
            send_reminder(args.message)
        else:
            print("No se proporcionó mensaje para la tarea send_message.")
            
if __name__ == '__main__':
    main()
```