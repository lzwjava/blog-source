---
audio: false
generated: true
lang: es
layout: post
title: Recordatorios De Tarjeta Perforada Con Supabase
translated: true
type: note
---

Te ayudo a modificar el flujo de trabajo de GitHub Actions y el script de Python existentes para implementar recordatorios de tarjeta de horario de miércoles a viernes, con recordatorios cada 5 minutos durante 12 PM a 3 PM (entrada) y 6 PM a 9 PM (salida) SGT, deteniéndose cuando se reciba un mensaje de "punch" a través de Telegram. Usaremos Supabase para rastrear los estados de los punches y evitar recordatorios redundantes.

A continuación están las instrucciones y código completos:

---

### Flujo de trabajo de GitHub Actions
El flujo de trabajo debe ejecutarse cada 5 minutos durante las ventanas de tiempo especificadas en SGT (UTC+8):
- Entrada: 12 PM a 3 PM SGT = 4 AM a 7 AM UTC
- Salida: 6 PM a 9 PM SGT = 10 AM a 1 PM UTC
- Días: Miércoles a Viernes (3-5 en sintaxis cron)

Usaremos un único programa cron que combine estas horas y dejaremos que el script determine la acción.

```yaml
name: Recordatorios de Tarjeta de Horario

on:
  schedule:
    # Ejecutar cada 5 minutos desde 4-7 AM y 10 AM-1 PM UTC, Mié-Vie
    # 4-7 AM UTC = 12 PM-3 PM SGT, 10 AM-1 PM UTC = 6 PM-9 PM SGT
    - cron: '*/5 4-7,10-13 * * 3-5'

  workflow_dispatch:
    inputs:
      job_name:
        description: 'Trabajo a ejecutar (punch_reminder, send_message)'
        required: true
        default: 'punch_reminder'
      message:
        description: 'Mensaje personalizado para el trabajo send_message (opcional)'
        required: false
        default: 'Este es un mensaje de prueba de activación manual desde GitHub Actions.'

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

### Script de Python
El script:
- Verificará la hora actual en SGT para determinar si está en la ventana de entrada o salida
- Usará Supabase para rastrear los estados de los punches
- Obtendrá las actualizaciones de Telegram para mensajes de "punch"
- Enviará recordatorios si el punch no ha sido registrado

Actualiza tu `requirements.simple.txt` para incluir:
```
requests
supabase
pytz
```

Aquí está el script modificado:

```python
import os
import requests
import datetime
import pytz
from supabase import create_client
import argparse

# Cargar variables de entorno
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY")
TELEGRAM_CHAT_ID = "610574272"  # Tu ID de chat

def send_telegram_message(bot_token, chat_id, message):
    """Envía un mensaje a un chat de Telegram usando la Telegram Bot API."""
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
    """Envía un mensaje de recordatorio de punch."""
    message = f"⏰ *Recordatorio:* Por favor registra tu {action.replace('_', ' ')} enviando 'punch' a este bot."
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
        # Inicializar Supabase
        supabase = create_client(os.environ['SUPABASE_URL'], os.environ['SUPABASE_KEY'])

        # Obtener hora actual en SGT (UTC+8)
        sgt = pytz.timezone('Asia/Singapore')
        now_utc = datetime.datetime.utcnow()
        now_sgt = now_utc.replace(tzinfo=pytz.utc).astimezone(sgt)
        today_sgt = now_sgt.date()

        # Definir ventanas de tiempo
        punch_in_start = datetime.time(12, 0)  # 12 PM SGT
        punch_in_end = datetime.time(15, 0)    # 3 PM SGT
        punch_out_start = datetime.time(18, 0) # 6 PM SGT
        punch_out_end = datetime.time(21, 0)   # 9 PM SGT

        current_time = now_sgt.time()

        # Determinar ventana actual
        if punch_in_start <= current_time <= punch_in_end:
            window = 'punch_in'
        elif punch_out_start <= current_time <= punch_out_end:
            window = 'punch_out'
        else:
            window = None

        if not window:
            print("Outside punch reminder windows.")
            return

        # Obtener registro de punch de hoy
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # Verificar si el punch ya se realizó
        if window == 'punch_in' and punch_record and punch_record['punch_in_time']:
            print("Already punched in today.")
            return
        if window == 'punch_out' and punch_record and punch_record['punch_out_time']:
            print("Already punched out today.")
            return

        # Obtener último ID de actualización de Telegram procesado
        state_response = supabase.table('telegram_state').select('last_update_id').eq('id', 1).execute()
        last_update_id = state_response.data[0]['last_update_id'] if state_response.data else 0

        # Obtener nuevas actualizaciones de Telegram
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
                # Procesar mensaje "punch"
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

        # Actualizar last_update_id
        if max_update_id > last_update_id:
            supabase.table('telegram_state').update({
                'last_update_id': max_update_id
            }).eq('id', 1).execute()

        # Volver a obtener el registro de punch para verificar el estado más reciente
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # Enviar recordatorio si el punch no está registrado
        if window == 'punch_in' and (not punch_record or not punch_record['punch_in_time']):
            send_reminder('punch_in')
        elif window == 'punch_out' and (not punch_record or not punch_record['punch_out_time']):
            send_reminder('punch_out')

