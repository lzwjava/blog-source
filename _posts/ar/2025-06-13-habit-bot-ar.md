---
audio: false
generated: false
image: false
lang: ar
layout: post
title: بناء بوت العادات باستخدام ميسترال
translated: true
type: post
---

في هذه المقالة، نستكشف إنشاء بوت العادات المصمم لإرسال تذكيرات آلية باستخدام Python وGitHub Actions. يستفيد هذا البوت من واجهة برمجة تطبيقات Telegram للمراسلة ويتكامل مع Mistral AI لتوليد مطالبات ذات صلة سياقية. من خلال جدولة المهام باستخدام GitHub Actions، يشجع البوت على العادات المتسقة عبر الإشعارات في الوقت المناسب. سنستعرض الإعداد، بدءًا من تكوين البيئة إلى البرمجة والنشر، ونقدم دليلًا عمليًا لأتمتة نظام تتبع العادات الخاص بك.

## الكود

```python
import os
import requests
import argparse
import re
import datetime
from dotenv import load_dotenv
import random

# تحميل المتغيرات البيئية من ملف .env
load_dotenv()

# المتغيرات البيئية
TELEGRAM_HABIT_BOT_API_KEY = os.environ.get("TELEGRAM_HABIT_BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

# الحد الأقصى لطول رسالة Telegram
TELEGRAM_MAX_LENGTH = 4096

def send_telegram_message(bot_token, chat_id, message):
    """يرسل رسالة إلى دردشة Telegram باستخدام واجهة برمجة تطبيقات Telegram Bot."""
    if not bot_token or not chat_id:
        print("خطأ: TELEGRAM_HABIT_BOT_API_KEY أو TELEGRAM_CHAT_ID غير مضبوط.")
        return False
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # إزالة علامات Markdown والروابط لضمان التوافق مع Telegram
    message_no_stars = message.replace('*', '')
    url_pattern = re.compile(r'(https?://[^\s]+)')
    message_no_links = url_pattern.sub('', message_no_stars)
    # تقسيم الرسالة إذا تجاوزت الحد الأقصى لطول Telegram
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
            print(f"تم إرسال جزء من رسالة Telegram بنجاح ({len(part)} حرفًا).")
        except requests.exceptions.RequestException as e:
            print(f"خطأ في إرسال رسالة Telegram: {e}")
            success = False
    return success


def call_mistral_api(prompt, model="mistral-large-latest"):
    """يستدعي واجهة برمجة تطبيقات Mistral لتوليد رد."""
    if not MISTRAL_API_KEY:
        print("خطأ: متغير البيئة MISTRAL_API_KEY غير مضبوط.")
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
        "temperature": 0.7,  # ضبط درجة الحرارة للإبداع
        "max_tokens": 300  # تحديد طول الرد
    }
    try:
        print(f"استدعاء واجهة Mistral API بالنموذج: {model}")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"محتوى Mistral API: {content}")
            return content
        print(f"خطأ في Mistral API: تنسيق رد غير صالح: {response_json}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"خطأ في Mistral API: {e}")
        return None

def generate_copilot_message():
    """يولد جملة مطالبة تقنية تشجع على استخدام Copilot عبر واجهة Mistral API."""
    prompt = (
        f"قم بتوليد جملة مطالبة تقنية فريدة ومحددة لمهندس Backend"
        "اختر عشوائيًا تقنية واحدة من: Java, Spring Boot, Control-M, IBM WebSphere, Maven, multithreading, Nexus, Windows, JVM, Service-NOW, Python, AI أو DevOps, Linux. الخوارزميات والخدمات المصرفية "
        "قم بصياغتها كـ 'هل تواجه مشكلة في [تحدي محدد]؟ اسأل Copilot!' أو 'هل تعاني من [مهمة]؟ ابحث عن Copilot للمساعدة!' "
        "تأكد من تنوع التحديات (مثل التهيئة، تصحيح الأخطاء، التحسين). "
        "احتفظ بها تحت 300 حرف، وتجنب Markdown أو الروابط، وأخرج الجملة فقط."
    )
    message = call_mistral_api(prompt)
    if message:
        return message.strip()[:300]
    return "هل تواجه مشكلة في تهيئة تاريخ طلب Control-M؟ اسأل Copilot!"

def main():
    parser = argparse.ArgumentParser(description="بوت تذكير العادات على Telegram")
    parser.add_argument("--job", choices=["send_reminder", "send_message"], required=True, help="المهمة المطلوبة")
    parser.add_argument("--message", type=str, help="الرسالة المراد إرسالها لمهمة 'send_message'")
    args = parser.parse_args()

    if args.job == "send_reminder":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = generate_copilot_message()
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("خطأ: TELEGRAM_HABIT_BOT_API_KEY أو TELEGRAM_CHAT_ID غير مضبوط.")
    elif args.job == "send_message":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "رسالة اختبار افتراضية من البوت!"
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("خطأ: TELEGRAM_HABIT_BOT_API_KEY أو TELEGRAM_CHAT_ID غير مضبوط.")

if __name__ == "__main__":
    main()
```

## إجراء GitHub

```yaml
name: العادات

on:
  schedule:
    # تشغيل كل 10 دقائق (0, 10, 20, 30, 40, 50 دقيقة بعد الساعة) من 05:00–13:00 UTC، من الاثنين إلى الجمعة
    # 05:00–13:00 UTC = 13:00–21:00 بتوقيت بكين (UTC+8)
    - cron: '0,10,20,30,40,50 5-13 * * 1-5'

  workflow_dispatch:
    # السماح بالتشغيل اليدوي للاختبار
    inputs:
      message:
        description: 'رسالة مخصصة للاختبار (اختياري)'
        required: false
        default: 'رسالة اختبار من GitHub Actions.'
      job:
        description: 'المهمة المطلوبة (اختياري)'
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
      - name: استنساخ المستودع
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: إعداد Python 3.13
        uses: actions/setup-python@v4
        with:
          python-version: "3.13"

      - name: تثبيت التبعيات
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: تشغيل نص تذكير العادات (المجدول)
        run: python scripts/bot/habit_bot.py --job send_reminder
        if: github.event_name == 'schedule'

      - name: تشغيل نص تذكير العادات (تشغيل يدوي)
        run: python scripts/bot/habit_bot.py --job ${{ github.event.inputs.job }} --message "${{ github.event.inputs.message }}"
        if: github.event_name == 'workflow_dispatch'

      - name: إشعار عند الدفع إلى الفرع الرئيسي
        run: python scripts/bot/habit_bot.py --job send_message --message "تم دفع تغييرات الكود لبوت العادات إلى الفرع الرئيسي."
        if: github.event_name == 'push'

```