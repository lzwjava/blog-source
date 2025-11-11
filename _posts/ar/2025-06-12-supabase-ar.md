---
audio: false
generated: true
lang: ar
layout: post
title: تذكيرات البطاقة المثقوبة مع سوبابيس
translated: true
type: note
---

سأساعدك في تعديل سير عمل GitHub Actions والنص البرمجي Python الحاليين لتنفيذ تذكيرات البطاقة المثقوبة من الأربعاء إلى الجمعة، مع تذكيرات كل 5 دقائق خلال الساعة 12 ظهرًا إلى 3 مساءً (ثقب الدخول) و 6 مساءً إلى 9 مساءً (ثقب الخروج) بتوقيت سنغافورة (SGT)، مع التوقف عند استلام رسالة "punch" عبر Telegram. سنستخدم Supabase لتتبع حالات الثقب لمنع التذكيرات الزائدة عن الحاجة.

أدناه التعليمات البرمجية الكاملة:

---

### سير عمل GitHub Actions
يحتاج سير العمل إلى التشغيل كل 5 دقائق خلال نوافذ الوقت المحددة في توقيت سنغافورة (UTC+8):
- ثقب الدخول: 12 ظهرًا إلى 3 مساءً بتوقيت سنغافورة = 4 صباحًا إلى 7 صباحًا بالتوقيت العالمي المنسق (UTC)
- ثقب الخروج: 6 مساءً إلى 9 مساءً بتوقيت سنغافورة = 10 صباحًا إلى 1 مساءً بالتوقيت العالمي المنسق (UTC)
- الأيام: الأربعاء إلى الجمعة (3-5 في صيغة cron)

سنستخدم جدول cron واحد يجمع هذه الساعات ونترك للنص البرمجي تحديد الإجراء.

```yaml
name: Punch Card Reminders

on:
  schedule:
    # التشغيل كل 5 دقائق من 4-7 صباحًا و 10 صباحًا-1 مساءً بالتوقيت العالمي المنسق، الأربعاء-الجمعة
    # 4-7 صباحًا بالتوقيت العالمي المنسق = 12 ظهرًا-3 مساءً بتوقيت سنغافورة، 10 صباحًا-1 مساءً بالتوقيت العالمي المنسق = 6 مساءً-9 مساءً بتوقيت سنغافورة
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

### النص البرمجي Python
سيقوم النص البرمجي بما يلي:
- التحقق من وقت توقيت سنغافورة الحالي لتحديد ما إذا كان ضمن نافذة ثقب الدخول أو الخروج
- استخدام Supabase لتتبع حالات الثقب
- جلب تحديثات Telegram لرسائل "punch"
- إرسال تذكيرات إذا لم يتم تسجيل الثقب

قم بتحديث ملف `requirements.simple.txt` ليشمل:
```
requests
supabase
pytz
```

إليك النص البرمجي المعدل:

```python
import os
import requests
import datetime
import pytz
from supabase import create_client
import argparse

# تحميل متغيرات البيئة
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY")
TELEGRAM_CHAT_ID = "610574272"  # معرف الدردشة الخاص بك

def send_telegram_message(bot_token, chat_id, message):
    """يرسل رسالة إلى دردشة Telegram باستخدام Telegram Bot API."""
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
    """يرسل رسالة تذكير بالثقب."""
    message = f"⏰ *Reminder:* Please punch {action.replace('_', ' ')} by sending 'punch' to this bot."
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
        # تهيئة Supabase
        supabase = create_client(os.environ['SUPABASE_URL'], os.environ['SUPABASE_KEY'])

        # الحصول على الوقت الحالي بتوقيت سنغافورة (UTC+8)
        sgt = pytz.timezone('Asia/Singapore')
        now_utc = datetime.datetime.utcnow()
        now_sgt = now_utc.replace(tzinfo=pytz.utc).astimezone(sgt)
        today_sgt = now_sgt.date()

        # تعريف نوافذ الوقت
        punch_in_start = datetime.time(12, 0)  # 12 ظهرًا بتوقيت سنغافورة
        punch_in_end = datetime.time(15, 0)    # 3 مساءً بتوقيت سنغافورة
        punch_out_start = datetime.time(18, 0) # 6 مساءً بتوقيت سنغافورة
        punch_out_end = datetime.time(21, 0)   # 9 مساءً بتوقيت سنغافورة

        current_time = now_sgt.time()

        # تحديد النافذة الحالية
        if punch_in_start <= current_time <= punch_in_end:
            window = 'punch_in'
        elif punch_out_start <= current_time <= punch_out_end:
            window = 'punch_out'
        else:
            window = None

        if not window:
            print("Outside punch reminder windows.")
            return

        # جلب سجل الثقب لليوم
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # التحقق مما إذا كان الثقب قد تم بالفعل
        if window == 'punch_in' and punch_record and punch_record['punch_in_time']:
            print("Already punched in today.")
            return
        if window == 'punch_out' and punch_record and punch_record['punch_out_time']:
            print("Already punched out today.")
            return

        # جلب آخر معرف تحديث تمت معالجته في Telegram
        state_response = supabase.table('telegram_state').select('last_update_id').eq('id', 1).execute()
        last_update_id = state_response.data[0]['last_update_id'] if state_response.data else 0

        # الحصول على تحديثات Telegram الجديدة
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
                # معالجة رسالة "punch"
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

        # تحديث last_update_id
        if max_update_id > last_update_id:
            supabase.table('telegram_state').update({
                'last_update_id': max_update_id
            }).eq('id', 1).execute()

        # إعادة جلب سجل الثقب للتحقق من أحدث حالة
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # إرسال تذكير إذا لم يتم تسجيل الثقب
        if window == 'punch_in' and (not punch_record or not punch_record['punch_in_time']):
            send_reminder('punch_in')
        elif window == 'punch_out' and (not punch_record or not punch_record['punch_out_time']):
            send_reminder('punch_out')