if __name__ == '__main__':
    main()
```

---

### Configuración de Supabase
Crearemos dos tablas en Supabase para gestionar los estados de los punches y las actualizaciones de Telegram.

#### Instrucciones SQL
Ejecuta estos comandos SQL en el Editor SQL de Supabase:

```sql
-- Tabla para almacenar registros diarios de punches
CREATE TABLE punch_records (
    date DATE PRIMARY KEY,
    punch_in_time TIMESTAMP,
    punch_out_time TIMESTAMP
);

-- Tabla para gestionar el estado de Telegram
CREATE TABLE telegram_state (
    id INTEGER PRIMARY KEY,
    last_update_id BIGINT NOT NULL DEFAULT 0
);

-- Inicializar telegram_state con una sola fila
INSERT INTO telegram_state (id, last_update_id) VALUES (1, 0);
```

#### Pasos para ejecutar
1. Inicia sesión en tu panel de control de Supabase.
2. Navega a **SQL Editor**.
3. Pega y ejecuta el código SQL anterior para crear e inicializar las tablas.

---

### Variables de entorno
Asegúrate de que estos secrets estén configurados en tu repositorio de GitHub bajo **Settings > Secrets and variables > Actions > Secrets**:
- `TELEGRAM_LOCATION_BOT_API_KEY`: Tu token del bot de Telegram.
- `SUPABASE_URL`: La URL de tu proyecto de Supabase (ej. `https://xyz.supabase.co`).
- `SUPABASE_KEY`: Tu anon key de Supabase (encontrada en **Settings > API**).

---

### Cómo funciona
1. **Programación**: El flujo de trabajo se ejecuta cada 5 minutos durante 12 PM-3 PM y 6 PM-9 PM SGT (ajustado a UTC) de miércoles a viernes.
2. **Verificación de hora**: El script verifica la hora actual en SGT para determinar si está en la ventana de entrada o salida.
3. **Gestión de estado**:
   - Verifica `punch_records` para los punches de hoy.
   - Si ya se registró el punch (ej. `punch_in_time` está establecido durante 12 PM-3 PM), no se envía recordatorio.
4. **Actualizaciones de Telegram**:
   - Obtiene actualizaciones desde el último `update_id` procesado.
   - Si se encuentra un mensaje "punch", actualiza `punch_records` con la hora actual para entrada o salida.
   - Actualiza `telegram_state` con el último `update_id`.
5. **Recordatorios**: Envía un recordatorio cada 5 minutos si el punch no ha sido registrado para la ventana actual.

---

### Pruebas
- **Activación manual**: Usa `workflow_dispatch` con `job_name: punch_reminder` para probar manualmente.
- **Telegram**: Envía "punch" a tu bot durante la ventana para detener los recordatorios de esa sesión.
- **Supabase**: Verifica la tabla `punch_records` para confirmar que los tiempos de punch estén registrados.

Esta configuración reemplaza la lógica basada en ubicación con recordatorios de punch basados en tiempo, aprovechando Supabase para la gestión de estado persistente dentro de las limitaciones de GitHub Actions.