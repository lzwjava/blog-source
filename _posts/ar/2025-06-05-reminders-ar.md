---
audio: true
generated: false
image: false
lang: ar
layout: post
title: تبسيط التذكيرات عبر Telegram
translated: true
type: post
---

في هذا المشروع، قمت بإعداد نظام تذكير آلي باستخدام GitHub Actions وبوت Telegram للحفاظ على مهامي اليومية والشهرية على المسار الصحيح. من خلال الاستفادة من جداول cron، قمت بتكوين تذكيرات للمهام المتعلقة بالعمل مثل تسجيل الدخول في WeCom، وإرسال جداول الزمن، والتحقق من الرواتب، بالإضافة إلى المهام الشخصية مثل زيارة العائلة، والتسوق على JD.com، وحتى مشاهدة التلفزيون مع شريكي. يستخدم النظام برنامج نصي بلغة Python لإرسال الرسائل عبر واجهة برمجة تطبيقات بوت Telegram، مع تخزين المتغيرات البيئية بأمان في GitHub Secrets. يضمن هذا الإعداد عدم تفويتي لمواعيد نهائية حرجة أو التزامات شخصية، حيث يدمج التكنولوجيا مع الحياة اليومية لتحقيق أقصى قدر من الكفاءة.

```yaml
name: التذكيرات

on:
  schedule:
    # يعمل كل ساعتين من 12 ظهرًا حتى 8 مساءً (بتوقيت بكين، UTC+8) من الأربعاء إلى الجمعة.
    - cron: '0 4,6,8,10,12 * * 3-5'
    # يعمل في الـ27 من كل شهر عند الساعة 12 ظهرًا (بتوقيت بكين، UTC+8).
    - cron: '0 4 27 * *'
    # يعمل في الـ30 من كل شهر عند الساعة 2 مساءً (بتوقيت بكين، UTC+8).
    - cron: '0 6 30 * *'
    # يعمل كل يوم عند الساعة 1 صباحًا بتوقيت بكين (5 مساءً UTC في اليوم السابق).
    - cron: '0 17 * * *'
    # يعمل كل يوم عند الساعة 11 صباحًا بتوقيت بكين (3 صباحًا UTC).
    - cron: '0 3 * * *'
    # يذكر بالذهاب إلى منزل الوالدين في اليوم التالي: 9 مساءً بتوقيت بكين (1 مساءً UTC) يوم الثلاثاء، الأربعاء، الخميس.
    - cron: '0 13 * * 2-4'
    # يذكر بالذهاب إلى المنزل الخاص في اليوم التالي: 9 مساءً بتوقيت بكين (1 مساءً UTC) يوم الأحد، الاثنين، الجمعة، السبت.
    - cron: '0 13 * * 0,1,5,6'
    # يذكر بشراء المنتجات الطازجة مباشرة من المصدر في JD.com: 9 مساءً بتوقيت بكين (1 مساءً UTC) يوم الأربعاء.
    - cron: '0 13 * * 3'
    # يذكر بشراء طعام التوصيل السريع من JD.com: 9 مساءً بتوقيت بكين (1 مساءً UTC) يوم الجمعة.
    - cron: '0 13 * * 5'
    # يذكر بامتحان الدرجة المساعدة في مارس، أبريل، سبتمبر، وأكتوبر كل يوم اثنين عند الساعة 1 مساءً بتوقيت بكين (5 صباحًا UTC).
    - cron: '0 5 * 3,4,9,10 1'
    # يذكر بإرسال جدول الزمن clarity كل يوم جمعة عند الساعة 5 مساءً بتوقيت تايبيه (9 صباحًا UTC).
    - cron: '0 9 * * 5'
    # يذكر بإرسال جدول الزمن للبائع في الـ25 من كل شهر عند الساعة 12 صباحًا بتوقيت تايبيه (4 مساءً UTC في اليوم السابق).
    - cron: '0 16 25 * *'
    # يذكر بطلب دعم العائلة لدفع الرهن العقاري في الـ16 من كل شهر عند الساعة 9 مساءً بتوقيت تايبيه (1 مساءً UTC).
    - cron: '0 13 16 * *'
    # يذكر بمشاهدة التلفزيون مع الشريك كل يوم جمعة، سبت، وأحد عند الساعة 10 مساءً بتوقيت تايبيه (2 مساءً UTC).
    - cron: '0 14 * * 5,6,0'
    # يذكر بإزالة ملصق تصريح وقوف السيارات عند الساعة 2 صباحًا بتوقيت بكين (6 مساءً UTC) يوم الأربعاء، الخميس، الجمعة.
    - cron: '0 18 * * 3,4,5'
  workflow_dispatch:  # يسمح بالتشغيل اليدوي

concurrency:
  group: 'التذكيرات'
  cancel-in-progress: false

jobs:
  إرسال-التذكيرات:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_BOT2_API_KEY: ${{ secrets.TELEGRAM_BOT2_API_KEY }}

    steps:
      - name: التحقق من المستودع
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: إعداد Python 3.10.x
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: تثبيت التبعيات
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: تشغيل البرنامج النصي لـTelegram لتذكير تسجيل الدخول اليومي
        run: python scripts/release/reminders_bot.py --job send_message --message "تسجيل الدخول في WeCom"
        if: github.event.schedule == '0 4,6,8,10,12 * * 3-5'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير الرهن العقاري الشهري
        run: python scripts/release/reminders_bot.py --job send_message --message "تحضير خصم رهن المنزل"
        if: github.event.schedule == '0 4 27 * *'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير التحقق من الراتب الشهري
        run: python scripts/release/reminders_bot.py --job send_message --message "التحقق من الراتب"
        if: github.event.schedule == '0 6 30 * *'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير النوم
        run: python scripts/release/reminders_bot.py --job send_message --message "حان وقت النوم!"
        if: github.event.schedule == '0 17 * * *'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير الاستيقاظ
        run: python scripts/release/reminders_bot.py --job send_message --message "حان وقت الاستيقاظ!"
        if: github.event.schedule == '0 3 * * *'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير منزل الوالدين
        run: python scripts/release/reminders_bot.py --job send_message --message "اذهب إلى منزل الوالدين غدًا!"
        if: github.event.schedule == '0 13 * * 2-4'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير المنزل الخاص
        run: python scripts/release/reminders_bot.py --job send_message --message "اذهب إلى منزلك غدًا!"
        if: github.event.schedule == '0 13 * * 0,1,5,6'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير شراء المنتجات الطازجة من JD.com
        run: python scripts/release/reminders_bot.py --job send_message --message "اشترِ المنتجات الطازجة مباشرة من المصدر في JD.com!"
        if: github.event.schedule == '0 13 * * 3'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير شراء طعام التوصيل السريع من JD.com
        run: python scripts/release/reminders_bot.py --job send_message --message "اشترِ طعام التوصيل السريع من JD.com!"
        if: github.event.schedule == '0 13 * * 5'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير امتحان الدرجة المساعدة
        run: python scripts/release/reminders_bot.py --job send_message --message "سجل لامتحان الدرجة المساعدة"
        if: github.event.schedule == '0 5 * 3,4,9,10 1'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير إرسال جدول الزمن clarity
        run: python scripts/release/reminders_bot.py --job send_message --message "أرسل جدول الزمن clarity"
        if: github.event.schedule == '0 9 * * 5'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير إرسال جدول الزمن للبائع
        run: python scripts/release/reminders_bot.py --job send_message --message "أرسل جدول الزمن للبائع"
        if: github.event.schedule == '0 16 25 * *'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير دعم العائلة للرهن العقاري
        run: python scripts/release/reminders_bot.py --job send_message --message "اطلب من العائلة دعم دفع الرهن العقاري"
        if: github.event.schedule == '0 13 16 * *'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير مشاهدة التلفزيون مع الشريك
        run: python scripts/release/reminders_bot.py --job send_message --message "حان وقت مشاهدة التلفزيون مع شريكك!"
        if: github.event.schedule == '0 14 * * 5,6,0'

      - name: تشغيل البرنامج النصي لـTelegram لتذكير إزالة ملصق تصريح وقوف السيارات
        run: python scripts/release/reminders_bot.py --job send_message --message "أزل ملصق تصريح وقوف السيارات من نافذة السيارة"
        if: github.event.schedule == '0 18 * * 3,4,5'

      - name: تشغيل البرنامج النصي لـTelegram لرسالة الاختبار
        run: python scripts/release/reminders_bot.py --job send_message --message "هذه رسالة اختبار من GitHub Actions."
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
    """يرسل رسالة إلى دردشة Telegram باستخدام واجهة برمجة تطبيقات بوت Telegram."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"خطأ في إرسال رسالة Telegram: {response.status_code} - {response.text}")

def get_chat_id(bot_token):
    """يسترد معرف الدردشة للرسالة الأخيرة المرسلة إلى البوت."""
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
    """يرسل رسالة تذكير إلى Telegram."""
    if TELEGRAM_BOT2_API_KEY and TELEGRAM_CHAT_ID:
        send_telegram_message(TELEGRAM_BOT2_API_KEY, TELEGRAM_CHAT_ID, f"تذكير: {message}")
    else:
        print("TELEGRAM_BOT2_API_KEY و TELEGRAM_CHAT_ID غير مضبوطين.")

def main():
    parser = argparse.ArgumentParser(description="برنامج نصي لبوت Telegram")
    parser.add_argument('--job', choices=['get_chat_id', 'send_message'], required=True, help="المهمة المطلوبة")
    parser.add_argument('--message', help="الرسالة المخصصة للإرسال", default=None)
    args = parser.parse_args()

    if args.job == 'get_chat_id':
        bot_token = TELEGRAM_BOT2_API_KEY
        chat_id = get_chat_id(bot_token)
        if chat_id:
            print(f"معرف الدردشة: {chat_id}")
        else:
            print("تعذر استرداد معرف الدردشة.")

    elif args.job == 'send_message':
        if args.message:
            send_reminder(args.message)
        else:
            print("لم يتم توفير رسالة لمهمة send_message.")
            
if __name__ == '__main__':
    main()
```