if __name__ == '__main__':
    main()
```

---

### إعداد Supabase
سنقوم بإنشاء جدولين في Supabase لإدارة حالات الثقب وتحديثات Telegram.

#### تعليمات SQL
شغّل أوامر SQL هذه في محرر SQL في Supabase:

```sql
-- جدول لتخزين سجلات الثقب اليومية
CREATE TABLE punch_records (
    date DATE PRIMARY KEY,
    punch_in_time TIMESTAMP,
    punch_out_time TIMESTAMP
);

-- جدول لتخزين حالة Telegram
CREATE TABLE telegram_state (
    id INTEGER PRIMARY KEY,
    last_update_id BIGINT NOT NULL DEFAULT 0
);

-- تهيئة telegram_state بصف واحد
INSERT INTO telegram_state (id, last_update_id) VALUES (1, 0);
```

#### خطوات التنفيذ
1. سجّل الدخول إلى لوحة تحكم Supabase.
2. انتقل إلى **محرر SQL**.
3. الصق وشغّل كود SQL أعلاه لإنشاء وتهيئة الجداول.

---

### متغيرات البيئة
تأكد من تعيين الأسرار التالية في مستودع GitHub الخاص بك تحت **الإعدادات > الأسرار والمتغيرات > الإجراءات > الأسرار**:
- `TELEGRAM_LOCATION_BOT_API_KEY`: رمز بوت Telegram الخاص بك.
- `SUPABASE_URL`: عنوان URL لمشروع Supabase الخاص بك (مثال: `https://xyz.supabase.co`).
- `SUPABASE_KEY`: مفتاح Supabase المجهول الخاص بك (موجود في **الإعدادات > API**).

---

### آلية العمل
1. **الجدولة**: يعمل سير العمل كل 5 دقائق خلال الساعة 12 ظهرًا-3 مساءً و 6 مساءً-9 مساءً بتوقيت سنغافورة (معدلة إلى UTC) من الأربعاء إلى الجمعة.
2. **التحقق من الوقت**: يتحقق النص البرمجي من وقت توقيت سنغافورة الحالي لتحديد ما إذا كان ضمن نافذة ثقب الدخول أو الخروج.
3. **إدارة الحالة**:
   - يتحقق من `punch_records` لثقوب اليوم.
   - إذا تم الثقب بالفعل (مثال: تم تعيين `punch_in_time` خلال 12 ظهرًا-3 مساءً)، لا يتم إرسال تذكير.
4. **تحديثات Telegram**:
   - يجلب التحديثات منذ آخر `update_id` تمت معالجته.
   - إذا تم العثور على رسالة "punch"، يقوم بتحديث `punch_records` بالوقت الحالي لثقب الدخول أو الخروج.
   - يقوم بتحديث `telegram_state` بأحدث `update_id`.
5. **التذكيرات**: يرسل تذكيرًا كل 5 دقائق إذا لم يتم تسجيل الثقب للنافذة الحالية.

---

### الاختبار
- **التشغيل اليدوي**: استخدم `workflow_dispatch` مع `job_name: punch_reminder` للاختبار يدويًا.
- **Telegram**: أرسل "punch" إلى بوتك خلال النافذة لإيقاف التذكيرات لتلك الجلسة.
- **Supabase**: تحقق من جدول `punch_records` للتحقق من تسجيل أوقات الثقب.

هذا الإعداد يستبدل المنطق القائم على الموقع بتذكيرات الثقب القائمة على الوقت، مستفيدًا من Supabase لإدارة الحالة المستمرة ضمن قيود GitHub Actions.